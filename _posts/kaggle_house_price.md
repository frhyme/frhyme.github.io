---
title: kaggle) 집 가격을 예측해 봅시다. 
category: machine-learning
tags: kaggle machine-learning python python-lib sklearn

---

## kaggle) 집 가격을 잘 예측해봅시다. 

- 이 문제는 간단히 말하면, regression 문제네요. 이전에 풀어본 mnist, titanic의 경우는 classification의 문제에 속했는데, 이 문제는 regression 문제입니다. 
- 다 좋은데, 대략 data를 보면, 너무 다양한 column이 있습니다. categorical, numerical data가 섞여 있는데, 이 중에서 어느 놈이 유의미한지 찾는 것이 이번 kaggle의 핵심이 되겠네요. 또한, 이 feature들을 잘 조합하여, 새로운 feature를 뽑아내는 것들, **feature engineering**이 가장 중요한 것 같습니다. 
- 이번에는 하나씩, 칼럼을 하나씩 늘려가면서, 잘 맞추는지를 보려고 합니다. 제가 성격이 급해서 그걸 잘할 수 있을지 잘 모르겠지만 아무튼!

## column selection: corr and heatmap 

- numeric column의 경우는 일단 target variable에 영향을 많이 미치는 변수들을 뽑아서 scaling하고 log-normalization하면서 진행하면 됩니다.
    - missing value의 경우는 일단 `fillna(mean)`로 하면 되고요. 

- 그런데, non-numeric column의 경우는 간단하게 이 값들이 target variable에 영향을 미치는지 아닌지 확인이 어렵습니다. 
    - class별로 target variable의 변화에 관여하는지를, group별로 평균을 내서 볼 수도 있지만, 그냥 다 귀찮고, `pd.get_dummies()`로 한번에 다 해결할 거에요. 
    - 단 이를 위해서는, test_df의 column에 있는 value set와 train_df의 column의 value set가 같아야 합니다(예를 들어, '지역'이라는 칼럼에 train_df에서는 ['천안', '서울']이 있었다면, test_df에서도 반드시 ['천안', '서울']만 있어야 함). 그렇지 않을 경우, 매우 성가셔 집니다. 그리고, 노력 대비 효과가 있는지도 잘 모르겠습니다. 

### numeric column selection 

- data set을 보면, numeric column과 non numeric column이 섞여 있습니다. 
- numeric column은 그 값을 그대로 사용해도 되지만, non numeric column은 `pd.get_dummies()`를 이용해서 feature를 분화한다음에 사용해야 합니다. 
- 현재 데이터 set에 column의 수가 너무 많고, missing value도 섞여 있기 때문에, 한꺼번에 다 넣으면 답이 없습니다. 오히려, 전체 column중에서 우리가 예측하려고 하는 target valued인 `SalePrice`에 영향을 미치는 것이 무엇인지를 보고, 순서대로 하나씩 넣어주는 것이 좋아요. 
- 또한, feature 간에도 비슷한 것이 있고, 독립적인 것들이 있습니다. 이는 `sns.heatmap`을 통해서 볼 수 있어요. 

```python
import pandas as pd
import sklearn
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import skew, pearsonr

from sklearn.preprocessing import MinMaxScaler, RobustScaler
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.linear_model import ElasticNet, Lasso,  BayesianRidge, LassoLarsIC
from sklearn.model_selection import GridSearchCV
from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor
from sklearn.tree import DecisionTreeRegressor
from sklearn.neural_network import MLPRegressor
from sklearn.pipeline import make_pipeline
from sklearn.kernel_ridge import KernelRidge
import xgboost as xgb

"""
- 전체 칼럼 중에서, numeric과 non-numeric 을 구분합니다. 
"""
cols = train_df.columns
NumericCols = []
nonNumericCols = []
for c in cols:
    col_dtype= train_df[c].dtype
    if col_dtype in ['int64', 'float64']:
        NumericCols.append(c)
    else:
        nonNumericCols.append(c)
print("Numeric Cols")
print(NumericCols)
print("------------")
print("NonNumeric Cols")
print(nonNumericCols)
print("------------")

"""
- numeric column에 대해서 correlation matrix를 구성한 다음, 
- SalePrice에 영향을 미치는 상위 10가지 index에 대해서 correlation matrix를 활용하여 
- sns.heatmap으로 확인함. 
"""
top_10_index = train_df[NumericCols].corr()['SalePrice'].sort_values(ascending=False)[:10].index

plt.figure(figsize=(15, 6))
sns.heatmap(train_df[top_10_index].corr(), 
            annot=True, 
            linewidths = 3, 
            cbar=True, 
            fmt=".2f"
           )

plt.tick_params(labelsize=13)
plt.gca().xaxis.tick_top() 
plt.xticks(rotation=45)
plt.yticks(rotation=0)
plt.savefig('../../assets/images/markdown_img/180606_2223_corr_heatmap_top_10_col.svg')
plt.show()
```

