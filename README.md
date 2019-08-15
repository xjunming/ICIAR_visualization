# ICIAR_visualization

## 关于环境设置

如果有需要，可以在虚拟环境下安装该环境，步骤为如下

- `pip install virtualenv` 安装virtualenv

- `virtualenv venv` 创建一个虚拟环境
- `source venv/bin/active` 激活环境

安装该项目的环境`pip install -r requirement.txt `

## 关于文件说明

`count_color.py` 是统计黑、灰、白、红、橙、黄、绿、青、蓝和紫颜色的像素，输出各个颜色的像素数量，作为k-means聚类的特征向量；

`dominant_color.py` 是根据像素的均值来判断一张图片的**一种**主颜色，返回这张图的主颜色的(R,G,B)；

`k_means_class.py` 是用上面其中之一的代码作为特征向量，来做k-means聚类；

`visualization.ipynb` 最后，可视化该聚类效果。
