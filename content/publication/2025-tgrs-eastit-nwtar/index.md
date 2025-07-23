---
title: "Infrared Small Target Detection via Nonconvex Weighted Tensor Rank Minimization and Adaptive Spatial–Temporal Modeling"

authors:
- Yang Sun
- Zaiping Lin
- Ting Liu
- Boyang Li
- Qian Yin
- Yingwu Chen
- admin

author_notes:
- 
- 
- 
- 
- 
- 
- Corresponding Author

# 日期格式：2025-04-23
# 期刊类型、卷号、页码、DOI等

date: "2025-04-23"

publication_types: ["article-journal"]

publication: "IEEE Transactions on Geoscience and Remote Sensing"
publication_short: "IEEE TGRS"
volume: 63
pages: "5003918"
publisher: "IEEE"
doi: "10.1109/TGRS.2025.3563495"

abstract: |
  Infrared (IR) small target detection (TD) is of great significance for various applications. However, it is significantly challenged by complex backgrounds and low signal-to-clutter ratios. Although low-rank and sparse decomposition (LRSD)-based methods are widely employed, they are hampered by fixed temporal step sizes, transpose errors in tensor recovery, and the suboptimal approximation of sparsity using the l1 norm. To tackle these problems, we propose an entropy-based adaptive spatial-temporal IR tensor with nonconvex weighted average tensor rank (EASTIT-NWTAR) method. First, we propose an adaptive spatial-temporal tensor construction approach that leverages tensor information entropy to dynamically adjust the temporal step size, ensuring an accurate representation of background changes and maintaining its low-rank property. Second, we propose a nonconvex weighted tensor norm combining the Laplace norm and weighted average tensor rank (WTAR) norm to effectively mitigate transpose errors and enhance low-rank recovery. Finally, we substitute the l1 norm with the smoothly clipped absolute deviation (SCAD) norm to improve sparse target reconstruction accuracy. The proposed method is effectively solved using the alternating direction multiplier method (ADMM). Extensive experiments demonstrate that proposed method outperforms state-of-the-art methods in both TD and background suppression (BS).

summary: This paper proposes EASTIT-NWTAR, a novel method for infrared small target detection using adaptive spatial-temporal tensor modeling and nonconvex weighted tensor rank minimization.

tags:
- Infrared Small Target Detection
- Tensor Decomposition
- Low-Rank Modeling
- Adaptive Modeling
- EASTIT-NWTAR

featured: false

url_pdf: ""
url_code: ""
url_dataset: ""
url_poster: ""
url_project: ""
url_slides: ""
url_source: ""
url_video: ""

image:
  preview_only: false
--- 