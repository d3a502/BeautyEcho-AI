from pathlib import Path

import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, r2_score
from sklearn.model_selection import train_test_split


ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "outputs" / "公开数据评分预测摘要.txt"


def resolve_data_path() -> Path:
    candidates = [
        ROOT / "data" / "skincare_df.csv",
        ROOT.parent / "archive" / "skincare_df.csv",
    ]
    for candidate in candidates:
        if candidate.exists():
            return candidate
    raise FileNotFoundError(
        "未找到 Sephora 数据集，请将 skincare_df.csv 放到 data/ 目录，"
        "或放在仓库同级目录 archive/ 下。"
    )


def main() -> None:
    data_path = resolve_data_path()
    df = pd.read_csv(data_path).drop(columns=["Unnamed: 0"], errors="ignore")

    feature_cols = [
        "price",
        "n_of_reviews",
        "n_of_loves",
        "size",
        "clean_product",
        "reviews_to_loves_ratio",
        "return_on_reviews",
        "price_per_ounce",
    ]
    model_df = df[feature_cols + ["review_score"]].dropna()

    x_train, x_test, y_train, y_test = train_test_split(
        model_df[feature_cols],
        model_df["review_score"],
        test_size=0.2,
        random_state=42,
    )

    model = RandomForestRegressor(n_estimators=300, random_state=42)
    model.fit(x_train, y_train)
    pred = model.predict(x_test)

    lines = [
        "公开数据评分预测基线",
        f"样本量: {len(model_df)}",
        f"MAE: {mean_absolute_error(y_test, pred):.4f}",
        f"R2: {r2_score(y_test, pred):.4f}",
        "",
        "Top Features:",
    ]

    importances = (
        pd.Series(model.feature_importances_, index=feature_cols)
        .sort_values(ascending=False)
        .head(5)
    )
    for name, value in importances.items():
        lines.append(f"- {name}: {value:.4f}")

    OUTPUT.write_text("\n".join(lines), encoding="utf-8")
    print("\n".join(lines))
    print("Saved:", OUTPUT)


if __name__ == "__main__":
    main()
