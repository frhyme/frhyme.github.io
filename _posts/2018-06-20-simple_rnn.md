---
title: 간단하게 rnn을 만들어 봅시다. 
category: machine-learning
tags: python python-lib matplotlib numpy keras rnn sklearn 
---

## 간단한 rnn을 그려 봅시다. 

- [이 포스트](https://datascienceschool.net/view-notebook/1d93b9dc6c624fbaa6af2ce9290e2479/)의 내용을 참고하여, 정리하였습니다. 
- 여러번 포스트에서 반복적으로 얘기하는 것 같기는 하지만, 데이터 예측, 데이터 분석, 머신러닝 아무튼 이런 모든 말들을 축약하면, **"A를 활용해서 B를 예측하는 것"** 입니다. 예를 들면, 이 "키와 몸무게로 월급을 예측하자" 이런것도 말은 됩니다. 잘 맞추는지는 몰라도. 
- 독립변수와 종속 변수가 명확하게 구분되어 있으면, 간단한데, 보통 그렇지 않아요. 단 하나의 sequence data만 있다고 가정합시다. 예를 들면, 매일의 기온, 습도 등이 여기에 포함되겠죠. 오늘의 온도에 가장 크게 영향을 주는 것이 무엇일까? 생각해보면, 아마도 어제의 온도, 혹은 그저께의 온도겠죠. 
    - 다르게 말하면, 시계열 데이터 분석이라는 것은, 지난 시점의 정보를 활용하여 오늘의 정보를 예측하는 것입니다. 
    - 지난 시점의 정보를 독립변수로 두고, 오늘의 정보를 종속 변수로 두고 설계하면, 일반적인 regression 문제와 유사하게 느껴지죠. 
    - 단, RNN에서의 차이가 있다면, 바로 앞의 정보(t-1)를 좀 강하게 받아들이는 것이 차이다, 라고 이야기는 할 수 있겠네요. 
- 물론, 이것 또한, 어느 정도의 시점의 데이터들을 어느 정도로 강하게 받아들여야 하는지에 따라서 서로 다른 cell을 설계하는 것이 필요할 수도 있죠. LSTM의 경우는 Long term and Short Term Memory의 약자인데, 옛날 기억과 지금 기억을 모두 보유하고 있는 놈을 말합니다. 
    - t-n의 기억, t-1의 기억, 장기기억, 단기기억 모두 경우에 따라서 필요할 때가 있는데, 이를 함께 제어할 수 있어서 좋은 놈이라는 이야기죠. 
- 아무튼 이래저래 말이 길어졌는데, 그냥, 간단하게는 sequence data를 예측할 때는 rnn을 씁니다. 라고 해석하면 됩니다. 

## (one or many) to (one or many)

- 입력을 몇 개나 받고, 출력을 몇 개나 하냐는 이야기입니다. 아래 그림에서 아주 친절하게 설명이 되어 있습니다만, 이를 정리하면 다음과 같아요(왼쪽부터 오른쪽으로 순서대로)
    1) One to One: t시점의 데이터만 받아서, 출력을 만듭니다. image classification이 이 범위에 들어갑니다. 
    2) One to Many: t시점의 데이터를 하나 입력 받아서, 여러 개의 출력을 만듭니다. 이미지를 읽어서, 이미지에 다양한 심볼(사람, 개 등)이 포함되어 있는지, 확인하는 경우 
    3) Many to One: text 등의 sequence 데이터를 받아서, 호불호를 체크하는 경우(sentiment analysis)
    4) Many to Many: MtoM은 다시 두 가지로 쪼갤 수 있다는데, 조금 미묘하군요 
        1) machine translation
        2) syncing video image 
- 흐음. 조금 미묘하네요. 이걸 반드시 알아둘 필요는 없을 것 같습니다..

