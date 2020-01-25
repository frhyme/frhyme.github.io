---
title: networkx를 이용하여 기본적인 centrality 분석하기 
category: python-lib
tags: python python-lib networkx matplotlib

---

## centrality는 무엇인가요? 

- 한국말로 하면 '중심도'가 되겠네요. 네트워크가 구성되었을 때, 우리가 궁금한 것은 네트워크에서 어떤 노드가 중요한 놈인가? 라는 것입니다. `centrality`란 네트워크 상에서 중요한 노드를 찾기 위한 일종의 metric이라고 말하면 될 것 같습니다. 

## degree centrality

- `degree centrality`는 각 node별로 직접 연결된 edge의 weight만을 고려합니다. 즉, 해당 node가 직접 가진 영향력의 크기는 얼마인가? 를 측정하는 것이 해당 metric의 의미가 되겠네요.

## weighted degree centrality 

- 다만, 해당 edge의 weight는 모두 같지 않기 때문에, 서로 다른 weight를 고려하는 것이 필요한데, 이상하게도, `networkx`에는 이 weight를 고려해서 degree centrality를 고려하는 일이 없습니다. 왜 그런지는 제가 잘 모르겠지만, 그래서 제가 직접 만들었습니다. 
- `normalization` 정도는 좀 다른데 일단 rank 자체는 별로 변하지 않아요. 

## closeness centrality

- `closeness centrality`는 네트워크의 모든 node로부터 얼마나 가깝게 위치해있는지를 고려하여 centrality를 계산한다.
- 약간의 특이한 점이라면, `closeness centrality`를 계산할 때는 `distance`를 고려해야 하고, 우리가 일반적으로 표현한 `weight`와는 약간 다르다. 
- 여기서 `distance`는 중요할수록 낮아야 하며, 일반적으로 논문 서지정보에서 저자키워드를 대상으로 네트워크를 구성했다면, 해당 edge의 빈도가 높을 수록 이 `distance`를 낮추는 것이 필요하다.
- 헷갈리지 않으려면 edge의 attribute에 `distance`, `weight`를 모두 작성해두는 것이 편할 수 있음. 

## betweenness centrality

- `betweenness centrality`는 네트워크의 모든 노드 쌍 간의 `shortest path`가 해당 노드를 지나는지를 고려한 centrality이다.
- 만약 모든 노드 페어의 `shortest path`가 node a를 지난다면 node a의 `betweenness centrality`는 높다. 
- 이 centrality가 중요한 이유는 이 값은 전체 네트워크의 흐름을 제어하며, 해당 노드가 없어질 경우, 전체 네트워크의 흐름 자체에 영향을 받게 된다.

## eigenvector centrality and pagerank

- 흔히 google의 `pagerank`로 해당 centrality를 말한다. 아주 간단하게 말하면, 아래와 같은데.

> 쎈 놈들이 나와 많이 연결되어 있을 수록 내 eigenvector centrality는 높아진다

- 미묘하게 `pagerank`와 `eigenvector centrality`는 다른데, 

> The eigenvector calculation is done by the power iteration method and has no guarantee of convergence. The iteration will stop after max_iter iterations or an error tolerance of number_of_nodes(G)*tol has been reached.
> The PageRank algorithm was designed for directed graphs but this algorithm does not check if the input graph is directed and will execute on undirected graphs by converting each edge in the directed graph to two edges.

- eigenvector centrality는 수렴하지 않는 경우가 있고 이 경우 에러가 발생된다는 것. pagerank의 경우는 수렴한다는 것 정도가 미묘한 차이라고 할 수 있다. 단, `pagerank`는 원래 웹을 분석하려고 나왔기 때문에, `directed network`를 기본으로 가정하고 진행한다. 그렇지 않을 경우 임의로 `undirected network`를 변환해서 하는데, 어쩌면 당연하지만, 이런 네트워크에서는 수렴하는 것이 쉽지 않다. 물론 weight에 따라 다를 수 있기는 하지만 그래도. 
- 그렇다고 쎈 놈들이 모든 node와 연결되어 있다면 의미가 없다. 쎈 놈이 작은 노드들과만 연결되어 있어서 해당 노드의 영향력이 지나치게 분산화되지 않으며, 그 쎈 놈이 다시 나와 연결되어 있을 때, 나 또한 너무 많은 노드와 연결되어 있지 않아야, 일종의 `sinking point`가 생긴다. 네트워크 상에서 값들이 수렴하는 어떤 지점이 발생하게 되며, 이러한 중심도를 `eigenvector centrality`라고 한다.
- 또한 `pagerank`는 굳이 `weight`를 argument로 넣어주지 않아도 알아서 분석한다. 뭐 그래도 습관적으로 넣어주는 것이 좋긴 하지만.

## just do it. 

- graph로부터 다음 세 가지 centrality와 pagerank를 계산하여 딕셔너리로 리턴해주는 함수를 만들었다. 
    - weighted degree centrality
    - closeness centrality
    - betweenness centrality
    - pagerank
- 분석을 위해 간단하게 만든 graph. 
    ![](/assets/images/markdown_img/sample_graph_for_centrality.svg)
- 정의한 함수 아래의 main code는 삭제해도 된다.

