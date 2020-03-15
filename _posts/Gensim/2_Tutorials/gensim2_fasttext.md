---
title: gensim - tutorial - fastText
category: python-libs
tags: python python-libs gensim similairty word2vec nlp doc2vec fastText
---

## 2-line summary 

- word2vec의 경우, 존재하지 않는 word(vocab에 등록되지 않은 word)에 대해서는 vector로 표현해주지 못한다. 


## word2vec의 한계 

- word2vec의 경우, 존재하지 않는 word(vocab에 등록되지 않은 word)에 대해서는 vector로 표현해주지 못한다. 가령 word2vec의 vocabulary에 "research"는 있지만, "researches"는 없는 경우, 'researches'가 사람이 보기에는 매우 비슷한 단어임에도 불구하고, 이를 vector로 표현해주지 못한다. 
- 다시 말하면, word2vec은 명확하게 정의된 vocabulary에 대해서, 모든 vocabulary가 서로 다르다는 것을 가정하고 학습을 하는 것을 말합니다. 따라서, research와 research가 앞뒤 노드가 의미적으로 같지 않다면, 매우 유사도 낮게 나올수도 있다는 이야기죠. 
- 이런 종류의 문제를 "out of vocabulary"라고 함. 

?? 다만, 가령 'boy', 'boys'라는 두 word가 모두 vocabulary에 존재할 때, 같은 방식으로 데이터를 학습하였을 때, word2vec은 단어의 앞 뒤 구조로 파악하므로 단어 자체의 특성을 반영하지 못하는 것은 맞는데, 
fastText가 단어간의 유사도를 가지고, in vocabulary에 대해서도 처리해주는지는 다시 이해하는 게 필요할 것으로 보임. 즉, "없는 단어를 예측할 때"만 음운 구조를 사용하는지, 아니면 그냥 내부의 단어간의 구조(rare word)에 대해서도 효과적으로 처리해주는지 이해하는 것이 필요. 다만 맞는 것 같은데?? 

- 또한 그렇다면, 다음 중 무엇이 더 좋은 방식인가? 
    1) doc2vec으로 학습하여, 복합어를 vector로 표현하는 것이 좋은 방식인가? 
    2) 그냥 모든 키워드들에 대해서 fasttext로 학습하고, 복합어가 out-of-vocabulary에 대해서도 예측하도록 하는 것이 좋은가?

## What is FastText? 

## When to use FastText

- fastText의 기본 원리는 단어에 존재하는 "morphological structure"를 활용하여, 단어의 의미 정보를 추출해내는 것입니다. 이는, 전통적인 traditional word embedding 방식인 word vocabulary에 근거한 word embedding 방식에서는 존재하지 않았던 것이죠. 따라서, 기존의 word2vec의 경우에는 word vocabulary에 존재하지 않는 "새로운 단어"에 대해서는 vector로 표현할 수 없었습니다. 

![morphological structure](https://www.cs.bham.ac.uk/~pjh/sem1a5/pt2/pt2_intro_morph_1.gif)

- 하지만, fastText의 경우는 morphological structure에 근거하여 단어의 의미를 추출하기 때문에, 존재하지 않더라도, 의미를 추출할 수 있습니다. 따라서, 형태적으로 어느 정도 비슷한, german, turkish와 같은 단어들에 대해서도 의미를 어느 정도 유추할 수 있다는 강점이 있죠. 
- fastText는 모든 단어들에 대해서 "그 단어를 내부 subword의 조합"으로 생각합니다. 여기서, subword는 character에 대한 ngram이라고 생각할 수도 있겠죠. 그리고, word에 대한 vector는 단순하게, char-ngram 각각의 벡터의 합으로 나타내어지는 것이죠. 따라서, fastText의 경우 vocabulary에 없는 단어들에 대해서도 효과적으로 추론할 수 있습니다. 최소한, 하나의 character라도 vocabulary에 존재한다면 해결된다는 이야기죠.



## reference

- [gensim - tutorials - fasttext](https://radimrehurek.com/gensim/auto_examples/tutorials/run_fasttext.html#sphx-glr-auto-examples-tutorials-run-fasttext-py)
- [FastText, Word representation using subword](https://lovit.github.io/nlp/representation/2018/10/22/fasttext_subword/)