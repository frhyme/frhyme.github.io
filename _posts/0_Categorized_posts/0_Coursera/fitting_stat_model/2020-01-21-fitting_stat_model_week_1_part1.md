---
title: Fitting Statistical Models to Data with Python - WEEK 1 - Part 1
category: python-libs
tags: python python-libs coursera statsmodel statistics
---

## WEEK 1 - OVERVIEW & CONSIDERATIONS FOR STATISTICAL MODELING

- 이 코스에서는 주로 `statsmodels`라는 파이썬 라이브러리를 주로 활용하며, 이를 활용해 이전에 배운 간단한 통계적 기법을 배웁니다. 
- 지금이야, 워낙 뉴럴 넷 기반의 다양한 모델들을 사용하지만, 각 변수의 해석 측면이나, 각 변수에 대한 다양한 분포를 가정하고 문제를 풀어나갈 수 있다는 점에서 봤을 때, 선형 모델은 데이터 분석의 기본 중의 기본이죠. 특히, 비교적 일관적인 데이터에서 수집되는, "머신러닝 용 데이터"들을 제외하고, 만약 설문조사 등을 통해서 데이터를 수집한다면, 그 데이터들은 보통 다양한 변화를 가지고 있습니다. 시간에 따라서 달라지고, 사람, 혹은 사람이 속한 집단에 따라서 다양한 분포와 분산을 가지죠. 즉, 데이터 세트 자체에 내재된 특성을 인지하고, 그로부터 변수의 특성을 고려하여 모델을 설계한다, 라고 보면 통계적 모델링은 좀 더 지적인 활동처럼 보이기도 합니다. 
- 물론, 딥러닝이 쌓아온 많은 아름다움이 있고, 특히 language model에서의 뛰어난 활약은 무시하기 어렵기는 하지만, 가끔은 그게 모두 노가다 처럼 보일 때도 있긴 하니까요. 
- 한참 딥러닝을 배울 때는, 가끔, 뭐 이런 노가다가 다 있나, 싶을 때가 있었는데, 기본적인 통계적 기법을 공부하다보니, 약간 또 이쪽 뽕을 맞은 것 같습니다 허허허허허. 
- 아무튼 본강의에서는 대략 다음과 같은 내용들을 배우게 됩니다. 
    - `descriptive statiscs`: mean, variance 등을 통해 해당 데이터의 분포를 측정하는 것. 
    - `confidence interval`: 모집단이 어떤 분포를 따르고, 표본 집단을 뽑아서, 모집단을 추정할 수 있는 어떤 지표를 만들었을 때, 이 지표가 가지는 분포를 토대로 아마도 어떤 구간 내에 95%등의 확률로 있을 것이다, 를 추정하는 것 
    - `hypothesis testing`: null hypothesis를 가정하고(즉, 데이터가 아마 이런 형태를 따를 것이다를 기본적으로 가정하고) 그 때 우리가 표본을 통해 추정한 결과가 이 가정에 따라서 충분히 생성가능한 것인지, 아닌지를 추정 p-value를 통해 정확히 파악할 수 있음.
- 또한, 이미 머신러닝에 익숙하신 분들에게는 쉽게 이해될 수 있을 것 같습니다. 그저, 모델을 선형방정식으로 고정했을 뿐이지, X, Y를 각각 넣어서 fitting하는 것과 다른게 없습니다. 다만, 머신러닝에서는 그저, '무슨 짓을 하든, 결과만 잘 맞으면 된다'에 가깝게 진행한다면, 여기서는 통계적인 설명력을 좀 더 강조한다고 볼 수있겠네요. 사실, 그래서 선형방정식을 고정하여 다양한 기법을 적용하게 되는 것이죠. 사실상 뉴럴넷은 설명력이 없고, 선형방정식은 각 변수의 영향력을 비교적 정확하게 측정할 수 있기 때문에 설명력이 높다고 할 수 있습니다. 

## OLS, GLM, GEE and etc.

- WEEK 1에서는 기본적으로 선형 방정식으로 기본으로 하여, 현재의 데이터 분포를 가장 잘 설명할 수 있는 Model을 만드는 것을 목적으로 합니다. `OLS`, `GLM`, `GEE`, `MIXEDLM` 모두, `statsmodels`의 기본적인 라이브러리이며, 각 모델에 대한 설명과, 기본적인 골격들을 다룹니다.
- 일단 이 코스에서는 nhanes 데이터를 활용하며, 아래 코드를 이용하여, 데이터를 읽고 필요 없는 데이터들을 날립니다. 

