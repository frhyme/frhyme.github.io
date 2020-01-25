---
title: kaggle) titanic 생존자 예측하기
category: machine-learning
tags: kaggle sklearn pandas numpy 
---

## titanic의 생존자들에게는 어떠한 특성이 있을까.

- kaggle에서 titanic 데이터를 활용해서 어떤 사람들이 살아남았는지 예측하는 데이터를 제공합니다. 약간...무서운 데이터기는 하지만 그래도, 해보도록 합니다.
- 살아남았는지, 살아남지 않았는지를 예측하는 binary classification 문제입니다. 따라서, accuracy뿐만 아니라, 다양한 metric들을 함께 사용해서 classifier의 성능을 판단해볼 수 있지 않을까? 싶어요. 


## data exploration 

- mnist 같은 데이터의 경우는, 데이터를 전처리하는 것이 상대적으로 쉬운 편입니다. 전부다 픽셀데이터고, 0-256 사이의 값으로만 존재하니까요. 물론 이러한 이미지 데이터도 복잡해지면, 해당 이미지를 특정 feature로 정리하는 것이 필요할 수 있습니다(뉴럴넷이 대신 해주긴 하지만, 코가 있는지 여부, 등등).

- 그러나, titanic 데이터는 상대적으로 깔끔하게 정리되어 있지 않아요. missing data도 많고, 개별 데이터의 의미도 불분명하게 느껴지는 것들이 있습니다. 일단 개별 칼럼과 칼럼의 의미들은 다음과 같아요. 

### data columns 

- **PassengerId**: 승객 번호, 연속된 숫자들이라서, 특별한 정보는 담고 있지 않은 것 같아요. 
- **Survived**: 승객이 살아남았는지 여부, 0 or 1 , Y 데이터
- **Pclass**: ticket class, 1,2,3으로 구분되는 categorical data
- **Name**: 이름 문자열 ==> mr, mrs 등의 정보를 뽑아낼 수 있음 
- **Sex**: 성별, categorical data 
- **Age**: 나이, numerical data 
- **SibSp**: 배우자 수 + 형제자매 수, discrete numerical data
- **Parch**: 부모님 수 + 자식 수, discrete numerical data
- **Ticket**: Ticket 이름 
- **Fare**: 요금 가격, numerical data 
- **Cabin**: 객실 번호, 문자열 데이터(값이 없는 경우 객실이 없는 사람)
- **Embarked**: 탑승 항구, categorical data 

- 사실 이미 주어진 categorical data들인 `Pclass`, `Sex`, `Cabin`, `Embarked` 만으로도 사실 train_data에 대해서 80% 가깝게 예측을 합니다. 이미 주어진 것들로도 80% 정도는 예측하는데, 훨씬 잘 예측하려면, 제가 이 데이터로부터 새로운 정보를 뽑아서 칼럼을 생성해줘야 합니다. 

### feature engineering 

- 아마도 titanic competition을 통해서 배울 수 있는 것은 혹은 가장 중요한 것은 data exploration, feature engineering이라고 생각합니다. 

