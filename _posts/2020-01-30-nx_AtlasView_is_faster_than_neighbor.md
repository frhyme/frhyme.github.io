---
title: python - networkx - `G.neighbors(n1)` is slower.
category: python-libs
tags: python python-libs networkx neighbors AtlasView
---

## Graph에서 Node간의 연결성을 확인하기 위해서는, AtlasView로 접근하는 것이 훨씬 빠르다. 

- 대상을 그래프로 관리하고 있을 때, 많이 활용하게 되는 것으로는, `node1`과 `node2`가 연결되어 있는가 연결되어 있지 않은가? 입니다. 같은 말이지만 "이 둘을 연결하는 edge가 있냐?"라는 것이죠. 
- `networkx`에서 이를 확인하는 방법은 2가지가 있는데, 그 두 가지 방법의 계산속도가 매우 큽니다. 
- 다음 코드를 보시면, 첫번째는 `G.neighbors(node_name)`으로 확인하는 경우, 두번째는 `G[node_name]`로 확인하는 경우가 있습니다. 그리고, 이 둘의 데이터 타입은 각각 `<class 'dict_keyiterator'>`와, `<class 'networkx.classes.coreviews.AtlasView'>`로 구성되어 있죠. 
    - 첫번째는 iterator의 구조로서, 하나씩 읽으면서 처리하는 방식. 
    - 그리고 두번째는 사실 뭔지 잘 모르겠지만 그냥 `Graph`에 `[]`로 접근하는 방식이죠.
- 그리고, 미리 말하지만, `G[1]`으로 접근하는 것이 `G.neighbors(1)`에 비해서 훨씬 빠릅니다.

```python
# (0, 1), (1, 2)의 edge를 가진 기본적인 Graph 생성
G = nx.Graph()
G.add_edges_from([(0, 1), (1, 2)])
####################################
# first method: `Gneighbors`
# type: <class 'dict_keyiterator'>
print(f"type: {type(G.neighbors(1))}")
print(0 in G.neighbors(1))
print(0 in G.neighbors(2))
print("--")
####################################
# second method: `G[node_name]`
# type: <class 'networkx.classes.coreviews.AtlasView'>
print(f"type: {type(G[1])}")
print(0 in G[1])
print(0 in G[2])
####################################
```

### What is `AtlasView`?

