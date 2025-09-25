import os
import re
import json
from datetime import datetime

print("--- 开始从截图中恢复排序记忆 ---")

# 1. 根据您的截图，我已将数据手动转录到这里
# 格式为：{ 原序号: "设定时间" }
screenshot_data = {
    1: "2025-09-01 09:00",
    32: "2025-09-13 09:00",
    34: "2025-09-16 09:00",
    33: "2025-09-16 09:01",
    36: "2025-09-17 09:00",
    35: "2025-09-17 09:01",
    37: "2025-09-17 09:02",
    6: "2025-09-17 09:03",
    2: "2025-09-17 09:04",
    4: "2025-09-17 09:05",
    5: "2025-09-17 09:06",
    19: "2025-09-17 09:07",
    22: "2025-09-17 09:08",
    20: "2025-09-17 09:09",
    23: "2025-09-17 09:10",
    21: "2025-09-17 09:11",
    26: "2025-09-17 09:12",
}

# 2. 定义相关变量
MEMORY_FILE = "time_memory.json"
title_pattern = re.compile(r"title: .*?（(\d+)）")
memory_to_save = {}
files_found = 0
files_matched = 0

# 3. 扫描当前目录下的所有 .md 文件
print("正在扫描当前目录下的 .md 文件...")
try:
    for filename in os.listdir('.'):
        if filename.endswith('.md'):
            files_found += 1
            try:
                with open(filename, 'r', encoding='utf-8') as f:
                    content_head = f.readlines(500)
                
                title_line_content = ""
                for line in content_head:
                    if line.startswith("title:"):
                        title_line_content = line
                        break

                match = title_pattern.search(title_line_content)
                if match:
                    num = int(match.group(1))
                    # 4. 如果文件的序号在我们的截图中，就建立映射关系
                    if num in screenshot_data:
                        files_matched += 1
                        # 将截图中的时间字符串转换为程序能识别的ISO格式
                        time_str = screenshot_data[num]
                        dt_object = datetime.strptime(time_str, '%Y-%m-%d %H:%M')
                        memory_to_save[filename] = dt_object.isoformat()
                        print(f"  [匹配成功] 文件: {filename} (序号 {num}) -> 时间: {time_str}")

            except Exception as e:
                print(f"处理文件 {filename} 时出错: {e}")

    # 5. 将最终生成的记忆写入 time_memory.json 文件
    if files_matched > 0:
        with open(MEMORY_FILE, 'w', encoding='utf-8') as f:
            json.dump(memory_to_save, f, indent=4)
        print("\n-------------------------------------------")
        print(f"🎉 成功！已为您生成记忆文件: {MEMORY_FILE}")
        print(f"总共扫描了 {files_found} 个 .md 文件，成功匹配并恢复了 {files_matched} 条记录。")
        print("您现在可以运行主程序了！")
        print("-------------------------------------------\n")
    else:
        print("\n警告：扫描完成，但没有找到任何与截图中序号匹配的文件。请检查脚本是否放置在正确的目录下。")

except Exception as e:
    print(f"\n发生严重错误: {e}")