---
title: "Brightness segmentation-based plateau histogram equalization algorithm for displaying high dynamic range infrared images"
authors:
- Feifei Zhang
- Yimian Dai
- Xuedian Peng
- Chun Wu
- Xiongyong Zhu
- Ruqi Zhou
- Yilin Wu
  
author_notes:
- 
- "Corresponding Author"
- 
- 
- 
- "Corresponding Author"
date: "2023-11-01T00:00:00Z"
# Enter a publication type from the CSL standard.
publication_types: ["article-journal"]

# Publication name and optional abbreviated publication name.
abstract: Third-generation thermal cameras produce images with high dynamic range (HDR), low contrast, and blurry edges, which makes them difficult to visualize on traditional display devices. Thus, tone mapping methods are required to adapt the recorded signal to the display in order to maintain, and possibly improve, object’s visibility and contrast. Since the traditional global tone mapping methods cannot take account of the trade-off between clearly displaying the details of dark regions and bright regions of the infrared image, this paper proposes a global tone mapping algorithm based on brightness segmentation for the enhancement and display of HDR infrared images. Firstly, the HDR infrared image is divided into different brightness regions in accordance with the characteristics of the human visual system’s ability to perceive brightness. Secondly, the determination of the boundary value of each brightness region is optimized by combining the gray statistics of the HDR infrared image, to achieve the adaptive brightness region segmentation of the infrared image from various scenes. Thirdly, the plateau histogram equalization method is designed to enhance different brightness regions separately, according to their brightness levels. Finally, the enhanced brightness regions are recombined to produce a more visually pleasing output image. The effectiveness of the proposed method is analyzed of HDR infrared images taken from different scenes. A comparison of the proposed method with well-established global tone mapping techniques is provided, along with subjective and objective evaluation methods that demonstrate the potential benefits of this method in enhancing brightness, compressing dynamic range, and improving global contrast.


# Summary. An optional shortened abstract.
summary: 

tags:
- 
featured: false

# links:
# - name: ""
#   url: ""
url_pdf: https://www.sciencedirect.com/science/article/pii/S1350449523003523
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
