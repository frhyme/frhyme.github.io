---
title: Algorithm - dynamic programming - basic
category: algorithm 
tags: python algorithm dynamic-programming codefight recursion

---

## intro

- dynamic programming은 음...일단은 'recursion'이라고 생각해도 상관없다. 이전에 계산한 값을 가지고, 이후의 값을 계산할 수 있는 것을 의미하는데, 쉽게는 fibonacci가 이 경우에 포함된다. 
	- knapsack problem도 여기에 포함되고. 
	- 물론 개념은 간단하지만, 전체 문제가 무엇이고, subproblem이 무엇인지를 정의하는 것이 어렵다.
	- 더 말하고 싶은 것들이 많고, 추가되어야 할 것들도 많지만, 지식이 얕기 때문에 일단은 이쯤에서 마무리를....
- 예를 가지고 설명하는 것이 더 좋을 것 같으므로 바로 문제를 풀어보는 게 좋을 것 같다. 

- 아무튼, 아주 간단한 문제를 풀어봅시당. 

## climbingStair(n)

### Problem

- n 개의 계단이 있을 때, 사람은 1칸 씩 오르거나, 2칸씩 오를 수 있다. 계단을 올라갈 수 있는 방법의 수는 몇 가지인가? 라는 문제를 풀어보자. 
	- 예를 들어서, 3개의 계단이 있을 경우, (1,1,1), (2,1), (1,2) 라는 세 가지 조합이 나올 수 있습니다. 따라서 3을 리턴하면 됩니다.
- 그래서, 이게 다이나믹 프로그래밍과 무슨 관련이 있죠? 라는 생각이 들 수도 있을텐데요, 앞서 말한 것처럼 이전에 계산한 값을 이용해서 이후의 값을 계산할 수 있는 것을 다이나믹 프로그래밍이라고 합니다. 
- 이 문제의 경우는 다음처럼 쪼갤 수 있죠. 
	1. n==1: 1 가지
	2. n==2: 2 가지, (1,1), (2)
	3. n==k: 
		- 2 칸을 올랐을 경우, k-2칸을 더 오르면 되고
		- 1 칸을 올랐을 경우, k-1칸을 더 오르면 된다. 
- 너무 recursive하지 않나요. 그래서 다음 처럼 아주 간단하게 recursive로 표현할 수 있습니다. 
	- 단 python에서는 tail-recursion optimization을 지원하지 않기 때문에, 이렇게만 할 경우 연산속도가 느려질 수 있습니다. 
- n 이 적을때는 문제가 없지만, n이 증가하면, 점점 익스포넨셜하게 증가합니다. 
	- n 이 35 일 때, 
		- recursive: 3.642163038253784
		- iterative: 0.00024890899658203125
		
- 그래서 iterative한 형태로 바꿔줍니다. 

#### climbingStairs - recursive

```python
def climbingStairs_recursive(n):
    if n==1:
        return 1
    elif n==2:
        return 2
    else:
        return climbingStairs_recursive(n-1)+climbingStairs_recursive(n-2)
```

#### climbingStairs - iterative

```python
def climbingStairs_iterative(n):
    new_dict = {1:1, 2:2}
    def aaa(k):
        if k in new_dict.keys():
            return new_dict[k]
        else:
            return aaa(k-2)+aaa(k-1)
    for i in range(1, n+1):
        new_dict[i]=aaa(i)
    return new_dict[n]
```
