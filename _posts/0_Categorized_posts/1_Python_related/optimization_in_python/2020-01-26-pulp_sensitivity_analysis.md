---
title: python - pulp - sensitivity analysis 
category: python-libs
tags: python python-libs gurobi LP linearprogramming optimization pulp
---

## LP for handling uncertainty.

- 기본적으로 LP는 특정한 상황(constraint)일 때 최적의 해를 구하는 방법이죠. 따라서 만약 coef들이 달라진다면, 최적해도 달라지게 됩니다. 우리가 가정한 모든 값들이 무조건 맞다고 할 수는 없는 것이니까요. 
- 따라서, 이와 같은 '불확실성'에 대응하기 위해서는 두 가지 정도의 방법이 있습니다. 
    1) 값들 자체에 noise를 섞어서, 다양한 LP에 대한 최적해를 뽑아내고 히스토그램으로 그 변화도를 인지하는 것.
    2) 두번째로는 sensitivity analysis라고 하는, coef가 달라지면 이것이 obj에 얼마나 영향을 미치는지 분석하는 것. 
- 1)의 경우는 그냥 값들 자체에 noise를 넣어서 처리하는 것이므로 굳이 추가할 필요는 없을 것 같고, 여기서는 sensitivity analysis중 하나인 shadow price에 대해서 정리합니다.

## shadow price.

- shadow price는 Constraint의 RHS(Right Hand Side)가 1 증가할 때 obj value가 어떻게 달라지는지를 보여주는
- 코드는 대략 다음과 같습니다. 

```python
import pulp
import numpy as np 

"""
# shadow prices
: Constraint의 RHS(Right Hand Side)가 1 증가할 때, 변화할 때, obj value가 어떻게 달라지는지를 보여주는 것
"""

np.random.seed(0)

# Initialize Class, Define Vars., and Objective
model = pulp.LpProblem(
    name="MODEL1",
    sense=pulp.LpMaximize)
######################################
# Define VARIABLE
vars = pulp.LpVariable.dicts(
    name = 'var', # prefix of each LP var
    indexs = ['A', 'B', 'C'], 
    lowBound = 0, 
    cat = 'Continuous'
)
print(vars)
######################################
# Define OBJECTIVE FUNCTION
coef_dict = {'A':500, 'B':450, 'C':600}
model.objective = pulp.lpSum(
    coef_dict[k]*var for k, var in vars.items()
)
print(model.objective)

######################################
# Define CONSTRAINTS

RHS = [60, 150, 8]
LHS = [
    [6, 5, 8], 
    [10.5, 20, 10], 
    [1, 0, 0]
]
for i in range(0, 3):
    constraint = LHS[i][0]*vars['A'] + LHS[i][1]*vars['B'] + LHS[i][2]*vars['C']<= RHS[i]
    model.constraints[f"const_{i}"] = constraint
# SOLVE it

model.solve()
print(f"Status: {pulp.LpStatus[model.status]}")
print(f"Objective: {pulp.value(model.objective)}")
for v in model.variables():
    print(f"{v.name}: {v.varValue:7.3f}")
print("=="*20)
print("== shadow price")
# shadow price: constraint의 RHS가 1증가할 때, obj가 얼마나 커지는가를 의미함.
# slack: RHS가 얼마나 남아 있는지를 의미함. 따라서, slack이 0이라는 말은 binding, 해당 constraint가 equality라는 것을 의미함. 
for name, c in model.constraints.items():
    shadow_p, slack = c.pi, c.slack 
    print(f"{name} - shadow price: {shadow_p:6.2f}, slack: {slack:6.2f}")
for i in range(0, 3):
    print("=="*30)


```

- 결과는 다음과 같습니다. 

```
{'A': var_A, 'B': var_B, 'C': var_C}
500*var_A + 450*var_B + 600*var_C
Status: Optimal
Objective: 5133.333350000001
var_A:   6.667
var_B:   4.000
var_C:   0.000
========================================
== shadow price
const_0 - shadow price:  78.15, slack:  -0.00
const_1 - shadow price:   2.96, slack:  -0.00
const_2 - shadow price:  -0.00, slack:   1.33
============================================================
============================================================
============================================================
```

## wrap-up

- 결국 애초에, 상황이 달라질 수 있기 때문에, 완벽한 LP 모델은 있을 수 없다. 따라서, 발생할 수 있는 '불확실성'을 알기 위하여, 다양한 상수들에 noise를 섞어서 obj가 어떻게 달라지는지를 파악하고 shadow price와 sensitivty analsys를 통해 불확실성이 미칠 영향을 정확하게 파악하는 것이 중요하다.