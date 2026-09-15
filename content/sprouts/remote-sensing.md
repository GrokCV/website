---
title: 新芽专题介绍（26）：遥感多模态大模型
date: 2025-09-18T01:34:00Z
draft: false
math: true
---


## 研究背景

近年来，以 Transformer 和自监督学习为代表的“大模型”（Foundation Models）范式，彻底改变了自然语言处理领域。这股浪潮正以惊人的速度席卷计算机视觉，推动了“通用感知大模型”的诞生。这些模型通过在海量、多样化的数据上进行预训练，学习到了通用的、可迁移的视觉表征，从而在**无需大量任务专属标注**的情况下，展现出强大的零样本（Zero-shot）和少样本（Few-shot）学习能力。

与此同时，随着空天信息技术的发展，遥感卫星和无人机正以前所未有的规模采集地球观测数据。如何从这些**多模态、大尺度、高维度的遥感数据**中自动、高效地提取有价值的信息，已成为全球性的技术挑战。将通用感知大模型的强大能力与遥感领域的独特需求相结合，构建“遥感感知大模型”，为地球科学、环境监测、城市规划、防灾减灾等应用带来了革命性的机遇。

## 研究意义

通用及遥感感知大模型旨在打破传统视觉任务“一个模型对应一个任务”的壁垒，实现“一模多能”，其研究意义深远：

- **推动人工智能的通用化**：构建能够理解并处理多样化视觉任务的统一模型，是迈向通用人工智能（AGI）的关键一步。
- **革新遥感数据分析范式**：遥感大模型能够自动化解译海量对地观测数据，极大提升了全球尺度环境监测、资源勘探和灾害应急响应的效率。
- **降低AI应用门槛**：强大的零样本/少样本能力，使得用户无需大量标注数据和繁琐的模型训练，即可快速将AI能力应用于特定场景，促进技术普惠。
- **促进前沿技术融合**：该方向是多模态学习、自监督学习、大规模分布式训练等前沿技术的交汇点，为探索下一代AI算法提供了理想的“试验场”。

▲ 遥感大模型能够对全球范围的卫星影像进行高效、自动化的解译和分析。

## 当前挑战

将大模型应用于通用及遥感感知领域，仍然是一项充满挑战的任务：

- **挑战一：数据与算力的“双重壁垒”**

- 大模型的预训练需要亿级甚至十亿级的图像数据和数千卡的并行计算资源，这对大多数研究机构构成了巨大的挑战。
- 高质量、多样化的遥感数据获取、清洗和标注成本极高。

- **挑战二：自然图像与遥感影像的“领域鸿沟”**

- **模态差异**：遥感数据通常包含可见光之外的多个光谱波段（如红外、SAR），且存在巨大的尺度变化，这与自然图像有显著不同。
- **目标特性**：遥感影像中的目标方向任意、尺寸微小且背景极其复杂，通用模型直接应用效果不佳。

- **挑战三：模型泛化与下游任务适配的“最后一公里”**

- 如何设计高效的微调（Fine-tuning）策略，使预训练好的大模型能以低成本、高性能的方式适配多样化的下游任务（如目标检测、语义分割、变化检测等），是核心技术难题。
- 模型的评估和可解释性尚不完善，尤其在决策攸关的遥感应用中，如何确保其可靠性至关重要。

综上，通用及遥感感知大模型是一个方兴未艾、机遇与挑战并存的前沿方向，非常适合有志于探索AI技术边界的学生进行系统性学习和研究。

## 基础资料

