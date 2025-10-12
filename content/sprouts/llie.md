---
title: 新芽专题介绍：暗光图像增强
date: 2025-09-17T00:58:00Z
draft: false
math: true
---

> 此专题由非南开大学老师发布，选修南开大学 2025 秋《人工智能实践课-初级》课程的同学请勿选择此专题。非本课程选修同学可自由选择。 

### 一、专题介绍

#### 1.1 研究背景

在计算机视觉领域中，**暗光环境下的图像增强（Low-Light Image Enhancement, LLIE）** 一直是一个具有重要应用价值和研究意义的课题。随着智能手机摄影、视频监控、自动驾驶、医疗影像分析以及夜间无人机导航等场景的普及，人们对在低照度环境下获取清晰、真实图像的需求日益增长。然而，由于光照不足，暗光图像往往存在**亮度低、噪声高、细节丢失、颜色失真**等问题，严重影响后续任务（如目标检测、识别、分割等）的性能和可靠性。

传统的暗光增强方法多基于图像处理算法，如直方图均衡、Retinex模型、Gamma校正等。这些方法在某些场景下能够改善图像亮度和对比度，但普遍存在**增强结果过度、细节模糊、颜色偏差**等问题，无法在复杂光照条件下保持图像的自然感和一致性。近年来，深度学习技术的兴起为暗光增强提供了新的思路。CNN和GAN等模型能够通过数据驱动的方式学习从低光到正常光图像的映射关系，在亮度恢复、噪声抑制和细节重建方面取得了显著进展。然而，这类方法仍面临诸多挑战：例如，**训练数据匮乏、模型泛化性差、增强结果失真、实时性不足**等。

因此，构建一种能够**在多场景、多设备条件下稳定提升图像质量**的暗光增强模型，成为当前研究的关键目标。该模型不仅应提高图像的视觉质量，还需兼顾**噪声抑制、色彩还原、结构保持和计算效率**，以满足实际应用的需求。

#### 1.2 研究意义

本研究旨在开发一个高性能、可解释的暗光图像增强模型，提升低照度图像的视觉质量和可用性，其意义主要体现在以下几个方面：

1.  **提升图像可视化质量与人眼感知体验：** 通过自动化的暗光增强算法，能够显著改善图像的亮度与对比度，使人眼在夜间或弱光条件下也能清晰识别场景细节。这对于移动摄影、夜景视频拍摄和安防监控等应用具有直接价值。
2.  **促进下游计算机视觉任务的性能提升：** 低照度图像通常会降低目标检测、识别与跟踪等任务的准确率。通过暗光增强模型的预处理，可有效提高这些任务的输入质量，从而提升整体系统的性能与鲁棒性，尤其是在自动驾驶和无人系统中。
3.  **推动智能成像与视觉感知系统的发展：** 暗光增强技术是智能视觉系统的重要组成部分。高质量的增强算法可被集成到相机硬件、图像信号处理芯片及移动端设备中，助力智能终端实现更好的夜拍和视觉计算体验。
4.  **促进人机交互和公共安全领域的应用：** 在医疗、监控、应急救援等场景中，清晰的暗光图像有助于更准确地识别关键信息，提升决策效率和安全性。本研究将为这些领域提供可靠的技术支撑。

#### 1.3 当前主要挑战

尽管暗光增强研究已取得显著进展，但在理论与实践层面仍存在以下主要挑战：

1.  **低光数据的稀缺性与多样性不足：** 高质量的成对数据（低光图像与正常光图像）获取难度较大，尤其是在真实场景下，不同光照、设备和环境条件都会影响成像效果。缺乏大规模、高多样性的训练数据集限制了模型的泛化能力。
2.  **增强效果与噪声抑制的平衡困难：** 在提升亮度的同时，暗光图像中的噪声往往被放大。如何在保持细节和纹理的同时有效抑制噪声，是当前模型设计中的核心问题。过度增强或过度平滑都会导致视觉失真或结构信息丢失。
3.  **模型的泛化性与鲁棒性不足：** 许多深度学习模型在特定数据集上表现优异，但在不同设备、场景或光照条件下表现不稳定。缺乏跨域泛化能力会限制算法在真实世界中的应用。
4.  **缺乏统一、客观的评价体系：** 暗光增强的效果评估目前仍依赖主观评分或有限的客观指标（如PSNR、SSIM）。这些指标无法充分反映增强图像的感知质量、色彩真实性与视觉自然度。因此，如何构建科学合理的综合评价体系，是评估模型性能的重要难点。

