#!/usr/bin/env python3

import sys

for line in sys.stdin:
    line = line.strip()

    if not line:
        continue
    try:
        product_id, rating = line.split("\t")
        rating = float(rating)

        print(f"{product_id}\t{rating}")

    except ValueError:
        continue