```
Numeric Cols
['Id', 'MSSubClass', 'LotFrontage', 'LotArea', 'OverallQual', 'OverallCond', 'YearBuilt', 'YearRemodAdd', 'MasVnrArea', 'BsmtFinSF1', 'BsmtFinSF2', 'BsmtUnfSF', 'TotalBsmtSF', '1stFlrSF', '2ndFlrSF', 'LowQualFinSF', 'GrLivArea', 'BsmtFullBath', 'BsmtHalfBath', 'FullBath', 'HalfBath', 'BedroomAbvGr', 'KitchenAbvGr', 'TotRmsAbvGrd', 'Fireplaces', 'GarageYrBlt', 'GarageCars', 'GarageArea', 'WoodDeckSF', 'OpenPorchSF', 'EnclosedPorch', '3SsnPorch', 'ScreenPorch', 'PoolArea', 'MiscVal', 'MoSold', 'YrSold', 'SalePrice']
------------
NonNumeric Cols
['MSZoning', 'Street', 'Alley', 'LotShape', 'LandContour', 'Utilities', 'LotConfig', 'LandSlope', 'Neighborhood', 'Condition1', 'Condition2', 'BldgType', 'HouseStyle', 'RoofStyle', 'RoofMatl', 'Exterior1st', 'Exterior2nd', 'MasVnrType', 'ExterQual', 'ExterCond', 'Foundation', 'BsmtQual', 'BsmtCond', 'BsmtExposure', 'BsmtFinType1', 'BsmtFinType2', 'Heating', 'HeatingQC', 'CentralAir', 'Electrical', 'KitchenQual', 'Functional', 'FireplaceQu', 'GarageType', 'GarageFinish', 'GarageQual', 'GarageCond', 'PavedDrive', 'PoolQC', 'Fence', 'MiscFeature', 'SaleType', 'SaleCondition']
------------
```

![](/assets/images/markdown_img/180606_2223_corr_heatmap_top_10_col.svg)

### non-numeric columns 

- 그냥 간단하게 다음 처럼 해결했씁니다. 
- `both_non_numeric_cols`라는 리스트에 양쪽에 모두 같은 value set에 있는 칼럼들만 넣어 줬습니다. 

```python
both_non_numeric_cols = []
for col in nonNumericCols:
    try:
        if set(train_df[col])==set(test_df[col]):
            both_non_numeric_cols.append(col)
    except:
        continue
print(both_non_numeric_cols)
```

```
['Street', 'Alley', 'LotShape', 'LandContour', 'LotConfig', 'LandSlope', 'Neighborhood', 'Condition1', 'BldgType', 'RoofStyle', 'MasVnrType', 'ExterQual', 'ExterCond', 'Foundation', 'BsmtQual', 'BsmtCond', 'BsmtExposure', 'BsmtFinType1', 'BsmtFinType2', 'HeatingQC', 'CentralAir', 'FireplaceQu', 'GarageType', 'GarageFinish', 'GarageCond', 'PavedDrive', 'Fence', 'SaleCondition']
```

## preprocessing and modeling 

- skewness가 높은 경우, `np.log`를 활용해 skewness를 줄여주고, 
- numeric columns에 대해서는 fillna로 일단은 간단하게 처리하고 
- non-numeric columns에 대해서는 `pd.get_dummies()`로 간단하게 처리합니다. 
- 이 결과로 나온 데이터를 일괄적으로 다양한 모델에 넣고 그 값들의 평균을 계산해줍니다. 
- 그 값으로 예측해야 잘 나옴 끝!

