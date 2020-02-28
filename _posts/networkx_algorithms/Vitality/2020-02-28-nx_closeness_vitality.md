---
title: networkx - closeness vitality
category: python-libs
tags: python python-libs networkx topology closeness betweenness-centrality
---

## 1-line summary 

- closeness vitality

## Closeness vitality

- Closeness vitality는 번역하자면, "근접 생명력/필수"처럼 번역될텐데, 의미가 이상해지는 군요. 
- 계산방법으로 보면, 이는 특정 노드가 해당 네트워크에서 삭제되었을 때, 전체 graph에서 모든 node pair간의 shortest-path-length가 얼마나 달라지는지를 의미합니다. 
- 즉, "node `u`를 제거했을 때, 네트워크의 총 shortest path length의 값이 크게 증가한다면, 니는 해당 노드가 그래프 내에서 미치는 영향 혹은 전체 flow에 미치는 영향이 크다고 말할 수 있는 것이죠. 
- 따라서, 이 값은 기존의 closeness-centrality, betweenness-centrality등과 비슷한 경향성을 보일 수 있죠. 
- 다시, 여기서 "생명력"이나 "필수적임"을 뜻하는 `vitality`를 쓰게 된 이유는 "transportation network에서 얼마나 필수적인 노드 인지를 측정하기 위해서" 입니다. 즉, 특정 node의 closeness vitality가 크다면 이는 해당 노드가 네트워크에 미치는 영향이 크다는 것을 말하는 것이죠.

## implementation `closeness_vitality`

- 예외처리를 제외하면, `nx.closeness_vitality(G)`와 동일합니다.

```python
import networkx as nx 

def closeness_vitality(G, weight=True):
    """
    wiener_index: graph G의 모든 node pair의 shortest_path_length의 합.
    각 node가 제외되었을 때, wiener_index가 어떻게 변화하는지를 측정.
    즉, 해당 node가 전체 graph의 flow에 얼마나 영향을 미치는지를 측정하며, 
    betweenness centrality와 유사한 결과가 도출됨.
    """
    clo_vital_dict = {n: None for n in G}
    Before_weiner_index = nx.wiener_index(G, weight=weight)
    for n in G: 
        G_cp = G.copy() 
        G_cp.remove_node(n)
        After_weiner_index = nx.wiener_index(G_cp, weight=weight)
        clo_vital_dict[n] = (Before_weiner_index - After_weiner_index)
    return clo_vital_dict 
```

## reference

- [networkx.algorithms.vitality.closeness_vitality](https://networkx.github.io/documentation/stable/reference/algorithms/generated/networkx.algorithms.vitality.closeness_vitality.html#networkx.algorithms.vitality.closeness_vitality)
