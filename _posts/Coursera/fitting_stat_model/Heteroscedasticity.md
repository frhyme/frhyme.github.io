---
title: wikipedia - Heteroscedasticity
category: others
tags: GLM statistics
---

## intro. 

- 최근에 기본적인 통계들과 선형방정식을 활용한 다양한 기법들을 정리하고 있습니다. 사실, 뉴럴 넷이 나온 다음부터는 거의 사람들이 언급하지 않는 것이기는 하죠. 뉴럴넷은 어쩌면, 좀 그냥 '돌려보니까 좋았더라, 그냥 막 돌려보고 가장 좋은 것을 고르자'에 가까운 이야기들이니까요. 
- 그런데, 통계에서는 '데이터 자체에 내재되어 있는 문제 혹은 한계'를 좀 더 과학적으로 풀려고 합니다. 가령, 이 데이터는 이 분포를 따른다고 할 수 있는가? 이 데이터는 모두 같은 분포에 속한다고 할 수 있을까? 그렇다면, 이 오차를 줄이기 위해서는 어떤 모델을 쓰는 것이 타당할까? 와 같은, 비교적 탄탄한 백그라운드가 필요하죠. 
- 다시, 머신러닝으로 돌아와서 보면, 

## What is Heteroscedasticity? 

In statistics, a collection of random variables is heteroscedastic (or heteroskedastic;[a] from Ancient Greek hetero “different” and skedasis “dispersion”) if there are sub-populations that have different variabilities from others. Here "variability" could be quantified by the variance or any other measure of statistical dispersion. Thus heteroscedasticity is the absence of homoscedasticity.

The existence of heteroscedasticity is a major concern in the application of regression analysis, including the analysis of variance, as it can invalidate statistical tests of significance that assume that the modelling errors are uncorrelated and uniform—hence that their variances do not vary with the effects being modeled. For instance, while the ordinary least squares estimator is still unbiased in the presence of heteroscedasticity, it is inefficient because the true variance and covariance are underestimated.[2][3] Similarly, in testing for differences between sub-populations using a location test, some standard tests assume that variances within groups are equal.

Because heteroscedasticity concerns expectations of the second moment of the errors, its presence is referred to as misspecification of the second order.[4]