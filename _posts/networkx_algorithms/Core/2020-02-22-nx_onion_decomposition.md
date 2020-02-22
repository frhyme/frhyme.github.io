---
title: networkx - onion decomposition 
category: python-libs
tags: python python-libs networkx k-core degeneracy core-number k-shell
---

## 2-line summary 

- `k-shell`은 "core number를 `k`로 가지는 node들의 subgraph, 그리고, (k+1)-core에 존재하지 않는 노드들을 말하죠"
- 사실, 별거 아닌것 같은데, 종종 complex network에서 node들의 계층적인 구조를 구분할 때 사용되는 경우들이 있죠.


## onion decomposition 

- onion decomposition은 논문 [Multi-scale structure and topological anomaly detection via a new network statistic: The onion decomposition](https://www.nature.com/articles/srep31708)에서 제시된 graph decomposition 방법으로, k-core에 속하지 않는 노드들을 모두 한 layer로 합쳐 버리는 기존의 방법을 넘어서, 좀더 세부적인 layer를 제시하는 것에 가깝습니다.
- 이해를 돕기 위해서, 다음의 그림을 보시면, 사실 해당 graph에는 1-core, 2-core만이 존재하는 것으로 보이지만, 1-core에서도, degree가 작은 노드들(외곽에 있는 노드들)이 존재합니다. 
- 따라서, 이 노드들간에 서로 "차이가 존재한다"는 것을 가정하고, 다른 layer에 배치하는 것을 말하죠.

![onion decomposition example](https://media.springernature.com/lw685/springer-static/image/art%3A10.1038%2Fsrep31708/MediaObjects/41598_2016_Article_BFsrep31708_Fig1_HTML.jpg?as=webp)

### illustration 

- 조금 더 풀어서 설명하자면, 
    1) (isolate가 없다고 가정하고) 맨 처음의 graph `G`는 1-core죠(모든 노드가 최소 1의 degree를 가지니까요) 
    2) 현재 core가 1이므로, degree가 core인 1과 같거나 작은 모든 node를 잘라냅니다. 그리고 이 때 잘려나간 아이들이 첫번째 layer가 되겠죠
    3) 가장 작은 degree를 가진 애들을 잘라냈지만, 여전히 1-core입니다. 다시, 또 잘라내고 이 아이들을 두번째 layer에 배치시킵니다. 
    4) 이를 반복하다 보니, 어느새 `G`가 2-core가 되었다고 합시다. 이때부터는, degree가 2와 같거나 작은 아이들을 잘라서 layer에 배치합니다. 
    5) 또 반복하다보니, `G`가 3-core라고 합시다. 그럼 이제, degree가 3과 같거나 작은 아이들을 잘라서 새로운 layer에 배치합니다. 
    6) 더이상 G에 node가 없다면, 이를 그만둡니다.
- 대략 이렇습니다. 즉, 원래라면, 그냥 `k-crust`로 묶여서 나갈 아이들이 사실은, 그 사이에도 계층적인 구조가 있다, 라는 것을 보여준 셈이죠.

## python implementation 

- 언제나 그렇듯, 이미 `networkx`에 해당 알고리즘이 구현되어 있으나, 공부하기 위해서 직접 코딩을 했습니다. 
- 그리고 기존에 있는 `nx.onion_layers(G)`와 비교해봤는데, 같은 결과가 나오더군요.

```python
def onion_layers(G):
    """
    - `current_core`는 1부터 시작(isolate가 있을 때는 0부터)
    - `current_core`보다 degree가 작은 node들을 뽑아서 새로운 layer로 만들어줌
    - node들이 제외되면서, 남아있는 graph가 2-core가 되면, 
    이후부터는 2보다 degree가 작거나 같은 node들은 같은 layer에 배치됨.
    """
    G = G.copy()
    # onion_layer_dict: 이 함수에서 return {node: layer_number}
    onion_layer_dict = {}
    # isolate가 있으면, core는 0부터 시작함
    current_core = 0
    # layer는 1부터 시작함.
    current_layer = 1
    while True:
        # 현재의 `G`에서 가장 작은 degree가 현재의 current_core보다 크면, 값을 업데이트.
        degrees = nx.degree(G)
        min_degree = min(degrees, key=lambda x: x[1])[1]
        if min_degree > current_core:
            current_core = min_degree
        # nodes_in_this_layer:
        # 현재 `G`에서 degree가 current_core보다 작은 모든 node.
        nodes_in_this_layer = [n for n, deg in degrees if deg <= current_core]
        # 현재 layer에 속하는 node들읍 업데이트하고.
        for n in nodes_in_this_layer:
            onion_layer_dict[n] = current_layer
        G.remove_nodes_from(nodes_in_this_layer)
        # Termination: G에 더 node가 없으면 loop stop
        if len(G)==0:
            break
        else:
            current_layer+=1
    return onion_layer_dict
```


## wrap-up

- 다른 글들에서도 비슷하게 썼지만, 이 방식은 application 측면에서 좀 유용하게 쓸 수 있지 않을까, 생각해봅니다.

## reference 

- [Multi-scale structure and topological anomaly detection via a new network statistic: The onion decomposition](https://www.nature.com/articles/srep31708)
- [networkx.algorithms.core.onion_layers](https://networkx.github.io/documentation/stable/reference/algorithms/generated/networkx.algorithms.core.onion_layers.html#networkx.algorithms.core.onion_layers)