### 二、学习资料与参考文献

#### 2.1 基础教材与学习材料

为了便于初学者夯实基础，下面分享一些实用的教程：

-   李沐[《动手学深度学习》](https://zh.d2l.ai/)——适合中文初学者的深度学习教材，以及[课程系列视频](https://space.bilibili.com/1567748478/lists/358497?type=series)
-   [《Deep Learning》](https://www.deeplearningbook.org/)——深度学习入门经典教材
-   [PyTorch 官方教程](https://pytorch.org/tutorials)，也可以使用 [PyTorch 中文文档](https://pytorch-cn.readthedocs.io/zh/latest/)
-   [《Pattern Recognition and Machine Learning》](https://www.microsoft.com/en-us/research/wp-content/uploads/2006/01/Bishop-Pattern-Recognition-and-Machine-Learning-2006.pdf)——机器学习原理入门

此外，也可以使用一些**入门工具**：

-   [Google Colab](https://colab.research.google.com/)：免费云平台，不用安装软件，就能跑PyTorch代码
-   [Kaggle平台](https://www.kaggle.com/)：免费数据集和竞赛

#### 2.2 综述文献

《Low-Light Image and Video Enhancement Using Deep Learning: A Survey》：这篇TPAMI综述总结了**传统暗光图像增强领域的经典方法**以及早期的经典深度学习方法，可以帮助初学者快速理解该领域。

#### 2.3 入门文献

-   [传统低光照增强方法](https://blog.csdn.net/lutlx20010913/article/details/145052990)总结，有助于理解基本图像处理方式。（[补充链接](https://blog.csdn.net/m0_46366547/article/details/131060664)）
-   **PyDiff**：[Pyramid Diffusion Models For Low-light Image Enhancement](https://arxiv.org/abs/2305.10028)
-   **GSAD**：[Global Structure-Aware Diffusion Process for Low-Light Image Enhancement](https://arxiv.org/abs/2311.17253)
-   **HVI**: [A New Color Space for Low-light Image Enhancement](https://arxiv.org/abs/2502.20272)
-   **Enlightengan**: [Deep light enhancement without paired supervision](https://arxiv.org/abs/1906.06972)
-   **NeRCo**：[Implicit Neural Representation for Cooperative Low-light Image Enhancement](https://arxiv.org/abs/2303.11722)
-   **FoCo**：[Improving Visual and Downstream Performance of Low-Light Enhancer with Vision Foundation Models Collaboration](https://openaccess.thecvf.com/content/CVPR2025/papers/Gu_Improving_Visual_and_Downstream_Performance_of_Low-Light_Enhancer_with_Vision_CVPR_2025_paper.pdf)
-   **Zero-DCE**：[Zero-reference deep curve estimation for low-light image enhancement](https://arxiv.org/abs/2001.06826)
-   **SACC**：[Unsupervised Illumination Adaptation for Low-Light Vision](https://ieeexplore.ieee.org/document/10480646)

### 三、学习任务

#### 3.1 论文学习及体系构建

-   从传统算法、早期深度学习方法、现有主流深度学习方法（有监督&无监督）以及未来展望几个方面，总结暗光图像增强领域的现状。
-   结合自己的思考，分析现有方法的不足，探索暗光增强与其他自然退化（去雪、去雨等）之间的联系。
-   撰写学习笔记。

#### 3.2 代码复现

上述2.3中展现的文献都是具备开源代码的，挑选传统方法、有监督学习方法、无监督学习方法各一个进行复现。

-   报告中应该展示模型整体清晰的数据流，输入是什么，如何经过网络一步一步得到输出结果的。
-   请总结这篇文章相比于其他的文章的创新点在哪，做了哪些改进？（尝试在Introduction和Related Work里寻找答案，加上自己跑实验的一些感悟）
-   报告中应该包含对所复现方法的实验结果以及代码展示，以及对实验结果的分析，注意总结的逻辑性和条理性。
-   报告建议以PDF格式提交，代码使用pytorch环境（建议pycharm+anaconda）。
-   数据集建议采用LOL和LSRW来训练，并可额外尝试在VV等无真值数据集中测量感知指标，[数据集链接1](https://blog.csdn.net/lutlx20010913/article/details/145048364)，[数据集链接2](https://github.com/Li-Chongyi/Lighting-the-Darkness-in-the-Deep-Learning-Era-Open?tab=readme-ov-file)。

#### 3.3 辅助链接

-   [环境配置辅助教程](https://zhuanlan.zhihu.com/p/27577871722)