---
title: isListPalindrome(l)
category: algorithm
tags: python algorithm palindrome linked-list code-fight

---

## Problem

- linked list `l`이 Palindrome인가? 를 확인하는 함수 



### ReversedLinkedList(head)

- Palindrome인지를 확인하기 위해서는 Reverse하는 것이 중요하고, 이를 따로 함수로 정의하였습니다. 
	- 간단하게, linked list를 읽어들이면서, 새로 읽은 값을 연속해서 앞으로 붙여준다고 생각하면 됩니다. 
	- 설명이 참 미묘하지만, (새로 읽은 놈)의 next를 (기존에 읽어서 만든 리스트의 대가리)로 해준다 로 생각하면 좋구요
	- 만약 이 부분에서 설명이 확 와닿지 않는다면, 아마도 linked list에 대한 개념이 조금 부족한 것이 아닐까 싶습니다(제가 그랬듯이ㅠㅠㅠ)

```python
def ReversedLinkedList(head):
    new_head = None
    while head:
        temp = head  
        head = temp.next  
        temp.next = new_head
        new_head = temp
    return new_head
```


### other usefule function that used in here

- 아래는 이전에 설명한 적이 있기 때문에 따로 설명하지 않겠습니당

```python
def Return_nth(l, n):
    cur = l 
    for i in range(0, n):
        cur = cur.next
    return cur
def length(l):
    i = 0
    cursor = l 
    while cursor:
        i+=1
        cursor=cursor.next
    return i
```


## solution

1. 우선 길이를 확인하고, 해당 linked list에서 중간 point를 찾아줍니다. 
2. 중간 point부터 왼쪽 오른쪽 리스트를 각각 따로 만듭니다. 
	- 한 리스트는 reversed로 만듭니다. 
	- 만약 palindrome이라면 이 두 리스트를 순서대로 읽었을 때 모두 같아야 합니다.
3. 읽어들이면서 다르면 바로 False를 리턴하고, 끝까지 모두 같다면 True를 리턴합니다. 

```python
def isListPalindrome(l):
    l_len = length(l)
    if l_len<=1: # 길이가 1일 경우는 당연히 palindrome
        return True
    mid = Return_nth(l, l_len//2)
    mid_left = l 

    if l_len%2==0: #길이가 짝수일 경우와 홀수일 경우에, 잡아야 하는 중간 위치가 다름. 
        mid_right = mid
    else:
        mid_right = mid.next
    
    cursor = l
    while True: 
    """
    linked list를 크기가 같은 두 개의 linked list로 잘라주기 위해서, 
    중간 커서에서 next를 None으로 처리하여 linked list를 끊어줍니다. 
    """
        if cursor.next==mid:
            cursor.next=None
            break
        else:
            cursor = cursor.next
    """
    왼쪽 linked list의 head는 left_cursor
    오른쪽 linked list의 head는 right_cursor
    """
    mid_right = ReversedLinkedList(mid_right)
    left_cursor = mid_left
    right_cursor = mid_right
    while left_cursor != None or right_cursor!=None:
        if left_cursor.value != right_cursor.value:
            return False
        else:
            left_cursor = left_cursor.next
            right_cursor = right_cursor.next
            continue
    return True
```
