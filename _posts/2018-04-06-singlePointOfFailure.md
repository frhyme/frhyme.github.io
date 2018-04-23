# singlePointOfFailure(connections)

## Problem 

- `connections` 는 2 dimensional array로, `connections[i][j]`가 1이면, node `i` `j` 가 연결되어 있음을 의미한다(o/w 0)
- connections를 이용하여 네트워크를 그릴 수 있으며, 입력받은 connections의 경우 모든 노드가 연결되어 있다. 
- 이 때 특정한 edge를 하나 자르면, 해당 네트워크에서 모든 노드 간에 연결되는 것이 아니고, 어떤 노드들의 경우 연결성이 끊어진다. 
- 그림으로 설명하면 좋은데, 예를 들어, 0-1-2-3-4 의 네트워크라면, 이 사이의 어떤 edge를 끊어도 네트워크 전체의 연결성은 끊어지게 된다. 
	- 해당 edge가 전체 네트워크의 유동성에 가장 중요한 역할을 가진 edge라고 표현할 수도 있다. 

## solution

- node i, j 에 대해서, 서로 직접 연결되어 있으며 또 다른 path가 없는 경우를 모두 카운트해주면 된다. 
- 처음에는 다른 방식으로 풀었으나(왠지 graph 문제니까, bright한 방법이 있지 않을까? 하고 고민하다가 실패함) 결국 tree search(BFS) 형태로 돌아옴. 
- graph를 모델링하는 다양한 방법이 있을 수 있다. linked list도 가능하지만, 여기서는 간단하게 딕셔너리로 구현하였다. 
- `IsConnectedTwice(i, j)`는 내부 함수로, 두 node 간에 연결되어 있는 방법이 두 번인지를 True/False로 리턴해준다. 

```python
def singlePointOfFailure(connections):
    con_d = {}
    for i, row in enumerate(connections):
        con_d[i]=[]
        for j, elem in enumerate(row):
            if elem==1:
                con_d[i].append(j)
    def IsConnectedTwice(i, j):
        if j in con_d[i]:
            # count 1
            visited = set([j])
            cur_nodes = set(con_d[j]).difference(visited)
            cur_nodes = set(con_d[j]).difference([i])
            while True:
                l = len(visited)
                for c in cur_nodes:
                    visited.add(c)
                if i in visited:
                    return True
                if l==len(visited):
                    return False
                temp_nodes = set()
                for k in cur_nodes:
                    temp_nodes.update(con_d[k])
                cur_nodes = temp_nodes.difference(visited)
        else:
            return False
    r = 0 
    for i in range(0, len(connections)):
        for j in range(i+1, len(connections)):
            #print("{}, {} : {}".format(i, j, IsConnectedTwice(i, j)))
            if IsConnectedTwice(i, j)==False and connections[i][j]==1:
                r+=1
    return r
```


## drawing graph

- connections을 매트릭스로만 보는 것보다, 그림으로 직접 그려봐야, 지금 내가 잘하고 있는지를 확인할 수 있는데, 간단하게 그림을 그릴 수 있는 코드를 첨부하였다. 

```python
import networkx as nx
import matplotlib.pyplot as plt 

def draw_connections(connections):
    g = nx.Graph()
    for i in range(0, len(connections)):
        for j in range(0, len(connections)):
            if connections[i][j]==1:
                g.add_edge(i, j)
    nx.draw_networkx(g)
    plt.show()
draw_connections(connections)
```
