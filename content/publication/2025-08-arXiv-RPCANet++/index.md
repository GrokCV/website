---
title: "RPCANet++: Deep Interpretable Robust PCA for Sparse Object Segmentation"

authors:
- Fengyi Wu
- admin
- Tianfang Zhang
- Yixuan Ding
- Jian Yang
- Ming-Ming Cheng
- Zhenming Peng

author_notes:
- 
- 
- 
- 
- 
- 

date: "2025-08-06T00:00:00Z"
doi: "arXiv:2508.04190"

# Schedule page publish date (NOT publication's date).
publishDate: "2025-08-06T00:00:00Z"

publication_types: ["article-journal"]

publication: "*IEEE Transactions on Geoscience and Remote Sensing*, vol. 63, pp. 1-15, 2025"
# publication_short: "IEEE TGRS"
# pages: "1-15"
# publisher: "IEEE"
# doi: "10.1109/TGRS.2025.3588753"

abstract: |
  Robust principal component analysis (RPCA) decomposes an observation matrix into low-rank background and sparse object components. This capability has enabled its application in tasks ranging from image restoration to segmentation. However, traditional RPCA models suffer from computational burdens caused by matrix operations, reliance on finely tuned hyperparameters, and rigid priors that limit adaptability in dynamic scenarios. To solve these limitations, we propose RPCANet++, a sparse object segmentation framework that fuses the interpretability of RPCA with efficient deep architectures. Our approach unfolds a relaxed RPCA model into a structured network comprising a Background Approximation Module (BAM), an Object Extraction Module (OEM), and an Image Restoration Module (IRM). To mitigate inter-stage transmission loss in the BAM, we introduce a Memory-Augmented Module (MAM) to enhance background feature preservation, while a Deep Contrast Prior Module (DCPM) leverages saliency cues to expedite object extraction. Extensive experiments on diverse datasets demonstrate that RPCANet++ achieves state-of-the-art performance under various imaging scenarios. We further improve interpretability via visual and numerical low-rankness and sparsity measurements. By combining the theoretical strengths of RPCA with the efficiency of deep networks, our approach sets a new baseline for reliable and interpretable sparse object segmentation. Codes are available at our Project Webpage https://fengyiwu98.github.io/rpcanetx. 

summary: This paper proposes RPCANet++, a framework that fuses the interpretability of Robust Principal Component Analysis (RPCA) with deep networks for reliable and efficient sparse object segmentation.

tags:
- 
- 
- 
- 

featured: false

url_pdf: "https://arxiv.org/pdf/2508.04190"
url_code: "https://github.com/fengyiwu98/RPCANet"
url_dataset: ""
url_poster: ""
url_project: ""
url_slides: ""
url_source: ""
url_video: ""
url_cn_pdf: ""
url_cn_blog: "https://grokcv.ai/blog/rpcanet/rpcanet++/"
url_cn_video: ""

image:
  preview_only: false
--- 