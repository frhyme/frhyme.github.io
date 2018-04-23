---
title: Algorithm - isTreeSymmetric(t)
category: algorithm
tags: python binary-tree algorithm codefight 

---

## Problem 

- binary tree t가 symmetric한지를 검사하는 함수입니다. 

### define binary tree

- value, left, right를 가지는 아주 간단한 객체. 

```python
class Tree(object):
    def __init__(self, x):
        self.value = x
        self.left = None
        self.right = None
```

- shallow copy를 조심하기 위해서, copy function을 몇 개 만들어줍니다. 
	- 해당 class의 내부 메소드로 만들어줘도 상관없습니다. 

```python
def copyNode(node):
    if node is None:
        return None
    else:
        new_node = Tree(node.value)
        new_node.left = node.left
        new_node.right = node.right
        return new_node

def copyTree(t):
    if t is None:
        return None
    else:
        new_node = copyNode(t)
        new_node.left = copyNode(new_node.left)
        new_node.right = copyNode(new_node.right)
        return new_node
```

- dictionary 를 tree로 만들어주는 함수, 역함수를 만들어줍니다. 
	- 꼭 필요한 건 아닙니다 하핫. 

```python
def DictToTree(input_dict):
    if input_dict==None:
        return None
    else:
        root = Tree(input_dict['value'])
        root.left = DictToTree( input_dict['left'] if 'left' in input_dict.keys() else None )
        root.right = DictToTree( input_dict['right'] if 'right' in input_dict.keys() else None )
        return root

def TreeToDict(in_t):
    if in_t==None:
        return None
    else:
        return {'value':in_t.value, 'left':TreeToDict(in_t.left), 'right':TreeToDict(in_t.right)}
```

## solution 

- binary tree t가 symmetric하려면, 
	- 우선 t.left와 t.right의 value가 같아야 하고
	- `t.left.left == t.right.right`, `t.left.right == t.right.left` 이어야 합니다. 
- 간단하게, 
	- 왼쪽 오른쪽을 바꿔주는 함수를 만들고 
	- t.left를 변환해준 다음, t.right와 같은지를 체크해주면 끝남. 
- 참 쉽죠? 

```python
def change_left_right(t):
    if t is None:
        return None
    else:
        new_root = copyNode(t)
        new_root.left = change_left_right(copyTree(t.right))
        new_root.right = change_left_right(copyTree(t.left))
        return new_root

def isTreeEqual(t1, t2):
    if t1 is None:
        if t2 is None:
            return True
        else:
            return False
    else:
        if t2 is None:
            return False
        else:
            if t1.value==t2.value:
                return isTreeEqual(t1.left, t2.left) and isTreeEqual(t1.right, t2.right)
            else:
                return False

def isTreeSymmetric(t):
    if t is None:
        return True
    else:
        return isTreeEqual(t.left, change_left_right(t.right))


```
