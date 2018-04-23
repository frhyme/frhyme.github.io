# mergeTwoLinkedList(l1, l2)


## Problem

- 두 non-increasing linked list가 들어왔을 때, 이 둘을 합친 non-increasing linked list를 만드는 함수 

#### example

- mergeTwoLinkedList([0, 1, 5], [3,3,3,7]) ==> [0,1,3,3,3,5,7]

## solution 

1. linked list 각각을 읽어들이는 cursor를 두 개 만들고, 
2. 읽어들이면서 그 값이 작은 쪽을 새로 만들어진 head에 순차적으로 넣어준다.
3. 새로 만들어진 linked list의 head를 리턴한다. 

```python
def mergeTwoLinkedLists(l1, l2):
    head = None
    r_cur = None
    lc = l1
    rc = l2
    newVal = None
    while True:
        if lc is not None:
            if rc is not None:# both not none
                if lc.value < rc.value:
                    newVal = lc.value
                    lc = lc.next
                else:
                    newVal = rc.value
                    rc = rc.next
            else:#only l2 none
                newVal = lc.value
                lc = lc.next
        else:#l1 None
            if rc is not None:
                newVal = rc.value
                rc = rc.next
            else:
                return head
        if head is None:
            head = ListNode(newVal)
            r_cur = head
        else:
            r_cur.next = ListNode(newVal)
            r_cur = r_cur.next
```
