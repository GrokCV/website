---
title: 新芽专题介绍（11）：大模型的压缩和推理加速
date: 2025-09-18T01:49:00Z
draft: false
math: true
---

## 一、专题介绍

### 1.1 研究背景

近年来，大语言模型和多模态大模型的参数规模、网络深度和输入序列长度不断增长，带来了显著的性能提升，也造成了较高的计算、存储和能耗开销。对于包含图像或视频输入的多模态大模型，大量视觉 Token 和视频帧会进一步增加预填充时间、显存占用和端到端推理延迟，使模型难以直接部署在消费级 GPU、边缘设备和实时应用中。

大模型的压缩和推理加速主要包括两条技术路线：一是量化，即将模型权重、激活值或 KV Cache 从 FP16/BF16 映射为 INT8、INT4、FP8/FP4，乃至二值、三值等更低比特表示，从而降低模型存储、显存占用和计算开销；二是 Token 压缩与剪枝，即识别并删除、合并或跳过低价值的文本、视觉和视频 Token，从而缩短输入序列并减少注意力计算。两类方法分别从“降低单次计算与存储成本”和“减少参与计算的信息数量”两个角度提升推理效率，具有较强的互补性。本专题将以量化和 Token 压缩/剪枝为两条核心主线，同时介绍知识蒸馏、注意力优化和 KV Cache 管理等相关技术。

### 1.2 研究意义

1. **降低模型存储与显存开销**  
   通过低比特量化减少模型权重、激活值和 KV Cache 的存储成本，使大模型能够在资源受限的设备上运行。

2. **减少多模态输入中的冗余计算**  
   通过视觉 Token、视频 Token 和文本 Token 的动态选择、剪枝与合并，缩短输入序列，降低注意力计算开销。

3. **实现多种压缩技术的协同优化**  
   探索量化与 Token 压缩、剪枝等方法的组合，在较高压缩率下尽可能保持模型性能。

4. **促进多模态大模型的高效部署**  
   面向视觉问答、图像理解和视频理解等任务，同时降低模型体积、显存占用和端到端推理延迟。

5. **培养系统化实验能力**  
   引导学生同时关注任务精度、模型规模、显存、延迟和吞吐率，形成规范评测、定位瓶颈和优化系统的科研能力。

### 1.3 当前主要挑战

1. **低比特量化容易造成性能下降**：权重、激活值和 KV Cache 中可能存在异常值，不同层对量化误差的敏感程度也存在明显差异。
2. **不同模态的量化特性不同**：视觉编码器、跨模态连接模块和语言模型具有不同的数值分布，视觉 Token 与文本 Token 对量化误差的敏感性也不完全一致。
3. **Token 重要性难以准确判断**：过度删除或合并 Token 可能损失小目标、细粒度语义、关键视频帧和跨模态对齐信息。
4. **组合压缩可能产生误差叠加**：量化与Token压缩分别造成数值误差和信息损失，二者联合使用时需要合理分配压缩强度。
5. **理论压缩不一定带来真实加速**：模型大小或FLOPs的下降还需要低比特算子、稀疏计算和具体硬件的支持，才能转化为真实延迟收益。

---

## 二、主要学习内容与研究方向

### 2.1 基础知识与性能分析

学生首先学习 Transformer、大模型推理流程、数值表示和 GPU 计算基础，理解参数量、模型大小、FLOPs、MACs、显存占用、延迟与吞吐率等指标。选择一个公开模型建立推理基线，使用性能分析工具定位权重加载、注意力计算、视觉编码和语言生成等环节的主要开销。

### 2.2 大模型量化

重点学习量化的基本原理和实现方法，包括均匀量化与非均匀量化、对称量化与非对称量化、逐张量与逐通道量化，以及训练后量化和量化感知训练。在大模型场景下，进一步研究权重量化、权重—激活联合量化和 KV Cache 量化，比较 W8A8、W4A16（或 W4 权重量化）、W4A8、W4A4 等不同量化配置对模型精度、显存占用和推理速度的影响，并分析异常值、校准数据、量化粒度和混合精度策略对模型性能的影响。对于多模态大模型，还应比较视觉编码器、跨模态连接模块和语言模型的量化敏感性。

