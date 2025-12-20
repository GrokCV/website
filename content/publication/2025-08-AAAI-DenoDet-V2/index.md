---
title: "DenoDet V2: Phase-Amplitude Cross Denoising for SAR Object Detection"

# Authors
# If you created a profile for a user (e.g. the default `admin` user), write the username (folder name) here
# and it will be replaced with their full name and linked to their profile.
authors:
- Kang Ni
- Minrui Zou
- Yuxuan Li
- Xiang Li
- Kehua Guo
- Ming-Ming Cheng
- admin

author_notes:
- Equal Contribution
- Equal Contribution
- 
- 
- 
- 
- "Corresponding Author"

date: "2025-08-12"
doi: ""

# Schedule page publish date (NOT publication's date).
publishDate: ''

# Publication type.
# Accepts a single type but formatted as a YAML list (for Hugo requirements).
# Enter a publication type from the CSL standard.
publication_types: ['paper-conference']

# Publication name and optional abbreviated publication name.
publication: "*Proceedings of the The 40th Annual AAAI Conference on Artificial Intelligence (AAAI)*"
# publication_short: "ICCV 2025"


abstract: |
  One of the primary challenges in Synthetic Aperture Radar (SAR) object detection lies in the pervasive influence of coherent noise. As a common practice, most existing methods, whether handcrafted approaches or deep learning-based methods, employ the analysis or enhancement of object spatial-domain characteristics to achieve implicit denoising. In this paper, we propose DenoDet V2, which explores a completely novel and different perspective to deconstruct and modulate the features in the transform domain via a carefully designed attention architecture. Compared to DenoDet V1, DenoDet V2 is a major advancement that exploits the complementary nature of amplitude and phase information through a band-wise mutual modulation mechanism, which enables a reciprocal enhancement between phase and amplitude spectra. Extensive experiments on various SAR datasets demonstrate the state-of-the-art performance of DenoDet V2. Notably, DenoDet V2 achieves a significant 0.8\% improvement on SARDet-100K dataset compared to DenoDet V1, while reducing the model complexity by half. The code is available at https://github.com/GrokCV/GrokSAR.

# Summary. An optional shortened abstract.
summary: This paper proposes DenoDet V2, a novel SAR object detection model that modulates features in the transform domain via a band-wise mutual modulation mechanism, achieving state-of-the-art performance with significantly reduced complexity.

tags:
- Target Detection
- Ojbect Detection
- SAR

# Display this page in the Featured widget?
featured: false

# Custom links (uncomment lines below)
# links:
# - name: Custom Link
#   url: http://example.org

url_pdf: "https://arxiv.org/pdf/2508.09392"
url_code: "https://github.com/GrokCV/GrokSAR"
url_poster: "https://gitee.com/YimianDai/filebed/raw/master/poster/2026-AAAI-DenoDet-V2-Poster.pdf"
url_project: ""
url_slides: ""
url_source: ""
url_video: ""
url_cn_pdf: "https://gitee.com/YimianDai/filebed/raw/master/translation/2026-AAAI-DenoDet-V2-CN-Translation.pdf"
url_cn_blog: ""
url_cn_video: ""

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


