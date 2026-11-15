import pyarrow.parquet as pq
import pandas as pd
import glob
import os

files = sorted(glob.glob(
    os.path.expanduser("~/product_review_analytics/dataset/*.parquet")
))
parquet_file = pq.ParquetFile(files[0])
samples = []

for batch_no, batch in enumerate(
    parquet_file.iter_batches(
        batch_size=50000,
        columns=["rating", "text"]
    )
):
    df = batch.to_pandas()
    df = df.dropna(subset=["rating", "text"])
    df["text"] = df["text"].astype(str).str.strip()
    df = df[df["text"].str.len() > 0]

    negative = df[df["rating"].isin([1.0, 2.0])].sample(
        n=min(300, len(df[df["rating"].isin([1.0, 2.0])])),
        random_state=batch_no
    )

    positive = df[df["rating"].isin([4.0, 5.0])].sample(
        n=min(300, len(df[df["rating"].isin([4.0, 5.0])])),
        random_state=batch_no
    )

    negative = negative.copy()
    positive = positive.copy()

    negative["sentiment"] = 0
    positive["sentiment"] = 1

    samples.extend([negative, positive])

    print("Processed batch:", batch_no + 1)

result = pd.concat(samples, ignore_index=True)
result = result.sample(frac=1, random_state=42)

output = os.path.expanduser(
    "~/product_review_analytics/ml/reviews_sample.csv"
)

result[["text", "sentiment"]].to_csv(output, index=False)

print("\nDataset created successfully!")
print("Total samples:", len(result))
print("\nSentiment distribution:")
print(result["sentiment"].value_counts())
print("\nSaved to:", output)
