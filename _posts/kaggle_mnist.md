---
title: kaggle) mnist 이미지 인식하기 
category: machine-learning
tags: kaggle python machine-learning mnist neural-network CNN keras sklearn 
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

## keras를 이용합시다

- 93%도 충분히 높은 값이기는 하지만, `sklearn`만으로는 이미지 분류에는 한계가 있는 것 같아요. 그래서 저는 `keras`로 넘어가려고 합니다. 
- 일단은 기본적인 `neural network`를 사용해보고, 이후에 `CNN`을 만들어보려고 해요. 

### nn with keras 

- sklearn과 동일하지만, 일단 잘 되는지 확인하려고 한번 돌려봅니다. 
- kaggle에서 데이터를 가져왔을때, mnist데이터는 normalization이 되어 있지 않습니다. pixel의 값들이 0-256 에 분포되어 있는데, 이 경우 학습이 잘 되지 않고, 높지 않은 cost에서 계속 정체되어 있는 것을 알 수 있습니다. 
- `tensorflow.examples.tutorials.mnist.input_data.read_data_sets("MNIST_data/", one_hot=True).train.images`에 있는 데이터들은 0과 1.0 사이에 일정하게 분포해 있는 것을 알 수 있습니다. kaggle과는 차이가 있으며, 이 차이 때문에, 학습에 문제가 발생할 수 있습니다. 학습을 잘 시키려면 이 값들을 0과 1.0 사이로 normalization해주는 것이 좋습니다. 
    - 만약, 원래 데이터를 바꾸고 싶지 않을 경우에는 `learning-rate`를 상대적으로 더 낮추면 나아지는데, 그냥 원래 데이터를 0-1.0 으로 변경하는 것이 훨씬 효율적입니다. 
- optimizer를 `SGD`에서 `Adam`으로 변경하였더니, 10 epoch만에 SGD에서 30 epoch을 돌린 결과와 비슷하게 나옵니다. 앞으로는 `Adam`만 쓰도록 하겠습니다. 

```python
"""
- keras에서는 Y를 one_hot vector로 바꾸어 사용해야 함
- X의 값들이 0과 256 사이에 분포해있으므로, 이를 0과 1.0 사이로 움직임 
- train, test set으로 구분하여 진행
"""
X = train_df[train_df.columns[1:]]
Y = pd.get_dummies(train_df['label'])
x_train, x_test, y_train, y_test = train_test_split(X.values.astype(np.float64)/256.0, 
                                                    Y.values.astype(np.float32), 
                                                    test_size = 0.2, random_state=42)

from keras.models import Sequential
from keras.layers import Dense, Activation
from keras.optimizers import Adam, SGD
from keras import metrics
"""
- 원래 데이터가 784이므로, 비슷한 1024로 두고 이를 감소시키는 뉴럴넷 설계
- 총 10개로 클래스를 구분하므로, 마지막 Dense는 10개의 노드를 가지고 있어야함
- 그리고, 마지막은 softmax
"""
model = Sequential([
    Dense(1024, input_shape=(784,)),
    Activation('relu'),
    Dense(512),
    Activation('relu'),
    Dense(256),
    Activation('relu'),
    Dense(128),
    Activation('relu'),
    Dense(32),
    Activation('relu'),
    Dense(10),
    Activation('softmax'),
])
"""
- multi classification이므로 loss는 'categorical_crossentropy'
- metric에는 내가 추적할 지표들이 들어감. 최적화는 loss에 따라 되는데, epoch 마다 평가될 지표들이 metric에 들어감. 
"""
model.compile(loss='categorical_crossentropy', 
              #optimizer=SGD(lr=0.01, decay=1e-6, momentum=0.9, nesterov=True), 
              optimizer=Adam(lr=0.001, beta_1=0.9, beta_2=0.999, epsilon=1e-8),
              metrics=[metrics.categorical_accuracy])
"""
- one epoch = one forward pass and one backward pass of all the training examples
- batch size = the number of training examples in one forward/backward pass. 

- 즉, epoch을 증가한다는 것은 전체 데이터 셋을 몇 번 돌릴 것이냐 를 결정하는 것이고, 
- batch_size는 backpropagation을 몇 개의 size로 돌릴 것이냐? 를 결정하는 이야기다.
"""
train_history = model.fit(x_train, y_train, epochs=20, batch_size=500, verbose=2)
train_history = train_history.history # epoch마다 변화한 loss, metric

# 아래 세 줄은 필요없는 코드인데, 그래도 이후에 사용될 수 있어서 일단 넣어둠. 
y_predict = model.predict_classes(x_train, verbose=0)
y_true = [ np.argmax(y) for y in y_train]
accuracy = np.sum([y_comp[0]==y_comp[1] for y_comp in zip(y_predict, y_true)])

loss_and_metric = model.evaluate(x_train, y_train, batch_size=128, verbose=0)
print("train, loss and metric: {}".format(loss_and_metric))
loss_and_metric = model.evaluate(x_test, y_test, batch_size=128, verbose=0)
print("test, loss and metric: {}".format(loss_and_metric))
```

