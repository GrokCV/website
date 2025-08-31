---
title: "Pick of the Bunch: Detecting Infrared Small Targets Beyond Hit-Miss Trade-Offs via Selective Rank-Aware Attention"

authors:
- admin
- Peiwen Pan
- Yulei Qian
- Yuxuan Li
- Xiang Li
- Jian Yang
- Huan Wang

author_notes:
- "Equal Contribution"
- "Equal Contribution"
- 
- 
- 
- "Corresponding Author"
- "Corresponding Author"

date: "2024-09-11T00:00:00Z"
doi: "10.1109/TGRS.2024.3458896"

# Schedule page publish date (NOT publication's date).
publishDate: "2024-09-11T00:00:00Z"

# Publication type.
# Accepts a single type but formatted as a YAML list (for Hugo requirements).
# Enter a publication type from the CSL standard.
publication_types: ["article-journal"]

# Publication name and optional abbreviated publication name.
publication: "*IEEE Transactions on Geoscience and Remote Sensing*, 2024."
publication_short: "IEEE TGRS"

abstract: Infrared small target detection faces the inherent challenge of precisely localizing dim targets amidst complex background clutter. Traditional approaches struggle to balance detection precision and false alarm rates. To break this dilemma, we propose SeRankDet, a deep network that achieves high accuracy beyond the conventional hit-miss trade-off, by following the “Pick of the Bunch” principle. At its core lies our Selective Rank-Aware Attention (SeRank) module, employing a non-linear Top-K selection process that preserves the most salient responses, preventing target signal dilution while maintaining constant complexity. Furthermore, we replace the static concatenation typical in U-Net structures with our Large Selective Feature Fusion (LSFF) module, a dynamic fusion strategy that empowers SeRankDet with adaptive feature integration, enhancing its ability to discriminate true targets from false alarms. The network’s discernment is further refined by our Dilated Difference Convolution (DDC) module, which merges differential convolution aimed at amplifying subtle target characteristics with dilated convolution to expand the receptive field, thereby substantially improving target-background separation. Despite its lightweight architecture, the proposed SeRankDet sets new benchmarks in state-of-the-art performance across multiple public datasets. The code is available at https://github.com/GrokCV/SeRankDet.

# Summary. An optional shortened abstract.
summary: This paper introduces SeRankDet, a deep learning model for infrared small target detection. SeRankDet leverages our novel Selective Rank-Aware Attention module for preserving salient responses, Large Selective Feature Fusion for dynamic feature integration, and Dilated Difference Convolution for improved target-background separation. Despite its lightweight design, SeRankDet delivers state-of-the-art performance.

tags:
- Infrared Small Target Detection

featured: false

# links:
# - name: ""
#   url: ""
url_pdf: https://www.arxiv.org/pdf/2408.03717
url_code: 'https://github.com/GrokCV/SeRankDet'
url_dataset: ''
url_poster: ''
url_project: ''
url_slides: ''
url_source: ''
url_video: ''
url_cn_pdf: ""
url_cn_blog: ""
url_cn_video: ""

# Featured image
# To use, add an image named `featured.jpg/png` to your page's folder. 
image:
  # caption: 'Image credit: [**Unsplash**](https://unsplash.com/photos/jdD8gXaTZsc)'
  # focal_point: ""
  preview_only: false

# Associated Projects (optional).
#   Associate this publication with one or more of your projects.
#   Simply enter your project's folder or file name without extension.
#   E.g. `internal-project` references `content/project/internal-project/index.md`.
#   Otherwise, set `projects: []`.
# projects: []

# Slides (optional).
#   Associate this publication with Markdown slides.
#   Simply enter your slide deck's filename without extension.
#   E.g. `slides: "example"` references `content/slides/example/index.md`.
#   Otherwise, set `slides: ""`.
# slides: example
---
