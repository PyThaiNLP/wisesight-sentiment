---
SPDX-License-Identifier: CC0-1.0
---

# Wisesight Sentiment Corpus

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.3457446.svg)](https://doi.org/10.5281/zenodo.3457446)

ข้อความภาษาไทยจากสื่อสังคมออนไลน์ พร้อมกับป้ายกำกับความรู้สึก (บวก, กลางๆ, ลบ, คำถาม)
รวม 26,737 ข้อความ
**เผยแพร่เป็นสมบัติสาธารณะ** โดยการสละสิทธิ์ตาม [CC0 1.0 Universal][cc0]

Social media messages in Thai language with sentiment label
(positive, neutral, negative, question). Contains 26,737 messages.
**Dedicated to the public domain** under [CC0 1.0 Universal][cc0].

## Table of contents

- [Changelog](#changelog)
- [Data characteristics and preprocessing](#data-characteristics-and-preprocessing)
- [Annotation methodology](#annotation-methodology)
- [Corpus file structure](#corpus-file-structure)
- [Copyright and disclaimer](#copyright-and-disclaimer)
- [Citation](#citation)
- [Acknowledgement](#acknowledgement)
- [Additional resources](#additional-resources)

## Changelog

- 2024-11-07: Released v1.1 with updated copyright text, contributors,
  and a software bill of materials (SBOM).
- 2020-12-01: Added Hugging Face format
  [PR #7](https://github.com/PyThaiNLP/wisesight-sentiment/pull/7)
- 2019-10-01: Fixed path in data preparation notebook
  [PR #6](https://github.com/PyThaiNLP/wisesight-sentiment/pull/6)
- 2019-08-22: Added tokenization annotation for ~1,000 samples
  [PR #4](https://github.com/PyThaiNLP/wisesight-sentiment/pull/4)
- 2019-07-03: Added tokenization annotation for 160 samples
  [PR #2](https://github.com/PyThaiNLP/wisesight-sentiment/pull/2)
- 2019-03-31: Updated data.

## Data characteristics and preprocessing

*This corpus does not claim to be a statistically representative sample of the
Thai language register.*

General information:

- **Size:** 26,737 messages.
- **Language:** Central Thai.
- **Style:**
  Informal and conversational, with some news headlines and advertisements.

Data coverage:

- **Time period:**
  Approximately 2016 to early 2019, with a small amount from other periods.
- **Domains:**
  Mixed, with a majority focusing on consumer products and services
  (restaurants, cosmetics, drinks, cars, hotels).
  Some current affairs topics are also included.

Privacy:

- Messages were collected from publicly available online sources only
  (websites, blogs, social network sites).
- For Facebook data, this includes public comments on public pages.
- The dataset does not contain private/protected messages or messages from
  groups, chats, and inboxes.
- Personally identifiable information has been removed or masked.

Data alterations and modifications:

- A large portion of messages are not in their original form:
  - Usernames and non-public figure names are removed.
  - Phone numbers are masked (e.g., 088-888-8888, 09-9999-9999, 0-2222-2222).
  - Duplicated, leading, and trailing whitespaces are removed.
  - Other punctuations, symbols, and emojis are retained.
  - Misspellings remain uncorrected.
- Messages exceeding 2,000 characters or non-Thai messages are removed.
- Duplicate messages (exact matches) are removed.

Further exploration:

- Refer to [sbom.spdx3.json](./sbom.spdx3.json) for a machine-readable data
  bill of materials (BOM) in [SPDX 3.0](https://spdx.dev/use/specifications/)
  format.
- Explore additional data characteristics using this
  [notebook](https://github.com/PyThaiNLP/wisesight-sentiment/blob/master/exploration.ipynb).

## Annotation methodology

- Sentiment values are assigned by human annotators.
- A human annotator put his/her best effort to assign just one label,
  out of four, to a message.
- A message can be ambiguous. When possible, the judgement will be based solely
  on the text itself.
  - In some situation, like when the context is missing, the annotator may have
    to rely on his/her own world knowledge and just guess.
  - In some cases, the human annotator may have access to the message's
    context, like an image.
    These additional information are not included as part of this corpus.
- Agreement, enjoyment, and satisfaction are positive. Disagreement, sadness,
  and disappointment are negative.
- Showing interest in a topic or in a product is counted as positive.
  - In this sense, a question about a particular product could have a positive
    sentiment value, if it shows the interest in the product.
- Saying that other product or service is better is counted as negative.
- General information or news title tend to be counted as neutral.
- For word tokenization annotation methodology, please refer to
  [word-tokenization/README.md](./word-tokenization/README.md).

## Corpus file structure

- All files are UTF-8 encoded plaintext.
- One message per line.
- A newline character in the original message will be replaced with a space.
- `q.txt`: Questions (575 messages).
- `neg.txt`: Message with negative sentiment (6,823).
- `neu.txt`: Message with neutral sentiment (14,561).
- `pos.txt`: Message with positive sentiment (4,778).
- [huggingface](./huggingface/) directory contains an archive file meant to be
  fetched by Hugging Face Datasets
- [kaggle-competition/](./kaggle-competition/) directory contains the legacy
  dataset in Kaggle competition format:
  - `train.txt`: Message for training (24,066 messages).
  - `train_label.txt`: Label for training.
    Each line is the label corresponding to the same line in `train.txt`.
  - `test.txt` - Message for testing (2,674 messages)
  - `test_label.txt`: Label for testing.
    Each line is the label corresponding to the same line in `test.txt`.
  - `test_majority.csv`: Sample submission in Kaggle format.
    Contains `neu` class as all the predictions.
  - `test_solution.csv`: Test solution in Kaggle format.
  - Sample code for data exploration, training, and prediction are provided.
- [word-tokenization](./word-tokenization/) directory contains
  `wisesight-160` and `wisesight-1000` datasets,
  which are samples from the full corpus in a tokenized form.

## Copyright and disclaimer

This dataset contains social media text extracted from publicly accessible
sources on the internet. The selection, organization, curation, and
transformation of this dataset are original works that were previously
copyrighted. However, the copyright holder has waived all rights to this
dataset and dedicated it to the public domain under the
[Creative Commons Zero v1.0 Universal Public Domain Dedication][cc0].

Any trademarks or trade names appearing in the messages belong to their
respective owners.

[Wisesight (Thailand) Co., Ltd.](https://wisesight.com/) has assisted in the
collection and sentiment labeling of this dataset, but does not necessarily
endorse the labels assigned by human annotators.
These annotations are for research purposes only and do not represent the
professional work Wisesight performs for its clients.

Please note that human annotators may not personally agree or disagree with
the messages they label. Additionally, the labels assigned do not necessarily
reflect their personal opinions on the content.

*You are free to use this dataset for any purpose, without any restrictions.*

## Citation

Please cite the following if you make use of the dataset:

> Suriyawongkul, Arthit, Ekapol Chuangsuwanich, Pattarawat Chormai, Nitchakarn Chantarapratin, Ponrawee Prasertsom, Jitkapat Sawatphol, Nozomi Yamada, Attapol Rutherford, Charin Polpanumas, and Can Udomcharoenchaikit. “PyThaiNLP/Wisesight Sentiment Corpus with Word Tokenization Label”. Zenodo, 7 November 2024. <https://doi.org/10.5281/zenodo.3457446>.

BibTeX:

```bibtex
@misc{Suriyawongkul_PyThaiNLP_Wisesight_Sentiment_Corpus_2020,
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
  version      = {v1.1},
  year         = 2024
}
```

## Acknowledgement

We would like to thank:

- The [PyThaiNLP community](https://github.com/PyThaiNLP/) and
  [Kitsuchart Pasupa](https://www.it.kmitl.ac.th/~kitsuchart/) (Faculty of
  Information Technology, King Mongkut's Institute of Technology Ladkrabang)
  for their advice.
- The [Natural Language Processing Lab](https://attapol.github.io/lab.html) at
  Department of Linguistics, Faculty of Arts, Chulalongkorn University for
  their support with tokenization annotation.
- Ekapol Chuangsuwanich for his initiative in creating the original Kaggle
  competition using an earlier version of this corpus. The competition can be
  found at <https://www.kaggle.com/c/wisesight-sentiment/>.

## Additional resources

- For classification examples, see
  [Thai Text Classification Benchmarks](https://github.com/PyThaiNLP/classification-benchmarks).
- This corpus is also available at Hugging Face Datasets:
  - [wisesight_sentiment](https://huggingface.co/datasets/wisesight_sentiment)
    (using the earlier version of this corpus)
  - [wisesight1000](https://huggingface.co/datasets/wisesight1000)

[cc0]: https://creativecommons.org/publicdomain/zero/1.0/
