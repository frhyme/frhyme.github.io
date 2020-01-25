---
title: What is a link function?
category: others
tags: GLM statistics
---

## What is a link function? 

- link function은 Generalized linear model(GLM)에서 사용되는 함수로, linear model에서 만들어진 결과를 우리가 필요한 response로 변경해주는 것을 말합니다. 네, 이렇게 마ㅏㄹ하니까 무슨 말인지 모르겠죠? 
- 우선, OLS(Ordinary Least Square)와 같은 모델은 기본적으로 `y = ax1 + bx2`의 형태를 가정합니다. 그리고, 여기에는 `y`라는 response variable도 다른 변수들과 마찬가지로 normal distribtuion을 따른다는 것을 가정하죠. 
- 그런데, 우리가 실제로 마주치는 많은 문제들, 종속 변수들은 모두 normal distribution을 따른다고 할 수 없어요. 가령, clasisfication 문제를 예로 들어보면, 이 때 y는 normal distribution이 아니잖아요. 따라서, 선형방정식을 통해서 이런 값을 예측하기 위해서는 다른 형태의 함수가 필요합니다. 즉, 이 둘 사이를 이어주는 것이 바로 link function이죠.
- 개념적으로는 이렇습니다. 조금 더 자세한 설명은 [What is a link function? ](https://support.minitab.com/en-us/minitab/19/help-and-how-to/modeling-statistics/regression/supporting-topics/logistic-regression/link-function/)에서 보시면 도움이 될 것 같습니다.


## reference

<https://support.minitab.com/en-us/minitab/19/help-and-how-to/modeling-statistics/regression/supporting-topics/logistic-regression/link-function/>