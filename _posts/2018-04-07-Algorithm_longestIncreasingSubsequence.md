# longestIncreasingSubsequence(sequence)

## Problem 

- Given `sequence`, find the longest IncreasingSubsequence. 
	- 정확히는 길이만 계산해주면 되는 함수

### example 

- consecutive가 아니고, integer position 상에서 앞과 뒤의 관계만 지켜지면 된다. 
	- [1,2,3] ==> [1,2,3]
	- [1,4,3] ==> [1,4] or [1,3]
	- [1,8,9,2,4,5] ==> [1,2,4,5]

## solution - first try, failed because of computation time

### allMaximalSubSeq

- 우선, 부분적으로 increasing sequence들을 분할해야 좀 더 효과적으로 계산할 수 있지 않을까? 라는 생각을 하여, 현재 시퀀스를 개별적인 increasing sequence들로 분할해주는 함수를 만들었다. 
	- allMaximalSubSeq([1,2,3,5,4, 6, 3, 1,2]) ==>
		- [[1, 2, 3, 5], [4, 6], [3], [1, 2]]

```python
def allMaximalSubSeq(seq):
    rs = []
    start_pos = 0 
    for i in range(1, len(seq)):
        if seq[i-1]>=seq[i]:
            rs.append(seq[start_pos:i])
            start_pos = i
    rs.append(seq[start_pos:])
    return rs
```

### allPossibleSeq

- 입력받은 increasing seq로부터 만들 수 있는 size 1부터 len(increaing seq)까지의 부분 seq를 리턴해주는 함수 
	- allPossibleSeq([1,2,3]) ==> 
		- [[1, 2, 3], [1, 2], [2, 3], [1], [2], [3]]

```python
def allPossibleSeq(seq):
    rs = []
    for n in range(len(seq)-1+1, 0, -1):
        for i in range(0, len(seq)-n+1):
            rs.append(seq[i:i+n])
    return rs
```

### longestIncreasingSubsequence

1. 기존 sequence로부터 increasing sequence들만 따로 뽑아 내고 
	- allMaximalSubSeq
2. 개별 increasing sequence를 순서대로 병합하면서 진행한다. 
	- increasing sequence i 
	- increasing sequence j (j>i)
	- inc seq i 의 모든 부분 집합과 j 의 모든 부분 집합을 통해 만들 수 있는 모든 새로운 increasing seq를 만든다. 
	- 이를 연속으로 수행하면, 마지막에는 만들 수 있는 모든 increasing sequence를 만들어 낼 수 있음. 

- 다만, 이는 결국 full enumeration이라서, 계산시간이 너무 오래 걸린다는 한계가 명확하게 있다. 
	- 특히, codefights에서 요구하는 sequence의 사이즈는 700개가 넘는데, 그 경우에는 으어...
- 그래서 아예 새롭게 풀어보기로 했다. 

```python
def longestIncreasingSubsequence(sequence):
    all_subseq = allMaximalSubSeq(sequence)
    if len(all_subseq)==1:
        return len(sequence)
    else:
        head=allPossibleSeq(all_subseq[0])
        for i in range(1, len(all_subseq)):
            rs =[]
            for s1 in head:
                for s2 in allPossibleSeq(all_subseq[i]):
                    if s1[-1]<s2[0]:
                        rs.append(s1+s2)
                    else:
                        if s1 not in rs:
                            rs.append(s1)
                        if s2 not in rs:
                            rs.append(s2)
            rs = sorted(rs, key=lambda x: len(x), reverse=True)
            head=rs
        return len(head[0])
```

## second try - simple and better solution 

- 이 방법은 list 를 
- 대략 연산 시간은, 45개의 sequence를 연산할 때, 2000배 정도의 차이가 난다. 그러니까, 이렇게 알고리즘이 중요합니다. 
	- first try: 0.8 sec
	- second try: 0.0004
- 이 문제는 헷갈리기 쉽기 때문에, 아래에 다양한 예시를 첨부하였다. 

```python
def longestIncreasingSubsequence(seq):
    rnk_lst = [1]*len(seq)
    print("sequence: {}".format(seq))
    for j in range(1, len(seq)): # always i<j
        for i in range(0, j):
            print("i: {}, j: {}, rnk_lst:{}".format(i, j, rnk_lst))
            if seq[i]<seq[j]: # 만약, j 앞에 있는 i의 값이 더 작을 경우에
                if rnk_lst[j]==rnk_lst[i]: #또한 그 값이 j앞에 있는 원소중에서 가장 큰 원소일 경우, 
                    rnk_lst[j]+=1
                else:#현재 원소보다 작긴하지만, 작은 원소 중에서 가장 큰 원소가 아니기 때문에, 넘어간다. 
                	continue
            else: # 현재 원소보다 앞에 있지만, 더 값이 크기 때문에, 해당 rank를 참고할 필요가 없다. 
            	continue
    print("final rnk_lst: {}".format(rnk_lst))
    return max(rnk_lst)
```


