---
title: networkx - link prediction - Preferential attachment
category: python-libs
tags: python python-libs networkx distance preferential-attachment
---

## 3-line summary 

- [preferentail attachment](https://en.wikipedia.org/wiki/Preferential_attachment)는 이른바 "빈익빈 부익부"를 말하며, "강한 놈은 더 강해진다"라는 의미죠. 
- 네트워크에서도 동일하며, 새로 발생할 가능성이 높은 link는 아마도, "힘이 쎈 노드들일 수록 붙을 확률이 높다"라는 개념을 담고 있습니다. 
- 그리고 이 값은 그냥, "두 노드의 degee를 곱"하여 계산됩니다.

## Compute Preferential-attachment link prediction prob.

- degree를 곱하면 끝이므로, 매우 간단합니다. 다만, normalization은 되어 있지 않죠.

```python 
import networkx as nx
import numpy as np

#G = np.random.seed(0)

N = 10
G = nx.scale_free_graph(N, seed=0)
G = nx.Graph(G)

def customer_preferential_attachment(G, u, v):
    # degree의 곱
    return nx.degree(G, u)*nx.degree(G, v)

for u, v, nx_PA in nx.preferential_attachment(G):
    assert nx_PA == customer_preferential_attachment(G, u, v)

print("Assertion complete")
print("=="*20)

```


## wrap-up

- 물론, 무리하게, min-max scaling을 수행할 수도 있습니다. scaling을 해봤자, 이 그래프에서의 0.5와 다른 그래프에서의 0.5는 서로 다른 population에서 normalization했기 때문에 다른 의미를 가집니다. 즉, scaling하지 마세요. 그대로 두어야, 다른 그래프와도 비교가 가능해집니다.

## reference

- [Preferential Attachment](https://en.wikipedia.org/wiki/Preferential_attachment)