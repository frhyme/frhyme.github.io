---
title: sumInRange(nums, queries)
category: algorithm
tags: python algorithm codefight summation

---

## Problem

- 간단한 코드로 쓰자면 다음과같다. 다만, 현재는 계산속도가 느려서 개선하고 있는 상황. 
	- nums: int list
		- ex: [1,2,3,4,5,6]
	- queries: list of (position pair)
		- ex: [[0, 2], [2, 4]]
	- `sum(sum(nums[query[0]:query[1]+1]) for query in queries])` 
	- 또한 최종 return 값은 `10**9+7` 로 나눈 다음 리턴되어야 함. 
- codefights 300점을 달성해야 넘어가는데, 현재는 167임. 

## solution 

### first try - (score: 167/300)

- 일반적인 파이썬 코드 
	- 단, 아직 점수가 모자람

```python
def sumInRange(nums, queries):
    return sum([sum(nums[query[0]:query[1]+1]) for query in queries])%(10**9+7)
```

### second try - (score: still 167/300)

- query에 의해서 만들어지는 새로운 배열의 합을 매번 모든 원소를 더하여 계산하는 것보다는, '새로 들어오는 원소들'과 '나가는 원소들'만을 더하고 빼서 계산할 수 있지 않을까? 라고 생각하여, 다음을 수행함.
- 그러나, 스포일러를 하자면, 별 차이가 없음 휴....

1. queries를 개별 원소 내의 길이가 긴 원소부터 정렬
	- [1, 10]이 [3,4]보다 훨씬 길이가 김. 
	- 길이가 긴 원소부터 정렬해야 기존에 합한 합에서 상대적으로 적은 수의 원소만 더하고 빼서 새로운 합을 만들 수 있음
2. queries를 통해 합을 계산할 때, 이전에 계산한 partial_sum을 이용하여 포함된 원소와 포함되지 않은 원소들을 더하고 빼서 계산

```python
def sumInRange(nums, queries):
    queries = sorted(queries, key=lambda x: x[1]-x[0], reverse=True)
    queries = sorted(queries, key=lambda x: x[0])
    x, y = queries[0][0], queries[0][1]
    nums = [x%(10**9 + 7) for x in nums]
    partial_sum = sum(nums[x:y+1])
    r = partial_sum
    for qu in queries[1:]:
        new_x, new_y = qu[0], qu[1]
        if x == new_x:
            if y == new_y:
                partial_sum = partial_sum
            elif y < new_y:
                partial_sum += sum(nums[y+1:new_y+1])
            else:# new_y < y 
                partial_sum -= sum(nums[new_y+1:y+1])
        elif x < new_x:
            partial_sum -= sum(nums[x:new_x])
            if y == new_y:
                partial_sum = partial_sum
            elif y < new_y:
                partial_sum += sum(nums[y+1:new_y+1])
            else:# new_y < y 
                partial_sum -= sum(nums[new_y+1:y+1])
        else:# new_x < x
            partial_sum += sum(nums[new_x:x])
            if y == new_y:
                partial_sum = partial_sum
            elif y < new_y:
                partial_sum += sum(nums[y+1:new_y+1])
            else:# new_y < y 
                partial_sum -= sum(nums[new_y+1:y+1])
        x, y = new_x, new_y
        r+=partial_sum
    return r% (10**9+7)
```


### third try - (score: 167/300)

- 부분 리스트의 합을 구할 때, 전체를 합친 값에서 빼는 것이 빠를 수도 있고, 그냥 더하는 것이 더 빠를 수도 있으므로 이를 구분해서 계산하면 좋지 않을까? 라고 생각하지만 별 차이가 없습니다. 


```python
def sumInRange(nums, queries):
    r = 0
    l = len(nums)
    mod = 10**9+7
    nums = list(map(lambda x: x%mod if x>0 else x, nums))
    total_sum = sum(nums)
    for qu in queries:
        x, y = qu[0], qu[1]
        partial_sum = 0
        if x+(l-y) > (y-x): # from zero
            partial_sum+=sum(nums[x:y+1])
        else:
            partial_sum+= (total_sum - sum(nums[:x]+nums[y+1:]))
        r+=partial_sum
    return r%mod
```


