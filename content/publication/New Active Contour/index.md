---
title: "A new active contour remote sensing river image segmentation algorithm inspired from the cross entropy"
authors:
- admin
- Yu Song
- Yiquan Wu
- Yimian Dai

author_notes:
- 
-
- 
-

date: "2016-01-01T00:00:00Z"
doi: ""

# Schedule page publish date (NOT publication's date).
publishDate: "2016-01-01T00:00:00Z"

# Publication type.
# Accepts a single type but formatted as a YAML list (for Hugo requirements).
# Enter a publication type from the CSL standard.
publication_types: ["article-journal"]

# Publication name and optional abbreviated publication name.
publication: "Digital Signal Processing"
publication_short: "DSP"

abstract: The CV (Chan–Vese) model is a piecewise constant approximation of the Mumford and Shah model. It assumes that the original image can be segmented into two regions such that each region can be represented as constant grayscale value. In fact, the objective functional of the CV model actually finds a segmentation of the image such that the within-class variance is minimized. This is equivalent to the Otsu image thresholding algorithm which also aims to minimize the within-class variance. Similarly to the Otsu image thresholding algorithm, cross entropy is another widely used image thresholding algorithm and it finds a segmentation such that the cross entropy of the segmented image and the original image is minimized. Inspired from the cross entropy, a new active contour image segmentation algorithm is proposed. The region term in the new objective functional is the integral of the logarithm of the ratio between the grayscale of the original image and the mean value computed from the segmented image weighted by the grayscale of the original image. The new objective functional can be solved by the level set evolution method. A distance regularized term is added to the level set evolution equation so the level set need not be reinitialized periodically. A fast global minimization algorithm of the objective functional is also proposed which incorporates the edge term originated from the geodesic active contour model. Experimental results show that, the algorithm proposed can segment images more accurately than the CV model and the implementation speed of the fast global minimization algorithm is fast.

# Summary. An optional shortened abstract.
summary: 

tags:
- CV
featured: false

# links:
# - name: ""
#   url: ""
url_pdf: https://www.sciencedirect.com/science/article/abs/pii/S1051200415003048


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