```python
def preprocessingX(input_df):
    r = pd.DataFrame({
        'OverallQual': input_df['OverallQual'], # categorical 
        'GrLivArea': np.log(input_df['GrLivArea']), #categorical, skewed
        'GarageCars': input_df['GarageCars'].fillna(input_df['GarageCars'].mean()),# test case, nan exists
        'GarageArea': input_df['GarageArea'].fillna(input_df['GarageArea'].mean()), # test case, nan exists
        'TotalBsmtSF': input_df['TotalBsmtSF'].fillna(input_df['TotalBsmtSF'].mean()), # test case, nan exists
        'FullBath': input_df['FullBath'], 
        'YearBuilt': input_df['YearBuilt'],
        'YearRemodAdd': input_df['YearRemodAdd'],
        'GarageYrBlt': input_df['GarageYrBlt'].fillna(input_df['GarageYrBlt'].mean()),
        'TotalSF': input_df['TotalBsmtSF'].fillna(input_df['TotalBsmtSF'].mean()) + input_df['1stFlrSF'].fillna(input_df['1stFlrSF'].mean()) + input_df['2ndFlrSF'].fillna(input_df['2ndFlrSF'].mean())
    })
    
    for col in both_non_numeric_cols:
        r = r.join(pd.get_dummies(input_df[col].fillna('None'), prefix=col))
    r['HasBsmt'] = r['TotalBsmtSF'] > 0
    r['TotalSF'] = np.log1p(r['TotalSF'])
    r['TotalBsmtSF'] = np.log1p(r['TotalBsmtSF'])
    
    r = pd.DataFrame(MinMaxScaler().fit_transform(r), columns = r.columns)
    r = pd.DataFrame(RobustScaler().fit_transform(r), columns = r.columns)
    return scaler.fit_transform(r)

x_train = preprocessingX(train_df)
x_test = preprocessingX(test_df)

y_true = train_df['SalePrice']
y_true_log = np.log(train_df['SalePrice'])
"""

"""
models = [RandomForestRegressor(n_estimators=n) for n in [5, 10, 30, 50, 100]]
models+=[Lasso(alpha =0.0005, random_state=1)]
models+=[ElasticNet(alpha=0.0005, l1_ratio=.9, random_state=3)]
models+=[KernelRidge(alpha=0.6, kernel='polynomial', degree=2, coef0=2.5)]
models+=[GradientBoostingRegressor(n_estimators=3000, learning_rate=0.05,
                                   max_depth=4, max_features='sqrt',
                                   min_samples_leaf=15, min_samples_split=10, 
                                   loss='huber', random_state =5)]
models+=[xgb.XGBRegressor(colsample_bytree=0.4603, gamma=0.0468, 
                             learning_rate=0.05, max_depth=3, 
                             min_child_weight=1.7817, n_estimators=2200,
                             reg_alpha=0.4640, reg_lambda=0.8571,
                             subsample=0.5213, silent=1,
                             random_state =7, nthread = -1)
]
#models+= [MLPRegressor(hidden_layer_sizes = layers) for layers in [ [10 for i in range(0, 5)] ]]


x_train_sub1, x_train_sub2, y_train_sub1, y_train_sub2 = train_test_split(x_train, y_true_log, train_size=0.7, 
                                                                          random_state=42)

print("---")
for i,m in enumerate(models):
    print(i, m.__class__)
    m.fit(x_train_sub1, y_train_sub1)
    print("sub1: {}, sub2: {}".format(
        r2_score(y_train_sub1, m.predict(x_train_sub1)), 
        r2_score(y_train_sub2, m.predict(x_train_sub2))
    ))
    print("----")

# r2_score가 높은 순으로 model을 정렬해준다. 
models = sorted(models, key=lambda m: r2_score(y_train_sub2, m.predict(x_train_sub2)), reverse=True)

y_preds = np.array([m.predict(x_train_sub2) for m in models]).T
y_preds_mean = y_preds.mean(axis=1)

#y_preds_w_mean = y_preds.dot(np.array([0.1, 0.4, 0.0, 0.0, 0.2, 0.3, 0.0, 0.0]))

y_pred_log = np.sum([m.predict(x_test) for m in models], axis=0)/len(models)
#y_pred_w_log = np.array([m.predict(x_test) for m in models[:8]]).T.dot(np.array([0.1, 0.4, 0.0, 0.0, 0.2, 0.3, 0.0, 0.0]))

submit_df = pd.DataFrame({'Id':test_df['Id'], 'SalePrice':np.exp(y_pred_log)})
submit_df.to_csv('kaggle_house_price.csv', index=False)
print('complete')
```

