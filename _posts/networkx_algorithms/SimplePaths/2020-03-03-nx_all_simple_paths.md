---
title: networkx - simple paths
category: python-libs
tags: python python-libs networkx path recursion generator
---

## 1-line summary 

- `nx.all_simple_paths(G, source, target)`은 graph `G`에서 "source로부터 target까지 가지는 모든 중복없는 노드 traversal"을 리턴.

## all_simple_path. 

- graph에서 path는 중복 없는 노드 traversal을 말합니다. 특정 시작 node(source)부터 종료 node(target)까지 노드를 중복하지 않고 갈 수 있는 방법을 리턴하죠. 
- 이런 것들에 관심을 가지기 시작하면 이른바 알고리즘, 이라고 하는 것들을 생각하게 되는데요, 우리는 쉽게 그냥 반복문을 쓰지만, 반복문의 갯수가 늘어가면서 계산 시간과 메모리는 기하급수적으로 증가하게 됩니다. 그리고, graph의 경우도 마찬가지죠. 

## python implementation: bad algorithm 

- 간단하게, 다음처럼 코딩해봤습니다. source부터 target까지 갈때 발생하는 모든 branch들을 list에 박아두고 순서대로 읽어가면서 처리합니다. 사실, Graph의 크기가 작을 때는 이렇게 해도 문제가 없긴 한데, 조금만 커져도, 시간이 꽤 걸리기 시작합니다.
- 아래 코드의 문제는 branch간에 중복되는 값들이 많다는 것이죠. 가령 `[0, 1, 2, 3, 4, 5]`, `[0, 1, 2, 3, 4, 6]`이라는 두 branch가 있다고 하면, 이 둘은 마지막 원소를 제외하면 모두 동일하죠. 하지만 아래 알고리즘에서는 이 둘이 중복되지만 그대로 모두 저장하고 있습니다. 이렇게 할 경우에는 메모리가 효율적으로 관리되지 못하는 것은 물론이고, 시간도 많이 걸리게 되죠.

```python 
def all_simple_paths(G, source, target, cutoff=None):
    """
    G의 source로부터 target까지의 path(node 반복없는 길)중에서 
    길이가 cutoff 이하인 모든 path generator
    cutoff: depth, 탐색 깊이를 의미함. 
    # branches: target에 도달할 가능성이 있는 여러 길들 
    """
    if cutoff is None: 
        cutoff = len(G)
    branches = [[source]]
    while len(branches)!=0: 
        for current_brch in branches.copy():
            # 현재 branch에 대해서 끝 노드의 이웃 노드들로 탐색 
            brch_tail = current_brch[-1]
            # 이미 방문한 곳인지 탐색하고
            not_visited = set(G[brch_tail]) - set(current_brch)
            # 아직 방문할 곳이 남았으므로 찾음.
            if len(not_visited)!=0:
                for new_tail in not_visited: 
                    new_brch = current_brch + [new_tail]
                    if new_tail == target: 
                        # target에 도달했으므로 값을 리턴.
                        yield new_brch
                    else:
                        # 아직 값에 도달하지 못했으므로 새로운 브랜치를 업데이트해줌
                        # cutoff보다 큰 branch는 무시함.
                        if len(new_brch) <= cutoff: 
                            branches.append(new_brch)
            # 더이상 탐색할 곳이 남지 않았거나, 업데이트 했으므로 종료.
            branches.remove(current_brch)
```


## python implementation: better algorithm 

- python의 generator와 recursion을 사용하여 아래와 같이 간단하게 처리하였습니다. 

```python
def all_simple_paths_better(G, source, target, cutoff=None, visited=[]):
    """
    G의 source로부터 target까지의 path(node 반복없는 길)중에서 
    # branches: target에 도달할 가능성이 있는 여러 길들 
    """
    #print(f"source: {source}, target: {target}")
    new_visited = visited + [source]
    not_visited = set(G[source]) - set(new_visited)
    
    if len(not_visited)!=0:
        for nbr in not_visited: 
            if nbr == target: 
                yield new_visited + [nbr]
            else: 
                # generator를 recursion으로 다시 읽을 때는 yield from을 사용함
                yield from all_simple_paths_better(G, nbr, target, cutoff=cutoff, visited=new_visited)
```

## performance check. 

- 간단한 퍼포먼스 체크를 해봤습니다. 결과를 보시면, 기존 알고리즘보다, 더 속도 측면에서 우수한 것을 알 수 있습니다. 물론, 정말 그런지를 더 면밀하게 파악하려면 더 큰 수에 대해서도 처리해줘야 하지만 귀찮으므로 하지 않습니다 호호호.

```python
# Graph generation 
n = 150
G = nx.scale_free_graph(n=n, seed=0)
G = nx.Graph(G)
G.remove_edges_from(nx.selfloop_edges(G))

# performance check
start_time = time.time() 
nx_simple_paths = list(nx.all_simple_paths(G, 0, 1))
print(f"== nx.all_shortest_path :: {time.time() - start_time:.5f}")
start_time = time.time()
simple_paths_worse = list(all_simple_paths_worse(G, 0, 1))
print(f"== all_shortest_path worse:: {time.time() - start_time:.5f}")
start_time = time.time()
simple_paths_better = list(all_simple_paths_better(G, 0, 1))
print(f"== all_shortest_path better:: {time.time() - start_time:.5f}")

assert len(nx_simple_paths)==len(simple_paths_better)
assert len(nx_simple_paths) == len(simple_paths_worse)
```

```
== nx.all_shortest_path     :: 1.24089
== all_shortest_path worse  :: 3.09624
== all_shortest_path better :: 0.81955
```

## wrap-up

- generator와 recursion을 효과적으로 결합하여, 보아 유연하고 단순한 코드를 만들었다고 생각합니다. 
- 사실 처음에는 [networkx/algorithms/simple_paths](https://networkx.github.io/documentation/stable/_modules/networkx/algorithms/simple_paths.html#all_simple_paths) 을 이해하려고 했는데, 역시나 다른 사람의 코드를 보고 이해하는 것은 참 어려워요. 그래서 개념만 대충 이해하고, 제가 직접 러프하게 코딩을 한 다음, 가볍게 하려고 generator와 recursion을 사용하여 결합하였습니다. 하고 나니, 매우 즐거운 일이군요 호호호.


## reference

- [networkx/algorithms/simple_paths](https://networkx.github.io/documentation/stable/_modules/networkx/algorithms/simple_paths.html#all_simple_paths)
- [stakcover - recursin with generator](https://stackoverflow.com/questions/38254304/can-generators-be-recursive)