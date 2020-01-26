---
title: Optimization in python with pulp - Basic.
category: python-libs
tags: python python-libs gurobi LP linearprogramming optimization pulp
---

## python으로 선형 계획법 문제를 풀어 봅시다. 

- [pulp](https://www.coin-or.org/PuLP/index.html)라는 python에서 linear programming을 할 수 있는 라이브러리를 정리합니다. 우선, 본격적으로 최적화 문제를 풀어야 한다면, 즉, 변수들의 수가 엄청나게 많고 복잡하다면, 그냥 cplex를 사시거나 아니면 gurobi를 사서 풀어보는 것이 더 좋을 수 있습니다. 비교적 pulp의 문서화는 좀 부족하거든요. 
- 아무튼, 일단 설치부터 합시다. 

```
pip install pulp
```

## solve the simple problem

- modeling이라는 것은 "현실에서의 문제에서 중요하게 고려하는 부분을 선정하여, 특정한 형태로 변경하는 것"을 말하죠. LP modeling 또한, 주어진 문제를 어떻게 잘 정의하는가, 로부터 출발합니다. 사실 가장 중요한 부분이죠. 주어진 LP 문제가 얼마나 현실을 설득력 있게 대표하는가? 가 제일 중요하지만, 그 부분은 본 포스트의 범위를 넘어가므로 제외합니다. 
- 우리는, LP 문제가 완벽하게 주어졌고, 그걸 pulp에게 어떻게 잘 전달하여, 최적해를 찾을 것인가? 로 넘어갈 거에요. 
- 아래의 코드로 비교적 간단하게 LP 문제를 풀고 최적해를 찾습니다. 

```python
import pulp

# LpProblem:
# Problem은 variable, constraints, objective function까지 모두 고려한 것이 Problem이 된다. 즉, 
# sense: pulp.LpMaximize or pulp.LpMinimize(default)
LPmodel_simple = pulp.LpProblem(
    name="simple program", 
    sense=pulp.LpMaximize 
)
############################################
# DEFINE decision variable 
# cat: category, "Continuous"(default), "Integer", "Binary"
X1 = pulp.LpVariable(
    name='X1', lowBound=None, upBound=None, cat='Continuous'
)
X2 = pulp.LpVariable(
    name='X2', lowBound=None, upBound=None, cat='Integer'
)

############################################
# Define OBJECTIVE function
LPmodel_simple.objective = 10*X1 + 20*X2
print(LPmodel_simple.objective)
############################################
# Define CONSTRAINTS
# pythonic하게 생각하면, 아래 list에 있는 값들이 모두 logical value처럼 보이겠지만
# 아래 형태의 유형은 <class 'pulp.pulp.LpConstraint'> 이다. 
constraints = [
    X1 + X2 <= 100, 
    2.0 * X1 - X2 >=10
]
#print(type(constraints[0]))
# LPmodel.constraints 는 <class 'collections.OrderedDict'>
# 따라서, 아래처럼 key, value의 형태로 넘겨줌. 
#print(type(LPmodel.constraints))
for i, c in enumerate(constraints):
    constraint_name = f"const_{i}"
    LPmodel_simple.constraints[constraint_name] = c
#print(LPmodel.Lpconstraint)
############################################
# SOLVE model
LPmodel_simple.solve()

# 결과를 출력합니다.
for v in LPmodel_simple.variables():
    print(f"Produce {v.varValue:5.1f} Cake {v}")
```

```
10*X1 + 20*X2
Produce  37.0 Cake X1
Produce  63.0 Cake X2
```

## solve the complex problem

- 그냥 toy problem으로서 변수가 10개 가 안되는 위와 같은 문제들은 그냥 이렇게 풀어내면 됩니다. 
- 하지만, 복잡해질 경우, 가령, variable이 100개가 넘는다고만 해도, 위처럼 variable 과 constraint를 만들어주는 것은 힘들어지죠. 
- 따라서, 조금 더 복잡해지는 경우에는 다음과 같이 프로그래밍하여 문제를 풀어야 합니다.

```python
print("== for COMPLEX model")
LPmodel_complex = pulp.LpProblem(
    name="Complex_problem", 
    sense=pulp.LpMaximize 
)
############################################
# Define VARIABLE
# 기존에는 각 변수를 한번에 하나씩만 만들었지만, 아래와 같이 dictionary로 변수들을 한번에 만들 수도있음. 
# 또한, constraint에서도 이 딕셔너리에 key로 접근하여 변수들의 제한사항을 입력해줘야 함.
# 또한, var이 많아지면, 아래와 같이 dict로 한꺼번에 만들수도있음. 
vars = pulp.LpVariable.dicts(
    name = 'var', # prefix of each LP var
    indexs = ['A', 'B'], 
    lowBound = 0, 
    cat = 'Continuous'
)
print(vars)
############################################
# Define OBJECTIVE function
# 이 때는 pulp.lpSum을 사용해서 비교적 간단하게 처리할 수도 있음. 
coef = [20, 40]
LPmodel_complex.objective = pulp.lpSum(
    c*v for c, v in zip(coef, vars.values())
)
print(LPmodel_complex.objective)

# 앞에서 variable을 dictionary를 사용해서 만들어줬으므로, 여기서도 key로 접근하여 constrain를 작성해줘야 함.
constraints = [
    1 * vars['A'] + 1 * vars['B'] <= 100, 
    2.0 * vars['A'] - 1.0 * vars['B'] >= 10
]
for i, c in enumerate(constraints):
    constraint_name = f"const_{i}"
    LPmodel_complex.constraints[constraint_name] = c

LPmodel_complex.solve()
# 잘 풀렸는지 확인, infeasible 등이 없는지 확인할 것. 
print("Status:", pulp.LpStatus[LPmodel_complex.status])

for v in LPmodel_complex.variables():
    print(f"Produce {v.varValue:5.1f} Cake {v}")
```

```
== for COMPLEX model
{'A': var_A, 'B': var_B}
20*var_A + 40*var_B
Status: Optimal
Produce  36.7 Cake var_A
Produce  63.3 Cake var_B
```

## wrap-up

- 오늘은 python에서 선형계획법, linear programming을 풀기 위해 필요한 `pulp`를 사용하여, 간단한 선형계획법을 풀어봤습니다.

## reference

- <https://www.coin-or.org/PuLP/index.html>