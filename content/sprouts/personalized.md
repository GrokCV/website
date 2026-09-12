---
title: 新芽专题介绍（10）：多模态大模型及其个性化
date: 2025-09-18T01:50:00Z
draft: false
math: true
---

## 一、专题介绍

### 1.1 研究背景

随着人工智能由单一模态处理迈向多模态协同理解，多模态大模型（Multimodal Large Language Models，MLLMs）正在成为连接图像、文本和视频等多源信息的重要技术基础。通过视觉编码器、跨模态连接模块和大语言模型的协同，多模态大模型能够完成图像描述、视觉问答、跨模态检索、目标定位、图像分割和视频理解等任务，并展现出较强的知识迁移与推理能力。

然而，通用多模态大模型主要依赖大规模开放数据训练，其知识分布、回答方式和任务能力不一定与具体用户或专业场景一致。例如，在遥感、工业检测、医学影像等领域，模型需要理解专业类别、行业术语和特定任务要求；不同用户也可能对输出内容、表达风格和交互方式有不同需求。因此，如何以较低的数据和计算成本，使通用多模态大模型适配特定领域、任务或用户，是大模型研究与应用中的重要问题。

本专题围绕“多模态大模型及其个性化”展开，以多模态模型的基本结构和跨模态对齐机制为基础，重点学习参数高效微调、提示学习、少样本学习和领域知识增强等技术，探索通用模型向具体任务和个性化需求迁移的方法。

### 1.2 研究意义

1. **理解多模态大模型的基本原理**  
   学习视觉编码器、大语言模型、跨模态连接模块和指令微调等核心组成，理解图像与文本等不同模态如何被表示、对齐和联合推理。

2. **掌握低成本个性化方法**  
   通过 LoRA、Adapter、Prompt Tuning 等参数高效微调方法，仅更新少量参数即可使模型适配新任务，降低完整微调带来的显存、时间和存储开销。

3. **提升少样本条件下的任务适应能力**  
   探索 zero-shot、few-shot、检索增强和知识迁移等方法，使模型在标注数据有限的情况下仍能适应专业场景。

4. **服务具体视觉感知任务**  
   将多模态大模型的语言知识和推理能力用于分类、检测、分割、变化理解等下游任务，增强传统视觉模型对开放类别、复杂指令和专业语义的理解能力。

5. **培养本科生的科研实践能力**  
   通过文献阅读、模型复现、实验对比和方法改进，使学生形成从提出问题、设计实验到分析结果和撰写报告的基本科研能力。

### 1.3 当前主要挑战

1. **跨模态语义对齐困难**：图像、文本和视频具有不同的数据结构与信息密度，如何实现细粒度、稳定且可解释的跨模态对齐仍是难点。
2. **专业数据数量有限**：领域数据往往规模较小、标注成本较高，容易导致模型过拟合或无法充分学习专业知识。
3. **个性化与通用能力存在冲突**：模型适配特定任务后，可能出现原有知识遗忘、跨任务泛化能力下降等问题。
4. **方法选择与参数配置复杂**：不同适配层、模块插入位置、LoRA 秩值以及训练数据配比都会影响个性化效果，需要建立规范的对比与分析方法。
5. **评价体系尚不统一**：除任务精度外，还需要综合评价训练参数量、显存占用、数据需求、迁移能力和模型原有能力保持程度。

---

## 二、主要学习内容与研究方向

### 2.1 基础知识学习

学生首先学习深度学习、卷积神经网络、Transformer 和视觉 Transformer 的基本原理，掌握 PyTorch 的基本使用方法；随后了解 CLIP、BLIP、LLaVA 等代表性视觉语言模型，熟悉多模态大模型从视觉特征提取、跨模态映射到语言生成的基本流程。

### 2.2 多模态大模型实践

选择具有公开代码和模型权重的多模态大模型，在开源数据集上完成环境配置与推理测试，观察不同图像、问题和提示词对模型输出的影响。学生应能够分析模型的数据流、主要模块和输入输出形式，并建立可重复的实验基线。

### 2.3 参数高效微调与个性化

围绕特定领域或任务构建小规模训练与测试数据，重点学习并比较以下方法：

- **低秩适配**：LoRA、AdaLoRA、DoRA、PiSSA 等；
- **轻量适配模块**：Adapter、跨模态 Adapter；
- **提示学习**：Prompt Tuning、Visual Prompt Tuning、软提示学习；
- **少样本与知识增强**：上下文学习、检索增强、类别或属性知识提示；
- **任务适配**：将多模态知识用于视觉问答、分类、检测、分割或其他感知任务。

### 2.4 建议研究切入点

学生可根据兴趣和基础，从下列方向中选择一个开展研究：

1. 面向遥感、工业检测或其他专业场景的多模态大模型 LoRA 微调；
2. LoRA、Adapter 与 Prompt Tuning 的性能、参数量和训练成本对比；
3. 面向少样本视觉任务的类别描述、属性提示或视觉提示设计；
4. 面向不同任务或不同用户的动态低秩分配与模块组合；
5. 利用多模态大模型辅助开放词汇分类、检测或分割；
6. 个性化微调后的通用能力保持与灾难性遗忘分析。

---

## 三、学习资料与参考文献

### 3.1 基础教材与工具

