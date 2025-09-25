import os
import re
import json 
import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime

# 定义记忆文件的名称
MEMORY_FILE = "time_memory.json"

# 尝试导入sv_ttk主题，如果失败则使用默认主题
try:
    import sv_ttk
    THEME_ENABLED = True
except ImportError:
    THEME_ENABLED = False

class TimeInputDialog(tk.Toplevel):
    def __init__(self, parent, initial_datetime=None):
        super().__init__(parent)
        self.transient(parent)
        self.title("设定时间")
        self.parent = parent
        self.result = None
        initial_day = ""
        initial_seq = "1"
        if initial_datetime:
            initial_day = str(initial_datetime.day)
            initial_seq = str((initial_datetime.hour - 9) * 60 + initial_datetime.minute + 1)
        body = ttk.Frame(self, padding="15")
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)
        body.grid(sticky="nsew")
        ttk.Label(body, text="日期 (9月):").grid(row=0, column=0, padx=5, pady=5, sticky="w")
        self.day_var = tk.StringVar(value=initial_day)
        self.day_selector = ttk.Combobox(body, textvariable=self.day_var, values=[str(i) for i in range(1, 31)], width=10, state="readonly")
        self.day_selector.grid(row=0, column=1, padx=5, pady=5)
        ttk.Label(body, text="当天顺序:").grid(row=1, column=0, padx=5, pady=5, sticky="w")
        self.sequence_var = tk.StringVar(value=initial_seq)
        self.sequence_entry = ttk.Entry(body, textvariable=self.sequence_var, width=12)
        self.sequence_entry.grid(row=1, column=1, padx=5, pady=5)
        self.sequence_entry.focus_set()
        self.sequence_entry.select_range(0, 'end')
        button_frame = ttk.Frame(body, padding=(0, 10, 0, 0))
        button_frame.grid(row=2, column=0, columnspan=2)
        ok_button = ttk.Button(button_frame, text="确定", command=self.on_ok, style="Accent.TButton")
        ok_button.pack(side="left", padx=5)
        cancel_button = ttk.Button(button_frame, text="取消", command=self.destroy)
        cancel_button.pack(side="left", padx=5)
        self.bind("<Return>", self.on_ok)
        self.bind("<Escape>", lambda e: self.destroy())
        self.protocol("WM_DELETE_WINDOW", self.destroy)
        self.geometry(f"+{parent.winfo_rootx()+150}+{parent.winfo_rooty()+150}")
        self.grab_set()
        self.wait_window(self)
    def on_ok(self, event=None):
        try:
            day = int(self.day_var.get())
            sequence = int(self.sequence_var.get())
            if not (1 <= sequence): raise ValueError
            self.result = (day, sequence)
            self.destroy()
        except (ValueError, TypeError):
            messagebox.showerror("输入错误", "日期和当天顺序必须是有效的正整数。", parent=self)

