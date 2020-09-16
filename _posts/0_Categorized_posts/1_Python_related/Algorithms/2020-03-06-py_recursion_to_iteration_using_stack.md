---
title: stack을 이용해서 recursion을 iteration으로 바꾸기.
category: python-basic
tags: python python-basic stack recursion data-structure
---

## 1-line summary

- stack을 이용해서 recursion DFS를 iteration으로 변경해봄.

## Recursion

- 프로그래머의 성향에 따라서 다를 수 있지만, recursion이라는 직관적으로 문제를 풀 수 있는 방법을 알려줍니다. 뿐만 아니라, 해당 기법은 `for`를 이용한 iteration보다 훨씬 이해가 쉽다는 장점이 있죠. 사실, 저는 "가독성이 매우 뛰어나다"라는 측면에서 recursion의 중요성을 이해합니다. 
- 하지만, recursion의 경우는 함수에서 또 다른 함수를 반복적으로 call을 하기 때문에, 현재의 함수 call이 어떤 함수로부터 발생한 것인지를 다 기억해야 한다는 한계가 있죠. 간단하게 아래와 같은 `factorial(n)`이 있다고 합시다. `factorial(10)`을 call하면, "10에서 9를 불렀고, 9에서 8을 불렀고, 이 과정을 다 컴퓨터가 기억해놓아야 합니다". 그래야 이후에 다 합쳐서 문제없이 해결할 수 있을 테니까요. 
- 이를 해결하기 위해서, recursion call을 함수의 맨 끝에만 위치시킴으로써 효율적으로 해결하는 tail-recursion이라는 기법도 있습니다. 이 기법은 함수 끝에서 recursion call을 하게 되므로, 이전의 함수를 기억할 필요가 없다는 장점이 있죠. 하지만, 이것이 가능하려면 해당 언어에서 tail-recursion optimization이라는 것을 지원해야 합니다만, python에서는 지원하지 않아요.

```python
def factorial(n): 
    if n==1:
        return 1
    else:
        return n*factorial(n-1)
```

- 아무튼, 뭐 웬만한 개발에서는 recursion을 그냥 써도 됩니다만, 아래 코드를 보시면, 제 컴퓨터에서는 recursion이 1000개만 되어도, maximum recursion depth를 초과하는 문제가 발생합니다. 물론 `sys.setrecursionlimit`를 사용해서 최대 recursion을 조정할 수 있지만, 저는 하지 않겠습니다. 잘못 건드리면 스택오버플로우가 발생하거든요.
- 또한, 사실 아래 문제의 경우는 iteration으로 바꾸는 게 워낙 쉽기도 하죠. 그냥 바꾸는 것이 쉽습니다.

```python
import networkx as nx
import sys

def factorial_recursive(n): 
    if n==1:
        return 1
    else: 
        return n*factorial_recursive(n-1)

def factorial_iteration(n): 
    r = 1
    for i in range(n, 0, -1):
        r = r*i
    return r

assert factorial_recursive(10) == factorial_iteration(10)
try: 
    recursion_limit = sys.getrecursionlimit()
    print(f"recursion limit: {recursion_limit}")
    factorial_recursive(recursion_limit)
except Exception as error_code:
    # 하지만, recursion은 수행 횟수에 제한이 있어서, 효과적이지 못할 때가 있음.
    print("Exception: ",error_code)
print("=="*30)
```

```plaintext
recursion limit: 1000
Exception:  maximum recursion depth exceeded in comparison
============================================================
```

## Depth first search(DFS) problem

- graph를 Depth-first search로 풀 때, recursive, iterative하게 풀었습니다. 
- recursion을 iterative하게 풀 때 중요한 것은 "각 recursion에서 필요로 하는 것이 어떤 값들(argument)인가?"죠.

### Graph DFS traversal: recursion

- factorial과 같은 문제는 recursion을 iteration으로 변경하는 것이 쉽습니다만, graph나 tree처럼 조금 복잡하게 recursion이 걸리는 경우에는 변경하는 것이 약간 어렵습니다. 그래도, 우선은 그냥 recursion으로 풀어보죠. 
- 저는 간단하게, graph `G`에서 source로부터 출발하여 모든 node를 DFS로 탐색하는, 간단한 함수를 만들었습니다. 

