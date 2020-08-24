---
title: python - networkx - AtlasView object
category: python-libs
tags: python python-libs networkx 
---


## Error: 'AtlasView' object does not support item assignment

- `networkx`로 코딩을 하다보면 종종 뜨는 에러 중에서 다음의 에러가 있습니다. 

```
TypeError: 'AtlasView' object does not support item assignment
```

- 에러 코드를 그대로 해석하자면 "AtlasView 오브젝트는 item assignment를 어용하지 않는다"라는 말이죠. 

## What is AtlasView object? 

- [AtlasView](https://kite.com/python/docs/networkx.coreviews.AtlasView)는 "dictionary of dictionary로 되어 있는 Read-only 구조"를 말합니다. networkx에서 node, edge를 접근할 때, dictionary처럼 `[]`로 접근하는 것을 AtlasView라고 말하죠.
- 즉, 위에서 말한 error code가 떴다는 것은 Read-only에 대해서 item assignment를 했다는 말이죠. 
- 위 에러는 가령 다음과 같이 `nx.Graph`에 대해서 `[]`로 바로 접근하는 경우 에러가 발생합니다. 

```python
G[0]['weight']=10
```

- 따라서, 위처럼 처리하지 않고, 아래처럼 변경해주면 해결됩니다. 

```python
G.nodes[0]['weight']=10
```


## raw code

```python
import networkx as nx

"""
What is Atlas view object
when, why happen?

TypeError: 'AtlasView' object does not support item assignment
"""
N = 6
p = 0.5
G = nx.fast_gnp_random_graph(N, p)


print(G.edges(data=True))
# 아래와 같이 Graph에 대해서 dictionary처럼 접근하여 값을 할당하는 경우, 에러가 발생합니다.
try:
    G[0]['weight']=10
    #G.nodes[0]['weight'] = 10 #이렇게 
    print(G.nodes(data=True))
except Exception as e:
    print("SOMETHING WRONG")
    print("== error message")
    print(e)
    print("=="*20)
```