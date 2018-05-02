---
title: Algorithm - arrayMaxConsecutiveSum(inputArray, k))
category: algorithm
tags: python algorithm list iterator codefight

---

## Problem
- size `l`의 배열이 있을 때, 해당 배열로부터는 크기 `k`의 연속된 배열을 `l-k+1`개 만들 수 있다. 
- 만들 수 있는 배열 중에서 가장 큰 합은 무엇인가? 

## solution

### slower, but pythonic way

- 사실 아래 방법이 보통 파이썬을 쓰는 사람들이 많이 하는 방법이긴 합니다만, 
- inputArray의 크기가 클 때를 고려하면, 연속된 배열을 미리 다 만들어 놓을 필요는 없습니다. 
- 따라서, 다음 코드에서는 `list`를 미리 만들지 않고, generator를 만들어서 진행해보겠씁니다. 

```python
def arrayMaxConsecutiveSum1(inputArray, k):
    kxs = [inputArray[i:i+k] for i in range(0, len(inputArray)-k+1)]
    return max(map(lambda xs: sum(xs), kxs))
```

### little better, with generator

- list로 만들어 주지 않고, generator를 사용해서 `k` 크기의 배열을 필요할 때마다 생성해서 가져오는 식으로 처리했습니다. 
- 속도 자체도 위의 코드에 비해서 4배 정도(크기 10000의 리스트에 대해) 빨라지고, memory usage도 훨씬 줄어듭니다. 
- 하지만, 생각해보면, 연속된 배열을 만들 때마다, 이전에 만든 배열과 새로 만들어진 배열은 대부분의 원소가 같을텐데, 매번 새로운 배열을 만들어줄 필요가 있나? 하는 생각이 듭니다. 
- 따라서, 다른 방식을 취해볼게요. 

```python
def arrayMaxConsecutiveSum2(inputArray, k):
    kxs = (inputArray[i:i+k] for i in range(0, len(inputArray)-k+1))
    m = 0 
    for x in kxs:
        t = sum(x)
        m = m if m>t else t
    return m
```

### intelligent way

- 연속된 수열이기 때문에, 새로 만들어지는 수열(`new_xs`)은 기존 수열(xs)에서 xs[1:]에 새로운 원소를 하나 추가하는 형태를 가집니다. 
- 따라서 새로운 수열에서 빠지는 원소의 값 보다 새로 들어오는 원소의 값이 더 클 경우, 해당 리스트의 합은 더 커지게 됩니다. 
- 따라서 수열을 굳이 만들 필요 없이, `inputArray`를 딱 한번만 읽으면서 진행하면 되기 때문에 훨씬 이득입니다. 
- 속도 측면에서도 바로 위에 비해 3배 정도 빠릅니다. 

```python
def arrayMaxConsecutiveSum3(inputArray, k):
    max_v = sum(inputArray[0:k])
    l = len(inputArray)
    last_v = max_v
    for i in range(k, l):
        last_v = last_v+inputArray[i]-inputArray[i-k]
        if max_v < last_v:
            max_v = last_v
    return max_v
```
