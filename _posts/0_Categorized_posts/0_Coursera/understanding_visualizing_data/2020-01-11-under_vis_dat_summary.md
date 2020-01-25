---
title: Coursera) Understanding Visualization Data
category: python-libs
tags: python python-libs coursera
---

## intro. 

- coursera의 수업 중에 [Understanding visualization data](https://www.coursera.org/learn/understanding-visualization-data/home/week/1) 코스를 공부하고 내용을 정리하였습니다. 사실 이 수업보다는 이 다음 수업인 [Inferential Statistical Analysis with Python](https://www.coursera.org/learn/inferential-statistical-analysis-python/home/welcome)를 보기 위해서 훑고 넘어가는 목적이 크고, 그냥 슥슥 봤습니다. 그리고 비교적 내용도 쉬운 편이라서, 어렵지 않았구요. 
- 따라서, 매우 간략하게 내용을 정리하였습니다. 

## WEEK 1 - INTRODUCTION TO DATA

- Data라는 것이 왜 필요하고, 통계의 기법이 현재의 시대에서 왜 중요한지, Data에 대한 기본적인 지표들과 python을 이용해서 Data management를 할 때 어떤 라이브러리들을 쓰고, 어떤 데이터 타입이 있고 등등에 대해서 정리되어 있습니다. 
- 특히, 아무리 빅데이터 시대에 살고 있다고 해도, 내가 수집할 수 있는 데이터에는 한계가 있다(데이터 수집에 필요한 돈이 제한적이므로). 따라서, 현재의 제한적인 데이터로부터, 유의미한 결과를 도출하고, 특히 이 결과가 얼마나 유의미한지를 파악하기 위해서는 통계적 기법을 정확하게 아는 것이 매우 중요하다, 라는 것이 본 코스의 학습목적이죠.

## WEEK 2 - UNIVARIATE DATA

- 여러 칼럼이 있는 경우가 아닌, 하나의 칼럼만 있는 경우(Univariate Data)를 중심으로 데이터의 특성을 파악하는 기본적인 작업을 수행합니다. 주로, boxplot 등 다양한 시각화를 통해서 현재 데이터에 내재되어 있는 특성들을 인지하는 것을 목적으로 하죠. 
- 대부분, scipy, matplotlib, seaborn, pandas, numpy 등을 통해 수행되며, 이미 알고 있던 내용이라서 간략하게 정리하고 넘어간다.

## WEEK 3 - MULTIVARIATE DATA

- Week2와 유사합니다만, 다차원적인 데이터를 대상으로 합니다. 다른 내용보다는 Simpson's paradox를 다시 복기하면서 재밌었습니다. 이 Simpson's paradox가 전체 코스에서 저에게 가장 유용했던 것 같습니다. 결국, 데이터세트가 얼마나 일관적으로 존재하는지, 내가 조절하지 못한 혹은 인지하지 못한 패턴이 데이터세트에 있을 경우, 데이터세트에 따라서 다른 값이 나오게 된다는 것이죠. 
- 이처럼 데이터세트에서 걸러내지 못한, 혼란을 야기하는 변수를 Confounding variable이라고 하며, 이로 인해 심슨의 역설과 같은 문제가 발생하게 됩니다

## WEEK 4 - POPULATIONS AND SAMPLES

- 여기서는 모집단(Population)으로부터 샘플을 어떻게 뽑아야 하는지에 대해서 이야기합니다. 이는 다시 Probability sampling과 non-probability sampling으로 구분되며, 샘플링이 잘 뽑였을 때, 이로부터 어떻게 모집단에 대해서 추론을 할 수 있는지에 대해 정리되어 있죠. 다만, python을 활용해서 이를 어떻게 할지에 대해서는 자세히 나와 있지 않습니다. 아마도 다음 챕터에서 하지 않을까 싶네요.