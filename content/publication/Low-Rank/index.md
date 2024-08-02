---
title: "Infrared Small Target Detection via L0 Sparse Gradient Regularized Tensor Spectral Support Low-Rank Decomposition"
authors:
- admin
- Fei Zhou
- Maixia Fu
- Yule Duan
- Yimian Dai
- Yiquan Wu
  
author_notes:
- 
- "Corresponding Author"
- 
- 
- 
- "Corresponding Author"
date: "2022-09-26T00:00:00Z"
# Enter a publication type from the CSL standard.
publication_types: ["article-journal"]

# Publication name and optional abbreviated publication name.
abstract: Infrared small target detection has been extensively investigated by incorporating the low-rank and sparse prior into tensor decomposition frameworks. Despite its success, the said paradigm remains several limitations in complex scenes, such as: 1) the inadequate spatial-temporal information exploitation among sequential patches; 2) the incomplete suppression of the complex background interference. To mitigate the defects, this article provides a tensor decomposition method integrating spatial-temporal  sparse gradient regularization and spectral support constraint. First, we present a skillfully connected multiframe patch group (CMPG) model to explore local spatial information and adjacent interframe correlation among multiframes patches. Then, for CMPG model, a scalable tensor spectral support constraint is employed to distinctively regularize its redundant and rare components. Considering the nonlocal uniqueness of small targets and the local continuity of rare distractors, an extended spatial-temporal gradient constraint is embedded into target-background separation for better suppression of structural clutter, and a reweighted scheme is also used to eliminate isolated nontarget points. The final model is efficiently solved by the alternating direction method of multipliers. Experiments are conducted on extensive simulating datasets and real scenes, suggesting that the proposed method achieves a considerable boost against other competitors in terms of visual effect and subjective evaluation.


# Summary. An optional shortened abstract.
summary: 

tags:
- 
featured: false

# links:
# - name: ""
#   url: ""
url_pdf: https://ieeexplore.ieee.org/abstract/document/9903329/
url_code: ''
url_dataset: ''
url_poster: ''
url_project: ''
url_slides: ''
url_source: ''
url_video: ''

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
projects: []

# Slides (optional).
#   Associate this publication with Markdown slides.
#   Simply enter your slide deck's filename without extension.
#   E.g. `slides: "example"` references `content/slides/example/index.md`.
#   Otherwise, set `slides: ""`.
# slides: example
---