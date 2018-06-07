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
        'TotalSF': input_df['TotalBsmtSF'].fillna(input_df['TotalBsmtSF'].mean()) + input_df['1stFlrSF'].fillna(input_df['1stFlrSF'].mean()) + input_df['2ndFlrSF'].fillna(input_df['2ndFlrSF'].mean()),

        #'MasVnrArea':input_df['MasVnrArea'].fillna(input_df['MasVnrArea'].mean()),
        #'Fireplaces':input_df['Fireplaces'].fillna(input_df['Fireplaces'].mean()),
        #'TotRmsAbvGrd':input_df['TotRmsAbvGrd'].fillna(input_df['TotRmsAbvGrd'].mean()),   
    })
    """
    아래 변수들을 추가했는데(이 변수들은 SalePrice와의 corr이 0.3 정도)
    오히려, r2_score가 떨어져서 제외함.
    """
    
    for col in both_non_numeric_cols:
        r = r.join(pd.get_dummies(input_df[col].fillna('None'), prefix=col))
    r['HasBsmt'] = r['TotalBsmtSF'] > 0# TotalBsmtSF가 0인 경우는 basement가 없는 경우이므로, feature를 새로 만들어준다. 
    r['TotalSF'] = np.log1p(r['TotalSF']) # skewness를 조절
    r['TotalBsmtSF'] = np.log1p(r['TotalBsmtSF']) # skewness를 조절
    """
    최종 결정된 column들의 missing value, skewness 등을 체크한다. 
    """
    def print_missing_count_and_skewness():
        temp_r =pd.DataFrame({'missing_v':[r[col].isnull().sum() for col in r.columns], 
                             'skewness':[skew(r[col]) for col in r.columns], 
                             'uniq_count':[len(set(r[col])) for col in r.columns]
                            }, index=r.columns)
        return temp_r[temp_r['uniq_count']>5]
    #print(print_missing_count_and_skewness())
    
    r = pd.DataFrame(MinMaxScaler().fit_transform(r), columns = r.columns)
    r = pd.DataFrame(RobustScaler().fit_transform(r), columns = r.columns)
    return scaler.fit_transform(r)

x_train = preprocessingX(train_df)
x_test = preprocessingX(test_df)

y_true = train_df['SalePrice']
y_true_log = np.log(train_df['SalePrice'])
"""

"""
models = [RandomForestRegressor(n_estimators=n, random_state=42) for n in [10, 30, 50, 100]]
models+=[Lasso(alpha =0.0005, random_state=1)]
models+=[ElasticNet(alpha=0.0005, l1_ratio=.9, random_state=3)]
"""
KernelRidge를 gridsearch로 돌려본 결과, degree가 3일 때 더 좋았음. 
"""
models+=[KernelRidge(alpha=0.6, kernel='polynomial', degree=i, coef0=2.5) for i in range(2, 10)]

models+=[GradientBoostingRegressor(n_estimators=n_e, learning_rate=0.05,
                                   max_depth=4, max_features='sqrt',
                                   min_samples_leaf=15, min_samples_split=10, 
                                   loss='huber', random_state =5) for n_e in [3000, 5000]]
models+=[xgb.XGBRegressor(colsample_bytree=0.4603, gamma=0.0468, 
                             learning_rate=0.05, max_depth=3, 
                             min_child_weight=1.7817, n_estimators=2200,
                             reg_alpha=0.4640, reg_lambda=0.8571,
                             subsample=0.5213, silent=1,
                             random_state =7, nthread = -1)]
models+=[xgb.XGBRegressor(colsample_bytree=0.4603, gamma=0.0468, 
                             learning_rate=0.05, max_depth=5, 
                             min_child_weight=1.7817, n_estimators=5000,
                             reg_alpha=0.4640, reg_lambda=0.8571,
                             subsample=0.5213, silent=1,
                             random_state =7, nthread = -1)]
models+=[xgb.XGBRegressor(colsample_bytree=0.4603, gamma=0.0468, 
                             learning_rate=0.05, max_depth=10, 
                             min_child_weight=1.7817, n_estimators=2200,
                             reg_alpha=0.4640, reg_lambda=0.8571,
                             subsample=0.5213, silent=1,
                             random_state =7, nthread = -1)]


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
#y_preds_mean = y_preds.mean(axis=1)
y_preds_mean = y_preds.dot(np.linspace(1.0, 0.0, len(models))/sum(np.linspace(1.0, 0.0, len(models))))
print("train test set, r2_score: {}".format(r2_score(np.exp(y_train_sub2), np.exp(y_preds_mean))))
"""
- test_score에 대해서 r2_score가 높은 대로 가중치를 주고 곱하여, y_pred_log를 계산한다. 
"""
y_pred_log = np.array([m.predict(x_test) for m in models]).T.dot(
    np.linspace(1.0, 0.0, len(models))/sum(np.linspace(1.0, 0.0, len(models))))

