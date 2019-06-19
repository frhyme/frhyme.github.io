---
title: Graph에서 랜덤 워크 생성하기. 
category: python-libs
tags: python python-libs graph networkx random-walk node2vec
---

## random walk generation 

- random walk라 함은, 말 그대로 무작위로 이리저리 움직이는 것을 말합니다. 이걸 그래프에서 이야기하자면, 주어진 그래프에서 정의한 노드와 엣지의 특성에 맞춰서 이런저런 시퀀스를 만드는 것을 일종의 random walk라고 할 수 있죠. 뭐 표현에 따라서 sequence sampling이라고 할 수도 있겠네요. 
- 아무튼, 뜬금없이 graph로부터 sequence를 도출하는 이유는 노드투벡을 사용하다가 제가 원하는 대로 학습이 잘 안 되어서죠. 저는 [node2vec github repo](https://github.com/eliorc/node2vec)에서 다른 사람이 이미 만들어놓은 라이브러리를 가지고 사용했습니다. 그러나, 이 과정에서 만들어지는 시퀀스를 보니까, 다음과 같은 문제점들이 있었습니다. 
    - edge의 weight를 고려하여 traversal하지 않는다. 
    - `p`, `q`의 하이퍼 파라미터를 활용하여 시퀀스릐 traversal를 조절하는데, return parameter가 내 의도만큼 민감하게 움직이지 않는다. 
    - random.seed를 고정시킬 수 없다. 파라미터 튜닝을 하거나 알고리즘을 변경하면서 잘 되고 있는지를 알기 위해서는 무작위성을 어느정도 고정하고 수행해야 합니다. 그러나, 해당 라이브러리는 그게 안되서, 문제가 발생하고 있죠. 
- 사실, node2vec은 그래프로부터 샘플링하는 방법만 추가되었을 뿐이지, word2vec에서의 학습방법과 유사합니다. 즉, 제가 개인적으로 그래프로부터 시퀀스를 샘플링하는 방법을 만들고, word2vec을 사용해도 된다는 이야기죠. 
- 따라서, 그냥 직접 만들어봤습니다. 

## do it

- 코드는 다음과 같습니다. 


```python
import networkx as nx
import numpy as np 
np.random.seed(10)
"""
- G로부터 random walk를 생성함. 
"""
G = nx.Graph()
G.add_edges_from([
    ('a', 'b', {'weight':1}), ('b', 'c'), ('a', 'c'), 
    ('c', 'x'), 
    ('x', 'y'), ('y', 'z', {'weight':1}), ('x', 'z')
])
def make_random_walk_from_G(input_G, NUM_WALKS=10, WALK_LENGTH=5, RETURN_PARAMS = 0.0 ):
    """
    - G로부터 무작위의 랜덤 워크를 만든다. 
    - 기본적으로 weight를 고려하며, edge의 weight가 클수록 해당 edge를 많이 지나가도록 선택된다. 
    - 맨 처음 선택되는 시작 노드 또한, node의 weight에 따라서 선택된다. 
        - 사실 degree centrality등 다양한 뱡식으로 선택해서 처리할 수 있지만, 일단은 그냥 무작위.
    - RETURN_Param: 이전의 노드 시퀀스가 ('a', 'b')였고, 지금이 'b'인 상태에서 다음 스텝을 선택할 때, 'a'로 돌아갈 확률을 의미함. 
        - 예를 들어서, RETURN_Param가 0.3이라면, 'a'로 돌아갈 확률이 0.3이고, 나머지가 0.7에서 선택되는 것임. 
        - 다만 여기서, 나머지가 없다면(terminal node라면) 무조건 원래대로 돌아가게 되는 것이고. 
    """
    def find_next_node(input_G, previous_node, current_node, RETURN_PARAMS):
        """
        input_G의 current_node에서 weight를 고려하여 다음 노드를 선택함. 
        - 이 과정에서 RETURN_params를 고려함. 
        - 이 값은 previous_node로 돌아가는가 돌아가지 않는가를 정하게 됨. 
        """
        select_probabilities = {}
        for node in input_G.neighbors(current_node):
            try: # 'weight'가 attrdict에 있을 때 
                select_probabilities[node] = input_G[current_node][node]['weight']
            except:# 'weight'가 attrdict에 없을 때 
                select_probabilities[node] = 1
        if previous_node is not None:
            del select_probabilities[previous_node] # 이 노드는 RETURN_PARAMS에 의해 결정됨. 
        else:# RETURN이 없으므로 이 값도 0으로 변경해줌. 
            RETURN_PARAMS = 0.0
        select_probabilities_sum = sum(select_probabilities.values())
        select_probabilities = {k: v/select_probabilities_sum*(1-RETURN_PARAMS) for k, v in select_probabilities.items()}
        if previous_node is not None:
            select_probabilities[previous_node]=RETURN_PARAMS # 이 노드는 RETURN_PARAMS에 의해 결정됨. 
        #print(select_probabilities)
        selected_node = np.random.choice(
            a=[k for k in select_probabilities.keys()],
            p=[v for v in select_probabilities.values()]
        )
        return selected_node
    ####################################
    path_lst = []
    for i in range(0, NUM_WALKS):
        path = [np.random.choice(input_G.nodes())] # start node 
        # 처음에는 previous node가 없으므로, None으로 세팅하고 진행함. 
        next_node = find_next_node(G, None, path[-1], RETURN_PARAMS)
        path.append(next_node)
        # 이미 2 노드가 나왔으므로 그만큼 제외하고 새로운 노드를 찾고 넣어줌. 
        for j in range(2, WALK_LENGTH):
            next_node = find_next_node(G, path[-2], path[-1], RETURN_PARAMS)
            path.append(next_node)
        # 새로운 패스가 만들어졌으므로 넣어줌.
        path_lst.append(path)
    return path_lst
make_random_walk_from_G(G, 10, 10, 0.0)
```

- 실행 결과는 다음과 같습니다. 저는 `RETURN_PARAMS`를 0으로 세팅했기 때문에, 이전에 방문했던 노드에는 절대 가지않고, 'b', 'a', 'c'가 반복되는 것을 알 수 있습니다. 

```
[['b', 'a', 'c', 'b', 'a', 'c', 'b', 'a', 'c', 'b'],
 ['y', 'z', 'x', 'c', 'a', 'b', 'c', 'x', 'z', 'y'],
 ['z', 'x', 'c', 'b', 'a', 'c', 'b', 'a', 'c', 'x'],
 ['z', 'x', 'c', 'a', 'b', 'c', 'a', 'b', 'c', 'x'],
 ['x', 'c', 'a', 'b', 'c', 'x', 'y', 'z', 'x', 'y'],
 ['z', 'y', 'x', 'c', 'a', 'b', 'c', 'x', 'z', 'y'],
 ['y', 'x', 'c', 'b', 'a', 'c', 'b', 'a', 'c', 'b'],
 ['y', 'x', 'z', 'y', 'x', 'c', 'a', 'b', 'c', 'x'],
 ['b', 'c', 'a', 'b', 'c', 'a', 'b', 'c', 'x', 'y'],
 ['a', 'b', 'c', 'x', 'y', 'z', 'x', 'y', 'z', 'x']]
```

## wrap-up

- 그래프는 다양한 특성을 가지고 있고, 제가 그래프로부터 시퀀스를 가져올 때, 어떤 부분을 중심으로 볼 지가 중요합니다. node2vec에서도 비슷한 내용이 나오지만, BFS처럼 넓게 탐색을 할 것인가, 혹은 DFS처럼 깊게 탐색을 할 것인가에 따라서, 해당 그래프로부터 뽑아내는 특성이 달라지죠. 
- 이는 결국, 제가 해당 그래프에서 시퀀스를 어떠한 방법으로 뽑아내느냐에 따라서, 그 결과가 달라진다는 것을 의미합니다. 