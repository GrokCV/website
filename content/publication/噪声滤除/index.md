---
title: "基于非局部均值和 SUSAN 算子的混合噪声滤除"
authors:
- admin
- 吴一全
- 王凯
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
publication: "光子学报"
publication_short: ""

abstract: 为了更好地滤除图像中脉冲噪声和高斯噪声组成的混合噪声,提出了一种基于非局部均值和Small Univalue Segment Assimilating Nucleus(SUSAN)算子的混合噪声滤除方法.该方法首先根据脉冲噪声点与角点之间吸收核同值区形状特征的不同,采用SUSAN算子检测出大量的特征点,特征点主要是脉冲噪声点,也可能含有小部分角点.将特征点进行排序,出现频次最高两位的点为脉冲噪声点.然后采用改进的均值滤波法计算脉冲噪声点邻域中非脉冲噪声点的均值,以此替换脉冲噪声点灰度值.最后针对已滤除脉冲噪声的图像,采用考虑了图像块信息的非局部均值方法滤除剩余的高斯噪声.去噪实验结果表明:与自适应中值和加权均值结合的方法,中值滤波与小波结合的方法,脉冲耦合神经网络与中值滤波结合的方法相比,本文方法主观视觉效果更好,能够更好地保留图像中的边缘细节,客观评价指标峰值信噪比有较大的提高,滤除混合噪声的优势明显.

# Summary. An optional shortened abstract.
summary: 

tags:
- 噪声滤除
featured: false

# links:
# - name: ""
#   url: ""
url_pdf: https://scholar.google.com/scholar?cluster=13667962195373504428&hl=en&oi=scholarr


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
