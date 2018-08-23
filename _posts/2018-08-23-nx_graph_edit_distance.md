---
title: graph의 similarity는 어떻게 계산할까요. 
category: python-lib
tags: python python-lib networkx similarity graph ntlk distance
---

## edit-distance

- "abc", "abcd"는 얼마나 비슷할까요? 혹은 정량적으로 어떻게 비슷한 정도를 측정할 수 있을까요? 
- 간단하게 두 스트링을 비교해보면 캐릭터 하나만 추가되어있는 것을 알 수 있습니다. 즉, '하나만 지우면 같아질 것 같은데?'라는 생각이 들죠. 
- edit-distance는 이렇게 한쪽에서 다른 쪽으로 갈 때 얼마나 고쳐야 같아지는지를 측정해서 그 유사도를 측정하는 방식을 말합니다. 다음 세 가지 방식중 하나가 필요할 때마다 edit-distance는 하나씩 늘어납니다. 
    - insertion: 새로운 캐릭터가 삽입되어야 할 때 
    - deletion: 캐릭터 하나를 지워야 할 때 
    - substitution: 캐릭터를 변경해야 할 때 
- 이렇게 측정할 수 있습니다. 

## for word 

- 단어에 대해서는 아래처럼 쓸 수 있어요. 간단합니다. 

```python
from nltk import edit_distance

example_word = 'abc'
target_words = ['abc', 'abcd', 'a bcd', 'lsh', 'lsha']
for w in target_words:
    print("edit distance of <{}>: {}".format(w, edit_distance("abc", w)))
```

```
edit distance of <abc>: 0
edit distance of <abcd>: 1
edit distance of <a bcd>: 2
edit distance of <lsh>: 3
edit distance of <lsha>: 4
```

## for graph 

- graph의 경우는 다행히 이미 networkx에 관련 library가 만들어져 있습니다. 그걸 사용하면 됩니다 하하핫

```python
import networkx as nx 

g1 = nx.complete_graph(["n{}".format(i) for i in range(0, 5)])
g2 = nx.complete_graph(["n{}".format(i) for i in range(0, 5)])

for i in range(0, 3):
    r_n = np.random.choice(g2.nodes())
    print("node removed: {}".format(r_n))
    print("edge removed: {}".format([e for e in g2.edges() if r_n in e]))
    g2.remove_node(r_n)
    print(nx.similarity.graph_edit_distance(g1, g2))
    print("="*50)
```

```
node removed: n2
edge removed: [('n0', 'n2'), ('n1', 'n2'), ('n2', 'n3'), ('n2', 'n4')]
5.0
==================================================
node removed: n0
edge removed: [('n0', 'n1'), ('n0', 'n3'), ('n0', 'n4')]
9.0
==================================================
node removed: n3
edge removed: [('n1', 'n3'), ('n3', 'n4')]
12.0
==================================================
```

## for tree

- graph에도 다양한 형태가 있습니다. 그중에서 tree 구조에 대해서도 당연히(graph니까) edit-distance를 그릴 수 있습니다. 
- 그런데, 이유는 아직 알아보지는 않았지만, 계산속도가 매우 느려요. 진짜 느립니다. 

- 아래와 같은 두 그래프를 비교할 때 시간이 1초가 넘게 소요됩니다. 만약 두 tree의 깊이가 훨씬 깊고 넓을 경우에는 진짜, 밤새 해도 안 끝날 때가 있어요. 

![](/assets/images/markdown_img/180823_bt_edit.svg)

```python
import matplotlib.pyplot as plt 

f, axes = plt.subplots(2, 1)
f.set_size_inches(12, 8)
g1 = nx.balanced_tree(2, 2)
g2 = nx.balanced_tree(1, 6)

nx.draw_networkx(g1, ax=axes[0]), nx.draw_networkx(g2, ax=axes[1])
plt.savefig('../../assets/images/markdown_img/180823_bt_edit.svg')
plt.show()

start_time = time.time()
print("edit distance: {}".format(nx.graph_edit_distance(g1, g2)))
print(time.time() - start_time)
```

```
edit distance: 4.0
1.444833755493164
```

- 이럴때는 좀 간소하지만 optimal하지 않은 edit-distance를 찾으면서 계산할 수도 있습니다. `nx.optimize_graph_edit_distance(g1, g2)`의 경우 연속해서 optimal edit-distance를 찾아주는 iterator를 반환해줍니다. 따라서, 연속해서 읽어들이면 결국은 `nx.graph_edit_distance(g1, g2)`와 마찬가지로 optimal edit-distance를 찾아주긴 합니다. 
- 시간이 오래 걸리므로, 간단하게 `next()`로 초기 값만 읽어서 비교하는 것도 괜찮을 수 있어요. 

```python
for i, v in enumerate(nx.optimize_graph_edit_distance(g1, g2)):
    print("{}, edit distancne: {: >4.1f}".format(i, v))
```

```
0, edit distancne: 10.0
1, edit distancne:  8.0
2, edit distancne:  6.0
3, edit distancne:  4.0
```


## wrap-up

- 앞서 작성한 바와 같이, 경우에 따라서 edit-distance가 시간이 무척 오래 걸리는 경우가 있습니다. 이유는 제가 나중에 파악해봐야 할 것 같아요. 하고 깃헙에 이슈를 날리면 좋을 것 같습니다. 
    - 다만 지금 코드를 확인해보니 매우 복잡하군요.....다음에 하기로 한다. 쿠쿠
- 또한 굳이 edit-distance에 집착할 필요도 없어요. 만약 node의 수가 제한되어 있다면, 단순히 edge간의 차집합 크기를 고려해보면 대략 비슷하게 나올 수 있으니까요. 