from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data" / "amazon_all_beauty_sample.csv"
FIGURES = ROOT / "outputs" / "figures"
SUMMARY = ROOT / "outputs" / "amazon_public_sample_summary.txt"
FIGURES.mkdir(parents=True, exist_ok=True)


def main() -> None:
    df = pd.read_csv(DATA)

    rating_counts = df["rating"].value_counts().sort_index()
    ax = rating_counts.plot(kind="bar", color="#8f5fe8", title="Amazon All Beauty Sample Rating Distribution")
    ax.set_xlabel("Rating")
    ax.set_ylabel("Review Count")
    plt.tight_layout()
    plt.savefig(FIGURES / "amazon_rating_distribution.png", dpi=160)
    plt.close()

    verified_counts = df["verified_purchase"].value_counts()
    ax = verified_counts.plot(kind="bar", color="#4f9d8f", title="Verified Purchase Distribution")
    ax.set_xlabel("Verified Purchase")
    ax.set_ylabel("Review Count")
    plt.tight_layout()
    plt.savefig(FIGURES / "amazon_verified_purchase_distribution.png", dpi=160)
    plt.close()

    text_lengths = df["text"].fillna("").astype(str).str.len()
    summary = [
        f"Rows: {len(df)}",
        f"Average rating: {df['rating'].mean():.2f}",
        f"Average review length: {text_lengths.mean():.1f} characters",
        f"Verified purchase ratio: {df['verified_purchase'].mean():.2%}",
    ]
    SUMMARY.write_text("\n".join(summary) + "\n", encoding="utf-8")
    print("\n".join(summary))
    print("Saved figures to:", FIGURES)


if __name__ == "__main__":
    main()