- 시간은 조금 걸렸지만, 맨 아래에 있는 결과를 보면 train set에는 99.6%, test set에는 97% 정도의 accuracy를 가지는 것을 알 수 있습니다. 
- `Adam`이 최고입니다 최고에요!! 학습 시간 자체를 확실히 줄여주네요. 

```
Epoch 1/20
12s - loss: 0.5048 - categorical_accuracy: 0.8413
Epoch 2/20
10s - loss: 0.1401 - categorical_accuracy: 0.9580
Epoch 3/20
9s - loss: 0.0832 - categorical_accuracy: 0.9748
Epoch 4/20
9s - loss: 0.0586 - categorical_accuracy: 0.9816
Epoch 5/20
9s - loss: 0.0446 - categorical_accuracy: 0.9864
Epoch 6/20
9s - loss: 0.0327 - categorical_accuracy: 0.9898
Epoch 7/20
11s - loss: 0.0212 - categorical_accuracy: 0.9933
Epoch 8/20
11s - loss: 0.0141 - categorical_accuracy: 0.9956
Epoch 9/20
12s - loss: 0.0121 - categorical_accuracy: 0.9963
Epoch 10/20
11s - loss: 0.0167 - categorical_accuracy: 0.9943
Epoch 11/20
11s - loss: 0.0139 - categorical_accuracy: 0.9957
Epoch 12/20
11s - loss: 0.0084 - categorical_accuracy: 0.9976
Epoch 13/20
11s - loss: 0.0078 - categorical_accuracy: 0.9974
Epoch 14/20
10s - loss: 0.0108 - categorical_accuracy: 0.9966
Epoch 15/20
9s - loss: 0.0029 - categorical_accuracy: 0.9992
Epoch 16/20
10s - loss: 0.0082 - categorical_accuracy: 0.9976
Epoch 17/20
11s - loss: 0.0191 - categorical_accuracy: 0.9937
Epoch 18/20
12s - loss: 0.0104 - categorical_accuracy: 0.9963
Epoch 19/20
12s - loss: 0.0136 - categorical_accuracy: 0.9958
Epoch 20/20
11s - loss: 0.0080 - categorical_accuracy: 0.9976
train, loss and metric: [0.011053406523133162, 0.99630952380952376]
test, loss and metric: [0.13161088258205425, 0.97297619024912518]
```

### CNN with keras 

