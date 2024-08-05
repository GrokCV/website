---
title: "基于 Shearlet 变换和 Krawtchouk 矩不变量的河流 SAR 图像分割"
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

date: "2015-01-14T00:00:00Z"
doi: ""

# Schedule page publish date (NOT publication's date).
publishDate: "2015-01-14T00:00:00Z"

# Publication type.
# Accepts a single type but formatted as a YAML list (for Hugo requirements).
# Enter a publication type from the CSL standard.
publication_types: ["article-journal"]

# Publication name and optional abbreviated publication name.
publication: "应用科学学报"
publication_short: ""

abstract: 合成孔径雷达 (synthetic aperture radar, SAR) 图像分割是河流检测与识别的关键步骤, 为了进一步提高河流 SAR 图像分割的准确性, 提出一种基于 Shearlet 变换, Krawtchouk 矩不变量及模糊局部信息 C 均值聚类的河流 SAR 图像分割方法. 首先, 对河流 SAR 图像进行 Shearlet 分解, 提取其纹理特征, 构成特征向量的前半部分; 然后, 计算河流 SAR 图像的 Krawtchouk 矩不变量, 作为其形状特征, 构成特征向量的后半部分; 最后, 利用模糊局部信息 C 均值算法依照上述特征向量进行聚类, 由此得到河流 SAR 图像分割结果. 大量实验结果表明, 与近年来提出的脉冲耦合神经网络结合最大方差比准则分割法, Gabor 小波变换结合模糊 C 均值聚类分割法, FLICM 聚类分割法相比, 所提出的方法在主观视觉效果以及客观定量评价指标误分割率上均有明显优势, 且分割河流 SAR 图像更加准确.

# Summary. An optional shortened abstract.
summary: 合成孔径雷达 (synthetic aperture radar, SAR) 图像分割是河流检测与识别的关键步骤, 为了进一步提高河流 SAR 图像分割的准确性, 提出一种基于 Shearlet 变换, Krawtchouk 矩不变量及模糊局部信息 C 均值聚类的河流 SAR 图像分割方法. 

tags:
- 图像分割
featured: false

# links:
# - name: ""
#   url: ""
url_pdf: https://www.jas.shu.edu.cn/CN/abstract/abstract1671.shtml


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
