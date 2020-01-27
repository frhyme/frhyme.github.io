---
title: Optimization in python with cvxpy
category: python-libs
tags: python python-libs gurobi LP linearprogramming optimization
---

## Optimization.

- 요즘 대부분의 사람들은 '머신러닝'에 꽂혀 있지만, 그 외로 최적화(Optimization)이라는 분야가 있죠. 일반적으로, 주어진 제한조건(constraint)들 내에서, 우리가 목적으로 하는 함수(objective function)를 최대화하기 위해서는, 각 변수를 어떤 값으로 설정해야 하는가, 와 같은 문제를 풀고, Linear programming, Quadratic programming, Integer programming들이 있죠. 그리고, 사실 머신러닝 모델을 만드는 것 또한, 가령 '오차'를 최소화하는 상수를 찾는 다는 점에서 보면 최적화 문제와 동일합니다. 
- 문제를 모델링하는 측면에서는 위와 같이 LP, QP, IP등이 있고 문제들은 Network, Scheduling, knapasack 등 흔히, 알고리즘에 속하는 문제들이 여기에 많이 포진되어 있습니다. 
- 아무튼 이 분야의 문제들을 풀려면 가장 유명하고, 제일 잘 풀어주는 cplex, gurobi 그리고 python 패키지인 scipy도 이 부분을 지원하는데, 일단 오늘은 `cvxpy`라는 라이브러리를 가져옵니다(원래는 `Pulp`라는 라이브러리를 사용하려고 했는데, 이 아이는 documentation이 별로 좋지 않은 것 같아서 일단 넘깁니다). 

## CVXPY

- [CVXPY](https://www.cvxpy.org/tutorial/intro/index.html)는 convex optimization 문제를 풀기 위한 python-embedded modeling language라고 합니다. 다른 것보다, [convex optimization](http://sanghyukchun.github.io/63/)은 최적화 문제들 중 한 형태를 말하는데요, 다음 그림을 보면 무엇인지 감이 옵니다. 

![](https://www.researchgate.net/profile/Jennifer_Rexford/publication/226717592/figure/fig4/AS:302225588015118@1449067603956/Convex-and-nonconvex-functions-A-function-g-is-a-convex-function-if-domain-of-g-is-a.png)

- 단적으로 말하면, convex는 유일한 극점이 존재하여, 머신러닝과 같은 모델에서 gradient-descent method 등으로 해를 찾을 수 있는 경우를 말하고, non-convex는 극점이 여러개 존재하여, 해를 찾기 어려운 경우를 말합니다. 좀 더 명확한 정의가 필요하다면 [이 글](http://sanghyukchun.github.io/63/)을 보시면 도움이 될 것 같습니다.
- 그리고, 일단은 그냥 "파이썬 내에서 최적화 문제를 풀기 위한 라이브러리"라고 생각하셔도 문제가 없습니다. 
- 일단은 설치부터 해보죠. 

```
pip install cvxpy
```

## Basic usage of it. 

- [cvxpy - documentation](https://www.cvxpy.org/tutorial/intro/index.html#changing-the-problem)에서 제공하는 가장 간단한 문제를 다음과 같이 풀어봅니다. 
- 그냥 '이런 것을 할 수 있다'를 보이기 위해서 다음의 코드를 작성하였으나, 실제로 현장에서 발생하는 문제들에서는 훨씬 많은 변수들이 들어가게 됩니다. 즉, 현재 코드에서오 같이 symbolic expression으로 처리하지 못하고, matrix의 형태로 표현하는 것이 필요하겠죠. 당연하지만, 그 부분도 여기서 지원합니다. 

```python
import cvxpy as cp 

# 최적화 문제에서 고려되어야 하는 변수들을 정의해줍니다.
# integer programming 경우에는 아래와 같이 parameter를 설정해줌.
x1 = cp.Variable(integer=True)
x2 = cp.Variable(integer=True)

# 제한 조건들을 정의합니다
constraints = [
    x1 >= 0, 
    x2 >= 0, 
    x1 + x2 == 100,
    x1 - x2 >= 1
]

# 목적함수와 최대/최소를 정의합니다.
obj = cp.Minimize((x1 - x2)**2)

# Form and solve problem.
prob = cp.Problem(obj, constraints)
prob.solve()  # Returns the optimal value.
print("=="*20)
if prob.status=='optimal':
    print(f"status: {prob.status}") # 만약 infeasible이거나, 문제가 있을 경우 여기서 알 수 있음.
    print("optimal value", prob.value)
    print("optimal var", x1.value, x2.value)
else:
    print(f"Wrong status: {prob.status}")
print("=="*20)
```

- 코드 실행 결과는 다음과 같습니다. 

```
========================================
status: optimal
optimal value 3.9999996830743783
optimal var 51.000000028191366 48.999999971893374
========================================
```

## wrap-up

- 사실, 조금 더 알아보려고 했지만, cvxpy는 scipy에서 제공하는 optimize와 거의 동일하죠. 현재 저는 보다 전통적인 LP 분야의 테크닉들을 알아보고 있는 상황이며, 현재 제가 원하는 방향과 조금 달라서, 이 정도로만 정리하였습니다. 


## reference

- <https://datascienceschool.net/view-notebook/0fca28c71c13460fb7168ee2adb9a8be/>