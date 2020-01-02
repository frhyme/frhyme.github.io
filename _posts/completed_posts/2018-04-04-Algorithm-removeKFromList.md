---
title: Algorithm - removeKFromList(l, k)
category: algorithm
tags: python linked-list codefight

---

## Problem 

- linked list `l` 에 `k` 가 포함되어 있을 경우, 모든 `k`를 삭제하고 삭제된 linked list를 리턴하는 함수를 만듭니다. 

### example 

- removeKFromList([3,1,2,3], 3) ==> [1,2]

## solution

```python
def removeKFromList(l, k):
    first = l
    while first: # k 가 아닌 head를 찾기 
        if first.value==k:
            first=first.next
        else:
            break
    pr = first
    if pr==None: # linked list의 크기가 0이므로 그대로 리턴. 
        return pr
    cr = first.next # cr은 scanner라고 생각하면 좋음 
    while cr:
        if cr.value==k: # 삭제하고 앞뒤를 연결함 
            pr.next = cr.next
            cr = cr.next
        else: # 삭제할 필요 없으므로 그대로 넘어감 
            pr = cr
            cr = cr.next
    return first
```
