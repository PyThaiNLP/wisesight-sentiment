# Wisesight-Sentiment Corpus

Social media message with sentiment label (positive, neutral, negative, question). Released to public domain.

Last update: 2019-03-31

## Source

- Size: ~26,700 messages
- Language: Central Thai
- Style: Informal and conversational. With some news headlines and advertisement.
- Time period: Around 2016 to early 2019. With small amount from other period.
- Domains: Mixed. Majority are consumer products and services (restaurants, cosmetics, drinks, car, hotels), with some current affairs.
- Privacy:
  - Only messages that made available to the public on the internet (websites, blogs, social network sites).
  - For Facebook, this means the public comments (everyone can see) that made on a public page.
  - Private/protected messages and messages in groups, chat, and inbox are not included.
- Alternations and modifications:
  - Keep in mind that this corpus does not statistically represent anything in the language register.
  - Large amount of messages are not in their original form. Personal data are removed or masked.
  - Duplicated, leading, and trailing whitespaces are removed. Other punctuations, symbols, and emojis are kept intact.
  - (Mis)spellings are kept intact.
  - Messages longer than 2,000 characters are removed.
  - Long non-Thai messages are removed. Duplicated message (exact match) are removed.

## Corpus file structure

- All files are UTF-8 encoded plaintext
- One message per line. A newline character in the original message will be replaced with a space.
- `q.txt` Questions (~500 messages)
- `neg.txt` Message with negative sentiment (~6,800)
- `neu.txt` Message with neutral sentiment (~14,500)
- `pos.txt` Message with positive sentiment (~4,700)
- Exact dataset are also provided in Kaggle competition format, inside `kaggle-competition/` directory:
  - `train.txt` - Message for training (24,066 messages)
  - `train_label.txt` - Label for training. Each line is the label corresponding to the same line in `train.txt`
  - `test.txt` - Message for testing (2,674 messages)
  - `test_label.txt` - Label for testing. Each line is the label corresponding to the same line in `test.txt`
  - `test_majority.csv` - Sample submission in Kaggle format. Contains `neu` class as all the predictions.
  - `test_solution.csv` - Test solution in Kaggle format.
  - Sample code for data exploration, training, and prediction are also provided.


## Sentiment value annotation

- Sentiment values are assigned by human annotators.
- A human annotator put his/her best effort to assign just one label, out of three, to a message.
- A message can be ambiguous. When possible, the judgement will be based solely on the text itself.
  - In some situation, like when the context is missing, the annotator may have to rely on his/her own world knowledge and just guess.
  - In some cases, the human annotator may have an access to the message's context, like an image. These additional information are not included as part of this corpus.
- Agreement, enjoyment, and satisfaction are positive. Disagreement, sadness, and disappointment are negative.
- Showing interest in a topic or in a product is counted as positive.
  - In this sense, a question about a particular product could has a positive sentiment value, if it shows the interest in the product.
- Saying that other product or service is better is counted as negative.
- General information or news title tend to be counted as neutral.

## Classification Benchmark

pyThaiNLP uses this dataset as part of its [text classification benchmark](https://github.com/PyThaiNLP/classification-benchmarks). We use the same performance metric as [WISESIGHT Sentiment Analysis](https://www.kaggle.com/c/wisesight-sentiment/) competition, which is **accuracy**.

**Disclaimer** Note that the labels are obtained manually and are prone to errors so if you are planning to apply the models in the benchmark for real-world applications, be sure to benchmark it with **your own dataset**.

| Model               | Public Accuracy | Private Accuracy |
|---------------------|-----------------|------------------|
| Logistic Regression | 0.72781         | 0.7499           |
| FastText            | 0.63144         | 0.6131           |
| ULMFit              | 0.71259         | 0.74194          |
| ULMFit Semi-supervised    | 0.73119     | 0.75859      |
| ULMFit Semi-supervised Repeated One Time    | **0.73372**     | **0.75968**      |

See classification codes in `competition.ipynb` and data exploration in `exploration.ipynb`


## Personal data

- We trying to exclude personally identifiable information from this data set.
- Usernames and non-public figure names are removed
- Phone numbers are masked (e.g. 088-888-8888, 09-9999-9999, 0-2222-2222)
- If you see any personal data still remain in the set, please tell us - so we can remove them.


## Copyright and Disclaimer

- If applicable, copyright of each message content belongs to the original poster.
- Annotation data (labels) are released to public domain.
- [Wisesight (Thailand) Co., Ltd.](https://wisesight.com/) helps facilitate the annotation, but does not necessarily agree upon the labels made by the human annotators. This annotation is for research purpose and does not reflect the professional work that Wisesight has been done for its customers.
- The human annotator does not necessarily agree or disagree with the message. Likewise, the label he/she made to the message does not necessarily reflect his/her personal view towards the message.


## Acknowledgement

Thanks [PyThaiNLP](https://github.com/PyThaiNLP/pythainlp) community, [Kitsuchart Pasupa](http://www.it.kmitl.ac.th/~kitsuchart/) (Faculty of Information Technology, King Mongkut's Institute of Technology Ladkrabang), and [Ekapol Chuangsuwanich](https://www.cp.eng.chula.ac.th/en/about/faculty/ekapolc/) (Faculty of Engineering, Chulalongkorn University) for advice.
