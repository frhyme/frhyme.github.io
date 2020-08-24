---
title: random walk를 정리해봅시다. 
category: python
tags: python python-lib random-walk matplotlib numpy pandas sklearn 
---

## random walk

- 일반적으로 random walk는 현재의 상태가 이전의 상태에 영향을 받으며 랜덤하게 움직이는 경우를 말합니다. 만약 10 step의 random walk라면, 각각의 값이 따로 있는 것이 아니라, sequential하게 이전의 값에 영향을 받은 상태로 있는 것이죠. 
- 주식의 차트처럼 시간에 따라 값이 바뀌는 것을 일반적으로 random walk로 모델링할 수 있습니다. random walk, random process 등이 연결되서 함께 알아야 하는데, 귀찮으니 나중에 압시다. 

## plotting random walk 

- 1d, 2d, 3d에 대해서 random walk를 만들고 이걸 plotting해봤습니다. 
- 그림에서 보는 것처럼 아주 단순하게 모델링한 결과인데 뭔가 많이 본 주식차트처러 나오는 것을 알 수 있습니다. 지금은 step별 결과를 -1, 1로 uniform dist.로 움직인다고 가정했지만, 다르게 세팅할수록 결과는 판이하게 달라지죠. 

```python
import numpy as np 
import matplotlib.pyplot as plt

## random walk in 1dim 
move_set = [-1, 1]
plt.figure(figsize=(15, 4))
for i in range(0, 5):
    xs = np.array([np.random.choice(move_set) for i in range(0, 100)])
    cum_xs = np.cumsum(xs)
    plt.plot(np.arange(0, len(xs)), cum_xs, linestyle='--', label='random_walk_{}'.format(i))
plt.legend()
plt.savefig('../../assets/images/markdown_img/180612_1143_random_walk_1d.svg')
plt.show()

## random walk in 2dim
move_set = [[-1, 0], [1, 0], [0, -1], [0, 1]]
plt.figure(figsize=(10, 10))
for i in range(0, 5):
    moves = [[0, 0]]+[move_set[np.random.randint(0, len(move_set))] for i in range(0, 300)]
    moves = np.array([np.array(m) for m in moves])
    cum_moves = np.cumsum(moves, axis=0)
    plt.plot(cum_moves[:, 0], cum_moves[:, 1], marker='o', alpha=0.5)
plt.savefig('../../assets/images/markdown_img/180612_1143_random_walk_2d.svg')
plt.show()

## random walk in 3dim
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

fig = plt.figure(figsize=(15, 12))
ax = fig.add_subplot(111, projection='3d')
## random walk in 2dim
move_set = [[-1, 0, 0], [1, 0, 0], [0, 0, -1], [0, 0, 1], [0, 1, 0], [0, -1, 0]]

for i in range(0, 5):
    moves = [[0, 0, 0]]+[move_set[np.random.randint(0, len(move_set))] for i in range(0, 500)]
    moves = np.array([np.array(m) for m in moves])
    cum_moves = np.cumsum(moves, axis=0)
    ax.plot(cum_moves[:, 0], cum_moves[:, 1], cum_moves[:, 2], 
            marker='o', markersize=3, linestyle='-', linewidth=2)
plt.savefig('../../assets/images/markdown_img/180612_1143_random_walk_3d.svg')
plt.show()
```

![](/assets/images/markdown_img/180612_1143_random_walk_1d.svg)

![](/assets/images/markdown_img/180612_1143_random_walk_2d.svg)

![](/assets/images/markdown_img/180612_1143_random_walk_3d.svg)

## auto-correlation 

- 한국어로 하면 "자기상관성"정도로 표현할 수 있는데, 현재 시점의 데이터가 이전의 데이터와 관련이 있는가? 를 의미하는 것이 auto-correlation임. 
- auto-correlation을 예측하는 방법은 time lag을 변화시켜가면서, 시점 t와 시점 t+s에서 시작되는 일정 시점의 데이터간에 유사도가 높다면(pearson_r, similiarity 등) 이 둘 간에는 auto-correlation이 높다고 할 수 있다. 
- 간단하게는 `pandas.plotting.autocorrelation_plot`을 활용해서 확인해볼 수도 있습니다만, 조금 다르지만, 경향성은 단순히 time lag을 변화해가면서 pearsonr_r(혹은 다른 similarity)를 확인하면서도 알 수 있어요. 
- 아래 그림에서 알 수 있는 것은 단순히 pearsonr을 계산해봐도 오른쪽의 auto-correlation plot과 비슷한 형태를 가진다는 것이죠. 물론 범위는 좀 다릅니다. 그리고, 뜬금없이 60정도의 lag에서 auto correlation이 확 오르는 것을 알 수 있습니다. 
    - 이는 우리가 사용한 데이터가 `np.sin`이고 50 step마다 다시 원래의 값으로 돌아오기 때문입니다. 

![](/assets/images/markdown_img/180612_1322_autocorrelation_plot.svg)

