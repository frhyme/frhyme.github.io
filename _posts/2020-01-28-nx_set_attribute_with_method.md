---
title: python - networkx - nx.set_node_attribute
category: python-libs
tags: python python-libs networkx set_attribute
---

## node, edge의 attribute를 업데이트하자. 

- 대상을 graph로 표현한 다음 필요에 따라서 각 graph의 node, edge의 attribute를 업데이트합니다. 필요에 따라서, weight, centrality 등 다양한 값들을 업데이트하죠. 
- 이 때 흔히 쓰는 방식은 다음과 같습니다. 이렇게 직접 만들어서 쓸 수도 있지만, networkx에 있는 `nx.set_node_attributes`를 사용해서 처리할 수도 있죠.

```python
for n in G.nodes():
        G.nodes[n]['weight']=node_weight_dict[n]
for (u, v), value in edge_weight_dict.items():
    G[u][v]['weight'] = value
```

```python
nx.set_node_attributes(G, node_weight_dict, 'node_weight')
nx.set_edge_attributes(G, edge_weight_dict, 'edge_weight')
```

## Performance Comparison

- 궁금해서 비교해 봤습니다. Node의 수가 500개인 그래프에 대해서(edge는 complete graph 대비 60% 존재) 모든 node, edge에 대해 weight를 업데이트하는 실험을 30번 시행하여 비교하였습니다. 결과를 보면, 거의 차이가 없다고 할 수 있죠. 
- 즉, 이미 nx에서 제공하는 python code가 이미 충분히 pythonic하며, 병렬처리를 넣지 않는 이상, 굉장히 시간 단축이 되어 있는 것이라고 할 수 있습니다.

```
CASE1:     0.149
CASE2:     0.150
```

- 코드는 다음과 같구요.

```python
import networkx as nx
import numpy as np
import time
import timeit

"""
G.subgraph 는 subgraph_view이며, node를 추가하려면 복사해서 넣어야 한다. 

CASE 1: 각 노드, 엣지별로 weight를 일일이 넣어주는 경우 
CASE 2: nx.set_node_attributes 를 사용하여 한번에 업데이트해주는 경우.
"""
#G = nx.general_random_intersection_graph()
N = 500# 3000
p = 0.6
G = nx.fast_gnp_random_graph(N, p)

node_weight_dict = {
    n:v
    for n, v in zip(G.nodes(), np.random.uniform(0, 1, len(G.nodes())))
}
edge_weight_dict = {
    e: v
    for e, v in zip(G.edges(), np.random.uniform(0, 1, len(G.edges())))
}
def CASE1():
    print("== CASE 1: with loop")
    #print(edge_weight_dict)
    start_time = time.time()
    for n in G.nodes():
        G.nodes[n]['weight']=node_weight_dict[n]
    for (u, v), value in edge_weight_dict.items():
        G[u][v]['weight'] = value
    """
    for e in G.edges():
        G.edges[e]['weight']=edge_weight_dict[e]
    """
    #print(G.edges(data=True))
    time_performance = time.time() - start_time
    print(f"N: {N}, time: {time.time() - start_time:9.3f}")
    print("==" * 30)
    return time_performance

def CASE2():
    print("== CASE 2: nx.set_node_attributes")
    start_time = time.time()
    nx.set_node_attributes(G, node_weight_dict, 'node_weight')
    nx.set_edge_attributes(G, edge_weight_dict, 'edge_weight')
    time_performance = time.time() - start_time
    print(f"N: {N}, time: {time.time() - start_time:9.3f}")
    print("=="*30)
    return time_performance

exec_N = 30
case1_times = []
for i in range(0, exec_N):
    case1_times.append(CASE1())
case2_times = []
for i in range(0, exec_N):
    case2_times.append(CASE2())

print(f"CASE1: {np.mean(case1_times):9.3f}")
print(f"CASE2: {np.mean(case2_times):9.3f}")
```


## Worse Case

- 물론, 다음과 같이 코드를 작성할 경우, 느려질 수 있습니다. 

```python
# G.nodes가 이미 iterable한데, 이를 다시, 리스트로 복사하여 생성하므로 느려짐.
# 오히려 이런 경우에는 list comprehension을 만들지 말고 generator를 만드는 것이 훨씬 효과적.
for n in [n in for n G.nodes()]:
    G.nodes[n]['weight']=node_weight_dict[n]
```

- 이미 여러 번 접근하여 계속 값을 반복하여 읽어올 경우(지금처럼 `edge_weight_dict`에 접근, `G`에 접근) 할 경우 시간이 오래 걸림.

```python
# WORSE case
for e in G.edges():
    G.edges[e]['weight']=edge_weight_dict[e]
# Better case
for e, value in edge_weight_dict.items():
    G.edges[e]['weight'] = value
```


## wrap-up

- [nx.set_node_attributes](https://networkx.github.io/documentation/stable/_modules/networkx/classes/function.html#set_node_attributes)를 봐도 특별히 병렬적인 처리를 고려하고 있지는 않습니다. 
- 다만, 만약 `numpy`를 이용하여 조금 더 빠르게 처리한다거나, python pure하게 코딩하여 `numpy`의 형태로 읽고 쓸수 있다면, 더 빨라질 수도 있지 않을까? 싶어요. 
- 즉, pure python으로 코딩을 잘 했다면, 굳이 메소드를 쓸 필요는 없다, 라는 것을 말해주는 것이기도 하죠.