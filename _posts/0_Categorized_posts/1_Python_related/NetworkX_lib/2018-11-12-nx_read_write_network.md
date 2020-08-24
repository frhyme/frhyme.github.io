---
title: networkx의 graph를 읽고 씁시다. 
category: python-libs
tags: python python-libs networkx format graph 
---

## intro

- `nx.Graph`를 어렵게 구축했다면, 해당 그래프를 일정한 파일 포맷으로 저장해두어야 다음에 쓰기가 편할 수 있습니다. 
- 따라서, 여기서는 graph를 어떻게 저장하고, 다시 저장한 그래프를 불러오는지를 정리합니다. 

## Graph formats

- graph를 저장하는 format은 아주 다양하게 존재합니다. 자세한 내용은 [여기에서 보시면 좋습니다].
- Adjacency list나, edge list로 저장할 수도 있지만, 이 경우에는 node, edge, graph 등의 attribute등이 제외될 수 있습니다. 
- 가능하면 다음 중에서 선택해서 사용하시면 좋아요. 
    - [GML, Graph Modelling Language](https://en.wikipedia.org/wiki/Graph_Modelling_Language)
    - [GraphML](https://en.wikipedia.org/wiki/GraphML)
    - [json](https://en.wikipedia.org/wiki/JSON)
- GML이 상대적으로 Graph를 저장하는데 범용적으로 사용되는(많은 소프트웨어에서 지원하는) modelling language이라서 괜찮습니다만, json의 경우 D3.js와 연결이 쉽다는 강점이 있습니다.
- 따라서, 결론은 아무거나 사용하세요 허허허허헛.

## reading and writing graph

### GML 

```python
nx.write_gml(G, path="g_data")
with open("g_data", 'r') as f:
    print(f.read())
print("=="*20)
G_loaded = nx.read_gml(path='g_data')
print(f"nodes: {G_loaded.nodes(data=True)}")
print(f"edges: {G_loaded.edges(data=True)}")
```

```
graph [
  node [
    id 0
    label "a"
  ]
  node [
    id 1
    label "b"
  ]
  node [
    id 2
    label "c"
  ]
  edge [
    source 0
    target 1
  ]
  edge [
    source 0
    target 2
  ]
  edge [
    source 1
    target 2
  ]
]

========================================
nodes: [('a', {}), ('b', {}), ('c', {})]
edges: [('a', 'b', {}), ('a', 'c', {}), ('b', 'c', {})]
```

### json

- GML의 경우 파일을 저장하는데 반해서, 여기서는 딕셔너리를 리턴해줍니다. 
- 따라서, 이후 `json` 라이브러리를 사용하여 추가로 저장해주어야 합니다. 

```python
import json
G_dict = nx.node_link_data(G)
G_dict_json = json.dumps(G_dict, indent=4)
print(G_dict_json)
print("=="*20)
G_loaded = nx.node_link_graph(G_dict)
print(f"nodes: {G_loaded.nodes(data=True)}")
print(f"edges: {G_loaded.edges(data=True)}")
```

```
{
    "directed": false,
    "multigraph": false,
    "graph": {},
    "nodes": [
        {
            "id": "a"
        },
        {
            "id": "b"
        },
        {
            "id": "c"
        }
    ],
    "links": [
        {
            "source": "a",
            "target": "b"
        },
        {
            "source": "a",
            "target": "c"
        },
        {
            "source": "b",
            "target": "c"
        }
    ]
}
========================================
nodes: [('a', {}), ('b', {}), ('c', {})]
edges: [('a', 'b', {}), ('a', 'c', {}), ('b', 'c', {})]
```


## wrap-up

- 저는 GML이 파일로 직접 저장을 해주니까, 더 관리하기가 편한 것 같습니다. 
- 하지만, D3.js에서 그래프 시각화를 더 잘해준다거나 한다면, 아니 그 경우에도, GML로 저장된 것을 읽어서 다시 변환해주면 되는 것 같아서, 굳이 dictionary로 변환한다음, json으로 변환해줄 필요가 있나 싶네요.