```python
import networkx as nx
import matplotlib.pyplot as plt

"""
- graph로부터 다음 세 가지 centrality와 pagerank를 계산하여 딕셔너리로 리턴해주는 함수
    - weighted degree centrality
    - closeness centrality
    - betweenness centrality
    - pagerank
"""

def return_centralities_as_dict(input_g):
    # weighted degree centrality를 딕셔너리로 리턴
    def return_weighted_degree_centrality(input_g, normalized=False):
        w_d_centrality = {n:0.0 for n in input_g.nodes()}
        for u, v, d in input_g.edges(data=True):
            w_d_centrality[u]+=d['weight']
            w_d_centrality[v]+=d['weight']
        if normalized==True:
            weighted_sum = sum(w_d_centrality.values())
            return {k:v/weighted_sum for k, v in w_d_centrality.items()}
        else:
            return w_d_centrality
    def return_closeness_centrality(input_g):
        new_g_with_distance = input_g.copy()
        for u,v,d in new_g_with_distance.edges(data=True):
            if 'distance' not in d:
                d['distance'] = 1.0/d['weight']
        return nx.closeness_centrality(new_g_with_distance, distance='distance')
    def return_betweenness_centrality(input_g):
        return nx.betweenness_centrality(input_g, weight='weight')
    def return_pagerank(input_g):
        return nx.pagerank(input_g, weight='weight')
    return {
        'weighted_deg':return_weighted_degree_centrality(input_g),
        'closeness_cent':return_closeness_centrality(input_g), 
        'betweeness_cent':return_betweenness_centrality(input_g),
        'pagerank':return_pagerank(input_g)
    }

"""
main code, 나중에 사용할 때 아래 부분은 삭제하는 것이 좋음. 
"""
G = nx.Graph()
G.add_weighted_edges_from(
    [
        ('a', 'b', 10.0), ('b', 'c', 1.0), ('a', 'c', 100.0), ('a', 'd', 10.0)
    ]
)
nx.draw_networkx(G)
plt.axis('off')
plt.savefig('../../assets/images/markdown_img/sample_graph_for_centrality.svg')
for k, v in return_centralities_as_dict(G).items():
    print("{}: {}".format(k, v))
```

```
weighted_deg: {'a': 120.0, 'b': 11.0, 'c': 101.0, 'd': 10.0}
closeness_cent: {'a': 14.285714285714285, 'b': 7.317073170731707, 'c': 13.043478260869566, 'd': 7.317073170731707}
betweeness_cent: {'a': 0.6666666666666666, 'b': 0.6666666666666666, 'c': 0.0, 'd': 0.0}
pagerank: {'a': 0.4748970800683251, 'b': 0.07433357154696582, 'c': 0.3796306755336949, 'd': 0.0711386728510143}
```

## subGraph가 하나가 아니라면? 

- 사실 이상적으로는 모든 노드들이 연결되어 있으면 좋겠지만, 사실 그렇지 않다. `edges`로부터 그래프를 생성했을 때, 해당 그래프는 이미 하나가 아닌 두 개일 이상이기 쉽다. 그렇다면 이 때, centrality는 어떻게 계산되는가?
- 알아서 잘 계산된다. 예를 들어 `betweenness centrality`의 경우 서로 노드가 끊어져 있으면 unreachable하다고 생각하기 때문에, 0으로 계산해서 잘된다. 물론 당연히 `subgraph별로 계산하면 또 다르게 계산되고. 

```python
G = nx.Graph()
G.add_weighted_edges_from(
    [
        ('a', 'b', 1),
        ('a', 'c', 1),
        ('a', 'd', 1),
        ('f', 'g', 1),
        ('g', 'h', 1)
    ]
)
def return_weighted_degree_centrality(input_g, normalized=False):
    w_d_centrality = {n:0.0 for n in input_g.nodes()}
    for u, v, d in input_g.edges(data=True):
        w_d_centrality[u]+=d['weight']
        w_d_centrality[v]+=d['weight']
    if normalized==True:
        weighted_sum = sum(w_d_centrality.values())
        return {k:v/weighted_sum for k, v in w_d_centrality.items()}
    else:
        return w_d_centrality
def print_centrality(input_g, centrality_func):
    print(centrality_func(input_g))
    for i, subG in enumerate(nx.connected_component_subgraphs(input_g)):
        print("subG {}: {}".format(i, centrality_func(subG)))
print("weighted degree centrality")# normalized required
print_centrality(G, return_weighted_degree_centrality)
print("betweenness centrality")
print_centrality(G, nx.betweenness_centrality)
print("closeness centrality")
print_centrality(G, nx.closeness_centrality)
```

```
weighted degree centrality
{'a': 3.0, 'b': 1.0, 'c': 1.0, 'd': 1.0, 'f': 1.0, 'g': 2.0, 'h': 1.0}
subG 0: {'a': 3.0, 'b': 1.0, 'c': 1.0, 'd': 1.0}
subG 1: {'f': 1.0, 'g': 2.0, 'h': 1.0}
betweenness centrality
{'a': 0.2, 'b': 0.0, 'c': 0.0, 'd': 0.0, 'f': 0.0, 'g': 0.06666666666666667, 'h': 0.0}
subG 0: {'a': 1.0, 'b': 0.0, 'c': 0.0, 'd': 0.0}
subG 1: {'f': 0.0, 'g': 1.0, 'h': 0.0}
closeness centrality
{'a': 0.5, 'b': 0.3, 'c': 0.3, 'd': 0.3, 'f': 0.2222222222222222, 'g': 0.3333333333333333, 'h': 0.2222222222222222}
subG 0: {'a': 1.0, 'b': 0.6, 'c': 0.6, 'd': 0.6}
subG 1: {'f': 0.6666666666666666, 'g': 1.0, 'h': 0.6666666666666666}
```