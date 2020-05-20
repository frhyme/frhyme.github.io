---
title: PaperSummary - Enriching Word Vectors with Subword Information
category: paper-summary
tags: paper-summary nlp fastext
---

## Enriching Word Vectors with Subword Information

## Abstract 초월 번역

- 연속된 단어를 표현하는 방식(Continuous word representation)에 있어서, unlabeled corpora에 대해서 학습하는 것이 충분히 의미있다는 것을 word2vec과 같은 많은 NLP의 연구들이 증명했다.
- 다만, 대부분의 연구들은 단어의 morphology를 무시하였으며, vocabulary에 존재하는 word들에 대해서 각각 구별되는(distinct) vector를 적용하였다는 한계를 가진다. 특히, 이는 아주 큰 vocabulary와 희소한 단어들에게 한계가 될 수 있다.
- 이 연구에서는 각 단어들을 "bag of character n-gram"으로 표현하였다.
- 이 vector 표현 방식은 각 character의 n-gram으로 표현되며, 즉, 이 표현 방식으로 다시 word를 표현하게 된다. 이를 통해 만약 특정 keyword가 vocabulary에 존재하지 않더라도, character n-gram으로 표현하여, 새로운 단어에 대한 vector를 빠르게 에측할 수 있다.
- 이 방식을 서로 다른 언어들에 대해서 수행하였으며, 이 방식을 통해 향상되었다.

## reference

- [Enriching Word Vectors with Subword Information](https://arxiv.org/abs/1607.04606)
