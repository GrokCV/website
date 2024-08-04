---
title: "Graph-regularized laplace approximation for detecting small infrared target against complex backgrounds"
authors:
- admin
- Fei Zhou
- Yiquan Wu
- Yimian Dai
- Peng Wang
- Kang Ni

author_notes:
- 
-
- "Corresponding author"
-

date: "2019-06-28T00:00:00Z"
doi: ""

# Schedule page publish date (NOT publication's date).
publishDate: "2019-06-28T00:00:00Z"

# Publication type.
# Accepts a single type but formatted as a YAML list (for Hugo requirements).
# Enter a publication type from the CSL standard.
publication_types: ["article-journal"]

# Publication name and optional abbreviated publication name.
publication: "IEEE Access"
publication_short: "Access"

abstract: Against complex background containing the tiny target, high-performance infrared small target detection is always treated as a difficult task. Many low-rank recovery-based methods have shown great potential, but they may suffer from high false or missing alarm when encountering the background with intricate interferences. In this paper, a novel graph-regularized Laplace low-rank approximation detecting model (GRLA) is developed for infrared dim target scenes. Initially, a non-convex Laplace low-rank regularizer instead of the nuclear norm is employed to boost the accuracy of heterogeneous background estimation. Then, to maintain the intrinsic structure between background patch-image, the graph regularization is incorporated in the detecting model.Besides, aiming at reducing the nontarget outliers, a reweighted l1 norm with nonnegative constraint is used. Finally, the proposed model is extended to a generalized framework (G-GRLA) by replacing different non-convex rank functions. With the help of the alternating direction method of multiplier (ADMM), the solution of the proposed model is obtained by an iterative optimization scheme. The experimental results on extensive actual infrared images present the superior performance of our proposed method to compare with the state-of-the-art methods.

# Summary. An optional shortened abstract.
summary: 

tags:
- Small target detection
featured: false

# links:
# - name: ""
#   url: ""
url_pdf: https://ieeexplore.ieee.org/stamp/stamp.jsp?arnumber=8750835


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


