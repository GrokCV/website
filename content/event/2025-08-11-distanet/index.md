---
title: DISTA-Net：动态紧密排列红外小目标分离网络
draft: false
event: GrokCV Seminar
event_url: https://www.bilibili.com/video/BV1d8tPzxESh/?spm_id_from=333.337.search-card.all.click

location: Tencent Meeting
# address:
#   street: 450 Serra Mall
#   city: Stanford
#   region: CA
#   postcode: '94305'
#   country: United States

summary: 【工作分享】DISTA-Net：动态紧密排列红外小目标分离网络
abstract: 在红外成像中，解析密集集群中的紧密排列小目标是一个重大挑战，因为重叠信号阻碍了对其数量、亚像素位置和辐射强度的精确确定。虽然深度学习已经推进了红外小目标检测领域，但其在紧密排列红外小目标上的应用尚未被探索。这个空白主要存在于分离叠加特征的复杂性和缺乏开源基础设施。在这项工作中，我们提出了动态迭代收缩阈值网络（DISTA-Net），它在动态框架内重新概念化了传统的稀疏重建。DISTA-Net自适应地生成卷积权重和阈值参数，以实时定制重建过程。据我们所知，DISTA-Net是第一个专门为紧密排列红外小目标分离设计的深度学习模型，实现了卓越的亚像素检测精度。此外，我们建立了第一个开源生态系统来促进该领域的进一步研究。这个生态系统包含三个关键组件：(1) CSIST-100K，一个公开可用的基准数据集；(2) CSO-mAP，一个用于亚像素检测的自定义评估指标；(3) GrokCSO，一个包含DISTA-Net和其他模型的开源工具包。

# Talk start and end times.
#   End time can optionally be hidden by prefixing the line with `#`.
date: '2025-08-06T20:00:00Z'
#date_end: '2025-08-11T21:00:00Z'
all_day: false

# Schedule page publish date (NOT talk date).
publishDate: '2025-08-06T20:00:00Z'

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
    url: https://www.bilibili.com/video/BV1d8tPzxESh/?spm_id_from=333.337.search-card.all.click
url_code: 'https://github.com/GrokCV/GrokCSO'
url_pdf: 'https://arxiv.org/abs/2505.19148'
url_slides: 'https://github.com/GrokCV/Slides/blob/master/Shengdong/DISTA-Net%E6%8E%A8%E5%B9%BF.pdf'
url_video: 'https://www.bilibili.com/video/BV1d8tPzxESh/?spm_id_from=333.337.search-card.all.click'

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

