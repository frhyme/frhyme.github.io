---
title: networkx의 Graph의 isomorphic를 체크해봅시다. 
category: python-libs
tags: python python-libs networkx isomorphism python-basic graph
---

## graph의 isomorphic을 체크해봅시다. 

- 아래와 같이, 두 개의 그래프가 있다고 합시다. 
- 이 둘은 노드도, edge도 모두 동일합니다. 

```python
G1 = nx.Graph()
G1.add_nodes_from([('a', {'type':1}), ('b', {'type':1}), ('c', {'type':1})])
G1.add_edges_from([('a', 'b'), ('b', 'c')])

G2 = nx.Graph()
G2.add_nodes_from([('a', {'type':1}), ('b', {'type':1}), ('c', {'type':2})])
G2.add_edges_from([('b', 'c'), ('a', 'b')])
```

- 이 두 그래프가 같은지를 확인하려면 어떻게 하면 될까요? 
- 우리가 흔히 쓰는 것처럼 `==`을 써서 처리하면 될까요? 안됩니다. 그렇게 할 경우, False를 리턴하게 되죠. 
- 물론 다른 방법이 있습니다. 

## do it. 

- `nx.isomorphic`라는 함수에 두 그래프를 넘겨주면 됩니다. 
    - 물론 이 경우에는 node, edge만 체크하게 되는데, 세부 attr까지 체크하려면, `node_match`, `edge_match`에 펑션을 넘겨주면 됩니다. 

```python
import networkx as nx

G1 = nx.Graph()
G1.add_nodes_from([('a', {'type':1}), ('b', {'type':1}), ('c', {'type':1})])
G1.add_edges_from([('a', 'b'), ('b', 'c')])

G2 = nx.Graph()
G2.add_nodes_from([('a', {'type':1}), ('b', {'type':1}), ('c', {'type':2})])
G2.add_edges_from([('b', 'c'), ('a', 'b')])

G3 = nx.Graph()
G3.add_nodes_from([('a', {'type':1}), ('b', {'type':1}), ('c', {'type':2})])
G3.add_edges_from([('b', 'c'), ('a', 'b')])

def try_convert(input_func):
    # input_func에서 exception이 발생할 때의 기능을 추가해준다. 
    # 특히, lambda 펑션과 같이 쓸때 편해짐. 
    def temp_function(*args, **kwargs):
        try:
            return input_func(*args, **kwargs)
        except:
            return False
    return temp_function

print(f"G1==G2: {G1==G2}")
# node의 attr이 다른데도 True가 출력됨.
print(f"isomorphic without attr: {nx.is_isomorphic(G1, G2)}")
# node match function은 x, y를 인풋으로 받아서, True, False를 리턴해주는 함수 
# 여기서, x, y는 각각 노드의 attr dict임. 
node_match_func = lambda x, y: True if x['type']==y['type'] else False 
node_match_func = try_convert(node_match_func)
# G1, G2의 경우 node와 edge는 같지만, node의 attr이 다름. 
print(f"isomorphic with attr: {nx.is_isomorphic(G1, G2, node_match=node_match_func)}")
# G2, G3의 경우 node와 edge, node의 attr도 같음 
print(f"isomorphic with attr: {nx.is_isomorphic(G2, G3, node_match=node_match_func)}")
```

## wrap-up

- 저의 경우 다양한 그래프를 만든 다음, 이 그래프에서 유니크한 세트만 뽑아내는 일을 수행해야 하는데, 이를 위해서는 일종의 set operation을 사용하는 것이 필요합니다. 그렇지 않고, 이를 unique한 세트로 변경하려면 n**2만큼의 계산이 필요하게 됩니다. 
- 아무튼 뭐 해야죠 뭐.