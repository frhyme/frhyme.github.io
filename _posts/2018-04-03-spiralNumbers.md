---
title: spiralNumbers(n)
category: algorithm
tags: python algorithm matrix matrix-traversal code-fight

---

## Problem

- `spiral`은 나선형 이라는 뜻인데, 달팽이집처럼 뺑뺑 돌아나가는 것을 의미하고
- spiralNumbers(n)은 음...예시를 보는 게 더 빠를 것 같다. 

### examples

- 1부터 입력받은 정수까지를 n`*`n matrix에 시계방향으로 배치하고 해당 매트릭스를 리턴하는 함수를 말한다. 

#### code 

```python
for row in spiralNumbers(2):
    print(row)
```

#### code result

```
[1, 2]
[4, 3]
```

#### code 

```python
for row in spiralNumbers(4):
    print(row)
```
#### code result 

```
[1, 2, 3, 4]
[12, 13, 14, 5]
[11, 16, 15, 6]
[10, 9, 8, 7]
```

## solution

- spiralNumbers(n)과 move(mat, cur_pos, cur_dir, input_k)를 정의했다. 
	- 우선 아무 값도 할당되지 않은(value를 0 으로 세팅) 매트릭스를 생성하고
	- 집어넣어야 하는 값을 순서대로 불러온 다음(`k`)
	- move 함수에 현재 좌표와 넣어야 하는 값을 넣어주면
	- move 함수에서 해당 값을 매트릭스 상에서 적합한 위치에 넣어주고 다음 좌표를 리턴해준다. 
	- 반복하다가, 모든 값을 다 넣었을 때 루프를 종료하고 매트릭스를 리턴해준다

```python
def spiralNumbers(n):
    if n==1:
        return [[1 for j in range(0, n)] for i in range(0, n)] 
    else:
        r_mat = [[0 for j in range(0, n)] for i in range(0, n)]
        r_mat[0][0]=1
        a = (i for i in range(2, n**2+1))
        cur_pos=(0, 0)
        cur_dir=(0, 1)
        while True:
            try:
                k = next(a)
                r_mat, cur_pos, cur_dir = move(r_mat, cur_pos, cur_dir, k) 
            except:
                break
    return r_mat
```


- 진행하다가, 막히면 돌아가는 식으로 수행한다 
	- 왼쪽으로 가다가, 왼쪽이 막히면(이미 값이 있을 경우), 위로 
	- 오른쪽으로 가다가, 오른쪼이 막히면, 아래로
	- ... 
	- 아무튼 이렇게 진행해준다. 

```python
def move(mat, cur_pos, cur_dir, input_k):
    n = len(mat)
    ri, ci = cur_pos[0], cur_pos[1]
    LEFT = (0, -1)
    RIGHT = (0, 1)
    DOWN = (-1, 0)
    UP = (1, 0)
    while True:
        if cur_dir==LEFT:
            if ci-1<0 or mat[ri][ci-1]!=0:#change direction and update 
                cur_dir = UP
            else:
                cur_pos = (ri, ci-1)
                mat[cur_pos[0]][cur_pos[1]] = input_k
                return mat, cur_pos, cur_dir
        elif cur_dir==RIGHT:
            if ci+1>=n or mat[ri][ci+1]!=0:#change direction and update 
                cur_dir = DOWN
            else:
                cur_pos = (ri, ci+1)
                mat[cur_pos[0]][cur_pos[1]] = input_k
                return mat, cur_pos, cur_dir
        elif cur_dir==UP:
            if ri-1<0 or mat[ri-1][ci]!=0:#change direction and update 
                cur_dir = RIGHT
            else:
                cur_pos = (ri-1, ci)
                mat[cur_pos[0]][cur_pos[1]] = input_k
                return mat, cur_pos, cur_dir
        elif cur_dir==DOWN:
            if ri+1>=n or mat[ri+1][ci]!=0:#change direction and update 
                cur_dir = LEFT
            else:
                cur_pos = (ri+1, ci)
                mat[cur_pos[0]][cur_pos[1]] = input_k
                return mat, cur_pos, cur_dir
```

## lessson learned. 

- 예전에, 아마도 삼년 전즈음예, 이 문제를 풀었던 적이 있는데 그때는 못 풀었던 기억이 있다. 
- 알고리즘 문제들은 문제별로 다 상이하기 때문에, 내가 발전했는지 그때보다 실력이 증가했는지를 체크하는 것이 약간 어려운 부분이 있는데, 예전에 못 푼 문제를 비교적 쉽게 풀어서 기분이 좋았당. 헤헤 
