---
title: "Small target detection based on reweighted infrared patch‐image model"
authors:
- admin
- Jun Guo
- Yiquan Wu
- Yimian Dai
author_notes:

date: "2018-01-01T00:00:00Z"
doi: ""

# Schedule page publish date (NOT publication's date).
publishDate: "2018-01-01T00:00:00Z"

# Publication type.
# Accepts a single type but formatted as a YAML list (for Hugo requirements).
# Enter a publication type from the CSL standard.
publication_types: ["article-journal"]

# Publication name and optional abbreviated publication name.
publication: "IET Image Processing"
publication_short: "IET"

abstract: To further improve the effect of infrared small target detection, a reweighted infrared patch-image model is proposed. First, the authors point out that the nuclear norm in the infrared patch-image model could easily leave some sparse background edges in the target patch-image, leading to an inaccurate background estimation. Then, to overcome this defect, the reweighted nuclear norm is adopted to constrain the background patch-image, which could preserve the background edges better. Considering that some non-target sparse points could not be suppressed by only using l1 norm, the authors introduce the reweighted l1 norm to further enhance the sparsity of target image. Finally, the proposed model is formulated as a reweighted robust principal component analysis problem and solved by the inexact augmented Lagrangian multiplier method. Extensive experiments show that the proposed model outperforms the other six competitive methods in suppressing background clutter and detecting target.

# Summary. An optional shortened abstract.
summary: To further improve the effect of infrared small target detection, a reweighted infrared patch-image model is proposed.

tags:
-  Small Target Detection
featured: false

# links:
# - name: ""
#   url: ""
url_pdf: https://ietresearch.onlinelibrary.wiley.com/doi/full/10.1049/iet-ipr.2017.0353


# Featured image
# To use, add an image named `featured.jpg/png` to your page's folder. 
image:
  caption: 'Image credit: [**Unsplash**](https://unsplash.com/photos/jdD8gXaTZsc)'
  focal_point: ""
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
slides: example
---