![](https://i.stack.imgur.com/WSOie.png)


## do it. 

- `keras`를 이용하여 RNN을 만들었습니다. 뉴럴넷을 설계하는 것 자체는, 그리 어렵지 않아요. 
- `keras.layers.SimpleRNN`을 이용했습니다. 
- RNN에는 x 데이터가 (n_sample, time step, x vector의 크기)로 들어와야 합니다. 각각은 
    - n_sample: sample의 수 
    - time step: t-n 에서 n이 몇인가를 묻는 것
    - x vector의 dim: 당연하지만, y vector와 같아야 함. 
- RNN 뒤에 Dense cell을 추가하여 더 복잡하게 설계하는 것도 가능합니다. 

```python
"""
- 일단 RNN을 만들기 전에, 내가 만들려고 하는 것이 (many or one) to (many or one) 중에서 무엇인지 알아야 함
- 간단한 시계열 값을 예측한다고 할 때, 이전 data 3개를 가지고, 1개의 값을 예측한다면, many to one의 형태가 되겠다. 
"""
import numpy as np 
import matplotlib.pyplot as plt
from matplotlib import gridspec

from sklearn.linear_model import LinearRegression

s = np.sin(2 * np.pi * 0.125 * np.linspace(0, 20, 50))

timestep =3 # t-3, t-2, t-1 데이터를 이용하여 t 시점의 값을 예측한다. 
xs, ys = [], []

for i in range(timestep, len(s)):
    xs.append(np.array([s[i-j] for j in range(timestep, 0, -1)]))
    ys.append(s[i])
xs, ys = np.array(xs).reshape(len(xs), 3, 1), np.array(ys).reshape(len(ys), 1)

## 이제 rnn에 적용해 봅시다. 
from keras.models import Sequential
from keras.layers import SimpleRNN, Dense

"""
RNN에는 x 데이터가 (n_sample, time step, x vector의 크기)로 들어가야 함 
- n_sample: sample의 수 
- time step: t-n 에서 n이 몇인가를 묻는 것
- x vector의 크기: 현재는 1개짜리지만, 여러 값이 들어오고, 여러 값을 한번에 예측해야 할 경우도 있음. 
    - 그리고 xvector의 크기는 yvector의 크기과 같아야 함(당연)
"""
## benchmark model: Linear Regression
reg  = LinearRegression()
reg.fit(xs.reshape(len(xs), 3), ys)

## simple RNN model 
np.random.seed(0)# seed 고정
models = [#simpleRNN에서 units은 해당 cell의 결과로 나오는 dim을 말함. 
    Sequential([SimpleRNN(units=1, input_shape=(3, 1)),
    ]), 
    Sequential([SimpleRNN(units=1, input_shape=(3, 1)),
                Dense(10, activation='linear'), 
                Dense(1, activation='linear'), 
    ]),
]

for i, m in enumerate(models):
    m.compile(loss='mse', optimizer='sgd')
    history = m.fit(xs, ys, epochs=150, verbose=0)
    print("---model_{}: training complete---".format(i))

## 그림을 그립시다. 
fig = plt.figure(figsize=(15, 4)) 
plt.plot(s[3:], 'ro-', label='original data')# 원래 plot, 앞의 3칸의 경우, 
for i, m in enumerate(models):
    plt.plot(m.predict(xs), '--', marker='o', label='model_{}'.format(i))
plt.plot(reg.predict(xs.reshape(len(xs), 3)), label='Linear Reg')
plt.legend()

plt.savefig('../../assets/images/markdown_img/180620_1538_simple_rnn.svg')
plt.show()
```

![](/assets/images/markdown_img/180620_1538_simple_rnn.svg)


## wrap-up 

- 이미 말씀드린대로, 그냥 linear regression을 이용하는 것보다 예측을 잘 못합니다. 물론 RNN의 목적이 이 regression에만 국한되어 있는 것은 아니니까요. 
- 이후에는 RNN을 이용한 다른 짓들을 해볼 수 있을텐데, 그때는 뭐 더 재밌는 것들이 있겠죠. 먼산...

## reference 

- <https://keras.io/layers/recurrent/>