---
title: python-basic) member testing in python
category: python-basic
tags: python python-basic member-testing list set
---

## intro 

- 코딩할 때 빈번하게 하는 일 중 하나가 바로 "특정 자료 구조에 특정한 값이 있는지 확인"하는 것이죠. 이를 전문적인 말로 member testing 이라고 합니다.
- 매우 사소하지만, 이걸 list에 대해서 하는 경우와, set에 대해서 하는 경우는 계산 속도 측면에서 판이하게 다릅니다. 물론, list는 중복을 허용하고, set는 중복을 허용하지 않는 다는 측면에서 그 쓸모도 다르기는 하죠.

## code 

- 1,000,000 크기에 대해 10 회 수행하며 그 평균 시간을 비교하였다. 
- 다음과 같은 총 네 가지의 자료구조를 만들었다. 
  - 단, set의 경우, 1) list를 set로 변환하는데 소요되는 시간을 포함하는 경우 와 2) 포함하지 않는 경우를 나누어 계산하였다. 

```python
n = 1000000

a_set = set(range(0, n))
a_lst = list(range(0, n))
a_sorted_lst = sorted(list(range(0, n)))
d = {k:0 for k in a_lst}
```

- 시간을 계산한 코드는 간단하며, 다음과 같다. 

```python
import time
time_lst = []
for i in range(0, 10):
    start = time.time()
    k in a_set
    end = time.time()
    time_lst.append(end-start)
set_tm_without_setgen = sum(time_lst)/len(time_lst)

time_lst = []
for i in range(0, 10):
    start = time.time()
    k in set(a_lst)
    end = time.time()
    time_lst.append(end-start)
set_tm_with_setgen = sum(time_lst)/len(time_lst)

time_lst = []
for i in range(0, 10):
    start = time.time()
    k in a_lst
    end = time.time()
    time_lst.append(end-start)
lst_tm = sum(time_lst)/len(time_lst)

time_lst = []
for i in range(0, 10):
    start = time.time()
    k in sorted(a_lst)
    end = time.time()
    time_lst.append(end-start)
sorted_lst_tm = sum(time_lst)/len(time_lst)

time_lst = []
for i in range(0, 10):
    start = time.time()
    k in d.keys()
    end = time.time()
    time_lst.append(end-start)
d_k_tm = sum(time_lst)/len(time_lst)
```

- 결과를 출력해보면 다음과 같다. 

```python
print("set without set generation: {}".format(set_tm_without_setgen))
print("dictionary keys: {}".format(d_k_tm))
print("lst: {}".format(lst_tm))
print("sorted lst: {}".format(sorted_lst_tm))
print("set with set generation : {}".format(set_tm_with_setgen))
```

- 당연히 set에 대해서 member testing을 했을때가, 일단 list에 대해서 수백 배 빠른데
  - 물론 list를 set로 변환하는 시간을 고려하지 않을 경우를 말하며, 고려 했을 경우에는 훨씬 느려진다. 
  - 따라서, member testing을 자주 해야 할 경우에는 set를 활용하는 것이 좋으며, 아닐 경우에는 그냥 하자. 
- dictionary 의 keys의 경우는 set와 비슷한 시간이 걸린다. 

```plaintext
set without set generation: 4.291534423828125e-07
dictionary keys: 8.106231689453125e-07
lst: 0.0016021013259887695
sorted lst: 0.04324178695678711
set with set generation : 0.05456960201263428
```

## wrap-up

- 결론이라면, 당연히 membet testing에 대해서는 set가 list에 비해서 훨씬 빠르다.
- 다만 그렇다고 굳이 멀쩡한 list를 set로 변환한 다음 member testing할 필요는 없다. 그럼 더 느려짐.
