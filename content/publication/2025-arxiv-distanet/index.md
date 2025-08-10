---
title: "DISTA-Net: Dynamic Closely-Spaced Infrared Small Target Unmixing"

authors:
- Shengdong Han
- Shangdong Yang
- Xin Zhang
- Yuxuan Li
- Xiang Li
- Jian Yang
- Ming-Ming Cheng
- admin

author_notes:
- Equal Contribution
- Equal Contribution
- 
- 
- 
- 
- 
- "Corresponding Author"

date: "2025-05-25"

publication_types: ["preprint"]

publication: "arXiv preprint arXiv:2505.19148"
publication_short: "arXiv"
doi: "10.48550/arXiv.2505.19148"

abstract: |
  Resolving closely-spaced small targets in dense clusters presents a significant challenge in infrared imaging, as the overlapping signals hinder precise determination of their quantity, sub-pixel positions, and radiation intensities. While deep learning has advanced the field of infrared small target detection, its application to closely-spaced infrared small targets has not yet been explored. This gap exists primarily due to the complexity of separating superimposed characteristics and the lack of an open-source infrastructure. In this work, we propose the Dynamic Iterative Shrinkage Thresholding Network (DISTA-Net), which reconceptualizes traditional sparse reconstruction within a dynamic framework. DISTA-Net adaptively generates convolution weights and thresholding parameters to tailor the reconstruction process in real time. To the best of our knowledge, DISTA-Net is the first deep learning model designed specifically for the unmixing of closely-spaced infrared small targets, achieving superior sub-pixel detection accuracy. Moreover, we have established the first open-source ecosystem to foster further research in this field. This ecosystem comprises three key components: (1) CSIST-100K, a publicly available benchmark dataset; (2) CSO-mAP, a custom evaluation metric for sub-pixel detection; and (3) GrokCSO, an open-source toolkit featuring DISTA-Net and other models. Our code and dataset are available at https://github.com/GrokCV/GrokCSO.

summary: This paper proposes DISTA-Net, the first deep learning model for unmixing closely-spaced infrared small targets, and introduces an open-source ecosystem for this field.

tags:
- Infrared Small Target Detection
- Sparse Reconstruction
- Deep Learning
- DISTA-Net
- Sub-pixel Detection

featured: false

url_pdf: "https://arxiv.org/pdf/2505.19148"
url_code: "https://github.com/GrokCV/GrokCSO"
url_dataset: "https://github.com/GrokCV/GrokCSO"
url_poster: ""
url_project: ""
url_slides: ""
url_source: ""
url_video: ""

image:
  preview_only: false
--- 