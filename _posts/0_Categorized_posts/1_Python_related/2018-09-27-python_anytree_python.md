---
title: python에서 tree 구조 사용하기 
category: python-libs
tags: python python-libs tree data-structure anytree mixin
---

## intro

- monte-carlo tree search를 공부해보던 중에 tree구조를 사용해볼 필요성이 생겼습니다. 물론 `networkx`를 이용해서도 비슷하게 만들 수 있지만, 이때는 find parent, find children 등에서 약간 불편함이 발생하죠. 
- `networkx`와 유사하게 어떤 것이든 data로 넣을 수 있어야 하고, parent, children 등으로 tree traversal를 쉽게할 수 있는 라이브러리를 찾다보니, [anytree](https://anytree.readthedocs.io/en/latest/)라는 것을 발견했습니다. 

- 일단은 설치부터 하시죠. 

```bash
pip install anytree
```

## anytree tutorial 

- 간단하게 tree를 만듭니다. 
- 매번 `Node` class를 만들 때마다 parent를 지정해주면 됩니다. 
- 또, 현재 tree 구조를 파악할 때, 텍스트로 출력해서 볼 수 있다는 것이 매우 편하네요. 특히 이 지점은 기본 `dictionary`와 연결해서 편하게 사용할 수 있을 것 같기도 합니다. 

```python
from anytree import Node, RenderTree

## 가능하면 아래처럼 node set list를 하나 만들어서 관리해주는 것이 편함. 
all_node_set = []

## 새로운 변수를 추가해서 넣어줘도 상관없음. 
## 단 하나의 어떤 node에 data가 있을 경우 아래 모든 노드에서도 data를 넣어주어야 함
root = Node("root", data=0)

all_node_set.append(root)

for i in range(0, 3):
    ## root.children은 기본적으로 tuple구조이며, 따라서 append등으로 새로운 값을 넣어줄 수 없음
    ## 대신 아래처럼 새로운 node를 만들고, parent를 지정해주면 알아서 연결됨 
    new_node = Node(f'child_{i}', parent=root, data=0)
    ## child가 추가되면 data를 변경하도록 세팅 
    root.data+=1
    all_node_set.append(new_node)
Node("child_child_1", parent=root.children[0], data=0)

print("=="*20)
## text상에서, tree를 예쁘게 볼 수 있음. 
for row in RenderTree(root):
    pre, fill, node = row
    print(f"{pre}{node.name}, data: {node.data}")
print("=="*20)
## 기본적인 tree method를 지원
print(f"children: { [c.name for c in root.children] }")
print(f"parent: {root.children[0].parent}")
print(f"is_root: {root.is_root}")
print(f"is_leaf: {root.is_leaf}")
## path ==> root부터 target_Node까지의 길을 말함. 
target_node = root.children[0].children[0]
print(f"path: {target_node.path}")
print(f"ancestors: {target_node.ancestors}")
print("=="*20)
```

```
========================================
root, data: 3
├── child_0, data: 0
│   └── child_child_1, data: 0
├── child_1, data: 0
└── child_2, data: 0
========================================
children: ['child_0', 'child_1', 'child_2']
parent: Node('/root', data=3)
is_root: True
is_leaf: False
path: (Node('/root', data=3), Node('/root/child_0', data=0), Node('/root/child_0/child_child_1', data=0))
ancestors: (Node('/root', data=3), Node('/root/child_0', data=0))
========================================
```

## with mixin 

- class 를 설계할 때 mixin이라는 개념이 있습니다. 아래 그림을 보시면 이해가 훨씬 빠르실 것 같은데요. 
- 아래 그림에서처럼 서로 다른 두가지 클래스를 섞어서 새로운 클래스를 만들 때, 쓰는 개념이 Mixin입니다. 

![](https://stonzeteam.github.io/assets/img/160611_interface.png)

- `anytree`에서 mixin이라는 디자인패턴을 지원하고, 이를 사용해서 그냥 Node가 아니라, 제가 만든 새로운 클래스에 집어넣을 수 있습니다. 

```python
## with node mixin

from anytree import NodeMixin, RenderTree
class MyBaseClass(object):
    pass

## MyBaseClass 대신에 object를 넣어도 상관없을 것이라고 생각했는데, 안됨. 
class MyClass(MyBaseClass, NodeMixin):
    def __init__(self, name, gender, parent=None):
        self.name=name
        self.gender=gender
        self.parent=parent## 이 부분만 유의해서 넣어주면 됨. 
    def __repr__(self):
        return self.name
        
root = MyClass(name='root', gender=None, parent=None)
mother = MyClass(name='mother', gender='female', parent=root)
brother = MyClass(name='brother', gender='male', parent=mother)
me = MyClass(name='me', gender='male', parent=mother)

for row in RenderTree(root):
    pre, fill, node = row
    print(f"{pre}{node}")
print("=="*20)
## 기존 Node에서 쓰던 method를 그대로 사용할 수 있음. 
print(f"me.ancestors: {me.ancestors}")
print(f"mother.children: {mother.children}")
```

```
root
└── mother
    ├── brother
    └── me
========================================
me.ancestors: (root, mother)
mother.children: (brother, me)
```

## wrap-up

- `networkx`에 비해서 편한 부분들이 꽤 있습니다. 
- 새로운 class를 만들어서 mixin하고, 이를 `networkx`의 graph에 node로 집어넣어서, 양쪽 메소드를 동시에 사용하면서 쓸 수 있도록 해주면 더 강력해지지 않을까? 라는 생각을 해봅니다. 

