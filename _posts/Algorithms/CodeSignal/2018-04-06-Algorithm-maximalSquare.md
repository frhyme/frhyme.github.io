---
title: Algorithm - maximalSquare(matrix)
category: algorithm
tags: python algorithm codefight dynamic-programming

---

## Problem

- https://codefights.com/interview-practice/task/mkobsYSSQo3JpvYNN/
- 0, 1로 구성된 2 dimensional binary matrix(직사각형) 내부에 있는 가장 큰 정사각형의 넓이를 계산하는 함수 
	- 0은 빈칸, 1은 채워진 칸이므로 1로 구성된 가장 큰 정사각형의 넓이를 찾아준다. 

## solution

- 우선, 이 문제의 경우 원래는 dynamic programming으로 풀었으나, 계산 시간에서 원하는 점수를 달성하지 못해서, 그냥 다른 방식으로 풀었다(물론 그냥, 내가 제대로 못 풀었을 수 있고...ㅠㅠ)


### MaxLengthInMatrix(matrix)

- 입력받은 matrix에서 만들어질 수 있는 정사각형의 수는 뭐 엄청 많다. 
	- `sum([j**2 for j in range(1, i+1)])`
- 그렇기 때문에 `l`( `max( len(matrix) len(matrix[0]))`) 부터 1까지 모두 확인할 수는 없고, 우선 최대로 가능한 정사각형의 크기를 미리 계산해본다. 
- 각 row에 연속된 1의 갯수가 몇 개인지를 카운트한다. 모든 row에서 연속된 1의 개수가 5보다 큰 경우가 없다면, 해당 matrix에서 5 이상의 크기를 가진 square가 나올 수 있는 가능성은 없다. 따라서 이 경우에는 5부터 찾아주면 된다. 

```python
def MaxLengthInMatrix(matrix):
    r = []
    for row in matrix:
        r.append(MaxConsecInRow(row))
    l = 0 
    for k in range(1, max(r)+1): #lst size
        for i in range(0, len(r)-k+1):
            if all([x >= k for x in r[i:i+k]]):
                l = k
                break
    return l
```

### maximalSquare(matrix)

- 최대의 square 사이즈를 찾았다면, 이제 사이즈를 줄여가면서 가능한 square의 넓이를 리턴해준다. 

```python
def maximalSquare(matrix):
    if len(matrix)==0:
        return 0
    else:
        l = MaxLengthInMatrix(matrix)
        for l in range(l, -1, -1):
            for mat in GenDiceLstwithL(matrix, l):
                if sum(FlattenMatrix(mat))==l**2:
                    return l**2
```

### other useful function 

```python
"""
consecutive number means the maximal length of sqr
"""
def DiceMatrix(m, f_r, to_r, f_c, to_c):
    return [[m[i][j] for j in range(f_c, to_c)] for i in range(f_r, to_r)]
def GenDiceLstwithL(matrix, l):
    r_lst = []
    for i in range(0, len(matrix)-l+1):
        for j in range(0, len(matrix[0])-l+1):
            r_lst.append(DiceMatrix(matrix, i, i+l, j, j+l))
    return r_lst
def FlattenMatrix(m):
    return [int(m[i][j]) for i in range(0, len(m)) for j in range(0, len(m))]

def MaxConsecInRow(row):
    count = 0 
    max_count = 0 
    for i in range(1, len(row)):
        if row[i]==row[i-1] and row[i]=='1':
            count+=1
        else:
            if max_count< count:
                max_count=count
            count = 0 
    if max_count<count:
        max_count=count
    return max_count+1
```