- 일단, train보다 test에서는 조금 정확도가 떨어지는 것을 알 수 있습니다. 우리가 분석하려는 것은 image고 위 아래 양옆으로 비슷하게 위치한 값들을 함께 학습시키면 이러한 약간의 overfitting을 줄일 수 있지 않을까? 라고 생각해봅니다. 
- 중요한 것은,,,,여기서부터는 시간이 아주아주 많이 걸립니다. 켜놓고 다른 것을 하시면서 보는게 더 좋을 수 있어요. 물론 저처럼 맥북에어를 쓰시는 분이 아니고....괜찮은 GPU를 가지고 있다면 문제가 없습니다. ㅠㅠ
- 아무튼, CNN을 돌려봤습니다. 1시간 걸렸네요...ㅠㅠ

- 드롭아웃은 전혀 쓰지 않았고, 대신 Maxpooling하기 전에 Convolution을 같은 세팅으로 두 번씩 돌렸습니다. 이전에는 한 번씩만 돌렸는데, 그보다는 이렇게 두 번 연속으로 하는게 더 잘 워킹하는 것 같아요. 

```python
X = train_df[train_df.columns[1:]]
Y = pd.get_dummies(train_df['label'])

X_values = (X.values.astype(np.float64)/256.0).reshape(len(X_values), 28, 28, 1)
Y_values = Y.values.astype(np.float32)

x_train, x_test, y_train, y_test = train_test_split(X_values, Y_values, 
                                                    test_size = 0.2, random_state=42)

from keras.models import Sequential
from keras.layers import Dense, Dropout, Activation, Conv2D, Flatten, MaxPooling2D
from keras.optimizers import SGD
from keras import metrics
import numpy as np

model = Sequential([
    Conv2D(filters = 32, kernel_size = (5,5),padding = 'Same', activation ='relu', input_shape = (28,28,1)),
    Conv2D(filters = 32, kernel_size = (5,5),padding = 'Same', activation ='relu'),
    MaxPooling2D(pool_size=(2,2)),
    #Dropout(0.25),
    
    Conv2D(filters = 64, kernel_size = (3,3),padding = 'Same', activation ='relu'),
    Conv2D(filters = 64, kernel_size = (3,3),padding = 'Same', activation ='relu'),
    MaxPooling2D(pool_size=(2,2), strides=(2,2)),
    #Dropout(0.25),
    
    Flatten(),
    Dense(256, activation = "relu"),
    #Dropout(0.5),
    Dense(10, activation = "softmax")
])

model.compile(loss='categorical_crossentropy', 
              optimizer=Adam(lr=0.001, beta_1=0.9, beta_2=0.999, epsilon=1e-8), 
              metrics=[metrics.categorical_accuracy])

train_history = model.fit(x_train, y_train, epochs=10, batch_size=500, verbose=1)
train_history = train_history.history

loss_and_metric = model.evaluate(x_train, y_train, batch_size=128, verbose=0)
print("train, loss and metric: {}".format(loss_and_metric))
loss_and_metric = model.evaluate(x_test, y_test, batch_size=128, verbose=0)
print("test, loss and metric: {}".format(loss_and_metric))
```

- 결과는 train set에 99.7%, test set에 98.7% 정도 나옵니다. 꽤 높은 편이네요. 
- 이렇게 만들어진 model을 kaggle에 제출해보니, 0.98671 정도의 정확도(1034등)를 획득했습니다. 그동안 했던 것 들 중에서 가장 높은 값이기는 한데, 승에 차지는 않네요. 

```
Epoch 1/10
33600/33600 [==============================] - 433s - loss: 0.4611 - categorical_accuracy: 0.8610   
Epoch 2/10
33600/33600 [==============================] - 406s - loss: 0.0786 - categorical_accuracy: 0.9765   
Epoch 3/10
33600/33600 [==============================] - 382s - loss: 0.0510 - categorical_accuracy: 0.9841   
Epoch 4/10
33600/33600 [==============================] - 398s - loss: 0.0390 - categorical_accuracy: 0.9882   
Epoch 5/10
33600/33600 [==============================] - 411s - loss: 0.0299 - categorical_accuracy: 0.9905   
Epoch 6/10
33600/33600 [==============================] - 366s - loss: 0.0273 - categorical_accuracy: 0.9913   
Epoch 7/10
33600/33600 [==============================] - 395s - loss: 0.0217 - categorical_accuracy: 0.9931   
Epoch 8/10
33600/33600 [==============================] - 380s - loss: 0.0175 - categorical_accuracy: 0.9944   
Epoch 9/10
33600/33600 [==============================] - 393s - loss: 0.0159 - categorical_accuracy: 0.9949   
Epoch 10/10
33600/33600 [==============================] - 388s - loss: 0.0113 - categorical_accuracy: 0.9967   
train, loss and metric: [0.0098527891978821055, 0.99702380952380953]
test, loss and metric: [0.044221350852222667, 0.98761904784611299]
```

