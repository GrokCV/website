---
title: 【TGRS 2025】 SeqCSIST: Sequential Closely-Spaced Infrared Small Target Unmixing
date: 2025-08-08
draft: false
math: true
authors: 
- Ximeng Zhai
---

![](https://fastly.jsdelivr.net/gh/bucketio/img1@main/2025/08/03/1754234034174-819bdddd-cc58-4e29-8746-e8ffc9cd1080.png)

## 首次发布多帧空间邻近红外小目标解混数据集！DeRefNet 解混精度提升 5.3%，填补多帧检测空白

📄  arXiv地址：https://arxiv.org/abs/2507.09556

📂 代码开源地址：https://github.com/GrokCV/SeqCSIST

📂 数据集开源地址：https://pan.baidu.com/share/init?surl=_sxGh5oFQ8-3RpUUeMN2Mg&pwd=kxe9 或 https://1drv.ms/f/c/698f69b8b2172561/EuBC8549kZJIp_syz2Glft4BU2Fu5Ri-wYE888HJ9kmiiQ?e=zEISNc

## 背景与动机

#### 视觉成像特征

&#x20;     从宏观角度来看，由于光学透镜 **焦距** 和红外探测器 **分辨率** 的限制，随着远距离空间邻近红外小目标（Closely-Spaced Infrared Small Target, CSIST）群中 **子目标逐渐靠近**，目标能量逐渐发生混叠，目标群在红外图像中通常以 **能量混叠光斑** 的形式出现，现有方法无法做到精确的目标检测。具体效果如图1所示。

![](https://fastly.jsdelivr.net/gh/bucketio/img18@main/2025/08/03/1754234118436-1b7c2c51-96e9-4c57-92a6-f316ea04607e.png)


图1 远距离红外小目标靠近导致成像面能量逐渐发生混叠的过程示意图

从微观角度来看，由于远距离目标与成像系统 **距离较远**，加之 **空间尺度细小**，光学系统能够捕获的目标 **辐射强度&#x20;**&#x4F1A;很 **弱**。当目标出现在空间上密集聚集时，这种挑战会更加严峻，目标能量混叠原理（Imaging）及解混（Unmixing）示意，如图2所示，具体成像原理见下述光学成像机理。

![](https://fastly.jsdelivr.net/gh/bucketio/img16@main/2025/08/03/1754234144845-f2782c4d-472f-4585-8d68-879dd8d0858d.png)


图2 红外远距离空间邻近小目标成像及其解混过程示意图

#### 光学成像机理

当单色点光源通过透镜成像时，在焦点处会出现一种称为 "艾里斑" 的衍射图案，其特征是中心处有一个包含总能量 84% 的亮斑，周围环绕着多个同心衍射环。这种衍射效应通常用点扩散函数（PSF）来近似：

$$p\left(x,y\right)=\frac{1}{2\pi\sigma_{PSF}^2}\exp{\left[-\frac{\left(x-x_t\right)^2+\left(y-y_t\right)^2}{2\sigma_{PSF}^2}\right]}$$

其标准差取决于传感器的焦距比（f值）和探测波段，用于量化能量扩散。

在多目标成像中，每个像素捕获的强度是叠加点源的累积响应。特别是对于遥远的物体，每个物体都被视为点源，由此产生的 "艾里斑" 半径由 $1.22\lambda/D$ 决定，其中 $\lambda$ 为波长，D 为透镜直径。该半径等于高斯 PSF 的 $1.9\sigma$，标志着传感器的物理分辨率极限，符合瑞利单位的定义。本文采用84%能量集中度定义作为分辨率判据，将 $\sigma_{PSF}$ 设置为 0.5 个像素。像素 $(i,j)$ 对目标的响应被定义为 PSF 在其边界内的积分值：

$$g_{i,j}\left(x_t,y_t\right)=\int_{x_{i,j}-1/2D}^{x_{i,j}+1/2D}\int_{y_{i,j}-1/2D}^{y_{i,j}+1/2D}p\left(x,y\right)dxdy$$

一个由 $U\times V$ 个像素构成的红外焦平面，并且有 $K$ 个子像素级目标，其坐标分别为 $(x_k,y_k),k=1,\cdots,K$。通过将焦平面矩阵的列重新排列为 $UV\times 1$ 的向量，图像可以通过如下公式仿真计算：

$$\mathbf{z}=\left[\mathbf{g}^c\left(x_1,y_1\right)\mathbf{g}^c\left(x_2,y_2\right)\cdots\mathbf{g}^c\left(x_K,y_K\right)\right]\mathbf{s}+\mathbf{n}$$ 
$$=\mathbf{G}\left(\mathbf{x},\mathbf{y}\right)\mathbf{s}+\mathbf{n}$$

其中，G(x,y)是一个 $UV\times K$ 的导向矩阵，它封装了 CSIST 位置对每一像素响应的影响，列 $g^\mathrm{c}\left(x_k,y_k\right)$ 展现了目标对像素响应的贡献。目标的峰值强度用向量 $s=\left[s_1,s_2,\cdots,s_\mathrm{K}\right]^\top$ 表示，而 $\mathbf{n}$ 则代表具有方差 $\sigma_\mathrm{n}^2$ 的高斯白噪声，其在不同像素间是独立的。

#### 动机

现有方法无法做到精确的目标检测，具体表现为：

对于一个能量混叠光斑，只能检测到混叠光斑的位置，即 Bounding box，无法精确的检测出光斑内的目标 **数量** 和 **位置**。具体原因为：

  - 现有红外小目标检测方法局限于大视场但稀疏目标的场景，往往 缺少稀疏先验。
  - 现有红外小目标检测方法背后的假设是图像中检测到的目标与其对应的目标之间存在精确的一一映射 关系。

![](https://fastly.jsdelivr.net/gh/bucketio/img7@main/2025/08/03/1754234233261-64bfa6f3-f926-4195-a739-9804f5335817.png)

图3 传统红外小目标检测与空间邻近红外小目标解混的区别示意图

##  创新点

#### 🚀 **新任务** : 多帧空间邻近红外小目标解混（Closely-Spaced Infrared Small Target Unmixing, CSIST Unmixing），专注 CSIST 小目标的亚像素级定位和解混。

#### 🔓 **新开源数据集** : 首次提出了一个具有序列基准的多帧空间邻近红外小目标解混数据集 SeqCSIST。

#### 🛠️ **新开源工具包** : 包括客观评估新任务的指标及 23 种对比实验方法。

#### 🧠 **新方法** : 首次提出了一个用于多帧 CSIST Unmixing 的可变形细化网络 DeRefNet

###  开源数据集 SeqCSIST

**SeqCSIST 数据集** 包含 5000 个轨迹，总共 100000帧。每个轨迹由 20 帧组成，每 5 个连续帧形成一个序列（每个序列的初始帧在 0 到 15 的轨迹中有对应的序列号，因此总共有 16个 序列）。数据集分为三个子集：70% 用于训练（3500 个轨迹），15% 用于验证（750 个轨迹），15% 用于测试（750 个轨迹）。

![](https://fastly.jsdelivr.net/gh/bucketio/img10@main/2025/08/03/1754234250792-4d9f07bb-7c60-4a59-8989-cfafcc7609d6.png)


图4 SeqCSIST 示意图

### 新方法 : DeRefNet

DeReNet 亮点如下：

* **模型与数据双驱动** 架构 : 使用深度展开策略替换传统的残差堆叠结构进行特征提取。

* 多帧 **时序信息** 的融合与处理 : 采用 **轻量化** 的绝对位置编码，同时提高了解混的准确性。

* 多帧 **可变形对齐** 模块的设计 : 使用隐式的动态对齐替换传统的显式光流法，采用最大平均池化动态选择参考帧与中间帧的提取比重，使参考帧向中间帧动态对齐。

* “早期超分”策略 : 更早的提取充分的特征信息。

![](https://fastly.jsdelivr.net/gh/bucketio/img5@main/2025/08/03/1754234279348-430e001f-0b54-4319-8b24-6cd06b0963d5.png)


图5 DeRefNet 架构示意图

## 实验

### 实验设置

&#x20;     作为目标检测的下游后处理任务，我们的方法处理的数据是模拟传统目标检测的结果（即检测到的能量混叠斑块）而不是直接在原始图像中裁剪的目标块。在整个实验中，初始化超分辨率c设置为3。输入目标块大小为 11 × 11，GT 图像大小和输出解混图像大小均为 33 × 33。为了每次加载完整的轨迹，在我们的实验中，批处理大小被设置为 20。为了提高数据利用率和获得更好的模型性能，一次处理5个连续帧（1 − 5，2 − 6，...，16 − 20）。因此，每个轨迹包含 20 − 4 = 16 个序列，而不是 20 − 5 = 4 个序列。最后，残留块的数量 n 设置为 5。在涉及空间特征提取的实验的所有部分中，使用32通道卷积。为了优化，我们使用 Adam 优化器和 MMEngine 框架来执行网络，学习率始终保持在 10⁻⁴。

### 成果展示 | DeRefNet 解锁红外图像“看不清”的难题

#### Comparison with State-of-the-Art

![](https://fastly.jsdelivr.net/gh/bucketio/img7@main/2025/08/03/1754234301012-b5eb712e-813b-483d-8146-9e3785e90067.png)


表1 对比实验

如图表所示，我们的方法相比于传统模型驱动方法、超分方法、深度展开方法等三类方法，在就解混效果上表现优异。

#### Ablation Study

![](https://fastly.jsdelivr.net/gh/bucketio/img10@main/2025/08/03/1754234315875-1b7ec87b-411c-45a8-bd3d-6ba9c2d1a593.png)


表2 特征提取模块与残差堆叠模块效果对比

![](https://fastly.jsdelivr.net/gh/bucketio/img15@main/2025/08/03/1754234327166-f129c46d-4e76-4392-981b-74a9f378eb7f.png)


表3 DeRefNet 各模块消融实验

如图表所示，消融实验印证了上述 DeRefNet 亮点中提到的时序信息引入、可变形模块设计等亮点。

#### Visual Analysis

![](https://fastly.jsdelivr.net/gh/bucketio/img13@main/2025/08/03/1754234352043-18deed15-b082-4a3f-b3e6-1925d74c6b87.png)


图6 部分对比试验可视化

如图所示，我们的方法相比于传统的模型驱动方法、深度展开方法、超分方法等取得了最好的解混效果。

## 结论与讨论

&#x20;     在本文中，我们提出了一个新的任务，即 **序列空间邻近红外小目标解混**，以及一个 DeRefNet 框架，它由三个关键组件组成：一个稀疏驱动的特征提取模块，一个位置编码模块和一个时间可变形特征对齐（TDFA）模块。这是第一个将深度展开范式引入序列 CSIST Unmixing 设计的研究。通过比较研究和广泛的实验，实验结果表明，DeRefNet 框架有效解决了红外图像中 CSIST 能量混叠问题，实现了红外目标的解混和亚像素定位，并构建了一个开源的红外目标解混生态系统，包括序列基准数据集和工具包，为相关研究提供了宝贵的资源。

## 致谢

&#x20;     我们感谢西安光机所飞行器光学成像监视与测量技术研究室和天津市视觉计算与智能感知重点实验室（VCIP）提供的必要资源。计算部分由南开大学超级计算中心（NKSC）提供支持。

## 参考文献

\[1] D. Wang, J. Liu, L. Ma, R. Liu, and X. Fan, “Improving misaligned multi-modality image fusion with one-stage progressive dense registration,” IEEE Transactions on Circuits and Systems for Video Technology, 2024.

\[2] Y. Dai, P. Pan, Y. Qian, Y. Li, X. Li, J. Yang, and H. Wang, “Pick of the bunch: Detecting infrared small targets beyond hit-miss trade-offs via selective rank-aware attention,” IEEE Transactions on Geoscience and Remote Sensing, 2024.

\[3] M. Zhang, R. Zhang, Y. Yang, H. Bai, J. Zhang, and J. Guo, “ISNet: Shape matters for infrared small target detection,” in Proceedings of the IEEE Conference on Computer Vision and Pattern Recognition, 2022, pp. 877– 886.

\[4] Y. Dai, Y. Wu, F. Zhou, and K. Barnard, “Attentional local contrast networks for infrared small target detection,” IEEE Transactions on Geoscience and Remote Sensing, vol. 59, no. 11, pp. 9813–9824, 2021.

\[5] B. Li, C. Xiao, L. Wang, Y. Wang, Z. Lin, M. Li, W. An, and Y. Guo, “Dense nested attention network for infrared small target detection,” IEEE Transactions on Image Processing, vol. 32, pp. 1745–1758, 2022.

\[6] X. Wu, D. Hong, and J. Chanussot, “UIU-Net: U-Net in U-Net for infrared small object detection,” IEEE Transactions on Image Processing, vol. 32, pp. 364–376, 2022.

\[7] X. Li, T. Ma, Y. Hou, B. Shi, Y. Yang, Y. Liu, X. Wu, Q. Chen, Y. Li, Y. Qiao et al, “LoGoNet: Towards accurate 3d object detection with local-to-global crossmodal fusion,” in Proceedings of the IEEE Conference on Computer Vision and Pattern Recognition, 2023, pp.17 524–17 534.

\[8] L. Lin, H. Xu, D. Xu, and W. An, “Resolution of closely spaced objects via infrared focal plane using reversible jump Markov chain Monte-Carlo method,” Acta Opt. Sin, vol. 31, no. 5, p. 0510004, 2011.

\[9] X. Tong, Z. Zuo, S. Su, J. Wei, X. Sun, P. Wu, and Z. Zhao, “ST-Trans: Spatial-temporal transformer for infrared small target detection in sequential images,” IEEE Transactions on Geoscience and Remote Sensing, vol. 62, pp. 1–19, 2024

\[10] C. P. Chen, H. Li, Y. Wei, T. Xia, and Y. Y. Tang, “A local contrast method for small infrared target detection,” IEEE Transactions on Geoscience and Remote Sensing, vol. 52, no. 1, pp. 574–581, 2013.
