---
title: R&D knowledge map again. 
category: project
tags: python python-lib matplolt networkx 

---

## 후 키워드 네트워크부터 다시 합시다. 

- 키워드 네트워크를 구성했을 때, 만든 네트워크에서 잘못된 노드 들이 있는 경우가 발견되었습니다. `shape memory effect`의 경우 약자가 똑같이 'sme'인 것을 알 수 있습니다. 따라서 다른 것보다 우선 이 부분을 제외하는 것이 필요한 것 같습니다. 
- 또한 앞서 공부한 몇 가지를 활용해서 더 잘 코딩을 할 수 있지 않을까? 생각도 해봅니다. 


## 'shape memory effect' and 'sme'

- 우선 문제가 되는 부분은, 'sme' 는 'small and medium enterprise'일 수도 있고, 'shape memory effect'일 수도 있다는 겁니다. 스코퍼스에서 데이터를 가져올 때, 'sme'로 검색하여 양쪽의 데이터가 다 잡힌 것이죠. 이후에 word-embedding, structure equivalence 를 진행한다고 해도, 현재의 데이터 셋에 일관성이 없어서 이를 해결하는 것이 쉽지 않습니다. 
    - 처음에는 이를 `word-embedding`이 해결해줄거야! 라고 생각했던 것 같은데 그렇지는 않습니다.  
- 따라서, 어떻게 해결할까 고민하다가, 가장 힘이 센(여기서는 일단 degree centrality라고 생각했습니다) 노드를 잘라나가면서 만약 가장 힘이 쎈 노드를 잘라내도 해당 그래프가 여전히 연결성이 있다면(`nx.is_connected`)라면 해당 그래프는 충분히 균일한 구조라고 평가할 수 있지 않을까? 라고 생각했습니다. 

## make graph dense 

- 코드는 대략 다음과 같습니다. `nx.degree_centrality`가 가장 높은 노드를 제외하면서 계속 진행하고, 제외해도 networkx의 전체 connection이 유지되는 경우에는 해당 네트워크는 아직 충분히 유효하다고 가정합니다. 즉 가장 강한 노드에만 연결되어 있는 노드는 모두 삭제한 그래프를 리턴합니다. 
- 이 코드가 잘 되었는지 판단하는 것은 좀 애매한데, 최소한 'shape memory effect'는 더이상 남아 있지 않습니다. 어느 정도의 키워드 필터링(특히, 분야의 일관성을 유지하기 위한) 은 되었다고 할 수 있을 것 같네요. 물론, 이를 이론적으로 증명하는 것은 좀 어려울 것 같긴 합니다만, 그래도 유사 공대생인 저에게는 이정도면 나름 유의미하다고 가정하겠습니다. 

###### problem occurred

- 아님. 'shape memory effect'가 가지로 잘려나간 것이 아니라, 가장 높은 degree centrality를 가지고 있었기 때문에 잘려나간 것임. 'superconducting magnetic energy storage' 또한 여전히 살아남아있음. 그래서 마지막에 weight degree centrality가 높아서 제외했던 node를 다시 넣어주는 것이 적합하지 않다고 볼 수 있음. 
- weight degree centrality로 제외하는 것이 아니라, 다른 centrality를 사용해서 제외하는 것이 좋을까? 예를 들어서, closeness centrality가 betweenness centrality 가 높은 놈을 제외해주는 것이 더 자연스러운 것이 되지 않을까? 
    - 어쨌든 전체 네트워크에서 전체 거리 상에서 가장 가까운 놈, 혹은 먼 놈들을 삭제해주는 것이 필요하지 않나 싶긴 한데, 현재 node가 10000개를 넘는 상황에서 closensess 를 계산해주는 것이 계산상 개 빡센게 맞음. 

- 내가 하려는 것은 결국, 'shape memory effect', 'superconduction magnetic energ storage'를 사람이 발견해서 삭제하는 것이 아니라, 네트워크 분석에 의해서 합리적으로, 혹은 일종의 클러스터링으로 다른 분야라는 것이 명확하게 갈라질 수 있도록 하는 것. 
- 그런데, 이는 결국 클러스터링으로 쓰는 것이 적합할 것 같아요. 다시 생각해보면 서로 다른 분야라면 분명히 분리가 되어야 하니까요. 그리고, weight가 작은 것을 잘라 나간다고 반드시 'shape memory effect'가 잘려나간다고 할 수 없습니다. 결과에서 저 키워드를 중심으로 한 분야가 더 도미넌트할 수도 있는 거니까요.  

