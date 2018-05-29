---
title: tensorflow) logistic regression
category: machine-learning
tags: python tensorflow python-lib logistic-regression
---

## logistic regression

- 머신러닝은 단순하게, '모델(hypothesis)'을 세우고, 이 모델이 맞는지/아닌지 평가하는 cost function을 통해 변수를 조절하는 것을 말합니다. 
- classification의 경우도, '잘 예측할 만한 모델'을 세우고, 이 모델을 평가하는 'cost'를 세우고 변수를 최적화하면서 진행합니다. 이 포스트에서 배울 `logistic regression`은 classification에서 많이 썼던, 초기의 테크닉을 말합니다. 

![logistic function](https://upload.wikimedia.org/wikipedia/commons/thumb/8/88/Logistic-curve.svg/1200px-Logistic-curve.svg.png)

## logistic reg을 적용할 데이터 생성!

- 서로 다른 평균을 가지는 gaussian distribution에 따라 랜덤으로 (1000, 2)의 데이터를 각각 생성했습니다. 
    - 이후에는 평균을 좀 조절하면서 해볼게요. 

```python
import matplotlib.pyplot as plt
import numpy as np

sample_size = 1000
x_data = np.vstack(
    [np.array([np.random.normal(0, 1, sample_size) for i in range(0, 2)]).reshape(sample_size, 2),
     np.array([np.random.normal(5, 1, sample_size) for i in range(0, 2)]).reshape(sample_size, 2)]
)
y_data = np.array([0 for i in range(0, sample_size)]+[1 for i in range(0, sample_size)]).reshape(sample_size*2, 1)
plt.figure(figsize=(12, 4))
plt.scatter(x_data[:, 0], x_data[:, 1], c=y_data, cmap = plt.cm.rainbow, alpha=0.3)
plt.savefig('../../assets/images/markdown_img/guassian_random_sample_20180529_1545.svg')
plt.show()
```

![](/assets/images/markdown_img/guassian_random_sample_20180529_1545.svg)

## tensorlfow model 생성!

```python
X = tf.placeholder(tf.float32, shape=[None, 2])
Y = tf.placeholder(tf.float32, shape=[None, 1])

W = tf.Variable(tf.random_normal([2, 1]), name='weight')
b = tf.Variable(tf.random_normal([1]), name='bias')

"""
- 우리가 세운 모델은 sigmoid function처럼 맞는 경우, 확률이 커지고, 아닐 경우 확률이 줄어드는 모델입니다. 
- 대충 1/ (1 + e^(w*x + b))의 형태인데, 전체 sample에 대해서 이를 잘 분리해주는 w, b를 찾아내는 것이죠. 
"""
hypothesis = tf.sigmoid(tf.matmul(X, W) + b)
# cost/loss function
"""
- cost를 주는 방식은 다양한데, 
    1) 잘한 것을 평가하여 음수를 곱하여 minimize, 
    2) 못한 것을 평가하여 minimize
- hypothesis 는 무조건 0과 1사이의 값만을 가지며 따라서, log(hypothesis)는 (-inf, 0)의 값을 가집니다. 
    - hypothesis가 클수록 log(hypothesis)는 작은 음수값, (0, 1) => (-inf, 0)
    - hypothesis가 클수록, 적은 penalty(음수)를 가지도록 Y=1, Y=0 각각에 대해서 항을 정의하고 그 총합을 minimizegka 
"""
cost = -tf.reduce_mean(Y * tf.log(hypothesis) + (1 - Y) * tf.log(1 - hypothesis))
train = tf.train.GradientDescentOptimizer(learning_rate=0.01).minimize(cost)

# Accuracy computation
# True if hypothesis>0.5 else False
"""
- tf.cast는 boolean => tf.float32인 함수인 것 같네요 
- accuracy는 간단하게, predicted와 Y가 만을 때를 다 더하고 총 개수로 나누어줍니다(평균)
"""
predicted = tf.cast(hypothesis > 0.5, dtype=tf.float32)
accuracy = tf.reduce_mean(tf.cast(tf.equal(predicted, Y), dtype=tf.float32))

"""
- tf.Session()을 지역변수처럼 선언하고 썻기 때문에, 저 구문 밖에서는 생성된, W, b를 쓸 수 없어요. 물론 함수로 만들어서 해도 되긴 하지만, 귀찮아서 그냥 아래처럼 새로운 변수를 만들어 놓고 최종 값을 저기에 넣어주는 식으로 했어요. 
"""
npW = 0
npb = 0
# Launch graph
"""
- 이건, 아마도 처음 나온 형식인 것 같은데, 일종의 지역변수 설정이라고 생각하면 됩니다. 
with 구문 아래에 들여쓰기된 부분에서만 살아 있으며, 여기를 벗어나면 sess는 자동으로 사라짐. 
"""
with tf.Session() as sess:
    # Initialize TensorFlow variables
    sess.run(tf.global_variables_initializer())
    
    for step in range(10001):
        cost_val, _ = sess.run([cost, train], feed_dict={X: x_data, Y: y_data})
        if step % 2500 == 0:
            print(step, cost_val)
    # Accuracy report
    h, c, a = sess.run([hypothesis, predicted, accuracy],
                       feed_dict={X: x_data, Y: y_data})
    print("\nHypothesis: ", h, "\nCorrect (Y): ", c, "\nAccuracy: ", a)
    npW = sess.run(W)
    npb = sess.run(b)
```

- 아무튼, 돌려보면, 아래처럼 잘 나오는 것을 알 수 있습니다. 

```
0 0.233398
2500 0.0560301
5000 0.0350374
7500 0.0260067
10000 0.0209273

Hypothesis:  [[ 0.06183419]
 [ 0.00194065]
 [ 0.03753087]
 ..., 
 [ 0.99990153]
 [ 0.99748284]
 [ 0.99286121]] 
Correct (Y):  [[ 0.]
 [ 0.]
 [ 0.]
 ..., 
 [ 1.]
 [ 1.]
 [ 1.]] 
Accuracy:  1.0
```

## 그림을 그려 봅시다. 

- 잘 분류해주는지 보고싶어요. 이를 직접 그림에서 decision boundary를 그려낼 수 있으면 더 좋을 것 같구요. 