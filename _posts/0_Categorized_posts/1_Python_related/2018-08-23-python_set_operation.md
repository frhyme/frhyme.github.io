---
title: python의 set operation을 알아봅시다. 
category: python-lib
tags: python python-lib set 
---

## set가 빠릅니다. 

- 만약 해당 데이터 set이 unique하고 세트에 있는지 없는지 찾아야 하는 일이 많다면, 무조건 set로 처리하시는 것이 좋습니다. 

```python
## set operation 
import time

s = 100000000
lst_a = [i for i in range(0, s)]
iter_a = (i for i in range(0, s))
set_a = {i for i in range(0, s)}
start_time = time.time()
1000 in lst_a
print("list    : {:8.6f}".format(time.time() - start_time))
start_time = time.time()
1000 in iter_a
print("iterator: {:8.6f}".format(time.time() - start_time))
start_time = time.time()
1000 in set_a
print("set     : {:8.6f}".format(time.time() - start_time))
```

```
list    : 0.017207
iterator: 0.000481
set     : 0.000420
```

- 아무튼, python3에서 지원하는 set operation을 한번 정리하는 게 좋을 것 같아서 정리합니다. 

```python
set1 = set((i for i in range(0, 10)))
set2 = set((i for i in range(5, 15)))

print(set1.union(set2))
print(set1.intersection(set2))
print(set1.difference(set2))
print(set1.symmetric_difference(set2))
print(set1.issuperset(set1.intersection(set2)))
print(set1.issubset(set1.union(set2)))
print(set1.intersection(set2).isdisjoint(set1.symmetric_difference(set2)))
```

```
{0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14}
{5, 6, 7, 8, 9}
{0, 1, 2, 3, 4}
{0, 1, 2, 3, 4, 10, 11, 12, 13, 14}
True
True
True
```


## reference

- <https://docs.python.org/2/library/sets.html>