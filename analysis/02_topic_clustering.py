from pathlib import Path

import pandas as pd
from sklearn.cluster import KMeans
from sklearn.feature_extraction.text import TfidfVectorizer


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data" / "sample_beauty_reviews.csv"
OUTPUT = ROOT / "outputs" / "topic_clusters.csv"


def main() -> None:
    df = pd.read_csv(DATA)
    texts = df["review_text"].astype(str)

    vectorizer = TfidfVectorizer(analyzer="char", ngram_range=(2, 3), min_df=1)
    matrix = vectorizer.fit_transform(texts)

    model = KMeans(n_clusters=3, random_state=42, n_init=10)
    df["cluster"] = model.fit_predict(matrix)
    df.to_csv(OUTPUT, index=False)

    print("Cluster summary:")
    for cluster_id, group in df.groupby("cluster"):
        print(f"\nCluster {cluster_id}")
        for text in group["review_text"].tolist():
            print("-", text)
    print("\nSaved:", OUTPUT)


if __name__ == "__main__":
    main()

