---
title: Fitting Statistical Models to Data with Python - WEEK 2 - Part 2
category: python-libs
tags: python python-libs coursera statsmodel statistics
---

## probability, odds, logodds.

- 이제, binary outcome을 예측하는 모델을 만든다. 여기서는 `SMQ020`라고 하는, '흡연 유무(정확히는, "인생에서 최소 100개의 담배를 피웠는가"라는 질문에 대한 응답)'을 response varible로, 이를 예측하는 모델을 만들어본다.
- logistic regression은 event가 발생할 'odds'를 계산하는데, 만약 event가 `p`의 확률을 가지고 있다면, 이 event의 odd는 `p/(1-p)`가 된다. 
- 멀쩡히 잘 있는 probability를 무시하고, `Odds`를 사용하고, 그리고 거기에 log를 붙여서 `log-Odds`까지 붙이는 이유는, probability의 경우 0과 1사이의 값만을 가지는 반면, Odds의 경우 range(0, inf) 그리고 log-Odds의 경우는 range(-inf, inf)의 범위를 가진다. 
- 정리를 하자면, binary regression에서는 0과 1을 바로 나타낼 수 없기 때문에 우선 확률적인 값인 `P(E)`등을 이용하여 `P(E) = b0 + b1x1 + ... + bnxn` 형태로 표현합니다. 하지만, 이렇게 표현하게 될 경우, 좌변과 우변의 range가 다릅니다. 좌변은 proability이므로 range(0, 1)인 반면, 오늘쪽의 경우는 range(-inf, inf)를 가지죠. 따라서 이를 똑같이 mapping할 수 있도록 해주기 위해, Odds로 변경하고, 다시 Log-Odds로 변경해줍니다. 

### interpretation of log - odds

- `log - odds`는 기본적으로 다음과 같이 해석됩니다.
    - probability가 1/2이라면 odds는 1이 되고, log-odds는 0입니다. 
    - log-odds가 0보다 크다면, 첫번째 그룹이 두번째 그룹보다 odds가 더 크다는 것(당연히 probability도 크다는것)
    - log-odds가 0보다 작다면, 첫번째 그룹이 두번째 그룹보다 odds가 더 작다는 것(당연히 probability도 작다는것)

## check odds, log-odds first. 

- 그래서, 우리는 앞서 말한 바와 같이, '흡연유무'를 판단하는 기본적인 logistic regression model을 만들 것입니다. 
- 그리고, 'gender'를 예측 변수로 설정을 했다고 하고, 간단히 odds, log-odds등을 계산해봅니다. 

```python
# Read and Process data
# file link  
# https://github.com/kshedden/statswpy-nhanes/blob/master/merged/nhanes_2015_2016.csv
nhanes_df = pd.read_csv("nhanes_2015_2016.csv")
#print(nhanes_df.columns)
# 필요한 칼럼만 선택하고, 필요없는 것들 삭제 
vars = ["BPXSY1", "RIDAGEYR", "RIAGENDR", "RIDRETH1", "DMDEDUC2", "BMXBMI", "SMQ020"]
nhanes_df = nhanes_df[vars].dropna()
nhanes_df["RIAGENDRx"] = nhanes_df.RIAGENDR.replace({1: "Male", 2: "Female"})
print("== csv file processed")
# 7, 9 는 유효하지 않은 응답이므로 제외함(가령, '모름', '응답 거부')
nhanes_df["smq"] = nhanes_df.SMQ020.replace({2: 0, 7: np.nan, 9: np.nan})
##### 
# gender, smoke 로 crosstable를 만든 다음 
print("== Make CrossTable")
CT_Gender_SMQ = pd.crosstab(
    index=nhanes_df["RIAGENDRx"], 
    columns=nhanes_df["smq"], 
)
print(CT_Gender_SMQ)
print("== Change to proportion column")
# gender별로 흡연 유무의 비율 지표로 변경해줍니다.
# 더 짧은 명령어가 있으나, 가독성을 위해, 조금 길게 설명해보았습니다.
# CT_Gender_SMQ = CT_Gender_SMQ.apply(lambda x: x/x.sum(), axis=1)
CT_Gender_SMQ.columns = ['non_smoke_p', 'smoke_p']
CT_Gender_SMQ['sum'] = CT_Gender_SMQ['non_smoke_p']+CT_Gender_SMQ['smoke_p']
CT_Gender_SMQ['non_smoke_p'] /=CT_Gender_SMQ['sum']
CT_Gender_SMQ['smoke_p'] /=CT_Gender_SMQ['sum']
del CT_Gender_SMQ['sum']
print(CT_Gender_SMQ)
# 그리고, odds 를 의미하는 새로운 칼럼을 만들어주죠. 
CT_Gender_SMQ["odds"] = CT_Gender_SMQ["smoke_p"] / CT_Gender_SMQ["non_smoke_p"]
#CT_Gender_SMQ["odds"] = CT_Gender_SMQ.loc[:, 1] / CT_Gender_SMQ.loc[:, 0]
print("== Add odds column")
print(CT_Gender_SMQ)
print("== Add log-odds column")
CT_Gender_SMQ['logodds'] = np.log(CT_Gender_SMQ["odds"])
print(CT_Gender_SMQ)
```

