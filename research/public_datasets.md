# 公开数据集调研

本文件记录可用于美妆用户反馈分析、评分预测和内容策略研究的公开数据集。

## 1. Amazon Reviews 2023

链接：

- https://amazon-reviews-2023.github.io/
- https://huggingface.co/datasets/McAuley-Lab/Amazon-Reviews-2023

适用方向：

- Beauty and Personal Care / All Beauty 类目评论分析。
- 评论评分预测。
- 用户满意度分类。
- 商品元数据与评论文本关联。

可做分析：

- 评分分布。
- 高低评分评论关键词差异。
- 用户反馈主题聚类。
- 评论文本预测高评分/低评分。

注意：

- 数据规模较大，报名阶段建议只抽样使用。
- 使用时需注明来源和数据集名称。

## 2. Sephora Products and Skincare Reviews

链接：

- https://www.kaggle.com/datasets/nadyinky/sephora-products-and-skincare-reviews

适用方向：

- 护肤/美妆产品评论。
- 产品属性、评分、品牌和用户反馈分析。
- 与美妆场景较贴近，适合作为方案展示数据来源。

可做分析：

- 品牌评分对比。
- 产品类型与评分分布。
- 评论主题聚类。
- 高评分产品的关键词提取。

注意：

- Kaggle 数据集通常需要登录下载。
- 不建议直接把完整数据上传到仓库。

## 3. Cosmetics Ingredients Dataset

链接：

- https://www.kaggle.com/datasets/kingabzpro/cosmetics-datasets

适用方向：

- 成分、价格、品类、适用肤质分析。
- 产品卖点与用户需求匹配。
- 美妆产品标签体系构建。

可做分析：

- 不同品类常见成分。
- 价格分布。
- 适用肤质标签。
- 产品特征与内容卖点映射。

## 当前选择

报名阶段优先使用公开数据集做研究计划和小样例验证；若时间允许，优先抽样 Amazon Reviews 2023 或 Sephora Reviews 做 EDA、聚类和评分预测。