```python
import statsmodels.api as sm
import numpy as np
import pandas as pd 

# Read and Process data

# file link  
# https://github.com/kshedden/statswpy-nhanes/blob/master/merged/nhanes_2015_2016.csv
nhanes_df = pd.read_csv("nhanes_2015_2016.csv")
#print(nhanes_df.columns)
# Drop unused columns, drop rows with any missing values.
# 필요없는 칼럼들을 누락시키고, 
vars = ["BPXSY1", "RIDAGEYR", "RIAGENDR", "RIDRETH1", "DMDEDUC2", "BMXBMI", "SMQ020"]
nhanes_df = nhanes_df[vars].dropna()
# text로 되어 있는 값들을 0, 1로 변경하고,
nhanes_df["RIAGENDRx"] = nhanes_df.RIAGENDR.replace({1: "Male", 2: "Female"})
print("== file processing done")
print("== describe")
print(nhanes_df.describe())
print("=="*20)
```

```
== file processing done
== describe
            BPXSY1     RIDAGEYR     RIAGENDR     RIDRETH1     DMDEDUC2       BMXBMI       SMQ020
count  5102.000000  5102.000000  5102.000000  5102.000000  5102.000000  5102.000000  5102.000000
mean    125.626813    49.455116     1.517444     3.024108     3.438456    29.506978     1.588789
std      18.486560    17.682020     0.499745     1.283866     1.305679     6.977889     0.569994
min      82.000000    20.000000     1.000000     1.000000     1.000000    14.500000     1.000000
25%     112.500000    34.000000     1.000000     2.000000     3.000000    24.600000     1.000000
50%     124.000000    49.000000     2.000000     3.000000     4.000000    28.500000     2.000000
75%     136.000000    64.000000     2.000000     4.000000     4.000000    33.200000     2.000000
max     236.000000    80.000000     2.000000     5.000000     9.000000    64.600000     9.000000
========================================
```


### Ordinary Least Squares(OLS)

- OLS는 선형 방정식에서 우리의 target varible, 즉 우리가 관심을 두고 있는 목적 변수가 연속적(continuouse)일 때, 아직 잘 모르는 parameter를 예측하는 선형 방정식 모델링 기법이며, 가장 기본적인 deterministic linear regression입니다. 즉, `y = ax1 + bx2 + c`와 같은 식으로 선형 모형을 정하고, 이 때 a, b, c와 같은 parameter를 추정할 때, 이 모델을 통해서 추정할 수 있는 `y_estimate`와 실제 값인 `y_true`간의 차이의 제곱 합(redisudal sum of squares)을 최소화하는 값을 찾는 것을 말하죠. 
- 본 수업에서는 `statsmodels`를 사용하여 OLS를 구현하였지만, sklearn에도 있고 tensorflow에서도 동일한 짓을 할 수 있습니다. 다만, 여기서는 `R` 언어 에서 많이 사용하는 formula를 사용해서 넘길 수 있다는 것이, 경우에 따라서 편하죠.

```python
OLS = True
if OLS:
    #################################
    # OLS: 
    #################################
    # X: RIAGENDRx, RIAGENDRx
    # Y: BPXSY1
    # 다음과 같이, Y ~ X1 + X2 의 형태로 formula로 넘길 수도 있죠. 
    # sklearn의 경우에는 이처럼 formula의 형태로 넘기는 것이 없었던 것 같아요. 
    model = sm.OLS.from_formula(
        formula="BPXSY1 ~ RIDAGEYR + RIAGENDRx", 
        data=nhanes_df
    )
    res = model.fit()
    print("== Summary")
    print(res.summary())
    print("== OLS complete")
```

- 코드의 실행 결과는 다음과 같습니다. 현재 설계한 모델이 어느 정도의 정확도를 가지고 있는지, 기본적인 통계값을 통해서, 이 모델이 얼마나 신뢰성을 가지고 있으며, 각 coeff가 어떤 값을 가지며 또한 어떤 분포 속에 있다고 할 수 있는지 등에 대해서 보여줍니다.

