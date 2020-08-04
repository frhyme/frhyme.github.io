---
title: 매번 까먹는, 몬테카를로 시뮬레이션을 해봅시다!!
category: python-lib
tags: python python-lib monte-carlo-simulation
---

## Intro - 왜 몬테카를로는 쉽게 잊어버리는 걸까요

- 네, 사실 저도 알고 있습니다. 한 번 배울 때, 제대로 배우지 않고, 주먹구구식으로 배우니까, 이모양인 것이죠...그래서 이번에는 제 블로그에 꼭 써놓고 다음에 읽어보도록 하겠습니돠.

## Monte-carlo simulation 정의

- 'random number'를 활용해 값을 추정한다, 가 가장 정확한 정의인 것 같습니다만, 이걸로 좀 애매한 부분이 있는 것 같습니다. 

## 적용 문제

- 오히려, Monte-carlo simulation은 하나의 문제와 함게 외울 때 더 정확하게 외울 수 있는 것 같습니다.

### 원의 넓이 추정

> 넓이가 1인 정사각형에 독립적으로 random number를 x,y 각각 뽑고, 이를 n 번 반복했을때, x, y 가 x^2 + y^2 <=1 사이에 있는 비율이 바로 원의 넓이가 된다. 

- deterministic 하게 푸는 것이 아니라, random number를 생성하여, 해당 조건을 만족하는 경우의 비율을 계산하여 값을 추정하는 방식을 **몬테카를로 시뮬레이션**이라고 한다. 물론 지금의 우리는 pi를 알고 있고, pi를 통해 계산하면 되는데, 왜 몬테카를로를 쓰냐? 라고 물을 수 있다. 
- 몬테 카를로 시뮬레이션은 deterministic하게 방정식에 넣어서 값을 게산할 수 없을때, 일단 여러번 시행해서 계산해보자, 라는 방식의 계산법을 말한다. 흔한 말로, '마구잡이'라고 해도 뭐 대충 맞는 말일 것 같고 
- 다르게 표현하자면, '파이'를 일종의 **블랙박스**라고 생각하는 편이 편하다. **블랙박스**의 행동을 모르고, 모르지만 여러번 시행을 통해 영향력을 검증할 수 있는 정도 를 몬테카를로 시뮬레이션이라고 한다. 

```python
import numpy as np 
import matplotlib.pyplot as plt 

s = 2000
xs = np.random.random_sample(s)*4-2
ys = np.random.random_sample(s)*4-2

c = 0
plt.figure(figsize=(5, 5))
for i in range(0, s):
    x, y = xs[i], ys[i]
    if x**2 + y**2 <=4:
        c+=1
        plt.scatter(x, y, c='blue', alpha=0.2)
    else:
        plt.scatter(x, y, c='red', alpha=0.2)
print(c/s*4)
plt.show()
```

## wrap-up 

- 뭐, 여기저기 찾아봐도, 그냥 **랜덤으로 돌려서, 추정하는 방식** 이 몬테 카를로 시뮬레이션의 정의인 것 같다. 매우 광범위해서, 오히려 내가 잘 잊어버리게 되는 것 같은데, 
- 예측 혹은 계산을 엄밀하게 하는 것이 아니라, 몇 가지 가정을 기반으로 랜덤한 값들을 마구 생성하여, 결과를 보니, 대략 (귀납적으로) 이러한 결과를 가져오더라. 라고 예측할 수 있는 방식을 **몬테카를로 시뮬레이션**이라 함

## reference 

- [간단한 몬테카를로 기법 예시](http://codingdojang.com/scode/507)
