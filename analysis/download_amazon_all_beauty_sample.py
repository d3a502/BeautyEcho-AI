from __future__ import annotations

import csv
import gzip
import json
import urllib.request
from itertools import islice
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "data" / "amazon_all_beauty_sample.csv"
SOURCE_URL = "https://mcauleylab.ucsd.edu/public_datasets/data/amazon_2023/raw/review_categories/All_Beauty.jsonl.gz"


def main(limit: int = 500) -> None:
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    fields = ["rating", "title", "text", "asin", "parent_asin", "helpful_vote", "verified_purchase"]

    with urllib.request.urlopen(SOURCE_URL, timeout=30) as response:
        with gzip.GzipFile(fileobj=response) as gz_file:
            rows = []
            for line in islice(gz_file, limit):
                raw = json.loads(line)
                rows.append({field: raw.get(field) for field in fields})

    with OUTPUT.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields)
        writer.writeheader()
        writer.writerows(rows)

    print(f"Saved {len(rows)} rows to {OUTPUT}")
    print(f"Source: {SOURCE_URL}")


if __name__ == "__main__":
    main()

