---
title: "AuxDet: Auxiliary Metadata Matters for Omni-Domain Infrared Small Target Detection"

authors:
- Yangting Shi
- Renjie He
- Le Hui
- Xiang Li
- Jian Yang
- Ming-Ming Cheng
- admin

author_notes:
- 
- Corresponding Author
- 
- 
- 
- 
- Corresponding Author

date: "2025-05-21"

publication_types: ["preprint"]

publication: "arXiv preprint arXiv:2505.15184"
publication_short: "arXiv"
doi: "10.48550/arXiv.2505.15184"

abstract: |
  Omni-domain infrared small target detection (IRSTD) poses formidable challenges, as a single model must seamlessly adapt to diverse imaging systems, varying resolutions, and multiple spectral bands simultaneously. Current approaches predominantly rely on visual-only modeling paradigms that not only struggle with complex background interference and inherently scarce target features, but also exhibit limited generalization capabilities across complex omni-scene environments where significant domain shifts and appearance variations occur. In this work, we reveal a critical oversight in existing paradigms: the neglect of readily available auxiliary metadata describing imaging parameters and acquisition conditions, such as spectral bands, sensor platforms, resolution, and observation perspectives. To address this limitation, we propose the Auxiliary Metadata Driven Infrared Small Target Detector (AuxDet), a novel multi-modal framework that fundamentally reimagines the IRSTD paradigm by incorporating textual metadata for scene-aware optimization. Through a high-dimensional fusion module based on multi-layer perceptrons (MLPs), AuxDet dynamically integrates metadata semantics with visual features, guiding adaptive representation learning for each individual sample. Additionally, we design a lightweight prior-initialized enhancement module using 1D convolutional blocks to further refine fused features and recover fine-grained target cues. Extensive experiments on the challenging WideIRSTD-Full benchmark demonstrate that AuxDet consistently outperforms state-of-the-art methods, validating the critical role of auxiliary information in improving robustness and accuracy in omni-domain IRSTD tasks. Code is available at https://github.com/GrokCV/AuxDet.

summary: This paper proposes AuxDet, a multi-modal IRSTD framework that leverages auxiliary metadata for robust omni-domain infrared small target detection.

tags:
- Infrared Small Target Detection
- Metadata Fusion
- Omni-Domain
- Deep Learning
- AuxDet

featured: false

url_pdf: "https://arxiv.org/pdf/2505.15184"
url_code: "https://github.com/GrokCV/AuxDet"
url_dataset: ""
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