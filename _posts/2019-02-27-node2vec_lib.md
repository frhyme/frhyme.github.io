---
title: node2vec 라이브러리를 사용해봅시다. 
category: machine-learning
tags: machine-learning node2vec python
---

## recap: node2vec

- node2vec은 word2vec처럼 skip-gram을 사용해서 node를 vector로 표현하는 방법론입니다. 그 과정에서 word2vec의 sequence와 같은 것을 네트워크의 sampling strategy를 사용해서 처리하죠.
- 그러나, graph는 homophily(local structure)와 structural equivalence(global structure) 관점 중에서 무엇을 중요하게 생각하는지에 따라서 다르게 vector로 표현될 수 있습니다. 즉, 이 값은 p, q라는 hyper-parameter에 따라서 조절되게 되구요. 
- 이걸 직접 구현을 하려면 사실 좀 어려워지는데, 다행히 이미 구현을 해서 사용하고 있는 사람이 있습니다. [여기에 github repo](https://github.com/eliorc/node2vec)가 있습니다. 

## use node2vec lib

- 일단 설치부터 합시다. 아래를 실행하면 node2vec이 사용하는 `gensim`라이브러리도 함께 설치하게 됩니다. 

```
pip install node2vec
```

- `gensim`을 사용해본 적이 있으신 분의 경우 익숙하실 것입니다. `node2vec`의 경우 resampling을 만든 다음 `gensim`을 사용해서 학습을 시켜서 진행하는 것으로 대략 보이네요. 

## how to use it

### node2vec and clustering 

- `networkx`에 있는 네트워크를 가져와서 `node2vec`을 이용해서 각 node를 vector로 변환하고, 각 node의 벡터 표현을 활용해서 클러스터링을 수행해보려고 합니다. 
    - `p`, `q` 값을 조절하면서 그 변화를 측정해보려고 했는데, 생각보다 잘 작동하지는 않는 것 같습니다. 아마도 제 그래프가 작아서 그럴 것으로 보이기는 해요. 
- 아무튼 다음처럼 실행해서 진행해봤습니다. 결론만 말씀을 드리면, node2vec의 결과로 나온 값을 가지고 클러스터링을 돌려보면 그래프 상에서는 꽤 정확하게 나오게 되는 것 같습니다. 
    - 물론 homophily를 강조하는 측면으로 혹은 structural equivalence를 강조하는 측면을 구분해서 보여주는 것은 아직 잘 모르겠고요. 

```python
import networkx as nx
!pip install node2vec
from node2vec import Node2Vec

import matplotlib.pyplot as plt 
plt.style.use('default')

## node2vec을 이용해서 다른 방법론들과 함께 사용해보기 위함. 
from sklearn.manifold import TSNE
from sklearn.cluster import KMeans

#################################################
G = nx.karate_club_graph()

# 여기서 이 그래프의 경우 node의 이름이 int로 되어 있어서, 이걸 스트링으로 변환해줍니다. 변환하지 않을 경우 가끔 int, str 변환측면에서 에러가 발생할 수 있어요. 
G = nx.relabel_nodes(G, { n:str(n) for n in G.nodes()})

"""
- node2vec의 hyper-parameter를 조절하여 세팅하고
- fitting을 시킵니다. 
"""
# https://github.com/eliorc/node2vec

node2vec = Node2Vec(graph=G, # target graph
                    dimensions=50, # embedding dimension
                    walk_length=10, # number of nodes in each walks 
                    p = 1, # return hyper parameter
                    q = 0.0001, # inout parameter, q값을 작게 하면 structural equivalence를 강조하는 형태로 학습됩니다. 
                    weight_key=None, # if weight_key in attrdict 
                    num_walks=2000, 
                    workers=1,
                   )
# 대략 walk들이 어떻게 발생하는지를 아래처럼 볼 수도 있습니다. 
for i, each_walk in enumerate(node2vec.walks):
    print(f"{i:0>2d}, {each_walk}")
    if i>1:
        break
# 발생한 walk를 사용해서 학습을 시켜봅니다. 
# 여기서 fitting할때 사용하는 argument는 gensim의 word2vec과 같습니다. 
# 단 학습시킨 것을 model1처럼 어디에 집어넣어줘야 하는 것 같네요. 여기서 p나 q값을 조절하기는 어려운 것 같습니다. 
model1 = node2vec.fit(window=2)
# kmeans clustering을 진행해줍니다. 
K = 5
kmeans = KMeans(n_clusters=K, random_state=0).fit(model1.wv.vectors)
# node의 cluster 부분을 attrdict에 업데이트해줍니다. 
for n, label in zip(model1.wv.index2entity, kmeans.labels_):
    G.nodes[n]['label'] = label

# 그림을 그려줍니다.
plt.figure(figsize=(12, 6))
nx.draw_networkx(G, pos=nx.layout.spring_layout(G), 
                 node_color=[n[1]['label'] for n in G.nodes(data=True)], 
                 cmap=plt.cm.rainbow
                )
plt.axis('off')
plt.show()
```

### edge embedding

- node뿐만 아니라 edge 또한 embedding해서 사용할 수도 있습니다. 여기서는 기존 논문에 나온 것처럼 `HadamardEmbedder`를 사용해서 많이 씁니다. 
- link prediction 문제를 푼다고 할때 edge 벡터를 활용해서 해당 edge를 classification 한다거나, 하는 방식으로 사용할 수 있을 것 같습니다. 

```python
from node2vec.edges import HadamardEmbedder

edges_embs = HadamardEmbedder(keyed_vectors=model1.wv)

# 특정한 edge의 벡터 표현을 보고 싶을 때 
edges_embs[('24', '25')]
# 모든 edge의 벡터표현을 가져오고 싶을때 
# 이 경우 gensim에서 쓰는 것처럼 most_similar등의 메소드를 사용할 수 있습니다. 
edges_kv = edges_embs.as_keyed_vectors()
edges_kv.most_similar(str(('24', '25')))
```


## wrap-up 

- node2vec이 word2vec에 비해서 개념적으로 좀 더 큰 것 같습니다. 오히려 word2vec을 바로 쓰기보다는 텍스트에서 앞뒤간격 혹은 weight를 활용해서 네트워크를 구축하고 해당 네트워크를 node2vec으로 학습한다음 사용하는 것이 더 좋을 수 있지 않을까? 하는 생각도 들구요. 
- 일단 저한테는 그렇게 네트워크로 구축하고 진행하는 것이 더 인지하기 쉬운 것 같네요. 

## reference

- <https://github.com/eliorc/node2vec>