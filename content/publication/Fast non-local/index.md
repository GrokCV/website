---
title: "Fast non-local means algorithm based on Krawtchouk moments"
authors:
- admin
- Yiquan Wu
- Yimian Dai
- Jun Yin
- Jiansheng Wu

author_notes:
- 
-
- 
-

date: "2015-04-01T00:00:00Z"
doi: "https://doi.org/10.1007/s12209-015-2416-x"

# Schedule page publish date (NOT publication's date).
publishDate: "2015-04-01T00:00:00Z"

# Publication type.
# Accepts a single type but formatted as a YAML list (for Hugo requirements).
# Enter a publication type from the CSL standard.
publication_types: ["article-journal"]

# Publication name and optional abbreviated publication name.
publication: "Transactions of Tianjin University"
publication_short: ""

abstract: Non-local means (NLM) method is a state-of-the-art denoising algorithm, which replaces each pixel with a weighted average of all the pixels in the image. However, the huge computational complexity makes it impractical for real applications. Thus, a fast non-local means algorithm based on Krawtchouk moments is proposed to improve the denoising performance and reduce the computing time. Krawtchouk moments of each image patch are calculated and used in the subsequent similarity measure in order to perform a weighted averaging. Instead of computing the Euclidean distance of two image patches, the similarity measure is obtained by low-order Krawtchouk moments, which can reduce a lot of computational complexity. Since Krawtchouk moments can extract local features and have a good antinoise ability, they can classify the useful information out of noise and provide an accurate similarity measure. Detailed experiments demonstrate that the proposed method outperforms the original NLM method and other moment-based methods according to a comprehensive consideration on subjective visual quality, method noise, peak signal to noise ratio (PSNR), structural similarity (SSIM) index and computing time. Most importantly, the proposed method is around 35 times faster than the original NLM method.

# Summary. An optional shortened abstract.
summary: 

tags:
- Denosing
featured: false

# links:
# - name: ""
#   url: ""
url_pdf: https://link.springer.com/article/10.1007/s12209-015-2416-x


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
