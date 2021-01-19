---
title: Algorithm - sudoku(grid)
category: algorithm 
tags: python algorithm sudoku matrix
---

## Problem

- n * n matrix를 입력받아, 해당 매트릭스에서 스도쿠의 요건이 성립하는지를 체크하는 함수
	- 모든 row에 1 - 9 까지의 모든 값이 있을 것
	- 모든 column에 1 - 9 까지의 모든 값이 있을 것
	- 3칸 씩 잘라서 만든 square 9개 각각에 모두 1 - 9까지의 모든 값이 있을 것 


## solution

- row, column, square 각각에 대해서 1-9까지의 값들이 존재하는지를 파악하는 boolean list를 만든다. 
	- 물론 현재의 코드는 해당 리스트에 유니크한 9개의 원소가 존재한다는 것만을 증명한다. 
	- 만약 필요하다면, 해당 컨디션 체크함수를 다른 식으로 정의해서 사용하면 되기 때문에 여기서는 일단 이정도로 넘어간다
- boolean list 의 모든 값이 True인 것을 체크한다. 
	- `any`, `all` 은 boolean list에 대해서 사용되며 유용함. 

```python
def sudoku(grid):
    check_rows=[len(set(row))==9 for row in grid]
    check_cols=[len(set(row))==9 for row in cols(grid)]
    check_sqrs=[len(set(row))==9 for row in return_flat_9_square(grid)]
    return all(check_rows+check_cols+check_sqrs)
```


- 기타 정의한 함수들
	- `cols(grid)`: 칼럼 리스트를 리턴
	- `dice_flat_grid(grid, inrow, incol)`: inrow에 속하는 row, incol에 속하는 칼럼의 원소만을 리턴
	- `return_flat_9_square(grid)`: 총 9개의 스퀘어를 리스트를 리턴.

```python
def cols(grid):
    return [[grid[j][i] for j in range(0, len(grid))] for i in range(0, len(grid))]

def dice_flat_grid(grid, inrow, incol):
    r=[]
    for i in range(0, len(grid)):
        for j in range(0, len(grid)):
            if i in inrow and j in incol:
                r.append(grid[i][j])
    return r

def return_flat_9_square(grid):
    r = []
    for i in range(0, 3):
        for j in range(0, 3):
            r.append( dice_flat_grid(grid, range(i*3, (i+1)*3), range(j*3, (j+1)*3)) )
    return r
```
