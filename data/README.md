# 数据说明

本目录用于存放小样例数据和公开数据集抽样结果。

当前仓库不上传大型公开数据集。原因：

- 避免仓库体积过大。
- 避免违反数据集分发条款。
- 保持报名阶段材料轻量、可读。

推荐做法：

1. 在本地下载或抽样公开数据集。
2. 将清洗后的小样例保存为 CSV。
3. 在 `research/references.md` 中注明来源。
4. 不上传未经授权的完整第三方数据。

当前小样例：

- `sample_beauty_reviews.csv`：用于验证 EDA、聚类和评分预测流程。
- `amazon_all_beauty_sample.csv`：从 Amazon Reviews 2023 All Beauty 公开数据中抽取的小样本，不包含 `user_id` 和图片字段。
