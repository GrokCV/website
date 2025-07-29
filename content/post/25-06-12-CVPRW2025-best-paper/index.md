---
title: Champion Solution for CVPRW2025 Anti-Object Tracking Challenge Track 1
date: 2025-06-12
---

Congratulations to Jia Di and the team for winning first place in Track 1 of the CVPRW2025 Anti-Object Tracking Challenge.

<!--more-->

This challenge focused on tracking UAV targets in infrared video. Our approach is simple yet effective: we use a standard object detector as the base, and enhance it by stacking the current and previous two frames as input, allowing the model to learn both appearance and motion cues. A trajectory constraint is applied in post-processing to further improve accuracy. This method achieved the best results in Track 1 and runner-up in Track 2. For more details, see our [paper](https://www.arxiv.org/abs/2505.04917) and [code](https://github.com/facias914/A-Simple-Detector-is-a-Strong-Tracker).
