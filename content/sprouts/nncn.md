---
title: 新芽专题介绍：神经网络压缩与加速
date: 2025-09-17T01:23:00Z
draft: false
math: true
---

> 此专题由非南开大学老师发布，选修南开大学 2025 秋《人工智能实践课-初级》课程的同学请勿选择此专题。非本课程选修同学可自由选择。

## 一、专题介绍

### 1.1  研究背景

“如何实现低功耗人工智能”是2023年中国科协发布的10大年度问题之一，模型轻量化是实现低功耗人工智能的重要手段，旨在精度损失量可接受的前提下，将高参数量、高浮点运算需求的模型通过剪枝、蒸馏、量化等方式转化为低参数量、低浮点运算量的等价模型，从而降低功耗，提升推理速度，在蓬勃发展的具身智能、低轨星网卫星、大规模无人车/无人机集群等领域应用扮演重要角色。

### 1.2  研究意义

神经网络压缩与加速的研究具有极其重要的现实意义和战略价值，主要体现：

1. **推动产业落地**：模型轻量化将成为边缘AI落地的关键技术支撑。通过优化模型结构，促进AI技术在边缘计算设备（如无人机、卫星、物联网终端）的部署，解决传统模型因算力和存储限制难以落地的痛点。

2. **降低算力成本负担**：大型模型训练和推理需海量算力资源，轻量化技术可减少云计算中心能耗，降低AI应用门槛。

3. **技术推动**：模型压缩技术能够使大型网络在资源受限平台高效运行，实现“云-边-端”协同计算架构。



### 1.3  当前主要挑战

尽管方向重要，但实现神经网络压缩仍然面临多重挑战：

1. **挑战一：精度与效率平衡难**

   * 大幅压缩往往伴随信息损失，易在复杂任务中模型性能显著下降。

   * 非结构化稀疏在通用硬件加速效果不稳定，而结构化稀疏往往以更高的精度代价换取。

   * 蒸馏、剪枝、量化等组合测量的协同效应复杂，缺乏统一的理论框架。

2. **挑战二：跨平台异构性挑战**

   * 硬件生态多样，缺乏统一的压缩框架在各平台实现稳健加速。

   * 编译器与框架的支持鸿沟导致优化难以落地，缺乏端到端和自动化的部署工具链。

3. **挑战三：系统级整合和评测管理不足**

   * 缺乏统一且可重复的基准与评测体系，难以对比不同压缩策略的实际效益。

   * 端到端部署链路复杂，需要稳定的工具链支持和协作整合。

   * 在模型压缩过程中，易造成隐私数据迁移而导致泄露，对安全性提出更高要求。

综上，神经网络压缩与加速技术仍在探索和突破阶段，这是连接软件算法和智能硬件的中间桥梁：既能接触实际需求，又能跟随前沿探索研究。

***

## 二、学习资料与参考文献

为了引导新芽学子逐步进入研究，本专题结构分为以下四部分：

***

### 2.1  基础教材与学习材料

在开始探险之前，你需要掌握一些基础的“内功心法”，这些是后续一切学习的基石。以下是你可以使用的一些**书籍/教程**：