submit_df = pd.DataFrame({'Id':test_df['Id'], 'SalePrice':np.exp(y_pred_log)})
submit_df.to_csv('kaggle_house_price.csv', index=False)
print('complete')
```

```
---
0 <class 'sklearn.ensemble.forest.RandomForestRegressor'>
sub1: 0.9664234440240744, sub2: 0.8676383468292321
----
1 <class 'sklearn.ensemble.forest.RandomForestRegressor'>
sub1: 0.9767469395035311, sub2: 0.877665811350157
----
2 <class 'sklearn.ensemble.forest.RandomForestRegressor'>
sub1: 0.9778689874477956, sub2: 0.8792262558346684
----
3 <class 'sklearn.ensemble.forest.RandomForestRegressor'>
sub1: 0.9790148671975802, sub2: 0.8837212463937492
----
4 <class 'sklearn.linear_model.coordinate_descent.Lasso'>
sub1: 0.9022879704145137, sub2: 0.8927393030082648
----
5 <class 'sklearn.linear_model.coordinate_descent.ElasticNet'>
sub1: 0.9030091080039795, sub2: 0.8923683751653151
----
6 <class 'sklearn.kernel_ridge.KernelRidge'>
sub1: 0.9064163209137375, sub2: 0.8907039596035089
----
7 <class 'sklearn.kernel_ridge.KernelRidge'>
sub1: 0.930980146661506, sub2: 0.8910237154921481
----
8 <class 'sklearn.kernel_ridge.KernelRidge'>
sub1: 0.956256972993653, sub2: 0.8885662109990935
----
9 <class 'sklearn.kernel_ridge.KernelRidge'>
sub1: 0.9782451794248522, sub2: 0.8828419575402567
----
10 <class 'sklearn.kernel_ridge.KernelRidge'>
sub1: 0.99220242197982, sub2: 0.8699034150517814
----
11 <class 'sklearn.kernel_ridge.KernelRidge'>
sub1: 0.9979475593000363, sub2: 0.8529208943796519
----
12 <class 'sklearn.kernel_ridge.KernelRidge'>
sub1: 0.9995224208532009, sub2: 0.8397923462735553
----
13 <class 'sklearn.kernel_ridge.KernelRidge'>
sub1: 0.9998492796565807, sub2: 0.8332872300652225
----
14 <class 'sklearn.ensemble.gradient_boosting.GradientBoostingRegressor'>
sub1: 0.9764583223628012, sub2: 0.8885541742691342
----
15 <class 'sklearn.ensemble.gradient_boosting.GradientBoostingRegressor'>
sub1: 0.9829038967452599, sub2: 0.886243265137971
----
16 <class 'xgboost.sklearn.XGBRegressor'>
sub1: 0.9474169814699833, sub2: 0.8938965875690038
----
17 <class 'xgboost.sklearn.XGBRegressor'>
sub1: 0.9563279933012628, sub2: 0.8939831001157001
----
18 <class 'xgboost.sklearn.XGBRegressor'>
sub1: 0.9554470474404434, sub2: 0.8965731673598691
----
train test set, r2_score: 0.9069505262382791
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
- 그냥 새로운 model을 여러 개 더 추가하는 게 더 좋은 방법일 것 같습니다. 

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

## wrap-up

- 결국, `GridSearchCV`를 이용해서, 개별 모델에 대해서 가장 잘 예측하는 hyper-parameter 들을 찾고, 
- 그러한 모델을 여러 개 만들어서, 합해서 예측하는 것이 제일 좋습니다. 
- 단, 어떻게 합치는 것이 제일 좋은지에 대해서는 고민이 필요한 것 같아요. 
    - 그냥 `mean`을 구할지, `weighted_mean`을 구하는 지 등. 

- 아무튼, 그 결과로 kaggle의 house price prediction의 결과를 이전보다 꽤 올렸지만, 아직 많이 부족하네요. 절반 겨우 안 쪽에 들어온 수준입니다. 
    - 

## refernce

- <https://www.kaggle.com/c/house-prices-advanced-regression-techniques>
- <https://www.kaggle.com/pmarcelino/comprehensive-data-exploration-with-python>
- <https://www.kaggle.com/dansbecker/your-first-scikit-learn-model>
- <https://www.kaggle.com/serigne/stacked-regressions-top-4-on-leaderboard>

## 최종 code

