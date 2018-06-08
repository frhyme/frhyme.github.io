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

- 단순히 epoch만 증가했는데, 또 0.98842로 약간 score 상승

```
Epoch 1/20
33600/33600 [==============================] - 526s - loss: 0.5985 - categorical_accuracy: 0.8046   
Epoch 2/20
33600/33600 [==============================] - 482s - loss: 0.0885 - categorical_accuracy: 0.9729   
Epoch 3/20
33600/33600 [==============================] - 10337s - loss: 0.0556 - categorical_accuracy: 0.9826  
Epoch 4/20
33600/33600 [==============================] - 2295s - loss: 0.0458 - categorical_accuracy: 0.9856  
Epoch 5/20
33600/33600 [==============================] - 396s - loss: 0.0366 - categorical_accuracy: 0.9883   
Epoch 6/20
33600/33600 [==============================] - 384s - loss: 0.0277 - categorical_accuracy: 0.9914   
Epoch 7/20
33600/33600 [==============================] - 383s - loss: 0.0215 - categorical_accuracy: 0.9934   
Epoch 8/20
33600/33600 [==============================] - 379s - loss: 0.0216 - categorical_accuracy: 0.9925   
Epoch 9/20
33600/33600 [==============================] - 363s - loss: 0.0192 - categorical_accuracy: 0.9940   
Epoch 10/20
33600/33600 [==============================] - 371s - loss: 0.0147 - categorical_accuracy: 0.9947   
Epoch 11/20
33600/33600 [==============================] - 370s - loss: 0.0129 - categorical_accuracy: 0.9964   
Epoch 12/20
33600/33600 [==============================] - 377s - loss: 0.0110 - categorical_accuracy: 0.9965   
Epoch 13/20
33600/33600 [==============================] - 416s - loss: 0.0126 - categorical_accuracy: 0.9963   
Epoch 14/20
33600/33600 [==============================] - 391s - loss: 0.0080 - categorical_accuracy: 0.9976   
Epoch 15/20
33600/33600 [==============================] - 384s - loss: 0.0070 - categorical_accuracy: 0.9977   
Epoch 16/20
33600/33600 [==============================] - 386s - loss: 0.0077 - categorical_accuracy: 0.9974   
Epoch 17/20
33600/33600 [==============================] - 375s - loss: 0.0080 - categorical_accuracy: 0.9975   
Epoch 18/20
33600/33600 [==============================] - 387s - loss: 0.0057 - categorical_accuracy: 0.9981   
Epoch 19/20
33600/33600 [==============================] - 374s - loss: 0.0059 - categorical_accuracy: 0.9980   
Epoch 20/20
33600/33600 [==============================] - 381s - loss: 0.0065 - categorical_accuracy: 0.9978   
train, loss and metric: [0.010528954193425652, 0.9966666666666667]
test, loss and metric: [0.047946910524873862, 0.98821428594135108]
```

### epoch and more Convolution 

- epoch은 20으로 고정하고, convolution을 더 늘려보겠습니다. 아직 충분히 overfitting되었다고 생각하지 않아서, dropout은 넣지 않았습니다. 
- dropout을 넣지 않아서 그런지는 몰라도, 제출결과는 0.98765로 딱히 점수가 좋아지지는 않았습니다. 
- 다음에는 dropout을 추가해서 진행하면 좋을 것 같네요. 

