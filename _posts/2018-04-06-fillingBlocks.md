---
title: fillingBlocks(n)
category: algorithm
tags: python algorithm dynamic-programming codefight recursion

---

## Problem

- n * 4 의 직사각형을 2 * 1 혹은 1 * 2의 직사각형으로 채워야 할때, 채울 수 있는 방법의 수는 총 몇 가지 인지를 리턴하는 함수입니다. 
	- if n==1: 1 * 4 인 직사각형은 2 * 1을 가로로 두 번 채우는 것 밖에 방법이 없음 ==> 1
	- elif n==2:
		- if 왼쪽 위를 가로로 채웠을 경우 => 왼쪽 아래도 무조건 가로로 채워져야 함
			- if 오른쪽 위를 가로로 채웠을 경우 => 1
			- elif 오른쪽 첫번째를 세로로 채웠을 경우 => 1
		- elif 왼쪽을 세로로 채웠을 경우 => 
			- if 다시 세로로 하나 더 채울 경우 => 오른쪽 2 * 2가 남으며 이 경우는 2가지 
			- else 가로로 위를 하나 채우는 경우 => 1
	- elif n==3: 
		...
- 이런 식으로 반복되도록 프로그래밍할 수 있습니다. 


## solution 

- 따라서, 아래처럼 간단하게 recursive하게 코드를 만들 수 있다.
- if n> 3일 때는 다음처럼 케이스를 나누었는데 
	- event row: 왼쪽 위에 가로로 하나 채울 경우, 
	- event col: 왼쪽을 세로로 하나 채울 경우, 중요한 것은 not event row 일 경우 event col이라는 것이다. 왼쪽 위를 채울 수 있는 방법은 가로로 채우거나, 세로로 채우거나 일 방법밖에 없음
		- event col col row : 왼쪽을 세로로 두 개 가로로 하나 채우는 경우 
		- event col row col : 세로로 하나 가로로 하나 세로로 하나 채우는 경우 
		- event col col col col : 세로로 네 개를 연속으로 채우는 경우
		- 위 세 가지 event의 합집합은 event col이 된다. 
- **dynamic programming에서 중요한 것은 서로 exclusive한 event를 찾는 것이고, 개별 event들이 촘촘하게 엮여서, 빠지는 경우의 수가 없도록 잘 정리하는 것이다.**

```python
def fillingBlocks(n):
    if n ==0:
        return 0
    elif n ==1:
        return 1
    elif n==2:
        return 5
    else:
        row = fillingBlocks0011(n-1) # 왼쪽 위에 가로로 넣었을 때, 
        col_col_row = fillingBlocks0011(n-2) # 왼쪽부터 세로로 두 개, 가로로 하나 넣었을 경우, 
        col_row_col = fillingBlocks0110(n-2)
        # 왼쪽부터 세로로 하나, 가로로 하나, 세로로 하나 넣었을 때, 뿔처럼 위에 두 칸만 비는 경우 
        col_col_col_col = fillingBlocks(n-2) # 세로로 제일 위 두 줄을 채웠을 때 
        return row + col_col_row + col_row_col + col_col_col_col
```


- 아무튼 아래 함수에서 빠지는 경우의 수가 없도록 잘 정리했으니 이제 각각의 경우를 표현한 함수를 정리해보장
- `fillingBlocks0110(n)`은 `_--_` 의 형태를 채울 수 있는 가지 수를 의미한다. 
	- case1) 튀어나와 있는 부분을 가로로 채우는 경우 ==> fillingBlocks(n)
	- case2) 튀어나와 있는 부부을 세로로 채우는 경우 ==> fillingBlocks0110(n-2)

```python
def fillingBlocks0110(n):
    if n==0:
        return 1
    elif n==1:
        return 1
    else:
        return fillingBlocks(n)+fillingBlocks0110(n-2)
```

- `fillingBlocks0011(n)`은 `__--` 의 형태를 채울 수 있는 가지 수를 의미한다. 
	- case1) 튀어나와 있는 부분을 가로로 채우는 경우 ==> fillingBlocks(n)
	- case2) 튀어나와 있는 부부을 세로로 채우는 경우 ==> fillingBlocks0011(n-1)

```python
def fillingBlocks0011(n):
    if n==0:
        return 1
    else:
        return fillingBlocks(n)+fillingBlocks0011(n-1)
```


## make it iterative 

- 지난 번에 말한 것처럼 recursive하게 만들었을 경우 계산 시간이 오래 걸린다. 
	- if n==17, recursive는 4.5초, iterative는 0.0001
- 따라서, 값이 새로 생성되면 이를 dictionary에 저장을 하여, 함수 콜을 하지 않고 바로 값을 가져오도록 처리하도록 하자. 


```python
def fillingBlocks(n):
    b0011_d = {0:1}
    b0110_d = {0:1, 1:1}
    b_d = {0:0, 1:1, 2:5}
    for i in range(1, n+1):
        if i==1:
            b_d[i]=1
        elif i==2:
            b_d[i]=5
        else:
            if i-2 in b0011_d.keys():
                a = b0011_d[i-2]
            else:
                b0011_d[i-2] = b_d[i-2] + b0011_d[i-3]
                a = b0011_d[i-2]
            if i-1 in b0011_d.keys():
                b = b0011_d[i-1]
            else:
                b0011_d[i-1] = b_d[i-1] + b0011_d[i-2]
                b = b0011_d[i-1]
            if i-2 in b0110_d.keys():
                c = b0110_d[i-2]
            else:
                b0110_d[i-2] = b_d[i-2] + b0110_d[i-4]
                c = b0110_d[i-2]
            if i-2 in b_d.keys():
                d = b_d[i-2]
            else:
                b_d[i-2] = b0011_d[i-4]+b0011_d[i-3] + b0110_d[i-3]+b_d[i-4]
                d = b_d[i-2]
            b_d[i] = a+b+c+d
    return b_d[n]
```
