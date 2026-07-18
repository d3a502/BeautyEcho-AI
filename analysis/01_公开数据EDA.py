from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd


ROOT = Path(__file__).resolve().parents[1]
OUTPUT_DIR = ROOT / "outputs" / "figures"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)


def resolve_data_path() -> Path:
    candidates = [
        ROOT / "data" / "public_beauty_data.csv",
        ROOT.parent / "archive" / "public_beauty_data.csv",
        ROOT / "data" / "skincare_df.csv",
        ROOT.parent / "archive" / "skincare_df.csv",
    ]
    for candidate in candidates:
        if candidate.exists():
            return candidate
    raise FileNotFoundError(
        "未找到公开美妆数据文件，请将 public_beauty_data.csv 放到 data/ 目录，"
        "或放在仓库同级目录 archive/ 下。当前脚本也兼容 skincare_df.csv。"
    )


def main() -> None:
    data_path = resolve_data_path()
    df = pd.read_csv(data_path).drop(columns=["Unnamed: 0"], errors="ignore")

    brand_summary = (
        df.groupby("brand")
        .agg(product_count=("name", "count"), avg_score=("review_score", "mean"))
        .query("product_count >= 5")
        .sort_values("avg_score", ascending=False)
        .head(12)
    )

    fig, ax = plt.subplots(figsize=(10, 6))
    brand_summary["avg_score"].sort_values().plot(
        kind="barh",
        color="#8BB7A7",
        edgecolor="#6C9689",
        ax=ax,
    )
    ax.set_title("Top Brands by Average Review Score", fontsize=13)
    ax.set_xlabel("Average Review Score")
    ax.set_ylabel("")
    plt.tight_layout()
    plt.savefig(OUTPUT_DIR / "top_brands_by_score.png", dpi=180)
    plt.close(fig)

    fig, ax = plt.subplots(figsize=(10, 6))
    ax.scatter(
        df["price"],
        df["review_score"],
        s=28,
        alpha=0.55,
        color="#9CB8D8",
        edgecolors="none",
    )
    ax.set_title("Price vs Review Score", fontsize=13)
    ax.set_xlabel("Price")
    ax.set_ylabel("Review Score")
    plt.tight_layout()
    plt.savefig(OUTPUT_DIR / "price_vs_score.png", dpi=180)
    plt.close(fig)

    print("Rows:", len(df))
    print("Columns:", len(df.columns))
    print("Saved figures to:", OUTPUT_DIR)


if __name__ == "__main__":
    main()
