---
title: Fitting Statistical Models to Data with Python - WEEK 3 - part 2
category: python-libs
tags: python python-libs coursera statsmodels statistics
---

## Fitting a Marginal Model.

- Multilevel Model) Part1에서는 같은 피실험자(사람, 아이)에 대해서 오랜동안 관측한 데이터간의 correlation을 고려하여, 나이에 따른 random effect가 다를 것이라를 전제로, 해당 paremeter를 추정하는 식으로 진행됩니다. 
- 본 part에서 설명하는 marginal model도 동일하게 correlation을 반영하지만, 여기서는 GEE라는 모델로, 각 클래스 내의 correlation 구조를 주입하는 식으로 모델링됩니다. 아래의 설명을 들으면 좀 더 명확해질 것으로 생각되는데요.
- 본 파트에서는 같은 class 내의 observiation들 간의 분포 특성을 다음과 같은 종류로 선언합니다.
    - 첫번째는 exchangeable model이며, 여기서는 한명의 child(즉, class) 내의 모든 관측이 동일한 correlation, variance를 가지게 된다. 
    - 두번째의 covariance structure에서는 서로 independence를 가정하며, 여기서는 이 같은 child(cluster)의 관측이라도 서로 독립적인, 즉, 0의 correlation을 가진다고 가정한다.
- 따라서, 이 두 모델이 클래스별로 서로 다른 가정을 가졌다고 가정하고 이를 바탕으로 모델을 수립합니다. 
- 또한, 여기서, 만약 `age` 변수가 uniform하게 분포되어 있다면(즉, 모든 아이들의 측정이 같은 주기로 수행되었ㄷ면, autoregressive model을 집어넣어서, 이전의 값에 영향을 받도록 설계할 수 있습니다. 다만, 본 데이터는 그러한 형태로 구성된 것이 아니므로, 제외합니다. 이를 위해서는 `cov_struct = sm.cov_struct.Autoregressive()`를 변수로 전달해주면 됩니다.

```python
GEE = True
if GEE==True:
    # Fit the exchangable covariance GEE
    model_exch = sm.GEE.from_formula(
        formula = "vsae ~ age * C(sicdegp)",
        groups="childid",
        cov_struct=sm.cov_struct.Exchangeable(), 
        data=autism_df
        ).fit()
    print("== model cov exchangeable")
    print(model_exch.summary())
    print("=="*30)
    # Fit the independent covariance GEE
    model_indep = sm.GEE.from_formula(
        "vsae ~ age * C(sicdegp)",
        groups="childid",
        cov_struct = sm.cov_struct.Independence(), 
        data=autism_df
        ).fit()
    print(model_indep.summary())
    print("=="*30)
```

- 결과는 다음과 같죠. 

```
== model cov exchangeable
                               GEE Regression Results
===================================================================================
Dep. Variable:                        vsae   No. Observations:                  610
Model:                                 GEE   No. clusters:                      158
Method:                        Generalized   Min. cluster size:                   1
                      Estimating Equations   Max. cluster size:                   5
Family:                           Gaussian   Mean cluster size:                 3.9
Dependence structure:         Exchangeable   Num. iterations:                     6
Date:                     Mon, 20 Jan 2020   Scale:                         544.421
Covariance type:                    robust   Time:                         16:23:13
=======================================================================================
                          coef    std err          z      P>|z|      [0.025      0.975]
---------------------------------------------------------------------------------------
Intercept              17.5932      1.994      8.824      0.000      13.685      21.501
C(sicdegp)[T.2]         5.6402      2.950      1.912      0.056      -0.142      11.422
C(sicdegp)[T.3]        22.6497      3.554      6.373      0.000      15.684      29.616
age                     2.5989      0.512      5.076      0.000       1.595       3.603
age:C(sicdegp)[T.2]     1.4736      0.782      1.884      0.060      -0.059       3.006
age:C(sicdegp)[T.3]     4.4762      0.884      5.065      0.000       2.744       6.208
==============================================================================
Skew:                          2.1896   Kurtosis:                       8.6987
Centered skew:                 0.8490   Centered kurtosis:              4.8089
==============================================================================
============================================================
== model cov independence
                               GEE Regression Results
===================================================================================
Dep. Variable:                        vsae   No. Observations:                  610
Model:                                 GEE   No. clusters:                      158
Method:                        Generalized   Min. cluster size:                   1
                      Estimating Equations   Max. cluster size:                   5
Family:                           Gaussian   Mean cluster size:                 3.9
Dependence structure:         Independence   Num. iterations:                     2
Date:                     Mon, 20 Jan 2020   Scale:                         544.193
Covariance type:                    robust   Time:                         16:23:14
=======================================================================================
                          coef    std err          z      P>|z|      [0.025      0.975]
---------------------------------------------------------------------------------------
Intercept              17.4211      1.908      9.131      0.000      13.682      21.160
C(sicdegp)[T.2]         6.3593      2.883      2.206      0.027       0.708      12.010
C(sicdegp)[T.3]        23.4032      3.454      6.776      0.000      16.634      30.173
age                     2.5989      0.512      5.076      0.000       1.595       3.603
age:C(sicdegp)[T.2]     1.4736      0.782      1.884      0.060      -0.059       3.006
age:C(sicdegp)[T.3]     4.4762      0.884      5.065      0.000       2.744       6.208
==============================================================================
Skew:                          2.1805   Kurtosis:                       8.6849
Centered skew:                 0.8490   Centered kurtosis:              4.8089
==============================================================================
```

## wrap-up

- 이전에 multi level model로 제시된 `Mixed Linear Model`에서는 보통, 각 클래스들별로 random effect가 다르게 적용된다고 합니다. 따라서 아래와 같이, `random effect`를 의미하는 formula를 따로 넘겨주죠. 즉, noise를 구분하여, 설명가능하게 만들어주는 것이죠. 

```python
mlm_mod = sm.MixedLM.from_formula(
    formula = 'vsae ~ age * C(sicdegp)', 
    groups = 'childid', 
    re_formula="1 + age", 
    data=autism_df
)
```

- 다만, GEE의 경우는 이처럼 random effect의 값을 추정하지 않습니다. 그냥, 아래와 같이, `cov_struct`간의 관계를 주입하죠.
    - `exchangeable`: 같은 class 내의 관측들이 동일한 correlation, variance를 가진다. 
    - `independence`: 같은 class 내의 관측들이 서로 독립적이다. 
    - `autoregressive`: 이전의 관측에 영향을 받는, 자기 공선성을 가진다.
- 즉, 값을 추정하는 것이 아니라, "이 아이들은 이러한 관계를 가질것이다"라고, 추정하면서 진행된다는 차이가 있습니다.

```python
model_exch = sm.GEE.from_formula(
        formula = "vsae ~ age * C(sicdegp)",
        groups="childid",
        cov_struct=sm.cov_struct.Exchangeable(), 
        data=autism_df
    ).fit()
```