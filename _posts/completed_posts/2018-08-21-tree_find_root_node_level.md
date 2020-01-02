---
title: nx.graph가 tree일 때 root, level 찾기 
category: python-lib
tags: python python-lib networkx tree 
---

## tree에서 Root 찾기 

- networkx의 `nx.Graph()`를 사용해서 tree를 만들고 관리하는데, 그때 적절한 root를 찾는 것이 중요해요. 
- 또 해당 root를 중심으로 다른 node들이 얼마나 멀리 떨어져 있는지를 파악하는 것도 중요하구요. 

- 그래서 아래에서 두 가지 함수를 만들었습니다만.....
- 생각해보니, level의 경우는 root에서의 거리를 재면 그냥 나오는 군요...왜 저렇게 짰지....

```python
nx.shortest_path_length(R_net_alt, 'R03', 'R12')
```


```python
def find_root(inputG):
    """
    tree를 입력받아서 diameter를 기준으로 중간의 node를 root로 인식합니다. 
    만약 diameter가 균등하게 나누어지지 않을 경우에는 betweenness를 중심으로 root를 찾습니다. 
    input: tree
    output: 
    """
    if nx.is_tree(inputG):
        if nx.diameter(inputG)%2==0:
            sp_lst = (nx.shortest_path(inputG, n1, n2) for n1 in inputG.nodes() for n2 in inputG.nodes)
            sp_lst = (sp for sp in sp_lst if nx.diameter(inputG)==(len(sp)-1)) 
            sp = next(sp_lst)
            return sp[len(sp)//2]
        else: ## between
            return sorted(nx.betweenness_centrality(R_net_alt).items(), key=lambda x: x[1], reverse=True)[0][0]
    else:
        print("inputG is not tree")
def find_node_level(inputG):
    ## root를 찾고 root에서부터의 거리를 레벨로 인식하고 나열함 
    """
    input: tree graph 
    output: dictionary(key: level, value: node list)
    {0: {'R06'}, 1: {'R00', 'R04', 'R05', 'R10', 'R11', 'R14', 'R19'}, 
    2: {'R02', 'R03', 'R07', 'R08', 'R13', 'R15', 'R16', 'R18'}, 
    3: {'R01', 'R09', 'R12'}, 4: {'R17'}}
    """
    r_dict = {0: {find_root(inputG)} }
    remain_node_set = {n for n in inputG.nodes()}.difference(r_dict[0])
    current_level = 1
    while len(remain_node_set)>=1:
        new_node_set = set()
        for n in r_dict[current_level-1]:
            new_node_set = new_node_set.union(set(inputG.neighbors(n)))
        new_node_set = new_node_set.intersection(remain_node_set)
        r_dict[current_level] = new_node_set
        remain_node_set = remain_node_set.difference(new_node_set)
        current_level+=1
    return r_dict
```