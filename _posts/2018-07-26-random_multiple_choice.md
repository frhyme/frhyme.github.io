---
title: random multiple choice
category: python-lib
tags: python python-lib random choice numpy 
---

## 중복없이 n개의 값을 뽑는 방법 

- 바구니에 n개의 서로 다른 공이 들어 있습니다. 이 공에서 3개의 공을 뽑고싶은데 어떻게 코딩해야 하나요? 
- 처음에는 약간 어렵게 다음처럼 해야 한다고 생각했는데요.

```python
import numpy as np 

cands = [i for i in range(0, 10)]

def selection(basket, n):
    new_basket = basket.copy()
    r_lst = []
    for i in range(0, n):
        temp = new_basket.pop(np.random.choice([i for i in range(0, len(new_basket))]))
        r_lst.append(temp)
    return r_lst

print( selection(cands, 10) )
```

```
[8, 6, 1, 4, 0, 7, 3, 5, 9, 2]
```

## 간단하게 

- 그냥 있는 함수를 쓰면 됩니다 하하핫. 

```python
import numpy as np 

cands = [i for i in range(0, 10)]
np.random.choice(cands, 10, replace=False)
```

```
array([4, 2, 0, 8, 9, 6, 5, 3, 7, 1])
```