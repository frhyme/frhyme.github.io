---
title: kaggle) bike sharind demand를 맞춰봅시다!
category: machin-learning 
tags: python kaggle machine-learning python-lib sklearn rmsle make_score 
---

## kaggle) bike sharing demand를 맞춰봅시다!

- 아주 행복하게도, missing value가 없습니다 개좋음!!
- Linear model로 했을때보다, randomforest를 넣었을때 훨씬 좋게 나옵니다. 사실 너무 당연한 거죠. 

## just do it. 

- 보통 저는, benchmark model로 만만한, linear model을 만듭니다. 저는 randomforest를 주로 쓰구요. 
- house price prediction을 할때는 gradient boosting method가 괜찮았는데, 여기서는 잘 먹히지 않아요. 흠. 
- 일단은 randomforest를 이용해서, 0.65정도를 찍었습니다. 이후에도 `MLPRegressor`도 써보고, linear model과 gradientboosting도 써봤으나, 잘 안되는 관계로, scoring에 문제가 있는 것은 아닐까, 라는 생각을 해봤습니다. 
- kaggle의 다양한 kernel들을 확인해보니, rmsle(root mean squared log error)를 사용하는 경우가 많아서, scoring을 바꾸고, GridSearchCV에서 해당 scoring을 사용하여 적절한 GradientBoosting model을 만들어봤으나, 여전히 잘 되지 않네요 제기랄. kernel에서 만든 모델과 별 차이 없는데 왜 그럴까요 흠. 
- 그만할래요. 후. 
- 저의 경우는 RandomforestRegressor를 쓴 경우가 GradientBoosting보다 잘 나왔습니다. 

```python
import numpy as np 
import pandas as pd

from sklearn.preprocessing import MinMaxScaler, RobustScaler
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.linear_model import LinearRegression, Lasso
from sklearn.metrics import make_scorer, mean_squared_error, make_scorer
from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor
from sklearn.neural_network import MLPRegressor

train_url = ""
test_url = ""

train_df = pd.read_csv(train_url)
test_df = pd.read_csv(test_url)

#train_df = train_df[train_df['count'] < (count_mean + 3* count_std)].reset_index(drop=True)

count_mean = train_df['count'].mean()
count_std = train_df['count'].std()
train_df = train_df[train_df['count'] < (count_mean + 3* count_std)]
print("reading data complete")

def rmsle(actual_values, predicted_values, convertExp=True):
    """
    - root mean squared log error는 error를 로그화값으로 변환하고, 제곱하고, 평균을 내고, 루트를 씌웁니다.
    - skewness를 해결하기 위해 np.log1p를 했기 때문에, 값을 예측할 때 이를 다시 변환해서 처리해주는 것이 필요합니다. 
    """
    if convertExp==True:
        predicted_values = np.exp(predicted_values),
        actual_values = np.exp(actual_values)
        
    log_predicted_values = np.log(np.array(predicted_values)+1)
    log_actual_values = np.log(np.array(actual_values)+1)

    # 위에서 계산한 예측값에서 실제값을 빼주고 제곱을 해준다.
    difference = np.square(log_predicted_values - log_actual_values)
    return np.sqrt(difference.mean())

def preprocessingX(input_df):
    r_df = input_df.copy()
    r_df['datetime'] = pd.to_datetime(r_df['datetime'])
    r_df['weekday'] = r_df['datetime'].apply(lambda d: d.weekday())
    r_df['year'] = r_df['datetime'].apply(lambda dt: dt.year)
    r_df['month'] = r_df['datetime'].apply(lambda dt: dt.month)
    r_df['days'] = r_df['datetime'].apply(lambda dt: dt.day)
    r_df['hour'] = r_df['datetime'].apply(lambda dt: dt.hour)
    r_df['day_from_start'] = (r_df['datetime'] - r_df['datetime'][0]).apply(lambda td: td.days)
    r_df['day_from_start//30'] = r_df['day_from_start']//30
    r_df['day_from_start/180'] = r_df['day_from_start']//180
    r_df['non_windspeed'] = r_df['windspeed'] ==0
    try:
        del r_df['registered']
        del r_df['casual']
    except:
        pass
    del r_df['datetime']
    ## making categorical colm
    for col in ['holiday', 'season', 'workingday', 'hour']:
        r_df = r_df.join(pd.get_dummies(r_df[col], prefix=col)) 
    r_df_v = r_df.values
    #r_df_v = RobustScaler().fit_transform(r_df_v)
    ##r_df_v = MinMaxScaler().fit_transform(r_df_v)
    return pd.DataFrame(r_df_v, columns=r_df.columns)

# outlier removal 

x = preprocessingX(train_df[list(set(train_df.columns)-set(['count']))])
y = train_df['count']
y_log = np.log1p(y)

x_train, x_test, y_train, y_test = train_test_split(x.values, y_log, train_size=0.8, test_size=0.2, random_state=42)

#reg = GradientBoostingRegressor(n_estimators=5000, alpha=0.01)
#reg = MLPRegressor(hidden_layer_sizes=[512, 64, 4], max_iter=1000, alpha=0.005, random_state=42)

#reg = GridSearchCV(  Lasso(), { 'max_iter':[3000], 'alpha':1/np.array([0.1, 1, 2, 3, 4, 10, 30,100,200,300,400,800,900,1000])}, cv=5)
#reg = GridSearchCV(GradientBoostingRegressor(), {"n_estimators":[5, 500, 1000], 'alpha':[0.001, 0.01, 0.1, 0.5]}, scoring=make_scorer(rmsle))

reg = GridSearchCV(GradientBoostingRegressor(), {"n_estimators":[4000], 'alpha':[0.01]}, cv=3,
                   scoring=make_scorer(rmsle))
reg = GridSearchCV(RandomForestRegressor(), {"n_estimators":[5, 50, 100, 500]}, cv=3,
                   scoring=make_scorer(rmsle))
reg.fit(x.values, y_log)

## submission 
submit_df = pd.DataFrame({'datetime':test_df['datetime'], 
                          'count':[max(0, x) for x in np.exp(reg.predict(preprocessingX(test_df)))],
                          #'count':list(map(lambda x: round(x, 0), np.exp(reg.predict(preprocessingX(test_df)))))
                         })
submit_df.to_csv('bycicle.csv', index=False)
print("----complete----")
```


## wrap-up 

- 처음에는 시간에 따른 변화를 어떻게 트래킹할 수 있을까? 라고 생각했는데, 거시적으로 추정할 것이라면, 그냥 처음 시작부터 날짜를 하나의 변수로 집어넣으면 된다. 
- 그렇게 만들면, 시간의 흐름에 따라 증가하는 것을 알 수있고, 요일 등의 변수를 이용해서 대략 적으로 추정할 수 있음. 
- fitting할 때, param_grid에만 신경을 많이 쓰곤 하는데, scoring을 잘 이용하는 것 또한 매우 중요하다. 경우에 따라 적합한 scoring을 정의하여 주는 것이 필요하며, 이를 위해서 sklearn에 있는 make_score를 쓰는 것이 필요하다. 

## reference 

- <https://programmers.co.kr/learn/courses/21/lessons/945>