```
---
0 <class 'sklearn.ensemble.forest.RandomForestRegressor'>
sub1: 0.9643347434729889, sub2: 0.8541013081097738
----
1 <class 'sklearn.ensemble.forest.RandomForestRegressor'>
sub1: 0.9730554277568784, sub2: 0.8630829970639083
----
2 <class 'sklearn.ensemble.forest.RandomForestRegressor'>
sub1: 0.9760136528673168, sub2: 0.8804436703679014
----
3 <class 'sklearn.ensemble.forest.RandomForestRegressor'>
sub1: 0.9782058227106628, sub2: 0.8820298019022488
----
4 <class 'sklearn.ensemble.forest.RandomForestRegressor'>
sub1: 0.979645767549436, sub2: 0.8825189970925168
----
5 <class 'sklearn.linear_model.coordinate_descent.Lasso'>
sub1: 0.9022879704145137, sub2: 0.8927393030082648
----
6 <class 'sklearn.linear_model.coordinate_descent.ElasticNet'>
sub1: 0.9030091080039795, sub2: 0.8923683751653151
----
7 <class 'sklearn.kernel_ridge.KernelRidge'>
sub1: 0.9064163209137375, sub2: 0.8907039596035089
----
8 <class 'sklearn.ensemble.gradient_boosting.GradientBoostingRegressor'>
sub1: 0.9764583223628012, sub2: 0.8885541742691342
----
9 <class 'xgboost.sklearn.XGBRegressor'>
sub1: 0.9474169814699833, sub2: 0.8938965875690038
----
complete
```

## y predicted weighted mean

- 총 10개의 model의 상위8개의 `r2_score`가 0.88이상 입니다. 이들의 weighted_mean을 구하면 정확도가 더 올라갈 수 있지 않을까요? 단순히 mean이 아니라 중요한 놈에게 weight를 더 주면 좋지 않을까요? 라고 생각했습니다
- 총 8가지의 model이라고 생각하고, 8개짜리 합이 1.0인 모든 array를 만드는 함수까지는 만들었는데, 이게, 계산 자체가 아주 많이 걸립니다. 
- 또한, step을 줄여서 그 결과를 확인해봤는데, 딱히 `r2_score`가 올라가지도 않는 것 같아요. 그래도 아까우니 일단 넣어놨습니다. 

```python
from itertools import product
import itertools

def divide_it_two_group(r_v = 1.0, step=0.05):
    return [[i*step, r_v-i*step] for i in range(0, int(r_v/step)+1)]
def divide_it_four_group(r_v = 1.0, step=0.05):
    all_g = []
    for left_v, right_v in divide_it_two_group(r_v, step):
        k = product(divide_it_two_group(left_v, step), 
                divide_it_two_group(right_v, step)
               )
        k = map(lambda x: list(itertools.chain.from_iterable(list(x))), k)
        all_g+=list(k)
    return all_g
def divide_it_eight_group(r_v = 1.0, step=0.05):
    all_g = []
    for left_v, right_v in divide_it_two_group(r_v, step):
        k = product(divide_it_four_group(left_v, step), 
                divide_it_four_group(right_v, step)
               )
        k = map(lambda x: list(itertools.chain.from_iterable(list(x))), k)
        all_g+=list(k)
    return all_g

xs_score_lst = []
for i, xs in enumerate(divide_it_eight_group(1.0, 0.2)):
    if i%500==0:
        print(i)
    xs_score_lst.append((xs, r2_score(y_train_sub2, 
                                      np.array([m.predict(x_train_sub2) for m in models[:8]]).T.dot(np.array(xs)))))
sorted(xs_score_lst, key=lambda x: x[1], reverse=True)[:5]
```

- 0.2 구간으로 고려했을 때, `[0.0, 0.4, 0.0, 0.0, 0.2, 0.2, 0.0, 0.19999999999999996]`이 가장 놓은 방법이라고는 하는데(model이 8개 일때), `r2_score`는 0.90112888432637572로 별로 올라가지 않네요. 
- 그냥 새로운 model을 몇 개 더 추가하는 게 더 좋은 방법일 것 같습니다. 

```
[([0.0, 0.4, 0.0, 0.0, 0.2, 0.2, 0.0, 0.19999999999999996],
  0.90112888432637572),
 ([0.0, 0.2, 0.2, 0.0, 0.2, 0.2, 0.0, 0.19999999999999996],
  0.90110879496652896),
 ([0.0, 0.0, 0.4, 0.0, 0.2, 0.2, 0.0, 0.19999999999999996],
  0.90108631456968791),
 ([0.0, 0.4, 0.0, 0.0, 0.2, 0.0, 0.2, 0.19999999999999996],
  0.90098165635136196),
 ([0.0, 0.2, 0.2, 0.0, 0.2, 0.0, 0.2, 0.19999999999999996],
  0.90096434620718768)]
```


## 최종 code

```python
```


## refernce

- <https://www.kaggle.com/c/house-prices-advanced-regression-techniques>
- <https://www.kaggle.com/pmarcelino/comprehensive-data-exploration-with-python>
- <https://www.kaggle.com/dansbecker/your-first-scikit-learn-model>
- <https://www.kaggle.com/serigne/stacked-regressions-top-4-on-leaderboard>