---
title: Algorithm - reverseNodesInKGroups(head, k)
category: algorithm
tags: python linked-list algorithm reversing codefight

---

## Problem

- linked list를 k 개만큼씩 끊고 각자 reversing하여 다시 연결해주는 함수를 말한다. 

### example

- reverseNodesInKGroups([1,2,3,4], 2) ==> [2,1,4,3]
- reverseNodesInKGroups([1,2,3,4], 3) ==> [3,2,1,4]

## solution

### split_k(head, k)

- 우선 linked list를 k 크기의 linked list와 나머지 linked list로 분할하여 리턴하는 함수를 만들었다. 

```python
def split_k(head, k):
    if head is None:
        return None, None
    cursor = head
    new_head = None
    for i in range(1, k):
        if cursor.next is None:
            return head, None
        else:
            cursor = cursor.next
    new_head = cursor.next
    cursor.next = None
    return head, new_head
```


### ReversedLinkedList(head)

```python
def ReversedLinkedList(head):
    new_head = None
    while True:
        temp = head  
        head = temp.next
        temp.next = new_head
        new_head = temp
        if head==None:
            break
    return new_head
```

### tail(head)

- 가장 끝에 있는 element를 리턴하는 함수 

```python
def tail(head):
    cursor = head
    while cursor.next:
        cursor=cursor.next
    return cursor
```

### length(l)

```python
def length(l):
    i = 0
    cursor = l 
    while cursor:
        i+=1
        cursor=cursor.next
    return i
```

### reverseNodesInKGroups(l, k)

1. split_k를 이용하여 linked list를 둘로 쪼갠다. 
2. 앞의 list의 경우 reversing.
3. 연속적으로 수행하며, 연결해준다. 

```python
def reverseNodesInKGroups(l, k):
    r_head, new_head = split_k(l, k)
    r_head = ReversedLinkedList(r_head)
    while True:
        head, new_head = split_k(new_head, k)
        if new_head is None:
            if length(head)==k:
                tail(r_head).next = ReversedLinkedList(head)
            else:
                tail(r_head).next = head
            break
        tail(r_head).next = ReversedLinkedList(head)
    return r_head
```
