---
title: "Reweighted infrared patch-tensor model with both nonlocal and local priors for single-frame small target detection"
authors:
- admin
- Yimian Dai
- Yiquan Wu
author_notes:
- 
date: "2017-05-23T00:00:00Z"
doi: ""

# Schedule page publish date (NOT publication's date).
publishDate: "2017-05-23T00:00:00Z"

# Publication type.
# Accepts a single type but formatted as a YAML list (for Hugo requirements).
# Enter a publication type from the CSL standard.
publication_types: ["article-journal"]

# Publication name and optional abbreviated publication name.
publication: "IEEE journal of selected topics in applied earth observations and remote sensing"


abstract: Many state-of-the-art methods have been proposed for infrared small target detection. They work well on the images with homogeneous backgrounds and high-contrast targets. However, when facing highly heterogeneous backgrounds, they would not perform very well, mainly due to: 1) the existence of strong edges and other interfering components, 2) not utilizing the priors fully. Inspired by this, we propose a novel method to exploit both local and nonlocal priors simultaneously. First, we employ a new infrared patch-tensor (IPT) model to represent the image and preserve its spatial correlations. Exploiting the target sparse prior and background nonlocal self-correlation prior, the target-background separation is modeled as a robust low-rank tensor recovery problem. Moreover, with the help of the structure tensor and reweighted idea, we design an entrywise local-structure-adaptive and sparsity enhancing weight to replace the globally constant weighting parameter. The decomposition could be achieved via the element-wise reweighted higher-order robust principal component analysis with an additional convergence condition according to the practical situation of target detection. Extensive experiments demonstrate that our model outperforms the other state-of-the-arts, in particular for the images with very dim targets and heavy clutters.


# Summary. An optional shortened abstract.
summary:  Many state-of-the-art methods have been proposed for infrared small target detection. Inspired by this, we propose a novel method to exploit both local and non-local priors simultaneously. 

tags:
- Infrared Small Target Detection
featured: false

# links:
# - name: ""
#   url: ""
url_pdf: https://arxiv.org/pdf/1703.09157


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

