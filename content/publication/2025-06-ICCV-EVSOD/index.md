---
title: "Event-based Tiny Object Detection: A Benchmark Dataset and Baseline"

authors:
- Nuo Chen
- Chao Xiao
- admin
- Shiman He
- Miao Li
- Wei An

author_notes:
- 
- 
- 
- 
- 
- 

date: "2025-06-30"

publication_types: ["paper-conference"]

publication: "Proceedings of the IEEE/CVF International Conference on Computer Vision (ICCV)"
publication_short: "ICCV"
doi: "10.48550/arXiv.2506.23575"

abstract: |
  Small object detection (SOD) in anti-UAV task is a challenging problem due to the small size of UAVs and complex backgrounds. Traditional frame-based cameras struggle to detect small objects in complex environments due to their low frame rates, limited dynamic range, and data redundancy. Event cameras, with microsecond temporal resolution and high dynamic range, provide a more effective solution for SOD. However, existing event-based object detection datasets are limited in scale, feature large targets size, and lack diverse backgrounds, making them unsuitable for SOD benchmarks. In this paper, we introduce a Event-based Small object detection (EVSOD) dataset (namely EV-UAV), the first large-scale, highly diverse benchmark for anti-UAV tasks. It includes 147 sequences with over 2.3 million event-level annotations, featuring extremely small targets (averaging 6.8×5.4 pixels) and diverse scenarios such as urban clutter and extreme lighting conditions. Furthermore, based on the observation that small moving targets form continuous curves in spatiotemporal event point clouds, we propose Event based Sparse Segmentation Network (EV-SpSegNet), a novel baseline for event segmentation in point cloud space, along with a Spatiotemporal Correlation (STC) loss that leverages motion continuity to guide the network in retaining target events. Extensive experiments on the EV-UAV dataset demonstrate the superiority of our method and provide a benchmark for future research in EVSOD. The dataset and code are at https://github.com/ChenYichen9527/Ev-UAV.

summary: This paper introduces EV-UAV, the first large-scale event-based small object detection dataset for anti-UAV tasks, and proposes EV-SpSegNet as a novel baseline.

tags:
- Event-based Detection
- Small Object Detection
- Anti-UAV
- Deep Learning
- EVSOD

featured: false

url_pdf: "https://arxiv.org/pdf/2506.23575"
url_code: "https://github.com/ChenYichen9527/Ev-UAV"
url_dataset: "https://github.com/ChenYichen9527/Ev-UAV"
url_poster: ""
url_project: ""
url_slides: ""
url_source: ""
url_video: ""
url_cn_pdf: ""
url_cn_blog: ""
url_cn_video: ""

image:
  preview_only: false
--- 