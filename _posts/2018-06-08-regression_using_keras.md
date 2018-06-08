---
title: keras로 regression 문제 풀기
category: machine-learning
tags: keras regression machine-learning

---

## keras로 regression 문제를 풉니다. 

- 보통, neural network는 classification 문제에 적용하는 경우가 많지만, 사실 regression 문제에도 적용할 수 있습니다. 생각해보니, 저번에 mlpregressor를 사용해 본적도 있군요. 
- 아무튼, 오늘은 keras를 사용해서 직접 뉴럴넷을 모델링하고 이를 regression에 적용해보는 짓을 할 겁니다 하하핫. 
- 사실, 결론부터 말씀드리면 간단합니다. 

## modelling nn

- 뉴럴넷의 마지막 레이어의 노드 개수를 1개로 만든다.
- 이전 레이어들은 만들고 싶은 대로 뚝딱뚝딱 만든다. 
- loss function은 regression등에서 쓰이는 `keras.metris.mse`등을 이용한다. 
    - sklearn에서 이용하던 `r2_score`는 이용할 수 없습니다. 물론 직접 코딩해서 사용하실 수 는 있습니다만. 
- 그리고, 생각보다 시간이 오래 걸릴 수 있습니다. 

### case 1: regression for polynomial line

- 4제곱이 포함되어 있는 곡선이라고 해도 내가 믿는! 뉴럴넷은 알아서 잘 해결해줄 것이라 믿었는데, 꽤나 복잡하게 들어가야, 제대로 그려줍니다. 흠. 특히, 시작할때, 여러변수로부터 그려지는 것이 아니라, 하나의 변수부터 확장되는 형태라서, feature를 쪼개는 것에 어려움을 겪는 것이 아닐까 싶어요.
- 그래서 weight initializing을 잘해주는 것이 필요할 것 같습니다. 

```python
import numpy as np 
import matplotlib.pyplot as plt

from keras.models import Sequential
from keras.layers import Dense, Dropout, Activation
from keras.optimizers import SGD, Adam
from keras import metrics

from sklearn.metrics import r2_score

# data genration 
sample_size = 500

x = np.random.uniform(-15, 15, sample_size)
y = x**4 + x**3 + x + np.random.normal(0, 2, sample_size)
####

# neural net modeling 
# 생각보다, fitting하려면 복잡한 모델이 필요합니다. 
model = Sequential([
    Dense(32, kernel_initializer='normal', activation = "relu", input_shape=(1,)), 
    Dense(256, kernel_initializer='normal', activation = "relu"),
    Dense(512, kernel_initializer='normal', activation = "relu"),
    Dense(512, kernel_initializer='normal', activation = "relu"),
    Dense(512, kernel_initializer='normal', activation = "relu"),
    Dense(64, kernel_initializer='normal', activation = "relu"),
    Dense(1, kernel_initializer='normal', activation = "relu"), 
])
# regression하기 때문에, loss와 metrics들을 mean_squared_error로 선정합니다. 
model.compile(loss='mean_squared_error', 
              optimizer=Adam(lr=0.001, beta_1=0.9, beta_2=0.999, epsilon=1e-8), 
              metrics=[metrics.mse, metrics.mean_absolute_percentage_error])
####

train_history = model.fit(x, y, epochs=50, batch_size=10, validation_split=0.2, verbose=0)

print(r2_score(y, model.predict(x)))


# 대충 잘 맞는지 보기 위해서 scatter합니다. 
plt.figure(figsize=(12, 4))
plt.scatter(x, y, alpha=0.7, label='y_true')
plt.scatter(x, model.predict(x), alpha=0.7, label='y_pred')
plt.legend()
plt.savefig('../../assets/images/markdown_img/180608_1330_keras_regression.svg')
plt.show()

train_history.history.keys()

val_loss_lst = train_history.history['val_loss']
train_loss_lst = train_history.history['loss']

plt.figure(figsize=(12, 4))
plt.plot(range(0, len(val_loss_lst)), val_loss_lst, label='val_loss')
plt.plot(range(0, len(train_loss_lst)), train_loss_lst, label='train_loss')
plt.legend()
plt.savefig('../../assets/images/markdown_img/180608_1330_keras_regression_train_val_score.svg')
plt.show()
```

![](/assets/images/markdown_img/180608_1330_keras_regression.svg)

![](/assets/images/markdown_img/180608_1330_keras_regression_train_val_score.svg)

### case 2: regression for sin line

- 지금 첨부한 그림에는 전혀 Fitting이 되지 않은 직선이 그려져 있지만, 가끔 구부러진 형태로 fitting이 되기는 합니다. 
- 하지만, 형편없죠. 

```python
import numpy as np 
import matplotlib.pyplot as plt

from keras.models import Sequential
from keras.layers import Dense, Dropout, Activation
from keras.optimizers import SGD, Adam
from keras.initializers import lecun_normal
from keras import metrics

from sklearn.metrics import r2_score

# data generation
sample_size = 1000

a = np.random.uniform(-15, 15, sample_size)
b = np.sin(a)*10 + a + np.random.normal(0, 3, sample_size)
#####

# neural network modeling 
model = Sequential([
    Dense(1024, kernel_initializer=lecun_normal(seed=None), activation = "relu", input_shape=(1,)), 
    Dense(512, kernel_initializer=lecun_normal(seed=None), activation = "relu"),
    Dense(512, kernel_initializer='normal', activation = "relu"),
    Dense(512, kernel_initializer='normal', activation = "relu"),
    Dense(512, kernel_initializer='normal', activation = "relu"),
    Dense(256, kernel_initializer='normal', activation = "relu"),
    Dense(1, kernel_initializer='normal', activation = "relu"),
    
])

model.compile(loss='mean_squared_error', optimizer=Adam(lr=0.001, beta_1=0.9, beta_2=0.999, epsilon=1e-8), 
              metrics=[metrics.mse])

train_history = model.fit(a, b, epochs=100, batch_size=200, validation_split=0.2, verbose=0)
####
print("r2 score of train set: {}".format(r2_score(b, model.predict(a))))

plt.figure(figsize=(12, 4))
plt.scatter(a, b, alpha=0.6, label='y_true')
plt.scatter(a, model.predict(a), label='y_pred')
plt.legend()
plt.savefig('../../assets/images/markdown_img/180608_1333_keras_regression_sin.svg')
plt.show()

plt.figure(figsize=(12, 4))
plt.plot(range(0, len(train_history.history['val_loss'])), train_history.history['val_loss'], 
         label='val_loss')
plt.plot(range(0, len(train_history.history['val_loss'])), train_history.history['loss'], 
         label='loss')
plt.legend()
plt.savefig('../../assets/images/markdown_img/180608_1333_keras_regression_sin_score.svg')
plt.show()
```
![](/assets/images/markdown_img/180608_1333_keras_regression_sin.svg)

![](/assets/images/markdown_img/180608_1333_keras_regression_sin_score.svg)

## wrap-up 

- 생각보다, 적합한 모델을 찾는데 시간이 꽤 오래 걸렸습니다. 그리고, layer가 길고 복잡하기 때문에, 학습 자체도 오래 걸리는 문제가 있구요. 
- 다른 데이터 같은 경우에는 웬만하면 잘 작동했는데, sin곡선이 포함된 경우, 즉 fluctuation이 있는 데이터에 대해서는 상당히 적응을 못하는 것 같아요. 흠, 이것이 아마도 Recurrent Neural Network의 필요성이 아닐까 싶기도 한데, 아무튼, 그만할래요 귀찮습니다. 

## reference 

