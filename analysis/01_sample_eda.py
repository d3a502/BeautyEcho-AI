from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data" / "sample_beauty_reviews.csv"
FIGURES = ROOT / "outputs" / "figures"
FIGURES.mkdir(parents=True, exist_ok=True)


def main() -> None:
    df = pd.read_csv(DATA)

    rating_counts = df["rating"].value_counts().sort_index()
    ax = rating_counts.plot(kind="bar", color="#8f5fe8", title="Sample Rating Distribution")
    ax.set_xlabel("Rating")
    ax.set_ylabel("Count")
    plt.tight_layout()
    plt.savefig(FIGURES / "rating_distribution.png", dpi=160)
    plt.close()

    product_counts = df["product_type"].value_counts()
    ax = product_counts.plot(kind="bar", color="#4f9d8f", title="Sample Product Type Distribution")
    ax.set_xlabel("Product Type")
    ax.set_ylabel("Count")
    plt.tight_layout()
    plt.savefig(FIGURES / "product_type_distribution.png", dpi=160)
    plt.close()

    print("Rows:", len(df))
    print("Saved figures to:", FIGURES)


if __name__ == "__main__":
    main()