```
== Summary
                            OLS Regression Results
==============================================================================
Dep. Variable:                 BPXSY1   R-squared:                       0.215
Model:                            OLS   Adj. R-squared:                  0.214
Method:                 Least Squares   F-statistic:                     697.4
Date:                Wed, 15 Jan 2020   Prob (F-statistic):          1.87e-268
Time:                        17:05:54   Log-Likelihood:                -21505.
No. Observations:                5102   AIC:                         4.302e+04
Df Residuals:                    5099   BIC:                         4.304e+04
Df Model:                           2
Covariance Type:            nonrobust
=====================================================================================
                        coef    std err          t      P>|t|      [0.025      0.975]
-------------------------------------------------------------------------------------
Intercept           100.6305      0.712    141.257      0.000      99.234     102.027
RIAGENDRx[T.Male]     3.2322      0.459      7.040      0.000       2.332       4.132
RIDAGEYR              0.4739      0.013     36.518      0.000       0.448       0.499
==============================================================================
Omnibus:                      706.732   Durbin-Watson:                   2.036
Prob(Omnibus):                  0.000   Jarque-Bera (JB):             1582.730
Skew:                           0.818   Prob(JB):                         0.00
Kurtosis:                       5.184   Cond. No.                         168.
==============================================================================

Warnings:
[1] Standard Errors assume that the covariance matrix of the errors is correctly specified.
== OLS complete
```

### Generalized Linear Models(GLM)

- 사실 GLM은 말 그대로, 일반화된 선형 모델이라고 해석됩니다(flexible generalization of ordinary linear regression). 여기서, OLS와 같은 모델에서는 종속변수들이 normal distribution을 따른다고 가정하는 반면, GLM에서는 종속변수(+잔차의 분포)가 반드시 normal distribution일 필요가 없습니다. 예를 들어서, binary classification 문제들의 경우는 결과값이 normal distribution이 아니잖아요. 즉, 이런 것처럼 linear model을 통해서 나온 결과(y)를 실제 response variable로 변형해주기 위해 이 둘을 이어주는 일종의 변환함수를 [link function](https://support.minitab.com/en-us/minitab/19/help-and-how-to/modeling-statistics/regression/supporting-topics/logistic-regression/link-function/)이라고 합니다.
- 본 코스에서는 모든 GLM을 다루지는 않고, binary classification을 위한, logistic function만을 모델링합니다.

```python
GLM = True
if GLM==True: 
    # smq: smoker인지 아닌지에 대한 binary variable이며 
    # RIAGENDRx: gender를 말합니다
    nhanes_df["smq"] = nhanes_df.SMQ020.replace({2: 0, 7: np.nan, 9: np.nan})
    model = sm.GLM.from_formula(
        formula="smq ~ RIAGENDRx", 
        family=sm.families.Binomial(), 
        data=nhanes_df
    )
    res = model.fit()
    print("== Summary")
    print(res.summary())
    print("== GLM complete")
```

```
== Summary
                 Generalized Linear Model Regression Results
==============================================================================
Dep. Variable:                    smq   No. Observations:                 5094
Model:                            GLM   Df Residuals:                     5092
Model Family:                Binomial   Df Model:                            1
Link Function:                  logit   Scale:                          1.0000
Method:                          IRLS   Log-Likelihood:                -3350.6
Date:                Wed, 15 Jan 2020   Deviance:                       6701.2
Time:                        17:31:14   Pearson chi2:                 5.09e+03
No. Iterations:                     4
Covariance Type:            nonrobust
=====================================================================================
                        coef    std err          z      P>|z|      [0.025      0.975]
-------------------------------------------------------------------------------------
Intercept            -0.7547      0.042    -18.071      0.000      -0.837      -0.673
RIAGENDRx[T.Male]     0.8851      0.058     15.227      0.000       0.771       0.999
=====================================================================================
== GLM complete
```

### Generalized Estimated Equations(GEE), 보완 필요!

#### Background

- Limitation of GLM) GLM은 오류(error)들이 독립적이라는 것에서 출발합니다. 하지만, 우리가 실제로 관측한 많은 데이터들은 이 error들이 독립적이라고 보기 어렵습니다. 하나의 예로, 만약 사람 A의 혈당량과 같은 데이터를 N1 번 관측했다고 해봅시다. 그리고 사람 B의 혈당량과 같은 데이터를 N2 번 관측했다고 해보죠. 이 때 우리가 가진 데이터는 A의 혈당량 N1번, B의 혈당량 N2번이 됩니다. 그리고 이 데이터들은 각각 A라는 사람과 B라는 사람에게 깊게 의존하기 때문에, 독립적이라고 보기 어렵습니다. 즉, 앞서 말한 바와 같이, 개개인의 차이가 제어되지 않은 상태인 것이죠. 
- GLMM) 이처럼 outcome이 독립적이지 않을 때, GLMM(Generalized Linear Mixed Model)을 사용해서 피험자별로 random effect를 다르게 적용하여, 해결할 수도 있습니다. 즉, 그 error를 분리하여, 피험자에게 다른 분포가 적용될 수 있음을 통해서 outcome의 의존성을 해결해주는 것이죠. 따라서, covariance structure를 추정함으로써 variance의 변화를 반영한다는 점에서 이 방법은 모수적 방법(parameteric method)가 됩니다. 
- Limit of GLMM) GLMM의 경우, 추정된 covariance structure에 따라서 모델을 fitting하게 되는데요, 이 때 상대적으로 covariance에 민감하게 반응하게 됩니다. 또한, 데이터 세트에 내재되어 있는 측정되지 않는, 다른 의존성들을 처리할 수는 없다는 한계를 가지고 있기도 하죠. 
- GEE) GEE 또한, panel, cluster 등 반복 측정된 데이터들에 대해서, Heteroscedasticity가 내재되어 있는 경우에, 이를 해결하기 위해서 사용됩니다. covariance structure를 기반으로 진행하는 GLMM과 달리, GEE의 parameter tuning은 상대적으로 일관적입니다. 
- 까지 알겠고, 아직 명확하지 않은 부분들이 있어서, 넘어갑니다. 사실, 이 부분에서는 어찌 보면, 그냥 모든 기법을 다 사용해서 통계갑을 비교하는 것이 제일 적합해 보이기도 해요. 가령, GEE는 내재되어 있는(혹은 숨겨져 있는) 공분산구조를 알아서 측정할 수 있도록 