```python
def make_graph_dense(i_G):
    """graph에서 degree centrality가 가장 높은 node를 삭제해도, graph는 여전히 connected여야 함
    그럴때마다 잘려나가는 node는 모두 삭제함. 
    """
    tempG = i_G.copy()
    removed_nodes = set(i_G.nodes())
    for i in range(0, 100):
        top_deg_node = max(nx.degree_centrality(tempG).items(), key=lambda k: k[1])[0]
        removed_nodes.remove(top_deg_node)# 이 node는 마지막에 다시 넣어줘야 함.
        tempG.remove_nodes_from([top_deg_node])
        if nx.is_connected(tempG)==True:
            print("after try {}: remove top degree centrality doesn't matter".format(i))
            break
        else:
            tempG = max(nx.connected_component_subgraphs(tempG), key=lambda subG: len(subG.nodes()))
    """만약 100번을 넘어도 커넥션이 유지되지 않는다면 이를 메세지로 알려주는 것이 필요한데."""
    removed_nodes.difference_update(set(tempG.nodes()))
    rG = i_G.copy()
    rG.remove_nodes_from(removed_nodes)
    """단 이렇게 변형했을때, node의 weight attribute는 그대로 유지됨. 뭐 근데 별 의미없을 수 잇지만."""
    return rG
denseG = make_graph_dense(g)
```

## use other method

- 그래서, 다시 syntactical similarity를 확인하고, 단어를 정리해준 다음, clustering을 통해 아웃라이어를 발견해보려고 합니다. 
- `difflib.SequenceMatcher`를 활용하여 단어 간의 형태적 유사도를 측정하고, `above_sim`을 넘으며 `above_node_w`를 넘는 키워드들에 대한 변환 딕셔너리를 만들어주는 함수를 정의했습니다. 

```python
def syntactical_simialrity_dict(i_Series, above_node_w=10, above_sim=0.9):
    kwd_counter = itertools.chain.from_iterable(i_Series)
    kwd_count_dct = {w:c for w, c in Counter(kwd_counter).most_common() if c >= above_node_w}
    print("for computation efficienty, cut down node got below weight, remaining node is {}".format(len(kwd_count_dct)))
    """
    """
    kwd_changed_dct = {}
    for w1 in sorted(kwd_count_dct.keys()):
        for w2 in sorted(kwd_count_dct.keys()):
            if w1 < w2 and w1[0]==w2[0] and " " in w1 and " " in w2:
                """중복을 피하고, 처음 캐릭터가 같고, 해당 단어가 복합어일 것 
                """
                sim_v = difflib.SequenceMatcher(None,w1, w2).ratio()
                if sim_v >= above_sim:
                    if kwd_count_dct[w1] >= kwd_count_dct[w2]:
                        kwd_changed_dct[w2]=w1
                    else:
                        kwd_changed_dct[w1]=w2
    def make_non_transitive(input_dct):
        print('solving transivity')
        non_transvitiy_kwd_dict = {}
        for k, v in input_dct.items():
            while v in input_dct.keys():
                v = input_dct[v]
            non_transvitiy_kwd_dict[k] = v
        return non_transvitiy_kwd_dict
    return make_non_transitive(kwd_changed_dct)
"""
변환 dictionary를 series에 적용하는 함수
"""
def transform_by_dict(i_Series, input_dct):
    print('keyword set size: {}'.format(len(set(itertools.chain.from_iterable(i_Series)))))
    r_S = i_Series.apply(lambda ks: list(set([input_dct[k] if k in input_dct.keys() else k for k in ks])))
    print('keyword set size: {}'.format(len(set(itertools.chain.from_iterable(r_S)))))
    return r_S
```

- 형태적인 분석으로도 키워드들이 많이 감소될 수 있을 줄 알고, 모든 키워드(node weight가 1인 경우까지 포함하여) 페어에 대해서 형태적인 유사도를 평가했으나, 생각보다 많이 감소되지 않았습니다. 계산시간은 30분 정도가 걸렸습니다. 겨우 1200개를 줄이자고 이런 짓을 하는 것이 의미가 있는가? 싶지만, 필요하면 해야죠...네, 아무튼 요런 형태로 형태를 변환합니다. 

```python
temp = basic_filter_Series(rawDF['Author Keywords'])
import time
start = time.time()
temp = transform_by_dict(temp, syntactical_simialrity_dict(temp, 1, 0.9))
end = time.time()
print(end-start)
```
```
for computation efficienty, cut down node got below weight, remaining node is 22883
solving transivity
keyword set size: 22883
keyword set size: 21644
1639.8741281032562
```

## 의미론적인 분석 

- 형태만으로 분석하는 것은 node weight가 1일 경우를 고려하여, 1000개 정도만 변환할 수 있습니다. 물론 이 정도도 나름 의미가 있기는 한데(이게 적합한지는 아직 체크를 못한 상황입니다), 이제 의미적으로 분석을 해볼게요. 
- adjacency matrix를 통해, 거리상으로 가까운 놈들을 확인해볼게요. 거리는 `jaccard`와 `euclidean`을 사용했습니다. discrete space라서, `jaccard`가 더 적합할 것 같기는 한데 일단은 둘다 사용해봤습니다. 

- 해봤지만, 문제가 있습니다. 
- 의미론적인 분석에서 도출해낼 수 있는 가까운 키워드 페어를 예로 들자면 'Business Process modeling'과 'process modeling' 나, 'workflow mining'와 'process mining'등을 말할 수 있습니다만, 해당 분야의 전문가가 아니라면, 해당 semantic이 유의미하게 되었는지에 대해서 의문이 드는 것이 사실입니다. 다시 말해 **그래, 얘들 간에 관계가 네트워크 구조적으로 가깝게 도출되었다는 것은 알겠는데, 그래서 '실제'로 얘네 의미가 같은가?**는 어떻게 알 수 있을까요? 요 부분이 문제가 됩니다. 결국 domain expert가 '맞다', '아니다'를 확인해주기 전까지는 이 방식만으로는 한계가 있는 것이죠. 

