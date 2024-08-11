---
title: "Background Semantics Matter: Cross-Task Feature Exchange Network for Clustered Infrared Small Target Detection With Sky-Annotated Dataset"
authors:
- admin
- Yimian Dai
- Mengxuan Xiao
- Yiming Zhu
- Huan Wang
- Kehua Guo
- Jian Yang


date: "2024-07-29T00:00:00Z"
# Schedule page publish date (NOT publication's date).
publishDate: "2017-01-01T00:00:00Z"

# Publication type.
# Accepts a single type but formatted as a YAML list (for Hugo requirements).
# Enter a publication type from the CSL standard.
publication_types: ["article"]

# Publication name and optional abbreviated publication name.
publication: ""
publication_short: ""

abstract: Infrared small target detection poses unique challenges due to the scarcity of intrinsic target features and the abundance of similar background distractors. We argue that background semantics play a pivotal role in distinguishing visually similar objects for this task. To address this, we introduce a new task -- clustered infrared small target detection, and present DenseSIRST, a novel benchmark dataset that provides per-pixel semantic annotations for background regions, enabling the transition from sparse to dense target detection. Leveraging this dataset, we propose the Background-Aware Feature Exchange Network (BAFE-Net), which transforms the detection paradigm from a single task focused on the foreground to a multi-task architecture that jointly performs target detection and background semantic segmentation. BAFE-Net introduces a cross-task feature hard-exchange mechanism to embed target and background semantics between the two tasks. Furthermore, we propose the Background-Aware Gaussian Copy-Paste (BAG-CP) method, which selectively pastes small targets into sky regions during training, avoiding the creation of false alarm targets in complex non-sky backgrounds. Extensive experiments validate the effectiveness of BAG-CP and BAFE-Net in improving target detection accuracy while reducing false alarms. The DenseSIRST dataset, code, and trained models are available at https://github.com/GrokCV/BAFE-Net.


# Summary. An optional shortened abstract.
summary: 

tags:
- Infrared Small Target Detection
featured: false

# links:
# - name: ""
#   url: ""
url_pdf: https://arxiv.org/pdf/2407.20078
url_code: 'https://github.com/GrokCV/BAFE-Net'
url_dataset: ''
url_poster: ''
url_project: ''
url_slides: ''
url_source: ''
url_video: ''

# Featured image
# To use, add an image named `featured.jpg/png` to your page's folder. 
image:
  caption: 'Image credit: [**Unsplash**](https://unsplash.com/photos/s9CC2SKySJM)'
  focal_point: ""
  preview_only: false

# Associated Projects (optional).
#   Associate this publication with one or more of your projects.
#   Simply enter your project's folder or file name without extension.
#   E.g. `internal-project` references `content/project/internal-project/index.md`.
#   Otherwise, set `projects: []`.
projects:
- internal-project

# Slides (optional).
#   Associate this publication with Markdown slides.
#   Simply enter your slide deck's filename without extension.
#   E.g. `slides: "example"` references `content/slides/example/index.md`.
#   Otherwise, set `slides: ""`.
slides: example
---
