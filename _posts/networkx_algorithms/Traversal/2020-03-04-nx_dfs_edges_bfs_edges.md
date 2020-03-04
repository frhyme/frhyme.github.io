---
title: networkx - traversal - DFS, BFS
category: python-libs
tags: python python-libs networkx dfs bfs traversal generator recursion
---

## 1-line summary 

- network에 대해서 DFS(depth-first-search), BFS(Breadth-first-search)를 generator를 사용하여 구현함.

## DFS(Depth-First-Search)

- 네트워크를 깊이 중심으로 탐색하는 방법을 말합니다. 뒤에서 설명할 BFS의 경우 "너비"를 중심으로 탐색하기 때문에, source으 이웃들을 모두 탐색한 다음에야 다른 노드를 탐색하는 반면, DFS에서는 이웃의 이웃의 이웃을 다 탐색하고 난 다음에야 처음으로 돌아오죠. 
- 아래에 generator를 사용하여 간단하게 구현하였습니다. 결과는 `depth_limit`에 따라서 달라지며, 이 값은 깊이가 해당 값보다 커지면 탐색하지 않는다는 이야기죠.

```python
def dfs_edges(G, source, depth_limit=None, visited = None): 
    """
    G에서 source로부터 가능한 depth_limit에 대한 traversal
    depth_limit는 source로부터의 거리를 의미한다. 
    depth를 고정하면서 탐색
    ---- 
    visited: 방문한 node들을 업데이트해줌. recursion에서 deep copy되는 것이 아니므로 
    같은 컨테이너가 공유되므로, 다른 함수들에서도 동일하게 visited여부를 체크할 수 있음.
    not_visited_nbrs: 방문하지 않는 source의 neighbor들
    """
    if depth_limit is None: 
        depth_limit = len(G)
    if visited is None: 
        # python의 모든 것은 object이며 function 또한 마찬가지임. 
        # 즉, parameter의 초기 값을 위처럼 정하면, 함수가 처음 콜되었을 때 내부 변수로 정의됨. 
        # 따라서, 만약 다음에 같은 함수를 콜하게 되면 해당 값을 그대로 가져오게 됨. 
        # 따라서, 매번 내부에서 초기화해주는 방식이 좋음.
        visited = set()
        visited.update([source])
    not_visited_nbrs = set(G[source]) - visited
    if len(not_visited_nbrs) > 0:
        # neighbor들을 순차적으로 돌아감.
        for next_source in not_visited_nbrs: 
            if next_source not in visited: 
                # next_source에 방문하지 않았으면 방문하고 edge를 yield하고 업데이트
                yield (source, next_source)
                visited.update([next_source])
                # depth_limit가 2보다 크거나 같으면 다음 recursion 실행.
                if depth_limit >= 2: 
                    yield from dfs_edges(G, next_source, depth_limit=depth_limit-1, visited=visited)
```

## BFS(Breadth-First-Search)

- 네트워크를 너비 중심으로 탐색하는 방법을 말합니다. DFS의 경우 "깊이"를 중심으로 탐색하기 때문에, source의 이웃을 다 탐색하지 않더라도 일단 더 깊게 뻗어나갑니다. 하지만, BFS에서는 source의 이웃을 다 탐색한 다음, 이웃의 이웃으로 넘어가게 되죠. 
- 아래에 generator를 사용하여 간단하게 구현하였습니다. 

```python
def bfs_edges(G, source, depth_limit=None, visited=None):
    """
    graph G에 대해서 너비 중심으로 탐색하는 방법. 
    generator를 사용하였으며, 
    """
    if depth_limit is None: 
        depth_limit = len(G)
    if visited is None:
        visited = set()
        visited.update([source])
    not_visited_nbrs = set(G[source]) - visited
    if len(not_visited_nbrs) > 0:
        for next_source in not_visited_nbrs:
            if next_source not in visited:
                # next_source에 방문하지 않았으면 방문하고 edge를 yield하고 업데이트
                yield (source, next_source)
                visited.update([next_source])
                # depth_limit가 2보다 크거나 같으면 다음 recursion 실행.
        for next_source in list(visited):
            if depth_limit >= 2:
                yield from bfs_edges(G, next_source, depth_limit = depth_limit-1, visited=visited)
```

## wrap-up

- 저는 recursion을 사용하여 구현하였습니다. 사실 보통 recursion이 더 직관적이고 깔끔해 보이기는 하지만, network처럼 큰 규모의 데이터를 처리해야 할때는 종종 recursion의 제한 회수보다 많은 recursion이 발생할 수 있어서 문제가 될 수도 있죠. 
- 따라서 사실 가능하면 stack을 사용해서 recursion을 iteration한 형식으로 변형해주는 것이 좋습니다. 
- 추가로, tail-recursion이라고 하는 일종의 recursion을 효율적으로 처리하도록 도와주는 기법이 있는데 이 기법은 python에서는 아직 적용되지 않은 것으로 알고 있습니다. 



## reference

- [networkx.algorithms.traversal.breadth_first_search.bfs_edges](https://networkx.github.io/documentation/stable/reference/algorithms/generated/networkx.algorithms.traversal.breadth_first_search.bfs_edges.html#networkx.algorithms.traversal.breadth_first_search.bfs_edges)