- [《动手学深度学习》](https://space.bilibili.com/1567748478/lists/358497?type=series) - 适合中文初学者的深度学习教材
- [《Deep Learning》](https://www.deeplearningbook.org/) - 深度学习入门经典教材
- [《Pattern Recognition and Machine Learning》](https://www.microsoft.com/en-us/research/wp-content/uploads/2006/01/Bishop-Pattern-Recognition-and-Machine-Learning-2006.pdf) - 机器学习原理入门
- [Google Colab](https://colab.research.google.com/) - 免费云平台，不用安装软件，就能跑PyTorch代码
- [Hugging Face](https://huggingface.co/) - 获取预训练模型、数据集和学习教程的开源社区

## 入门文献

- [An Image is Worth 16x16 Words: Transformers for Image Recognition at Scale](https://arxiv.org/pdf/2010.11929) (ICLR 2021)
- [Swin Transformer: Hierarchical Vision Transformer using Shifted Windows](https://arxiv.org/pdf/2103.14030) (ICCV 2021)
- [A convnet for the 2020s](https://openaccess.thecvf.com/content/CVPR2022/papers/Liu_A_ConvNet_for_the_2020s_CVPR_2022_paper.pdf) (CVPR 2022)
- [Segment Anything](https://arxiv.org/pdf/2304.02643) (ICCV 2023)
- [Learning Transferable Visual Models From Natural Language Supervision](https://arxiv.org/pdf/2103.00020) (ICML 2021)
- [Masked Autoencoders Are Scalable Vision Learners](https://arxiv.org/pdf/2111.06377) (CVPR 2022)
- [Momentum Contrast for Unsupervised Visual Representation Learning](https://arxiv.org/pdf/1911.05722) (CVPR 2020)
- [A Simple Framework for Contrastive Learning of Visual Representations](https://arxiv.org/pdf/2002.05709) (ICML 2020)
- [Emerging Properties in Self-Supervised Vision Transformers](https://arxiv.org/pdf/2104.14294) (ICCV 2021)
- [Pre-training of Deep Bidirectional Transformers for Language Understanding](https://arxiv.org/pdf/1810.04805) (NAACL 2019)
- [Exploring plain vision transformer backbones for object detection](https://arxiv.org/pdf/2203.16527) (ECCV 2022)

## 进阶文献

- [Sam 2: Segment anything in images and videos](https://arxiv.org/pdf/2408.00714) (arxiv)
- [DINOv2: Learning Robust Visual Features without Supervision](https://arxiv.org/pdf/2304.07193) (ICCV 2023)
- [DINOv3](https://arxiv.org/pdf/2508.10104) (arxiv)
- [Visual Instruction Pretraining for Domain-Specific Foundation Models](https://arxiv.org/pdf/2509.17562) (arxiv)
- [Visual Instruction Tuning](https://arxiv.org/pdf/2304.08485) (NeurIPS 2023)
- [A New Foundation Model for Computer Vision](https://arxiv.org/pdf/2111.11432) (arxiv)
- [Vision transformer adapter for dense predictions](https://arxiv.org/pdf/2205.08534) (ICLR 2023)
- [Qwen2. 5-vl technical report](https://arxiv.org/pdf/2502.13923) (arxiv)
- [Chain-of-thought prompting elicits reasoning in large language models](https://proceedings.neurips.cc/paper_files/paper/2022/file/9d5609613524ecf4f15af0f7b31abca4-Paper-Conference.pdf) (NeurIPS 2022)
- [LLaVA-CoT: Let Vision Language Models Reason Step-by-Step](https://arxiv.org/pdf/2411.10440) (NeurIPS 2024)
- [Marrying DINO with Grounded Pre-Training for Open-Set Object Detection](https://arxiv.org/pdf/2303.05499) (ICLR 2024)
- [Recognize Anything: A Strong Image Tagging Model](https://arxiv.org/pdf/2306.03514) (ICCV 2023)
- [Exploring Large-Scale Vision Foundation Models with Deformable Convolutions](https://arxiv.org/pdf/2211.05778) (CVPR 2023)
- [Simple Open-Vocabulary Object Detection with Vision Transformers](https://arxiv.org/pdf/2205.06230) (ECCV 2022)
- [Visual-RFT: Visual reinforcement fine-tuning](https://arxiv.org/pdf/2503.01785) (ICCV 2025)

## 相关文献

- [Lsknet: A foundation lightweight backbone for remote sensing](https://arxiv.org/pdf/2403.11735) (IJCV 2025)
- [A Multi-Modal Remote Sensing Foundation Model for Versatile Downstream Tasks ](https://arxiv.org/pdf/2402.06454) (arxiv)
- [A Scale-Aware Masked Autoencoder for Multiscale Geospatial Representation Learning](https://arxiv.org/pdf/2306.13025) (ICCV 2023)
- [SkySense V2: A unified foundation model for multi-modal remote sensing](https://arxiv.org/pdf/2507.13812) (ICCV 2025)
- [MTP: Advancing remote sensing foundation model via multitask pretraining](https://ieeexplore.ieee.org/iel8/4609443/4609444/10547536.pdf) (arxiv)
- [Feature guided masked autoencoder for self-supervised learning in remote sensing](https://ieeexplore.ieee.org/stamp/stamp.jsp?arnumber=10766851) (arxiv)
- [Multimae: Multi-modal multi-task masked autoencoders](https://arxiv.org/pdf/2204.01678) (ECCV 2022)

## 结语

“新芽计划”的初衷是点燃新芽学子对未知探索的热情，并为大家提供一片成长的沃土。通用及遥感感知大模型是当前人工智能领域最激动人心的前沿之一，它既是技术创新的“新高地”，也是解决全球性挑战的“金钥匙”。希望通过这个专题，新芽学子不仅能掌握大模型的核心技术，更能培养出跨领域融合、系统性思考和解决大规模复杂问题的卓越能力。

我们热切期待，在最终的汇报中，能看到大家闪耀着智慧火花的解读与创见！
