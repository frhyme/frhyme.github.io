---
title: numpy - along axis vs. over axes
category: python-libs
tags: python numpy apply python-libs 
---

## intro 

- 사실, 저는 `np.array`를 사용해서 코딩하는 것보다는, list를 사용하는 것이 훨씬 익숙합니다. `map`, `filter`, `reduce`를 이용하면 제가 원하는 형태의 코딩을 꽤 빠르게 할 수 있거든요. 
- 그래서 `np.array`를 활용해서 좀 더 복잡한 계산들을 빠르게 끝낼 수 있어요. 아마 두 가지 이유가 있겠죠, 우선은 해당 라이브러리는 pure python이 아니라 c로 포팅되어 있고, 그 내부에서 병렬 계산도 지원을 하기 때문이겠죠. 
- 아무튼 `np.array`를 활용할 때, 사용할 수 있는 `apply`는 두 개가 있습니다. 이 두개가 미묘하게 다른데, 사실 하나만 잘 알면 되기는 합니다. 그래도 헷갈리니까 이 두 가지를 잘 작성해두도록 하죠 

## np.apply_along_axis

- [np.apply_along_axis](https://docs.scipy.org/doc/numpy/reference/generated/numpy.apply_along_axis.html)는 주어진 함수를 주어진 축에 적용해서 그 값을 리턴하는 것을 말합니다. axes가 아니고 axis인 것이 중요하죠. 

### example 

- 간단하게 사용해보면 대략 다음과 같아요. 
- 아래 코드에서는 (2, 3, 4) 차원으로 구성된 array에 대해서 
    - 처음에는 0번째 axis에 대해서 `np.sum`을 적용하고, 
    - 리턴된 (3, 4)차원으로 구성된 array에 대해서 
    - 1번째 axis에 대해서 `np.sum`을 적용합니다. 
- 즉 결과로는 (2,3,4) 차원에서 3만 살아있다고 보면 되겠쬬. 

```python
import numpy as np 

a = np.arange(24).reshape(2,3,4)
print(f"shape: {a.shape}")
print(a)
print("=="*20)
result = np.apply_along_axis(func1d=np.sum, axis=0, arr=a)
print(f"shape: {result.shape}")
print(result)
print("=="*20)
result = np.apply_along_axis(func1d=np.sum, axis=1, arr=result)
print(f"shape: {result.shape}")
print(result)
```

```
shape: (2, 3, 4)
[[[ 0  1  2  3]
  [ 4  5  6  7]
  [ 8  9 10 11]]

 [[12 13 14 15]
  [16 17 18 19]
  [20 21 22 23]]]
========================================
shape: (3, 4)
[[12 14 16 18]
 [20 22 24 26]
 [28 30 32 34]]
========================================
shape: (3,)
[ 60  92 124]
```

## np.apply_over_axes

- 눈썰미가 좋으신 분은 아실 수도 있겠지만, 여기는 axis가 아니라 **axes**입니다. 복수죠. 즉, 여러 축을 연속으로 적용하는 경우를 말합니다. 

### example

- 아래에서는 shape이 (2,3,4)인 array에 대해서, 0번째, 2번째 axis에 대해서 `np.sum`을 연속으로 적용합니다. 
- 결과를 보시면 `np.apply_along_axis`와 같은 것을 알 수 있죠. 

```python
import numpy as np 

a = np.arange(24).reshape(2,3,4)
print(f"shape: {a.shape}")
print(a)
print("=="*20)
result = np.apply_over_axes(func=np.sum, axes=(0, 2), a=a)
print(f"shape: {result.shape}")
print(result)
print("=="*20)
print(result.reshape(3))
```

```
shape: (2, 3, 4)
[[[ 0  1  2  3]
  [ 4  5  6  7]
  [ 8  9 10 11]]

 [[12 13 14 15]
  [16 17 18 19]
  [20 21 22 23]]]
========================================
shape: (1, 3, 1)
[[[ 60]
  [ 92]
  [124]]]
========================================
[ 60  92 124]
```

## wrap-up

- 뭐 사실 저는 그냥 np.apply_along_axis를 쓰는 것이 더 좋은 것 같습니다. 
- 이게 더 직관적이에요. 
- 그리고 넘기는 argument의 순서가 func, axis, arr 인 것을 유의하면 좋을 것 같아요. 