- 아래 결과를 보면, Male이 Female에 비해서, 확실히 odds가 높다는 것을 알 수 있습니다. 이는 다시 말해, '성별'이 '흡연 유무'에 영향을 줄 수 있는 예측변수가 될 수 있다는 것을 의미하죠.  

```
== csv file processed
== Make CrossTable
smq         0.0   1.0
RIAGENDRx
Female     1793   843
Male       1149  1309
== Change to proportion column
           non_smoke_p   smoke_p
RIAGENDRx
Female        0.680197  0.319803
Male          0.467453  0.532547
== Add odds column
           non_smoke_p   smoke_p      odds
RIAGENDRx
Female        0.680197  0.319803  0.470162
Male          0.467453  0.532547  1.139252
== Add log-odds column
           non_smoke_p   smoke_p      odds   logodds
RIAGENDRx
Female        0.680197  0.319803  0.470162 -0.754679
Male          0.467453  0.532547  1.139252  0.130371
```

## Basic logistic regression

- 이제는 logistic regression 모델을 세워 봅시다. 예측변수(covariate)는 '성별', 결과변수(outcome)은 '흡연유무'로 세팅되죠. 
- 여기서는 Genearelized Linear Model(GLM)을 이용해서 logistic regression을 표현합니다. logistic regression은 GLM의 한 형태로서, 이외에도 poisson regression과 같은 다른 방법들도 있죠. 
- 아무튼, GLM 모델을 parameter `family`에 `sm.families.Binomial()`을 넘겨주는 것이, logistic regression을 만드는 기본형태가 됩니다. 선형 방정식으로 만들어낸 식을 link function을 통해서 어떤 분포의 값으로 변경되느냐? 라고 보면 좀 더 정확할 수도 있습니다.

```python
model = sm.GLM.from_formula(
        formula="smq ~ RIAGENDRx", 
        # 여기를 binomial 로 넘겨주는 것이 logistic regression으로 만들어주는 것. 
        family=sm.families.Binomial(), 
        data=nhanes_df
    )
    result = model.fit()
    print("== GLM ")
    print(result.summary())
```

- 실행하고 나면 다음과 같은 결과가 나옵니다. `coef`는 동일하지만, OLS에 있던 R-square와 같은 값이 사라졌습니다. 
- 또한, 여기서 `RIAGENDRx[T.Male]`의 coef 값은 0.8851 이며, 이 값은 앞서 log-odd statistics의 차이와 동일합니다. 그리고, 당연하지만, 이는 covariate가 하나일때만 유효해지는 성질이기도 하죠.
    - logodds for Female : -0.754679
    - logodds for Male   : 0.130371

