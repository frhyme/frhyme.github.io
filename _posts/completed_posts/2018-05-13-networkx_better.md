---
title: understand networkx better. 
category: python-lib
tags: networkx python python-lib 

---

## understand networkx better. 

- 일반적으로 쓰는 networkx 의 function들은 centrality, draw, add/remove node and edges 가 다인데, 이 외에도 꽤나 유용한 함수들이 많이 있습니다. 이것들을 좀 정리해두는 것이 필요하다고 생각됨. 

## nx.is_connected and nx.is_bipartite

- 노드와 엣지를 그래프에 밀어넣은 다음, 반드시 해야 하는 작업은 현재 네트워크가 모두 연결되어 있는지 확인하는 것이다. 간단한 함수로 확인하고, 나서 불필요한 네트워크는 모두 삭제해주는 것이 좋을 수 있다. 
- 특히 키워드 분석에서는 연결되지 않은 네트워크는 검색 과정에서 잘못 모인 데이터일 수 있다. 예를 들어서 우리가 찾고 싶은 키워드는 'Small Medium Enterprise"이고 따라서 "SME"도 함께 검색했더니 결과적으로 "Shape Memory Effect"가 함께 선정되는 경우를 말한다. 이럴 경우에는 가장 큰 node인 "SME"를 삭제하고 나머지 subgroup이 몇 개로 갈라지는지를 확인하는 것이 필요하다.

### not bipartite

- `nx.is_connected(G)`: 해당 네트워크가 연결되어 있는지를 boolean 값으로 리턴
- `nx.connected_component_subgraphs(G)`: G에 1개 이상의 연결된 componenet들이 있을 때 이를 생성하는 generator를 만들어준다. 위의 `nx.is_connected(G)`와 함께 활용하여, 해당 G의 모든 노드가 서로 연결되어 있지 않을 경우에는, subgraph를 확인하는 것이 필요함
- `nx.adjacency_matrix(G)`: nodes to nodes 인 matrix를 만들어준다. 개별 값은 weight가 있을 경우에는 weight값을 넣어 준다.(directed graph에 대해서는 아직 확인하지 않음)
- `nx.compose_all(G_lst)`: 그래프를 합쳐 주지만, 그래프별로 겹치는 node가 있을 때, weight 값은 최종적으로 들어간 node의 weight가 된다. 예를 들어 `G_lst[0]`에 있는 node `n1`의 weight가 10이고, `G_lst[1]`에 있는 node `n1`의 weight가 100이면, 합쳐지는 것이 아니라, 합쳐진 그래프에서 `n1`의 weight는 110이 된다. 따라서, weight가 중요한 경우에는 직접 코딩을 하는 것이 좋다. 사실 어렵지 않은 부분이니까. 

### for bipartite graph

- `nx.is_bipartite(G)`: 해당 네트워크가 bipartite인지를 boolean으로 리턴. is_connected 가 true가 아니더라도 bipartite할 수는 있다(모든 subG가 is_bipartite 라면 문제가 없음), 단 not connected 인데 bipartite인 경우에는 `biadjacency matrix`를 뽑을 수가 없음. adjacency matrix를 뽑으려면 set를 두 개로 뽑아야 하는데, not connected인 경우에는 이를 알 수 없음
- `nx.bipartite.sets(G)`: bipartite 한 두 세트를 리턴. `setA, setB = nx.bipartite.sets(G)`
- `nx.bipartite.biadjacency_matrix(g1, row_order=setA)`: biadjancecy matrix를 리턴해주는 함수인데, `row_order`(쉽게 행의 이름, index)를 지정해주지 않으면 에러가 발생함. 단 리턴되는 매트릭스는 `scipy.sparse.matrix`. 귀찮아서 그냥 `.toarray()`로 바꿔주거나 `pd.DataFrame()`로 변경해서 활용한다.

- 간단하게 만든 코드 

```python
g1 = nx.Graph()
g1.add_edges_from(
    [(1, 4, {'weight':10}), (1, 6), (1, 2), (3, 2)]
)
print("is bipartite: {}".format(nx.is_bipartite(g1)))
setA, setB = nx.bipartite.sets(g1)
print(setA, setB)
print()
bi_df = pd.DataFrame(
    nx.bipartite.biadjacency_matrix(g1, row_order=setA).toarray(), index=setA, columns=setB
)
print(bi_df)
```
```
is bipartite: True
{1, 3} {2, 4, 6}

   2   4  6
1  1  10  1
3  1   0  0
```


### find clique

- 일반적으로는 component도 많이 쓰지만, `clique`도 군집화된 정도를 보기 위해서 많이 사용하는 편이다. 
- 아래 코드는 간단하게, size가 3이 넘는 clique를 찾는 코드. 2짜리는(edge) 많고, 3짜리가 적음. 

```python
for cliq in nx.find_cliques(biG):
    if len(cliq)>=3:
        print(cliq)
```