#### GEE) do it. 

- 아무튼, 본 코스에서는 이전과 동일하게 `statsmodels`를 이용하여, GEE를 설계합니다.
- 다만 이전에 나온 다른 model의 summary와 다른 점은 `Y ~ X`의 형태로 formula를 넘기지 않고, 마치, `group`이라는 변수를 넘기는 것입니다. 다르게 보면, 이는 각 'group에 대해서 이를 가장 잘 설명할 수 있는 분포의 형태를 찾는 것이다'처럼 보이기도 합니다.
- 이렇게 쓰고 보니, 그냥 '클러스터링'처럼 보이기도 하네요 흠. 

```python
GEE = True
if GEE == True:
    print("== GEE Summary")
    nhanes_df["group"] = 10*nhanes_df.SDMVSTRA + nhanes_df.SDMVPSU
    #print(nhanes_df["group"].head(20))
    model = sm.GEE.from_formula(
        formula="BPXSY1 ~ 1", 
        groups="group", 
        # 여기서와 같이, cov_struct(공분산구조)가 어떤 형태인지를 정의해줌. 이를 통해 
        cov_struct=sm.cov_struct.Exchangeable(), 
        data=nhanes_df
    )
    res = model.fit()
    print(res.cov_struct.summary())
    print(res.summary())
```

- `No. clusters`가 있는 것이 조금 특이하게 보입니다.

```
== GEE Summary
The correlation between two observations in the same cluster is 0.030
                               GEE Regression Results
===================================================================================
Dep. Variable:                      BPXSY1   No. Observations:                 5102
Model:                                 GEE   No. clusters:                       30
Method:                        Generalized   Min. cluster size:                 106
                      Estimating Equations   Max. cluster size:                 226
Family:                           Gaussian   Mean cluster size:               170.1
Dependence structure:         Exchangeable   Num. iterations:                     6
Date:                     Thu, 16 Jan 2020   Scale:                         341.838
Covariance type:                    robust   Time:                         16:02:34
==============================================================================
                 coef    std err          z      P>|z|      [0.025      0.975]
------------------------------------------------------------------------------
Intercept    125.3352      0.615    203.894      0.000     124.130     126.540
==============================================================================
Skew:                          0.9922   Kurtosis:                       1.7588
Centered skew:                 0.9683   Centered kurtosis:              1.6972
==============================================================================
```