```
Epoch 1/20
33600/33600 [==============================] - 470s - loss: 0.9917 - categorical_accuracy: 0.6965   
Epoch 2/20
33600/33600 [==============================] - 433s - loss: 0.1283 - categorical_accuracy: 0.9590   
Epoch 3/20
33600/33600 [==============================] - 423s - loss: 0.0739 - categorical_accuracy: 0.9766   
Epoch 4/20
33600/33600 [==============================] - 424s - loss: 0.0603 - categorical_accuracy: 0.9813   
Epoch 5/20
33600/33600 [==============================] - 417s - loss: 0.0408 - categorical_accuracy: 0.9873   
Epoch 6/20
33600/33600 [==============================] - 421s - loss: 0.0317 - categorical_accuracy: 0.9900   
Epoch 7/20
33600/33600 [==============================] - 415s - loss: 0.0342 - categorical_accuracy: 0.9884   
Epoch 8/20
33600/33600 [==============================] - 427s - loss: 0.0281 - categorical_accuracy: 0.9906   
Epoch 9/20
33600/33600 [==============================] - 406s - loss: 0.0219 - categorical_accuracy: 0.9930   
Epoch 10/20
33600/33600 [==============================] - 407s - loss: 0.0171 - categorical_accuracy: 0.9949   
Epoch 11/20
33600/33600 [==============================] - 414s - loss: 0.0154 - categorical_accuracy: 0.9950   
Epoch 12/20
33600/33600 [==============================] - 408s - loss: 0.0155 - categorical_accuracy: 0.9948   
Epoch 13/20
33600/33600 [==============================] - 406s - loss: 0.0168 - categorical_accuracy: 0.9941   
Epoch 14/20
33600/33600 [==============================] - 406s - loss: 0.0177 - categorical_accuracy: 0.9938   
Epoch 15/20
33600/33600 [==============================] - 409s - loss: 0.0106 - categorical_accuracy: 0.9960   
Epoch 16/20
33600/33600 [==============================] - 415s - loss: 0.0199 - categorical_accuracy: 0.9936   
Epoch 17/20
33600/33600 [==============================] - 406s - loss: 0.0167 - categorical_accuracy: 0.9948   
Epoch 18/20
33600/33600 [==============================] - 406s - loss: 0.0072 - categorical_accuracy: 0.9976   
Epoch 19/20
33600/33600 [==============================] - 413s - loss: 0.0183 - categorical_accuracy: 0.9940   
Epoch 20/20
33600/33600 [==============================] - 408s - loss: 0.0085 - categorical_accuracy: 0.9975   
train, loss and metric: [0.0082378579511229576, 0.99711309523809522]
test, loss and metric: [0.043590596066787841, 0.98916666689373201]
```


### increase epoch and add dropout

- dropout을 0.25의 비율로 각 레이어들 사이에 넣었습니다.
- epoch 또한 30으로 증가했습니다. 
- 그 결과, 0.99를 넘겼습니다. 0.99185. 

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
    Dropout(0.25),
    
    Conv2D(filters = 64, kernel_size = (3,3),padding = 'Same', activation ='relu'),
    Conv2D(filters = 64, kernel_size = (3,3),padding = 'Same', activation ='relu'),
    MaxPooling2D(pool_size=(2,2), strides=(2,2)),
    Dropout(0.25),
    
    Conv2D(filters = 128, kernel_size = (2,2),padding = 'Same', activation ='relu'),
    Conv2D(filters = 128, kernel_size = (2,2),padding = 'Same', activation ='relu'),
    MaxPooling2D(pool_size=(2,2), strides=(2,2)),
    Dropout(0.25),
    
    Conv2D(filters = 256, kernel_size = (2,2),padding = 'Same', activation ='relu'),
    Conv2D(filters = 256, kernel_size = (2,2),padding = 'Same', activation ='relu'),
    MaxPooling2D(pool_size=(2,2), strides=(2,2)),
    Dropout(0.25),
    
    Flatten(),
    Dense(256, activation = "relu"),
    #Dropout(0.5),
    Dense(10, activation = "softmax")
])

model.compile(loss='categorical_crossentropy', 
              optimizer=Adam(lr=0.001, beta_1=0.9, beta_2=0.999, epsilon=1e-8), 
              metrics=[metrics.categorical_accuracy])

train_history = model.fit(x_train, y_train, epochs=30, batch_size=500, verbose=1)
train_history = train_history.history

loss_and_metric = model.evaluate(x_train, y_train, batch_size=128, verbose=0)
print("train, loss and metric: {}".format(loss_and_metric))
loss_and_metric = model.evaluate(x_test, y_test, batch_size=128, verbose=0)
print("test, loss and metric: {}".format(loss_and_metric))

