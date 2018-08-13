---
title: nx에서 random bipartite graph만들기 
category: python-lib
tags: networkx python python-lib bipartite random numpy 
---

## havel_hakimi_graph

- networkx에 `havel_hakimi_graph`라는 랜덤한 bipartite 그래프 생성기가 있습니다. 
- 만약 bipartite set가 각각 5개, 3개 라면, 그 크기의 각 node의 deg sequence를 넘겨주면 그 deg들에 맞는 graph를 만들어줍니다. 

- 예를 들어서 아래와 같은 코드가 있을 경우 `seq_a`, `seq_b`는 각각 node들의 degree 리스트를 말하죠. 따라서 두 리스트의 deg sum은 같아야 합니다. 
    - 추가로, 당연하지만, deg_sum은 seq_a와 seq_b의 곱보다는 작거나 같아야 합니다. 

```python
nx.bipartite.havel_hakimi_graph(
    seq_a = [1,1,1,1,1], 
    seq_b = [1,2,2]
)
```

## do it. 

- 여기서 문제는 어떤 임의의 큰 bipartite graph를 만들 때죠. 예를 들어서, 제가 bipartite set가 각각 20, 50짜리를 만든다고 해봅시다. 이럴 때 쓸 수 있는 간단한 코드를 만들었습니다. 

```python
def make_deg_seq(deg_sum, seq_a_len, max_deg):
    ## deg_sum에 맡도록 degree dist를 랜덤하게 분포함
    ## max_deg는 한 node가 가질 수 있는 최대 degree, 여기서는 multi graph가 아닌 graph로 가정 
    if deg_sum > (seq_a_len*max_deg):
        print("deg_sum is impossible")
    else: 
        seq_a = [1 for i in range(0, seq_a_len)]
        remain_seq_a = deg_sum - seq_a_len
        while remain_seq_a>0:
            idx = np.random.choice(seq_a_len)
            if seq_a[idx]+1<=max_deg:
                seq_a[idx]+=1
                remain_seq_a-=1
        return seq_a
deg_sum = 20
a, b = make_deg_seq(deg_sum, 4, 8), make_deg_seq(deg_sum, 8, 4)
# print(a, b)
newg = nx.bipartite.havel_hakimi_graph(a, b)

plt.figure(figsize=(12, 5))
nx.draw_networkx(newg, pos=bipartite_layout(newg))
plt.axis('off')
plt.savefig('../../assets/images/markdown_img/180811_random_bip_deg_seq.svg')
plt.show()
```

![](/assets/images/markdown_img/180811_random_bip_deg_seq.svg)