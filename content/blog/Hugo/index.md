---
title: Hugo
date: 2025-06-20
draft: true
math: true
authors: 
- admin
# image:
#   placement: 2
#   caption: 'Image credit: [**John Moeses Bauan**](https://unsplash.com/photos/OGZtQF8iC0g)'
# image:
#   placement: 2
#   caption: '[](https://github.com/GrokCV/imgbed/blob/master/blog/AuxDet/author.png?raw=true)'
---

### 网站结构

来自 [Hugo Blox | Docs 的 Site structure 文档](https://docs.hugoblox.com/reference/site-structure/)

There are **4 main folders for Hugo-based sites**:

- `content/` for your Markdown-formatted content files (homepage, etc.)
  - `_index.md` the homepage (**Hugo requires that the homepage and archive pages have an underscore prefix**)
- `assets/`
  - `media/` for your media files (images, videos)
    - `icons/custom/` upload any custom SVG icons you want to use
- `config/_default/` for your site configuration files
  - `hugo.yaml` to configure Hugo (site title, URL, Hugo options, setup per-folder page features)
  - `module.yaml` to install or uninstall Hugo themes and plugins
  - `params.yaml` to configure Hugo Blox options (SEO, analytics, site features)
  - `menus.yaml` to configure your menu links (if the menu is enabled in `params.yaml`)
  - `languages.yaml` to configure your site’s language or to set language-specific options in a multilingual site
- `static/uploads/` for any files you want visitors to download, such as a PDF of your resume
- `hugo-blox/blox/community/` install custom or community blox here
- `go.mod` sets the version of Hugo themes/plugins which your site uses - [learn how to update](https://docs.hugoblox.com/reference/update/)

### 文件命名约定

来自 [Hugo Blox | Docs 的 Hugo File Naming Convention 文档](https://docs.hugoblox.com/reference/site-structure/)

Hugo 为我们提供了两种命名标准页面文件的选项：`TITLE/index.md` 或 `TITLE.md`，其中 TITLE 是您的页面名称。

页面名称应该是小写，并使用连字符（`-`）而不是空格。

这两种方法产生相同的输出，因此您可以选择自己喜欢的方法来命名和组织文件。基于文件夹的方法的一个好处是，页面的所有文件（如图像）都包含在页面的文件夹中，因此如果您希望与他人共享原始 Markdown 页面，则更易于移植。

主页是一个特例，因为 Hugo 要求主页和列表页面命名为 `_index.md`。

## `config`

### `config/_default/params.yaml`

#### 开启 LaTeX 渲染

```yaml
features:
  math: true
```

#### 开启站内搜索

In your `config/_default/params.yaml`, ensure that the navigation bar (menu) is displayed and that the search button, show_search, is displayed on the menu:

```yaml
header:
  navbar:
    enable: true
    show_search: true
```

### `/config/_default/menus.yaml`

`config/_default/menus.yaml` 是用来设置导航栏菜单栏名称的, url 需要和 content 下的文件夹名称保持一致，比如 url 有个 blog，那么 content 下也有有个 blog 文件夹，name 是用来设定导航栏名称的，可以改成中文，比如「博客」

```markdown
main:
  - name: Home
    url: /
    weight: 10
  - name: Blog
    url: blog
    weight: 20
  - name: About
    url: about/
    weight: 30
```

### `content`

#### `/content/_index.md`

`/content/_index.md` 是用来设置首页 `/` 的配置的

yimian.grokcv.ai 的设置如下：

```markdown
sections:
  - block: hero
  - block: about.biography
  - block: collection
    id: publication
  - block: collection
    id: talks
  - block: collection
    id: blog
```

specify the URL as a hash `#` followed by the filename of the desired widget in your `content/home/` folder. The weight parameter defines the order that the links will appear in. 不是用来设置导航栏菜单栏名称的