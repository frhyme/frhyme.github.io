---
title: Algorithm - `hasPathWithGivenSum(t, s)` 
category: algorithm
tags: python binary-tree algorithm codefight

---

## Problem

- tree `t`가 주어졌을 때, leaf로부터 root까지의 합이 s인 path가 존재하는지를 찾는 함수를 만듭니다. 

### example

- 

### Define Tree(binary)

- linked list 말고도 Tree 형태의 자료구조도 있습니다. 여기서는 우선 binary만 다루겠습니다. 
- linked list와 유사한 형태입니다, 사실 아래 코드만으로는 bidirectional linked list와 차이가 없다고 느껴지기도 하지요.  
	- binary 말고 여러 개의 child를 허용할 경우에는 아마도 `self.child=xs.copy()`의 형태로 넣어야 하지 않을까 싶습니다. deep copy하지 않으면 문제가 생길 것 같네요(아마도....먼산...)

```python
class Tree(object):
    def __init__(self, x):
        self.value = x
        self.left = None
        self.right = None
```

### dictionary to Tree

- dictionary를 Tree로 변환해주는 함수를 만들었습니다. 

```python
def DictToTree(in_dict):
    r = Tree(in_dict['value'])
    if in_dict['left'] is not None:
        if in_dict['right'] is not None:
            r.left = DictToTree(in_dict['left'])
            r.right = DictToTree(in_dict['right'])
            return r
        else:
            r.left = DictToTree(in_dict['left'])
            return r
    elif in_dict['left'] is not None:
        r.left = DictToTree(in_dict['left'])
        return r
    else:
        return r
```

## solution

1. tree의 root부터 시작합니다. 
2. root에게 왼쪽 자식 과 오른쪽 자식이 있는지를 확인합니다. 
	-  만약 있다면, 각각 재귀적으로 처리해줍니다. 
		- hasPathWithGivenSum(t.left, s-t.value)
3. 반복해서 수행하며, 어떤 경우라도 True인 것이 존재한다면, True를 리턴해주도록 합니다. 
	- 여기서는 `any`를 사용하여, 하나의 True라도 있을 경우를 고려했습니다. 

```python
def hasPathWithGivenSum(t, s):
    if t is None:
        if s==0:
            return True
        else:
            return False
    else:
        if t.left is not None and t.right is not None:
            return any([hasPathWithGivenSum(t.left, s-t.value), hasPathWithGivenSum(t.right, s-t.value)])
        elif t.left is not None:
            return hasPathWithGivenSum(t.left, s-t.value)
        elif t.right is not None:
            return hasPathWithGivenSum(t.right, s-t.value)
        else:
            if t.value==s:
                return True
            else:
                return False
```
