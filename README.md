---
SPDX-License-Identifier: CC0-1.0
---

# Wisesight Sentiment Corpus

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.3457446.svg)](https://doi.org/10.5281/zenodo.3457446)

ข้อความภาษาไทยจากสื่อสังคมออนไลน์ พร้อมกับป้ายกำกับความรู้สึก (บวก, กลางๆ, ลบ, คำถาม) รวม 26,737 ข้อความ
**เผยแพร่เป็นสมบัติสาธารณะ** ภายใต้[สัญญาอนุญาต Creative Commons Zero v1.0 Universal][cc]

Social media messages in Thai language with sentiment label (positive, neutral, negative, question).
**Released to public domain** under [Creative Commons Zero v1.0 Universal license][cc].

[cc]: https://creativecommons.org/publicdomain/zero/1.0/

## Changelog

- 2024-11-06 - Release v1.0.1 with updated contributors
- 2020-12-01 - Add Hugging Face format - [PR #7](https://github.com/PyThaiNLP/wisesight-sentiment/pull/7)
- 2019-10-01 - Fix path in data preparation notebook - [PR #6](https://github.com/PyThaiNLP/wisesight-sentiment/pull/6)
- 2019-08-22 - Add tokenization annotation for ~1,000 samples - [PR #4](https://github.com/PyThaiNLP/wisesight-sentiment/pull/4)
- 2019-07-03 - Add tokenization annotation for 160 samples - [PR #2](https://github.com/PyThaiNLP/wisesight-sentiment/pull/2)
- 2019-03-31 - Update data

## Related corpus

- For `wisesight-160` and `wisesight-1000`, which are samples from this corpus in a tokenized form,
  see <https://github.com/PyThaiNLP/wisesight-sentiment/tree/master/word-tokenization>

- For data exploration and classification examples,
  see [Thai Text Classification Benchmarks](https://github.com/PyThaiNLP/classification-benchmarks).

- Also available as Huggingface datasets:
  - [wisesight_sentiment](https://huggingface.co/datasets/wisesight_sentiment)
    (using the earlier version of this corpus)
  - [wisesight1000](https://huggingface.co/datasets/wisesight1000)

## Source

- Size: 26,737 messages
- Language: Central Thai
- Style: Informal and conversational. With some news headlines and advertisement.
- Time period: Around 2016 to early 2019. With small amount from other period.
- Domains: Mixed. Majority are consumer products and services
  (restaurants, cosmetics, drinks, car, hotels), with some current affairs.
- Privacy:
  - Only messages that made available to the public on the internet
    (websites, blogs, social network sites).
  - For Facebook, this means the public comments (everyone can see) that made on a public page.
  - Private/protected messages and messages in groups, chat, and inbox are not included.
- Alternations and modifications:
  - Keep in mind that this corpus does not statistically represent anything in the language register.
  - Large amount of messages are not in their original form. Personal data are removed or masked.
  - Duplicated, leading, and trailing whitespaces are removed.
    Other punctuations, symbols, and emojis are kept intact.
  - (Mis)spellings are kept intact.
  - Messages longer than 2,000 characters are removed.
  - Long non-Thai messages are removed. Duplicated message (exact match) are removed.
- More characteristics of the data can be explored by this
  [notebook](https://github.com/PyThaiNLP/wisesight-sentiment/blob/master/exploration.ipynb).

## Corpus file structure

- All files are UTF-8 encoded plaintext
- One message per line. A newline character in the original message will be replaced with a space.
- `q.txt` Questions (575 messages)
- `neg.txt` Message with negative sentiment (6,823)
- `neu.txt` Message with neutral sentiment (14,561)
- `pos.txt` Message with positive sentiment (4,778)
- The legacy dataset in Kaggle competition format is also provided inside `kaggle-competition/` directory:
  - `train.txt` - Message for training (24,066 messages)
  - `train_label.txt` - Label for training. Each line is the label corresponding to the same line in `train.txt`
  - `test.txt` - Message for testing (2,674 messages)
  - `test_label.txt` - Label for testing. Each line is the label corresponding to the same line in `test.txt`
  - `test_majority.csv` - Sample submission in Kaggle format. Contains `neu` class as all the predictions.
  - `test_solution.csv` - Test solution in Kaggle format.
  - Sample code for data exploration, training, and prediction are also provided.

## Personal data

- We trying to exclude any known personally identifiable information from this data set.
- Usernames and non-public figure names are removed
- Phone numbers are masked (e.g. 088-888-8888, 09-9999-9999, 0-2222-2222)
- If you see any personal data still remain in the set, please tell us - so we can remove them.

## Sentiment value annotation methodology

- Sentiment values are assigned by human annotators.
- A human annotator put his/her best effort to assign just one label, out of three, to a message.
- A message can be ambiguous. When possible, the judgement will be based solely on the text itself.
  - In some situation, like when the context is missing, the annotator may have to rely on his/her own world knowledge and just guess.
  - In some cases, the human annotator may have access to the message's context, like an image.
    These additional information are not included as part of this corpus.
- Agreement, enjoyment, and satisfaction are positive. Disagreement, sadness, and disappointment are negative.
- Showing interest in a topic or in a product is counted as positive.
  - In this sense, a question about a particular product could have a positive sentiment value, if it shows the interest in the product.
- Saying that other product or service is better is counted as negative.
- General information or news title tend to be counted as neutral.

## Copyright and Disclaimer

- If applicable, copyright of each message content belongs to the original poster.
- **Annotation data (labels) are released to public domain.**
- [Wisesight (Thailand) Co., Ltd.](https://github.com/wisesight/) helps facilitate the annotation,
  but does not necessarily agree upon the labels made by the human annotators.
  This annotation is for research purpose and does not reflect the professional work that Wisesight has been done for its customers.
- The human annotator does not necessarily agree or disagree with the message.
  Likewise, the label he/she made to the message does not necessarily reflect his/her personal view towards the message.

## Citation

Please cite the following if you make use of the dataset:

> Arthit Suriyawongkul, Ekapol Chuangsuwanich, Pattarawat Chormai, Nitchakarn Chantarapratin, Ponrawee Prasertsom, Jitkapat Sawatphol, Nozomi Yamada, Attapol Rutherford, Charin Polpanumas, and Can Udomcharoenchaikit. 2024. **PyThaiNLP/Wisesight Sentiment Corpus with Word Tokenization Label (Version 1.0.1)** November.

BibTeX:

```
@software{Suriyawongkul_PyThaiNLP_Wisesight_Sentiment_Corpus_2020,
  author       = {Suriyawongkul, Arthit and
                  Chuangsuwanich, Ekapol and
                  Chormai, Pattarawat and
                  Chantarapratin, Nitchakarn and
                  Prasertsom, Ponrawee and
                  Sawatphol, Jitkapat and
                  Yamada, Nozomi and
                  Rutherford, Attapol and
                  Polpanumas, Charin and
                  Udomcharoenchaikit, Can},
  doi          = {10.5281/zenodo.3457446},
  license      = {CC0-1.0},
  month        = nov,
  publisher    = {Zenodo},
  title        = {{PyThaiNLP/Wisesight Sentiment Corpus with Word Tokenization Label}},
  url          = {https://doi.org/10.5281/zenodo.3457446},
  version      = {v1.0.1},
  year         = 2024
}
```

## Acknowledgement

- Thanks [PyThaiNLP](https://github.com/PyThaiNLP/pythainlp) community and
  [Kitsuchart Pasupa](https://www.it.kmitl.ac.th/~kitsuchart/)
  (Faculty of Information Technology, King Mongkut's Institute of Technology
  Ladkrabang) for advice.
- The tokenization annotation was done by the support of
  the [Natural Language Processing Lab](https://attapol.github.io/lab.html)
  at Department of Linguistics, Faculty of Arts, Chulalongkorn University.
- The original Kaggle competition, by Ekapol Chuangsuwanich,
  using the earlier version of this corpus,
  can be found at <https://www.kaggle.com/c/wisesight-sentiment/>.
