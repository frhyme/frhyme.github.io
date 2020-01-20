---
title: Fitting Statistical Models to Data with Python - WEEK 3 - part 1
category: python-libs
tags: python python-libs coursera statsmodels statistics
---

## Fitting a multilevel Model 

- 본 주차에서는 자폐증(autism)을 가진 아이들을 대상으로 수행된 longitudinal study를 대상으로 데이터를 분석한다. 주로 다음의 변수들을 분석한다. 
    - `AGE`: "피실험자들의 나이", 2살과 13살의 사이로 구성됨.
    - `VSAE`: "피실험자들의 사회화(socialization)" 정도를 말하며, 이것이 우리가 예측하려고 하는 Outcome이 됩니다.
    - `SICDEGP`: "1과 3사이의 값을 가지는 2세 때 expressive language group", 높을수록, 더 풍부한 언어(expressive language)를 사용함을 말함.
    - `CHILDID`: "피실험자를 식별할 수 있는 식별자"
- 본 실험에서는 같은 피실험자(아이)를 대상으로 반복적인 측정을 하였으므로, children별로 random effect가 존재함. 따라서, 이를 반영한 multilevel model을 설계하여 parameter를 fitting함.
- 해당 [데이터는 이 링크를 통해서 다운](http://www.umich.edu/~kwelch/workshops/sasgraph/autism.csv)받을 수 있습니다.

## Why Mixed Linear Model

- Mixed Linear Model은 Outcome 변수들이 서로 독립적이지 않고, 관련이 있을때 사용합니다. 
- 기본적인 Linear Model은 각 outcome들이 모두 독립적이라고 생각합니다. 하지만, 본 실험에서 예측하려고 사용하는 데이터들은 각 피실험자를 대상으로 동일한 측정을 통해서 여러번 반복된 결과이며, 따라서, 각 실험자들별로 데이터의 분포가 다르다는 특징이 있죠. 
    - 가령, 피실험자1이 가지고 있는 데이터의 분포와, 피실험자2가 가지고 있는 데이터의 분포는 다릅니다. 이 데이터의 분포 혹은 서로 다른 데이터의 변동 폭을 반영하지 않고, 그대로 그냥 Linear Model을 구축할 경우에는 정확도가 떨어지게 되겠죠. 
- 즉, 이처럼 outcome들간에 연관이 되어 있을 경우에는 이에 따른 변동폭을 outcome별로 다르게 적용할 수 있습니다. 이 때 적용되는 변동 폭을 보통 random effect라고 부르죠. 그리고, 이를 반영하는 경우를 Mixed Linear Model이라고 합니다.

### Fit the Model 

- 따라서, 아래와 같이, 데이터를 사용하여, 간단한 MLM(Mixed Linear Model)을 만들어서 fitting을 해봅니다. 여기서 만드는 기본적인 model은 categorical value인 `sicdegp`와 `age`의 interaction term이 사회화 정도인 `vsae`를 예측할 수 있다고, 가정하고 세워집니다. 
    - `formula = 'vsae ~ age * C(sicdegp)', `



```python
import numpy as np
import pandas as pd
import statsmodels.api as sm
from sklearn import linear_model
import patsy
from scipy.stats import chi2 # for sig testing

# Read the data
autism_df = pd.read_csv("autism.csv").dropna()
print(autism_df.head())

print("== Fit the Model without Centering")
print("=="*20)
# Build the model
# Mixed Linear Model을 만듬.
## re_formula : A one-sided formula defining the variance structure of the model. The default gives a random intercept for each group.

RE_FORMULAT_ONE = True
if RE_FORMULAT_ONE==True:
    mlm_mod = sm.MixedLM.from_formula(
        formula = 'vsae ~ age * C(sicdegp)', 
        groups = 'childid', 
        re_formula="1 + age", 
        data=autism_df
    )
    # Run the fit
    mlm_result = mlm_mod.fit()

    # Print out the summary of the fit
    print(mlm_result.summary())
```

- 그러나, 결과를 보면, 우선 데이터들이 다음과 같은 두 가지 Warning이 발생합니다. 
    - Mamimum Likelihood optimization이 converge하는데 실패했다는 이야기죠. 

```
ConvergenceWarning: Maximum Likelihood optimization failed to converge. Check mle_retvals
  "Check mle_retvals", ConvergenceWarning)
ConvergenceWarning: Retrying MixedLM optimization with lbfgs

             Mixed Linear Model Regression Results
===============================================================
Model:               MixedLM   Dependent Variable:   vsae
No. Observations:    610       Method:               REML
No. Groups:          158       Scale:                62.2592
Min. group size:     1         Likelihood:           -2348.7987
Max. group size:     5         Converged:            Yes
Mean group size:     3.9
---------------------------------------------------------------
                     Coef.  Std.Err.   z    P>|z| [0.025 0.975]
---------------------------------------------------------------
Intercept             1.901    1.600  1.188 0.235 -1.235  5.038
C(sicdegp)[T.2]      -0.415    2.109 -0.197 0.844 -4.549  3.718
C(sicdegp)[T.3]      -3.917    2.345 -1.670 0.095 -8.514  0.680
age                   2.957    0.593  4.986 0.000  1.794  4.119
age:C(sicdegp)[T.2]   0.741    0.784  0.945 0.344 -0.795  2.277
age:C(sicdegp)[T.3]   4.356    0.869  5.014 0.000  2.653  6.058
childid Var          58.265    2.990
childid x age Cov   -28.736    0.697
age Var              14.204    0.283
===============================================================
```

- 여기서, 우리는 Random intercept를 1로 가정했습니다. 이는, 아이가 태어나자마자(0살일 때), socialization이 1이라는 이야기죠. 사실, 태어났을 때 모든 아이들의 socialization은 같다고 가정할 수 있다는 이야기죠. 따라서, 기존의 random intercept가 1이었던 반면, 이를 0으로 변경합니다. 그리고 다음과 같이, model을 수정하여 fitting을 해봅니다. 
- 또한, 해석의 용이성을 위해서 `age`를 centering해주었습니다. 이렇게 할 경우, intercept가 최소값이 아닌, 평균을 의미하게 되죠.

```python
autism_df["age"] = autism_df.groupby("childid")["age"].transform(lambda x: x - x.mean())

CENTERING_AGE = True
if CENTERING_AGE==True:
    # Refit the model, again, without the random intercepts
    mlm_mod = sm.MixedLM.from_formula(
        formula = 'vsae ~ age * C(sicdegp)', 
        groups = 'childid', 
        re_formula="0 + age", # random effect formula
        data=autism_df
    )

    # Run the fit
    mlm_result = mlm_mod.fit()

    # Print out the summary of the fit
    print(mlm_result.summary())
```

- 이처럼 random intercept만 변경하였는데, 아까 표시된 warninig이 없어지고, converge하는 것을 알 수 있습니다.
- 우리가 만든 fitting model의 기본 가정을 정리하자면, expressive language group을 의미하는 변수 `sicdegp`와 `age` 변수간의 interaction term이 아이의 사회화 정도를 의미하는 `vsae`에 positive한 영향을 미친다는 것을 알 수 있습니다. 
    - 이를 더 꼼꼼히 보면, `age:C(sicdegp)[T.3]`의 coef가 다른 coef에 비해서 높은 것을 알 수 있으며, 이는 third expressive language group에서 age라는 변수가 큰 영향을 미친다는 것을 알 수 있습니다.

```
========================================
            Mixed Linear Model Regression Results
==============================================================
Model:              MixedLM   Dependent Variable:   vsae
No. Observations:   610       Method:               REML
No. Groups:         158       Scale:                410.7496
Min. group size:    1         Likelihood:           -2752.2106
Max. group size:    5         Converged:            Yes
Mean group size:    3.9
--------------------------------------------------------------
                    Coef.  Std.Err.   z    P>|z| [0.025 0.975]
--------------------------------------------------------------
Intercept           17.421    1.470 11.848 0.000 14.539 20.303
C(sicdegp)[T.2]      6.359    1.942  3.274 0.001  2.552 10.166
C(sicdegp)[T.3]     23.403    2.157 10.852 0.000 19.176 27.630
age                  2.731    0.641  4.257 0.000  1.474  3.988
age:C(sicdegp)[T.2]  1.188    0.843  1.409 0.159 -0.465  2.840
age:C(sicdegp)[T.3]  4.555    0.931  4.891 0.000  2.730  6.381
age Var              9.609    0.112
==============================================================
```

### Significance Testing

- 자, 앞에서는 우리가 age에 따라서 서로 다른 random effect를 가진다고 가정하고 모델을 만들었습니다. 그런데, 이게 정말 그런지에 대해서 확인하기 위해서는 random effect를 가지지 않는 모델과 비교하여 보는 것이 필요하죠. 
- 이를 위해서, 여기서는 Random effect를 고려한 Mixed Model과 고려하지 않은 OLS를 각각 설계하여 그 통계 값을 가지고 둘의 차이가 존재함을 비교합니다. 결과의 log-likelihood 값을 사용하여 이 분포가 같은 것을 null hypothesis로 두고, 다른 것을 alternative hypothesis로 두고 비교하였는데, 정확히 이해가 되지 않아서, 이 부분은 일단 넘어갑니다.

```python
SIG_TESTING = True
if SIG_TESTING==True:
    # Random Effects Mixed Model with centering
    mlm_mod = sm.MixedLM.from_formula(
        formula = 'vsae ~ age * C(sicdegp)', 
        groups = 'childid', 
        re_formula="0 + age", # random effect formula
        data=autism_df
    )
    # OLS model - no mixed effects
    # age에 따른 random effect가 고려되어 있지 않습니다.
    ols_mod = sm.OLS.from_formula(
        formula = "vsae ~ age * C(sicdegp)",
        data = autism_df
    )

    # Run each of the fits
    mlm_result = mlm_mod.fit()
    ols_result = ols_mod.fit()

    # Print out the summary of the fit
    print("== Random effects Mixed Model")
    print(mlm_result.summary())
    print("=="*20)
    print("== Ordinary Least Squares")
    print(ols_result.summary())
```

```
== Random effects Mixed Model
            Mixed Linear Model Regression Results
==============================================================
Model:              MixedLM   Dependent Variable:   vsae
No. Observations:   610       Method:               REML
No. Groups:         158       Scale:                410.7496
Min. group size:    1         Likelihood:           -2752.2106
Max. group size:    5         Converged:            Yes
Mean group size:    3.9
--------------------------------------------------------------
                    Coef.  Std.Err.   z    P>|z| [0.025 0.975]
--------------------------------------------------------------
Intercept           17.421    1.470 11.848 0.000 14.539 20.303
C(sicdegp)[T.2]      6.359    1.942  3.274 0.001  2.552 10.166
C(sicdegp)[T.3]     23.403    2.157 10.852 0.000 19.176 27.630
age                  2.731    0.641  4.257 0.000  1.474  3.988
age:C(sicdegp)[T.2]  1.188    0.843  1.409 0.159 -0.465  2.840
age:C(sicdegp)[T.3]  4.555    0.931  4.891 0.000  2.730  6.381
age Var              9.609    0.112
==============================================================

== Ordinary Least Squares
                            OLS Regression Results
==============================================================================
Dep. Variable:                   vsae   R-squared:                       0.431
Model:                            OLS   Adj. R-squared:                  0.426
Method:                 Least Squares   F-statistic:                     91.38
Date:                Mon, 20 Jan 2020   Prob (F-statistic):           1.48e-71
Time:                        15:48:53   Log-Likelihood:                -2783.8
No. Observations:                 610   AIC:                             5580.
Df Residuals:                     604   BIC:                             5606.
Df Model:                           5
Covariance Type:            nonrobust
=======================================================================================
                          coef    std err          t      P>|t|      [0.025      0.975]
---------------------------------------------------------------------------------------
Intercept              17.4211      1.692     10.294      0.000      14.097      20.745
C(sicdegp)[T.2]         6.3593      2.236      2.844      0.005       1.969      10.750
C(sicdegp)[T.3]        23.4032      2.482      9.428      0.000      18.528      28.278
age                     2.5989      0.459      5.666      0.000       1.698       3.500
age:C(sicdegp)[T.2]     1.4736      0.599      2.458      0.014       0.296       2.651
age:C(sicdegp)[T.3]     4.4762      0.662      6.757      0.000       3.175       5.777
==============================================================================
Omnibus:                      315.218   Durbin-Watson:                   1.236
Prob(Omnibus):                  0.000   Jarque-Bera (JB):             2400.509
Skew:                           2.181   Prob(JB):                         0.00
Kurtosis:                      11.685   Cond. No.                         14.7
==============================================================================

```


## wrap-up

- 이전에 공부했던 내용들에 비해서 그 난이도가 갑자기 급증하였습니다. 개념적으로는, 같은 피실험자를 대상으로 축적된 데이터이므로, `group`을 구분하고, 또, `age`에 따라 다른 random effect가 적용될 것이므로 이 값을 집어넣어서 모델링을 한다, 라는 것이 전부이기는 하지만, 뒤쪽에, "그래서, 실제로 random effect가 다른지 아닌지에 대해서 보여준 부분"은 전혀 이해하지 못하고 넘어간 것 같습니다.
- 만약, 이후에, 여기서 분석한 데이터와 동일하게, "같은 피실험자를 대상으로 오랜 기간동안 추적한 데이터"라면, 이와 같은 방식으로 적용하여 비슷한 결론을 내릴 수는 있을 것 같습니다만, 다시 결국 significance testing을 제대로 하지 못하면 그다지 큰 의미가 있다고 보여지지 않네요.



## reference

- <https://robotcat.tistory.com/393>