# 테스트 셋에 적용함. 
test_X_values = (test_df.values.astype(np.float64)/256.0).reshape(len(test_df), 28, 28, 1)
test_y_pred = model.predict_classes(test_X_values)

submit_df = pd.DataFrame({"ImageId":range(1, 1+len(test_y_pred)), "Label":test_y_pred})
submit_df.to_csv('test_mnist.csv', index=False)
```

- 단지, `Dropout`을 추가하고, epoch을 늘렸더니, train, test set에 대해서 모두 0.99를 넘긴 것을 알 수 있음. 
- 다음에 이 상태 그대로 epoch만 늘려서 계산하면, 0.99를 더 넘길 수 있을까? 

```
Epoch 1/30
33600/33600 [==============================] - 600s - loss: 1.2807 - categorical_accuracy: 0.5363   
Epoch 2/30
33600/33600 [==============================] - 642s - loss: 0.1953 - categorical_accuracy: 0.9403   
Epoch 3/30
33600/33600 [==============================] - 530s - loss: 0.1280 - categorical_accuracy: 0.9613   
Epoch 4/30
33600/33600 [==============================] - 516s - loss: 0.0981 - categorical_accuracy: 0.9710   
Epoch 5/30
33600/33600 [==============================] - 545s - loss: 0.0818 - categorical_accuracy: 0.9754   
Epoch 6/30
33600/33600 [==============================] - 596s - loss: 0.0693 - categorical_accuracy: 0.9790   
Epoch 7/30
33600/33600 [==============================] - 488s - loss: 0.0646 - categorical_accuracy: 0.9806   
Epoch 8/30
33600/33600 [==============================] - 601s - loss: 0.0586 - categorical_accuracy: 0.9825   
Epoch 9/30
33600/33600 [==============================] - 500s - loss: 0.0588 - categorical_accuracy: 0.9827   
Epoch 10/30
33600/33600 [==============================] - 490s - loss: 0.0475 - categorical_accuracy: 0.9861   
Epoch 11/30
33600/33600 [==============================] - 492s - loss: 0.0439 - categorical_accuracy: 0.9869   
Epoch 12/30
33600/33600 [==============================] - 522s - loss: 0.0394 - categorical_accuracy: 0.9875   
Epoch 13/30
33600/33600 [==============================] - 488s - loss: 0.0397 - categorical_accuracy: 0.9879   
Epoch 14/30
33600/33600 [==============================] - 499s - loss: 0.0370 - categorical_accuracy: 0.9890   
Epoch 15/30
33600/33600 [==============================] - 551s - loss: 0.0316 - categorical_accuracy: 0.9907   
Epoch 16/30
33600/33600 [==============================] - 499s - loss: 0.0317 - categorical_accuracy: 0.9901   
Epoch 17/30
33600/33600 [==============================] - 494s - loss: 0.0311 - categorical_accuracy: 0.9903   
Epoch 18/30
33600/33600 [==============================] - 557s - loss: 0.0339 - categorical_accuracy: 0.9893   
Epoch 19/30
33600/33600 [==============================] - 520s - loss: 0.0313 - categorical_accuracy: 0.9901   
Epoch 20/30
33600/33600 [==============================] - 551s - loss: 0.0281 - categorical_accuracy: 0.9913   
Epoch 21/30
33600/33600 [==============================] - 569s - loss: 0.0231 - categorical_accuracy: 0.9929   
Epoch 22/30
33600/33600 [==============================] - 533s - loss: 0.0252 - categorical_accuracy: 0.9920   
Epoch 23/30
33600/33600 [==============================] - 574s - loss: 0.0222 - categorical_accuracy: 0.9927   
Epoch 24/30
33600/33600 [==============================] - 522s - loss: 0.0206 - categorical_accuracy: 0.9933   
Epoch 25/30
33600/33600 [==============================] - 478s - loss: 0.0334 - categorical_accuracy: 0.9899   
Epoch 26/30
33600/33600 [==============================] - 508s - loss: 0.0263 - categorical_accuracy: 0.9917   
Epoch 27/30
33600/33600 [==============================] - 584s - loss: 0.0223 - categorical_accuracy: 0.9936   
Epoch 28/30
33600/33600 [==============================] - 539s - loss: 0.0178 - categorical_accuracy: 0.9946   
Epoch 29/30
33600/33600 [==============================] - 502s - loss: 0.0169 - categorical_accuracy: 0.9951   
Epoch 30/30
33600/33600 [==============================] - 648s - loss: 0.0177 - categorical_accuracy: 0.9945   
train, loss and metric: [0.0060941704176920687, 0.99824404761904761]
test, loss and metric: [0.028339080603438475, 0.99226190476190479]
```

### more dropout, more epoch, more fully connecte layer 

- dropout을 추가하고, epoch도 추가하고, fully connected layer도 추가했다. 
- 그 결과로 0.99271 까지 올렸음. 지금까지 최고 기록. 
- epoch을 한 더 올려서 한번만 더 해보면 좋을 것 같다.
- epoch에 따른 score의 변화 정도를 보면, epoch을 좀 더 올려도 괜찮을 것 같은데, 흠.


```python
import pandas as pd
import numpy as np
import keras
import tensorflow as tf 

