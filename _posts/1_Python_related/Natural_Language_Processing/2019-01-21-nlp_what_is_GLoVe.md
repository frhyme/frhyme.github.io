---
title: What is GLoVe?? 
category: others
tags: nlp word2vec word-embedding machine-learning
---

## intro

- 저는 단어의 semantic similarity를 계산하기 위하여 Spacy를 사용하고 있습니다. 
    - spacy는 기학습된 단어의 word-vector를 가지고 계산을 하는데, 이 과정에서 쓰는 word vector는 [GLoVe](https://nlp.stanford.edu/pubs/glove.pdf)입니다. 
- 그래서 쓰고는 있고, 쓸 때 꽤 결과가 잘 나오니까 잘 나오나보다, 라고 생각은 하고 있지만, 누군가 나에게 "그게 Word2Vec과 뭐가 다르지?", "그건 어떻게 학습된건데?"라고 묻는다면, 와카리마셍 허허허. 
- 아무튼, 그래서 직접 알아보기로 했습니다. 

## What is GLoVe?? 

> 
GloVe is an unsupervised learning algorithm for obtaining vector representations for words. Training is performed on aggregated global word-word co-occurrence statistics from a corpus, and the resulting representations showcase interesting linear substructures of the word vector space.

- 글로브는 키워드에 대한 vector representation을 획득하기 위해서 만들어진 unsupervised learning algorithm입니다. 학습은 corpus(말뭉치)의 word-word co-occurrence statistics로부터 수행됩니다. 
- 제 기억이 맞다면, word2vec의 경우는 skip-gram 등으로 해당 단어의 앞뒤로 어떤 단어들이 있는지를 통해서 학습을 시켰던 것 같습니다. 
- 그 측면으로 보면, 글로브는 Word2Vec이 간과하는 co-occurrence정보를 충분히 담을 수 있도록 학습했다는 말이 되는군요. 흠, 정말 그런가요. 
- 사실 말이 길었지만, 기본적인 접근 자체는 count와 다르지 않습니다. 단어는 corpus에 많이 등장하는 키워드의 수와 유사하다는 개념이고, 이를 벡터로 표현하고 그 유사성을 비교하여 단어간의 유사성을 확인할 수 있다는 말이죠. 

## 그럼 언제 Word2vec을 써야 하고, 언제 GloVe을 써야하나요? 

- 음, 사실 잘 모르겠습니다. 예를 들어서, 단어간의 유사성을 평가함에 있어서는 GloVe가 좋다, 뭐 그런 말이라도 있으면 좋겠는데, 저는 아직 찾을 수가 없군요. 

## 결론

- 그냥 spacy에 포함되어 있는 GloVe를 쓰겟습니다 하하핫.