### example 

```python
seq = [1,2,3]
longestIncreasingSubsequence(seq)
```

```
sequence: [1, 2, 3]
i: 0, j: 1, rnk_lst:[1, 1, 1]
i: 0, j: 2, rnk_lst:[1, 2, 1]
i: 1, j: 2, rnk_lst:[1, 2, 2]
final rnk_lst: [1, 2, 3]
```

```python
seq = [1,2,3,4,5]
longestIncreasingSubsequence(seq)
```

```
sequence: [1, 2, 3, 4, 5]
i: 0, j: 1, rnk_lst:[1, 1, 1, 1, 1]
i: 0, j: 2, rnk_lst:[1, 2, 1, 1, 1]
i: 1, j: 2, rnk_lst:[1, 2, 2, 1, 1]
i: 0, j: 3, rnk_lst:[1, 2, 3, 1, 1]
i: 1, j: 3, rnk_lst:[1, 2, 3, 2, 1]
i: 2, j: 3, rnk_lst:[1, 2, 3, 3, 1]
i: 0, j: 4, rnk_lst:[1, 2, 3, 4, 1]
i: 1, j: 4, rnk_lst:[1, 2, 3, 4, 2]
i: 2, j: 4, rnk_lst:[1, 2, 3, 4, 3]
i: 3, j: 4, rnk_lst:[1, 2, 3, 4, 4]
final rnk_lst: [1, 2, 3, 4, 5]
```

```python
seq = [1,2,3,1,2,3]
longestIncreasingSubsequence(seq)
```

```
sequence: [1, 2, 3, 1, 2, 3]
i: 0, j: 1, rnk_lst:[1, 1, 1, 1, 1, 1]
i: 0, j: 2, rnk_lst:[1, 2, 1, 1, 1, 1]
i: 1, j: 2, rnk_lst:[1, 2, 2, 1, 1, 1]
i: 0, j: 3, rnk_lst:[1, 2, 3, 1, 1, 1]
i: 1, j: 3, rnk_lst:[1, 2, 3, 1, 1, 1]
i: 2, j: 3, rnk_lst:[1, 2, 3, 1, 1, 1]
i: 0, j: 4, rnk_lst:[1, 2, 3, 1, 1, 1]
i: 1, j: 4, rnk_lst:[1, 2, 3, 1, 2, 1]
i: 2, j: 4, rnk_lst:[1, 2, 3, 1, 2, 1]
i: 3, j: 4, rnk_lst:[1, 2, 3, 1, 2, 1]
i: 0, j: 5, rnk_lst:[1, 2, 3, 1, 2, 1]
i: 1, j: 5, rnk_lst:[1, 2, 3, 1, 2, 2]
i: 2, j: 5, rnk_lst:[1, 2, 3, 1, 2, 3]
i: 3, j: 5, rnk_lst:[1, 2, 3, 1, 2, 3]
i: 4, j: 5, rnk_lst:[1, 2, 3, 1, 2, 3]
final rnk_lst: [1, 2, 3, 1, 2, 3]
```

```python
seq = [1,2,3,2,3,4]
longestIncreasingSubsequence(seq)
```

```
sequence: [1, 2, 3, 2, 3, 4]
i: 0, j: 1, rnk_lst:[1, 1, 1, 1, 1, 1]
i: 0, j: 2, rnk_lst:[1, 2, 1, 1, 1, 1]
i: 1, j: 2, rnk_lst:[1, 2, 2, 1, 1, 1]
i: 0, j: 3, rnk_lst:[1, 2, 3, 1, 1, 1]
i: 1, j: 3, rnk_lst:[1, 2, 3, 2, 1, 1]
i: 2, j: 3, rnk_lst:[1, 2, 3, 2, 1, 1]
i: 0, j: 4, rnk_lst:[1, 2, 3, 2, 1, 1]
i: 1, j: 4, rnk_lst:[1, 2, 3, 2, 2, 1]
i: 2, j: 4, rnk_lst:[1, 2, 3, 2, 3, 1]
i: 3, j: 4, rnk_lst:[1, 2, 3, 2, 3, 1]
i: 0, j: 5, rnk_lst:[1, 2, 3, 2, 3, 1]
i: 1, j: 5, rnk_lst:[1, 2, 3, 2, 3, 2]
i: 2, j: 5, rnk_lst:[1, 2, 3, 2, 3, 3]
i: 3, j: 5, rnk_lst:[1, 2, 3, 2, 3, 4]
i: 4, j: 5, rnk_lst:[1, 2, 3, 2, 3, 4]
final rnk_lst: [1, 2, 3, 2, 3, 4]
```