class MarkdownModifierApp:
    def __init__(self, root):
        self.root = root
        self.root.title("新芽专题批量修改器 v3.2 (带记忆功能)")
        self.root.geometry("1100x700")
        if THEME_ENABLED: sv_ttk.set_theme("dark")
        self.files_data = []
        self._create_widgets()
        self.scan_and_load_files()

    def _load_time_memory(self):
        if not os.path.exists(MEMORY_FILE):
            return {}
        try:
            with open(MEMORY_FILE, 'r', encoding='utf-8') as f:
                return json.load(f)
        except (json.JSONDecodeError, IOError) as e:
            print(f"读取记忆文件失败: {e}")
            return {}

    def _save_time_memory(self):
        memory_data = {}
        for item in self.files_data:
            if item.get('new_time'):
                memory_data[item['path']] = item['new_time'].isoformat()
        try:
            with open(MEMORY_FILE, 'w', encoding='utf-8') as f:
                json.dump(memory_data, f, indent=4)
        except IOError as e:
            print(f"保存记忆文件失败: {e}")

    def _create_widgets(self):
        main_frame = ttk.Frame(self.root, padding="10")
        main_frame.pack(fill=tk.BOTH, expand=True)
        controls_frame = ttk.LabelFrame(main_frame, text="操作控制", padding="10")
        controls_frame.pack(fill=tk.X, pady=(0, 10))
        controls_frame.grid_columnconfigure(1, weight=1)
        time_frame = ttk.LabelFrame(controls_frame, text="批量时间设定 (选中文件后操作)", padding="10")
        time_frame.grid(row=0, column=0, padx=(0, 20), sticky="w")
        ttk.Label(time_frame, text="日期 (9月):").grid(row=0, column=0, padx=(0, 5), sticky="w")
        self.day_var = tk.StringVar()
        self.day_selector = ttk.Combobox(time_frame, textvariable=self.day_var, values=[str(i) for i in range(1, 31)], width=5, state="readonly")
        self.day_selector.grid(row=0, column=1, padx=(0, 10))
        ttk.Label(time_frame, text="当天顺序:").grid(row=0, column=2, padx=(0, 5), sticky="w")
        self.sequence_var = tk.StringVar(value="1")
        self.sequence_entry = ttk.Entry(time_frame, textvariable=self.sequence_var, width=5)
        self.sequence_entry.grid(row=0, column=3, padx=(0, 10))
        self.set_time_button = ttk.Button(time_frame, text="批量设定", command=self.set_time_for_selected)
        self.set_time_button.grid(row=0, column=4)
        action_frame = ttk.Frame(controls_frame)
        action_frame.grid(row=0, column=2, sticky="e")
        self.sort_button = ttk.Button(action_frame, text="📅 按时间排序", command=self.sort_and_redisplay, style="Accent.TButton")
        self.sort_button.pack(side=tk.LEFT, padx=(0, 10))
        self.refresh_button = ttk.Button(action_frame, text="🔄 刷新列表", command=self.scan_and_load_files)
        self.refresh_button.pack(side=tk.LEFT, padx=(0, 10))
        self.apply_button = ttk.Button(action_frame, text="💾 应用新序号", command=self.handle_apply, state="disabled")
        self.apply_button.pack(side=tk.LEFT, padx=(0, 10))
        tree_frame = ttk.Frame(main_frame)
        tree_frame.pack(fill=tk.BOTH, expand=True)
        columns = ("Title", "OldNum", "SetTime", "NewNum")
        self.tree = ttk.Treeview(tree_frame, columns=columns, show="headings")
        self.tree.heading("Title", text="文章标题")
        self.tree.heading("OldNum", text="原序号")
        self.tree.heading("SetTime", text="设定时间 (双击修改)")
        self.tree.heading("NewNum", text="新序号 (预览)")
        self.tree.column("Title", width=450); self.tree.column("OldNum", width=80, anchor="center"); self.tree.column("SetTime", width=180, anchor="center"); self.tree.column("NewNum", width=120, anchor="center")
        self.tree.bind("<Double-1>", self._on_tree_double_click)
        vsb = ttk.Scrollbar(tree_frame, orient="vertical", command=self.tree.yview); hsb = ttk.Scrollbar(tree_frame, orient="horizontal", command=self.tree.xview)
        self.tree.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)
        vsb.pack(side="right", fill="y"); hsb.pack(side="bottom", fill="x"); self.tree.pack(side="left", fill="both", expand=True)
        self.tree.tag_configure("time_set", foreground="#57a9ff"); self.tree.tag_configure("not_set", foreground="#a0a0a0"); self.tree.tag_configure("separator", foreground="#555555")
        self.status_var = tk.StringVar(value="准备就绪。")
        status_bar = ttk.Label(main_frame, textvariable=self.status_var, anchor="w"); status_bar.pack(fill=tk.X, side=tk.BOTTOM, pady=(10, 0))

    def scan_and_load_files(self):
        self.tree.delete(*self.tree.get_children())
        self.apply_button.config(state="disabled")
        title_pattern = re.compile(r"title: (新芽专题介绍（(\d+)）.*)")
        temp_files = []
        for filename in os.listdir('.'):
            if filename.endswith('.md'):
                try:
                    with open(filename, 'r', encoding='utf-8') as f: content_head = f.readlines(500)
                    title_line_content = ""
                    for line in content_head:
                        if line.startswith("title:"): title_line_content = line; break
                    match = title_pattern.search(title_line_content)
                    if match:
                        full_title = match.group(1).strip()
                        num = int(match.group(2))
                        file_info = {"path": filename, "num": num, "title": full_title, "new_time": None}
                        temp_files.append(file_info)
                except Exception as e:
                    print(f"处理 {filename} 出错: {e}")
        self.files_data = sorted(temp_files, key=lambda item: item['num'])
        time_memory = self._load_time_memory()
        if time_memory:
            for item in self.files_data:
                if item['path'] in time_memory:
                    try: item['new_time'] = datetime.fromisoformat(time_memory[item['path']])
                    except ValueError: print(f"无法解析记忆中的时间格式: {time_memory[item['path']]}")
            self.status_var.set(f"已加载 {len(time_memory)} 条时间记忆。正在为您自动排序...")
            self.sort_and_redisplay(is_initial_load=True)
        else:
            self._redisplay_tree()
            self.status_var.set(f"刷新完成，找到 {len(self.files_data)} 个文件。未找到时间记忆。")

    def _set_time_for_item(self, iid, day, sequence):
        file_info = self._get_file_info_by_path(iid)
        if not file_info: return
        hour = 9 + (sequence - 1) // 60; minute = (sequence - 1) % 60
        new_dt = datetime(datetime.now().year, 9, day, hour, minute)
        file_info['new_time'] = new_dt
        time_str = new_dt.strftime('%Y-%m-%d %H:%M')
        self.tree.item(iid, values=(file_info["title"], file_info["num"], time_str, self.tree.item(iid, 'values')[3]), tags=("time_set",))
        self._save_time_memory()

    def sort_and_redisplay(self, is_initial_load=False):
        with_time = [item for item in self.files_data if item['new_time'] is not None]
        if not with_time:
            if not is_initial_load: messagebox.showinfo("提示", "没有文件设定了时间，无法排序。")
            return
        without_time = [item for item in self.files_data if item['new_time'] is None]
        with_time.sort(key=lambda item: item['new_time'])
        self.files_data = with_time + without_time
        self._redisplay_tree(show_new_num=True)
        self.apply_button.config(state="normal")
        if not is_initial_load: self.status_var.set("排序完成！“新序号”已更新为预览效果。")

    def _on_tree_double_click(self, event):
        region = self.tree.identify("region", event.x, event.y)
        if region != "cell": return
        column_id = self.tree.identify_column(event.x)
        if column_id == "#3":
            iid = self.tree.identify_row(event.y)
            if not iid: return
            file_info = self._get_file_info_by_path(iid)
            if not file_info: return
            dialog = TimeInputDialog(self.root, initial_datetime=file_info.get('new_time'))
            if dialog.result:
                day, sequence = dialog.result
                self._set_time_for_item(iid, day, sequence)
                self.status_var.set(f"文件 '{os.path.basename(iid)}' 的时间已更新并保存。")

    def _get_file_info_by_path(self, path):
        return next((item for item in self.files_data if item["path"] == path), None)
    
    def set_time_for_selected(self):
        selected_iids = self.tree.selection()
        if not selected_iids: messagebox.showwarning("操作提示", "请先在列表中选择至少一个文件。"); return
        try:
            day = int(self.day_var.get())
            sequence = int(self.sequence_var.get())
            if not (1 <= sequence): raise ValueError
        except (ValueError, TypeError): messagebox.showerror("输入错误", "日期和当天顺序必须是有效的正整数。"); return
        for iid in selected_iids: self._set_time_for_item(iid, day, sequence)
        self.status_var.set(f"成功为 {len(selected_iids)} 个文件批量设定了时间并已保存。")

    def _redisplay_tree(self, show_new_num=False):
        self.tree.delete(*self.tree.get_children())
        last_num = None; line_char = "─" * 200
        for index, file_info in enumerate(self.files_data):
            current_num = file_info["num"]
            if not show_new_num and last_num is not None and current_num > last_num + 1: self.tree.insert("", "end", values=(line_char, "", "", ""), tags=("separator",))
            title = file_info["title"]
            time_str = file_info['new_time'].strftime('%Y-%m-%d %H:%M') if file_info['new_time'] else "--- 未设定 ---"
            new_num_preview = index + 1 if show_new_num else ""
            tag = "time_set" if file_info['new_time'] else "not_set"
            self.tree.insert("", "end", iid=file_info['path'], values=(title, current_num, time_str, new_num_preview), tags=(tag,))
            last_num = current_num

    def handle_apply(self):
        if not messagebox.askyesno("请确认", f"您确定要根据当前排序，为列表中的 {len(self.files_data)} 个文件重新编号吗？\n此操作不可撤销！"): self.status_var.set("操作已取消。"); return
        title_pattern = re.compile(r"(title: .*?（)(\d+)(）.*)"); date_pattern = re.compile(r"(date: \d{4}-\d{2}-\d{2}T\d{2}:)(\d{2})(:.*Z)")
        modified_count = 0
        for index, file_info in enumerate(self.files_data):
            try:
                filename = file_info['path']; new_num = index + 1
                with open(filename, 'r', encoding='utf-8') as f: content = f.read()
                new_minute = 51 - new_num if 1 <= new_num <= 50 else new_num % 60
                content = title_pattern.sub(rf"\g<1>{new_num}\g<3>", content, count=1); content = date_pattern.sub(rf"\g<1>{new_minute:02d}\g<3>", content, count=1)
                with open(filename, 'w', encoding='utf-8') as f: f.write(content)
                modified_count += 1
            except Exception as e: messagebox.showerror("文件写入错误", f"修改文件 {filename} 时出错:\n{e}"); self.status_var.set(f"在修改 {filename} 时发生错误！"); return
        messagebox.showinfo("操作成功", f"成功修改了 {modified_count} 个文件。")
        self.status_var.set(f"操作完成！成功修改了 {modified_count} 个文件。正在重新加载...")
        self.scan_and_load_files()

if __name__ == "__main__":
    try:
        target_directory = r"D:\website\content\sprouts" 
        os.chdir(target_directory)
    except FileNotFoundError:
        root_tk = tk.Tk()
        root_tk.withdraw()
        messagebox.showerror("路径错误", f"指定的目录不存在，请检查路径：\n{target_directory}")
        exit()
    root = tk.Tk()
    app = MarkdownModifierApp(root)
    root.mainloop()