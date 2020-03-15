---
title: gensim - tutorial - doc2vec with trained word2vec
category: python-libs
tags: python python-libs gensim similairty word2vec nlp doc2vec 
---

## 2-line summary 

## intro 

- 지금까지 저는 word2vec도 공부했고, doc2vec도 공부했습니다. 그리고, doc2vec은 word2vec과 연결되어 있죠. 

### word2vec 

- word2vec은 각 문장내에 존재하는 word들을 vector로 변환해주는 것을 말합니다. 
- 복합어, 가령 "Research and development"는 어떻게 처리해주는 것이 좋은가? 
    - by word2vec: "research and develop"를 하나의 word로 생각하고, 각 단어가 sentence 내에 포함되어 있을 경우 해당 단어를 잘 tokenize하여 준다. 하지만, 이럴 경우, 이 단어는 research, and, development라는 3가지 단어의 벡터와 전혀 영향을 주고 받지 않게 된다는 한계가 있다.
    - by doc2vec: doc2vec은 word2vec을 학습하며 동시에 해당 단어들이 하나의 document 라는 것도 함께 넘겨주게 된다. 즉, 우리는 "reserach and develop"라는 단어를 하나의 document로 인식하고 처리한다는 것을 말한다. 따라서, abstract 내 문장을 구분하여, 처리하고, 이를 통해 
    - by fastext: fasttext는 word2vec에 비해서 "존재하지 않는 키워드들"에 대해서도 처리해준다는 강점이 있음. 이는 결국 subword를 가지고 처리해준다는 말. 다만, 이 아이가 복합어들에 대해서도 잘 처리를 해주는 건가? 