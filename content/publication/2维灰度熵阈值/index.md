---
title: "基于 2 维灰度熵阈值选取快速迭代的图像分割"
authors:
- admin
- 吴诗婳
- 吴一全
- 周建江
- 孟天亮
- 戴一冕

author_notes:
- 
-
- 
-

date: "2015-08-13T00:00:00Z"
doi: ""

# Schedule page publish date (NOT publication's date).
publishDate: "2015-08-13T00:00:00Z"

# Publication type.
# Accepts a single type but formatted as a YAML list (for Hugo requirements).
# Enter a publication type from the CSL standard.
publication_types: ["article-journal"]

# Publication name and optional abbreviated publication name.
publication: "中国图象图形学报"
publication_short: ""

abstract: 目的 为了使图像阈值分割的精度和速度进一步提高,提出了一种基于2维灰度熵阈值选取快速迭代的图像分割方法。方法 首先,提出了1维灰度熵阈值选取的快速迭代算法;然后,考虑图像目标和背景的类内灰度均匀性,给出了基于灰度—邻域平均灰度级直方图的灰度熵阈值选取准则;最后,提出了2维灰度熵阈值选取的快速迭代算法,并采用递推方式计算准则函数中的中间变量,避免其重复运算,加快了运算速度,大大减少了运算量。结果 大量实验结果表明,与近年来提出的3种阈值分割法相比,所提出的方法分割性能更优,分割后的图像中目标区域完整,边缘清晰,细节丰富且运行时间短,仅为基于混沌小生境粒子群优化的二维斜分倒数熵分割法运行时间的3%左右。结论 本文方法对不同类型灰度级图像的分割效果及运行速度均有明显优势,是实际系统中可选择的一种快速有效的图像分割方法。

# Summary. An optional shortened abstract.
summary: 

tags:
- 图像分割
featured: false

# links:
# - name: ""
#   url: ""
url_pdf: http://www.cjig.cn/jig/ch/reader/view_abstract.aspx?journal_id=jig&file_no=20150807&html_url=jig/article/html/20150807


# Featured image
# To use, add an image named `featured.jpg/png` to your page's folder. 
image:
  caption: 'Image credit: [**Unsplash**](https://unsplash.com/photos/jdD8gXaTZsc)'
  focal_point: ""
  preview_only: false

# Associated Projects (optional).
#   Associate this publication with one or more of your projects.
#   Simply enter your project's folder or file name without extension.
#   E.g. `internal-project` references `content/project/internal-project/index.md`.
#   Otherwise, set `projects: []`.
projects: []

# Slides (optional).
#   Associate this publication with Markdown slides.
#   Simply enter your slide deck's filename without extension.
#   E.g. `slides: "example"` references `content/slides/example/index.md`.
#   Otherwise, set `slides: ""`.
slides: example
---
