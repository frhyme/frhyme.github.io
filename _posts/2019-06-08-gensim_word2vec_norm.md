---
title: genmsim의 word2vec normalize하기
category: python-libs
tags: python-libs python gensim word2vec normalization
---

## word2vec.wv.similarity

- word2vec은 각 단어를 벡터화하여 표현한 것을 말합니다. 뭐 쉬운것이니까 넘어가고, 여기서 종종 발생하는 문제점은 normalization이죠. 
- 단어간의 유사성을 고려해서, 가장 유사한 놈을 찾거나 할때, similarity 혹은 distance를 사용해서 처리하게 됩니다. 그런데, word2vec을 가지고 유사성을 비교할 때 그 결과가 -0.1과 1의 사이로 나와야 하는데, 1보다 큰 , 그것도 엄청 큰 값이 나올 때가 있어요. 
- 즉 다음 코드를 사용할 때요.

```python
model.wv.similarity('actor', 'actress')
```

- [해당 method에서는 cosin similarity를 사용하는 방법을 사용한다고 합니다](https://radimrehurek.com/gensim/models/keyedvectors.html#gensim.models.keyedvectors.WordEmbeddingsKeyedVectors.similarity). 즉, 그렇다면 값이 이렇게 나오면 안되는데, 거의 10^36승까지 나오는 것으로 봐서는, 뭔가 문제가 있는게 아닐까 싶습니다. 


## how to correct it

- 저는 해당 메소드에 문제가 있다고 판단하고, 그냥 `scipy.distance`를 사용해서 계산했씁니다. 
- 여기서 오히려 중요하게 알아야 하는 것은 'similarity'와 'distance'의 차이죠.

```python
from scipy.spatial import distance
dis = distance.cosine(model1.wv[w1], model1.wv[w2])
```

- distance는 비교적 간단한 개념입니다. 두 벡터간에 거리가 얼마나 떨어져 있느냐, 라는 것이 다죠. 
- similarity는 일면 비슷해 보이지만 계산법이 다른 것 같습니다. 아마도. 뭐 개념적으로 달라서 그런것 같은데, 귀찮으니까 더 하지는 않을래요 하하하하.

## wrap-up

- 저는 distance가 similarity보다 분명한 개념이라고 생각합니다. 
- 앞으로는 distance를 사용해서 계산해보려고 합니다.

## reference

- <https://stackoverflow.com/questions/53971240/normalize-vectors-in-gensim-model>