---
title: 新芽专题介绍（31）：多模态大模型的个性化和推理加速
date: 2025-09-17T01:20:00Z
draft: false
math: true
---

## 一、专题介绍

### 1.1 研究背景

随着人工智能从单模态迈向多模态时代，多模态大模型（Multimodal Large Models, MLMs）成为智能感知与理解的核心引擎。它们能够同时处理图像、文本、语音、视频等多源信息，展现出类人般的推理与生成能力。在跨模态检索、智能问答、视觉理解、机器人感知等任务中，MLMs 已经展现出强大的潜力。然而，如何让大模型更好地**适应特定任务或个性化需求**，以及如何**在有限算力环境下高效推理**，成为当前研究与应用中的两大核心问题。因此，本专题围绕“个性化”和“推理加速”两个方面展开，探讨相关方法与前沿技术。

### 1.2 研究意义

1. **个性化（训练侧）**  
   个性化强调如何让多模态大模型适配具体场景或下游任务。例如：  
   * 通过参数高效微调（如 **LoRA、Adapter、Prompt Tuning** 等），快速将通用模型迁移到特定任务；  
   * 利用大模型的知识迁移，提升 **分割、检测、Reasoning感知** 等视觉任务性能；  
   * 探索 **zero-shot、few-shot** 学习能力，使模型在缺乏大规模标注的情况下依旧保持竞争力。  

2. **推理加速（推理侧）**  
   推理加速强调如何降低模型在推理阶段的计算与存储开销。例如：  
   * **剪枝（Pruning）**：去除冗余结构，提高模型稀疏性；  
   * **量化（Quantization）**：将高精度参数压缩为低比特表示，提升速度、降低功耗；  
   * **蒸馏（Distillation）**：用大模型指导小模型训练，获得轻量化替代方案。  

个性化与推理加速分别从训练和推理两个维度切入，是推动多模态大模型走向实际落地的关键。

### 1.3 当前主要挑战

1. **任务与场景多样性**：不同领域对多模态交互的需求差异大，如何设计通用且高效的个性化方案仍是难题。  
2. **大模型计算开销巨大**：数百亿参数的多模态模型在部署和应用中常受限于算力和能耗。  
3. **个性化与高效性的平衡**：如何在保持模型性能的同时，兼顾灵活性与推理效率，是一个需要不断权衡和创新的方向。  

***

## 二、学习资料与参考文献

为了帮助学生更好地进入研究，本专题推荐以下学习材料：

### 2.1 基础教材与学习材料

