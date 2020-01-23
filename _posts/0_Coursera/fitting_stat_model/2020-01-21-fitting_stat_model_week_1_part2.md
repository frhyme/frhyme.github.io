---
title: Fitting Statistical Models to Data with Python - WEEK 1 - Part 2
category: python-libs
tags: python python-libs coursera statsmodel statistics
---

## Data Modeling in Python

- 일반적으로, 데이터에 대해 통계적 모델을 세운다는 것은 다음과 같은 과정에 따라서 진행된다.
    1. varaible이 가지는 분포에 대한 성질(mean, variance, covariance)를 유추(estimate)하고, 
    2. variable들간에 내재되어 있는 관계(relationship)를 추론하고, 
    3. 다른 prediction variable을 통해, 우리가 관심있는 variable의 값을 예측하는 것. 
- 1, 2가 보통 현재의 머신러닝 학습들에서 무시되는 내용들이죠. 물론, 뉴럴넷이 워낙 잘해주고, 무시할만 하니까 무시해주는 것이기는 합니다만 호호.

### Modeling Structure. 

- 특히 선형 방정식 모델에서, 모델링을 한다는 것은 '무엇(X)으로 무엇(Y)를 예측할 것인가'를 결정한다는 것이며, 이 X, Y는 각각 다음과 같은 다른 이름들을 가지기도 한다. 
    - `X`: predictor variable, covariates, regressors, exogeneous variable
    - `Y`: outcome, response, endogeneous variables, variables of interest

## wrap-up

- 그 외로는, Exploratory Data Analysis에 대한 내용이 있다. 가령 seaborn을 이용하여 heatmap을 그려보는 것, scatter plot을 통해 데이터의 분산이나 평균이 어떻게 변화하는지 보는 것등이 있다.
- 딱히, 특별한 내용이 있다고 생각되지 않아서 넘어갔다.