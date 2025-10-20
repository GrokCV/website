---
title: 📄【TGRS 2025】DRPCA-Net：低秩-稀疏先验遇上深度展开的动态革新
date: 2025-07-13
draft: false
math: true
authors: 
- Zihao Xiong
---


<img src="https://github.com/GrokCV/website/blob/master/content/blog/DRPCA-Net/figs/title.png?raw=true" title="" alt="![[title.png]]" data-align="center">

Paper：[DRPCA-Net: Make Robust PCA Great Again for Infrared Small Target Detection](https://arxiv.org/abs/2507.09541)

GitHub：[github.com/GrokCV/DRPCA-Net](https://github.com/GrokCV/DRPCA-Net)

作者：熊子豪，周飞，伍风翼，袁帅，付麦霞，彭真明，杨健，戴一冕

**RPCA＋动态参数打赢小目标检测，跑分和解释性ALL IN!**

**欢迎来到 RPCA 2.0 时代，DRPCA-Net，把“低秩背景 + 稀疏目标”的数学先验，做成可学习、会随场景自适应的动态展开网络。**

<img title="" src="https://github.com/GrokCV/website/blob/master/content/blog/DRPCA-Net/figs/meme1.jpg?raw=true" alt="" width="429" data-align="center">

---

## 太长不看版

许多红外小目标只占寥寥数个像素，有着目标稀疏性和背景低秩性的特征，对比度低、噪声大，端到端堆复杂卷积并不总能泛化；而”目标稀疏、背景低秩”的RPCA先验恰好对症：假设图像 = 低秩背景 + 稀疏目标，很符合红外小目标检测的物理先验。不过遗憾的是，RPCA静态优化，超参数固定，不同场景下鲁棒性不足。针对此，我们设计了让 RPCA “动起来”的**DRPCA-Net**，把RPCA的优化过程中的关键参数动态化，其为利用轻量超网络按输入场景逐迭代关键生成参数，让每一步都“看内容”再更新。

---

## 主要内容讲解

<img title="" src="https://github.com/GrokCV/website/blob/master/content/blog/DRPCA-Net/figs/motivation.png?raw=true" alt="![[title.png]]" data-align="center">

图 1 传统静态展开（RPCANet）与我们提出的动态展开（DRPCA-Net）的视觉比较。
不同阶段（1、3 和 6）的可视化结果表明，动态参数生成机制有助于有效抑制背景干扰。

### 研究背景

红外小目标有两个关键特性：**目标稀疏性**（目标在图像中占比极小，呈现稀疏分布）和**背景低秩性**（背景像素往往具有空间相关性，可近似为低秩矩阵）。传统的模型驱动方法（如鲁棒主成分分析 RPCA）正是基于这两个特性，通过矩阵分解分离目标与背景。但这类方法有个致命缺陷：参数固定且依赖人工设计，面对复杂背景时，很难自适应调整分解策略，导致误报率高。

而深度学习方法虽然通过多层卷积提取特征，在复杂场景中表现更好，但又走向了另一个极端：模型越堆越复杂。比如有些网络为了提升精度，叠加大量注意力模块和高分辨率特征图，不仅计算量爆炸，还忽略了红外目标的固有稀疏性先验，相当于“用大炮打蚊子”，在小目标场景中容易过拟合。

最近，RPCANet<sup>[[1]](#ref1)</sup>引入了深度展开策略，将传统的低秩稀疏分解模型转变为分层和可学习的深度框架，该框架可以利用来自低秩稀疏性的全局先验和数据驱动方法的优势。但这些将特定领域的先验与深度架构桥接的尝试仍然揭示了现实世界 IRSTD 场景中的关键局限性。

现有方法普遍存在以下痛点：

**先验利用不足**：当前的对比增强网络通过局部强度变化隐式地指导目标定位，但未能明确编码红外小目标的全局稀疏性和背景的低秩。这会导致真正的稀疏目标和高对比度背景噪声之间的模糊区分，从而导致持续的误报。

**先验建模僵化**：现有的展开网络采用固定的卷积核进行背景估计，假设场景之间的空间相关性是一致的。如图 1 所示，这种刚性方法与红外背景的异质性相冲突，导致结构过度平滑或残余杂波。

### 研究动机

为了解决上述限制，我们从新的角度重新审视了经典的 RPCA 公式。我们要问：我们能否构建一个可学习但先验感知的架构，并动态适应其优化轨迹到输入场景，同时保留 RPCA 的核心低秩/稀疏分解原则？我们的回答是肯定的。从超网络的概念中汲取灵感，我们引入了一种动态展开范式，该范式支持以输入为条件的自适应迭代参数生成。这种以上下文为条件的先验展开机制使网络能够保留 RPCA 的数学清晰度，同时获得深度学习的灵活性。

基于这个想法，我们提出了 DRPCA-Net，这是一种新颖的深度展开网络，它将每个迭代步骤的参数化与静态训练解耦，而是通过轻量级超网络动态生成，其根据场景的特征以动态方式预测它们，从而允许模型为每个实例定制其推理轨迹。

## DRPCA-Net：动态、可解释的检测新范式

DRPCA-Net 的核心思想是将 RPCA 的迭代优化过程展开为一个多阶段的深度网络。DRPCA-Net 引入了**两大创新设计：**


### 1.  **动态参数生成机制 (Dynamic Parameter Generation)**

我们不再使用固定的、全局学习的参数，而是设计了一个轻量级的**参数生成器**。 这个生成器能够根据每一张输入图像的特性，为网络的不同处理阶段（stage）动态地、自适应地生成最优的迭代参数（如平衡系数 γ 和更新步长 ε ）。这使得 DRPCA-Net 能够根据场景变化实时调整其推理路径，极大提升了模型对不同背景的鲁棒性和泛化能力。

僵：$$\mathbf{T}^{k}=\mathbf{T}^{k-1}+\mathbf{D}^{k-1}-\mathbf{B}^{k}-\varepsilon^{k}\mathcal{G}^{k}(\mathbf{T}^{k-1}+\mathbf{D}^{k-1}-\mathbf{B}^{k})$$

动：
$$
\begin{aligned}
\mathbf{T}^k =& \gamma_D^k \mathbf{T}^{k-1} + (1 - \gamma_D^k)(\mathbf{D}^{k-1} - \mathbf{B}^k) \\
&- \varepsilon_D^k S^k\left( \gamma_D^k \mathbf{T}^{k-1} + (1 - \gamma_D^k)(\mathbf{D}^{k-1} - \mathbf{B}^k) \right)
\end{aligned}
$$

### 2.  **动态残差组 (Dynamic Residual Group, DRG)**

为了更精确地估计和重建背景与目标，我们设计了 DRG 模块。 该模块创新性地集成了**动态空间注意力**（DSA）机制。 与传统注意力机制不同，DSA 能根据输入特征动态生成定制化的卷积核，从而实现对空间特征的自适应调整，能够更好地捕捉背景中的上下文变化。<img title="" src="https://github.com/GrokCV/website/blob/master/content/blog/DRPCA-Net/figs/DRPCA-Net.png?raw=true" alt="![[DRPCA-Net.png]]" data-align="center" width="806">图 2 DRPCA-Net 的总体结构。介绍了第 k 级的详细结构，包括潜在背景编码器模块（LBEM）、动态目标提取模块（DTEM）、动态图像重建模块（DIRM）和参数生成器。其中，DSA 被嵌在 DRG 中。

**网络架构概述**：DRPCA-Net 的整体架构如图 2 所示。该网络包括 K 个阶段，每个阶段结构相同并且实现背景估计、动态目标提取和动态图像重建的一个循环。输入的红外图像 X 初始化 D<sup>0</sup>，且 T<sup>0</sup> 被设置为零。第 k−1 级的输出，即 D<sup>k−1</sup> 和 T<sup>k−1</sup>，被馈入第 k 级。在阶段 k 内，LBEM 计算 B<sup>k</sup>。随后，DTEM 利用 D<sup>k−1</sup>、B<sup>k</sup> 和 T<sup>k−1</sup>，根据参数生成器动态生成的参数（ γ、ε ）来计算 T<sup>k</sup>。最后，DIRM 采用 B<sup>k</sup> 和 T<sup>k</sup> 来重建 D<sup>k</sup> 用作下一阶段的输入。最终的目标图从最后一级的目标估计 T<sup>K</sup> 输出。整个网络，包括所有 LBEM、DTEM、DIRM（包括 DRG）的参数，以及所有 K 个阶段上的参数生成器，被端到端地训练。

## 实验性能与结果分析

### 实验准备

对 DRPCA-Net 进行严格和全面的评估，我们的实验利用了已建立的基准数据集，标准化的评估指标和实施参数。我们在四个广泛采用的红外小目标检测基准数据集上进行了实验：SIRST V1 <sup>[[2]](#ref2)</sup>，IRSTD-1K <sup>[[3]](#ref3)</sup>，NUDT-SIRST <sup>[[4]](#ref4)</sup>和 SIRST-Aug<sup>[[5]](#ref5)</sup>。这些数据集共同代表了真实世界和合成红外成像场景的不同光谱，包括目标尺度、强度和形态的显著变化，以及背景杂波复杂性（例如，城市、海洋、空中、自然景观）和传感器特性。包含真实世界的捕获和增强数据确保了对模型有效性，鲁棒性和泛化能力的全面评估。

### 性能对比

表 I 不同方法在 SIRST V1、NUDT-SIRST、SIRST-AUG 和 IRSTD-1K 上的性能比较，以 IoU（%）、$F_1$（%）、$P_d$（%）、$F_a$（10<sup>−6</sup>）和参数数（M）表示。最佳结果以粗体红色字体突出显示。

<img title="" src="https://github.com/GrokCV/website/blob/master/content/blog/DRPCA-Net/figs/experiment.png?raw=true" alt="" data-align="center" width="730">

我们提出的方法在大多数数据集和评估指标上始终如一地取得了最先进或极具竞争力的结果。值得注意的是，DRPCA-Net 在 IoU、 $F_1$ 以及 $P_d$ 在 SIRST V1、SIRST-AUG 和 NUDT-SIRST 数据集中排名靠前。这种一致的优越性证明了动态展开机制的效力以及 DRG 模块促进的增强特征表示，能够稳健地适应不同的目标特征和背景复杂性。

<img title="" src="https://github.com/GrokCV/website/blob/master/content/blog/DRPCA-Net/figs/Visualization.png?raw=true" alt="![[Visualization.png]]" data-align="center">
图 3 具有挑战性的红外场景的定性比较。各列显示原始图像、来自 TopHat、RDIAN、ISNet、UIUNet、L2SKNet、我们的 DRPCA-Net 和地面实况（GT）的结果。正确检测用红色框标记，遗漏检测用绿色框标记，误报用白色虚线圆圈标记。

图 3 直观展示了我们方法与部分前沿方法的检测效果对比。可以看出，DRPCA-Net 在漏检和虚警方面均表现出明显优势，检测结果更加精准可靠。

## 无限可能性

本文提出的 DRPCA-Net 通过引入由超网络驱动的动态参数生成机制以及用于精细化特征提取的 DRG 模块，在保持模型可解释性的同时，实现了对不同场景的强大自适应能力，并在多个基准测试中树立了新的性能标杆。值得注意的是，这一动态深度展开范式具有良好的通用性，可进一步尝试在其他模型上应用，以提升其自适应特性和整体性能。

我们坦诚地分析了模型的局限性。DRPCA-Net 的强大性能部分来源于其基于 RPCA 的先验假设（背景低秩、目标稀疏）。 因此，当遇到严重违反这些假设的场景时（例如，在 IRSTD-1K 数据集中某些包含大量类目标干扰的复杂地面场景），模型的性能优势会有所减弱。这为未来的工作指明了方向：探索如何让模型在坚持有效先验的同时，具备识别和处理**先验失效**场景的能力，是进一步提升模型鲁棒性和泛化性的关键。


如果你也对我们的 DRPCA-Net 感兴趣、如果你也在做**红外小目标/低信噪检测**，欢迎**Star&试用！**

我们的代码已经开源：[GitHub DRPCA-Net](https://github.com/GrokCV/DRPCA-Net)

欢迎交流~

## 致谢

我们感谢天津市视觉计算与智能感知重点实验室（VCIP）提供的必要资源。计算部分由南开大学超级计算中心提供支持。

## 参考文献

<a name="ref1">[1]</a>: F. Wu, T. Zhang, L. Li, Y. Huang, and Z. Peng, **RPCANet: Deep unfolding RPCA based infrared small target detection**,in IEEE Winter Conference on Applications of Computer Vision, 2024, pp. 4797–4806.

<a name="ref2">[2]</a>: Y. Dai, Y. Wu, F. Zhou, and K. Barnard, **Asymmetric contextual modulation for infrared small target detection,** IEEE Transactions on Geoscience and Remote Sensing, vol. 59, no. 11, pp. 9813–9824, 2021.

<a name="ref3">[3]</a>: M. Zhang, R. Zhang, Y. Yang, H. Bai, J. Zhang, and J. Guo, **ISNet: Shape matters for infrared small target detection,** in IEEE Conference on Computer Vision and Pattern Recognition, 2022, pp. 867–876.

<a name="ref4">[4]</a>: H. Wang, L. Zhou, and L. Wang, **Miss detection vs. false alarm: Adversarial learning for small object segmentation in infrared images,** in IEEE International Conference on Computer Vision, 2019, pp. 8508–8517.

<a name="ref5">[5]</a>: T. Zhang, L. Li, S. Cao, T. Pu, and Z. Peng, **Attention guided pyramid context networks for detecting infrared small target under complex background,** IEEE Transac tions on Aerospace and Electronic Systems, vol. 59, no. 4, pp. 4250–4261, 2023.