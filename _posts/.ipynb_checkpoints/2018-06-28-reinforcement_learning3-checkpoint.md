---
title: 강화학습을 공부해봅시다. 3편 
category: machine-learning
tags: reinforcement-learning python python-lib gym matplotlib tensorflow

---

## 진짜 게임들에 적용하려면. 

- 우리는 좀전까지 Frozen world를 대상으로 강화학습을 수행했습니다. 그리고 Q(quality) table을 만들어서, 매 스텝이 reward에 얼마나 기여하는지를 측정했죠. 
- 이것이 가능했던 것은, `action_space`는 4이고, `observation_space`는 16(4 by 4)이기 때문입니다. 큐테이블이 16 by 4면 되니까요. 그래서 각 큐테이블에 값을 저장하고, 이를 확인하면서 움직이면 됩니다. reward에 따라서, Q-table을 계속 업데이트해나가구요. 
- 하지만, 바둑이나 오목의 예를 들어봅시다. `action_space`와 `observation_space`가 너무 많아집니다.
    - 간단하게, 바둑판을 4\*4로 두고, math.factorial(16)\*2로만 계산해도, 41845579776000의 값이 나옵니다. 표현되는 `observation_space`가 너무 많다는 생각이 듭니다. 
- 실제로 강화학습을 적용해야 하는 경우는 아주 많은 관찰 가지수와, 액션 스페이스로 구성되는데, 이를 큐테이블로 적용할 수는 없어요. 
- 그래요. 좋습니다. 그럼 이제 어떻게 해야 하는지 알려주시죠? 이럴때는 Approximation을 수행합니다. 이제 뉴럴넷을 이용하게 되구요. 

## Q-approximation 

- 아래 그림을 보면, 현재 state와 action을 input으로 받고, Q-value를 output으로 내뱉는 네트워크를 내뱉는 것을 알 수 있습니다. 
- 우리가 만들려고 하는 네트워크도 같아요. 일단은 Frozen-world에 적용합니다. 결국 X를 넣고, Y를 내뱉는 모델을 만드는데, 
    - input: X는 현재 state(one hot vector)
    - output: Y는 현재 state의 action별 Q-value

