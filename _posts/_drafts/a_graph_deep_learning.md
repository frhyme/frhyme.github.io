---
title:
category:
tags: 
---

## intro 

- 일반적으로 CNN, RNN을 돌릴 때, euclidean data를 이용합니다. 
- 하지만, neural network에 graph data를 넘기려면 어떻게 해야 할까요? 

## representational learning

- representational learning이라는 것은 쉽게 말해 '무엇인가'를 vector로 표현하는 것을 말합니다. 
    - word를 vector로 표현하는 word2vec
    - document를 vector로 표현하는 doc2vec
    - 그리고 인풋 데이터가 graph라면 graph의 node를 vector로 표현하는 node2vec 등이여기에 포함되죠. 
    - 물론 graph2vec도 가능합니다. 

- neural network을 사용해서 graph의 node들을 특정 point로 embedding합니다. 
    - 여기서 embedding이라 함은 각 노드의 기하학적 위치를 찾아주는 작업을 말하죠. 간단히는 node를 벡터로 변환해준다고 해도 됩니다. 
    - 이렇게 node를 기하학적 공간에 위치시킴으로써 가까운 놈들은 아마도 실제로 가까운 놈들, 아닌 놈들은 실제로 먼 놈들, 이렇게 해석해서 진행할 수 있습니다. 
    - 즉, 

- CNN을 활용해서, 진행하면, 특정 위치에 embedding할 수 있고, 
- timely data를 활용하여 RNN에 넘기면(물론 학습이 되어 있다는 전제 하에), 해당 그래프가 점점 어떻게 변화하는지를 파악할 수 있을 것 같습니다. 
- 마찬가지로, classification, clustering 등도 잘할 수 있겠죠. 
- 다르게 생각하면, text도 하나의 graph로 고려하고, 개별 word를 node로 고려한 것과 비슷합니다. 가까운 node는 서로 비슷한 의미를 가진다는 개념으로 접근한 것이, word-embedding이죠. 그 방법 그대로, text를 분류하기도 하고, 클러스터링하기도 하고, RNN에 넣어서 번역하기도 합니다. 

- 마찬가지로, graph도 텍스트처럼, 분류되고, 클러스터링되고, 할 수 있다면 훨씬 재미있지 않을까요? 

- 또한, 시간이 지남에 따라서 새롭게 어떤 link가 생겨날 것인지, link prediction을 할 수도 있겠죠. 


## reference 

- <https://towardsdatascience.com/how-to-do-deep-learning-on-graphs-with-graph-convolutional-networks-7d2250723780>
- <http://tkipf.github.io/misc/SlidesCambridge.pdf>
- <http://tkipf.github.io/graph-convolutional-networks/>
- <http://geometricdeeplearning.com/>
- <https://skymind.ai/wiki/graph-analysis>
- <https://www.slideshare.net/PetteriTeikariPhD/geometric-deep-learning>