from pathlib import Path

import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data" / "amazon_all_beauty_sample.csv"
OUTPUT = ROOT / "outputs" / "amazon_rating_prediction_report.txt"


def main() -> None:
    df = pd.read_csv(DATA)
    df["review_text"] = (df["title"].fillna("") + " " + df["text"].fillna("")).str.strip()
    df["high_rating"] = (df["rating"] >= 4).astype(int)

    x_train, x_test, y_train, y_test = train_test_split(
        df["review_text"],
        df["high_rating"],
        test_size=0.25,
        random_state=42,
        stratify=df["high_rating"],
    )

    model = Pipeline(
        [
            ("tfidf", TfidfVectorizer(stop_words="english", max_features=3000, ngram_range=(1, 2))),
            ("clf", LogisticRegression(max_iter=1000)),
        ]
    )
    model.fit(x_train, y_train)
    predictions = model.predict(x_test)

    report = classification_report(y_test, predictions, zero_division=0)
    OUTPUT.write_text(report, encoding="utf-8")
    print(report)
    print("Saved:", OUTPUT)


if __name__ == "__main__":
    main()

