---
title: 新芽专题介绍：增量目标检测
date: 2025-09-17T01:13:00Z
draft: true
math: true
---

## 一、专题介绍

### 1.1 研究背景

在现实应用场景中，目标检测模型常常面临 **类别不断扩展** 和 **域不断变化** 的双重挑战。例如，自动驾驶不仅需要识别新的交通标志和车辆类别，还需适应雨天、夜晚、雾天等多样环境；安防监控系统需要学习新的异常行为类别，同时适配不同摄像头和光照条件下的数据分布；卫星遥感既要检测新的地物类别，又需迁移至不同地区或分辨率的卫星影像。

传统目标检测方法通常依赖 **在所有类别或全量数据上统一训练**，一旦出现新类别或新域，就必须重新训练模型，带来高昂的计算成本和存储开销。同时，出于数据隐私保护的考虑，旧数据往往难以获取。

为应对这一问题，研究者提出了 **增量目标检测（Incremental Object Detection, IOD）**。其核心目标是：在保留已有检测能力的前提下，能够逐步学习新类别或新域，避免灾难性遗忘，同时尽可能减少对旧数据的依赖。

### 1.2 研究意义

增量目标检测不仅是深度学习与计算机视觉中的前沿研究方向，也具有显著的应用价值：

1. **实际需求驱动**：智能系统需要持续适应环境中出现的新目标类别或新域，具备动态扩展能力。
2. **降低存储成本**：无需保存大量旧数据，从而减轻数据存储和传输压力。
3. **延长模型寿命**：通过持续学习，检测模型能够不断更新和优化，避免过时。
4. **跨领域融合**：增量检测涉及持续学习、知识蒸馏、少样本学习等多个研究领域，是人工智能的交叉热点。

因此，研究增量目标检测对于推动人工智能向 **开放世界感知** 发展具有重要意义。

### 1.3 当前主要挑战

增量目标检测仍然处于快速发展阶段，面临以下挑战：

1. **灾难性遗忘问题**

   * 新类别训练容易覆盖旧类别知识，导致旧类别检测精度急剧下降。
   * 如何在有限旧数据甚至无旧数据的条件下保持历史性能，是研究的核心难题。

2. **正负样本混淆**

   * 新类别的目标区域可能与旧类别存在重叠或相似，容易被错误标注为背景或负样本。
   * 如何设计合理的样本选择与伪标注机制，是提升增量检测精度的关键。

3. **存储与计算限制**

   * 保存全部旧数据代价过高，不符合现实条件约束。
   * 需要结合 **知识蒸馏、样本选择、特征记忆** 等方法实现轻量化增量学习。

4. **评价与基准数据集不足**

   * 现有的目标检测数据集（如 COCO、VOC）并非为增量学习设计，缺乏统一的实验协议和评价指标。
   * 公平比较与标准化评测体系仍需进一步建立。

---

## 二、学习资料与参考文献

为了帮助新芽学子快速入门，本专题的学习结构可分为以下三个层次。

---

### 2.1 基础教材与学习材料

在进入增量目标检测之前，需要先掌握 **深度学习与目标检测的基本方法**。推荐的学习资料包括：