```python
import networkx as nx

def dfs_recursive(G, source, visited=set()): 
    """
    G: nx.Graph
    source: DFS로 탐색할 때 첫번째 노드
    visited: 방문한 node들의 set, 모든 recursion에서 같은 객체를 공유함.
    """
    if len(visited)==len(G):
        # visited와 G의 크기가 같으면 모든 노드를 방문했다는 말이므로, 빈 edge를 리턴함.
        return []
    else: 
        # source를 방문했으므로 visited에 업데이트하고.
        visited.add(source)
        # source로부터 visited를 방문하지 않고 탐색하는 edge
        edges = []
        for nbr in (set(G[source]) - visited):
            # 현재 source의 neighbor중에서 visited에 포함되지 않는 노드 nbr에 대해서 
            # 매번 nbr이 visited에 추가되지 않았는지 확인하고
            if nbr not in visited: 
                # 추가할 수 있는 경우 다음 edge를 추가해주고, recursion을 수행함.
                edges.append((source, nbr))
                edges += dfs_recursive(G, nbr, visited=visited)
        return edges
```

### Graph DFS traversal: iteration 

- 앞서 말한 것처럼 recursion으로 풀 경우 python에서 graph의 크기가 충분히 커졌을 때, 문제가 생길 수 있습니다. 따라서, 이럴 때는 stack을 이용해서 iteration으로 풀어주는 것이 좋죠.
- 방법이야 여러 가지가 있게지만, 저는 `stack`을 이용해서 recursion을 call하는 함수와, call되는 함수를 매번 state로 기억해두기로 했습니다. 즉, call stack처럼 만들어준 것이죠.
- recursion을 iteration으로 변경할 때 신경써야 하는 것은 "각 recursion마다 필요로 하는 argument들이 무엇이고, 그 상태를 어떻게 저장해야 하는가?"입니다. 사실, 정작 만들고 나니까, 생각보다 간단해서 놀랐습니다.
- 아래 iteration에서도 `state_stack`이라는 리스트에, 각 recursion마다 필요한 argument 값을 저장해두고 마치 recursion과 유사하게 돌아가는 것이죠.

```python
def dfs_iterative(G, source): 
    # shared contain in all recursion call. 
    edges = []
    visited = set([source])
    # state_stack: 어떤 recurstion이 어떤 recursion을 콜했는지, argument에 대해서 저장해둠
    # parent => child recursion을 포함한 recursion의 argument
    # child => parent child recurtion에서 새롭게 콜하는 recurion의 argument
    # 즉, 아래에서 source가 argument이 recursion들에서는 다시 nbr의 argument에 대해서 
    # 새롭게 recursion을 call하게 됩니다. 이러한 구조를 stack에 저장해주는 것이죠.
    state_stack = [{'parent': source, 'child': nbr} for nbr in G[source]]

    while True: 
        # state_stack이 비어 있다는 것은 더이상 실행할 recursion이 없다는 것. 
        if len(state_stack)==0:
            return edges
        else:
            # 새로운 state를 끝에서 가져옴.
            cur_state = state_stack.pop()
            from_n, to_n = cur_state['parent'], cur_state['child']
            if to_n not in visited: 
                visited.add(to_n)
                edges.append((from_n, to_n))
                # Update New states: 새로운 state를 update해줌
                for nbr in G[to_n]: 
                    if nbr not in visited: 
                        state_stack.append({'parent': to_n, 'child': nbr})
```

## wrap-up

- 사실, recursion을 stack을 이용해서 간단하게 iteration의 형태로 변경해봤지만, 사실 모든 recursion이 이렇게 쉽게 변형되는 것은 아닙니다. 꽤 복잡한 경우도 매우 많죠. 
- 하지만, 그래도, 대부분의 경우 stack은 이용한다는 것, recursion이 돌아가는 방식이 결국은 가장 최근에 발생한 놈을 다시 사용한다는, stack과 유사한 LIFO의 방식을 사용한다는 것만 정확하게 기억해두시는 것이 좋겠네요.

## reference

- [way to go from recursion to iteration](https://stackoverflow.com/questions/159590/way-to-go-from-recursion-to-iteration)