### 2.3 Token 压缩与动态剪枝

针对多模态大模型中视觉和视频输入带来的长序列问题，学习 Token 剪枝、合并、聚类、重要性选择和动态保留等方法；进一步了解注意力优化、KV Cache 管理等高效推理技术。研究时应重点分析被压缩 Token 的位置、语义和时序分布，以及不同问题或任务下压缩策略的变化。

### 2.4 建议研究切入点

学生可根据兴趣和实验条件，从下列方向中选择一个开展研究：

1. 开源语言模型或多模态大模型的 W8/W4 训练后量化与误差分析；
2. 权重、激活值和 KV Cache 的量化敏感性及混合精度配置；
3. 面向图像理解的视觉 Token 重要性评估与动态剪枝；
4. 面向视频理解的关键帧选择与视频 Token 压缩；
5. 量化与 Token 压缩/剪枝的联合优化；
6. 面向实际 GPU 或边缘设备的端到端推理加速。

---

## 三、学习资料与参考文献

### 3.1 基础教材与工具

- [《动手学深度学习》](https://zh.d2l.ai/)——深度学习入门教程
- [PyTorch 官方教程](https://pytorch.org/tutorials)——模型构建与性能分析基础
- [Transformers 官方文档](https://huggingface.co/docs/transformers)——大模型加载与推理工具
- [Optimum 官方文档](https://huggingface.co/docs/optimum)——模型优化与硬件加速工具
- [Google Colab](https://colab.research.google.com/)——在线实验环境
- [Kaggle](https://www.kaggle.com/)——开源数据集与实践平台

### 3.2 模型量化与低比特推理文献

- XNOR-Net: ImageNet Classification Using Binary Convolutional Neural Networks (ECCV 2016)
- Quantized Neural Networks: Training Neural Networks with Low Precision Weights and Activations (JMLR 2018)
- Post Training 4-bit Quantization of Convolutional Networks for Rapid-Deployment (NeurIPS 2019)
- Up or Down? Adaptive Rounding for Post-Training Quantization (ICML 2020)
- GPTQ: Accurate Post-Training Quantization for Generative Pre-trained Transformers (ICLR 2023)
- SmoothQuant: Accurate and Efficient Post-Training Quantization for Large Language Models (ICML 2023)
- OmniQuant: Omnidirectionally Calibrated Quantization for Large Language Models (ICLR 2024)
- AWQ: Activation-aware Weight Quantization for On-Device LLM Compression and Acceleration (MLSys 2024)
- KIVI: A Tuning-Free Asymmetric 2bit Quantization for KV Cache (ICML 2024)
- Q-VLM: Post-training Quantization for Large Vision-Language Models (NeurIPS 2024)
- SpinQuant: LLM Quantization with Learned Rotations (ICLR 2025)
- MBQ: Modality-Balanced Quantization for Large Vision-Language Models (CVPR 2025)
- When W4A4 Breaks Camouflaged Object Detection: Token-Group Dual-Constraint Activation Quantization (ECCV 2026)

### 3.3 视觉模型 Token 压缩与动态剪枝文献

- DynamicViT: Efficient Vision Transformers with Dynamic Token Sparsification (NeurIPS 2021)
- TokenLearner: Adaptive Space-Time Tokenization for Videos (NeurIPS 2021)
- Not All Patches are What You Need: Expediting Vision Transformers via Token Reorganizations (ICLR 2022)
- AdaViT: Adaptive Vision Transformers for Efficient Image Recognition (CVPR 2022)
- A-ViT: Adaptive Tokens for Efficient Vision Transformer (CVPR 2022)
- SPViT: Enabling Faster Vision Transformers via Latency-Aware Soft Token Pruning (ECCV 2022)
- Adaptive Token Sampling for Efficient Vision Transformers (ECCV 2022)
- Token Merging: Your ViT But Faster (ICLR 2023)
- Joint Token Pruning and Squeezing Towards More Aggressive Compression of Vision Transformers (CVPR 2023)
- Dynamic Token Pruning in Plain Vision Transformers for Semantic Segmentation (ICCV 2023)
- DiffRate: Differentiable Compression Rate for Efficient Vision Transformers (ICCV 2023)
- AiluRus: A Scalable ViT Framework for Dense Prediction (NeurIPS 2023)
- Rethinking Token Reduction with Parameter-Efficient Fine-Tuning in ViT for Pixel-Level Tasks (CVPR 2025)
- Faster Parameter-Efficient Tuning with Token Redundancy Reduction (CVPR 2025)

### 3.4 多模态大模型与视频 Token 压缩文献

- MovieChat: From Dense Token to Sparse Memory for Long Video Understanding (CVPR 2024)
- An Image is Worth 1/2 Tokens After Layer 2: Plug-and-Play Inference Acceleration for Large Vision-Language Models (ECCV 2024)
- LLaMA-VID: An Image is Worth 2 Tokens in Large Language Models (ECCV 2024)
- Boosting Multimodal Large Language Models with Visual Tokens Withdrawal for Rapid Inference (AAAI 2025)
- LLaVA-Mini: Efficient Image and Video Large Multimodal Models with One Vision Token (ICLR 2025)
- SparseVLM: Visual Token Sparsification for Efficient Vision-Language Model Inference (ICML 2025)
- LongVU: Spatiotemporal Adaptive Compression for Long Video-Language Understanding (ICML 2025)
- DivPrune: Diversity-based Visual Token Pruning for Large Multimodal Models (CVPR 2025)
- VoCo-LLaMA: Towards Vision Compression with Large Language Models (CVPR 2025)
- FlashSloth: Lightning Multimodal Large Language Models via Embedded Visual Compression (CVPR 2025)
- Hybrid-Level Instruction Injection for Video Token Compression in Multi-modal Large Language Models (CVPR 2025)
- DyCoke: Dynamic Compression of Tokens for Fast Video Large Language Models (CVPR 2025)
- VisionZip: Longer is Better but Not Necessary in Vision Language Models (CVPR 2025)
- LLaVA-PruMerge: Adaptive Token Reduction for Efficient Large Multimodal Models (ICCV 2025)
- STAC: Selective Spatiotemporal Aggregation and Compression for Video Reasoning Segmentation (ECCV 2026)

### 3.5 其他压缩与高效推理文献

- Distilling the Knowledge in a Neural Network (arXiv 2015)
- Deep Compression: Compressing Deep Neural Networks with Pruning, Trained Quantization and Huffman Coding (ICLR 2016)
- Training Data-Efficient Image Transformers & Distillation through Attention (ICML 2021)
- FlashAttention: Fast and Memory-Efficient Exact Attention with IO-Awareness (NeurIPS 2022)
- SparseGPT: Massive Language Models Can Be Accurately Pruned in One-Shot (ICML 2023)
- Fast Inference from Transformers via Speculative Decoding (ICML 2023)
- LLM-Pruner: On the Structural Pruning of Large Language Models (NeurIPS 2023)
- H2O: Heavy-Hitter Oracle for Efficient Generative Inference of Large Language Models (NeurIPS 2023)
- Efficient Memory Management for Large Language Model Serving with PagedAttention (SOSP 2023)
- FlashAttention-2: Faster Attention with Better Parallelism and Work Partitioning (ICLR 2024)
- Wanda: A Simple and Effective Pruning Approach for Large Language Models (ICLR 2024)
- Efficient Streaming Language Models with Attention Sinks (ICLR 2024)
- DistServe: Disaggregating Prefill and Decoding for Goodput-optimized Large Language Model Serving (OSDI 2024)
- MInference 1.0: Accelerating Pre-filling for Long-Context LLMs via Dynamic Sparse Attention (NeurIPS 2024)

> 学生根据数学基础、编程能力和硬件条件选择不同难度的研究内容。低年级学生可从量化评测或固定比例 Token 剪枝入手，高年级学生可进一步研究动态压缩、组合压缩或硬件感知优化。

---

## 四、结语与期望

本专题旨在帮助学生理解大模型计算开销的来源，重点掌握大模型量化和Token压缩/剪枝的基本原理，并了解知识蒸馏、注意力优化和高效推理系统等相关技术。希望学生能够从可复现的性能分析出发，发现模型中的冗余与瓶颈，逐步提出兼顾任务性能和部署效率的改进方案，为大模型在实际设备和应用中的高效运行奠定基础。