from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import accuracy_score

from keras.models import Sequential
from keras.layers import Dense, Dropout, Activation, Conv2D, Flatten, MaxPooling2D
from keras.optimizers import SGD
from keras import metrics


X = train_df[train_df.columns[1:]]
Y = pd.get_dummies(train_df['label'])

X_values = (X.values.astype(np.float64)/256.0).reshape(len(X), 28, 28, 1)
Y_values = Y.values.astype(np.float32)

x_train, x_test, y_train, y_test = train_test_split(X_values, Y_values, 
                                                    test_size = 0.2, random_state=42)


model = Sequential([
    Conv2D(filters = 32, kernel_size = (5,5),padding = 'Same', activation ='relu', input_shape = (28,28,1)),
    Conv2D(filters = 32, kernel_size = (5,5),padding = 'Same', activation ='relu'),
    MaxPooling2D(pool_size=(2,2)),
    Dropout(0.25),
    
    Conv2D(filters = 64, kernel_size = (3,3),padding = 'Same', activation ='relu'),
    Conv2D(filters = 64, kernel_size = (3,3),padding = 'Same', activation ='relu'),
    MaxPooling2D(pool_size=(2,2), strides=(2,2)),
    Dropout(0.25),
    
    Conv2D(filters = 128, kernel_size = (2,2),padding = 'Same', activation ='relu'),
    Conv2D(filters = 128, kernel_size = (2,2),padding = 'Same', activation ='relu'),
    MaxPooling2D(pool_size=(2,2), strides=(2,2)),
    Dropout(0.25),
    
    Conv2D(filters = 256, kernel_size = (2,2),padding = 'Same', activation ='relu'),
    Conv2D(filters = 256, kernel_size = (2,2),padding = 'Same', activation ='relu'),
    MaxPooling2D(pool_size=(2,2), strides=(2,2)),
    Dropout(0.25),
    
    Flatten(),
    Dense(1024, activation = "relu"),
    Dropout(0.5),
    Dense(512, activation = "relu"),
    Dropout(0.5),
    Dense(256, activation = "relu"),
    Dropout(0.5),
    Dense(128, activation = "relu"),
    Dropout(0.5),
    Dense(32, activation = "relu"),
    Dense(10, activation = "softmax")
])

model.compile(loss='categorical_crossentropy', 
              optimizer=Adam(lr=0.001, beta_1=0.9, beta_2=0.999, epsilon=1e-8), 
              metrics=[metrics.categorical_accuracy])

train_history = model.fit(x_train, y_train, epochs=60, batch_size=500, verbose=1)
train_history = train_history.history

