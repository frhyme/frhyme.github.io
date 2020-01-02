---
title: pandas에서 time series 활용하기
category: python-lib
tags: python python-lib pandas time-series matplotlib datetime

---

## pandas에서 time series 활용하기

- 최근에 kaggle에서 뭘 좀 하다가, time series 데이터를 분석할 일이 있었습니다. 생각해보니, 예전에도 datacamp에서 사용했던 적이 있었는데, 아무튼 기본적인 time series 활용법을 정리해두려고 합니당. 
- 우선 제가 참고한 포스트에서는 `pandas-datareader`에서 데이터를 가져와서 분석합니다. 저도 같은 방식으로 진행할 것이기 때문에 `conda install pandas-datareader`을 해주세용
- 라고 했으나, 다음 오류가 발생합니다. google finance API가 더이상 지원되지 않는 것 같습니다. 망했네요. 그냥 random walk 데이터를 이용해서 진행하겠습니다. 후 
    - 실제 데이터를 이용할 경우, 주기에 따른 데이터 변화가 좀 더 명확하게 드러나는 반면, 저는 그냥 간단한 random walk로 데이터를 만들었기 때문에, 그 주기성이 부족할 것 같아요. 

```
/Users/frhyme/anaconda3/lib/python3.6/site-packages/pandas_datareader/google/daily.py:40: UnstableAPIWarning: 
The Google Finance API has not been stable since late 2017. Requests seem
to fail at random. Failure is especially common when bulk downloading.

  warnings.warn(UNSTABLE_WARNING, UnstableAPIWarning)
```

## resampling and rolling 

- 일단, random walk를 값으로 가지고, index가 datetime의 형태인 dataframe을 만들었습니다. 
- resampling과 rolling은 groupby와 거의 같습니다. 일정 주기로 값을 묶어서 그룹별로 게산해주죠. 

```python
import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt

idx = pd.date_range('2000-01-01', '2018-01-01')
df = pd.DataFrame({'x':np.cumsum(np.random.normal(0, 1, len(idx))*10)}, 
                  index = idx)

plt.figure(figsize=(15, 5))
plt.plot(df.index, df['x'])
plt.plot(df.resample('W').mean(), label='Week')
plt.plot(df.resample('M').mean(), label='Month')
plt.plot(df.rolling(180).mean(), label='180D')
plt.plot(df.resample('A').mean(), label='annual')
plt.legend()
plt.savefig("../../assets/images/markdown_img/180612_1422_df_time_series.svg")
plt.show()
```

![](/assets/images/markdown_img/180612_1422_df_time_series.svg)

## time shift 

- 간단하게 `shift`로 시간을 옮길 수 있습니다. 이는 만약 우리가 사용하는 데이터가 60일을 주기로 autocorrelation을 가진다면, `shift(60)`으로 새로운 칼럼을 만들어서 사용할 수 있다는 것을 의미합니다. 쓰고 보니 뭐낙 비문인데 고치기 귀찮네요 하하핫

```python
for shift_v in [-1, 1, 2]:
    df["shift_{}".format(shift_v)] = df['x'].shift(shift_v)
print(df.head(10))
```

```
                   x   shift_-1    shift_1    shift_2
2000-01-01 -12.235593 -11.298887        NaN        NaN
2000-01-02 -11.298887  15.379539 -12.235593        NaN
2000-01-03  15.379539  19.195769 -11.298887 -12.235593
2000-01-04  19.195769  16.808412  15.379539 -11.298887
2000-01-05  16.808412  17.593410  19.195769  15.379539
2000-01-06  17.593410  17.818314  16.808412  19.195769
2000-01-07  17.818314  22.679743  17.593410  16.808412
2000-01-08  22.679743  29.726933  17.818314  17.593410
2000-01-09  29.726933  34.502865  22.679743  17.818314
2000-01-10  34.502865   6.953065  29.726933  22.679743
```

## wrap-up

- 요즘, 아주 간단한 것들인데 이렇게 포스트로 쓰는 일들이 좀 있네요. 무언가 고민하면서 문제를 풀다 보면, 한번씩 자잘한데, 자주 까먹고, 또 써두지 않으면 나중에 번거로운 일들이 있습니다. 이 포스트도 사실 나중에 덜 번거로우려고 써두었습니다. 하하핳

## reference 

- <https://jakevdp.github.io/PythonDataScienceHandbook/03.11-working-with-time-series.html>