### 레이어를 하나 더 쌓아봅시다. 

- 무엇을 해야 할까요? CNN을 더 복잡하게 만들어서 쌓아볼까요? 128 짜리를 두 개 추가해봤습니다. 
- 단순히, 이렇게만 추가했는데, 0.98742의 score를 획득했습니다. 이전에 비해서 train, test 모두 score가 증가한 것을 알 수 있구요. 따라서, 아직은 overfitting은 아닌 것 같습니다. 굳이 dropout을 추가할 필요는 없을 것 같네요. 

```python
model = Sequential([
    Conv2D(filters = 32, kernel_size = (5,5),padding = 'Same', activation ='relu', input_shape = (28,28,1)),
    Conv2D(filters = 32, kernel_size = (5,5),padding = 'Same', activation ='relu'),
    MaxPooling2D(pool_size=(2,2)),
    #Dropout(0.25),
    
    Conv2D(filters = 64, kernel_size = (3,3),padding = 'Same', activation ='relu'),
    Conv2D(filters = 64, kernel_size = (3,3),padding = 'Same', activation ='relu'),
    MaxPooling2D(pool_size=(2,2), strides=(2,2)),
    #Dropout(0.25),
    
    Conv2D(filters = 128, kernel_size = (2,2),padding = 'Same', activation ='relu'),
    Conv2D(filters = 128, kernel_size = (2,2),padding = 'Same', activation ='relu'),
    MaxPooling2D(pool_size=(2,2), strides=(2,2)),
    
    Flatten(),
    Dense(256, activation = "relu"),
    #Dropout(0.5),
    Dense(10, activation = "softmax")
])
```

```
Epoch 1/10
33600/33600 [==============================] - 504s - loss: 0.5980 - categorical_accuracy: 0.8100   
Epoch 2/10
33600/33600 [==============================] - 481s - loss: 0.0938 - categorical_accuracy: 0.9699   
Epoch 3/10
33600/33600 [==============================] - 462s - loss: 0.0650 - categorical_accuracy: 0.9795   
Epoch 4/10
33600/33600 [==============================] - 478s - loss: 0.0479 - categorical_accuracy: 0.9854   
Epoch 5/10
33600/33600 [==============================] - 462s - loss: 0.0354 - categorical_accuracy: 0.9884   
Epoch 6/10
33600/33600 [==============================] - 438s - loss: 0.0271 - categorical_accuracy: 0.9913   
Epoch 7/10
33600/33600 [==============================] - 416s - loss: 0.0263 - categorical_accuracy: 0.9912   
Epoch 8/10
33600/33600 [==============================] - 442s - loss: 0.0209 - categorical_accuracy: 0.9929   
Epoch 9/10
33600/33600 [==============================] - 474s - loss: 0.0223 - categorical_accuracy: 0.9922   
Epoch 10/10
33600/33600 [==============================] - 521s - loss: 0.0130 - categorical_accuracy: 0.9958   
train, loss and metric: [0.010848363778620427, 0.99648809523809523]
test, loss and metric: [0.042763131727420148, 0.98869047630400886]
```

### epoch 증가하기(10 ==> 20)




## reference

- <https://www.kaggle.com/yassineghouzam/introduction-to-cnn-keras-0-997-top-6>