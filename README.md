# Using-color-gamut-limitations-such-as-HSV-and-RGB-for-object-detection
This project summarizes some core traditional visual algorithms commonly used in all drone competitions during undergraduate studies
该项目总结了本科期间参加所有无人机竞赛时常用的一些核心传统视觉算法

传统算法做目标检测有一个很常用的方法是使用颜色识别，可以称为色块检测，具体流程分为三步：

1.提取包含目标的视频帧，读取目标的HSV或者RGB等其他色域其中一种或多种的三个通道范围--readhsv.py

2.在第一步返回的通道范围基础上进一步微调范围以达到最优效果--Fine_tuning_range.py

3.使用微调后的最优范围作为先验条件以对视频流做检测，返回目标的位置--color_track.py
