---
title: gensim - tutorial - doc2vec with trained word2vec
category: python-libs
tags: python python-libs gensim similairty word2vec nlp doc2vec 
---

## 2-line summary 

## intro 

- 지금까지 저는 word2vec도 공부했고, doc2vec도 공부했습니다. 그리고, doc2vec은 word2vec과 연결되어 있죠. 
- 우선 간단하게 지금까지 공부한 것들을 복습해보겠습니다.

### AGAIN: word2vec 

- word2vec은 각 문장내에 존재하는 word들을 vector로 변환해주는 것을 말합니다. 하나의 document혹은 sentence 내에 존재하는 각각의 word를 모두 vector로 표현하고, skip-gram, CBOW 등으로 처리하죠. 
- 다만, 이 아이는 우선, Out-of-Vocabulary에 대해서 처리해주지 못합니다. 따라서, 여러 단어들로 구성된 복합어들이 이미 vocabulary에 존재하지 않는다면, 해당 단어를 vector로 표현할 수 없죠. 
- 뿐만 아니라, 형태적으로 유사한 것들에 대해서 정확하게 파악해주지 못한다는 한계를 가지고 있습니다. 가령 'universities'와 'university'라는 단어가 있다고 할때, 우리는 두 단어가 "형태적으로 유사하다는 것"을 딱 보면 알기 때문에, "매우 높은 확률로 비슷할 것이다"라고 추측할 수 있지만, 이 아이는 그걸 하지 못해요. 초기 가정에서 "형태가 다른 word는 모두 다르다"라는 가정을 가지고 진행하기 때문이죠.

### AGAIN: fasttext 

- fasttext는 기존 word2vec이 가진 한계인 "형태적으로 유사한 것들"을 이해할 수 있습니다. 즉, out-of-vocabulary에 대해서도, 기존의 비슷한 단어들이 있었다면 vector를 유사하게 유추해내죠. 이는 character의 n-gram에 대해서 학습을 진행하기 때문입니다. 
- 따라서, 비교적 적은 학습에 대해서, 특히 단수/복수 형태와 같은 아이들에 대해서 꽤 잘학습을 해주죠.
- 하지만, 이 아이도 "복합어"를 처리할 때는 한계를 가집니다. 이유는 모르겠으나, 복합어를 넘겼을 때는, 좀 문제가 있는 결과들이 꽤 나오더군요. 


### AGAIN: doc2vec. 

- Doc2vec는 각 Document를 vector로 표현하는 모델입니다. word2vec과 유사하나, 여기에 output에 대해서 각 document에 대한 ID를 넣음으로써, 같은 ID를 가진 word들은 비슷한 차원에 위치하게 되죠. 
- 따라서, document를 넣었을때, 해당 document를 가장 잘 표현하는 vector를 찾아줍니다. 그리고 그 과정에서 word2vec의 경우도 자연스럽게 학습이 되죠.


## Doc2Vec with pre-trained word2vec.

- 제가 오늘 하려는 것은 "이미 학습된 word2vec"모델을 가져와서 doc2vec의 word2vec 모델을 초기화시키고, 그 다음 doc2vec 모델을 학습시켜줌으로써, 빠르게 document를 학습해주려고 합니다.