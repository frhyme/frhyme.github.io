---
title: `G.has_edge(u, v)`는 `v in G[u]`보다 빠른가? 
category: python-libs
tags: python python-libs networkx 
---

## 2-line summary. 

- graph `G`의 node간 연결성을 체크하는 방법중에서 `G.has_edge(u, v)`가 `v in G[u]`보다 2배 이상 빠름. 
- 물론, `b in G._adj[a]` 를 사용하면, 더 빨라지지만, 위험성이 있으므로 가급적 하지 않는 것을 추천.

## `G.has_edge(u, v)`는 `v in G[u]`보다 빠른가? 

- 저는 보통 node들의 연결성(edge의 존재유무)을 체크할 때, `v in G[u]`를 사용합니다. 즉, "`u`의 이웃에 `v`가 포함되어있는가"를 체크하는 것이죠. 

```
v in G[u]
```

- 그런데, 종종 코드를 보면 다음으로 처리하는 경우들이 있더라구요. 

```python
G.has_edge(u, v)
```

- 별 차이가 없을 것 같기는 한데, 그냥 궁금해서 한번 시간을 비교해봤습니다. 

### performance check. 

- 적당한 크기의 `scale_free_graph`를 만들고, 여러번 edge를 체크하면서 걸린 시간을 총 합하여 처리하였습니다.

```python
import networkx as nx
import numpy as np
import time

"""
nx.has_edge 는 충분히 빠른가? 
"""

np.random.seed(0)

# Graph Generation
n = 3000
G = nx.scale_free_graph(n=n)
G = nx.Graph(G)

method1_total_time = 0
method2_total_time = 0

print("--" * 20)
print("== start")
for i in range(0, 1000):
    a, b = np.random.choice(G, 2)
    # method 1: a, b에 edge가 있는지 체크하고 시간을 체크.
    start_time = time.time()
    a_b_has_edge= G.has_edge(a, b)
    method1_total_time += (time.time() - start_time)
    # method 2: a의 이웃에 b가 포함되는지 체크.
    start_time = time.time()
    a_b_neighbor = b in G[a]
    method2_total_time  += (time.time() - start_time)
    # assertion에 오류가 나면
    assert a_b_neighbor == a_b_has_edge

print(f"method1(has_edge) time: {method1_total_time:.5f}")
print(f"method2(neighbor) time: {method2_total_time:.5f}")
print("--"*20)
```

- 결과를 보시면, `G.has_edg`가 약 60%정도의 시간을 절약하는 것을 알 수 있습니다.

```
----------------------------------------
== start
method1(has_edge) time: 0.00222
method2(neighbor) time: 0.00553
----------------------------------------
```

## 왜, `G.has_edge(u, v)`가 더 빠른가? 

### `G.has_edge`의 경우 

- `G.has_edge`의 코드는 다음과 같습니다. `self._adj` 딕셔너리로부터 값을 참고하여, 바로 가져오죠.

```
try:
    return v in self._adj[u]
except KeyError:
    return False
```

- `self._adj`는 대략 다음의 형태를 가집니다. 즉, `G`에 `(u, v)`라는 edge가 추가되면, 위에 `u`라는 key를 추가하고 다시 `v`를 키로 하는 dictionary를 추가되는 식이죠. 이게 기본적으로 `nx.Graph()`에서 adjacency를 관리하는 방법이죠. 
- 즉, `G.has_edge`는 adjacency를 관리하는 기본적인 자료구조에 바로 접근하기 때문에 훨씬 빠릅니다.

```python
{0: {1: {}, 2: {}}, 1: {0: {}, 2: {}}, 2: {1: {}, 0: {}}}
```

### `v in G[u]`의 경우 

- 이 아이는 G의 내부 메소드인 `__getitem__`을 확인해봐야 합니다. 다음과 같이 되어 있군요.

```
return self.adj[n]
```

- `self.adj`를 확인해보면 다음과 같습니다

```
return AdjacencyView(self._adj)
```

- `AdjacencyView`는 `networkx.coreview`를 확인해야 하는데, 매우 귀찮으므로 넘어갑니다. 
- 아무튼 그냥 바로 확인하는 것이 아니고, 여러번 체크해서 넘어가야 하므로 매우 귀찮아진다, 라고만 이해하기로 합니다.

## use `b in G._adj[a]`

- 따라서, 굳이 method를 쓸 필요 없이, `b in G._adj[a]`로 자료구조에 바로 접근하면 훨씬 빠릅니다. 
- 앞서 사용한 `G.has_edge(u, v)`보다 2배 이상 빠릅니다. 


## wrap-up

- 코드에 대해서 궁금증을 가지고, 간단한 performance check를 한 다음, 왜 더 빠른지 혹은 왜 더 느린지를 체크하는 것은 매우 흥미로운 일이죠. 
- python에서는 기본적인 자료구조를 dictionary로 세팅하는 것이 좋고, 내부의 자료구조를 건드리지 않고, 외부 interface를 통해서 제어하도록 하는 기본적인 객체 지향 프로그래밍 패러다임을 가집니다. 
- 하지만, private, public의 개념이 모호하므로, 사실 `b in G._adj[a]` 를 사용해도 에러가 발생하지 않죠. 물론, 그렇다고 `_`가 붙어 있는 아이들을 함부로 건드리면 나중에 문제가 발생할 수 있습니다.