* 李沐[《动手学深度学习》](https://zh.d2l.ai/)——适合中文初学者的深度学习教材，以及[课程系列视频](https://space.bilibili.com/1567748478/lists/358497?type=series)
* [《Deep Learning》](https://www.deeplearningbook.org/)（Ian Goodfellow 等）——深度学习入门经典教材
* [PyTorch 官方教程](https://pytorch.org/tutorials)，也可以使用 [PyTorch 中文文档](https://pytorch-cn.readthedocs.io/zh/latest/)
* [《Pattern Recognition and Machine Learning》](https://www.microsoft.com/en-us/research/wp-content/uploads/2006/01/Bishop-Pattern-Recognition-and-Machine-Learning-2006.pdf)（Christopher M. Bishop）——机器学习原理入门（难度不小）
* [MMDetection 文档](https://mmdetection.readthedocs.io/) —— 开源检测框架，支持 Faster R-CNN、YOLO、DETR 等方法，模块化设计便于研究增量检测。
* [Detectron2](https://github.com/facebookresearch/detectron2) —— Facebook AI 开发的检测与分割框架，适合快速实验。

---

### 2.2 入门文献（目标检测与持续学习经典方法）

> 学生第一阶段的阅读训练，可帮助理解目标检测、持续学习这一通用方向。**仅用于入门，不可选择此部分文献汇报**。



* [R-CNN](https://www.cv-foundation.org/openaccess/content_cvpr_2014/papers/Girshick_Rich_Feature_Hierarchies_2014_CVPR_paper.pdf): Rich Feature Hierarchies for Accurate Object Detection and Semantic Segmentation（CVPR 2014）
* [Fast R-CNN](https://www.cv-foundation.org/openaccess/content_iccv_2015/papers/Girshick_Fast_R-CNN_ICCV_2015_paper.pdf): Fast R-CNN（ICCV 2015）
* [Faster R-CNN](https://proceedings.neurips.cc/paper_files/paper/2015/file/14bfa6bb14875e45bba028a21ed38046-Paper.pdf): Towards Real-Time Object Detection with Region Proposal Networks (NeurIPS 2015）
* [RetinaNet](https://openaccess.thecvf.com/content_ICCV_2017/papers/Lin_Focal_Loss_for_ICCV_2017_paper.pdf): Focal Loss for Dense Object Detection（ICCV 2017）
* [Mask R-CNN](https://openaccess.thecvf.com/content_ICCV_2017/papers/He_Mask_R-CNN_ICCV_2017_paper.pdf): Mask R-CNN（ICCV 2017）
* [FCOS](https://openaccess.thecvf.com/content_ICCV_2019/papers/Tian_FCOS_Fully_Convolutional_One-Stage_Object_Detection_ICCV_2019_paper.pdf): FCOS: Fully Convolutional One-Stage Object Detection（ICCV 2019）
* [DETR](https://link.springer.com/content/pdf/10.1007/978-3-030-58452-8.pdf): End-to-End Object Detection with Transformers（ECCV 2020）
* [Deformable-DETR](https://arxiv.org/abs/2010.04159): Deformable Transformers for End-to-End Object Detection（ICLR 2021）
* [EWC](https://www.pnas.org/doi/epdf/10.1073/pnas.1611835114): Overcoming catastrophic forgetting in neural networks（PNAS 2017）
* [LwF](https://ieeexplore.ieee.org/stamp/stamp.jsp?tp=&arnumber=8107520): Learning without forgetting（TPAMI 2017）
* [iCaRL](https://openaccess.thecvf.com/content_cvpr_2017/papers/Rebuffi_iCaRL_Incremental_Classifier_CVPR_2017_paper.pdf): Incremental Classifier and Representation Learning（CVPR 2017）
* [EER](https://proceedings.neurips.cc/paper_files/paper/2019/file/fa7cdfad1a5aaf8370ebeda47a1ff1c3-Paper.pdf): Efficient Experience Replay for Continual Learning（NeurIPS 2019）
* [DEN](https://arxiv.org/abs/1708.01547): Lifelong Learning with Dynamically Expandable Networks（ICLR 2018）

---

### 2.3 进阶文献（目标检测与持续学习前沿研究）
> 学生可在此部分选择进阶文献进行专题汇报，或自行查找最新的同类重要文献。

* [Deformable-DETR](https://arxiv.org/abs/2010.04159): Deformable Transformers for End-to-End Object Detection（ICLR 2021）
* [Sparse R-CNN](https://arxiv.org/pdf/2011.12450): End-to-End Object Detection with Learnable Proposals (CVPR 2021)**
* [Cascade R-CNN](https://arxiv.org/pdf/1712.00726): Delving into High Quality Object Detection (CVPR 2018)
* [ATSS](https://arxiv.org/pdf/1912.02424): Bridging the Gap Between Anchor-based and Anchor-free Detection via Adaptive Training Sample Selection (CVPR 2020)
* [YOLOX](https://arxiv.org/pdf/2107.08430): Exceeding YOLO Series in 2021 (ArXiv 2021)
* [DAB-DETR](https://arxiv.org/pdf/2201.12329): Dynamic Anchor Boxes are Better Queries for DETR (ICLR 2022)
* [DINO](https://arxiv.org/pdf/2203.03605): DETR with Improved DeNoising Anchor Boxes for End-to-End Object Detection (ICLR 2023)
* [DiffusionDet](https://arxiv.org/pdf/2211.09788): Diffusion Model for Object Detection (ICCV 2023)
* [RT-DETR](https://arxiv.org/pdf/2304.08069): DETRs Beat YOLOs on Real-time Object Detection (CVPR 2024)
* [CO-DETR](https://arxiv.org/pdf/2211.12860): DETRs with Collaborative Hybrid Assignments Training (ICCV 2023)
* [L2P](https://arxiv.org/abs/2112.08654): Learning to Prompt for Continual Learning (NeurIPS 2022)
* [DER](https://proceedings.neurips.cc/paper/2020/file/b704ea2c39778f07c617f6b7ce480e9e-Paper.pdf): Dark Experience for General Continual Learning (NeurIPS 2021)
* [Foster](https://arxiv.org/abs/2204.04662): Feature Boosting and Compression for Continual Learning (ICLR 2022)
* [DyTox](https://arxiv.org/abs/2111.11326): Transformers for Continual Learning with Dynamic Token Expansion (CVPR 2022)
* [CODA-Prompt](https://openaccess.thecvf.com/content/CVPR2023/papers/Smith_CODA-Prompt_COntinual_Decomposed_Attention-Based_Prompting_for_Rehearsal-Free_Continual_Learning_CVPR_2023_paper.pdf): Continual Decomposed Attention-based Prompting for Task-Incremental Learning (NeurIPS 2022)
* [Beyond Prompt Learning](https://arxiv.org/abs/2407.10281):  Continual Adapter for Efficient Rehearsal-Free Continual Learning (ECCV 2024)

---

### 2.4  增量目标检测领域相关文献

> 结合本专题的研究背景，逐渐引导学生进入增量目标检测。学生可在此部分选择进阶文献进行专题汇报，或自行查找最新的同类重要文献。
>


* [ILOD](https://openaccess.thecvf.com/content_ICCV_2017/papers/Shmelkov_Incremental_Learning_of_ICCV_2017_paper.pdf): Incremental Learning of Object Detectors without Catastrophic Forgetting（ICCV 2017）
* [Wanderlust](https://openaccess.thecvf.com/content/ICCV2021/papers/Wang_Wanderlust_Online_Continual_Object_Detection_in_the_Real_World_ICCV_2021_paper.pdf): Wanderlust: Online Continual Object Detection in the Real World（ICCV 2021）
* [IncDet](https://ieeexplore.ieee.org/document/9127478): IncDet: In Defense of Elastic Weight Consolidation for Incremental Object Detection（TNNLS 2020）
* [iOD](https://ieeexplore.ieee.org/document/9599446): Incremental Object Detection via Meta-Learning（TPAMI 2021）
* [BNC](https://arxiv.org/abs/2106.01847): Bridging Non Co-occurrence with Unlabeled In-the-wild Data for Incremental Object Detection（NeurIPS 2021）
* [RD-IOD](https://dl.acm.org/doi/10.1145/3472393): RD-IOD: Two-Level Residual-Distillation-Based Triple-Network for Incremental Object Detection（TOMM 2022）
* [MVCD](https://www.sciencedirect.com/science/article/pii/S0031320322003442): Multi-View Correlation Distillation for Incremental Object Detection（PR 2022）
* [ROSETTA](https://openaccess.thecvf.com/content/CVPR2022/papers/Yang_Continual_Object_Detection_via_Prototypical_Task_Correlation_Guided_Gating_Mechanism_CVPR_2022_paper.pdf): Continual Object Detection via Prototypical Task Correlation Guided Gating Mechanism（CVPR 2022）
* [ERD](https://openaccess.thecvf.com/content/CVPR2022/papers/Feng_Overcoming_Catastrophic_Forgetting_in_Incremental_Object_Detection_via_Elastic_Response_CVPR_2022_paper.pdf): Overcoming Catastrophic Forgetting in Incremental Object Detection via Elastic Response Distillation（CVPR 2022）
* [Incremental-DETR](https://ojs.aaai.org/index.php/AAAI/article/download/25129/24901): Incremental-DETR: Incremental Few-Shot Object Detection via Self-Supervised Learning（AAAI 2023）
* [OSR](https://ojs.aaai.org/index.php/AAAI/article/view/25417): One-Shot Replay: Boosting Incremental Object Detection via Retrospecting One Object（AAAI 2023）
* [CL-DETR](https://openaccess.thecvf.com/content/CVPR2023/papers/Liu_Continual_Detection_Transformer_for_Incremental_Object_Detection_CVPR_2023_paper.pdf): Continual Detection Transformer for Incremental Object Detection（CVPR 2023）
* [ACF](https://openaccess.thecvf.com/content/ICCV2023/papers/Kang_Alleviating_Catastrophic_Forgetting_of_Incremental_Object_Detection_via_Within-Class_and_ICCV_2023_paper.pdf): Alleviating Catastrophic Forgetting of Incremental Object Detection via Within-Class and Between-Class Knowledge Distillation（ICCV 2023）
* [ABR](https://openaccess.thecvf.com/content/ICCV2023/papers/Liu_Augmented_Box_Replay_Overcoming_Foreground_Shift_for_Incremental_Object_Detection_ICCV_2023_paper.pdf): Augmented Box Replay: Overcoming Foreground Shift for Incremental Object Detection（ICCV 2023）
* [Efficient-CLS](https://openaccess.thecvf.com/content/ICCV2023/papers/Wu_Label-Efficient_Online_Continual_Object_Detection_in_Streaming_Video_ICCV_2023_paper.pdf): Label-Efficient Online Continual Object Detection in Streaming Video（ICCV 2023）
* [PseudoRM](https://dl.acm.org/doi/pdf/10.1145/3581783.3611952): Pseudo Object Replay and Mining for Incremental Object Detection（MM 2023）
* [CIOD](https://www.sciencedirect.com/science/article/pii/S0031320323001887): Class-incremental Object Detection（PR 2023）
* [TP-DIOD](https://ieeexplore.ieee.org/document/10148995): Domain Incremental Object Detection Based on Feature Space Topology Preserving Strategy（TCSVT 2023）
* [TALIR](https://ojs.aaai.org/index.php/AAAI/article/view/28537): Learning Task-Aware Language-Image Representation for Class-Incremental Object Detection（AAAI 2024）
* [LDB](https://ojs.aaai.org/index.php/AAAI/article/view/29427): Non-exemplar Domain Incremental Object Detection via Learning Domain Bias（AAAI 2024）
* [PD](https://dlnext.acm.org/doi/pdf/10.1145/3664647.3681031): Purified Distillation: Bridging Domain Shift and Category Gap in Incremental Object Detection（MM 2024）
* [ZiRa](https://papers.nips.cc/paper_files/paper/2024/file/f6f4b34d255c2c6c2391af975bed0428-Paper-Conference.pdf): Zero-shot Generalizable Incremental Learning for Vision-Language Object Detection（NeurIPS 2024）
* [MD-DETR](https://arxiv.org/abs/2405.XXXX): Preventing Catastrophic Forgetting through Memory Networks in Continuous Detection（ECCV 2024）
* [BPF](https://link.springer.com/chapter/10.1007/978-3-031-72907-2_26): Bridge Past and Future: Overcoming Information Asymmetry in Incremental Object Detection（ECCV 2024）
* [SDDGR](https://openaccess.thecvf.com/content/CVPR2024/papers/Kim_SDDGR_Stable_Diffusion-based_Deep_Generative_Replay_for_Class_Incremental_Object_CVPR_2024_paper.pdf): SDDGR: Stable Diffusion-based Deep Generative Replay for Class Incremental Object Detection（CVPR 2024）
* [TNC](https://link.springer.com/article/10.1007/s11263-024-02048-0): Towards Non Co-occurrence Incremental Object Detection with Unlabeled In-the-Wild Data（IJCV 2024）
* [LRE](https://ieeexplore.ieee.org/stamp/stamp.jsp?tp=&arnumber=10886990): Replay-Based Incremental Object Detection With Local Response Exploration（TMM 2025）
* [DCA](https://ojs.aaai.org/index.php/AAAI/article/view/33068/35223): DCA: Dividing and Conquering Amnesia in Incremental Object Detection（AAAI 2025）
* [GCD](https://ojs.aaai.org/index.php/AAAI/article/view/32864): GCD: Advancing Vision-Language Models for Incremental Object Detection via Global Alignment and Correspondence Distillation（AAAI 2025）
* [GMDP](https://openreview.net/forum?id=6T8czSBWce): High-dimension Prototype is a Better Incremental Object Detection Learner（ICLR 2025）
* [PseDet](https://openreview.net/forum?id=Iu8FVcUmVp): PseDet: Revisiting the Power of Pseudo Label in Incremental Object Detection（ICLR 2025）
* [NSGP-RePRE](https://openreview.net/forum?id=PFdWf0H4V2): Demystifying Catastrophic Forgetting in Two-Stage Incremental Object Detector（ICML 2025）
* [RGR](https://openaccess.thecvf.com/content/CVPR2025/papers/Zhang_Revisiting_Generative_Replay_for_Class_Incremental_Object_Detection_CVPR_2025_paper.pdf): Revisiting Generative Replay for Class Incremental Object Detection（CVPR 2025）
* [SOYO](https://openaccess.thecvf.com/content/CVPR2025/papers/Wang_Boosting_Domain_Incremental_Learning_Selecting_the_Optimal_Parameters_is_All_CVPR_2025_paper.pdf): Boosting Domain Incremental Learning: Selecting the Optimal Parameters is All You Need（CVPR 2025）
* [LEA](https://openaccess.thecvf.com/content/CVPR2025/papers/Song_Learning_Endogenous_Attention_for_Incremental_Object_Detection_CVPR_2025_paper.pdf): Learning Endogenous Attention for Incremental Object Detection（CVPR 2025）

这些文献涵盖了从 **蒸馏方法、样本选择、记忆回放到任务适配** 等多方面的研究策略。

---

## 三、结语与期望

增量目标检测是人工智能迈向 **开放世界感知** 的关键一环。它不仅在学术研究上充满挑战，也在实际应用中有着广阔前景。本专题旨在帮助新芽学子理解其背景、挑战与研究价值，逐步进入这一前沿领域。

我们期待在最终的汇报中，看到大家结合所学知识，提出独立见解与创新思路！

