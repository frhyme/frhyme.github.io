---
title: Fitting Statistical Models to Data with Python - WEEK 2 - Part 1
category: python-libs
tags: python python-libs coursera statsmodel statistics
---

## WEEK 2 - FITTING MODELS TO INDEPENDENT DATA - PART 1

- 2주차에는 linear regression과 logistic regression을 배운다. 그리고, 이 모델의 정확도를 어떻게 측정할 수 있는지에 대해서 평가하고 그 결과를 해석하기도 한다.

## Linear regression modelling: one ind var.

- 아주 간단한 모형인, linear regression을 모델링합니다. 각 변수에 대한 설명은 다음과 같습니다. 
    - Y: `BPXSY1` : 피실험자에 대해서 1번째로 측정된 Bloods pressure
    - X: `RIDAGEYR` : 피실험자의 나이.
- 즉, 여기서는, "피실험자의 나이"라는 변수가, "혈압"에 영향을 미칠 것이다, 라는 것을 가정하고 모델을 세운 것이죠. (또한, 지금은 중요하지 않지만, BP가 "***1번째 측정된***" 이라는 말에 유의하세요). 
- 아래와 같이, 간단한 모델을 세우고 dataframe과 formula를 함께 넘겨줍니다.

```python 
# Read and Process data
# file link  
# https://github.com/kshedden/statswpy-nhanes/blob/master/merged/nhanes_2015_2016.csv
nhanes_df = pd.read_csv("nhanes_2015_2016.csv")
print(nhanes_df.columns)
# 필요한 칼럼만 선택하고, 필요없는 것들 삭제 
vars = ["BPXSY1", "RIDAGEYR", "RIAGENDR", "RIDRETH1", "DMDEDUC2", "BMXBMI", "SMQ020"]
nhanes_df = nhanes_df[vars].dropna()
print("== csv file processed")

OLS = True
if OLS==True:
    print("== OLS summary")
    model = sm.OLS.from_formula("BPXSY1 ~ RIDAGEYR", data=nhanes_df)
    result = model.fit()
    print(result.summary())
    print("== OLS done")
```

- 실행 결과는 다음과 같습니다. 

```
== csv file processed
== OLS summary
                            OLS Regression Results
==============================================================================
Dep. Variable:                 BPXSY1   R-squared:                       0.207
Model:                            OLS   Adj. R-squared:                  0.207
Method:                 Least Squares   F-statistic:                     1333.
Date:                Thu, 16 Jan 2020   Prob (F-statistic):          2.09e-259
Time:                        16:32:25   Log-Likelihood:                -21530.
No. Observations:                5102   AIC:                         4.306e+04
Df Residuals:                    5100   BIC:                         4.308e+04
Df Model:                           1
Covariance Type:            nonrobust
==============================================================================
                 coef    std err          t      P>|t|      [0.025      0.975]
------------------------------------------------------------------------------
Intercept    102.0935      0.685    149.120      0.000     100.751     103.436
RIDAGEYR       0.4759      0.013     36.504      0.000       0.450       0.501
==============================================================================
Omnibus:                      690.261   Durbin-Watson:                   2.039
Prob(Omnibus):                  0.000   Jarque-Bera (JB):             1505.999
Skew:                           0.810   Prob(JB):                         0.00
Kurtosis:                       5.112   Cond. No.                         156.
==============================================================================

Warnings:
[1] Standard Errors assume that the covariance matrix of the errors is correctly specified.
== OLS done
```

### coefficient

- `coef`: X라는 변수가 Y라는 변수에 얼마나 민감하게 영향을 주는가?에 대한 것을 말하죠. 소위 기울기, 와 같은 것이고, 대략적인 구간도 알 수 있습니다. `RIDAGEYR`는 0.4759의 coef를 가지죠. 즉, 1년은 `BPXSY1`에 0.48만큼의 변화를 가져온다, 라고 할 수 있죠. 그리고 p-value 또한, 충분히 작기 때문에, 매우 유효하다고 할 수 있습니다. 

### R-squared and correlation

- 흔히, 독립변수(independent var)가 종속변수(dependent var)의 분산을 얼마나 잘 설명하는지, 이를 설명하기 위한 값으로, `R-squared`가 사용됩니다(물론, 현재 방정식에서는 1개의 독립변수와 1개의 종속 변수가 사용되어, correlation과 별 차이가 없습니다만)
- 위 표에서 보는 값은 0.207이며, 이는, 종속 변수의 변화의 21%가 독립변수에 의해서 결정된다는 이야기죠. 

## Linear regression modelling: two ind var.

- 사실, 1개의 독립변수로 종속 변수를 예측하는 경우는 잘 없죠. 그래서, 여기서는 하나의 종속 변수를 더 추가해봅니다. 아마도, 2개의 종속 변수를 사용해서 예측한다면, 보다 정확하게 나오지 않을까(즉 R-Square 값이 커지지 않을까?)라고 상상해봅니다.
- 본 코스에서는 `RIAGENDR`라는, 성별을 의미하는 categorical value를 집어넣습니다. 보통, 다른 머신러닝 패키지에서는 이 값을, numerical value로 바꾸는데, 여기서는 그냥 "Male", "Female"인 문자열로 바꾸어 집어넣습니다. 알아서 잘 해석하나봅니다. 

