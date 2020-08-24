---
title: networkx의 bipartite 다루기 
category: python-lib
tags: python python-lib networkx bipartite 
---

## bipartite graph 

- bipartie graph는 set A와 set B 간에는 연결되는데, A의 node a들 끼리 연결되거나, B의 node b들 끼리 연결되는 일이 없는 경우를 말합니다. 예를 들면, set A는 사람이고, set B는 영화일 경우, "이승훈이 '인크레더블'을 봤다"라는 것을 그래프로 표현하면, bipartite graph가 됩니다. 이러한 경우를 보통 bipartite한 graph로 고려합니다. 

## complete bipartite graph 

- 완전한 bipartite graph를 만들어봅시다. 

```python
import networkx as nx 

cbg = nx.complete_bipartite_graph(3, 7)
bs1, bs2 = nx.bipartite.sets(cbg)## bipartite 세트로 나누어줍니다. 

plt.figure(figsize=(8, 4))
nx.draw_networkx(cbg, pos = nx.shell_layout(cbg))
plt.axis('off')
plt.savefig("../../assets/images/markdown_img/180810_bipartite_cg.svg")
plt.show()
```

![](/assets/images/markdown_img/180810_bipartite_cg.svg)

- 그런데, 그림이 썩 마음에 들지는 않아요. bipartite한 graph에 맞는 layout이 있을 텐데, 아직은 라이브러리에서 개발중인 것 같습니다. 
- 그래서 제가 임의로 만들어줍니다. 

```python
def bipartite_layout(inputG):
    ## bipartite한 graph의 layout
    if nx.is_bipartite(inputG) and nx.is_connected(inputG):## connected and bipartite
        bs1, bs2 = nx.bipartite.sets(inputG)
        pos = {}
        pos.update({n:(0, 1.0/(len(bs1)+1)*(i+1)) for i, n in enumerate(bs1)})
        pos.update({n:(1, 1.0/(len(bs2)+1)*(i+1)) for i, n in enumerate(bs2)})
        return pos
    else:# 이 경우 none을 리턴하므로, default layout으로 그림이 그려지게 됩니다. 
        print("it is not bipartite and not connected")
        
cbg = nx.complete_bipartite_graph(3, 7)
bs1, bs2 = nx.bipartite.sets(cbg)## bipartite 세트로 나누어줍니다. 

plt.figure(figsize=(8, 4))
nx.draw_networkx(cbg, pos = bipartite_layout(cbg))
plt.axis('off')
plt.savefig("../../assets/images/markdown_img/180810_bipartite_cg_with_bi_layout.svg")
plt.show()
```

![](/assets/images/markdown_img/180810_bipartite_cg_with_bi_layout.svg)

## random bipartite graph 

- 일단 complete bipartite graph 말고 random bipartite graph를 만들어봅시다. 

```python
## edge의 수를 비율로 조절. 단 이 경우에는, 가끔 connected가 유지되지 않는 상태로 나올 수 있음. 
rbg = nx.bipartite.random_graph(3, 6, 0.5)
## degree list를 넘김. 따라서, 두 list의 sum이 같아야 함. 이 경우에도 connected가 유지되지 않는 경우가 종종 발생함. 
## 하지만, 어떤 node도 모두 연결되도록 할 수는 있음. 
g = nx.bipartite.configuration_model(aseq=[2, 2, 2], bseq=[1, 2, 3], 
                                     create_using=nx.Graph()## nx.MultiGraph()로 넘기면 edge가 여러개 생기는 경우 
                                    )
## 이 방법의 경우 connection이 거의 끊어지지 않음. 
g = nx.bipartite.havel_hakimi_graph([2, 2, 2], [1,2,3], create_using=nx.Graph())

nx.draw_networkx(g, pos=bipartite_layout(g))
plt.axis('off')
plt.savefig("../../assets/images/markdown_img/180810_bipartite_config_model.svg")
plt.show()
```

![](/assets/images/markdown_img/180810_bipartite_config_model.svg)


## projection 

- bipartite graph를 one-mode graph로 변형합니다. 
- 간단히 말하면 (a1, b1), (b1, a2) 라는 엣지들이 있으면 이를 (a1, a2)로 변경해주는 것을 말합니다. 

```python
g = nx.complete_bipartite_graph(5, 3)

plt.figure(figsize=(12, 6))
nx.draw_networkx(g, pos=bipartite_layout(g))
s1, s2 = nx.bipartite.sets(g)
plt.title('bipartite graph')
plt.savefig('../../assets/images/markdown_img/180808_bipartite_graph_original.svg')
plt.show()

plt.figure(figsize=(12, 4))
f, axes = plt.subplots(1, 2)
f.set_size_inches(12, 6)
nx.draw_networkx(
    nx.bipartite.projected_graph(g, s1), ax=axes[0]## set1에 대해 projection
)
nx.draw_networkx(
    nx.bipartite.projected_graph(g, s2), ax=axes[1]## set2에 대해 projection
)
plt.savefig('../../assets/images/markdown_img/180808_projected_graph.svg')
plt.show()
```

- 원래 그래프가  

![](/assets/images/markdown_img/180808_bipartite_graph_original.svg)

- 다음처럼 변경됩니다. 

![](/assets/images/markdown_img/180808_projected_graph.svg)