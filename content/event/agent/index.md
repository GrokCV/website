---
title: 【新芽（大一）结业汇报】变化检测：从特征融合到 Agent 智能体

event: GrokCV Seminar
event_url: https://space.bilibili.com/833564

location: Virtual
# address:
#   street: 450 Serra Mall
#   city: Stanford
#   region: CA
#   postcode: '94305'
#   country: United States

summary: 红外弱小目标检测的 SOTA 方法，也是 PRCV 2024、ICPR 2024 Track 1、ICPR 2024 Track 2 三项比赛优胜方案的 Baseline
abstract: Infrared small target detection (IRSTD) has recently benefitted greatly from U-shaped neural models. However, largely overlooking effective global information modeling, existing techniques struggle when the target has high similarities with the background. We present a Spatial-channel Cross Transformer Network (SCTransNet) that leverages spatial-channel cross transformer blocks (SCTBs) on top of long-range skip connections to address the aforementioned challenge. In the proposed SCTBs, the outputs of all encoders are interacted with cross transformer to generate mixed features, which are redistributed to all decoders to effectively reinforce semantic differences between the target and clutter at full scales. Specifically, SCTB contains the following two key elements, (a) spatial-embedded single-head channel-cross attention (SSCA) for exchanging local spatial features and full-level global channel information to eliminate ambiguity among the encoders and facilitate high-level semantic associations of the images, and (b) a complementary feed-forward network (CFN) for enhancing the feature discriminability via a multi-scale strategy and cross-spatial-channel information interaction to promote beneficial information transfer. Our SCTransNet effectively encodes the semantic differences between targets and backgrounds to boost its internal representation for detecting small infrared targets accurately. Extensive experiments on three public datasets, NUDT-SIRST, NUAA-SIRST, and IRSTD-1k, demonstrate that the proposed SCTransNet outperforms existing IRSTD methods. Our code will be made public at <https://github.com/xdFai>.

# Talk start and end times.
#   End time can optionally be hidden by prefixing the line with `#`.
date: '2024-07-13T18:32:00Z'
date_end: '2024-07-13T19:00:00Z'
all_day: false

# Schedule page publish date (NOT talk date).
publishDate: '2024-07-13T18:32:00Z'

authors: []
tags: []

# Is this a featured talk? (true/false)
featured: false

image:
  # caption: 'Image credit: [**Unsplash**](https://unsplash.com/photos/bzdhc5b3Bxs)'
  # focal_point: Right

links:
  - icon: youtube
    icon_pack: fab
    name: Follow
    url: https://www.bilibili.com/video/BV1kr421M7wx/
url_code: 'https://github.com/xdFai'
url_pdf: 'https://arxiv.org/pdf/2401.15583'
url_slides: 'https://github.com/GrokCV/Slides/blob/master/ShuaiYuan/SCTransNet-Slides.pdf'
url_video: 'https://www.bilibili.com/video/BV1Gf421z7Ed/?share_source=copy_web&vd_source=0cff7c155de885f3bea907819b93a04e'

# Markdown Slides (optional).
#   Associate this talk with Markdown slides.
#   Simply enter your slide deck's filename without extension.
#   E.g. `slides = "example-slides"` references `content/slides/example-slides.md`.
#   Otherwise, set `slides = ""`.
#   slides: "https://github.com/GrokCV/Slides/blob/master/Yimian/2023-11-03-HADAR-Slides.pdf"

# Projects (optional).
#   Associate this post with one or more of your projects.
#   Simply enter your project's folder or file name without extension.
#   E.g. `projects = ["internal-project"]` references `content/project/deep-learning/index.md`.
#   Otherwise, set `projects = []`.
#   projects:
#   - example
---