```
== GLM
                 Generalized Linear Model Regression Results
==============================================================================
Dep. Variable:                    smq   No. Observations:                 5094
Model:                            GLM   Df Residuals:                     5092
Model Family:                Binomial   Df Model:                            1
Link Function:                  logit   Scale:                          1.0000
Method:                          IRLS   Log-Likelihood:                -3350.6
Date:                Fri, 17 Jan 2020   Deviance:                       6701.2
Time:                        20:49:25   Pearson chi2:                 5.09e+03
No. Iterations:                     4
Covariance Type:            nonrobust
=====================================================================================
                        coef    std err          z      P>|z|      [0.025      0.975]
-------------------------------------------------------------------------------------
Intercept            -0.7547      0.042    -18.071      0.000      -0.837      -0.673
RIAGENDRx[T.Male]     0.8851      0.058     15.227      0.000       0.771       0.999
=====================================================================================
```

### Add more covariate(two covariate) 

- 예측변수를 추가합니다. 새로운 변수로는 '나이'를 넣어봅니다.


```python
model = sm.GLM.from_formula(
    formula="smq ~ RIDAGEYR + RIAGENDRx", 
    family=sm.families.Binomial(), 
    data=nhanes_df
)
result = model.fit()
print("== GLM ")
print(result.summary())
```

- 결과를 보면, gender parameter가 약간 변화하였습니다(0.885 to 0.892). 사실, 새로운 변수가 추가되거나, 없어질 경우에 coef는 상당히 많이 변하게 되지만, 여기서는 아주 작은 값만이 변화하였죠. 즉, 이 두 변수는 거의 독립적이라고 할 수 있습니다. 즉, 이 두 변수가 outcome에 주는 영향은 additive하죠(적층적이다, 즉 그냥 각각 더하면 된다). 
- 또한, year라는 변수 coef는 0.017입니다. 이 값은 log-odd 의 차이이며, 만약 두 사람간에 20년의 차이가 난다면, 두 사람간의 log-odd 차이는 0.34, odd 차이는 exp(0.34)가 되며, 즉, 두 사람간의 odds는 exp(0.34)가 됩니다.\
- 또한, 만약 30 year의 여성과 50 year의 남성을 비교한다고 하면, 이 차이는 `0.89 + 0.017*20`, `1.23`이 됩니다. 그리고, odds는 `exp(1.23)`, 3.42가 되며, 3.42만큼의 한쪽이 다른 한쪽에 비해 smoking할 가능성이 높다는 것이죠.
- 또한, logistic regression에서 two coviriate, 지금처럼 age, gender가 있을 때, 이 각각의 coefficient는 **conditionsl log odds**의 관점에서 해석되어야 합니다. 즉, 하나의 covariate가 고정되어 있을 때, 그 변화만이 반영된다는 것이죠. 앞서서, "30세의 여성"과 "50세의 남성"을 비교했는데, 이 경우는 두 covariate가 모두 다릅니다. 물론, 이 두 covariate가 서로 거의 독립인것처럼 보이므로, 큰 상관은 없을 것같긴하지만, 기본적으로는 이런 경우에는 각각 coef를 더해서, additive한 방식으로 값을 계산할 수는 없습니다.

```
== GLM
                 Generalized Linear Model Regression Results
==============================================================================
Dep. Variable:                    smq   No. Observations:                 5094
Model:                            GLM   Df Residuals:                     5091
Model Family:                Binomial   Df Model:                            2
Link Function:                  logit   Scale:                          1.0000
Method:                          IRLS   Log-Likelihood:                -3296.6
Date:                Fri, 17 Jan 2020   Deviance:                       6593.2
Time:                        21:02:20   Pearson chi2:                 5.10e+03
No. Iterations:                     4
Covariance Type:            nonrobust
=====================================================================================
                        coef    std err          z      P>|z|      [0.025      0.975]
-------------------------------------------------------------------------------------
Intercept            -1.6166      0.095    -16.985      0.000      -1.803      -1.430
RIAGENDRx[T.Male]     0.8920      0.059     15.170      0.000       0.777       1.007
RIDAGEYR              0.0172      0.002     10.289      0.000       0.014       0.021
=====================================================================================
```

### Add more covariate(three covariate)

- 이제 변수를 하나 더 넣어보겠습니다. `DMDEDUC2`라는, '피실험자의 교육정도'를 의미하는 변수를 추가합니다.

