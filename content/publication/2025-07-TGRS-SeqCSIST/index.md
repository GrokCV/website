---
title: "SeqCSIST: Sequential Closely-Spaced Infrared Small Target Unmixing"

authors:
- Ximeng Zhai
- Bohan Xu
- Yaohong Chen
- Hao Wang
- Kehua Guo
- admin

author_notes:
- 
- 
- Corresponding Author
- 
- 
- Corresponding Author

date: "2025-07-14T00:00:00Z"
doi: "10.1109/TGRS.2025.3588753"

# Schedule page publish date (NOT publication's date).
publishDate: "2025-07-14T00:00:00Z"

publication_types: ["article-journal"]

publication: "*IEEE Transactions on Geoscience and Remote Sensing*, vol. 63, pp. 1-15, 2025."
# publication_short: "IEEE TGRS"
# pages: "1-15"
# publisher: "IEEE"
# doi: "10.1109/TGRS.2025.3588753"

abstract: |
  Due to the limitation of the optical lens focal length and the resolution of the infrared detector, distant Closely-Spaced Infrared Small Target (CSIST) groups typically appear as mixing spots in the infrared image. In this paper, we propose a novel task, Sequential CSIST Unmixing, namely detecting all targets in the form of sub-pixel localization from a highly dense CSIST group. However, achieving such precise detection is an extremely difficult challenge. In addition, the lack of high-quality public datasets has also restricted the research progress. To this end, firstly, we contribute an open-source ecosystem, including SeqCSIST, a sequential benchmark dataset, and a toolkit that provides objective evaluation metrics for this special task, along with the implementation of 23 relevant methods. Furthermore, we propose the Deformable Refinement Network (DeRefNet), a model-driven deep learning framework that introduces a Temporal Deformable Feature Alignment (TDFA) module enabling adaptive inter-frame information aggregation. To the best of our knowledge, this work is the first endeavor to address the CSIST Unmixing task within a multi-frame paradigm. Experiments on the SeqCSIST dataset demonstrate that our method outperforms the state-of-the-art approaches with mean Average Precision (mAP) metric improved by 5.3%. Our dataset and toolkit are available from https://github.com/GrokCV/SeqCSIST.

summary: This paper proposes SeqCSIST, a new task and benchmark for sequential closely-spaced infrared small target unmixing, and introduces DeRefNet for adaptive inter-frame information aggregation.

tags:
- Infrared Small Target Detection
- Deep Learning
- SeqCSIST
- DeRefNet

featured: false

url_pdf: "https://arxiv.org/pdf/2507.09556"
url_code: "https://github.com/GrokCV/SeqCSIST"
url_dataset: "https://github.com/GrokCV/SeqCSIST"
url_poster: ""
url_project: ""
url_slides: ""
url_source: ""
url_video: ""
url_cn_pdf: "https://github.com/YimianDai/public/blob/master/translation/2025-TGRS-SeqCSIST-CN-Translation.pdf"
url_cn_blog: "https://grokcv.ai/blog/seqcsist/"
url_cn_video: ""

image:
  preview_only: false
--- 