```python
from scipy.stats import pearsonr
import numpy as np 
import matplotlib.pyplot as plt
from pandas.plotting import autocorrelation_plot

#x = np.cumsum(np.random.normal(0, 1, 100))
x = np.sin(np.linspace(0, 3.14*4, 120)) # 60 step이 한 주기가 됨 

ac_lst = []
f, ax = plt.subplots(1, 2, figsize=(14, 4))
for lag in range(1, 80):
    ac_lst.append(pearsonr(x[0:len(x)-lag], x[lag:len(x)])[0])
ax[0].plot(np.arange(0, len(ac_lst)), ac_lst)
ax[0].set_title('pearsonr')
autocorrelation_plot(x, ax=ax[1])
ax[1].set_title('pandas.plotting.autocorrelation_plot')
plt.savefig('../../assets/images/markdown_img/180612_1322_autocorrelation_plot.svg')
plt.show()
```

## predicting time series data 

- 그렇다면, 만약 일정 주기로 sin곡선과 비슷한 값을 가지는 어떤 time series 데이터가 있다면 이 데이터를 예측할 수 있을까요? 한번 해봅시다. 
- 너무도 당연하게, 잘되네요. 해보니까 왜 했나 싶기도 한데...아무튼 뭐 그렇습니다. 

```python
import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

cycle = 10 # 몇 개의 cycle
point_per_cycle = 30 # cycle 별로 몇 개의 데이터? 
df = pd.DataFrame({'x':np.sin(np.linspace(0, 3.14*cycle*2, cycle*point_per_cycle))},
                  index = pd.date_range('2018-01-01', periods=cycle*point_per_cycle)
                 )
df['x'] = np.arange(0, len(df))/len(df)*3 + df['x'] + np.random.normal(0, 0.3, cycle*point_per_cycle)
df['d'] = np.arange(0, len(df))

## time shifting data generation 
for shift_v in [30, 60, 120]:
    df['shift_{}'.format(shift_v)] = df['x'].shift(shift_v)
ind_columns = list(set(df.columns) - set(['x']))
df_dropna = df.dropna()
## data modeling and fitting
reg = LinearRegression()
reg.fit(df_dropna[ind_columns][:100], df_dropna['x'][:100])
## plotting
plt.figure(figsize=(12, 4))
plt.plot(df.index, df['x'], marker='o', alpha=0.5, label='y_true')
plt.plot(df_dropna.index, reg.predict(df_dropna[ind_columns]), 
         linestyle='--', linewidth=3, label='y_pred', color='red')
plt.legend()
plt.savefig('../../assets/images/markdown_img/180612_1454_timeseries-plotting_reg.svg')
plt.show()
```

![](/assets/images/markdown_img/180612_1454_timeseries-plotting_reg.svg)


## prediction random walk

- 막상 해보니까, 당연하게도 엉망으로 예측되는데, 사실 당연합니다...이거 왜했지...

```python
import numpy as np 
import matplotlib.pyplot as plt
import pandas as pd 
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor

sample_size = 1000
df_rw = pd.DataFrame({'x': np.cumsum(np.random.normal(0, 1, sample_size))}, 
                     index =  pd.date_range('2018-01-01', periods=sample_size)
                 )
for shift_v in [30, 50, 100, 200]:
    df_rw['shift_{}'.format(shift_v)] = df_rw['x'].shift(shift_v)

ind_columns = list(set(df_rw.columns) - set(['x']))
df_rw_dropna = df_rw.dropna()
## data modeling and fitting
reg_lin = LinearRegression()
reg_rf = RandomForestRegressor()

reg_rf.fit(df_rw_dropna[ind_columns][:len(df_rw_dropna)//2], df_rw_dropna['x'][:len(df_rw_dropna)//2])
reg_lin.fit(df_rw_dropna[ind_columns][:len(df_rw_dropna)//2], df_rw_dropna['x'][:len(df_rw_dropna)//2])

plt.figure(figsize=(12, 6))
plt.plot(df_rw['x'], label='y_true')
plt.plot(df_rw_dropna.index, reg_rf.predict(df_rw_dropna[ind_columns]), label='random forest', linestyle='--')
plt.plot(df_rw_dropna.index, reg_lin.predict(df_rw_dropna[ind_columns]), label='lin reg', linestyle=':')
plt.legend()
plt.savefig("../../assets/images/markdown_img/180612_1511_random_walk_fitting.svg")
plt.show()
```

![](/assets/images/markdown_img/180612_1511_random_walk_fitting.svg)

## wrap-up

- random walk에서 시작해서, time series로 빠져버린 느낌이 있는데, 뭐 어쩔수 없죠 하하핫
- 다음에는 rnn을 이용해보겠숩니다 


## reference 

- <http://adventuresinmachinelearning.com/keras-lstm-tutorial/>
- <https://en.wikipedia.org/wiki/Random_walk>
- <https://machinelearningmastery.com/gentle-introduction-autocorrelation-partial-autocorrelation/>