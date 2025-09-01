---
title: "DRPCA-Net: Make Robust PCA Great Again for Infrared Small Target Detection"

authors:
- Zihao Xiong
- Fei Zhou
- Fengyi Wu
- Shuai Yuan
- Maixia Fu
- Zhenming Peng
- Jian Yang
- admin

author_notes:
- 
- 
- 
- 
- Corresponding Author
- 
- 
- Corresponding Author

date: "2025-07-14"

publication_types: ["article-journal"]

publication: "IEEE Transactions on Geoscience and Remote Sensing"
# publication_short: "IEEE TGRS"
pages: "1-16"
publisher: "IEEE"
doi: "10.1109/TGRS.2025.3588392"

abstract: |
  Infrared small target detection plays a vital role in remote sensing, industrial monitoring, and various civilian applications. Despite recent progress powered by deep learning, many end-to-end convolutional models tend to pursue performance by stacking increasingly complex architectures, often at the expense of interpretability, parameter efficiency, and generalization. These models typically overlook the intrinsic sparsity prior of infrared small targets–an essential cue that can be explicitly modeled for both performance and efficiency gains. To address this, we revisit the model-based paradigm of Robust Principal Component Analysis (RPCA) and propose Dynamic RPCA Network (DRPCA-Net), a novel deep unfolding network that integrates the sparsity-aware prior into a learnable architecture. Unlike conventional deep unfolding methods that rely on static, globally learned parameters, DRPCA-Net introduces a dynamic unfolding mechanism via a lightweight hypernetwork. This design enables the model to adaptively generate iteration-wise parameters conditioned on the input scene, thereby enhancing its robustness and generalization across diverse backgrounds. Furthermore, we design a Dynamic Residual Group (DRG) module to better capture contextual variations within the background, leading to more accurate low-rank estimation and improved separation of small targets. Extensive experiments on multiple public infrared datasets demonstrate that DRPCA-Net significantly outperforms existing state-of-the-art methods in detection accuracy. Code is available at https://github.com/GrokCV/DRPCA-Net.

summary: This paper proposes DRPCA-Net, a dynamic deep unfolding network for infrared small target detection, integrating sparsity-aware priors and dynamic parameter generation for robust performance.

tags:
- Infrared Small Target Detection
- RPCA
- Deep Learning
- DRPCA-Net
- Robustness

featured: false

url_pdf: "https://arxiv.org/pdf/2507.09541"
url_code: "https://github.com/GrokCV/DRPCA-Net"
url_dataset: ""
url_poster: ""
url_project: ""
url_slides: ""
url_source: ""
url_video: ""
url_cn_pdf: ""
url_cn_blog: ""
url_cn_video: ""

image:
  preview_only: false
--- 