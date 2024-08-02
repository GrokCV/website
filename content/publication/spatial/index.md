---
title: "Infrared small target detection via incorporating spatial structural prior into intrinsic tensor sparsity regularization"
authors:
- admin
- Fei Zhou
- Yiquan Wu
- Yimian Dai
  
author_notes:
- 
- "Corresponding Author"
- 
- 
- 
- "Corresponding Author"
date: "2021-04-01T00:00:00Z"
# Enter a publication type from the CSL standard.
publication_types: ["article-journal"]

# Publication name and optional abbreviated publication name.
abstract: Infrared small target detection is a crucial stage in many searching and tracking applications. Many tensor decomposition-based methods have achieved well performance in the scenes with uniform backgrounds and salient targets. However, the performance is potentially prone to be degraded when encountering highly complex scenes. It is mainly because the decomposition error caused by the sparse edge structures and imprecise tensor rank measures make the recovered background deviate from the real one. To mitigate these issues, we introduce an infrared sequence tensor decomposition-based method, which combines an intrinsic tensor rank measure (ITRM) and spatial structure prior to improve background recovery. With the inter-frame background correlation, ITRM is used to regularize the low-rank component of the observed tensor, which encodes the intrinsic tensor rank insights delivered by two most typical tensor decompositions to finely rectify the estimation bias of the tensor rank. To further suppress edge structures during the decomposition, we design a spatial descriptor with edge awareness by using a nonlocal structure tensor to delineate intra-frame structural edge. Furthermore, an adaptive indicator, which fuses spatial edge information and sparsity enhancing weight, is employed to replace the inflexibly and globally sparse penalty. The solution of the proposed model is addressed by an alternative direction minimization of multipliers (ADMM). Extensive experiments on real-world infrared sequences demonstrate the outperformance of the proposed method against other state-of-the-art ones, both quantitatively and qualitatively.


# Summary. An optional shortened abstract.
summary: 

tags:
- 
featured: false

# links:
# - name: ""
#   url: ""
url_pdf: https://www.sciencedirect.com/science/article/pii/S1051200421000051
url_code: ''
url_dataset: ''
url_poster: ''
url_project: ''
url_slides: ''
url_source: ''
url_video: ''

# Featured image
# To use, add an image named `featured.jpg/png` to your page's folder. 
image:
  # caption: 'Image credit: [**Unsplash**](https://unsplash.com/photos/jdD8gXaTZsc)'
  # focal_point: ""
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
# slides: example
---