## wrap-up

- 사실 하나의 jupyter notebook에 너무 많은 내용들이 있어서, 따라가기 좀 벅찼는데요, 죽 읽어보니, OLS, GLM의 경우는 week2 에서 배우고, GEE, MIXEDLM의 경우는 week3 에서 배운다고 합니다. 후. 다행이네요.
- 또한, 앞서 말한것과 같이, 각 모델이 절대적으로 우월하다고 볼 수는 없어요. 필요에 따라서, 이 모델이 적합할 수도 있고, 다른 모델이 적합할 수도 있죠. 

## reference

- <https://elecs.tistory.com/348>


## raw code 

```python 
import statsmodels.api as sm
import numpy as np
import pandas as pd 

# Read and Process data

# file link  
# https://github.com/kshedden/statswpy-nhanes/blob/master/merged/nhanes_2015_2016.csv
nhanes_df = pd.read_csv("nhanes_2015_2016.csv")
print(nhanes_df.columns)
# Drop unused columns, drop rows with any missing values.
# 필요없는 칼럼들을 누락시키고, 
vars = ["BPXSY1", "RIDAGEYR", "RIAGENDR", "RIDRETH1", "DMDEDUC2", "BMXBMI",
        "SMQ020", "SDMVSTRA", "SDMVPSU"]
nhanes_df = nhanes_df[vars].dropna()
# text로 되어 있는 값들을 0, 1로 변경하고,
nhanes_df["RIAGENDRx"] = nhanes_df.RIAGENDR.replace({1: "Male", 2: "Female"})
print("== file processing done")

df_DESC = False
if df_DESC==True:
    print("== describe")
    print(nhanes_df.describe())
    print("=="*20)


OLS = False
if OLS:
    #################################
    # OLS: 
    #################################
    # X: RIAGENDRx, RIAGENDRx
    # Y: BPXSY1
    # 다음과 같이, Y ~ X1 + X2 의 형태로 formula로 넘길 수도 있죠. 
    # sklearn의 경우에는 이처럼 formula의 형태로 넘기는 것이 없었던 것 같아요. 
    model = sm.OLS.from_formula(
        formula="BPXSY1 ~ RIDAGEYR + RIAGENDRx", 
        data=nhanes_df
    )
    res = model.fit()
    print("== Summary")
    print(res.summary())
    print("== OLS complete")
    
GLM = False
if GLM==True: 
    nhanes_df["smq"] = nhanes_df.SMQ020.replace({2: 0, 7: np.nan, 9: np.nan})
    model = sm.GLM.from_formula(
        formula="smq ~ RIAGENDRx", 
        family=sm.families.Binomial(), 
        data=nhanes_df
    )
    res = model.fit()
    print("== Summary")
    print(res.summary())
    print("== GLM complete")

GEE = False
if GEE == True:
    print("== GEE Summary")
    nhanes_df["group"] = 10*nhanes_df.SDMVSTRA + nhanes_df.SDMVPSU
    #print(nhanes_df["group"].head(20))
    model = sm.GEE.from_formula(
        formula="BPXSY1 ~ 1", 
        groups="group", 
        cov_struct=sm.cov_struct.Exchangeable(), 
        data=nhanes_df
    )
    res = model.fit()
    print(res.cov_struct.summary())
    print(res.summary())

MM = True
if MM==True:
    print("== GEE Summary")
    nhanes_df["group"] = 10*nhanes_df.SDMVSTRA + nhanes_df.SDMVPSU
    nhanes_df["smq"] = nhanes_df.SMQ020.replace({2: 0, 7: np.nan, 9: np.nan})
    for v in ["BPXSY1", "RIDAGEYR", "BMXBMI", "smq", "SDMVSTRA"]:
        print(f"=== {v}")
        model = sm.GEE.from_formula(
            formula=v + " ~ 1", 
            groups="group",
            cov_struct=sm.cov_struct.Exchangeable(), 
            data=nhanes_df
        )
        result = model.fit()
        print(v, result.cov_struct.summary())
```
