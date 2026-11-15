import pyarrow.parquet as pq
import glob
import os

files = glob.glob(
    os.path.expanduser(
        "~/product_review_analytics/dataset/*.parquet"
    )
)
print("Total Parquet files:", len(files))

table = pq.read_table(
    files[0],
    columns=["asin", "rating", "text"]
)

print("\nDataset columns:")
print(table.schema)

print("\nSample reviews:")
for row in table.slice(0, 3).to_pylist():
    print(row)