```python
"""
import lib and data exploration
"""
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

"""
train_df, test_df 모두에 같은 칼럼 set를 가진 칼럼 선정 
"""

both_non_numeric_cols = []
for col in nonNumericCols:
    try:
        if set(train_df[col])==set(test_df[col]):
            both_non_numeric_cols.append(col)
    except:
        continue
print(both_non_numeric_cols)

"""
preprocessing and modeling 
"""
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
        'TotalSF': input_df['TotalBsmtSF'].fillna(input_df['TotalBsmtSF'].mean()) + input_df['1stFlrSF'].fillna(input_df['1stFlrSF'].mean()) + input_df['2ndFlrSF'].fillna(input_df['2ndFlrSF'].mean()),

        #'MasVnrArea':input_df['MasVnrArea'].fillna(input_df['MasVnrArea'].mean()),
        #'Fireplaces':input_df['Fireplaces'].fillna(input_df['Fireplaces'].mean()),
        #'TotRmsAbvGrd':input_df['TotRmsAbvGrd'].fillna(input_df['TotRmsAbvGrd'].mean()),   
    })
    """
    아래 변수들을 추가했는데(이 변수들은 SalePrice와의 corr이 0.3 정도)
    오히려, r2_score가 떨어져서 제외함.
    """
    
    for col in both_non_numeric_cols:
        r = r.join(pd.get_dummies(input_df[col].fillna('None'), prefix=col))
    r['HasBsmt'] = r['TotalBsmtSF'] > 0# TotalBsmtSF가 0인 경우는 basement가 없는 경우이므로, feature를 새로 만들어준다. 
    r['TotalSF'] = np.log1p(r['TotalSF']) # skewness를 조절
    r['TotalBsmtSF'] = np.log1p(r['TotalBsmtSF']) # skewness를 조절
    """
    최종 결정된 column들의 missing value, skewness 등을 체크한다. 
    """
    def print_missing_count_and_skewness():
        temp_r =pd.DataFrame({'missing_v':[r[col].isnull().sum() for col in r.columns], 
                             'skewness':[skew(r[col]) for col in r.columns], 
                             'uniq_count':[len(set(r[col])) for col in r.columns]
                            }, index=r.columns)
        return temp_r[temp_r['uniq_count']>5]
    #print(print_missing_count_and_skewness())
    
    r = pd.DataFrame(MinMaxScaler().fit_transform(r), columns = r.columns)
    r = pd.DataFrame(RobustScaler().fit_transform(r), columns = r.columns)
    return scaler.fit_transform(r)

x_train = preprocessingX(train_df)
x_test = preprocessingX(test_df)

y_true = train_df['SalePrice']
y_true_log = np.log(train_df['SalePrice'])
"""

"""
models = [RandomForestRegressor(n_estimators=n, random_state=42) for n in [10, 30, 50, 100]]
models+=[Lasso(alpha =0.0005, random_state=1)]
models+=[ElasticNet(alpha=0.0005, l1_ratio=.9, random_state=3)]
"""
KernelRidge를 gridsearch로 돌려본 결과, degree가 3일 때 더 좋았음. 
"""
models+=[KernelRidge(alpha=0.6, kernel='polynomial', degree=i, coef0=2.5) for i in range(2, 10)]

models+=[GradientBoostingRegressor(n_estimators=n_e, learning_rate=0.05,
                                   max_depth=4, max_features='sqrt',
                                   min_samples_leaf=15, min_samples_split=10, 
                                   loss='huber', random_state =5) for n_e in [3000, 5000]]
models+=[xgb.XGBRegressor(colsample_bytree=0.4603, gamma=0.0468, 
                             learning_rate=0.05, max_depth=3, 
                             min_child_weight=1.7817, n_estimators=2200,
                             reg_alpha=0.4640, reg_lambda=0.8571,
                             subsample=0.5213, silent=1,
                             random_state =7, nthread = -1)]
models+=[xgb.XGBRegressor(colsample_bytree=0.4603, gamma=0.0468, 
                             learning_rate=0.05, max_depth=5, 
                             min_child_weight=1.7817, n_estimators=5000,
                             reg_alpha=0.4640, reg_lambda=0.8571,
                             subsample=0.5213, silent=1,
                             random_state =7, nthread = -1)]
models+=[xgb.XGBRegressor(colsample_bytree=0.4603, gamma=0.0468, 
                             learning_rate=0.05, max_depth=10, 
                             min_child_weight=1.7817, n_estimators=2200,
                             reg_alpha=0.4640, reg_lambda=0.8571,
                             subsample=0.5213, silent=1,
                             random_state =7, nthread = -1)]


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
#y_preds_mean = y_preds.mean(axis=1)
y_preds_mean = y_preds.dot(np.linspace(1.0, 0.0, len(models))/sum(np.linspace(1.0, 0.0, len(models))))
print("train test set, r2_score: {}".format(r2_score(np.exp(y_train_sub2), np.exp(y_preds_mean))))
"""
- test_score에 대해서 r2_score가 높은 대로 가중치를 주고 곱하여, y_pred_log를 계산한다. 
"""
y_pred_log = np.array([m.predict(x_test) for m in models]).T.dot(
    np.linspace(1.0, 0.0, len(models))/sum(np.linspace(1.0, 0.0, len(models))))

submit_df = pd.DataFrame({'Id':test_df['Id'], 'SalePrice':np.exp(y_pred_log)})
submit_df.to_csv('kaggle_house_price.csv', index=False)
print('complete')
```