* [《动手学深度学习》](https://zh.d2l.ai/) —— 深度学习入门教程  
* [《Deep Learning》](https://www.deeplearningbook.org/) —— Ian Goodfellow 等编著  
* [PyTorch 官方教程](https://pytorch.org/tutorials) —— 深度学习框架基础  
* [Transformers 官方文档](https://huggingface.co/docs/transformers) —— 大模型训练与推理工具
* [Google Colab](https://colab.research.google.com/) —— 免费云平台不用安装软件，就能跑PyTorch代码
* [Kaggle平台](https://www.kaggle.com/) —— 竞赛和开源数据集  

### 2.2 入门文献（大模型微调与个性化）

* Deep Residual Learning for Image Recognition (CVPR 2016)
* Densely Connected Convolutional Networks (CVPR 2017)
* CBAM: Convolutional Block Attention Module (ECCV 2018)
* An Image is Worth 16x16 Words: Transformers for Image Recognition at Scale (ICLR 2021)
* P2T: Pyramid Pooling Transformer for Scene Understanding (TPAMI 2022)
* Vision Transformers with Hierarchical Attention (MIR 2024) 
* Exploiting Temporal State Space Sharing for Video Semantic Segmentation (CVPR 2025) 
* Learning Transferable Visual Models From Natural Language Supervision (ICML 2021)
* BLIP: Bootstrapping Language-Image Pre-training for Unified Vision-Language Understanding and Generation (ICML 2022)
* Visual Instruction Tuning (NeurIPS 2023)
* Denoising Diffusion Probabilistic Models (NeurIPS 2020)
* Low-Rank Adaptation of Large Language Models (ICLR 2022)
* Visual Prompt Tuning (ECCV 2022)
* DynamicViT: Efficient Vision Transformers with Dynamic Token Sparsification (NeurIPS 2021)
* Quantized Neural Networks: Training Neural Networks with Low Precision Weights and Activations (JMLR 2018)

### 2.3 进阶文献（推理加速）

* Segment Anything (ICCV 2023)
* SAM 2: Segment Anything in Images and Videos (ICLR 2025)
* RemoteSAM: Towards Segment Anything for Earth Observation (ACM MM 2025)
* PiSSA: Principal Singular Values and Singular Vectors Adaptation of Large Language Models (NeurIPS 2024)
* SVFT: Parameter-Efficient Fine-Tuning with Singular Vectors (NeurIPS 2024)
* DoRA: Weight-Decomposed Low-Rank Adaptation (ICML 2024)
* LISA: Reasoning Segmentation via Large Language Model (CVPR 2024)
* One Token to Seg Them All: Language Instructed Reasoning Segmentation in Videos (NeurIPS 2024)
* GLUS: Global-Local Reasoning Unified into A Single Large Language Model for Video Segmentation (CVPR 2025)
* Multimodality Helps Few-Shot 3D Point Cloud Semantic Segmentation (ICLR 2025)
* Generalized Few-shot 3D Point Cloud Segmentation with Vision-Language Model (CVPR 2025)
* Towards Real Zero-Shot Camouflaged Object Segmentation without Camouflaged Annotations (TPAMI 2025)
* DivPrune: Diversity-based Visual Token Pruning for Large Multimodal Models (CVPR 2025)
* LLaVA-PruMerge: Adaptive Token Reduction for Efficient Large Multimodal Models (ICCV 2025)
* Up or Down? Adaptive Rounding for Post-Training Quantization (ICML 2020)
* OPTQ: Accurate Quantization for Generative Pre-trained Transformers (ICLR 2023)
* DyCoke: Dynamic Compression of Tokens for Fast Video Large Language Models (CVPR 2025)

### 2.4 其他相关文献

> 结合本专题的研究背景，逐渐引导学生进入多模态大模型的个性化和推理加速。学生可在此部分选择进阶文献进行专题汇报，或自行查找最新的同类重要文献。

**多模态大模型**

* Flamingo: A Visual Language Model for Few-Shot Learning (NeurIPS 2022)  
* BLIP-2: Bootstrapping Language-Image Pre-training with Frozen Image Encoders and Large Language Models (ICML 2023)
* InstructBLIP: Towards General-purpose Vision-Language Models with Instruction Tuning (NeurIPS 2023)
* MiniGPT-4: Enhancing Vision-Language Understanding with Advanced Large Language Models (ICLR 2024)
* Language Is Not All You Need: Aligning Perception with Language Models (NeurIPS 2023) 

**大模型微调**

* AdaLoRA: Adaptive Budget Allocation for Parameter-Efficient Fine-Tuning (ICLR 2023)
* Bayesian Low-rank Adaptation for Large Language Models (ICLR 2024)
* SVFit: Parameter-Efficient Fine-Tuning of Large Pre-Trained Models Using Singular Values (arXiv 2024)
* RaSA: Rank-Sharing Low-Rank Adaptation (ICLR 2025)
* QLoRA: Efficient Finetuning of Quantized LLMs (NeurIPS 2023)
* LQ-LoRA: Low-rank plus Quantized Matrix Decomposition for Efficient Language Model Finetuning (ICLR 2024)
* LoftQ: LoRA-Fine-Tuning-aware Quantization for Large Language Models (ICLR 2024)
* Dynamic Low-Rank Sparse Adaptation for Large Language Models (ICLR 2025)

**多模态大模型用于提升下游感知任务**

* DenseCLIP: Language-Guided Dense Prediction with Context-Aware Prompting (CVPR 2022)
* GroupViT: Semantic Segmentation Emerges from Text Supervision (CVPR 2022)
* RegionCLIP: Region-based Language-Image Pretraining (CVPR 2022)
* Grounded Language-Image Pre-training (CVPR 2022)
* VisionLLM: Large Language Model is also an Open-Ended Decoder for Vision-Centric Tasks (NeurIPS 2023)
* InternVL: Scaling up Vision Foundation Models and Aligning for Generic Visual-Linguistic Tasks (CVPR 2024)
* Segment Everything Everywhere All at Once (NeurIPS 2023)
* Grounding DINO: Marrying DINO with Grounded Pre-Training for Open-Set Object Detection (ECCV 2024)
* Learning To Prompt for Open-Vocabulary Object Detection With Vision-Language Model (CVPR 2022)
* Emergent Open-Vocabulary Semantic Segmentation from Off-the-shelf Vision-Language Models (CVPR 2024)

**大模型推理加速**

* BinaryConnect: Training Deep Neural Networks with Binary Weights During Propagations (NeurIPS 2015)
* XNOR-Net: ImageNet Classification Using Binary Convolutional Neural Networks (ECCV 2016)
* Deep Compression: Compressing Deep Neural Networks with Pruning, Trained Quantization and Huffman Coding (ICLR 2016)
* Post Training 4-bit Quantization of Convolutional Networks for Rapid-Deployment (NeurIPS 2019)
* An Image is Worth 1/2 Tokens After Layer 2: Plug-and-Play Inference Acceleration for Large Vision-Language Models (ECCV 2024)
* VoCo-LLaMA: Towards Vision Compression with Large Language Models (CVPR 2025)
* FlashSloth: Lightning Multimodal Large Language Models via Embedded Visual Compression (CVPR 2025)
* Hybrid-Level Instruction Injection for Video Token Compression in Multi-modal Large Language Models (CVPR 2025)
* Boosting Multimodal Large Language Models with Visual Tokens Withdrawal for Rapid Inference (AAAI 2025)
* SPViT: Enabling Faster Vision Transformers via Latency-Aware Soft Token Pruning (ECCV 2022)
* Not All Patches are What You Need: Expediting Vision Transformers via Token Reorganizations (ICLR 2022)
* AdaViT: Adaptive Vision Transformers for Efficient Image Recognition (CVPR 2022)
* Dynamic Token Pruning in Plain Vision Transformers for Semantic Segmentation (ICCV 2023)

***

## 三、结语与期望

多模态大模型的个性化与推理加速，是推动 AI 从实验室走向产业落地的关键一环。本专题旨在让新芽学子深入理解参数高效微调和模型加速的核心思想，并在实践中掌握跨模态感知与优化推理的能力。希望大家能够在未来的汇报中，提出自己的见解，探索更多可能性，为多模态智能的发展贡献力量。
