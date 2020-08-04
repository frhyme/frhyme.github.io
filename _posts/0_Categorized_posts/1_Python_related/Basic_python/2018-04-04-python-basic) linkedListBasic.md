---
title: python-basic) Linked list(basic)
category: python-basic
tags: python linked-list python-basic
---

## intro

- 대학교에 입학해서 처음 C로 코딩을 할때, "array 우왕 좋아" 하면서 쓰다가, 처음 `linked list`를 만났을 때 매우 당황했던 기억이 있습니다. 특히, C로 배워서 처음 포인터를 만났을때 그 당혹감이 매우 컸었는데 계속 포인터를 써야 하니까 그 당혹감이 더 커졌었죠.
  - 물론 시간이 지나 개념이 잡히고 보니 오히려 포인터가 있는게 더 편하지만요. 
- 아무튼, 그래도 파이썬으로도 linked list를 만들어 봅니다.

## Define linked list

- 다양한 linked list를 만들 수 있습니다만, 저는 데이터 타입은 int이고, 한 방향으로 가는 linked list를 만들었습니다. 
  - 필요하다면, `self.previous=None`를 `__init__` 내부에 정의하고 매번 만들때 정의해주면 된다. 

```python
class ListNode(object):
    def __init__(self, x):
        self.value = x
        self.next = None
```

- 간단한 테스트를 해봅니다. 

```python
cr = ListNode(3)
cr.next = ListNode(4)
print(cr.value)
print(cr.next.value)
```

- 결과는 간단하죠. 

```plaintext
3
4
```

## some useful functions

### ListToLinkedList(lst)

- 보통 파이썬에서는 list를 많이 쓰고(생성하기 편하기도 하고), 테스트하려고 linkedlist를 만들어주는 것이 조금 성가셔서, list를 linked list로 변환해주는 간단한 함수를 만들었습니다. 

```python
def ListToLinkedList(lst):
    lst = iter(lst)
    first = ListNode(next(lst))
    cr = first
    for x in lst:
        cr.next = ListNode(x)
        cr = cr.next
    return first
```

### PrintLinkedList(l)

- linked list의 모든 원소를 출력해주는 함수입니다.
- 만들고 보니, 해당 함수는 앞서 정의한 ListNode의 내부 method로 정의해도 괜찮았을 것 같네요. 

```python
def PrintLinkedList(l):
    while l:
        print(l.value)
        l=l.next
```

### Return_nth(l, n)

- linked list의 n번째 원소를 출력해주는 함수 

```python
def Return_nth(l, n):
    cur = l 
    for i in range(0, n):
        cur = cur.next
    return cur
```

### length(l)

- linked list의 길이를 출력해주는 함수 

```python
def length(l):
    i = 0
    cursor = l 
    while cursor:
        i+=1
        cursor=cursor.next
    return i
```
