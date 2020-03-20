---
title: python - networkx - MultiGraph
category: python-libs
tags: python python-libs networkx multigraph 
---

## networkx.multigraph 사용하기.

- `networkx`의 경우 network(Graph)를 방향성(directionality), 다중-Edge-가능여부에 따라 총 4가지로 구분하죠. 

### nx.Graph()

- `nx.Graph()`: 방향성이 없고, node간에 하나의 edge만 허용합니다. 따라서, `(u, v)`를 입력하든, `(v, u)`를 입력하든 같은 edge를 의미하죠.
- 또한, 이미 `(u, v)`가 있는 상황에서, 새로운 `(u, v)` 혹은 `(v, u)`를 추가한다면, 기본적으로는 아무 변화가 없습니다. 다만, 만약 기존 edge에 `attribute_dict`가 있다면, 이 값이 update되는 식으로 처리되죠.
- 아래 코드를 보시면, `G`에 새로운 edge `(0, 1)`을 `{'weight':3, 'aaa'=10}`라는 정보와 함께 생성해주었습니다. 
- 그리고, 그 이후, 다시 같은 edge인 `(1, 0)`을 `weight=2`와 함께 넘겨줬죠. 만약, 이 때, edge가 제거 되고, 새롭게 생성되는 형태로 진행된다면, `'aaa'=10`이 남아있지 않아야 하는데, 여전히 남아 있는 것을 알 수 있습니다. 그냥, `weight`의 값만 바뀌었죠.

```python
G = nx.Graph() 

G.add_edge(0, 1, weight=3, aaa=10)
print(G.edges(data=True))
print("--"*20)
# 이미 동일한 edge인 (0, 1)이 있는 상황에서, 
# 새로운 edge를 업데이트하게 되면, 원래 edge의 attribute_dict가 업데이트되는 식으로 진행됨.
G.add_edge(1, 0, weight=2)
print(G.edges(data=True))
```
```
[(0, 1, {'weight': 3, 'aaa': 10})]
----------------------------------------
[(0, 1, {'weight': 2, 'aaa': 10})]
```

- `G`의 edge를 지우기 위해서는 아래 코드를 사용합니다. 방향성이 없으므로 `(u, v)`를 지우든 `(v, u)`를 지우든 별 차이가 없습니다.

```python
G.remove_edge(0, 1) # G.remove_edge(1, 0)
```

### nx.DiGraph()

- 이 아이는 방향성이 있다는 것이 다릅니다. 즉, `(u, v)`와 `(v, u)`를 다르게 인식한다는 것이죠. 따라서, edge를 넣거나 뺄 때, 방향성을 유념해서 넣어주어야 합니다. 
- 방향성이 있다고 가정하기 때문에, 모든 노드 pair에는 최대 2개의 edge가 존재할 수 있습니다. `(u, v)`이거나, `(v, u)`이거나 둘 중 하나죠. 그리고, 이는 각각 `G[u][v]` 혹은 `G[v][u]`와 같은 식으로 쉽게 접근 및 관리할 수 있습니다.
- 그것을 제외하고는 앞서 말한 `nx.Graph()`와 유사하므로 추가 설명을 하지는 않겠습니다. 

## Main TOPIC : nx.MultiGraph()

- 네, 사실은 오늘은 이 내용을 설명하기 위해서 앞 부분을 간단하게 설명한 것이죠. 
- 앞서 말한 바와 같이, `nx.MultiGraph()`는 여러 edge가 동시에 존재할 수 있도록 해줍니다. 매우 간단한 예를 들면, 서울에서 부산으로 갈때 존재하는 많은 도로들을 각각 edge로 표현해서 모델링하고 싶다면, 각 도로를 edge로 만들어주는 것이죠. 이 각각의 도로는 특성이 다르기 때문에, 하나의 edge로 표현하는 것이 아니라, 중복되는 여러 edge로 표현해줘야 합니다.
- 그렇다면 여기에서는 어떻게 edge들을 넣고 빼줄 수 있을까요? 

### MultiGraph.add_edge

- 사실 만들고 뻬는 것은 별로 어렵지 않습니다. 
- 아래 코드를 보시면 그냥 `(0, 1)`을 2번 넣어줬죠. 앞서 말한 것처럼 `nx.MultiGraph()`는 동시에 여러 edge를 동시에 표현할 수 있기 때문에, 이미 있는 상태에서 새로운 edge를 넣어주면 독립적인 edge를 넣는다고 생각하고, 새로운 edge를 넣어줍니다. 
- 그리고, 방향성이 없으므로 `(0, 1)`, `(1, 0)`을 넣어주나, `(0, 1)`, `(0, 1)`을 넣어주나 차이가 없습니다.

```python
import networkx as nx 

MG = nx.MultiGraph()
MG.add_edges_from([
    (0, 1, {'type':'car'}), (1, 0, {'type':'bus'})
])

print("== MG.edges() =====")
for e in MG.edges(data=True):
    print(e)
print("=="*20)
```

```
== MG.edges() =====
(0, 1, {'type': 'car'})
(0, 1, {'type': 'bus'})
```

### MultiGraph.remove_edge

- 이제 edge를 제거해보겠습니다. 앞서 만든 edge들 중에서 저는 'bus'라는 edge를 없애려고 합니다.
- 여기서 다음 코드를 보시면, MG의 edge를 읽기 위해서 `MG.edges(data=True, keys=True)`를 사용하였습니다. `data=True`는 익숙하죠? `keys`는 복수의 edge들을 관리할 때, edge을 구별해주는 key라고 보시면 됩니다. 
- 즉, `(u, v, k)`이 세 조합을 합치면, 무조건 어떤 edge에 대해서도 uniqueness 가 보장되는 것이죠. 

```python
for u, v, k, e_attr in MG.edges(data=True, keys=True):
    print(f"u: {u}, v: {v}, k: {k}, e_attr: {e_attr}")
```
```
== MG.edges(data=True) =====
u: 0, v: 1, k: 0, e_attr: {'type': 'car'}
u: 0, v: 1, k: 1, e_attr: {'type': 'bus'}
```

- edge를 추가할 때는 `k`에 대해서 알아서 하나씩 값을 올라가며 넣어줍니다. 
- 하지만, 제거할 때는 `u, v, k`를 모두 넣어줘야 합니다. 다음처럼 지워주면 정상적으로 edge가 잘 지워진 것을 알 수 있습니다.

```python
MG.remove_edges_from([
    (0, 1, 1)
])
print("== MG.edges(data=True) =====")
for u, v, k, e_attr in MG.edges(data=True, keys=True):
    print(f"u: {u}, v: {v}, k: {k}, e_attr: {e_attr}")
```
```
== MG.edges(data=True) =====
u: 0, v: 1, k: 0, e_attr: {'type': 'car'}
```

## wrap-up

- 다시 정리하자면, `nx.MultiGraph()`의 경우 복수의 edge를 동시에 관리해야 하므로, edge들에 대해서도 key값을 줘야 한다.
- 넣을때는 보통 0부터 시작해서 가장 큰 key값에서 하나씩 추가하는 식으로 값을 늘려나가기 때문에, 정의해줄 필요가 없지만, 
- 뺄 때는 정확한 key값을 정의해서 넘겨주는 것이 필요하다. 만약 그렇게 하지 않을 경우, 랜덤 edge가 지워지게 될 수도 있음.