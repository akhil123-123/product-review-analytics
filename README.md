# Product Review Analytics Using Hadoop MapReduce and Machine Learning

## Project Overview
This project analyzes Amazon Electronics customer reviews using Apache Hadoop MapReduce and Machine Learning.

It combines large-scale product review analytics with sentiment classification using Logistic Regression.

## Dataset Details
- Dataset: Amazon Reviews 2023 - Electronics
- Platform: Hugging Face
- URL: https://huggingface.co/datasets/McAuley-Lab/Amazon-Reviews-2023
- Total Reviews: 43,886,944
- Unique Products: 1,946,161

## Technologies Used
- Python 3.14.1
- Apache Hadoop 3.3.6
- Hadoop MapReduce
- HDFS
- Hadoop Streaming
- Scikit-learn
- TF-IDF
- Logistic Regression
- Ubuntu Linux

## Project Modules

### 1. Big Data Analytics
- Custom Python Mapper and Reducer.
- Processed Amazon reviews using Hadoop Streaming.
- Calculated product-wise review counts.
- Calculated average product ratings.
- Generated 1-star to 5-star rating distributions.
- Identified most-reviewed and highest-rated products.

### 2. Sentiment Analysis
- Feature extraction using TF-IDF.
- Classification using Logistic Regression.
- 1–2 star reviews labelled Negative.
- 4–5 star reviews labelled Positive.
- 3-star reviews excluded.

The initial ML experiment used 15,600 balanced reviews sampled from the first Parquet file.

## Machine Learning Results

| Metric | Score |
|---|---:|
| Accuracy | 87.93% |
| Precision | 88.57% |
| Recall | 86.09% |
| F1 Score | 87.31% |

Training samples: 12,480  
Testing samples: 3,120

## Hadoop Results

| Metric | Result |
|---|---:|
| Total Input Reviews | 44,512,987 |
| Valid Reviews | 44,512,983 |
| Excluded Reviews | 4 |
| Unique Products | 1,953,407 |
| Overall Average Rating | 4.10217 |

## Project Structure

```text
product_review_analytics/
├── mapreduce/
│   ├── mapper.py
│   ├── reducer.py
│   └── sample.txt
├── ml/
│   ├── inspect_dataset.py
│   ├── prepare_data.py
│   ├── train_model.py
│   └── logistic_regression_model.pkl
├── results/
│   └── project_summary.txt
├── .gitignore
└── README.md
