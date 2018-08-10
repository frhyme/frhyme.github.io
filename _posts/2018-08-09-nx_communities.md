---
title: 네트워크에서 비슷한 그룹을 찾아봅시다. 
category: python-lib
tags: python python-lib networkx network community clustering centrality betweenness metric 
---

## 네트워크에서 community 찾기 

- 일단 이건 일종의 clustering이라고 생각하셔도 상관없습니다. 일단 점과 선으로 된 네트워크를 구성했을 때, 비슷한 집단끼리 묶어보고싶잖아요. 전체 네트워크만 보는 건 큰 의미가 없으니까 이걸 좀 비슷한 놈끼리 묶어보자. 이런 생각이 들죠. 
- 이걸 네트워크에서 어떻게 할 수 있을까요? 

## 일단 clustering.

- 우리는 네트워크를 가지고 있습니다. 따라서 네트워크를 `adjancency matrix`로 변형할 수도 있죠. 
- 따라서, 개별 node를 다른 node들과 얼마나 떨어져 있는지를 vector값으로 표현할 수 있습니다. 각 값을 vector로 표현할 수 있으면 벡터간의 거리를 계산해서 가까운 놈은 묶어주고 아니면 안 묶어주고 이런 식으로 처리할 수 있죠. 이게 바로 클러스터링입니다. 
- 하지만, 클러스터링만으로는 잘 되지 않아요. `sklearn`에 있는 spectral clustering을 이용해봤는데 잘 안되더라구요. 

## cut edge

- 그래서 생각을 해봅니다. 네트워크에서 edge를 잘라가면서 네트워크가 어떻게 변화하는지를 볼 수 있지 않을까 하는 생각을 해요. 
- betweenness centrality가 높은 edge를 잘라나가다 보면 적절하게 클러스터가 나뉘지 않을까? 싶어요. 

- 예를 들면 다음과 같습니다. 
- 아래 그림에서처럼 가장 betweenness centrality가 높은 edge를 자르다보면 밀도 가 높은 두 sub-network로 구분되게 됩니다. 

![](/assets/images/markdown_img/180808_edge_bet_cent_cut.svg)

```python
## 테스트 그래프 생성
G = nx.Graph()
G.add_nodes_from([chr(c) for c in range(ord('A'), ord('A')+15)])
# add edge
G.add_edges_from([('A', n) for n in list(G.node())[:10]])
G.add_edges_from([('G', n) for n in list(G.node())[11:]])
G.add_edges_from([('B', 'J'), ('C', 'J'), ('C', 'H'), ('H', 'E'), ('E', 'D'), ('D', 'I'), 
                  ('I', 'F'), ('B', 'K'), ('K', 'F')])
G.add_edges_from([('O', 'N'), ('N', 'L'), ('M', 'L'), ('O', 'K'), ('K', 'M')])
G.add_edges_from([('A', 'K'), ('G', 'K')])
G.remove_edge('A', 'G'), 
#pos = nx.spring_layout(G)
#G.remove_node('K')
#G.remove_nodes_from(['A', 'G'])
####
f, axes = plt.subplots(1, 4, sharex=True, sharey=True)
f.set_size_inches((20, 6)) 
i=0
while True:
    #ax = axes[i//2][i%2]
    ax = axes[i]
    nx.draw_networkx_nodes(G, pos, node_shape='o', node_size=400, 
                           node_color='pink', ax=ax
                           #node_color=['Red' if n is 'K' else 'pink'  for n in G.nodes()]
                          )
    #edge_color_lst = list(nx.edge_betweenness_centrality(G).values())
    #edge_color_lst = [(ec)/(max(edge_color_lst) - min(edge_color_lst)) for ec in edge_color_lst]
    nx.draw_networkx_edges(G, pos, width = 3, 
                           edge_cmap = plt.cm.binary, ## 그냥 cmap이 아니라 edge_cmap으로 넘겨야 함 
                           edge_color = list(nx.edge_betweenness_centrality(G).values()), 
                           edge_vmin=-0.05, ax=ax
                           #edge_vmin=0, edge_vmax=1.0
                          )
    ## font family에는 font_name이 들어가야 함. 블로그에 정리해둠
    nx.draw_networkx_labels(
            G, pos, font_family='BM JUA_OTF', font_color='black', font_size=15,
            ax=ax
        )
    #plt.axis('off')
    ax.set_axis_off()
    #plt.savefig('../../assets/images/markdown_img/180807_centrality_deg_bet_net.png', dpi=200)
    #plt.show()
    if nx.is_connected(G):
        r_edge = max(list(nx.edge_betweenness_centrality(G).items()), key=lambda x: x[1])[0]
        G.remove_edge(*r_edge)
        i+=1
    else:
        break
plt.tight_layout()
plt.savefig('../../assets/images/markdown_img/180808_edge_bet_cent_cut.svg')
plt.show()
```

