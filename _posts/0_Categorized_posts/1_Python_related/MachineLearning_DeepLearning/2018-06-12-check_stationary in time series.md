---
title: time series의 stationarity를 체크해봅시다. 
category: python-lib
tags: python python-lib time-series stationarity statsmodels pandas numpy matplotlib

---

## time series의 stationarity를 체크해봅시다. 

- 말로 하기는 좀 귀찮으니까, 그림을 봅시다 허허. 아래 그림을 보시면, stationary time series와 non-stationary time series가 나타나 있습니다. 간단히 말하면, stationary의 경우는 시간이 변해도, 일정한 분포를 따르는 경우를 말하고, non-stationary 의 경우는 시간이 변해도, 일정한 분포를 따르지 않는 경우를 말합니다. 
- time series를 분석할 때, stationarity, 간단히 말하면 통계적 일관성이라고 말할 수도 있겠네요. 이게 지켜지면 얼마나 좋겠냐만, 보통은 지켜지지 않습니다. seasonality가 들어가거나, trend(값이 계속 증가하는 추세이거나) 등등의 변화로 인해 이 성질은 지켜지는 것이 어렵죠. 

![](https://upload.wikimedia.org/wikipedia/commons/thumb/e/e1/Stationarycomparison.png/390px-Stationarycomparison.png)

## check for stationarity

- [제가 참고한 포스트](https://machinelearningmastery.com/time-series-data-stationary-python/)에서는 우리가 가진 time series가 stationarity 성질을 갖추고 있는지 확인하기 위해서는 다음 세 가지 정도의 방법이 있다고 합니다. 
    - 눈으로 보기: 직접 plotting해서 시간에 따라 변하는지 볼 것
    - 간단한 평균 내보기: 대략 반으로 쪼개서 앞의 평균과 뒤의 평균이 얼마나 다른지 볼 것
    - statistical test: 통계적 검정하기

## do it. 

- 직접 해보도록 합니다. 여기서는 두 데이터 set을 사용합니다. 

### just plotting 

- 일단 그냥 그림으로도 airline passenger는 확실한 trend가 보입니다. 또 seasonal effect도 분명하게 보입니다. 그래서 non-stationary하죠. 
- 다만 female birth는 trend는 없는데, seasonal effect가 있는건지 아직은 잘 모르겠어요. 
- 또한, histogram을 봐도, airline passenge는 gaussian dist를 따르지 않는 것처럼 보이죠. female birth는 약간 따르는 것처럼 보입니다. gaussian을 따르는지 여부 또한, 중요한 stationarity check 기법 중 하나입니다. 
- 또한, data를 두 그룹으로 나누어(시간상 앞쪽인 그룹과, 뒤쪽인 그룹) 평균과 표준편차를 비교해보아도 비슷한 결과가 나오죠. 

```python
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns 
import numpy as np 

df_airline = pd.read_csv('/Users/frhyme/Downloads/international-airline-passengers.csv')[:-1]
df_airline.columns = ['m', 'q']
df_female = pd.read_csv('/Users/frhyme/Downloads/daily-total-female-births-in-cal.csv')[:-1]
df_female.columns = ['m', 'q']

## 1) just plotting 
f, axes = plt.subplots(1, 2, figsize=(14, 4))
axes[0].plot(df_airline['q'])
axes[0].set_title("air line passenger")
axes[1].plot(df_female['q'])
axes[1].set_title("femail birth")
plt.savefig("../../assets/images/markdown_img/180612_1811_just_plotting.svg")
plt.show()

## 2) plot histogram to check to follow gaussian dist. 
f, axes = plt.subplots(1, 2, figsize=(14, 4))
sns.distplot(df_airline['q'], ax=axes[0])
axes[0].set_title("air line passenger")
sns.distplot(df_female['q'], ax=axes[1])
axes[1].set_title("femail birth")
plt.savefig("../../assets/images/markdown_img/180612_1815_hist_comp.svg")
plt.show()

## 3) mean variance comparision 
print("---airline passenger---")
print("mean of left group, right group: {}, {}".format(
    df_airline['q'][:len(df_airline)//2].mean(), df_airline['q'][len(df_airline)//2:].mean())
)
print("std of left group, right group: {}, {}".format(
    df_airline['q'][:len(df_airline)//2].std(), df_airline['q'][len(df_airline)//2:].std())
)

print("---female birth---")
print("mean of left group, right group: {}, {}".format(
    df_female['q'][:len(df_female)//2].mean(), df_female['q'][len(df_female)//2:].mean())
)
print("std of left group, right group: {}, {}".format(
    df_female['q'][:len(df_female)//2].std(), df_female['q'][len(df_female)//2:].std())
)
```

![](/assets/images/markdown_img/180612_1811_just_plotting.svg)

![](/assets/images/markdown_img/180612_1815_hist_comp.svg)

```
---airline passenger---
mean of left group, right group: 182.90277777777777, 377.69444444444446
std of left group, right group: 47.7042413215282, 86.4392058427729
---female birth---
mean of left group, right group: 39.76373626373626, 44.185792349726775
std of left group, right group: 7.034579412457393, 6.998305548491794
```

## Augmented Dickey-Fuller test 

- 하지만, 지금까지 체크하는 방법은 약간 공학적이지 못하죠. 마구잡이로 하는 느낌이어서, 정확한 통계적 검정 방법을 거치는 것이 필요합니다. 
- [Augmented Dickey-Fuller test](https://en.wikipedia.org/wiki/Augmented_Dickey–Fuller_test)
- 아주 간단하게는, p_value가 넘는지 안넘는지를 보면 됩니다. 아까 그림으로 대충 확인한 것처럼, airline passenger의 경우는 stationarity 성질이 없고, femail birth의 경우는 stationarity 성질이 있네요. 

```python
from statsmodels.tsa.stattools import adfuller

def print_adfuller(inputSeries):
    result = adfuller(inputSeries)
    print('ADF Statistic: %f' % result[0])
    print('p-value: %f' % result[1])
    print('Critical Values:')
    for key, value in result[4].items():
        print('\t%s: %.3f' % (key, value))

print_adfuller(df_airline['q'])
print("--------")
print_adfuller(df_female['q'])
print("--------")
```

```
ADF Statistic: 0.815369
p-value: 0.991880
Critical Values:
	1%: -3.482
	5%: -2.884
	10%: -2.579
--------
ADF Statistic: -4.808291
p-value: 0.000052
Critical Values:
	1%: -3.449
	5%: -2.870
	10%: -2.571
--------
```

## wrap-up

- 일종의 concept-drift가 구간 내에서 발생했는지를 파악하는 기법들입니다. 
- 그런데, stationary면 뭐가 좋은건가? 그냥 그 data가 homogeneous하고, 동일한 집단에서 나왔다는 것 말고는 무슨 의미가 있는거지? 분석 시에 뭐 더 좋아지는 것이 있나? 

## reference

- <https://machinelearningmastery.com/time-series-data-stationary-python/>