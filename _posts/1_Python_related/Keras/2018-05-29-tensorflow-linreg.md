---
title: tensorflow) 기본부터 다시 - linear regression
category: machine-learning
tags: tensorflow machine-learning data-science python python-lib sklearn linear-regression

---

## 왜 나는 늘 복습만 하는가? 

- 텐서플로우는 예전부터 조금씩 공부를 하긴 했는데, 자료가 다 여기저기 흩어져 있어서ㅠㅠㅠ여기에 다시 정리해두기로 했습니다. 
- 사실, 솔직한 고민은 좀 있습니다. `keras`가 있는데 굳이 tensorflow를 써야 하나? 필요할까? 라는 생각도 들지만, 할까 말까 고민을 하다보면 하기 싫어서 뒤로 미루게 되더라고요. 
- 글을 쓰면서 생각해보니, 김성훈 교수님의 강화학습 자료를 정리하는데도 tensorflow가 쓰이기 때문에, 그냥 tensorflow를 다시 공부하면서 마무리하는 것이 훨씬 좋을 것 같습니다. 

## tensorflow basic

- tensorflow로 코딩하면서, 절대로 잊어버리지 않아야 하는 것들은 대략 다음과 같습니다. 

### type?

- `tf.Constant`: 그냥, 상수. 그러나 얘도 `tf.Session()`이 실행해줘야 값을 알 수 있음. 거의 쓸 일 없음. 
- `tf.placeholder`: 미리 데이터를 넣어주지 않고, 이후에 넘겨줍니다. placeholder를 이용해 만들어진 computation graph의 값을 계산하기 위해서, 돌릴 때, `feed_dict={}`의 형태로 안에 넘겨줍니다. 
- `tf.Variable`: 최소화되는 놈들(weight, bias 등)은 항상 `tf.Variable`로 선언되어야 함. 그래야, optimizer에게 cost를 minimize하라고 하면, 알아서 이 값들이 최적의 값으로 변경됨. 
    - 일반적으로 코딩에서 `variable`은 내가 값을 정의해주는 놈이라고 생각하지만, 텐서에서는 위대한 기계님이 결정해주는 값이다, 라고 생각하는 것이 좋음. 

### operation?

- tensorflow로 코딩한다는 것은 ==> computational graph를 설계한다는 것 
- lazy evaluation ==> 값은 `tf.Session()`에 넣어서 돌리기 전에는 값이 무엇인지 알 수 없다는 것 
- `tf.Session`을 무조건, 돌리기 전에는 초기화가 필요하다는 것
    - `tf.Variable()`의 경우는 아직 결정되지 않은 값이므로, 랜덤한 값으로 초기화해주는 것이 필요함. 

## 일단은 Linear regression이라고 해봅시다. 

- 해봐야 압니다. 해봐야 쉬워요. 

```python
import tensorflow as tf
import numpy as np 
import matplotlib.pyplot as plt

"""
임의의 값들을 y = 3 x1 + 2 x2 + 3에 의해 만들었습니다. 
"""
x_data = np.random.random_sample(10000).reshape(5000, 2)
y_data = x_data.dot(np.array([3,2]).reshape(2, 1)) + 3

"""
우리는 해당 x_data를 활용해 y_data를 잘 예측하려고 합니다. 다양한 복잡한 모델을 만들 수도 있지만, 
간단하게 1차 선형방정식의 형태로 모델을 세운다고 생각했습니다. 
- x_data에 곱해지는 W, 그리고 더해지는 b 는 '어떤 값'이 있을텐데, 아직은 모릅니다. 우리가 찾아줘야죠. 
- 이렇게 우리가 모르는 그것들을 아래처럼 tf.Variable로 만듭니다. 
- argument로 tf.random_normal([2,1])이라는 것이 들어가는데, 실행시에 초기값을 어떻게 설정해줄 것인지, 그 함수를 지정해줍니다. 
"""
W = tf.Variable(tf.random_normal([2, 1]), name='weight')
b = tf.Variable(tf.random_normal([1]), name='bias')

"""
- tf.placeholder 라는 타입으로 비워져 있도록 해두고, 이후에 앞서 만든 x_data, y_data를 여기에 연결해줍니다. 
- shape의 경우 행은 몇 개나 들어올지 모르니까, None으로 두고, 열은 2, 1로 각각 세팅해둡니다. 
"""
X = tf.placeholder(tf.float32, shape=[None, 2])
Y = tf.placeholder(tf.float32, shape=[None, 1])

# hypothesis function: 간단히, 우리가 정의한 예측 모델 
hypothesis = tf.matmul(X, W) + b
"""
hypothesis = tf.matmul(tf.multiply(X, X), W) + b
hypothesis를 바꾸어서 돌려도 상관없다. 요 부분 빼고 나머지는 모두 동일하므로. 
"""
# 
"""
- cost function은 현재 만들어진 모델이 얼마나 잘 만들어졌는지를 어떻게 평가할 것인가? 를 위해서 정의됩니다. 아래는 (hypothesis(우리가 예측한 모델) - 실제값)^2 을 모두 더해서 cost를 평가합니다. 
- optimizer는 최적화 방법을 말합니다. 보통 GradientDescent method(경사하강법)을 많이 사용하는데, learning_rate는 클수록 tf.Variable 의 변화가 크고, 적을수록 변화가 적습니다. 
- 정의된 optimizer에게, 'cost'를 최소화하는 방향으로 움직이라고 명령해줍니다. 
"""
cost = tf.reduce_mean(tf.square(hypothesis - Y))
optimizer = tf.train.GradientDescentOptimizer(learning_rate=0.01)
train = optimizer.minimize(cost)

sess = tf.Session()
sess.run(tf.global_variables_initializer())

for step in range(5000):
"""아래 sess.run()처럼 여러 변수를 리스트로 한번에 넘기고, 한번에 리턴받아서 처리하는 것이 깔끔한 형태 
"""
    cost_val, W_val, b_val, _ = sess.run([cost, W, b, train],
                                         feed_dict={X: x_data, Y: y_data}) # 1) 
    if step == 5000 -1:
        print("step {}: cost({})".format(step, cost_val))
        print("W: {}, \nb: {}".format(W_val, b_val))
```

