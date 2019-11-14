***NOTES: The most recent tutorial is being updated at https://github.com/PyThaiNLP/tutorials***

----

This directory contains data files in Kaggle competition format and Jupyter notebook (Python) for training, prediction, and evaluation.

## Classification Benchmark

PyThaiNLP uses Wisesight Sentiment dataset as part of its [text classification benchmark](https://github.com/PyThaiNLP/classification-benchmarks). We use the same performance metric as [Wisesight Sentiment Analysis](https://www.kaggle.com/c/wisesight-sentiment/) competition, which is **accuracy**.

**Disclaimer** Note that the labels are obtained manually and are prone to errors so if you are planning to apply the models in the benchmark for real-world applications, be sure to benchmark it with **your own dataset**.

| Model               | Public Accuracy | Private Accuracy |
|---------------------|-----------------|------------------|
| Logistic Regression | 0.72781         | 0.7499           |
| FastText            | 0.63144         | 0.6131           |
| ULMFit              | 0.71259         | 0.74194          |
| ULMFit Semi-supervised    | 0.73119     | 0.75859      |
| ULMFit Semi-supervised Repeated One Time    | **0.73372**     | **0.75968**      |

See classification code in `competition.ipynb`.

`text_generation.ipynb` is used to generate extra training data.