![](https://qph.fs.quoracdn.net/main-qimg-32471693b26503c8cd9a3129077d6d16)

### how to train

- 어떻게 학습하나요? 
    - 앞서 말한 바와 같이, X를 넣고, Y를 예측하는 모델을 만듭니다. state는 너무 명확한데, Y의 경우는 
        - terminal node인 경우: reward
        - non-terminal node인 경우: reward + decay_rate \* Q[new_state]
        - Q[new_state]는 우리가 만든 모델로 예측한 값입니다. 
- 또한, 이전에는 학습 데이터가 이미 완성되어 있었던 반면, 강화학습에서는 데이터가 매 에피소드마다 새롭게 생겨납니다. 즉, 한번에 한 데이터만 가지고 학습을 해야만 하죠. 그래서 epoch을 아주 크게 잡아야 합니다. batch_size는 1이 되겠죠. 
- 이렇게 fitting을 다 하고 나면, 이제 우리는 state만 집어넣으면, 개별 state의 action의 Q-value들을 예측해줍니다. 거기서 가장 Q-value가 높은 놈을 찾아서 저장해주면 되는 것이죠. 

- 사실 이 방식은 Q-table과 큰 차이가 있지는 않아요. weight 가 16 by 4로 큐테이블과 같은 크기를 잡아먹거든요. 
    - 물론 결과는 훨씬 잘 나옵니다. 
- 여기서는 이런 방식으로 뉴럴네트워크를 구성한다. 그거만 아시면 될 것 같습니다. 
    - 아마도, 이후에 좀 복잡한 게임을 모델링할 때는 컨볼루션이나 이것저것 들어가게 되지 않을까 싶어요. 
- 또한, 저도 명확하게 정리가 되어 있지는 않지만, 

> 값을 저장하는 것보다 weight(or coefficient)에 저장하는 것이 훨씬 효율적이다. 

- 는 것이 중요한 것 같아요. 메모리 사이즈도 같지만, 테이블보다는 뉴럴넷을 이용해서(물론 지금은 뉴럴넷이라기 보다 그냥 리니어 리그레션에 가깝긴 하지만), weight에 상황을 저장했더니 훨씬 잘 된다는 거죠. 이게 의미가 있는거라고 생각합니다. 


## do it. 

- 해봅시다. 


```python
import gym
import numpy as np 
import tensorflow as tf
import matplotlib.pyplot as plt

def one_hot(x):
    # x는 0-15 사이의 양수, 이 값을 one-hot vector로 변환 
    return np.identity(16)[x:x+1]
env = gym.make('FrozenLake-v0')
# X: observation Y: action 별 Quality 
input_size = env.observation_space.n
output_size = env.action_space.n

##
learning_rate, decay_rate, num_episodes= 0.1, 0.99, 30000

# X는 개별 상황, 즉 여기서는 16가지. 
X = tf.placeholder(shape=[1, input_size], dtype=tf.float32)
W = tf.Variable(tf.random_uniform([input_size, output_size], 0, 0.01))

Qpred = tf.matmul(X, W) # 우리가 예측하는, Q 
# Y는 개별 상황(X)에서 취할 수 있는 action의 quality를 예측 
Y = tf.placeholder(shape=[1, output_size], dtype=tf.float32)

loss = tf.reduce_sum(tf.square(Y - Qpred))
train = tf.train.GradientDescentOptimizer(learning_rate=learning_rate).minimize(loss)

rList = []
with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())
    for i in range(0, num_episodes):
        ### episode start
        state = env.reset()
        e = 1. / ((i/50)+10)
        rAll, done, local_loss = 0.0, False, []
        # q network training
        while not done:
            Qs = sess.run(Qpred, feed_dict={X: one_hot(state)})
            action = env.action_space.sample() if np.random.rand(1) < e else np.argmax(Qs)
            new_state, reward, done, _ = env.step(action)
            if done: # terminal 
                Qs[0, action] = reward
            else: # non-terminal 
                Qs[0, action] = reward + decay_rate*np.max(sess.run(Qpred, feed_dict={X:one_hot(new_state)}))
            sess.run(train, feed_dict={X: one_hot(state), Y: Qs})# training
            rAll += reward
            state = new_state
        ### episode end 
        rList.append(rAll)

plt.style.use(['dark_background'])

interval = 5000
mean_til_lst = [sum(rList[:i])/len(rList[:i]) for i in range(interval, len(rList))]
mean_interval_lst = [np.array(rList[i-interval:i]).mean() for i in range(interval, len(rList))]

plt.plot(range(0, len(mean_til_lst)), mean_til_lst, linewidth=1, label='mean_til')
plt.plot(range(0, len(mean_interval_lst)), mean_interval_lst, linewidth=1, label='mean_interval')

plt.grid(False)
plt.legend()
plt.savefig("../../assets/images/markdown_img/180628_reinforce_q_network_plot.svg")
plt.show()
```

- 그림을 보면, 전체 episode 중에서 65% 가 reward를 획득했고, 5000개씩 평균을 내보면, 나중에는 70%까지의 성공률을 보이는 것을 알 수 있다.

![](/assets/images/markdown_img/180628_reinforce_q_network_plot.svg)

## wrap-up

- epoch이 매우 크기는 하지만, 그래도 학습시간이 매우 많이 걸리는 것 같아요. 어떻게 하면 좀 더 빠르게 학습할 수 있도록 할 수 있나요. 
    - 지금은 batch_size가 1인데 이를 더 늘려서 한번에 학습(mini-batch)로 학습하는 것은 어떨까 싶은데, 문제는 
    - 사이즈가 달라질 수 있다는 거죠. 
- 그래서, 혹시나 싶어서 미니배치로도 해봤는데 별 차이가 없는것 같습니다...흠...

```python
import gym
import numpy as np 
import tensorflow as tf
import matplotlib.pyplot as plt

def one_hot(x):
    return np.identity(16)[x:x+1]

env = gym.make('FrozenLake-v0')
input_size = env.observation_space.n
output_size = env.action_space.n

learning_rate, decay_rate, num_episodes= 0.1, 0.99, 30000

X = tf.placeholder(shape=[None, input_size], dtype=tf.float32)
# X는 개별 상황, 즉 여기서는 16가지. 
W = tf.Variable(tf.random_uniform([input_size, output_size], 0, 0.01))

Qpred = tf.matmul(X, W) # 우리가 예측하는, Q 
Y = tf.placeholder(shape=[None, output_size], dtype=tf.float32)
# Y는 개별 상황(X)에서 취할 수 있는 action의 quality를 예측 

loss = tf.reduce_sum(tf.square(Y - Qpred))
train = tf.train.GradientDescentOptimizer(learning_rate=learning_rate).minimize(loss)

rList = []
with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())
    for i in range(0, num_episodes):
        ### episode start
        state = env.reset()
        e = 1. / ((i/50)+10)
        rAll, done, local_loss = 0.0, False, []
        # q network training
        X_batch = []
        Q_batch = []
        while not done:
            Qs = sess.run(Qpred, feed_dict={X: one_hot(state)})
            action = env.action_space.sample() if np.random.rand(1) < e else np.argmax(Qs)
            new_state, reward, done, _ = env.step(action)
            if done: # terminal 
                Qs[0, action] = reward
            else: # non-terminal 
                Qs[0, action] = reward + decay_rate*np.max(sess.run(Qpred, feed_dict={X:one_hot(new_state)}))
            X_batch.append(one_hot(state))
            Q_batch.append(Qs)
            rAll += reward
            state = new_state
        # mini batch training
        sess.run(train, feed_dict={X: np.array(X_batch).reshape(len(X_batch), 16), 
                                   Y: np.array(Q_batch).reshape(len(Q_batch), 4)})
        ### episode end 
        rList.append(rAll)
print(sum(rList)/len(rList))
```





## reference

- <https://hunkim.github.io/ml/RL/rl06.pdf>