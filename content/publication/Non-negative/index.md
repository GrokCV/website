---
title: "Non-negative infrared patch-image model: Robust target-background separation via partial sum minimization of singular values"
authors:
- admin
- Yimian Dai
- Yiquan Wu
- Yu Song
- Jun Guo

author_notes:
- 
-
- "Corresponding author"
-

date: "2017-03-01T00:00:00Z"
doi: ""

# Schedule page publish date (NOT publication's date).
publishDate: "2017-03-01T00:00:00Z"

# Publication type.
# Accepts a single type but formatted as a YAML list (for Hugo requirements).
# Enter a publication type from the CSL standard.
publication_types: ["article-journal"]

# Publication name and optional abbreviated publication name.
publication: "Infrared Physics & Technology"
publication_short: "IPT"

abstract: To further enhance the small targets and suppress the heavy clutters simultaneously, a robust non-negative infrared patch-image model via partial sum minimization of singular values is proposed. First, the intrinsic reason behind the undesirable performance of the state-of-the-art infrared patch-image (IPI) model when facing extremely complex backgrounds is analyzed. We point out that it lies in the mismatching of IPI model’s implicit assumption of a large number of observations with the reality of deficient observations of strong edges. To fix this problem, instead of the nuclear norm, we adopt the partial sum of singular values to constrain the low-rank background patch-image, which could provide a more accurate background estimation and almost eliminate all the salient residuals in the decomposed target image. In addition, considering the fact that the infrared small target is always brighter than its adjacent background, we propose an additional non-negative constraint to the sparse target patch-image, which could not only wipe off more undesirable components ulteriorly but also accelerate the convergence rate. Finally, an algorithm based on inexact augmented Lagrange multiplier method is developed to solve the proposed model. A large number of experiments are conducted demonstrating that the proposed model has a significant improvement over the other nine competitive methods in terms of both clutter suppressing performance and convergence rate.

# Summary. An optional shortened abstract.
summary: 

tags:
- Small target detection
featured: false

# links:
# - name: ""
#   url: ""
url_pdf: https://www.sciencedirect.com/science/article/abs/pii/S1350449516303723


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