- 아래 그림처럼, betweenness centrality가 높은 edge를 자르다보면, 밀집도가 높은 cluster로 잘라지게 됩니다. 이렇게 community를 만드는 방법을 **girvan_newman**이라고 합니다. 

![](/assets/images/markdown_img/180808_edge_bet_cent_cut.svg)

## finding communities: girvan_newman

- [girvan_newman](https://networkx.github.io/documentation/latest/reference/algorithms/generated/networkx.algorithms.community.centrality.girvan_newman.html#networkx.algorithms.community.centrality.girvan_newman)는 앞서 말씀드린 바와 같이 가장 betweenness centrality가 높은 edge를 자르면서 community 를 만듭니다. 

- 사용하는 방법은 다음처럼 매우 간단합니다. 

```python
from networkx.algorithms.community import girvan_newman

## girvan_newman은 가장 중요한 edge를 자르는데
## 아무 것도 넘기지 않고 실행하면, edge_betweenness centrality를 사용해서 자르고 
## 그렇지 않을 경우에는 graph를 input으로 받고, edge를 출력해주는 function을 넘겨주어야 함 
## 아래는 아무것도 넘기지 않았을때와 똑같은 의미를 가지는 함수 

def most_valuable_edge(g):
    return max(nx.edge_betweenness_centrality(g).items(), key=lambda x: x[1])[0]

comm = girvan_newman(G, most_valuable_edge=most_valuable_edge)

## girvan_newman으로 만든 iterator는 끝까지 가면 모두 1개 크기의 세트로 이루어진 커뮤니티 세트가 나옴 
for i, comms in enumerate(girvan_newman(G)):
    print('community set_{:0>2d}'.format(i))
    print("="*30)
    for i, c in enumerate(comms):
        print("community_{:0>2d}: {}".format(i, c))
    print("="*30)
```

- 실행 결과는 다음과 같습니다. 

```
community set_00
==============================
community_00: {'I', 'C', 'J', 'D', 'B', 'E', 'A', 'H', 'F'}
community_01: {'K', 'L', 'O', 'N', 'M', 'G'}
==============================
community set_01
==============================
community_00: {'I', 'C', 'D', 'E', 'A', 'H', 'F'}
community_01: {'J', 'B'}
community_02: {'K', 'L', 'O', 'N', 'M', 'G'}
==============================
community set_02
==============================
community_00: {'I', 'D', 'E', 'A', 'F'}
community_01: {'J', 'B'}
community_02: {'H', 'C'}
community_03: {'K', 'L', 'O', 'N', 'M', 'G'}
==============================
community set_03
==============================
community_00: {'F', 'I', 'A', 'D'}
community_01: {'J', 'B'}
community_02: {'H', 'C'}
community_03: {'E'}
community_04: {'K', 'L', 'O', 'N', 'M', 'G'}
==============================
community set_04
==============================
community_00: {'F', 'I', 'A', 'D'}
community_01: {'J', 'B'}
community_02: {'H', 'C'}
community_03: {'E'}
community_04: {'N', 'O', 'K', 'G'}
community_05: {'M', 'L'}
==============================
community set_05
==============================
community_00: {'F', 'I', 'A'}
community_01: {'J', 'B'}
community_02: {'H', 'C'}
community_03: {'D'}
community_04: {'E'}
community_05: {'N', 'O', 'K', 'G'}
community_06: {'M', 'L'}
==============================
community set_06
==============================
community_00: {'F', 'I', 'A'}
community_01: {'J', 'B'}
community_02: {'H', 'C'}
community_03: {'D'}
community_04: {'E'}
community_05: {'O', 'K', 'G'}
community_06: {'M', 'L'}
community_07: {'N'}
==============================
community set_07
==============================
community_00: {'A'}
community_01: {'J', 'B'}
community_02: {'H', 'C'}
community_03: {'D'}
community_04: {'E'}
community_05: {'F', 'I'}
community_06: {'O', 'K', 'G'}
community_07: {'M', 'L'}
community_08: {'N'}
==============================
community set_08
==============================
community_00: {'A'}
community_01: {'B'}
community_02: {'H', 'C'}
community_03: {'D'}
community_04: {'E'}
community_05: {'F', 'I'}
community_06: {'O', 'K', 'G'}
community_07: {'J'}
community_08: {'M', 'L'}
community_09: {'N'}
==============================
community set_09
==============================
community_00: {'A'}
community_01: {'B'}
community_02: {'C'}
community_03: {'D'}
community_04: {'E'}
community_05: {'F', 'I'}
community_06: {'O', 'K', 'G'}
community_07: {'H'}
community_08: {'J'}
community_09: {'M', 'L'}
community_10: {'N'}
==============================
community set_10
==============================
community_00: {'A'}
community_01: {'B'}
community_02: {'C'}
community_03: {'D'}
community_04: {'E'}
community_05: {'F'}
community_06: {'O', 'K', 'G'}
community_07: {'H'}
community_08: {'I'}
community_09: {'J'}
community_10: {'M', 'L'}
community_11: {'N'}
==============================
community set_11
==============================
community_00: {'A'}
community_01: {'B'}
community_02: {'C'}
community_03: {'D'}
community_04: {'E'}
community_05: {'F'}
community_06: {'G'}
community_07: {'H'}
community_08: {'I'}
community_09: {'J'}
community_10: {'O', 'K'}
community_11: {'M', 'L'}
community_12: {'N'}
==============================
community set_12
==============================
community_00: {'A'}
community_01: {'B'}
community_02: {'C'}
community_03: {'D'}
community_04: {'E'}
community_05: {'F'}
community_06: {'G'}
community_07: {'H'}
community_08: {'I'}
community_09: {'J'}
community_10: {'K'}
community_11: {'M', 'L'}
community_12: {'N'}
community_13: {'O'}
==============================
community set_13
==============================
community_00: {'A'}
community_01: {'B'}
community_02: {'C'}
community_03: {'D'}
community_04: {'E'}
community_05: {'F'}
community_06: {'G'}
community_07: {'H'}
community_08: {'I'}
community_09: {'J'}
community_10: {'K'}
community_11: {'L'}
community_12: {'M'}
community_13: {'N'}
community_14: {'O'}
==============================
```


## finding communities with k: asyn_fluidc

- 이는 k-clustering처럼 그룹의 수만큼 잘라주는 방법을 말합니다. 
- 매번 k의 값을 2로 하고, 큰 놈만 잘라주는 식으로 해도 나쁘지는 않겠네요. 

```python
from networkx.algorithms.community.asyn_fluidc import asyn_fluidc
## 끊어져 있는 graph에서는 돌아가지 않음. 
if nx.is_connected(G): 
    for k in range(1, 5):
        for i, community in enumerate(asyn_fluidc(G, k=k)):
            print("community_{:0>2d}: {}".format(i, community))
        print("="*40)
else:
    print("G가 not connected이면 실행안됨")
```

```
community_00: {'I', 'K', 'L', 'C', 'O', 'J', 'B', 'D', 'E', 'A', 'H', 'N', 'F', 'M', 'G'}
========================================
community_00: {'I', 'C', 'J', 'D', 'E', 'A', 'H', 'F'}
community_01: {'K', 'L', 'O', 'B', 'N', 'M', 'G'}
========================================
community_00: {'J', 'B', 'C'}
community_01: {'I', 'D', 'E', 'A', 'H', 'F'}
community_02: {'K', 'L', 'O', 'N', 'M', 'G'}
========================================
community_00: {'F', 'I', 'D'}
community_01: {'O', 'N', 'K', 'G'}
community_02: {'L', 'M'}
community_03: {'C', 'J', 'B', 'E', 'A', 'H'}
========================================
```

## finding communities: label propagation

- 이는 random하게 node에 라벨링을 해 가면서, 이웃 노드들에 가장 많이 칠해진 label을 본인 노드의 label로 정해가는, 일종의 greedy한 algorithm을 말하는 것 같습니다만. 이상헤 안되요. 
- 그래서 일단 무시합니다. 

```python
## 이 method의 경우는 girvan_newman과 다르게 단 한가지 방법에 대해서만 리턴함. 
## label propagation은 노드에 랜덤하게 라벨을 칠하고, 그 노드의 이웃한 노드들에서 가장 많이 발견되는 
## 라벨로 현재 노드를 칠해주는 것을 말함 

## directional graph의 경우 쓰는 method 
from networkx.algorithms.community.label_propagation import asyn_lpa_communities
## undirectional graph의 경우 쓰는 method 
from networkx.algorithms.community.label_propagation import label_propagation_communities

for i, comm in enumerate(asyn_lpa_communities(G)):
    print("community_{:0>2d}: {}".format(i, comm))
print("="*20)
for i, comm in enumerate(label_propagation_communities(G)):
    print("community_{:0>2d}: {}".format(i, comm))
```

## validation partition

- 그래서, 그 결과가 얼마나 잘 되었는지를 평가합니다. 
- `coverage`, `performance` 라는 두가지 메트릭이 있는데요. 다음처럼 쓸 수 있습니다. 

```python
from networkx.algorithms.community.asyn_fluidc import asyn_fluidc
from networkx.algorithms.community import coverage, performance

coverage_lst, performance_lst = [], [] 
for k in range(1, len(G.nodes())):
    communities = list(asyn_fluidc(G, k=k))
    coverage_lst.append( coverage(G, communities) )
    performance_lst.append( performance(G, communities) )
## 그림에서 보는 것처럼 performance가 충분히 높아지고 변화의 폭이 줄어들고 
## coverage가 충분히 큰 정도에서 멈추면 될듯함. 
## 따라서 적당한 k는 아마도 2-3 정도 
plt.figure(figsize=(14, 6))
plt.plot(coverage_lst, 'o-', label='coverage')
plt.plot(performance_lst, '^--', label='performance')
plt.legend(fontsize=15)
plt.savefig("../../assets/images/markdown_img/180808_coverage_performance_eva.svg")
plt.show()
```

![](/assets/images/markdown_img/180808_coverage_performance_eva.svg)


## 커뮤니티 뽑고 그림 그리기 

- 그래프에서 커뮤니티를 뽑고 그림을 그려줍니다. 
- `girvan_newman`을 이용해서 커뮤니티를 뽑았으며, performance의 변화 폭이 충분히 작아질때까지 자릅니다. 
- 그 다음 coverage, performance를 플로팅하여 적절하게 끊겼는지를 파악합니다. 

```python
## community 

import networkx as nx
import matplotlib.pyplot as plt
from networkx.algorithms.community import girvan_newman
#from networkx.algorithms.community.asyn_fluidc import asyn_fluidc
from networkx.algorithms.community import coverage, performance

community_lst = [] ## 커뮤니티 리스트 
coverage_lst, performance_lst = [], [] 
## 커뮤니티가 얼마나 잘 뽑혔는지를 평가하는 지표

for i, comms in enumerate(girvan_newman(tempG)):
    ## performance의 변화폭이 많이 적어지면 더이상 cluster를 나누어도 이득이 없으므로 멈춤
    if i!=0 and abs(performance(tempG, comms) - performance_lst[-1])< 0.01:
        break
    else:
        community_lst.append(comms), 
        coverage_lst.append(coverage(tempG, comms)), performance_lst.append(performance(tempG, comms))

## performance, coverage의 값을 확인한 다음 
## performance의 변화 폭이 작고, coverage가 충분히 클 때까지 자름
plt.figure(figsize=(8, 4))
plt.plot(coverage_lst, label='coverage', marker='o', color='r')
plt.plot(performance_lst, marker='^', label='performance', color='b')
plt.legend(fontsize=15)
plt.savefig('../../assets/images/markdown_img/180809_network_performance_coverage.svg')
plt.show()
```

![](/assets/images/markdown_img/180809_network_performance_coverage.svg)

- 그리고 만든 커뮤니티를 그림으로 표현해줍니다. 
    - 일단 원래 그래프의 node에 각 node가 속한 community 값을 넘겨주고, 그 값에 따라서 칼라링을 합니다. 
- 특히, 조금 어려웠던 부분은 legend를 그리는 부분 이었는데, 그냥 node에 label을 넘길 경우에는 그 값이 모두 node위에 텍스트로 표현되고, legend에는 모든 node의 개수가 다 뜹니다. 
- 그래서 저는 약간 돌려서, 제 axis 바깥 쪽에 `plt.scatter`를 이용해서 node와 같은 크기의 색깔의 점들을 찍고, label을 같이 넘긴 다음 `plt.legend()`로 사용했습니다. 뭔가 깔끔한 방법은 아니지만, 이렇게 하면 되긴 하니까요. 되는게 중요합니다. 

```python
## 원래 그래프의 노드의 attribute에 community 정보를 넘겨줌
## 원래 그래프의 노드의 attribute에 community 정보를 넘겨줌
selected_community = community_lst[-1]
for i, comm in enumerate(selected_community):
    for p in comm: 
        tempG.nodes()[p]['community'] = i 

## 이제 그림을 그려줌 

plt.figure(figsize=(18, 7))
#pos = nx.spring_layout(tempG)


## 아래처럼 노드별로 label을 먹여서 따로 그려줘도 안됨
## plt.legend를 찍으면 모든 node가 서로 다른 것처럼 표시됨. 
nx.draw_networkx_nodes(tempG, pos=pos, node_size = 200,
                       node_color = [n[1]['community'] for n in tempG.nodes(data=True)], 
                       cmap=plt.cm.gist_rainbow, 
                       alpha=0.5, labels={ n[0]:n[1]['community'] for n in tempG.nodes(data=True)},
                      )


edge_color = np.array([e[2]['weight'] for e in tempG.edges(data=True)])
## normalization 
for i in range(0, 3):
    edge_color = np.log1p(edge_color)
nx.draw_networkx_edges(tempG, pos=pos, 
                       edge_color = edge_color, edge_cmap= plt.cm.Greys, 
                       edge_vmin=edge_color.min(), edge_vmax=edge_color.max(), 
                      )

## 빈곳에 그림을 그리고 가림 
pos_min = (min((x for x, y in pos.values())), min((y for x, y in pos.values())))
pos_max = (max((x for x, y in pos.values())), max((y for x, y in pos.values())))


## 그려진 네트워크에 맞춰서 x, y 축을 조절 
plt.xlim(pos_min[0]-0.1, pos_max[0]+0.1)
plt.ylim(pos_min[1]-0.1, pos_max[1]+0.1)

tempx, tempy = 100, 100
community_label_lst = ['대학원사람들', '동아리1', '독서모임1', '가족', '훈련소', '개발모임', '동아리2', '독서모임2', '학과동기']
for i, c in enumerate(plt.cm.gist_rainbow(np.linspace(0.0, 1.0, len(selected_community)))):
    plt.scatter(tempx, tempy, c =c, s=100, marker='o', label=community_label_lst[i], 
                alpha=0.5, zorder=0)
plt.scatter(tempx, tempy, s=200, marker='o', c='white', zorder=1)
plt.legend(loc='upper left', 
           prop = fm.FontProperties(family=BMJUA.get_name(), 
                                    #style='normal', 
                                    size=20), 
           markerscale=1.2, ## 마커 크기를 조절하자. 
           bbox_to_anchor=(1.0, 0.75), 
           #prop = {'font_family':BMJUA.get_name()}
          )
plt.axis('off')
plt.tight_layout()
plt.savefig('../../assets/images/markdown_img/180809_network_community.png', dpi=200)
plt.show()
```

![](/assets/images/markdown_img/180809_network_community.svg)