```python
nhanes_df["DMDEDUC2x"] = nhanes_df["DMDEDUC2"].replace(
    {
        1: "lt9", 2: "x9_11", 3: "HS", 
        4: "SomeCollege",5: "College", 7: np.nan, 9: np.nan
    }
)
model = sm.GLM.from_formula(
    formula="smq ~ RIDAGEYR + RIAGENDRx + DMDEDUC2x", 
    family=sm.families.Binomial(), 
    data=nhanes_df
)
result = model.fit()
print("== GLM ")
print(result.summary())
```

- 결과는 다음과 같습니다. Reference level(기본 값, 기준 값)은 Female과 College가 되죠(결과에 나타나 있지 않으므로 기본 값이 됩니다). 
- educational attainment의 모든 coefficient는 positive이며(물론 `College`는 reference level이므로 College의 coef는 0입니다만), 따라서, College의 교육수준을 가진 사람들이 가장 낮은 흡연율을 가지고 있다고 할 수 있습니다. coef가 positive라는 것은 log-odd를 높인다는 것이니까요. 다시 말하지만, 여기서도 계산할 때 중요한 것은 이 모든 것이 `conditional` 이라는 것이죠(즉, 다른 변수들을 모두 고정한 상태에서만 비교 가능하다는 이야기입니다). 따라서, reference level을 기준으로 삼고, 모든 다른 레벨이 동일할 때, 어떤 변화가 발생하는지만을 파악할 수 있다는 이야기죠.

```
== GLM
                 Generalized Linear Model Regression Results
==============================================================================
Dep. Variable:                    smq   No. Observations:                 5093
Model:                            GLM   Df Residuals:                     5086
Model Family:                Binomial   Df Model:                            6
Link Function:                  logit   Scale:                          1.0000
Method:                          IRLS   Log-Likelihood:                -3201.2
Date:                Sat, 18 Jan 2020   Deviance:                       6402.4
Time:                        16:03:56   Pearson chi2:                 5.10e+03
No. Iterations:                     4
Covariance Type:            nonrobust
============================================================================================
                               coef    std err          z      P>|z|      [0.025      0.975]
--------------------------------------------------------------------------------------------
Intercept                   -2.3060      0.114    -20.174      0.000      -2.530      -2.082
RIAGENDRx[T.Male]            0.9096      0.060     15.118      0.000       0.792       1.028
DMDEDUC2x[T.HS]              0.9434      0.090     10.521      0.000       0.768       1.119
DMDEDUC2x[T.SomeCollege]     0.8322      0.084      9.865      0.000       0.667       0.998
DMDEDUC2x[T.lt9]             0.2662      0.109      2.438      0.015       0.052       0.480
DMDEDUC2x[T.x9_11]           1.0986      0.107     10.296      0.000       0.889       1.308
RIDAGEYR                     0.0183      0.002     10.582      0.000       0.015       0.022
============================================================================================
```


## wrap-up

- 과거에 사용했던 logistic regression을 배웠습니다. 그때도 probability, odds, log-odds를 모두 배웠던 것으로 기억하는데, 다시 이 개념을 확인해서 도움이 되었고 왜 logistic regression이 이러한 형태로 설계되어야만 했는지도 아주 명확하게 알게 되었습니다. 아마도, 이제 잊어버리지 않을 것 같습니다. 
- 현재의 많은 데이터 분석 기법들이 neural net을 기반으로 하고 있는 상황에서, 통계적인 엄밀성을 파악한다는 점에서 기본적인 통계 기법 특히 선형적인 방정식을 다시 배우는 것은 의미가 있습니다. 현재의 모델들은 대부분 그냥 R-square와 같은 기본적인 지표만을 이야기하며, '해석력'이 현저하게 떨어지니까요. 

## raw code

