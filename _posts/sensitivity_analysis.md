---
title: Sensitivity Analysis - 민감도 분석. 
category: others
tags: 
---

## Background

### Linear Programming. 

- "선형계획법(Linear Programming)"은 대상을 모델링할 때, 선형적인 관계로 모델링하는 것을 말한다. 
- 가령 다음과 같은 식이 있다고 하자. 아래 두 식은 X1, X2에 대한 범위를 설명하고 있으며, "주어진 조건"이라고 말해도 된다.
    - X1 + X2 <= 50
    - x1 + 2*X2 <= 100
    - X1 > 0 
    - X2 > 0 
- 그리고 이 때, 현재의 조건 하에서, 가장 최적의 해를 찾고 싶다. 우리는 여기서 "최적"을 X1+X2라고 정의한다. 즉, 두 변수의 합이 최대가 되는 곳을 찾고 싶다. 

### Sensitivity Analysis 

- 한국말로는 "민감도/감응도 분석"이라고 하는 것은, 다른 말로 사후 최적 분석(post optimality analysis)이라고 부르기도 한다. 즉, 이미 "최적해가 구해진 상태에서" 다른 조건들이 변경될 경우(가령, X1의 범위가 감소하거나 증가하거나 와 같은) "최적해에 어떠한 변화가 발생하게 되는지"를 파악하는 것을 Sensitivity Analysis라고 한다. 
- 가령, 우리는 "환율이 1000원과 1500원 사이일때를 가정하고 최적해를 찾았다" 그런데, 환율이 2000원까지 움직인다고 하면, 이럴 때, 최적해는 얼마나 달라지는지? 를 우리는 알고 싶어 하게 된다.

- 따라서, 이를 알기 위해서는 우선 최적해를 우선 찾아야 한다. 그리고 그때에 다른 변화를 파악하는 것이 있음. 

## scratch. 

- 민감도 분석(Sensitivity Analysis)는 일종의 불확실성에 대응하기 위한 방법으로, 초기에 세웠던 가정(가령 환율이 1000원일 것이다)이 달라진다면(가령 환율이 1100원이 될것이다), 그때 우리가 고려하는 변수(매출)에 어떤 영향을 미칠 것인지를 검증하는 것을 말한다. 
- 즉, "환율"이라는 변수가 "매출"이라는 변수에 얼마나 민감하게 영향을 미치는가? 를 보기 위한 것. 
- 이렇게 쓰고 나니, 약간 시나리오 플래닝, 시뮬레이션 기법과도 유사하게 느껴지는데 흠. 


- 즉, "민감도 분석"은 "What if"라는 질문을 던진다. 다음과 같은 What if가 있을 수 있다. 
    - 환율이 10% 증가한다면? 
    - 노동자들의 임금이 25% 증가한다면?
    - 기계가 고장나서, 일일 생산량이 감소한다면? 
- 즉, 이러한 what if가 발생할 때, 이것이 우리가 관심있어 하는 목적 변수(매출 등)에 어떤 영향을 미치게 되는지를 파악하는 것을 "민감도 분석"이라고 한다. 
- 이는 쉽게 "시뮬레이션"이라고 말할 수도 있다. 따라서, 우리가 시뮬레이션 시에 세운 가정들이 적합하다 혹은 유효하다는 가정에서 출발한다. 즉 "가정" 자체가 유효하지 않다면 시뮬레이션의 결과에 의미가 없다는 이야기. 


## cover

- LP에서 말하는 민감도 분석(sensitivity analysis)와 약간, 시나리오 플래닝 분야에서 말하는 sensitivity analysis가 조금 다르게 느껴짐. 아님. 똑같은데, 단지 형식이 조금 달라서 그렇게 느껴지는 것 뿐임. 
- 아무튼, 동일하게, "obj formula"를 세우고, obj formula를 구성하는 각 요소들에 대해서 constraint를 정의함. 이렇게 했을 경우, 현재 조건 내에서, 최적의 값을 찾아낼 수 있음.
- 그리고, 이 때, 다른 변수들이 변화하면 목적함수가 어느 정도 달라지는지를 파악하는 것이 sensitivity analysis임. 
- 아마, 참고한 다른 엑셀에서 arr_constrain 등이 있었던 것이 아마도, 매트릭스 형태로 값을 넘겨주기 때문인 것으로 보임. 


## reference

- [simplex method](https://blog.naver.com/ksj8406/221431564032)
- <https://rectamoptionem.com/2015/02/05/%EB%AF%BC%EA%B0%90%EB%8F%84-%EB%B6%84%EC%84%9D/>