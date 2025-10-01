---
title: "Attentional Local Contrast Networks for Infrared Small Target Detection"
authors:
- admin
- Yiquan Wu
- FeiZhou
- Kobus Barnard

author_notes:
- "Corresponding Author"
- 
- 
- 

date: "2021-01-05T13:37:23Z"
doi: "10.1109/TGRS.2023.3243062"

# Schedule page publish date (NOT publication's date).
publishDate: "2021-01-05T00:00:00Z"

# Publication type.
# Accepts a single type but formatted as a YAML list (for Hugo requirements).
# Enter a publication type from the CSL standard.
publication_types: ["article-journal"]

# Publication name and optional abbreviated publication name.
publication: "*IEEE Transactions on Geoscience and Remote Sensing*, vol. 59, no. 11, pp. 9813-9824, 2021"
# publication_short: "IEEE TGRS"

abstract: To mitigate the issue of minimal intrinsic features for pure data-driven methods, in this article, we propose a novel model-driven deep network for infrared small target detection, which combines discriminative networks and conventional model-driven methods to make use of both labeled data and the domain knowledge. By designing a feature map cyclic shift scheme, we modularize a conventional local contrast measure method as a depth-wise parameter-less nonlinear feature refinement layer in an end-to-end network, which encodes relatively long-range contextual interactions with clear physical interpretability. To highlight and preserve the small target features, we also exploit a bottom-up attentional modulation integrating the smaller scale subtle details of low-level features into high-level features of deeper layers. We conduct detailed ablation studies with varying network depths to empirically verify the effectiveness and efficiency of the design of each component in our network architecture. We also compare the performance of our network against other model-driven methods and deep networks on the open SIRST data set as well. The results suggest that our network yields a performance boost over its competitors.

# Summary. An optional shortened abstract.
summary: This paper proposes a model-driven deep network that combines discriminative networks and conventional model-driven methods, utilizing a feature map cyclic shift scheme and bottom-up attentional modulation to highlight and preserve infrared small target features.

tags:
- Infrared Small Target Detection
featured: false

# links:
# - name: ""
#   url: ""
url_pdf: https://arxiv.org/pdf/2012.08573.pdf
url_code: 'https://github.com/YimianDai/open-alcnet'
url_dataset: 'https://github.com/YimianDai/sirst'
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
projects: []

# Slides (optional).
#   Associate this publication with Markdown slides.
#   Simply enter your slide deck's filename without extension.
#   E.g. `slides: "example"` references `content/slides/example/index.md`.
#   Otherwise, set `slides: ""`.
# slides: example
---
