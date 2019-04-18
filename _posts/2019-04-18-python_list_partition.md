---
title: list의 k partition 구하기. 
category: others
tags: python python-libs partition
---

## 리스트로부터 k개의 partition을 구합니다. 

- 예를 들어서, 다음과 같은 리스트가 있다고 합시다. 
    - 아래 리스트를 2로 쪼갠다면, 다음과 같은 3 가지 방법이 있죠. 
        - (ab, c), (ac, b), (bc, a)

```python
a = ['a', 'b', 'c']
```

- 이렇게 k개수만큼 분할할 수 있는 모든 리스트를 리턴하는 함수를 만들어 봤습니다. 
- 물론 찾아보면, 훨씬 최적화된 방법이 많지만, 저는 그냥 마구잡이로 구햇씁니다. 그래서인지 이해는 쉬워요 하하하.

## do it. 

- 우선, k개 이하의 파티션으로 나눌 수 있는 모든 partition을 구합니다. 
    - 리커시브로 만들었고, k개만큼의 리스트에 새로운 요소를 넣어주면서 진행한다고 생각해주시면 됩니다. 
- 그 결과로 k개 이하의 모든 경우가 반환되었습니다. 
- 그 다음으로 우선, 빈 리스트가 있는지 확인하여(빈 리스트가 있을 경우 k개로 나누어지지 못한 것이죠), 제외하고 그 다음에는 같은 리스트를 제외합니다. 
    - 현재는 예를 들어, `[['a'], ['b']]`와 `[['b'], ['a']]`를 다른 것으로 생각합니다. 따라서, 이 둘은 같은 것이므로 같은 경우를 확인해서 제외합니다. 

```python
def k_partition_lst(input_lst, k):
    #######################################
    def all_partition(partition_lst, remain_lst):
        # parition_lst는 개별 partition로 구성된 list를 말함. 
        # 예를 들어서, 2개로 나눈다면, [[list(), list()]]로 초기값이 구성되어야 함.
        # 즉, 2개로 분할한 리스트의 리스트를 인풋으로 받아들임. 
        # 또한, 가능한 모든 partition을 리턴하며, 비워져 있는 parition도 있고, 중복도 있음 이는 추후에 변경 
        if len(remain_lst)==1:
            candidates = []
            for partition in partition_lst:
                for i in range(0, len(partition)):
                    new_candidate = [p.copy() for p in partition]
                    new_candidate[i].append(remain_lst[0])
                    candidates.append(new_candidate)
            return candidates
        elif len(remain_lst)==0:
            return partition_lst
        else:
            candidates = []
            for partition in partition_lst:
                for i in range(0, len(partition)):
                    # 현재 구조가 list of list인데, 이 때는 그냥 상위 리스트에서 copy를 하면, 아래 list가 얕은 복사가 되어 문제가 생김. 
                    new_candidate = [p.copy() for p in partition]
                    new_candidate[i].append(remain_lst[0])
                    candidates.append(new_candidate)
            return all_partition(candidates, remain_lst[1:])
    #######################################
    # k개로 분할할 수 있는 모든 종류의 리스트를 리턴 
    all_partition_lst = all_partition([[list() for i in range(0, k)]], input_lst )
    # sorted을 해야 이후에 tuple로 만들때 문제가 생기지 않음.
    all_partition_lst = [[sorted(each_p) for each_p in partition] for partition in all_partition_lst]
    r_partition_lst = []
    # vacant list를 삭제함: k로 분할되지 않았음.
    for partition in all_partition_lst:
        if [] not in partition: 
            r_partition_lst.append(sorted(partition, key=lambda x: x[0]))
    # remove duplicate required
    r_partition_lst = [tuple([tuple(each_p) for each_p in partition]) for partition in r_partition_lst]
    r_partition_lst = set(r_partition_lst)
    print(len(r_partition_lst))
    return [[list(each_p) for each_p in partition] for partition in r_partition_lst]

for partition in k_partition_lst(['a', 'b', 'c', 'd'], 3):
    print(partition)

```


## wrap-up

- 경우에 따라서는 리커시브로 짜는 것이 훨씬 이해도 그렇고, 짜기도 편한 것 같습니다. 