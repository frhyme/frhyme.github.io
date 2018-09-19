---
title: python에서 genetic algorithm 사용하기
category: python-lib
tags: python python-libs genetic-algorithm optimization numpy 
---

## intro

- Genetic algorithm에 대해서 예전에 수업때 사용해본적도 있고 했지만, 다시 한번 공부해보기로 했습니다. 
- 또 예전에 C++로 코딩할 때와 다르게 python으로 코딩하면서 부터는, 알고리즘을 구현하는 것이 상대적으로 쉬워서, 다시 한번 사용해보고 정리해보기로 했습니다. 

## genetic algorithm?? 

- 그냥 '적자생존'을 말하는 최적화 기법, 정확히는 메타휴리스틱 입니다. 
- 아래 그림에서 보시는 것처럼 
    - 해당 문제에 대해서 가능한 초기 솔루션들을 세팅하고 
    - 평가하여 특정 기준을 충족하는 솔루션들만 남기고
    - crossover(두 유전자끼리 교배하여 새로운 솔루션 생성), mutation(기존 유전자 변형)을 활용하여 새로운 솔루션들을 생성하고 
    - 이를 반복하는 것
- 을 말합니다. 

![](https://cdn-images-1.medium.com/max/1600/1*HP8JVxlJtOv14rGLJfXEzA.png)

- 반드시 optimality를 보장해준다고 할 수는 없지만, 꽤 빠른 시간 내에 근접해를 찾아주기는 하니까요. 랜덤성을 적절히 활용해서 프로블럼 스페이스를 줄인 형태로 보시면 될것 같습니다. 

## tutorial 1

- 이 블로그(https://towardsdatascience.com/genetic-algorithm-implementation-in-python-5ab67bb124a6)의 내용을 진행했습니다. 
- 간단하게 objective function을 정하고, 잘하는 솔루션을 남기고, crossover, mutation을 만들어서 돌렸습니다. 

```python
import numpy as np 

def calculate_fitness(solution):
    return np.array(solution).dot(parameters)

parameters = np.array([4,-2,3.5,5,-11,-4.7])

## initializae solution pool 
current_solution_pool = [list(np.random.normal(0, 1, 6)) for i in range(0, 8)]

for i in range(0, 10):
    ## 현재 솔루션 중에서 가장 성과가 좋은 놈만 남기고 모두 버림 
    new_parents = sorted(current_solution_pool, key=calculate_fitness, reverse=True)[:4]
    print(f"optimal fitness in {i:0>2d} generation: {calculate_fitness(new_parents[0])}")
    ## 간단하게 크로스오버 세팅
    crossovers = [
        new_parents[0][:3]+new_parents[1][3:],
        new_parents[1][:3]+new_parents[0][3:],
    ]
    ## 뮤테이션 세팅 
    mutations = [
        list(np.array(new_parents[0])+np.random.normal(0, 1, 6)), 
        list(np.array(new_parents[0])+np.random.normal(0, 1, 6)),
    ]
    current_solution_pool = new_parents + crossovers + mutations 

```

```
optimal fitness in 00 generation: 16.114142824605693
optimal fitness in 01 generation: 20.34874446758479
optimal fitness in 02 generation: 20.34874446758479
optimal fitness in 03 generation: 28.49241685227758
optimal fitness in 04 generation: 30.992930681221885
optimal fitness in 05 generation: 33.93284270330889
optimal fitness in 06 generation: 33.93284270330889
optimal fitness in 07 generation: 51.41840381571125
optimal fitness in 08 generation: 69.02581331815482
optimal fitness in 09 generation: 75.52541422895794
```

## reference

- <https://towardsdatascience.com/genetic-algorithm-implementation-in-python-5ab67bb124a6>