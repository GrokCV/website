---
title: "Detection of small target using schatten 1/2 quasi-norm regularization with reweighted sparse enhancement in complex infrared scenes"
authors:
- admin
- Fei Zhou
- Yiquan Wu
- Yimian Dai
- Peng Wang
author_notes:
- 
date: "2019-09-02T00:00:00Z"
doi: ""

# Schedule page publish date (NOT publication's date).
publishDate: ""

# Publication type.
# Accepts a single type but formatted as a YAML list (for Hugo requirements).
# Enter a publication type from the CSL standard.
publication_types: ["article-journal"]

# Publication name and optional abbreviated publication name.
publication: "Remote Sensing"
publication_short: ""

abstract: In uniform infrared scenes with single sparse high-contrast small targets, most existing small target detection algorithms perform well. However, when encountering multiple and/or structurally sparse targets in complex backgrounds, these methods potentially lead to high missing and false alarm rate. In this paper, a novel and robust infrared single-frame small target detection is proposed via an effective integration of Schatten 1/2 quasi-norm regularization and reweighted sparse enhancement (RS1/2NIPI). Initially, to achieve a tighter approximation to the original low-rank regularized assumption, a nonconvex low-rank regularizer termed as Schatten 1/2 quasi-norm (S1/2N) is utilized to replace the traditional convex-relaxed nuclear norm. Then, a reweighted l1 norm with adaptive penalty serving as sparse enhancement strategy is employed in our model for suppressing non-target residuals. Finally, the small target detection task is reformulated as a problem of nonconvex low-rank matrix recovery with sparse reweighting. The resulted model falls into the workable scope of inexact augment Lagrangian algorithm, in which the S1/2N minimization subproblem can be efficiently solved by the designed softening half-thresholding operator. Extensive experimental results on several real infrared scene datasets validate the superiority of the proposed method over the state-of-the-arts with respect to background interference suppression and target extraction.

# Summary. An optional shortened abstract.
summary: 

tags:
- Source Themes
featured: false

# links:
# - name: ""
#   url: ""
url_pdf: https://www.mdpi.com/2072-4292/11/17/2058

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
