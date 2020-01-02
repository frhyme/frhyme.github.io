---
title: julia vs. (pure)python
category: others
tags: python python-lib julia pi 
---

## 토끼와 거북이 

- 누가 더 빠를까요. python과 julia중에서. 

## how to compute pi - spigot alogirithm 

- pi를 계산합니다. 원주율을 말합니다. 빅파이 먹고 싶네요 
- 아무튼, 딴생각을 하다가 pi는 어떻게 계산하는지가 갑자기 궁금해졌습니다. 원주를 재고 반지름을 재고 뭐 그런 식으로 하지는 않을 거니까요(정밀도 문제가 있구요)
- 그래서 찾아보니, [위키피디아](https://en.wikipedia.org/wiki/Pi)에 구하는 방식이 있습니다. 
- 다양한 알고리즘이 있는데 spigot 알고리즘을 사용해보려고 합니다. 
- 방정식은 다음과 같습니다. 

![](https://wikimedia.org/api/rest_v1/media/math/render/svg/5be33d7e24e7ab4d284dd957955227fb6faee2d3)

- 파이썬 코드로 바꾸면 

```python
%%timeit -n 10 -r 1
def compute_pi(n=10):
    r = 0
    for k in range(0, n):
        r+= 1/(16**k)*( 4/(8*k+1) - 2/(8*k+4) - 1/(8*k+5) - 1/(8*k+6))
    return r
compute_pi(20000)
```

- julia 코드로 바꾸면 

```julia
@time begin
    function compute_pi(n=10)
        r = 0
        for k in 0:9
            r+= 1/(16^k)*( 4/(8k+1) - 2/(8k+4) - 1/(8k+5) - 1/(8k+6))
        end
        r
    end
    compute_pi(20000)
end 
```

- python의 경우는 2.46초가 걸리고, julia의 경우는 0.02초가 걸립니다....
- 좀 더 비교를 해보긴 해야겠지만, 빠르긴 진짜 개빠르네요.....
- 물론 `numpy`를 사용하면 속도가 매우 빨라지기는 합니다. 0.00047초, 쥴리아보다 더 빨라지기는 하죠. 

```python
%%timeit -n 1 -r 1
def compute_pi(n=10):
    return np.array([ 1/(16**k)*( 4/(8*k+1) - 2/(8*k+4) - 1/(8*k+5) - 1/(8*k+6)) for k in range(0, 10)]).sum()
print(compute_pi(20000))
```

## fibonacci 

- 이번에는 fibonacci로 비교해보겠습니다. 

- python의 경우 3.26초가 걸립니다. 

```python
%%timeit -n 1 -r 1
def fibo(n):
    if n in {0, 1}:
        return 1
    else: 
        return fibo(n-2)+fibo(n-1)
print(fibo(34))
```

```
9227465
3.26 s ± 0 ns per loop (mean ± std. dev. of 1 run, 1 loop each)
```

- julia의 경우 0.11초가 걸립니다. 즉 **julia가 약 30배 빠릅니다. 

```julia
@time begin
    function fibo(n)
        if n==0 || n==1
            return 1
        else
            return fibo(n-2) + fibo(n-1)
        end
    end
    fibo(34)
end
```

```
  0.110786 seconds (740 allocations: 41.846 KiB)
9227465
```

- 물론 memoization을 이용하면 python 11000배 빨라집니다만, [julia에도 lru_cache는 있습니다.](https://github.com/JuliaCollections/LRUCache.jl) pure하게 비교해야죠. 

```python
%%timeit -n 1 -r 1
from functools import lru_cache
@lru_cache(maxsize=12)
def fibo(n):
    if n in {0, 1}:
        return 1
    else: 
        return fibo(n-2)+fibo(n-1)
print(fibo(34))
```

```
9227465
288 µs ± 0 ns per loop (mean ± std. dev. of 1 run, 1 loop each)
```


## wrap-up

- 코딩할때의 편리함은 julia나 python이 유사한데, 속도 측면에서는 python이 julia를 따라잡을 수가 없습니다. 압살이네요. 
- 계산이 복잡할 때는 julia를 한번 써봐야될것 같아요. 그 부분만 따로 julia로 구성하고, julia에서 파이썬을 가져와서 쓰는 식으로 진행해도 좋을 것 같아요. 