- 위 코드를 `learning_rate=0.01` 로 10000번 돌리면, 아래처럼 거의 비슷하게 나오는 것을 알 수 있습니다. 

```
step 9999: cost(1.4084675648007305e-09)
W: [[ 2.99989271]
 [ 1.99992871]], 
b: [ 3.00009561]
```

## machine learning 과 data mining이 다릅니까? 

- 좀 뜬금없지만, deep learning/machine learning을 공부하기 위해서 `tensorflow` 를 공부하는데, 가장 먼저 접하는 것은 `linear regression`을 계산하는 것입니다. 그런데, 우리는 이미 data mining같은 통계 수업에서, `linear regression`을 찾는 공식을 배웠습니다. 
- 그럼 뭐가 다를까요? 접근 방식이 다릅니다. 
    - 우리가 원래 알던 linear regression은 공식에 넣어서 적합한 coefficient과 bias를 계산해주는 형태인데 반해서, machine learning에서는 `Hypothesis function`과 `cost function`을 정의하고, cost를 줄여주는 방향으로 Hypothesis의 weight, bias 등의 coefficient들을 update해가면서 최종적으로 가장 cost를 적게 가지는 hypothesis function의 coefficient를 찾아주는 것을 목적으로 합니다. 

- 즉, 요즘의 machine learning은 `iterative method`입니다. 
    - 따라서, 이전 data mining에서의 linear regression과는 계산 시간에에 압도적인 차이가 발생합니다. 
    - 실제로 sklearn에서 지원하는 linear regression의 경우는 공식에 넣어서 계산하므로 아주 빨리 그 값이 계산되는 반면, tensorflow에서는 매우 느리게 계산됩니다. 앞서 말한 이유에 의해서 그런 것이죠. 

- 또한, 당연한 이야기지만, tensorflow는 사실, hypothesis function이 linear model인지, polynomial인지, 무엇인지 전혀 관심이 없습니다. 
    - 그냥, 1) 원래 예측 모델과 그 계수들이 있고, 2) cost function으로 잘 맞추는지를 계산할 수 있고, 3) update를 통해 weight를 조절하여 cost 를 줄이는 방향으로 간다. 이것이 다죠. 그래서 좀 더 범용적이라고, 생각됩니다. 
    - sklearn에서도 모든 모델이 `fit`, `predict`로 같은 interface를 가지는데, 이것 또한, 모델 부분만 바꿔가면서 다양한 모델에 적용하는 것을 편하게 할 수 있도록 하는 것 같네요. 

### sklearn linreg vs. tensorflow

- 그래서, sklearn에서의 선형 회귀방정시을 구해보고, tensorflow에서도 구해보고 그 계산시간과 결과를 비교해보겠습니다. 
    - tensorflow 코드의 경우 5000번 돌릴 때, 4.9초 소요
    - sklearn로 작성한 아래 코드의 경우 0.05초 소요 
- 사실 자명하지만, sklearn이 훨씬 빠릅니다. 방법이 다르니까요. 

```python
from sklearn.linear_model import LinearRegression
linModel= LinearRegression()
linModel.fit(x_data, y_data)
print("W: {}, b: {}".format(linModel.coef_, linModel.intercept_))
```


## wrap-up 

- 다시, tensorflow를 공부하고 정리해두었습니다. 볼 때마다, 예전보다 쉽게 이해되는 것 같은 착각이 드는데 정말일까요. 
- `sklearn`만 잘 사용해도, 꽤 잘할 수 있는데, 굳이 텐서플로우를 배워야 하는가? 라는 생각이 솔직히 듭니다. 하지만, rnn도 공부하고, reinforcement learning도 해야 하니까, 그냥 계속 해볼게요 하하하핫. 