- [《动手学深度学习》](https://zh.d2l.ai/)——深度学习入门教程
- [PyTorch 官方教程](https://pytorch.org/tutorials)——深度学习框架基础
- [Transformers 官方文档](https://huggingface.co/docs/transformers)——大模型训练与推理工具
- [PEFT 官方文档](https://huggingface.co/docs/peft)——参数高效微调工具
- [Google Colab](https://colab.research.google.com/)——在线实验环境
- [Kaggle](https://www.kaggle.com/)——开源数据集与实践平台

### 3.2 多模态大模型基础文献

- An Image is Worth 16x16 Words: Transformers for Image Recognition at Scale (ICLR 2021)
- Learning Transferable Visual Models from Natural Language Supervision (ICML 2021)
- BLIP: Bootstrapping Language-Image Pre-training for Unified Vision-Language Understanding and Generation (ICML 2022)
- Flamingo: a Visual Language Model for Few-Shot Learning (NeurIPS 2022)
- BLIP-2: Bootstrapping Language-Image Pre-training with Frozen Image Encoders and Large Language Models (ICML 2023)
- Visual Instruction Tuning (NeurIPS 2023)
- InstructBLIP: Towards General-purpose Vision-Language Models with Instruction Tuning (NeurIPS 2023)
- PaLI: A Jointly-Scaled Multilingual Language-Image Model (ICLR 2023)
- MaPLe: Multi-Modal Prompt Learning (CVPR 2023)
- MiniGPT-4: Enhancing Vision-Language Understanding with Advanced Large Language Models (ICLR 2024)
- InternVL: Scaling up Vision Foundation Models and Aligning for Generic Visual-Linguistic Tasks (CVPR 2024)

### 3.3 参数高效微调与多模态个性化文献

- Parameter-Efficient Transfer Learning for NLP (ICML 2019)
- The Power of Scale for Parameter-Efficient Prompt Tuning (EMNLP 2021)
- LoRA: Low-Rank Adaptation of Large Language Models (ICLR 2022)
- VL-Adapter: Parameter-Efficient Transfer Learning for Vision-and-Language Tasks (CVPR 2022)
- Visual Prompt Tuning (ECCV 2022)
- AdaLoRA: Adaptive Budget Allocation for Parameter-Efficient Fine-Tuning (ICLR 2023)
- QLoRA: Efficient Finetuning of Quantized LLMs (NeurIPS 2023)
- DoRA: Weight-Decomposed Low-Rank Adaptation (ICML 2024)
- PiSSA: Principal Singular Values and Singular Vectors Adaptation of Large Language Models (NeurIPS 2024)
- SVFT: Parameter-Efficient Fine-Tuning with Singular Vectors (NeurIPS 2024)
- RaSA: Rank-Sharing Low-Rank Adaptation (ICLR 2025)
- LQ-LoRA: Low-rank plus Quantized Matrix Decomposition for Efficient Language Model Finetuning (ICLR 2024)
- LoftQ: LoRA-Fine-Tuning-aware Quantization for Large Language Models (ICLR 2024)

### 3.4 多模态大模型用于视觉感知的相关文献

- DenseCLIP: Language-Guided Dense Prediction with Context-Aware Prompting (CVPR 2022)
- RegionCLIP: Region-based Language-Image Pretraining (CVPR 2022)
- Grounded Language-Image Pre-training (CVPR 2022)
- GroupViT: Semantic Segmentation Emerges from Text Supervision (CVPR 2022)
- Generalized Decoding for Pixel, Image, and Language (CVPR 2023)
- Segment Anything (ICCV 2023)
- VisionLLM: Large Language Model is also an Open-Ended Decoder for Vision-Centric Tasks (NeurIPS 2023)
- Segment Everything Everywhere All at Once (NeurIPS 2023)
- LISA: Reasoning Segmentation via Large Language Model (CVPR 2024)
- GLaMM: Pixel Grounding Large Multimodal Model (CVPR 2024)
- PixelLM: Pixel Reasoning with Large Multimodal Model (CVPR 2024)
- One Token to Seg Them All: Language Instructed Reasoning Segmentation in Videos (NeurIPS 2024)
- OMG-LLaVA: Bridging Image-level, Object-level, Pixel-level Reasoning and Understanding (NeurIPS 2024)
- Grounding DINO: Marrying DINO with Grounded Pre-Training for Open-Set Object Detection (ECCV 2024)
- SAM 2: Segment Anything in Images and Videos (ICLR 2025)
- RemoteSAM: Towards Segment Anything for Earth Observation (ACM MM 2025)
- SAM 3: Segment Anything with Concepts (ICLR 2026)
- VLM-Loc: Localization in Point Cloud Maps via Vision-Language Models (CVPR 2026)

> 学生根据专业基础和选题方向，从上述文献中选择若干篇作为必读材料，其余作为进阶阅读。学生也可围绕具体研究问题补充近年的代表性工作。

---

## 四、结语与期望

本专题旨在帮助学生建立对多模态大模型的整体认识，理解通用模型为何需要面向领域、任务和用户进行个性化，并掌握参数高效微调与少样本适配的基本方法。希望学生在完成模型复现的基础上，能够从真实需求中发现问题，通过规范的实验验证自己的想法，逐步形成独立开展科研工作的能力。
