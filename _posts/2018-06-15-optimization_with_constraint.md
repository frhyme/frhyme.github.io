---
title: optimization with constraint
category: python-lib 
tags: python scipy python-lib optimization numpy 
---

## constraint가 있을 경우에 optimization 방법

- 이전에는 constraint가 없는 상황에서, 비교적 간단하게 최적화를 했습니다. constraint가 없는 경우에는 그냥 그려진 objective function만을 미분하여 gradient descent로 진행해도 되는 거니까요. 
- 그러나 만약에 weight에 대해서 어떤 조건이 반드시 성립되어야 할 경우(뭐 w_1이 반드시 1보다 커야 하고, 합이 10이어야 하고 뭐 그런 것들)에는 같은 방식으로 접근할 수 없습니다. 이럴 때는 어떻게 진행하는 것이 좋을까요? 

## 어떻게 푸는가?

- 기본적으로는 lagrange multiplier를 이용합니다. 간단히 말하면, 조건을 만족해야 하는 equality constraint, inequality constraint에 lambda를 개별적으로 곱하고, 이 함수를 objective function으로 새로 설정해줍니다. 
    - 이렇게 해야, optimize를 할 때, 개별 equality constraint가 충족될 경우, objective function에 lambda가 추가되어 증가하게 되기 때문에, 알아서 잘 찾게 됩니다. 흠. 역시나 문과적인 설명이군요 하하핫. 
- 저는 그냥 포스트에 있는 내용을 참고했습니다. 그림을 그려볼까 했는데, 귀찮네요. 

```python
import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt 
from scipy.optimize import fmin_slsqp
"""
- 직접 그림을 그려보지는 않았고, 그냥 참고한 포스트에 있는 내용을 그대로 사용함. 
- equality constraint, inequality constraint 상관없이, 모두 넘기면 되는데, 단 ineqaulity는 항상 positive하도록 넘겨야 함 
"""
def obj_fun(x):
    return x[0] ** 2 + x[1] ** 2
def eq_const1(x):
    return x[0] + x[1] - 1
def ieq_const1(x): # returned value should be positive  constraint >=0
    return np.atleast_1d(1 - np.sum(np.abs(x)))

x_opt = fmin_slsqp(obj_fun, np.array([0, 0]), 
           eqcons=[eq_const1], 
           ieqcons=[ieq_constraint])
print("-----")
print(x_opt)
```
```
Optimization terminated successfully.    (Exit mode 0)
            Current function value: 0.5
            Iterations: 3
            Function evaluations: 13
            Gradient evaluations: 3
-----
[ 0.5  0.5]
```

## infeasible 

- constraint가 infeasible인 경우, 출력 메세지에서 `Inequality constraints incompatible`라고 표시된다. 

```python
import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt 
from scipy.optimize import fmin_slsqp

def obj_fun(x):
    return x[0] ** 2 + x[1] ** 2
def eq_const1(x):
    return x[0] + x[1] - 1
def eq_const2(x):
    return x[0] + x[1] - 2
def ieq_const1(x): # returned value should be positive  constraint >=0
    return x[0]

x_opt = fmin_slsqp(obj_fun, np.array([0, 0]), 
           eqcons=[eq_const1, eq_const2], ieqcons=[ieq_const1])
print("-----")
print(x_opt)
```

```
Inequality constraints incompatible    (Exit mode 4)
            Current function value: 0.0
            Iterations: 1
            Function evaluations: 4
            Gradient evaluations: 1
-----
[ 0.  0.]
```

## wrap-up

- equailtiy function은 결과가 =0 의 형태로 
- inequality function은 결과가 >=0 의 형태로 

## reference 

- <https://datascienceschool.net/view-notebook/0c66f1810445488baf19cac79305793b/>