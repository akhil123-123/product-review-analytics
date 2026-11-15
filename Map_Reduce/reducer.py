#!/usr/bin/env python3

import sys
current_product = None
total_reviews = 0
rating_sum = 0.0
rating_counts = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0}

def output_result(product, total, rating_sum, counts):
    if product is not None and total > 0:
        average = rating_sum / total

        print(
            f"{product}\t{total}\t{rating_sum:.2f}\t"
            f"{average:.2f}\t"
            f"{counts[1]}\t{counts[2]}\t{counts[3]}\t"
            f"{counts[4]}\t{counts[5]}"
        )

for line in sys.stdin:
    try:
        product, rating = line.strip().split("\t")
        rating = float(rating)

        if rating < 1 or rating > 5:
            continue

        if product != current_product:
            output_result(
                current_product, total_reviews,
                rating_sum, rating_counts
            )

            current_product = product
            total_reviews = 0
            rating_sum = 0.0
            rating_counts = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0}

        total_reviews += 1
        rating_sum += rating

        star = int(rating)
        if rating == star:
            rating_counts[star] += 1

    except (ValueError, IndexError):
        continue

output_result(
    current_product, total_reviews,
    rating_sum, rating_counts
)