loss_and_metric = model.evaluate(x_train, y_train, batch_size=128, verbose=0)
print("train, loss and metric: {}".format(loss_and_metric))
loss_and_metric = model.evaluate(x_test, y_test, batch_size=128, verbose=0)
print("test, loss and metric: {}".format(loss_and_metric))
```

```
Epoch 1/60
33600/33600 [==============================] - 463s - loss: 2.2920 - categorical_accuracy: 0.1304   
Epoch 2/60
33600/33600 [==============================] - 446s - loss: 1.8574 - categorical_accuracy: 0.2776   
Epoch 3/60
33600/33600 [==============================] - 446s - loss: 0.7728 - categorical_accuracy: 0.7252   
Epoch 4/60
33600/33600 [==============================] - 431s - loss: 0.3059 - categorical_accuracy: 0.9269   
Epoch 5/60
33600/33600 [==============================] - 439s - loss: 0.2131 - categorical_accuracy: 0.9551   
Epoch 6/60
33600/33600 [==============================] - 433s - loss: 0.1614 - categorical_accuracy: 0.9657   
Epoch 7/60
33600/33600 [==============================] - 438s - loss: 0.1254 - categorical_accuracy: 0.9727   
Epoch 8/60
33600/33600 [==============================] - 440s - loss: 0.1074 - categorical_accuracy: 0.9790   
Epoch 9/60
33600/33600 [==============================] - 431s - loss: 0.1039 - categorical_accuracy: 0.9772   
Epoch 10/60
33600/33600 [==============================] - 428s - loss: 0.0926 - categorical_accuracy: 0.9812   
Epoch 11/60
33600/33600 [==============================] - 430s - loss: 0.0786 - categorical_accuracy: 0.9831   
Epoch 12/60
33600/33600 [==============================] - 428s - loss: 0.0829 - categorical_accuracy: 0.9827   
Epoch 13/60
33600/33600 [==============================] - 432s - loss: 0.0811 - categorical_accuracy: 0.9840   
Epoch 14/60
33600/33600 [==============================] - 429s - loss: 0.0647 - categorical_accuracy: 0.9871   
Epoch 15/60
33600/33600 [==============================] - 433s - loss: 0.0676 - categorical_accuracy: 0.9864   
Epoch 16/60
33600/33600 [==============================] - 444s - loss: 0.0622 - categorical_accuracy: 0.9869   
Epoch 17/60
33600/33600 [==============================] - 433s - loss: 0.0713 - categorical_accuracy: 0.9851   
Epoch 18/60
33600/33600 [==============================] - 433s - loss: 0.0545 - categorical_accuracy: 0.9885   
Epoch 19/60
33600/33600 [==============================] - 431s - loss: 0.0476 - categorical_accuracy: 0.9902   
Epoch 20/60
33600/33600 [==============================] - 432s - loss: 0.0478 - categorical_accuracy: 0.9903   
Epoch 21/60
33600/33600 [==============================] - 430s - loss: 0.0506 - categorical_accuracy: 0.9894   
Epoch 22/60
33600/33600 [==============================] - 431s - loss: 0.0474 - categorical_accuracy: 0.9907   
Epoch 23/60
33600/33600 [==============================] - 433s - loss: 0.0449 - categorical_accuracy: 0.9907   
Epoch 24/60
33600/33600 [==============================] - 435s - loss: 0.0483 - categorical_accuracy: 0.9896   
Epoch 25/60
33600/33600 [==============================] - 444s - loss: 0.0360 - categorical_accuracy: 0.9924   
Epoch 26/60
33600/33600 [==============================] - 442s - loss: 0.0473 - categorical_accuracy: 0.9901   
Epoch 27/60
33600/33600 [==============================] - 447s - loss: 0.0421 - categorical_accuracy: 0.9910   
Epoch 28/60
33600/33600 [==============================] - 445s - loss: 0.0382 - categorical_accuracy: 0.9916   
Epoch 29/60
33600/33600 [==============================] - 460s - loss: 0.0444 - categorical_accuracy: 0.9905   
Epoch 30/60
33600/33600 [==============================] - 429s - loss: 0.0385 - categorical_accuracy: 0.9914   
Epoch 31/60
33600/33600 [==============================] - 431s - loss: 0.0334 - categorical_accuracy: 0.9922   
Epoch 32/60
33600/33600 [==============================] - 432s - loss: 0.0356 - categorical_accuracy: 0.9925   
Epoch 33/60
33600/33600 [==============================] - 432s - loss: 0.0344 - categorical_accuracy: 0.9921   
Epoch 34/60
33600/33600 [==============================] - 432s - loss: 0.0511 - categorical_accuracy: 0.9890   
Epoch 35/60
33600/33600 [==============================] - 428s - loss: 0.0332 - categorical_accuracy: 0.9928   
Epoch 36/60
33600/33600 [==============================] - 431s - loss: 0.0367 - categorical_accuracy: 0.9925   
Epoch 37/60
33600/33600 [==============================] - 428s - loss: 0.0384 - categorical_accuracy: 0.9922   
Epoch 38/60
33600/33600 [==============================] - 433s - loss: 0.0316 - categorical_accuracy: 0.9936   
Epoch 39/60
33600/33600 [==============================] - 428s - loss: 0.0324 - categorical_accuracy: 0.9932   
Epoch 40/60
33600/33600 [==============================] - 432s - loss: 0.0333 - categorical_accuracy: 0.9933   
Epoch 41/60
33600/33600 [==============================] - 430s - loss: 0.0287 - categorical_accuracy: 0.9940   
Epoch 42/60
33600/33600 [==============================] - 428s - loss: 0.0326 - categorical_accuracy: 0.9936   
Epoch 43/60
33600/33600 [==============================] - 430s - loss: 0.0283 - categorical_accuracy: 0.9941   
Epoch 44/60
33600/33600 [==============================] - 428s - loss: 0.0285 - categorical_accuracy: 0.9943   
Epoch 45/60
33600/33600 [==============================] - 429s - loss: 0.0256 - categorical_accuracy: 0.9946   
Epoch 46/60
33600/33600 [==============================] - 434s - loss: 0.0249 - categorical_accuracy: 0.9950   
Epoch 47/60
33600/33600 [==============================] - 433s - loss: 0.0314 - categorical_accuracy: 0.9936   
Epoch 48/60
33600/33600 [==============================] - 429s - loss: 0.0278 - categorical_accuracy: 0.9943   
Epoch 49/60
33600/33600 [==============================] - 433s - loss: 0.0278 - categorical_accuracy: 0.9941   
Epoch 50/60
33600/33600 [==============================] - 428s - loss: 0.0258 - categorical_accuracy: 0.9949   
Epoch 51/60
33600/33600 [==============================] - 428s - loss: 0.0316 - categorical_accuracy: 0.9938   
Epoch 52/60
33600/33600 [==============================] - 428s - loss: 0.0282 - categorical_accuracy: 0.9944   
Epoch 53/60
33600/33600 [==============================] - 431s - loss: 0.0366 - categorical_accuracy: 0.9930   
Epoch 54/60
33600/33600 [==============================] - 432s - loss: 0.0360 - categorical_accuracy: 0.9928   
Epoch 55/60
33600/33600 [==============================] - 433s - loss: 0.0372 - categorical_accuracy: 0.9923   
Epoch 56/60
33600/33600 [==============================] - 436s - loss: 0.0336 - categorical_accuracy: 0.9929   
Epoch 57/60
33600/33600 [==============================] - 434s - loss: 0.0366 - categorical_accuracy: 0.9930   
Epoch 58/60
33600/33600 [==============================] - 435s - loss: 0.0302 - categorical_accuracy: 0.9938   
Epoch 59/60
33600/33600 [==============================] - 433s - loss: 0.0234 - categorical_accuracy: 0.9950   
Epoch 60/60
33600/33600 [==============================] - 432s - loss: 0.0282 - categorical_accuracy: 0.9941   
train, loss and metric: [0.005773499012014305, 0.99863095238095234]
test, loss and metric: [0.036450345025153923, 0.99321428594135108]
```


## more epoch

- epoch을 좀 더 올리고, 그만큼 dropout도 더 올려보자. 

## reference

- <https://www.kaggle.com/yassineghouzam/introduction-to-cnn-keras-0-997-top-6>