* 李沐[《动手学深度学习》](https://zh.d2l.ai/)——适合中文初学者的深度学习教材，以及[课程系列视频](https://space.bilibili.com/1567748478/lists/358497?type=series)

* [《Deep Learning》](https://www.deeplearningbook.org/)（Ian Goodfellow 等）——深度学习入门经典教材

* [PyTorch 官方教程](https://pytorch.org/tutorials)，也可以使用 [PyTorch 中文文档](https://pytorch-cn.readthedocs.io/zh/latest/)

* [《Pattern Recognition and Machine Learning》](https://www.microsoft.com/en-us/research/wp-content/uploads/2006/01/Bishop-Pattern-Recognition-and-Machine-Learning-2006.pdf)（Christopher M. Bishop）——机器学习原理入门（难度不小）

此外，你也可以使用一些**入门工具**：

* [Google Colab](https://colab.research.google.com/)：免费云平台，不用安装软件，就能跑PyTorch代码。

* [Kaggle平台](https://www.kaggle.com/)：免费数据集和竞赛

Tips：务必**摆脱所有基础都打好后，再进行下一阶段学习的心态**，在干中学，遇到不明白的再回溯补基础。

***

### 2.2  入门文献（神经网络压缩与加速经典方法）

> 学生第一阶段的阅读训练，可帮助理解神经网络压缩与加速的经典方法。

* **[Data-free](https://arxiv.org/abs/1507.06149): Data-free parameter pruning for deep neural networks (BMCV 2015)**

* **[SSL](https://arxiv.org/abs/1608.03665): Learning Structured Sparsity in Deep Neural Networks (NeurIPS 2016）**

* **[L1-Norm](https://arxiv.org/abs/1608.08710): Pruning Filters for Efficient ConvNets (arXiv 2016)**

* **[BNScale](https://arxiv.org/pdf/2005.12872): Learning Efficient Convolutional Networks Through Network Slimming (ICCV 2017)**

* [](https://arxiv.org/abs/1707.06168v2): Channel Pruning for Accelerating Very Deep Neural Networks (ICCV 2017)

* [APG](https://arxiv.org/pdf/2006.04388):Data-driven sparse structure selection for deep neural networks (ECCV 2018)

* [FPGM](https://openaccess.thecvf.com/content_CVPR_2019/papers/He_Filter_Pruning_via_Geometric_Median_for_Deep_Convolutional_Neural_Networks_CVPR_2019_paper.pdf): Keypoint Triplets for Object Detection (CVPR 2019)

* [Online](https://ieeexplore.ieee.org/abstract/document/8451123): Online Filter Clustering and Pruning for Efficient Convnets (ICIP 2018)

* [taylor](https://openaccess.thecvf.com/content_CVPR_2019/papers/Molchanov_Importance_Estimation_for_Neural_Network_Pruning_CVPR_2019_paper.pdf): Importance Estimation for Neural Network Pruning (CVPR 2019)

* [LAMP](https://arxiv.org/pdf/1808.01244v2): Layer-adaptive Sparsity for the Magnitude-based Pruning (ICLR 2021)

* [CURL](https://arxiv.org/pdf/1612.03144v2): Neural Network Pruning With Residual-Connections and Limited-Data (CVPR 2020)

* [DCN](https://arxiv.org/pdf/1703.06211v3): Learning Efficient Image Super-Resolution Networks via Structure-Regularized Pruning (ICCV 2017)

* [Metapruning](https://openaccess.thecvf.com/content_ICCV_2019/papers/Liu_MetaPruning_Meta_Learning_for_Automatic_Neural_Network_Channel_Pruning_ICCV_2019_paper.pdf): Meta learning for automatic neural network channel pruning (ICCV 2019)


* [KD](https://arxiv.org/abs/1503.02531): Distilling the Knowledge in a Neural Network (NIPS 2014)

* [OBKD](https://proceedings.neurips.cc/paper_files/paper/2017/file/e1e32e235eee1f970470a3a6658dfdd5-Paper.pdf): Learning efficient object detection models with knowledge distillation (NIPS 2017)

* [KT](https://arxiv.org/abs/1707.01219): Like What You Like: Knowledge Distill via Neuron Selectivity Transfer (NIPS 2017)

* [SSKD](https://link.springer.com/chapter/10.1007/978-3-030-58545-7_34): Knowledge distillation meets self-supervision (ECCV 2020)

* [RKD](https://openaccess.thecvf.com/content_CVPR_2019/papers/Park_Relational_Knowledge_Distillation_CVPR_2019_paper.pdf): Relational knowledge distillation (CVPR 2019)

* [CCKD](https://openaccess.thecvf.com/content_ICCV_2019/papers/Peng_Correlation_Congruence_for_Knowledge_Distillation_ICCV_2019_paper.pdf): Correlation congruence for knowledge distillation (ICCV 2019)

* [Binarized neural networks](Binarized neural networks:): Training deep neural networks with weights and activations constrained to+ 1 or-1 (ML 2016)

* [XNOR-Net](https://link.springer.com/chapter/10.1007/978-3-319-46493-0_32): ImageNet Classification Using Binary Convolutional Neural Networks (ECCV 2016)

* [Dorefa-net](Dorefa-net: Training low bitwidth convolutional neural networks with low bitwidth gradients): Training low bitwidth convolutional neural networks with low bitwidth gradients (NEC 2016)**

* [SSQ](https://arxiv.org/abs/1902.08153): Learned step size quantization (ML 2019)


***

### 2.3  进阶文献（神经网络压缩与加速前沿方法）

> 学生可在此部分选择进阶文献进行专题汇报。

* **[GCN](https://link.springer.com/article/10.1007/s10489-021-02802-8): Graph pruning for model compression (Springer 2022)**

* **[DepGraph](https://openaccess.thecvf.com/content/CVPR2023/papers/Fang_DepGraph_Towards_Any_Structural_Pruning_CVPR_2023_paper.pdf): Towards Any Structural Pruning (CVPR 2023)**

* **[Sparse R-CNN](https://arxiv.org/pdf/2011.12450): End-to-End Object Detection with Learnable Proposals (CVPR 2021)**

* [SRP](https://arxiv.org/pdf/1712.00726): LEARNING EFFICIENT IMAGE SUPER-RESOLUTION NETWORKS VIA STRUCTURE-REGULARIZED PRUNING (ICLR 2022)

* [MGD](https://link.springer.com/chapter/10.1007/978-3-031-20083-0_4): Masked generative distillation (ECCV 2022)

* [PKD](https://proceedings.neurips.cc/paper_files/paper/2022/file/631ad9ae3174bf4d6c0f6fdca77335a4-Paper-Conference.pdf): General distillation framework for object detectors via Pearson correlation coefficient (NIPS 2022)

* [CrossKD](https://openaccess.thecvf.com/content/CVPR2024/papers/Wang_CrossKD_Cross-Head_Knowledge_Distillation_for_Object_Detection_CVPR_2024_paper.pdf): Cross-head knowledge distillation for object detection (CVPR 2024)

* [LLT](https://arxiv.org/pdf/1909.06720): Learnable lookup table for neural network quantization (CVPR 2022)

* [EQV](https://ojs.aaai.org/index.php/AAAI/article/view/30108): Towards Efficient Verification of Quantized Neural Networks (AAAI 2024)

* [IGQ-ViT](https://openaccess.thecvf.com/content/CVPR2024/papers/Moon_Instance-Aware_Group_Quantization_for_Vision_Transformers_CVPR_2024_paper.pdf): Instance-Aware Group Quantization for Vision Transformers (CVPR 2024)

* [GPTVQ](https://arxiv.org/abs/2402.15319): The Blessing of Dimensionality for LLM Quantization (ML 2024)


***

### 2.4  弱小目标检测模型压缩与加速方法

> 结合本专题的研究背景，逐渐引导学生进入红外弱小目标检测模型压缩与加速方法。
>
> 红外弱小目标检测模型压缩与加速可分为剪枝、知识蒸馏、量化手段。

**剪枝方法**

1. **[Irprunedet](https://ojs.aaai.org/index.php/AAAI/article/view/28551)：Efficient Infrared small target detection via wavelet structure regularized soft channel pruning.（AAAI 2024）**

2. **[IRPruneDeXt](https://ieeexplore.ieee.org/abstract/document/11134487)：Efficient Infrared Small Target Detection via Musical Wavelet-Regularized Channel Pruning（TNNLS 2025）**

3. **[SAGCP](https://ieeexplore.ieee.org/abstract/document/10900537)：Sparsity-Aware Global Channel Pruning for Infrared Small-Target Detection Networks（TGRS 2025）**


**知识蒸馏**

1. **[KDD](https://arxiv.org/pdf/2409.12448v1)：An Efficient Knowledge Distillation-Based Detection Method for Infrared Small Targets（RS 2024）**

2. **[ST-KDNet](https://link.springer.com/chapter/10.1007/978-981-19-9968-0_11)：A Saliency-Transformer Combined Knowledge Distillation Guided Network for Infrared Small Target Detection（ICSINC 2022）**

3. **[IRKD](https://ieeexplore.ieee.org/abstract/document/10445437)：Feature-based knowledge distillation for infrared small target detection（GRSL 2022）**

4. **[SAM](https://dl.acm.org/doi/abs/10.1145/3664647.3680609)：Unleashing the Power of Generic Segmentation Model: A Simple Baseline for Infrared Small Target Detection（ACM MM'24）**

5. **[MM-IRSTD](https://www.mdpi.com/2072-4292/16/21/3937)：Conv Self-Attention-Based Multi-Modal Small and Dim Target Detection in Infrared Dual-Band Images（RS 2024）**


**量化**

1. **[SPMix-Q](https://ieeexplore.ieee.org/abstract/document/10379193): Mixed-Precision Network Quantization for Infrared Small Target Segmentation (TGRS 2023)**

2. **[BiisNet](https://arxiv.org/abs/2503.02662): 10K is Enough: An Ultra-Lightweight Binarized Network for Infrared Small-Target Detection (arXiv 2025)**

3. **[ILN-SSR](https://www.mdpi.com/2072-4292/16/21/4018): Improved Logarithmic Norm and Sparse Structure Refinement for Infrared Small Target Detection (RS 2024)**


***

## 三、结语与期望

“新芽计划”的初衷是点燃新芽学子对未知探索的热情，并为大家提供一片成长的沃土。红外弱小目标检测是一个充满挑战与机遇的领域，它既是国家需求的“硬骨头”，也是学术创新的“试金石”。希望通过这个专题，新芽学子不仅能学到前沿的 AI 知识，更能培养出独立思考、动手实践和解决复杂问题的能力。

我们热切期待，在最终的汇报中，能看到大家闪耀着智慧火花的解读与创见！
