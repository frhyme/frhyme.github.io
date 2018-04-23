# rotateMatrix

## Problem

- 매트릭스를 회전하는 함수를 만들어 봅니다. 
	- Transpose 는 diagonal line을 축으로 회전해주는 것이고, 여기서 만들려고 하는 것은 matrix의 중심에서 회전시키는 것을 말합니다. 
	- 역시 예제로 설명하는 것이 좋을 것 같네요....

### examples 

#### code 

- python에서 matrix를 그냥 `print`만으로 출력하면 모양이 예쁘게 안 나와서, row별로 출력하는 함수를 간단히 정의했습니다. 
- 제가 정의한 `rotateImage` 함수를 활용하면, 기존의 함수들이 모양이 시계방향으로 90도 돌려집니다. 
	- 해당 함수의 자세한 내용은 이후에 말씀드릴 테니, 일단은 이렇게 바꿔주는 문제구나, 라는 것만 이해하시면 될것 같습니다. 

```python
def print_mat(mat):
    for row in mat:
        print(row)

for n in [2,4]:
    test_mat = [[i*n+j+1 for j in range(0, n)] for i in range(0, n)]
    print("test_mat(not rotated):")
    print_mat(test_mat)
    print()
    print("test_mat(rotated)")
    print_mat( rotateImage(test_mat) )     
    print()
```

### result

```
test_mat(not rotated):
[1, 2]
[3, 4]

test_mat(rotated)
[3, 1]
[4, 2]

test_mat(not rotated):
[1, 2, 3]
[4, 5, 6]
[7, 8, 9]

test_mat(rotated)
[7, 4, 1]
[8, 5, 2]
[9, 6, 3]
```

## solution

- 고등학교 수학 시간에 배운, 회전 축이 되는 점(origin)을 중심으로 회전시키는 함수입니다. 
	- origin: 회전 점, 이번 문제에서는 매트릭스의 중간점이 됩니다. 
	- point: 회전되는 점
	- angle: 회전 각도, 여기서, 우리가 일반적으로 말하는 360도가 아닌 `radian`이라는 것이 중요합니다.
		- 간단히 `math.radians`로 변환할 수 있습니다. 

```python
import math
def rotate(origin, point, angle):
    ox, oy = origin
    px, py = point
    angle = math.radians(angle)
    qx = ox + math.cos(angle) * (px - ox) - math.sin(angle) * (py - oy)
    qy = oy + math.sin(angle) * (px - ox) + math.cos(angle) * (py - oy)
    return qx, qy
```


- matrix를 회전해주는 함수입니다. 여기서는 항상 시계방향으로 90도 회전하는 것으로 고정되어 있습니다. 
	- 또한, matrix의 row 개수와 columns의 개수는 항상 같다고 고정하고 진행했습니다. 

```python
def rotateImage(a):
    n = len(a)
    r_mat =[[0 for j in range(0, n)] for i in range(0, n)]
    for i in range(0, n):
        for j in range(0, n):
            r_i, r_j = rotate(((n-1)/2.0, (n-1)/2.0), (i,j), -90.0)
            r_i, r_j = int(r_i+0.5), int(r_j+0.5)
            r_mat[r_i][r_j] = a[i][j]
    return r_mat


```
