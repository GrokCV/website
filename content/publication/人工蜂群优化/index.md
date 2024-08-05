
---
title: "基于人工蜂群优化的 NSCT 域图像模糊集增强方法"
authors:
- admin
- 吴一全
- 殷骏
- 戴一冕

author_notes:
- 
-
- 
-

date: "2015-00-00T00:00:00Z"
doi: ""

# Schedule page publish date (NOT publication's date).
publishDate: "2015-00-00T00:00:00Z"

# Publication type.
# Accepts a single type but formatted as a YAML list (for Hugo requirements).
# Enter a publication type from the CSL standard.
publication_types: ["article-journal"]

# Publication name and optional abbreviated publication name.
publication: "华南理工大学学报: 自然科学版"
publication_short: ""

abstract: 针对实际应用中所采集的图像对比度低,边缘细节模糊的问题,提出了基于非下采样Contourlet变换(NSCT),模糊集,人工蜂群(ABC)优化的自适应图像增强方法.首先对输入图像进行NSCT分解,得到一个低频子带和多个高频子带;然后依据贝叶斯萎缩阈值和非线性增益函数增强高频子带系数,采用模糊增强法增强低频子带系数,并利用ABC算法优化其中的模糊参数,以提高模糊增强法的自适应性;接着用低频子带图像的信息熵作为ABC算法的适应度函数,同时引入较劣种群随机初始化策略改进ABC算法,以缩短增强方法的运行时间.文中采用该增强方法对淡水鱼,铁轨表面,储粮害虫3类图像进行了增强实验,并依据主观视觉效果和对比度增益,清晰度增益,信息熵3个客观定量评价指标,对文中方法及其他3种同类增强方法进行了比较.结果表明,所提出的方法视觉效果最佳,能提高图像的对比度和清晰度,目标边缘光滑,且增加了图像的信息量,便于后续准确地进行图像检测与识别.

# Summary. An optional shortened abstract.
summary: 

tags:
- 图像增强
featured: false

# links:
# - name: ""
#   url: ""
url_pdf: https://scholar.google.com/scholar?cluster=8769495547794182182&hl=en&oi=scholarr


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
