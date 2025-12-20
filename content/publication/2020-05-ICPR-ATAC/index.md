---
title: "Attention as Activation"

authors:
- admin
- Stefan Oehmcke
- Fabian Gieseke
- Yiquan Wu
- Kobus Barnard

date: "2020-07-15T00:00:00Z"

doi: "10.1109/ICPR48806.2021.9413020"

# Schedule page publish date (NOT publication's date).
publishDate: "2021-01-15T00:00:00Z"

# Publication type.
# Accepts a single type but formatted as a YAML list (for Hugo requirements).
# Enter a publication type from the CSL standard.
publication_types: ["paper-conference"]

# Publication name and optional abbreviated publication name.
publication: "*Proceedings of the 25th International Conference on Pattern Recognition (ICPR)*, pp. 9156–9163, 2021"
# publication_short: "ICPR 2020"

abstract: Activation functions and attention mechanisms are typically treated as having different purposes and have evolved differently. However, both concepts can be formulated as a nonlinear gating function. Inspired by their similarity, we propose a novel type of activation units called attentional activation units as a unification of activation functions and attention mechanisms. In particular, we propose a local channel attention module for the simultaneous non-linear activation and element-wise feature refinement, which locally aggregates point-wise cross channel feature contexts. By replacing the wellknown rectified linear units by such ATAC units in convolutional networks, we can construct fully attentional networks that perform significantly better with a modest number of additional parameters. We conducted detailed ablation studies on the ATAC units using several host networks with varying network depths to empirically verify the effectiveness and efficiency of the units. Furthermore, we compared the performance of the ATAC units against existing activation functions as well as other attention mechanisms on the CIFAR-10, CIFAR-100, and ImageNet datasets. Our experimental results show that networks constructed with the proposed ATAC units generally yield performance gains over their competitors given a comparable number of parameters.

# Summary. An optional shortened abstract.
summary: This paper introduces attentional activation units (ATAC), a unification of activation functions and attention mechanisms. ATAC units include a local channel attention module for simultaneous non-linear activation and element-wise feature refinement, locally aggregating point-wise cross-channel feature contexts in convolutional networks.

tags:
- Activation Function
- Attention Mechanism

featured: false

links:
# - name: 
url_pdf: https://arxiv.org/pdf/2007.07729
url_code: 'https://github.com/YimianDai/open-atac'
url_cn_pdf: ""
url_cn_blog: ""
url_cn_video: ""

# Featured image
# To use, add an image named `featured.jpg/png` to your page's folder. 
image:
  # caption: 'Image credit: [**Unsplash**](https://unsplash.com/photos/s9CC2SKySJM)'
  # focal_point: ""
  preview_only: false

# Associated Projects (optional).
#   Associate this publication with one or more of your projects.
#   Simply enter your project's folder or file name without extension.
#   E.g. `internal-project` references `content/project/internal-project/index.md`.
#   Otherwise, set `projects: []`.
# projects:
# - internal-project
projects: []

# Slides (optional).
#   Associate this publication with Markdown slides.
#   Simply enter your slide deck's filename without extension.
#   E.g. `slides: "example"` references `content/slides/example/index.md`.
#   Otherwise, set `slides: ""`.
# slides: example
---