### fourth try - (score: 167/300)

- `sum`의 횟수를 줄여볼까?, 그러나 별 차이가 없음
- 문제가 되는 테스트 케이스를 한번 체크해보기로 했다. 

```python
def sumInRange(nums, queries):
    xs = []
    for qu in queries:
        x, y = qu[0], qu[1]
        xs+=nums[x:y+1]
    return sum(xs)%(10**9+)7
```

#### test case checking

- 문제가 되는 테스트 케이스의 경우 100,000 개의 리스트 사이즈와, 299995 개의 queries를 가짐. 
- 맥북 에어에서는 상당히 많은 시간이 걸린다. 
	- 이거 하다가, 쥬피터 노트북은 한번 뻗음. 
	- 쥬피터 노트북이 계속 뻗음....아아 안돼....이거 돌릴 수도 없어 맥북에어에서는....ㅠㅠㅠㅠ
	- queries 10000개를 돌리는데, 7초가 걸림. 
- 그래서 queries를 1000개로 고정하고, 시간을 줄여 보면서 비교를 해

```python
import pandas as pd
import json

f = open(file_path, 'r').read().replace("\n", " ")
while "  " in f:
    f = f.replace(" ", "")

d = json.loads(f[1:])
nums = d['input']['nums']
queries = d['input']['queries']
print(len(nums))
print(len(queries))
```

### fifth try - (score: 167/300), but better computation. 

- 특정 구간 별 합을 기억해두고, 새로운 query의 구간을 기존에 저장해둔 특정 구간을 활용해서 도출할 수 있지 않을까?
- 따라서 특정한 구간(대략 5000개 정도)별로 값을 딕셔너리로 저장해두면, 매번 리스트를 합칠 필요없이, 빠르게 계산할 수 있지 않을까?


- 상위 쿼리 1000개만을 대상으로 했을 때, 기존 코드는 0.9초 정도 소요된 반면, 아래 코드는 0.1초 정도 소요된다. 
	- 물론 쥬피터 노트북으로 대략 계산비교한 것이지만, 너무 유의미한 차이임. 
	- 또한 step은 대략 3000 정도가 가장 빠르게 계산되는 정도임. 너무 늘리거나, 줄이면, 차이가 없음. 

```python
def sumInRange(nums, queries):
    r = 0
    l = len(nums)
    step = 3000
    if l>=step:
        r_dict = {(i+1):sum(nums[:(i+1)*step]) for i in range(0, l//step)}
        for qu in queries:
            x, y = qu[0], qu[1]
            partial_sum = 0 
            if y>=step:
                partial_sum += r_dict[y//step]
            partial_sum += sum(nums[(y//step)*step:y+1])
            if x>=step:
                partial_sum -= r_dict[x//step]
            partial_sum -= sum(nums[(x//step)*step:x])
            r+=partial_sum
        return r %(10**9+7)
    else:
        total_sum = sum(nums)
        for qu in queries:
            x, y = qu[0], qu[1]
            if (y-x) < x+(l-y):
                r += sum(nums[x:y+1])
            else:
                r += (total_sum - sum(nums[:x])- sum(nums[y+1:]))
        return r%(10**9+7)
```

### fifth try

- 그냥...간단하게, prefix sum, `y_n = sum(x[:n])` 을 가지는 새로운 리스트를 만들어서 풀었다....
	- 생각보다 너무 쉽게 풀려서 약간 당황...

```python
def sumInRange(nums, queries):
    r = 0
    numSums= [nums[0]]
    for i in range(1, len(nums)):
        numSums.append( numSums[-1] + nums[i] )
    for qu in queries:
        x, y = qu[0], qu[1]
        partial_sum = numSums[y]
        if x!=0:
            partial_sum -=numSums[x-1]
        r+=partial_sum
    return r%(10**9+7)
```





































