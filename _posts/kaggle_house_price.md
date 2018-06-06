---
title: kaggle) 집 가격을 예측해 봅시다. 
category: machine-learning
tags: kaggle machine-learning python python-lib sklearn

---

## kaggle) 집 가격을 잘 예측해봅시다. 

- 이 문제는 간단히 말하면, regression 문제네요. 이전에 풀어본 mnist, titanic의 경우는 classification의 문제에 속했는데, 이 문제는 regression 문제입니다. 
- 다 좋은데, 대략 data를 보면, 너무 다양한 column이 있습니다. categorical, numerical data가 섞여 있는데, 이 중에서 어느 놈이 유의미한지 찾는 것이 이번 kaggle의 핵심이 되겠네요. 또한, 이 feature들을 잘 조합하여, 새로운 feature를 뽑아내는 것들, **feature engineering**이 가장 중요한 것 같습니다. 
- 이번에는 하나씩, 칼럼을 하나씩 늘려가면서, 잘 맞추는지를 보려고 합니다. 제가 성격이 급해서 그걸 잘할 수 있을지 잘 모르겠지만 아무튼!

## data preprocessing 

- 기본적인 data 전처리 작업을 수행합니다. 일반적으로 수행하는 작업은 다음과 같습니다. 
    - resolving skewness 
    - handling missing values

## feature engineering...

- SalePrice를 예측해야 하는데, 이 값의 분포를 보면, 

- 일단 numeric column과 non numeric column으로 나누고, 값으로 saleprice를 추정할 수 있는지를 보고, 
- categorical value 별로 그룹 한 결과가, 개별 그룹당 샘플사이즈가 유의미하고, 그룹별 평균간의 차이가 크면 이를 pd.get_dummies로 넣음. 


categorical feature가 target 변수의 차이에 얼마나 관여하는가 를 어떻게 측정할 수 있을까? 


## y predicted weighted mean

- 총 10개의 model의 상위8개의 `r2_score`가 0.88이상 입니다. 이들의 weighted_mean을 구하면 정확도가 더 올라갈 수 있지 않을까요? 


## refernce

- <https://www.kaggle.com/c/house-prices-advanced-regression-techniques>
- <https://www.kaggle.com/pmarcelino/comprehensive-data-exploration-with-python>
- <https://www.kaggle.com/dansbecker/your-first-scikit-learn-model>
- <https://www.kaggle.com/serigne/stacked-regressions-top-4-on-leaderboard>