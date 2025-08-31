---
title: "Sparse Prior Is Not All You Need: When Differential Directionality Meets Saliency Coherence for Infrared Small Target Detection"

authors:
- FeiZhou
- Maixia Fu
- Yulei Qian
- Jian Yang
- admin

author_notes:
- 
- 
- 
- 
- Corresponding Author

date: "2024-07-22T00:00:00Z"
# Enter a publication type from the CSL standard.
publication_types: ["article-journal"]

# Publication name and optional abbreviated publication name.
publication: "arXiv"
publication_short: ""

# Publication name and optional abbreviated publication name.
abstract: Infrared small target detection is crucial for the efficacy of infrared search and tracking systems. Current tensor decomposition methods emphasize representing small targets with sparsity but struggle to separate targets from complex backgrounds due to insufficient use of intrinsic directional information and reduced target visibility during decomposition. To address these challenges, this study introduces a Sparse Differential Directionality prior (SDD) framework. SDD leverages the distinct directional characteristics of targets to differentiate them from the background, applying mixed sparse constraints on the differential directional images and continuity difference matrix of the temporal component, both derived from Tucker decomposition. We further enhance target detectability with a saliency coherence strategy that intensifies target contrast against the background during hierarchical decomposition. A Proximal Alternating Minimization-based (PAM) algorithm efficiently solves our proposed model. Experimental results on several real-world datasets validate our method's effectiveness, outperforming ten state-of-the-art methods in target detection and clutter suppression. Our code is available at https://github.com/GrokCV/SDD.


# Summary. An optional shortened abstract.
summary: A Sparse Differential Directionality prior (SDD) framework is proposed for infrared small target detection. SDD leverages directional characteristics to differentiate targets from background, applying mixed sparse constraints on differential directional images and continuity difference matrix derived from Tucker decomposition. Saliency coherence strategy further enhances target detectability during hierarchical decomposition.

tags:
- Infrared Small Target Detection

featured: false

# links:
# - name: ""
#   url: ""
url_pdf: https://arxiv.org/pdf/2407.15369
url_code: 'https://github.com/GrokCV/SDD'
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