```python
temp = basic_filter_Series(rawDF['Author Keywords'])
temp = transform_by_dict(temp, syntactical_simialrity_dict(temp, 6, 0.9))
g = make_graph_from_series(temp)
"""node가 너무 많으면, 계산이 어려워져서 일정 이상의 weight를 가진 node만이 의미있는 node라고 가정했습니다. 
"""
g.remove_nodes_from( [n[0] for n in g.copy().nodes(data=True) if n[1]['weight']<=8] )

temp_df = pd.DataFrame(
    nx.adjacency_matrix(g).toarray(), index=[n for n in g.nodes()], columns=[n for n in g.nodes()]
)
print("the dimension of dataframe is {}".format(temp_df.shape[0]))

###

from scipy.spatial.distance import euclidean, jaccard
def make_close_pair_lst(adj_df, dist_func):
    r_lst = []
    for i in range(0, len(adj_df)-1):
        for j in range(i+1, len(adj_df)):
            r_lst.append(
                (adj_df.index[i], adj_df.index[j], dist_func(adj_df.iloc()[i], adj_df.iloc()[j]))
            )
    return sorted(r_lst, key=lambda x: x[2])
        
print("top 10 closest pair: euclidean space::")
"""euclidean distance의 경우는 표준화가 필요함. 
"""
for p in make_close_pair_lst(temp_df.apply(lambda col: (col)/(col.max())).fillna(0), euclidean)[:10]:
    print(p)
print("top 10 closest pair: jaccard space::")
for p in make_close_pair_lst(temp_df, jaccard)[:10]:
    print(p)
```

- 실제로 아래 결과도 보면, '이게 된 건가, 아니면 안된건가 모르겠어요 솔직히'. 답이 없네요. 

```
for computation efficienty, cut down node got below weight, remaining node is 1077
solving transivity
keyword set size: 22883
keyword set size: 22842
the dimension of dataframe is 639
top 10 closest pair: euclidean space::
('binary mixture', 'metallacarboranes', 0.0)
('binary mixture', 'flotation', 0.0)
('metallacarboranes', 'flotation', 0.0)
('binary mixture', 'carbapenemase', 0.0125)
('carbapenemase', 'metallacarboranes', 0.0125)
('carbapenemase', 'flotation', 0.0125)
('transient stability', 'battery', 0.29829779253058464)
('transient stability', 'carbapenemase', 0.3305048960211117)
('transient stability', 'binary mixture', 0.3307411923149668)
('transient stability', 'metallacarboranes', 0.3307411923149668)

top 10 closest pair: jaccard space::
  np.double(np.bitwise_or(u != 0, v != 0).sum()))
('exploration', 'exploitation', 0.29629629629629628)
('pecking order theory', 'trade off theory', 0.45454545454545453)
('microstructure', 'niti', 0.63636363636363635)
('transient stability', 'power quality', 0.66666666666666663)
('power quality', 'ac loss', 0.66666666666666663)
('superelasticity', 'actuator', 0.66666666666666663)
('superelasticity', 'nitinol', 0.66666666666666663)
('industrial symbiosis', 'circular economy', 0.66666666666666663)
('usability', 'requirements engineering', 0.69230769230769229)
('ahp', 'analytic hierarchy process', 0.70588235294117652)
```

- 따라서, 뭔가 마음에 들지 않습니다. structural equivalence라고 해도, 저게 맞는지 아닌지를 모르는데 제가 뭘할 수 있나요 으앙.  우리가 찾는 파랑새나 황금섬 같은 건 없어여 시파. 

## for bipartite graph 

- 뭐 일단 시작한 김에 bipartite graph를 대상으로도 한번 수행해볼게요. 
- 'Author Keywords'의 경우는 저자가 직접 입력하는 것이기 때문에, 해당 논문을 가장 잘 설명하는 키워드라고도 할 수 있지만, '주관적'일 수 있다는 한계를 가집니다. 'index keywords'의 경우는 말 그대로 색인, 검색을 하기 위한 키워드기 때문에 일관적인 분류체계에 따라서 해당 콘텐츠를 분류하기 위해 사용하는 키워드라고 할 수 있습니다. 즉, 좀 더 일관적입니다. 
- 그렇다면 'Author Keywords' ==> 'Index Keywords'인 bipartite graph를 만들고 해당 네트워크에 대해서 similarity를 계산하면 




- 그렇다면, 단순히 단편적인 구조만 보는 것이 아니라 `hierarchical clustering`과 같은 방법으로 해주는 것은 어떨까요? 분명히 우리가 원하는 'small medium sized enterprise' 이외의 분야들도 현재 포함되어 있기 때문에, 클러스터링을 통해서 이외에 속하는 부분을 싹 지워줄 수 있지 않을까, 라고 생각합니다.