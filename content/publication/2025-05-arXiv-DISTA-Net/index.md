---
title: "DISTA-Net: Dynamic Closely-Spaced Infrared Small Target Unmixing"

# Authors
# If you created a profile for a user (e.g. the default `admin` user), write the username (folder name) here
# and it will be replaced with their full name and linked to their profile.
authors:
- Shengdong Han
- Shangdong Yang
- Yuxuan Li
- Xin Zhang
- Xiang Li
- Jian Yang
- Ming-Ming Cheng
- admin

author_notes:
- Equal Contribution
- Equal Contribution
- 
- 
- 
- 
- 
- "Corresponding Author"

date: "2025-05-25"
doi: "10.48550/arXiv.2505.19148"

# Schedule page publish date (NOT publication's date).
publishDate: '2025-05-15T00:00:00Z'

# Publication type.
# Accepts a single type but formatted as a YAML list (for Hugo requirements).
# Enter a publication type from the CSL standard.
publication_types: ['paper-conference']

# Publication name and optional abbreviated publication name.
publication: "2025 International Conference on Computer Vision (ICCV)"
publication_short: "ICCV 2025"


abstract: |
  Resolving closely-spaced small targets in dense clusters presents a significant challenge in infrared imaging, as the overlapping signals hinder precise determination of their quantity, sub-pixel positions, and radiation intensities. While deep learning has advanced the field of infrared small target detection, its application to closely-spaced infrared small targets has not yet been explored. This gap exists primarily due to the complexity of separating superimposed characteristics and the lack of an open-source infrastructure. In this work, we propose the Dynamic Iterative Shrinkage Thresholding Network (DISTA-Net), which reconceptualizes traditional sparse reconstruction within a dynamic framework. DISTA-Net adaptively generates convolution weights and thresholding parameters to tailor the reconstruction process in real time. To the best of our knowledge, DISTA-Net is the first deep learning model designed specifically for the unmixing of closely-spaced infrared small targets, achieving superior sub-pixel detection accuracy. Moreover, we have established the first open-source ecosystem to foster further research in this field. This ecosystem comprises three key components: (1) CSIST-100K, a publicly available benchmark dataset; (2) CSO-mAP, a custom evaluation metric for sub-pixel detection; and (3) GrokCSO, an open-source toolkit featuring DISTA-Net and other models. Our code and dataset are available at https://github.com/GrokCV/GrokCSO.

# Summary. An optional shortened abstract.
summary: This paper proposes DISTA-Net, the first deep learning model for unmixing closely-spaced infrared small targets, and introduces an open-source ecosystem for this field.

tags:
- Closely-Spaced Infrared Small Targets Unmixing
- Infrared Small Target Detection
- Sparse Reconstruction
- Deep Learning
- Sub-Pixel Detection

# Display this page in the Featured widget?
featured: false

# Custom links (uncomment lines below)
# links:
# - name: Custom Link
#   url: http://example.org

url_pdf: "https://arxiv.org/pdf/2505.19148"
url_code: "https://github.com/GrokCV/GrokCSO"
url_dataset: "https://github.com/GrokCV/GrokCSO"
url_poster: ""
url_project: ""
url_slides: ""
url_source: ""
url_video: ""
url_cn_pdf: "https://github.com/YimianDai/public/blob/master/translation/2025-ICCV-DISTA-Net-CN-Translation.pdf"
url_cn_blog: "https://grokcv.ai/blog/dista-net/"
url_cn_video: "https://www.bilibili.com/video/BV1d8tPzxESh/"

# Featured image
# To use, add an image named `featured.jpg/png` to your page's folder.
image:
  # caption: 'Image credit: [**Unsplash**](https://unsplash.com/photos/pLCdAaMFLTE)'
  # focal_point: ''
  preview_only: false

# Associated Projects (optional).
#   Associate this publication with one or more of your projects.
#   Simply enter your project's folder or file name without extension.
#   E.g. `internal-project` references `content/project/internal-project/index.md`.
#   Otherwise, set `projects: []`.
# projects:
#   - example

# Slides (optional).
#   Associate this publication with Markdown slides.
#   Simply enter your slide deck's filename without extension.
#   E.g. `slides: "example"` references `content/slides/example/index.md`.
#   Otherwise, set `slides: ""`.
# slides: example
---