- 매우 정확하게 하나하나 알고 싶으시다면, [networkx.class.coreviews.py](https://github.com/networkx/networkx/blob/master/networkx/classes/coreviews.py)에 있는 `AtlasView`에 대한 documentation을 읽어보는 것이 도움이 됩니다. 
- 간략하게 짚고 넘어가자면, 이 아이는 다음 코드의 `from collections.abc import Mapping`이라는 아이를 Abstract Base Class로서 상속받습니다(ABC는 그냥 interface를 비슷한 유지하기 위한 일종의 규약과 같은 것이죠.). 우리는 여기서 Mapping마저도, 그냥 `dictionary`라고 생각해도 상관없습니다. 그냥 `[]`를 통해 key로 접근해오는 아이를 특정 value로 넘겨준다, 라고 해석하면 된다는 이야기죠.
- 즉, `AtlasView`는 read-only의 dictionary of dictionary입니다. 네. 그냥 **딕셔너리라고요**. 그렇게 생각해도 아무 상관이 없어요.


## Performance Comparison 

- 자, 이제 우리는 `AtlasView`는 그냥 "Graph에 대한 정보 dictionary of dictionary의 구조로 만들어서, 데이터 관리하는 자료구조"라고 생각하면 됩니다. 
- 그리고, 다음 3가지에 대해서 성능을 비교해보려고 합니다. 
    - Case 1: `n1 in G.neighbors(n2)`를 `loop_n`번 수행하는데 필요한 시간을 리턴. 
    - Case 2: `n1 in input_G[n2]`를 `loop_n`번 수행하는데 필요한 시간을 리턴. 
    - Case 3: Case2에서 사용하는 `AtlasView`가 dictionary of dictionary 구조라면, 동일한 형태로, 실제 dictionary로 node 간의 관계를 구성한 다음, 그 관계를 읽을 경우, Case 2 와 유사한 시간이 소요되어야 함(최소한 linear 증가 관계)
- 코드는 대략 다음과 같습니다.

```python
def CASE1_neighbors(input_G):
    # G.neighbors를 사용하여 연결성을 체크
    start_time = time.time()
    for _ in range(0, loop_n):
        n1, n2 = np.random.randint(0, len(input_G), 2)
        # G.neighbors(n2): <class 'dict_keyiterator'>
        # iterator로 매번 하나씩 쭉 읽으면서 처리함.
        n1_is_neighbor_of_n2 = n1 in input_G.neighbors(n2)
    return time.time() - start_time


def CASE2_Atlasview(input_G):
    # G[]를 사용하여 연결성을 체크
    start_time = time.time()
    for _ in range(0, loop_n):
        n1, n2 = np.random.randint(0, len(input_G), 2)
        # <class 'networkx.classes.coreviews.AtlasView'>
        n1_is_neighbor_of_n2 = n1 in input_G[n2]
    return time.time() - start_time


def CASE3_dict_of_dict(input_G):
    # Case2에서 사용하는 `AtlasView`가 dictionary of dictionary 구조라면, 
    # 동일한 형태로, 실제 dictionary로 node들간의 관계를 변형한다음, 접근해도 동일한 결과가 나와야함.
    G_dict_of_dict = {n1: {n2: {} for n2 in input_G[n1]} for n1 in input_G}
    start_time = time.time()
    for _ in range(0, loop_n):
        n1, n2 = np.random.randint(0, len(input_G), 2)
        # node to node 구조로 만든 딕셔너리에 접근하여 연결성을 확인함.
        n1_is_neighbor_of_n2 = n1 in G_dict_of_dict[n2]
        #print(n1_is_neighbor_of_n2)
    return time.time() - start_time
```

- 이렇게 만들어진 세 함수를 `Node size`를 변경하며(당연히 `Edge size`는 exponential하게 증가) 세 케이스간의 시간이 얼마나 차이나는지를 비교해봤습니다.


```python
import networkx as nx
import numpy as np
import time

G = nx.Graph()
np.random.seed(0)

p = 0.6 # complete graph 대비 edge의 비율
loop_n = 10**4 # 이 값을 높일수록 더 무작위로 넓은 범위의 값들에 접근하므로, 신뢰도가올라감. 

print("==" * 30)
result_dict = {}
for N in range(400, 5000, 400):
    G = nx.fast_gnp_random_graph(N, p, seed=0)
    #print(n1, n2)
    # Case 1의 시간 저장.
    CASE1_time = CASE1_neighbors(G)
    # Case 2의 시간 저장.
    CASE2_time = CASE2_Atlasview(G)
    # Case 3의 시간 저장.
    CASE3_time = CASE3_dict_of_dict(G)
    # 결과를 배수로 표현하여 출력.
    print(
        f"N: {N:4d} complete, CASE2 is {CASE1_time/CASE2_time:7.2f} times faster than CASE1"
    )
    print(
        f"N: {N:4d} complete, CASE2 is {CASE3_time/CASE2_time:7.2f} times faster than CASE3"
    )
    print("--"*20)
print("=="*30)
```

- 결과를 보면, 노드의 수가 증가할수록(edge의 수가 기하급수적으로 증가할수록) 
    - Case2(`n1 in input_G[n2]`)가 Case1(`input_G.neighbors(n2)`)에 비해 기하급수적으로 빨라짐을 알 수 있습니다.
    - 또한, 어느 정도 Node의 크기가 유지될 때는, Case2(`n1 in input_G[n2]`)과 Case3(`dictionary of dictioanry`)간의 차이가 없지만, 노드가 많아질수록, 차이가 심해지죠. 본 결과에는 넣지 않았지만, 5000개를 넘는 경우에는 가끔 Case1보다도 느려지는 경우도 있었습니다.


```
============================================================
N:  400 complete, CASE2 is    2.36 times faster than CASE1
N:  400 complete, CASE2 is    0.85 times faster than CASE3
----------------------------------------
N:  800 complete, CASE2 is    3.91 times faster than CASE1
N:  800 complete, CASE2 is    0.88 times faster than CASE3
----------------------------------------
N: 1200 complete, CASE2 is    5.49 times faster than CASE1
N: 1200 complete, CASE2 is    0.88 times faster than CASE3
----------------------------------------
N: 1600 complete, CASE2 is    7.07 times faster than CASE1
N: 1600 complete, CASE2 is    0.85 times faster than CASE3
----------------------------------------
N: 2000 complete, CASE2 is    8.72 times faster than CASE1
N: 2000 complete, CASE2 is    0.94 times faster than CASE3
----------------------------------------
N: 2400 complete, CASE2 is   10.55 times faster than CASE1
N: 2400 complete, CASE2 is    1.00 times faster than CASE3
----------------------------------------
N: 2800 complete, CASE2 is   11.94 times faster than CASE1
N: 2800 complete, CASE2 is    1.00 times faster than CASE3
----------------------------------------
N: 3200 complete, CASE2 is   11.89 times faster than CASE1
N: 3200 complete, CASE2 is    1.16 times faster than CASE3
----------------------------------------
N: 3600 complete, CASE2 is   12.65 times faster than CASE1
N: 3600 complete, CASE2 is    1.84 times faster than CASE3
----------------------------------------
N: 4000 complete, CASE2 is   16.58 times faster than CASE1
N: 4000 complete, CASE2 is    7.80 times faster than CASE3
----------------------------------------
N: 4400 complete, CASE2 is   18.90 times faster than CASE1
N: 4400 complete, CASE2 is    6.03 times faster than CASE3
----------------------------------------
N: 4800 complete, CASE2 is   18.76 times faster than CASE1
N: 4800 complete, CASE2 is   10.55 times faster than CASE3
----------------------------------------
============================================================
```


## wrap-up

- 결론적으로, 저는 `AtlasView`가 "dictionary of dictionary"라고 가정하려고 합니다. 큰 차이는 없어요. 다만, 어느 정도 크기가 커져도, 속도에서 문제가 별로 발생하지 않는데, 이것은 왜 그런지 이후에 체크해보겠습니다. 
- 뿐만 아니라, 습관적으로 저는 `G.neighbors`와 같은 method로서 정보를 접근할 때가 있는데, 가능하면 `AtlasView`의 형태로 데이터를 접근해 보려고 합니다. 그게 훨씬 더 효율적인 방식인것 같아요.