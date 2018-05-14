---
title: bipartite graph를 다룰 거에요!!
category: python-lib
tags: python python-lib networkx 

---

## bipartite graph를 다뤄 봅시다. 

- author keyword 와 index keywords 는 서로 다른 의미를 가집니다. 하나의 논문에는 author keyword와 index keyword가 둘 다 있는데, 이 edge를 중심으로 equivalence를 측정할 수 있지 않을까? 생각해봅니다. 
- 단 `nx.Graph()`에서는 이름이 같으면 안되는데, 이건 그냥 끝에 '(i)' 를 붙이거나 해서 처리할 수 있을 것 같긴 하네요. 


## do it. but failed. 

- 아주 간단하게 author keyword 와 index keyword의 데이터를 전처리해주고, bipartite graph를 생성해줍니다. 여기서 node의 weight는 빈도, edge의 weight 또한 빈도입니다. 

```python
def basic_filtering_for_series(input_series):
    r_s = input_series.fillna("").apply(lambda s: s.strip().lower())
    r_s = r_s.apply(lambda s: s.split(";"))
    # remove special char and remove space 
    def change_word(in_w):
        r_c = []
        for c in in_w:
            if 'a' <= c <= 'z' or '0' <= c <='9' or c==' ':
                r_c.append(c)
        return "".join(r_c).strip()
    r_s = r_s.apply(lambda ks: list(filter(lambda k: True if k!="" else False, map(change_word, ks))))
    return r_s
auth_col = basic_filtering_for_series(df['Author Keywords'])
index_col = basic_filtering_for_series(df['Index Keywords'])
auth_index_df = pd.DataFrame({"auth_kwd":auth_col, "index_kwd":index_col})

biG = nx.Graph()
edge_lst = []
for i in range(0, len(auth_index_df)):
    auth_l = list(auth_index_df['auth_kwd'].iloc()[i])
    index_l = list(auth_index_df['index_kwd'].iloc()[i])
    if len(auth_l) != 0 and len(index_l)!=0:
        edge_lst += [ (auth, ind+"(i)") for auth in auth_l for ind in index_l ]
# add node
for e in collections.Counter(edge_lst).most_common():
    auth_node, ind_node = e[0][0], e[0][1]
    e_weight = e[1]
    for node in [auth_node, ind_node]:
        if node in biG.nodes():
            biG.nodes(data=True)[node]['weight'] = biG.nodes(data=True)[node]['weight'] + e_weight
        else:
            biG.add_nodes_from([(node, {'weight':e_weight})])
# add edges

biG.add_edges_from(
    (e[0][0], e[0][1], {'weight':e[1]}) for e in collections.Counter(edge_lst).most_common()
)
print("complete")
rawBiG = biG.copy()
```

- 만든 bipartite graph를 biadjacency matrix로 변환해줍니다. 여기서 `row order`는 auth keyword로 넘겨줍니다. 이렇게 한 다음, row vector 간의 거리를 재서 가까운 node pair를 뽑아내면 이 들 간은 '의미적으로 유사'하다는 성질을 가질 수 있지 않을까? 싶습니다. 그러나. 
    - 아래 결과를 보시면 그렇지 않아요. 맨 처음 나오는 의미적으로 가장 유사한 노드 페어는 ('shape memory effect', 'sme')입니다. 우리가 보려는 것은 'small medium enterprise'지, 'shape memory effect'가 아니죠. 이런 일종의 노이즈가 게속 잡히는 것 같은데, 이를 걸러내기 위해서는 전체 그래프를 구성하고, 혼동이 되는 node 'sme'를 삭제한 다음 subgraph를 파악해서 이를 게속 진행할 수 있을 것 같네요. 

- 결론적으로는 bipartite와 상관업이 데이터 자체에 문제가 있는 것으로 보이네요. 

```python
biG = rawBiG.copy()
print("is bipartite?: {}".format(nx.is_bipartite(biG)))
#left, right = nx.bipartite.sets(biG)
# drop thw low nodes
print("before filtering node size: {}".format(len(biG.nodes())))
for n in biG.copy().nodes(data=True):
    if n[1]['weight'] < 100: # 쓸데없는 node들을 삭제합니다. 
        biG.remove_node(n[0])
print("after filtering node size: {}".format(len(biG.nodes())))
nodesetA, nodesetB = nx.bipartite.sets(biG)
try:
    # need row order, 
    biadj_matrix = nx.algorithms.bipartite.biadjacency_matrix(biG, row_order=nodesetA)
except:
    print("not yet")
    
print()
bi_df = pd.DataFrame(biadj_matrix.toarray(), index=nodesetA, columns=nodesetB)
bi_df = bi_df.apply(lambda col: (col - 0)/(col.max() - col.min()))# scaling by column
n_n_dist_lst  = [
    ( bi_df.index[i], bi_df.index[j], euclidean(bi_df.iloc()[j], bi_df.iloc()[i]) ) 
    for i in range(0, len(bi_df)-1) for j in range(i+1, len(bi_df))
]

for nn in sorted(n_n_dist_lst, key=lambda x: x[2], reverse=True)[:10]:
    print(nn)
```

```
is bipartite?: True
before filtering node size: 38369
after filtering node size: 791

('smes', 'shape memory effect', 15.436279758020806)
('shape memory alloys', 'smes', 15.313835112256491)
('smes', 'apoptosis', 15.297551958555223)
('antioxidant', 'smes', 15.297110857498893)
('smes', 'martensitic transformation', 15.28047904820015)
('biodiesel', 'smes', 15.252823023508066)
('platinum', 'smes', 15.250537382105268)
('smes', 'crystal structure', 15.24602190003883)
('xray diffraction', 'smes', 15.228784583558754)
('oxidative stress', 'smes', 15.22873389330548)
```