---
title: python - networkx - random partition graph
category: python-libs
tags: python python-libs networkx 
---

## networkx - random partition graph

- 요즘은 networkx에서 community detection에 대해서 정리하고 있습니다. 
- 테크닉들에 대해서 테스트를 해보려면, 클러스터가 몇 개로 구성된 예제그래프가 필요합니다. 
- 그리고, 당연히도, `networkx`에서 이러한 예제 그래프를 지원하죠.

```python
import networkx as nx 
import matplotlib.pyplot as plt

G = nx.random_partition_graph(
    sizes=[20, 10, 5], # partition 별 node 개수
    p_in = 1.0, # partition 내의 edge 비율
    p_out = 0.1, # partition 밖의 edge 비율
    directed=False, # 방향성이 있는가
    seed = 0
)
#print(G.nodes(data=True))

block_to_color_dict = {
    0:'blue', 1:'red', 2:'green'
}
node_color = [block_to_color_dict[n[1]['block']]for n in G.nodes(data=True)]
plt.figure()
nx.draw_networkx(
    G, 
    node_color=node_color, 
)
plt.savefig("test.png", dpi=100)
```

- 위와 같이 실행하면 됩니다. 어렵지 않으므로, 추가 설명은 따로 하지 않을게요.