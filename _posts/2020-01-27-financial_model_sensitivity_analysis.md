---
title: Sensitivity Analysis in Financial modeling.
category: others
tags: excel sentivity-analysis 
---

## Two kinds of Sensitivity Analysis.

- LP 분야에서 말하는 Sensitivity Analysis와 Finance modeling 측면에서 말하는 Sensitivity Analysis는 서로 다릅니다. 
- LP(선형계획법)에서는 대상을 선형모델로 표현하고, 최적해를 찾습니다. 하지만, 선형모델에서 가정한 coefficient(목적함수 혹은 Constraint)들이 변할 수 있고, 이처럼 변할 때, 현재의 최적해가 언제까지 유효한지 혹은 최적 값이 어떻게 달라질 수 있는지 등을 찾아보는 것이 LP에서의 Sensitivity Analysis죠. 
- 반대로, Finance modeling에서 말하는 Sensitivity Analysis는 What-if Analysis에 가깝습니다. 일종의 시나리오 플래닝으로서, 시나리오 별로 우리가 관심있는 변수들의 값이 어떻게 변화하는지를 추적하는 것을 말하죠. 
- 가령, 매우 큰 테이블이 하나 있고, 그 테이블의 대부분의 값이 "환율"이라는 값을 참조한다고 합시다. 환율의 기본값은 1.0으로 되어 있다면 0.7이 될 때를 "Worst case"라고 가정하고, 1.3이 될 때를 "Best case" 시나리오라고 가정할 수 있습니다. 이런식으로 다양한 상황에 따라서, 우리가 관심을 가진 변수/지표(interest variable)들이 어떻게 달라지는지를 보는 것이 바로 엑셀에서의 What-if Analysis인 셈이죠. 
- 결국, 두 가지 모두 "불확실성을 조절하기 위해 강건한(Robust) 결론을 도출한다"는 면에서 공통점을 가지고 있기는 합니다.

## What-if Analysis in EXCEL. 

- EXCEL에서는 총 3가지의 What-if Analysis를 제공합니다(데이터 탭 내에 "가상 분석"이라는 이름으로 존재합니다.)
    1) **Scenario Planning**: 여기서 말하는 scenario는 입력 변수(input)의 조합입니다. 즉, "환율", "이자율"과 같이 우리가 관심을 가지는 결과변수(가령 이익)에 영향을 미치는 입력 변수(input)에 대해서 시나리오 별로 값을 다르게 구성하고, 그에 따라 출력 변수(output)이 어떻게 달라지는지를 파악합니다. "요약 보고서"를 통해서 값이 달라질 때 어떻게 되는지 볼 수 있습니다.
    2) **목표 값 찾기**: 수식으로 표현된 B15라는 셀이 있다고 합시다. 그리고 B15는 A15를 참조한다고 하죠. 이 때, B15를 1000과 같은 특정값으로 만들기 위해서는 A15에 어떤 값이 들어가면 되는지, 찾아줍니다. 그리고 당연하지만, X, Y와 같이 2개 이상의 값을 동시에 찾아주지는 못합니다. 그건 해가 여러 개가 될 수 있으니까요.
    3) **DataTable**: 저는 이 기능이 필요하다고 생각하지 않고, 더 헷갈린다고 생각합니다. Scenario planning과 동일하고 더 단순한 기능으로서, 1개 혹은 2개의 입력 변수(input variable)가 변화 할 때, 1개의 output variable이 어떻게 달라지는지를 Table의 형태로 보여줍니다. 그리고, 2개의 입력 변수가 최대죠. 이는 오히려 필요하다면 scenario planning으로 처리하거나 조금 복잡하더라도 참조테이블을 만들고 그 테이블로부터 값을 가져와서 값을 계산해주는 테이블을 각각 만들어서 처리해주면 되는 것 같아요. 즉, 굳이 이 기능을, 심지어 테이블을 만드는 방법 또한 직관적이지 않아서, 필요한지 모르겠네요. 

## wrap-up

- vlookup, match, index 등만 사용해도 처리할 수 있는 수준의 방법입니다. 저는, 마우스로 쿡쿡 눌러서 하는 엑셀보다, 바로 수식으로 입력하는 형태를 선호하기 때문에, 시나리오 플래닝이나 데이터 테이블을 굳이 사용할 것 같지 않습니다. 
- 아 그래도, "목표 값 찾기"는 아마 한번은 사용하지 않을까 싶어요.


## reference

- <https://www.wallstreetprep.com/knowledge/financial-modeling-techniques-selecting-operating-and-financing-scenarios/>