```python
nhanes_df = pd.read_csv("nhanes_2015_2016.csv")
#print(nhanes_df.columns)
# 필요한 칼럼만 선택하고, 필요없는 것들 삭제 
vars = ["BPXSY1", "RIDAGEYR", "RIAGENDR", "RIDRETH1", "DMDEDUC2", "BMXBMI", "SMQ020"]
nhanes_df = nhanes_df[vars].dropna()
nhanes_df["RIAGENDRx"] = nhanes_df.RIAGENDR.replace({1: "Male", 2: "Female"})
print("== csv file processed")

print("== OLS summary")
model = sm.OLS.from_formula("BPXSY1 ~ RIDAGEYR + RIAGENDRx", data=nhanes_df)

result = model.fit()
print(result.summary())
print("== OLS done")
```

```
== csv file processed
== OLS summary
                            OLS Regression Results
==============================================================================
Dep. Variable:                 BPXSY1   R-squared:                       0.215
Model:                            OLS   Adj. R-squared:                  0.214
Method:                 Least Squares   F-statistic:                     697.4
Date:                Thu, 16 Jan 2020   Prob (F-statistic):          1.87e-268
Time:                        16:48:59   Log-Likelihood:                -21505.
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
== OLS done
```

- 이제 이 모델은 "나이"와 "성별"을 사용하여 BP의 변화 정도를 설명할 수 있습니다. 
    - `coef`에 따르면, 1년이 추가될수록 0.47의 혈압이 높아지고, 성별은 Male의 경우 3.23이 더 높다고 표시됩니다. 또한, 나이의 경우는 새로운 변수인 "성별"이 추가되기 전과 이후의 `coef`의 변화가 거의 없습니다. 이는 보통, 이 둘간의 상관관계가 없음을 의미하죠. 


- categorical variable은 리그레션 모델에서 covariate(공변량)으로 사용되며, 

reference level은 그 category를 기본값으로 정한다는 말이다. 마치, 이전에 "Male의 경우 3.23이 더 높아지도록 설계된 것은 Female이 reference level이기 때문"이다. 당연하지만, 만약 "male을 reference level로 잡는다면, 해당 coefficient는 -3.23이 될것이다". 
- categorical variable은 보통 dummy variable로 변환된다. 즉, category가 3개라면, 3개의 칼럼을 만들어서 각 칼럼의 True/Fale를 말해주는 형태를 말한다. 즉, `statsmodels`에서도 동일하며, 여성을 reference level로 잡고, 남성이라는 칼럼을 만들어서, 0 or 1로 세팅해주는 것을 말한다.


## Linear regression modelling: Three ind var.

- 이번에는 `BMXBMI`, BMI라는 칼럼을 추가하였으며, 당연히도 `R_square` 값이 소폭 상향되었고, `coef` 도 유효하다.

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

print("== OLS summary")
model = sm.OLS.from_formula("BPXSY1 ~ RIDAGEYR + BMXBMI + RIAGENDRx", data=nhanes_df)
result = model.fit()
print(result.summary())
print("== OLS done")
```

```
== csv file processed
== OLS summary
                            OLS Regression Results
==============================================================================
Dep. Variable:                 BPXSY1   R-squared:                       0.228
Model:                            OLS   Adj. R-squared:                  0.228
Method:                 Least Squares   F-statistic:                     502.0
Date:                Thu, 16 Jan 2020   Prob (F-statistic):          8.54e-286
Time:                        17:03:52   Log-Likelihood:                -21461.
No. Observations:                5102   AIC:                         4.293e+04
Df Residuals:                    5098   BIC:                         4.296e+04
Df Model:                           3
Covariance Type:            nonrobust
=====================================================================================
                        coef    std err          t      P>|t|      [0.025      0.975]
-------------------------------------------------------------------------------------
Intercept            91.5840      1.198     76.456      0.000      89.236      93.932
RIAGENDRx[T.Male]     3.5783      0.457      7.833      0.000       2.683       4.474
RIDAGEYR              0.4709      0.013     36.582      0.000       0.446       0.496
BMXBMI                0.3060      0.033      9.351      0.000       0.242       0.370
==============================================================================
Omnibus:                      752.325   Durbin-Watson:                   2.040
Prob(Omnibus):                  0.000   Jarque-Bera (JB):             1776.087
Skew:                           0.847   Prob(JB):                         0.00
Kurtosis:                       5.343   Cond. No.                         316.
==============================================================================

Warnings:
[1] Standard Errors assume that the covariance matrix of the errors is correctly specified.
== OLS done
```

## wrap-up

- `statsmodels`에서 비교적 간단한 linear regression model을 구현하였다. 기본적인 Ordinary Least Square method를 사용하여, 예측치와 실제치의 차이를 최소화하는 parameter를 추정하는 식으로 진행되었다. 
- 특히, 독립변수가 1개일 때와, 2개, 3개 일때로 늘어나는 것을 통해, R-squared 값이 어떻게 달라지는지, 그리고 coef값이 무슨 의미를 가지며, 변수가 추가되면서 coef가 줄어들거나 할경우, 각 칼럼간의 상관관계(correlation)을 통해 서로 어떤 관련성이 있는지 등을 파악하는 것이 중요하다는 것. 그리고, coef 또한, p-value를 가지며, 너무 작은 값에 대해서는 유효하지 않다는 것 정도를 배웠다.
- 그 외로, 해당 모델을 시각화하는 방법들에 대해서도 배웠으나, 이 부분은 그저 제외하였다.