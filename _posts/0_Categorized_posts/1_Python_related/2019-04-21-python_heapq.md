---
title: heap 을 사용해봅시다. 
category: data-structure
tags: python python-libs data-struture heap
---

## heap을 사용해봅시다. 

- 요즘 심심할때 간단한 코딩 문제를 푸는데, 간단한 자료구조가 나옵니다. 이른바 heap이라는 것이죠. 
- complete binary graph(대충, children이 두개 씩만 있어야 하고, 음, 대충 꽉 채워진 그래프입니다 설명하기 귀찮네효 하하하)이고, max, min heap으로 나뉠 수 있는데 각각 parent가 children보다 항상 크거나, 항상 작거나의 조건을 만족해야 합니다. 
- 아무튼, 이걸 이용하면 우리가 흔히 사용하는 list를 효율적으로 사용할 수 있습니다. 말이 이상하네요. 
- 정리하자면. 
    - 힙을 사용하면, 가장 큰 값, 가장 작은 값등을 기존 방식들보다 효율적으로 뽑아낼 수 있습니다. 
    - 따라서, 정렬 등 다양한 방식에서 편하게 사용할 수 있습니다. 하하. 
    - 또한 그래프의 형태로 관리되어야 하나? 생각할 수 있지만, 기존 array를 그대로 사용할 수 있습니다. complete binary graph tree이므로, 그대로 사용해도 상관없ㅅ브니다. 하하.


## do it with library. 

- 당연하지만, python에서 기본적으로 제공하는 heap이 있습니다. 기본적은 아니고, 라이브러리가 있는 것이죠. 
- 간단하게, `heappush`와 `heappop`만 알면 됩니다. 알아서 계속 heap을 유지하면서 진행하게 해주죠. 

```python
from heapq import heappush, heappop

a = [4,5,6,2,7,9]
a = [x for x in a]
heap = []
for x in a:
    heappush(heap, x)
print(heap)
print(type(heap))
```

## do it alone

- 하지만, 직접 한번 짜보기로 합니다. 
- 사실, 해당 리스트를 heap의 형태로 변환해주는 `heapify`라는 것만 잘 사용하면 됩니다. 
    - 그 외의 push, pop는 결국 리스트에 값을 추가한다음 `heapify`하는 것 뿐이니까요. 

```python
def partial_heapify(unsorted_lst, root_index, max_or_min="max"):
    """
    - 정렬되지 않은 리스트를 받고, 
    - 부모 노드의 리스에서의 인덱스를 받고, 
    - heap의 크기, 즉, unsorted_lst의 크기를 받아서, 
    - unsorted_lst를 heap으로 변경해서 리턴해주는 함수 
    """
    # max heap인지, min heap인지에 따라서 값 비교 함수가 달라짐. 
    if max_or_min=="max":
        cmp = lambda x, y: True if x>y else False
    else:
        cmp = lambda x, y: True if x<y else False
    largest_index = root_index
    left_child_index, right_child_index = 2*root_index+1, 2*root_index+2
    if left_child_index < len(unsorted_lst):
        if cmp(unsorted_lst[left_child_index], unsorted_lst[largest_index]):
            largest_index = left_child_index
    if right_child_index < len(unsorted_lst):
        if cmp(unsorted_lst[right_child_index], unsorted_lst[largest_index]):
            largest_index = right_child_index
    if largest_index != root_index:
        print("unsorted_lst(before): ", unsorted_lst)
        unsorted_lst[largest_index], unsorted_lst[root_index] = unsorted_lst[root_index], unsorted_lst[largest_index]
        print("unsorted_lst(after):  ", unsorted_lst)
        print("root_index: ", root_index)
        print("="*30)
        partial_heapify(unsorted_lst, largest_index, max_or_min=max_or_min)
def heapify(unsorted_lst, min_or_max="max"):
    """
    - unsorted_lst를 heap으로 변경하고, 리턴. 
    """
    r_lst = unsorted_lst.copy()
    for i in range(len(r_lst)//2, -1, -1):
        partial_heapify(r_lst, i, min_or_max)
    return r_lst
a = [1,2,3,4,5,6,7, 1, 9, 25]
b = heapify(a, "max")

```

- 실행 결과는 다음과 같습니다. 

```
unsorted_lst(before):  [1, 2, 3, 4, 5, 6, 7, 1, 9, 25]
unsorted_lst(after):   [1, 2, 3, 4, 25, 6, 7, 1, 9, 5]
root_index:  4
==============================
unsorted_lst(before):  [1, 2, 3, 4, 25, 6, 7, 1, 9, 5]
unsorted_lst(after):   [1, 2, 3, 9, 25, 6, 7, 1, 4, 5]
root_index:  3
==============================
unsorted_lst(before):  [1, 2, 3, 9, 25, 6, 7, 1, 4, 5]
unsorted_lst(after):   [1, 2, 7, 9, 25, 6, 3, 1, 4, 5]
root_index:  2
==============================
unsorted_lst(before):  [1, 2, 7, 9, 25, 6, 3, 1, 4, 5]
unsorted_lst(after):   [1, 25, 7, 9, 2, 6, 3, 1, 4, 5]
root_index:  1
==============================
unsorted_lst(before):  [1, 25, 7, 9, 2, 6, 3, 1, 4, 5]
unsorted_lst(after):   [1, 25, 7, 9, 5, 6, 3, 1, 4, 2]
root_index:  4
==============================
unsorted_lst(before):  [1, 25, 7, 9, 5, 6, 3, 1, 4, 2]
unsorted_lst(after):   [25, 1, 7, 9, 5, 6, 3, 1, 4, 2]
root_index:  0
==============================
unsorted_lst(before):  [25, 1, 7, 9, 5, 6, 3, 1, 4, 2]
unsorted_lst(after):   [25, 9, 7, 1, 5, 6, 3, 1, 4, 2]
root_index:  1
==============================
unsorted_lst(before):  [25, 9, 7, 1, 5, 6, 3, 1, 4, 2]
unsorted_lst(after):   [25, 9, 7, 4, 5, 6, 3, 1, 1, 2]
root_index:  3
==============================
```

## wrap-up

- 자료구조인 heap을 만들어봤씁니다. 
- 사실, 다양한 자료구조를 잘 다루는 것이, 프로그램을 효율적으로 구성하는 기본인데, 매번 남이 만들어준 라이브러리를 사용하다보니, 이제 이런 간단한 것도 시간이 오래 걸리는 것 같아요. 문제입니다 문제 하하.

## reference

- <https://ratsgo.github.io/data%20structure&algorithm/2017/09/27/heapsort/>