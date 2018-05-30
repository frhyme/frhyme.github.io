---
title: kaggle) mnist 이미지 인식하기 
category: machine-learning
tags: kaggle python machine-learning mnist neural-network CNN
---

## mnist 이미지 분류기 만들기

- mnist는 이제 너무너무도 유명한 데이터이긴 하지만 아무튼. mnist는 사람이 손으로 0-9까지 쓴 hand-written number digit 데이터입니다. 공개로 풀려 있기 때문에, 많은 머신러닝 초보자들이 이 데이터를 이용합니다. kaggle에도 이 데이터를 이용한 컴페티션이 있구요. 
- 저도 예전에 했었는데, 다시 해보려고 합니당 하하핫

## 기본 neural network 만 사용하기

- 물론, image 를 분류할 때는 CNN을 사용하는 것이 좋다는 것을 알고 있지만, 일단 그냥 기본 뉴럴넷으로는 어느 정도의 정확도를 얻을 수 있는지 한번 확인해보도록 합니다. 또, sklearn에 꽤 유용한 함수들이 많이 있어요. 
- optimizer는 Adam, activation function은 ReLU 로 고정하고, 레이어들 갯수와 레이어별 노드 갯수만 조절하면서, 어느 정도의 차이가 발생하는지를 파악해볼게요. 

```python
from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import accuracy_score

def print_accuracy(clf):
    X = train_df[train_df.columns[1:]]
    Y = train_df['label']
    
    x_train, x_test, y_train, y_test = train_test_split(X, Y, test_size = 0.3, random_state=42)
    train_sample_size = len(x_train)
    x_train = x_train[x_train.columns][:train_sample_size]
    y_train = y_train[:train_sample_size]
    clf.fit(x_train, y_train)

    print("train accuracy: {:.2%}, test accuracy: {:.2%}".format(
        accuracy_score(y_train, clf.predict(x_train)),
        accuracy_score(y_test, clf.predict(x_test))
    ))
hidden_layer_size_lst = [
    [10, 10], 
    [10, 20, 10],
    [10, 80, 240, 80, 10],
    [10, 20, 40, 80, 40, 20, 10],
    [10, 20, 40, 80, 160, 80, 40, 20, 10],
    [10, 80, 240, 960, 240, 80, 10],
    [10, 80, 240, 480, 960, 480, 240, 80, 10],
]
for h_l_s in hidden_layer_size_lst:
    print("hidden_layer_size: {}".format(h_l_s))
    print_accuracy( MLPClassifier(hidden_layer_sizes=h_l_s, activation='relu', solver='adam') )
    print("-----------------")
```

- 그냥, 10개짜리로 두 층만 쌓아도, 정확도는 90% 이상 나옵니다. 
- 더 복잡하게 쌓을 수록 올라가기는 하는데 train size는 빠르게 올라가는 반면, (당연히) test size는 올라가는 속도가 더디네요. 
- 무조건 레이어를 많이, 노드 갯수도 많이 한다고, 무조건 accuracy가 올라간다고 볼 수는 없습니다. 

```
hidden_layer_size: [10, 10]
train accuracy: 91.27%, test accuracy: 88.73%
-----------------
hidden_layer_size: [10, 20, 10]
train accuracy: 94.61%, test accuracy: 91.24%
-----------------
hidden_layer_size: [10, 80, 240, 80, 10]
train accuracy: 96.34%, test accuracy: 92.65%
-----------------
hidden_layer_size: [10, 20, 40, 80, 40, 20, 10]
train accuracy: 96.73%, test accuracy: 92.60%
-----------------
hidden_layer_size: [10, 20, 40, 80, 160, 80, 40, 20, 10]
train accuracy: 96.98%, test accuracy: 93.29%
-----------------
hidden_layer_size: [10, 80, 240, 960, 240, 80, 10]
train accuracy: 96.83%, test accuracy: 92.52%
-----------------
hidden_layer_size: [10, 80, 240, 480, 960, 480, 240, 80, 10]
train accuracy: 93.98%, test accuracy: 90.95%
-----------------
```

## CNN을 사용합시다. 

- CNN을 사용하지 않고는 답이 없는 것 같아요. 그냥 nn에서는 대략 train/test 각각 97/93 정도의 상한선이 있는 것 같아요. 




## reference

- <https://www.kaggle.com/yassineghouzam/introduction-to-cnn-keras-0-997-top-6>