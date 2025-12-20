---
title: "DenoDet: Attention as Deformable Multi-Subspace Feature Denoising for Target Detection in SAR Images"

authors:
- admin
- Minrui Zou
- Yuxuan Li
- Xiang Li
- Kang Ni
- Jian Yang

author_notes:
- Equal contribution
- Equal contribution
- 
- 
- Corresponding author
- Corresponding author

date: "2024-11-28T00:00:00Z"
# Enter a publication type from the CSL standard.
publication_types: ["article-journal"]

# Publication name and optional abbreviated publication name.
publication: "*IEEE Transactions on Aerospace and Electronic Systems*, vol. 61, no. 2, pp. 4729–4743, 2024"
# publication_short: ""

# Publication name and optional abbreviated publication name.
abstract: Synthetic Aperture Radar (SAR) target detection has long been impeded by inherentspeckle noise and the prevalence of diminutive, ambiauous targets, While deep neuranetworks have advanced SAR target detection, their intrinsic low-frequency bias andstatic post-training weights falter with coherent noise and preserving subtle detailsacross heterogeneous terrains. Motivated by traditional SAR image denoising, we propose DenoDet, a network aided by explicit frequency domain transform to calibrateconvolutional biases and pay more attention to high-frequencies, forming a natural multi.scale subspace representation to detect targets from the perspective of multi-subspacedenoising. We desian TransDeno, a dynamic frequency domain attention module that performs as a transform domain soft thresholding operation, dynamically denoisingacross subspaces by preserving salient target signals and attenuating noise. Toadaptively adjust the granularity of subspace processing, we also propose a deformablegroup fully-connected layer (DeGroFC) that dynamically varies the group conditioned onthe input features. Without bells and whistles, our plug-and-play TransDeno sets state-of.the-art scores on multiple SAR target detection datasets. The code is available at https://github.com/GrokCV/GrokSAR.

# Summary. An optional shortened abstract.
summary: This study presents DenoDet, a novel synthetic aperture radar (SAR) target detection network that leverages frequency domain transform for multi-scale subspace representation. The proposed TransDeno module dynamically denoises across subspaces by preserving target signals and attenuating noise, and a deformable group fully-connected layer (DeGroFC) adjusts the granularity of subspace processing based on input features.

doi: '10.1109/TAES.2024.3507786'

tags:
- SAR Target Detection

featured: false

# links:
# - name: ""
#   url: ""
url_pdf: 'https://arxiv.org/pdf/2406.02833'
url_code: 'https://github.com/GrokCV/GrokSAR'
url_dataset: ''
url_poster: 'https://ieeexplore.ieee.org/document/10770564'
url_project: ''
url_slides: ''
url_source: ''
url_video: ''
url_cn_pdf: "https://gitee.com/YimianDai/filebed/blob/master/translation/2025-TAES-DenoDet-V1-CN-Translation.pdf"
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
