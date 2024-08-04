---
title: "Infrared small target and background separation via column-wise weighted robust principal component analysis"
authors:
- admin
- Yimian Dai
- Yiquan Wu
- Yu Song

author_notes:
- 
-
- 
-

date: "2016-07-01T00:00:00Z"
doi: ""

# Schedule page publish date (NOT publication's date).
publishDate: "2016-07-01T00:00:00Z"

# Publication type.
# Accepts a single type but formatted as a YAML list (for Hugo requirements).
# Enter a publication type from the CSL standard.
publication_types: ["article-journal"]

# Publication name and optional abbreviated publication name.
publication: "Infrared Physics & Technology"
publication_short: "IPT"

abstract: When facing extremely complex infrared background, due to the defect of 
 norm based sparsity measure, the state-of-the-art infrared patch-image (IPI) model would be in a dilemma where either the dim targets are over-shrinked in the separation or the strong cloud edges remains in the target image. In order to suppress the strong edges while preserving the dim targets, a weighted infrared patch-image (WIPI) model is proposed, incorporating structural prior information into the process of infrared small target and background separation. Instead of adopting a global weight, we allocate adaptive weight to each column of the target patch-image according to its patch structure. Then the proposed WIPI model is converted to a column-wise weighted robust principal component analysis (CWRPCA) problem. In addition, a target unlikelihood coefficient is designed based on the steering kernel, serving as the adaptive weight for each column. Finally, in order to solve the CWPRCA problem, a solution algorithm is developed based on Alternating Direction Method (ADM). Detailed experiment results demonstrate that the proposed method has a significant improvement over the other nine classical or state-of-the-art methods in terms of subjective visual quality, quantitative evaluation indexes and convergence rate.
# Summary. An optional shortened abstract.
summary: 

tags:
- Infrared Small Target
featured: false

# links:
# - name: ""
#   url: ""
url_pdf: https://www.sciencedirect.com/science/article/abs/pii/S1350449516300834

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