```python
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import statsmodels.api as sm
import numpy as np

LINEAR_REG = False
if LINEAR_REG==True:
    # Read and Process data
    # file link  
    # https://github.com/kshedden/statswpy-nhanes/blob/master/merged/nhanes_2015_2016.csv
    nhanes_df = pd.read_csv("nhanes_2015_2016.csv")
    #print(nhanes_df.columns)
    # 필요한 칼럼만 선택하고, 필요없는 것들 삭제 
    vars = ["BPXSY1", "RIDAGEYR", "RIAGENDR", "RIDRETH1", "DMDEDUC2", "BMXBMI", "SMQ020"]
    nhanes_df = nhanes_df[vars].dropna()
    nhanes_df["RIAGENDRx"] = nhanes_df.RIAGENDR.replace({1: "Male", 2: "Female"})
    print("== csv file processed")

    print("== OLS summary")
    model = sm.OLS.from_formula("BPXSY1 ~ RIDAGEYR + BMXBMI + RIAGENDRx", data=nhanes_df)
    result = model.fit()
    print(result.summary())
    print("== OLS done")

LOGIT_REG = True
if LOGIT_REG==True:
    # Read and Process data
    # file link  
    # https://github.com/kshedden/statswpy-nhanes/blob/master/merged/nhanes_2015_2016.csv
    nhanes_df = pd.read_csv("nhanes_2015_2016.csv")
    #print(nhanes_df.columns)
    # 필요한 칼럼만 선택하고, 필요없는 것들 삭제 
    vars = ["BPXSY1", "RIDAGEYR", "RIAGENDR", "RIDRETH1", "DMDEDUC2", "BMXBMI", "SMQ020"]
    nhanes_df = nhanes_df[vars].dropna()
    nhanes_df["RIAGENDRx"] = nhanes_df.RIAGENDR.replace({1: "Male", 2: "Female"})
    print("== csv file processed")
    # 7, 9 는 유효하지 않은 응답이므로 제외함(가령, '모름', '응답 거부')
    nhanes_df["smq"] = nhanes_df.SMQ020.replace({2: 0, 7: np.nan, 9: np.nan})

    
    CROSS_TAB = False
    if CROSS_TAB==True:
        ##### 
        # gender, smoke 로 crosstable를 만든 다음 
        print("== Make CrossTable")
        CT_Gender_SMQ = pd.crosstab(
            index=nhanes_df["RIAGENDRx"], 
            columns=nhanes_df["smq"], 
        )
        print(CT_Gender_SMQ)
        print("== Change to proportion column")
        # gender별로 흡연 유무의 비율 지표로 변경해줍니다.
        # 더 짧은 명령어가 있으나, 가독성을 위해, 조금 길게 설명해보았습니다.
        # CT_Gender_SMQ = CT_Gender_SMQ.apply(lambda x: x/x.sum(), axis=1)
        CT_Gender_SMQ.columns = ['non_smoke_p', 'smoke_p']
        CT_Gender_SMQ['sum'] = CT_Gender_SMQ['non_smoke_p']+CT_Gender_SMQ['smoke_p']
        CT_Gender_SMQ['non_smoke_p'] /=CT_Gender_SMQ['sum']
        CT_Gender_SMQ['smoke_p'] /=CT_Gender_SMQ['sum']
        del CT_Gender_SMQ['sum']
        print(CT_Gender_SMQ)
        # 그리고, odds 를 의미하는 새로운 칼럼을 만들어주죠. 
        CT_Gender_SMQ["odds"] = CT_Gender_SMQ["smoke_p"] / CT_Gender_SMQ["non_smoke_p"]
        #CT_Gender_SMQ["odds"] = CT_Gender_SMQ.loc[:, 1] / CT_Gender_SMQ.loc[:, 0]
        print("== Add odds column")
        print(CT_Gender_SMQ)
        print("== Add log-odds column")
        CT_Gender_SMQ['logodds'] = np.log(CT_Gender_SMQ["odds"])
        print(CT_Gender_SMQ)
    # Create a labeled version of the educational attainment variable
    nhanes_df["DMDEDUC2x"] = nhanes_df["DMDEDUC2"].replace(
        {
            1: "lt9", 2: "x9_11", 3: "HS", 
            4: "SomeCollege",5: "College", 7: np.nan, 9: np.nan
        }
    )
    model = sm.GLM.from_formula(
        formula="smq ~ RIDAGEYR + RIAGENDRx + DMDEDUC2x", 
        family=sm.families.Binomial(), 
        data=nhanes_df
    )
    result = model.fit()
    print("== GLM ")
    print(result.summary())

```