- 예를 들어서, 
    - parch, SibSp가 모두 0인 경우 `isAlone`라는 새로운 칼럼을 만든다(실제로 True인 경우 survival rate가 매우 낮아짐
    - Age를 적절하게 카테고리컬 데이터로 변형함. 
    - Name로부터 mr, mrs 등을 뽑아내고, 이것이 survival rate에 영향을 줌을 발견하고, 칼럼으로 만듬. 
- 등이 있습니다. 매우 귀찮습니다.... 
- 그래서 저는 하지 않았습니다 하하하하하 


## 간단하게 합시다. 

- 제가 편하고! 기계가 불편하도록! 노력합니다. 

- **대충 카테고리컬 데이터로 만들고, 원핫벡터화**: 중요하면, 그 칼럼이 무시되지 않을까요?ㅎㅎㅎㅎㅎㅎ
- **GridsearchCV와 다양한 clf를 매우 많이 사용**: 알아서 잘 찾아주지 않을까요? 


```python
import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt

from sklearn.preprocessing import MinMaxScaler

from sklearn.model_selection import train_test_split
from sklearn.model_selection import GridSearchCV

from sklearn.linear_model import LogisticRegression, LogisticRegressionCV
from sklearn.tree import DecisionTreeClassifier
from sklearn.neural_network import MLPClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.ensemble import RandomForestClassifier, AdaBoostClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.discriminant_analysis import QuadraticDiscriminantAnalysis
from sklearn.gaussian_process import GaussianProcessClassifier

from sklearn.metrics import accuracy_score, f1_score, roc_auc_score
"""
- cabin값이 있고, 없을때의 survival rate가 0.4 정도 차이남.
- 각각, sibling+spouse의 수, parent+child 의 수인데, 개별 class별로 차이가 발생함. 
- Age를 continuous하게 하지 않고, categorical로 처리했더니 정확도가 오르는 것을 알 수 있음. 
"""
def preprocessingX(inputDF):
    def find_preName(inputS):
        inputS = inputS.lower()
        if '.' in inputS:
            r = inputS[inputS.find(",")+2:inputS.find(".")]
            if r in ['mrs', 'miss', 'mr', 'master']:
                return  r
            else:
                return 'none'
        else:
            return "none"
    r = pd.get_dummies(inputDF['Pclass'], prefix='Pclass').join(
        pd.get_dummies(inputDF['Sex'], prefix='Sex')).join(
        pd.get_dummies(inputDF['Cabin'].isnull(), prefix='Cab')).join(
        pd.get_dummies((inputDF['SibSp'] + inputDF['Parch']), prefix='fam')).join(
        inputDF['Age'].fillna(inputDF['Age'].mean())//16).join(
        inputDF['Fare'].fillna(inputDF['Fare'].mean())).join(
        pd.get_dummies(inputDF['Name'].apply(find_preName))).join(
        pd.get_dummies(inputDF['Embarked'], prefix='Em'))
    r = pd.DataFrame(MinMaxScaler().fit_transform(r), columns=r.columns)
    return r

X = preprocessingX(df)
Y = df['Survived']

#train_X, test_X, train_Y, test_Y = train_test_split(X, Y, train_size=0.8, random_state=42)

models = {
    "logisticReg":GridSearchCV(LogisticRegression(), {'penalty':['l1', 'l2'], }),
    #"DecTreeClf":DecisionTreeClassifier(),
    "neural-net":GridSearchCV(MLPClassifier(), {'hidden_layer_sizes':[[10, 50, 10],
                                                                      [16, 32, 64, 32, 16, 8, 4], 
                                                                      [10, 20, 40, 80, 160, 80, 40, 20, 10],
                                                                      [16, 128, 16]
                                                                     ], 
                                                'activation':['relu', 'logistic'], 
                                                'solver':['adam']
                                               }, cv=2),
    'kneighborsClf':GridSearchCV(KNeighborsClassifier(), {'n_neighbors':[2, 3, 5, 10]}),
    'svc':GridSearchCV(SVC(), {'kernel':['rbf', 'poly', 'linear', 'sigmoid'], 'C':[1, 10]}),
    'randomforest':GridSearchCV(RandomForestClassifier(), {'n_estimators':[2, 3, 5, 10, 50, 75, 100]}),
    'AdaBoostClassifier':GridSearchCV(AdaBoostClassifier(), {'n_estimators':[2, 3, 5, 10]}),
    'GaussianNB':GaussianNB(), 
    'QuadraticDiscriminantAnalysis': QuadraticDiscriminantAnalysis(), 
    'GaussianProcessClassifier':GaussianProcessClassifier()
}

print('-------------------')
for k, m in models.items():
    m.fit(train_X, train_Y)
    print(k)
    y_true = Y
    y_pred = m.predict(X)
    print("train accuracy: {}".format( accuracy_score(y_true, y_pred) ))
    print("F1 score: {}".format( f1_score(y_true, y_pred)))
    print("--------")

test_df['Survived'] = models['neural-net'].predict(preprocessingX(test_df))
test_df[['PassengerId', 'Survived']].to_csv('titanic_submit.csv', index=False)
```

- 결과는, randomforest의 경우가 90% 정도로 나오기는 했는데, 제출해보면, 0.8이 채 못 나옵니다. 

```
-------------------
logisticReg
train accuracy: 0.8338945005611672
F1 score: 0.7784431137724551
--------
neural-net
train accuracy: 0.8451178451178452
F1 score: 0.779552715654952
--------
kneighborsClf
train accuracy: 0.8451178451178452
F1 score: 0.7759740259740259
--------
svc
train accuracy: 0.8305274971941639
F1 score: 0.7666151468315301
--------
randomforest
train accuracy: 0.9270482603815937
F1 score: 0.9042709867452136
--------
AdaBoostClassifier
train accuracy: 0.8226711560044894
F1 score: 0.7620481927710844
--------
GaussianNB
train accuracy: 0.4276094276094276
F1 score: 0.5721476510067114
--------
QuadraticDiscriminantAnalysis
train accuracy: 0.7586980920314254
F1 score: 0.7309136420525657
--------
GaussianProcessClassifier
train accuracy: 0.8451178451178452
F1 score: 0.7759740259740259
--------
```


## wrap-up 

- 이 컴페티션의 리더보드를 보면, 1.0에 위치해있는 사람들이 매우 많은 것을 알 수 있는데....어떻게 이럴 수있을까요.. 저는 0.8을 못 넘기겠습니다...
- 음, 사실, 0.8을 못 넘기는 이유는 다양한 것이 있을 것 같습니다(결국 결론을 '귀찮기 때문'이긴 한데). 아까 말한대로 feature engineering을 제대로 하지 않은 것과 데이터 자체가 너무 적은 것, 이 원인이 되지 않을까 싶어요. 
    - 저도 좀 높여보려고, 다른 사람들이 한 것들을 찾아봤는데, kaggle의 notebook 중에 0.9가 넘는 경우는 아직 찾지못했어요. 왜인지 모르겠는데,
- 아무튼 타이타닉은 점수를 높이는 과정에서, 머신러닝에 관한 일반적인 지식을 얻게 되는 것 같지 않아요. 앞으로 안할겁니다(정신승리 하하핫)

## reference

- <https://www.kaggle.com/startupsci/titanic-data-science-solutions>