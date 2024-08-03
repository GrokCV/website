---
title: "Robust Infrared Small Target Detection via Jointly Sparse Constraint of l1/2-Metric and Dual-Graph Regularization"
authors:
- admin
- Fei Zhou
- Yiquan Wu
- Yimian Dai
- Kang Ni

author_notes:
- 
date: "2020-06-18T00:00:00Z"
doi: ""

# Schedule page publish date (NOT publication's date).
publishDate: "2020-06-18T00:00:00Z"

# Publication type.
# Accepts a single type but formatted as a YAML list (for Hugo requirements).
# Enter a publication type from the CSL standard.
publication_types: ["article-journal"]

# Publication name and optional abbreviated publication name.
publication: ""
publication_short: "MDPI"

abstract: Small target detection is a critical step in remotely infrared searching and guiding applications. However, previously proposed algorithms would exhibit performance deterioration in the presence of complex background. It is attributed to two main reasons. First, some common background interferences are difficult to eliminate effectively by using conventional sparse measure. Second, most methods only exploit the spatial information typically, but ignore the structural priors across feature space. To address these issues, this paper gives a novel model combining the spatial-feature graph regularization and l1/2-norm sparse constraint. In this model, the spatial and feature regularizations are imposed on the sparse component in the form of graph Laplacians, where the sparse component is enforced as the eigenvectors of their graph Laplacian matrices. Such an approach is to explore the geometric information in both data and feature space simultaneously. Moreover, l1/2-norm acts as a substitute of the traditional l1-norm to constrain the sparse component, further reducing the fake targets. Finally, an efficient optimization algorithm equipped with linearized alternating direction method with adaptive penalty (LADMAP) is carefully designed for model solution. Comprehensive experiments on different infrared scenes substantiate the superiority of the proposed method beyond 11 competitive algorithms in subjective and objective evaluation.

# Summary. An optional shortened abstract.
summary: 

tags:
- Source Themes
featured: false

# links:
# - name: ""
#   url: ""
url_pdf: https://www.mdpi.com/2072-4292/12/12/1963


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

{{% callout note %}}
Click the *Cite* button above to demo the feature to enable visitors to import publication metadata into their reference management software.
{{% /callout %}}

{{% callout note %}}
Create your slides in Markdown - click the *Slides* button to check out the example.
{{% /callout %}}

Add the publication's **full text** or **supplementary notes** here. You can use rich formatting such as including [code, math, and images](https://wowchemy.com/docs/content/writing-markdown-latex/).
