---
title: DISTA-Net：动态空间邻近红外小目标解混
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
abstract: 在红外成像中，密集成团的空间邻近小目标解混存在严峻的技术挑战，因为信号混叠会严重影响目标数量统计、亚像素级定位以及辐射强度测定的准确性。尽管深度学习在红外小目标检测领域取得了一定的进展，但其在空间邻近红外小目标上的应用尚未得到探索。这一空白主要源于混叠特征分离的复杂性以及开源基础设施的缺失。在本研究中，我们提出了动态迭代收缩阈值网络 (Dynamic Iterative Shrinkage Thresholding Network, DISTA-Net)，该网络将传统稀疏重建方法重构为动态框架。DISTA-Net 能自适应地生成卷积权重和阈值参数，以实时调整重建过程。据我们所知，DISTA-Net 是首个专门针对空间邻近红外小目标解混设计的深度学习模型，实现了卓越的亚像素检测精度。此外，我们建立了该领域首个开源生态系统以促进后续研究。该生态系统包含三大核心组件：（1）CSIST-100K，一个公开的基准数据集；（2）CSO-mAP，一个用于亚像素检测的自定义专用评估指标；（3）GrokCSO，一个开源工具包，其中包含 DISTA-Net 及其他模型。


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

