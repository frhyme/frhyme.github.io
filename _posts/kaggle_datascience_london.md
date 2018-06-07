---
title: kaggle) simple binary classification 
category: machin-learning
tags: python python-lib sklearn classification 
---

## 간단한, classification을 풉니다. 

- kaggle에 있는 초보자를 위한 컴페티션 중에 [이 아이](https://www.kaggle.com/c/data-science-london-scikit-learn)를 골랐습니다. 물론, 이미 끝난 컴페티션이어서, 큰 의미는 없지만, 얼마나 할 수 있는지 보려고 합니다. 
- 아쉽게도, 그래서 kernel이 없습니다. 혼자 계속 부딪히면서 해봐야 하는 것 같아요. 
- data에 missing value가 없어서, 그냥 바로 적용할 수 있어서 편하기는 합니다. 

## just do it 

- 비교적 간단한, binary classification 문제고
- 모든 feature는 numeric 이고 
- missing value가 없으니까, 

- 당연히 매우 쉽게 풀 수 있을 줄 알았습니다. 사실 저런 상태면, 그냥 모델을 많이 만든 다음에, cross_validation이 제일 높은 놈을 골라서 넣어주면 끝난다고, 그렇게 생각했씁니다만, 그렇게 그냥 하고 제출하니, 0.84 정도의 score만 나왔습니다. 모델이랑 모델은 다 만들어보고, hyper-parameter도 막 바꾸면서 해봤는데, 안됩니다. 왜 안되는 걸까요. 여기서부터가 사실 뛰어난 데이터사이언티스트와 그렇지 않은 사람을 가르는 것이 아닐까 싶기는 합니다만...

## code 

- 일단 작성한 코드를 올립니다. 경우에 따라서는 scaling하지 않는 것이 score를 올리는 데 더 좋은 것 같기도 한데, 일단은 그냥 했습니다. 

### using random forest

- random forest와 knn을 이용하였습니다. 시간은 꽤 오래 걸렸구요... 정확도는 아쉽게도, 별로 높게 나오지는 않습니다. 
- 처음에는 PCA도 적용해서 해봤는데, 굳이 할 필요는 없을 것 같아요. 다른 블로그에 보니까 PCA를 사용하는 경우들이 있더라고요. 
- PCA를 쓰고 random-forest를 사용할 바에는 그냥, PCA를 쓰지 않고 뉴럴넷만으로 분류하는 것이 더 좋을 것 같네요. 
- kaggle에 제출해보니, 대략 0.83 정도의 score가 나왔습니다. 

```python
import pandas as pd
import numpy as np 

x_train = pd.read_csv(x_train_url, header=None)
y_train = pd.read_csv(y_train_url, header=None)
x_test = pd.read_csv(x_test_url, header=None)

from sklearn.preprocessing import MinMaxScaler, RobustScaler
from sklearn.decomposition import PCA

from sklearn.model_selection import GridSearchCV
from sklearn.ensemble import RandomForestClassifier

from sklearn.neighbors import KNeighborsClassifier
from sklearn.cross_validation import cross_val_score

def preprocessingX(input_df):
    r = RobustScaler().fit_transform(input_df)
    r = MinMaxScaler().fit_transform(r)
    #r = PCA(n_components=3).fit_transform(r)
    return r

x_train_v = preprocessingX(x_train)

rf_grid = GridSearchCV(RandomForestClassifier(), {'n_estimators':[100], 
                                            'max_depth':[5, 10, 13], 
                                            'min_samples_split': [2, 5, 10], 
                                            'random_state':[42],
                                           }, cv=10, scoring='accuracy')
rf_grid.fit(x_train_v, y_train.values.ravel())

#knn_grid = GridSearchCV(KNeighborsClassifier(), {'n_neighbors':[30, 50]}, cv=10, scoring='accuracy')
#knn_grid.fit(x_train_v, y_train.values.ravel())

rf_best = rf_grid.best_estimator_
#knn_best = knn_grid.best_estimator_

print('----')
for m in [rf_best]:
    # y 가 2차원 어레이일 때 문제가 생겨서, ravel로 수정해줌
    print(m.__class__)
    print("train: {}".format(m.score(x_train_v, y_train.values.ravel())))
    print("----")

print( cross_val_score(rf_best, x_train_v, y_train.values.ravel(),cv=10,scoring='accuracy') )
#print( cross_val_score(knn_best, x_train_v, y_train.values.ravel(),cv=10,scoring='accuracy') )

"""
submit_df 만들기
"""
submit_df = pd.DataFrame({'Id':range(1,1+len(x_test)), 
              'Solution':rf_best.predict(preprocessingX(x_test))
             })
submit_df.to_csv('180607_ds_london.csv', index=False)    
print("complete")
```

```
----
<class 'sklearn.ensemble.forest.RandomForestClassifier'>
train: 1.0
----
[ 0.88  0.86  0.89  0.88  0.83  0.88  0.9   0.88  0.86  0.85]
complete
```

### using MLPclassifier 

- 이 경우는 좀 나아집니다. score가 0.89까지 올릴 수 있습니다. 하지만, 가능하면 0.9는 넘기면 좋겠습니다. 
- 이 competition의 목적이, `sklearn`을 주로 사용하는 것이라서, 가능하면 저도, `sklearn`만으로 score를 올리면 좋겠습니다.
- `hidden_layer_sizes`와 `tol`를 변경시켜가면서, 조절했으나, 0.89가 현재로서는 맥스인것 같습니다. 
- 복잡하게 뉴럴넷을 만들어봤지만, 여전히 0.89정도로 멈춰 있는 것을 알 수 있습니다. 
- 나중에 좀 더 다양하게 돌려보겠씁니다. 

```python
"""
- MLPclasffieir로 한번 해보면 좋을 것 같다. 
- 
"""

import pandas as pd
import numpy as np 
from sklearn.neural_network import MLPClassifier
from sklearn.model_selection import cross_val_score, train_test_split

x_train = pd.read_csv(x_train_url, header=None)
y_train = pd.read_csv(y_train_url, header=None)
x_test = pd.read_csv(x_test_url, header=None)

x_train_v = x_train.values

x_train_train, x_train_test, y_train_train, y_train_test = train_test_split(x_train_v, y_train, 
                                                                            train_size=0.6, 
                                                                            test_size=0.4, 
                                                                            random_state=42
                                                                           )

models = [
    MLPClassifier(hidden_layer_sizes=[64, 32, 4], max_iter=5000, random_state=42), 
    MLPClassifier(hidden_layer_sizes=[2048, 512, 128], max_iter=5000, random_state=42), 
    MLPClassifier(hidden_layer_sizes=[8192, 2048, 128], max_iter=5000, random_state=42), 
    MLPClassifier(hidden_layer_sizes=[4092, 512, 64], max_iter=5000, random_state=42, verbose=False), 
    MLPClassifier(hidden_layer_sizes=[2048, 512, 128, 32, 16], max_iter=5000, random_state=42, verbose=False, tol=0.000001), 
    MLPClassifier(hidden_layer_sizes=[8192, 4096, 2048, 512, 128, 32, 16], max_iter=5000, random_state=42, verbose=True, tol=0.000001), 
    #MLPClassifier(hidden_layer_sizes=[4092*2, 512*2, 64*2], max_iter=5000, random_state=42, verbose=True), 
    #MLPClassifier(hidden_layer_sizes=[64, 32, 4], max_iter=5000, alpha=0.05), 
    #MLPClassifier(hidden_layer_sizes=[64, 32, 4], max_iter=5000, alpha=0.5), 
    #MLPClassifier(hidden_layer_sizes=[2048, 128, 4], max_iter=5000, alpha=0.05),
]

for m in models:
    # y 가 2차원 어레이일 때 문제가 생겨서, ravel로 수정해줌
    print(m.__class__)
    m.fit(x_train_train, y_train_train.values.ravel())
    print("train: {}".format(m.score(x_train_train, y_train_train.values.ravel())))
    print("test: {}".format(m.score(x_train_test, y_train_test.values.ravel())))
    #print(cross_val_score(m, x_train_train, y_train_train.values.ravel(),cv=10,scoring='accuracy'))
    print("----")

best_model = sorted(models, key=lambda m: m.score(x_train_test, y_train_test.values.ravel()), reverse=True)[0]

submit_df = pd.DataFrame({'Id':range(1,1+len(x_test)), 
              'Solution':best_model.predict(x_test.values)
             })
submit_df.to_csv('180607_ds_london.csv', index=False)    
print("complete")
```

- 복잡하게 뉴럴넷을 만들어봤지만, 여전히 0.89정도로 멈춰 있는 것을 알 수 있습니다. 

```
<class 'sklearn.neural_network.multilayer_perceptron.MLPClassifier'>
train: 0.9983333333333333
test: 0.87
----
<class 'sklearn.neural_network.multilayer_perceptron.MLPClassifier'>
train: 1.0
test: 0.8925
----
<class 'sklearn.neural_network.multilayer_perceptron.MLPClassifier'>
train: 1.0
test: 0.885
----
<class 'sklearn.neural_network.multilayer_perceptron.MLPClassifier'>
train: 1.0
test: 0.885
----
<class 'sklearn.neural_network.multilayer_perceptron.MLPClassifier'>
train: 1.0
test: 0.89
----
<class 'sklearn.neural_network.multilayer_perceptron.MLPClassifier'>
Iteration 1, loss = 0.63504406
Iteration 2, loss = 1.02627232
Iteration 3, loss = 0.58636568
Iteration 4, loss = 0.39818701
Iteration 5, loss = 0.36976756
Iteration 6, loss = 0.29988947
Iteration 7, loss = 0.25247464
Iteration 8, loss = 0.21701859
Iteration 9, loss = 0.16716805
Iteration 10, loss = 0.12269334
Iteration 11, loss = 0.08120724
Iteration 12, loss = 0.05184766
Iteration 13, loss = 0.03686217
Iteration 14, loss = 0.02119144
Iteration 15, loss = 0.01396260
Iteration 16, loss = 0.02903801
Iteration 17, loss = 0.04954998
Iteration 18, loss = 0.06622163
Training loss did not improve more than tol=0.000001 for two consecutive epochs. Stopping.
train: 0.9983333333333333
test: 0.8625
----
complete
```

### using keras

- overfitting 문제를 해결하기 위해서, dropout을 사용해야 할 것 같습니다. 이를 위해서는 keras를 이용해야 할 것 같네요. 

## wrap-up

- `sklearn`에 워낙 괜찮은 classifier들이 많아서, 그냥 그대로 사용하면 될 거라고 생각했는데, 

## reference 

- <https://www.kaggle.com/c/data-science-london-scikit-learn/data>
- <https://github.com/siddharthagarwal/Kaggle-Data-Science-London-Scikit-Learn/blob/master/london.py>