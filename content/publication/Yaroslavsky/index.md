---
title: "Improved preprocessed Yaroslavsky filter based on shearlet features"
authors:
- admin
- Yiquan Wu
- Yimian Dai
- Jiansheng Wu
author_notes:
- 
date: "2016-00-00T00:00:00Z"
doi: "10.15918/j.jbit1004-0579.201625.0120"

# Schedule page publish date (NOT publication's date).
publishDate: "2016-00-00T00:00:00Z"

# Publication type.
# Accepts a single type but formatted as a YAML list (for Hugo requirements).
# Enter a publication type from the CSL standard.
publication_types: ["article-journal"]

# Publication name and optional abbreviated publication name.
publication: "Journal of Beijing Institute of Technology"
publication_short: "BJUT"

abstract: An improved preprocessed Yaroslavsky filter (IPYF) is proposed to avoid the nick effects and obtain a better denoising result when the noise variance is unknown. Different from its predecessors, the similarity between two pixels is calculated by shearlet features. The feature vector consists of initial denoised results by the non-subsampled shearlet transform hard thresholding (NSST-HT) and NSST coefficients, which can help allocate the averaging weights more reasonably. With the correct estimated noise variance, the NSST-HT can provide good denoised results as the initial estimation and high-frequency coefficients contribute large weights to preserve textures. In case of the incorrect estimated noise variance, the low-frequency coefficients will mitigate the nick effect in cartoon regions greatly, making the IPYF more robust than the original PYF. Detailed experimental results show that the IPYF is a very competitive method based on a comprehensive consideration involving peak signal to noise ratio (PSNR), computing time, visual quality and method noise.

# Summary. An optional shortened abstract.
summary: 

tags:
- image processing
- image denoising
featured: false

# links:
# - name: ""
#   url: ""
url_pdf: https://journal.bit.edu.cn/jbit/en/article/pdf/preview/10.15918/j.jbit1004-0579.201625.0120.pdf

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

