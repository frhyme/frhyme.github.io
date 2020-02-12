---
title: networkx - Link Analysis - HITS(Hyperlink-Induced Topic Search)
category: python-libs
tags: python python-libs networkx centrality HITS
---


## What is HITS(Hyperlink-Induced Topic Search)

- HITS(Hyperlink-Induced Topic Search)는 보통 "hubs and authoritieis"로도 알려져있는, "웹페이지를 평가하는, link 분석 알고리즘"입니다. 대부분의 네트워크, 교통망, SNS 관계, 전력 등에서 공통으로 나타나는, Hub and spoke와 유사하죠. 웹페이지 또한 "거점(hub)"이 있고, 또 이 "거점을 유지하게 하는 권위있는 사이트(authority)"가 있습니다. 

> Hubs and authorities exhibit what could be called a mutually reinforcing relationship: a good hub is a page that points to many good authorities; a good authority is a page that is pointed to by many good hubs.
- Hub와 authority는 상호보완적으로 강화하는 관계를 가지는데, 다음과 같죠.
    - `Good Hub`: "좋은 hub는 많은 높은 authority를 가진 페이지를 가리키고
    - `Good Authority`: "좋은 authority는 좋은 hub로부터 가리켜진다. 

- 이를 "웹툰"에 적용해보면, 다음의 상호보완적인 관점을 가집니다.
    - "좋은 작가(authority)를 가진 웹툰은 좋은 웹툰 서비스(hub)"
    - "좋은 서비스(hub)에 포함된 작가는 좋은 작가(authority)"
- 이를 iterative하게 반복하면 되는, 단순한 알고리즘이죠.

### Set ROOT SET first.

- 위의 내용에서는 제외되어 있으나, [HIT algorithm](https://en.wikipedia.org/wiki/HITS_algorithm)에서는 "인터넷에 존재하는 모든 페이지를 대상으로 rank를 생성하는 pagerank"와 다음과 다르게, 
    - ROOT set: "Search query"를 통해 text-based search algorithm에 의해 도출된 페이지들을 결정하고(root set)
    - BASE set: root set과 연결된 모든 페이지를 찾아서, base set를 구축하고, 
    - 이렇게 구축된, subgraph를 대상으로 HITS algorithm이 수행합니다. 
- 해당 알고리즘을 구축한, [Jon_Kleinberg](https://en.wikipedia.org/wiki/Jon_Kleinberg)는 이 이유로, "이렇게 해야하만, 충분히 의미있는 authority가 포함된다"라고 말하기도 했죠. 즉, authority가 제대로 존재하지 못하면, HITS는 실패하므로, 이것이 잘 결정되어야 한다는, 말인것 같습니다.

### Difference with Pagerank. 

- 따라서, pagerank와 다음과 같은 차이점을 가지게 되죠. 
    - query dependent: text-based search algorithm에 따라서, 어떤 root-set이 결정되었느냐에 따라 결과가 달라짐. 또한, query를 날리면 실행되기 때문에, query-time 처리 시간에 영향을 준다.
    - 보통 search engine에 잘 사용되지 않는다. 
    - 모든 page를 대상으로 하는 pagerank와 다르게, ROOT set -> BASE set -> "Focused subgraph"를 대상으로 하므로, 차이점이 있다 

## Implement HITS Algorithm by python.

- 알고리즘은 앞서 말한 바와 같이, Hub, Authority를 반복적으로 계산해 나갑니다. 코드로 쓰면 대략 다음과 같죠. 

```python 
def HITS(G):
    # initialize all authority and hub. to 1
    hub_dict  =  {u: 1.0 for u in G}
    auth_dict = {u: 1.0 for u in G}
    # iteration
    for _ in range(0, 100):
        # udpate authority: sum of its in-edge node hub
        for u in G:
            auth_dict[u] = sum([hub_dict[v] for v in G.predecessors(u)])
        # update hub: sum of its out-edge node authority
        for u in G:
            hub_dict[u] = sum([auth_dict[v] for v in G.successors(u)])
        # normalized hub dictionary
        #hub_norm = np.sqrt(np.sum([v**2 for v in hub_dict.values()]))
        hub_norm = max(hub_dict.values())
        hub_dict = {k: v/hub_norm for k, v in hub_dict.items()}
        # normalized authority dictionary
        #auth_norm = np.sqrt(np.sum([v**2 for v in auth_dict.values()]))
        auth_norm = max(auth_dict.values())
        auth_dict = {k: v / auth_norm for k, v in auth_dict.items()}
```



## reference

- [HITS_algorithm](https://en.wikipedia.org/wiki/HITS_algorithm)
- [Pagerank and HITS](https://lovit.github.io/machine%20learning/2018/04/16/pagerank_and_hits/)

## Raw code. 

```python 
import networkx as nx
import numpy as np

np.random.seed(0)

N = 10
DG = nx.scale_free_graph(N, seed=0)
DG = nx.DiGraph(DG)

assert nx.is_weakly_connected(DG) == True

def custom_HITS(G):
    # initialize all authority and hub. to 1
    hub_dict  =  {u: 1.0 for u in G}
    auth_dict = {u: 1.0 for u in G}
    max_iter = 10**2
    for _ in range(0, max_iter):
        # udpate authority: sum of its in-edge node hub
        for u in G:
            auth_dict[u] = sum([hub_dict[v] for v in G.predecessors(u)])
        # update hub: sum of its out-edge node authority
        for u in G:
            hub_dict[u] = sum([auth_dict[v] for v in G.successors(u)])
        # normalized hub dictionary
        #hub_norm = np.sqrt(np.sum([v**2 for v in hub_dict.values()]))
        hub_norm = max(hub_dict.values())
        hub_dict = {k: v/hub_norm for k, v in hub_dict.items()}
        # normalized authority dictionary
        #auth_norm = np.sqrt(np.sum([v**2 for v in auth_dict.values()]))
        auth_norm = max(auth_dict.values())
        auth_dict = {k: v / auth_norm for k, v in auth_dict.items()}
    return (hub_dict, auth_dict)

def np_normalize_dict(input_dict):
    norm = np.linalg.norm(list(input_dict.values()))
    return {k: v/norm for k, v in input_dict.items()}

#############################################
nx_hub_dict, nx_auth_dict    = nx.hits(DG)
cus_hub_dict, cus_auth_dict = custom_HITS(DG)

# normalized by np.norm
nx_hub_dict = np_normalize_dict(nx_hub_dict)
nx_auth_dict = np_normalize_dict(nx_auth_dict)
cus_hub_dict = np_normalize_dict(cus_hub_dict)
cus_auth_dict = np_normalize_dict(cus_auth_dict)

print("=="*30)
print("== nx authority, hub dictionary ")
print(nx_auth_dict)
print(nx_hub_dict)
print("--"*30)
print("== custom authority, hub dictionary ")
print(cus_auth_dict)
print(cus_hub_dict)
print("==" * 30)

```