---
title: 강화학습을 공부해봅시다. 1편 
category: machine-learning
tags: reinforcement-learning python python-lib gym matplotlib deterministic numpy
---

## 강화학습이란 무엇인가. 

- 우선, 이 포스트는 [김성훈 교수님의 강의](https://hunkim.github.io/ml/RL/rl02.pdf) 중 lecture 1-4까지를 공부하고 정리한 내용입니다. 
- 강화학습은 간단히 말해서, 바둑, 오목, 미로 찾기 등에서 가장 효율적인 action 순서를 찾는 트레이닝 방법이라고 말할 수 있을 것 같습니다. 
- 어떤 action을 수행했을 때, 그 action으로 인해 reward가 발생한다면, 그 방향으로 feedback을 줍니다. reward가 발생되면, reward가 발생하는 방향으로 action을 반복 수행할 수 있도록 학습이 되겠죠. 
    - 오목에 적용을 해보면, 어떤 point에 돌을 두지 않으면 penalty가 발생하게 되죠(사실 reward와 penalty는 한 끗 차이라고 생각합니다). 그렇다면 다음 게임에는 해당 point에 돌을 두도록 학습을 시키는 것을 말합니다. 
- 이를 위해서는 다음과 같은 것들이 정의되어야 합니다. 
    - Context understanding: 현재 상황을 인지하는 것(오목 판 위의 돌 배치 등)
    - Action: 개별 상황에서 내가 취할 수 있는 액션 set(오목의 경우, 놓을 수 있는 돌의 위치, 미로찾기의 경우 방향키)
        - 동시에, 현재 상황을 이해한 상태에서, 어떤 action을 수행하는 것이 가장 적합한지를 찾는 알고리즘을 찾는 것 도 중요하겠죠. 
    - Reward: 포상을 어떻게 모델링할 것인가? 
        - 보통 게임에서는 reward가 win/lose 라는 하나의 지표로 주어집니다. 오목에서 승리로 가는 과정에는 수없이 많은 수순들이 있는데, 그 중에서 어떤 돌이 reward에 가장 큰 영향을 주었는가? 를 어떻게 알 수 있을까요?
        - 결국 reward를 쪼개서 어떤 수순이 가장 중요한 역할을 했는지 찾는 것이 또 중요하다고 할 수 있습니다. 
- 아무튼, 일단은 대략 이렇고요. 말이 길었으니 직접 하면서 해보도록 하겠습니다. 

## open AI gym

- open AI gym 이라는 것이 있습니다. 설명은 대략 다음과 같은데요 

> Gym is a toolkit for developing and comparing reinforcement learning algorithms. It supports teaching agents everything from walking to playing games like Pong or Pinball.

- reinforcement leanring을 적용할 수 있는 다양한 모델(아타리, 퐁, 미로 등)을 제공합니다. 다시 말하면, context, action, reward 를 모두 제공한다고 할 수 있겠죠. 
- 저는 여기서, 간단한 미로? 의 게임을 사용합니다(당연히 open AI gym에 있는 게임입니다)

## just do it. 

- 늘 그랬던 것처럼, 바로 시작하겠습니다. 
- 아래 코드는 그냥 바로 치고 시작하시는 게 좋습니다. 필요한 라이브러리들과, 몇 가지 상황을 세팅합니다. 
    - 만약, 이름이 중복된다고 하면 `id`를 변경해주시면 좋아요. 
    - 또한, `is_slippery`를 `False`로 변경하지 않으면, 방향키가 제대로 먹지 않습니다. 정확히 말을 하자면, 해당 게임은 얼음판 위에서 목적까지 도달하는 게임인데, 얼음판 위이기 때문에 자꾸 미끄러집니다. 이게 기본세팅이고, 이 세팅을 바꾸어야 좀 deterministic하게 게임을 할 수 있습니다. 
    - 나중에는 non-deterministic한 상황에서도 학습을 진행합니다. 

```python
import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt
import gym
from gym.envs.registration import register

# 아래의 방식을 통해 게임을 등록함. 특히 is_slippery는 매우 중요함. 
"""
- 새로운 게임 형식을 만들어줌.
"""
register(
    id='FrozenLakeNotSlippery-v1',
    entry_point='gym.envs.toy_text:FrozenLakeEnv',
    kwargs={'map_name' : '4x4', 'is_slippery': False},
)
```

### play game

- 일단, 게임을 해보겠습니다. 이 게임 판에는 Start, Frozen, Hole, Goal 이라는 세 가지 종류의 판들이 있는데, Start부터 Goal까지 잘 도착하는 것이 목적입니다. Hole에 빠지면 죽습니다. 
- 아무튼, 딱 눈으로 보면 사실 길은 보입니다. 오른쪽오른쪽, 아래아래아래, 오른쪽 으로 가면 도착하죠. 
- 그렇게 하면 잘 도착하는지 보겠습니다. 

```
SFFF
FHFH
FFFH
HFFG
```

- 그래서, 게임을 진행해봅니다. 제가 정의한 `complete_actions`에 따라서 제 말이 움직이게 되죠. 

```python
env = gym.make("FrozenLakeNotSlippery-v1")
env.reset()
"""
0: left, 1: down, 2: right, 3: up 
"""
complete_actions = [2, 2, 1, 1, 1, 2]
for action in complete_actions:
    #action = env.action_space.sample() # randomly select action 
    """
    - new_state: 액션을 취해서 새롭게 옮겨진 위치 
    - reward: 보상을 얻었는지 여부
    - done: 게임이 끝났는지 여부(hole에 빠지거나, )
    """
    new_state, reward, done, _ = env.step(action)# action을 적용하고 업데이트
    env.render() #현재 상황을 보여줌
    if done is True:
        print("done, reward: {}".format(reward))
```

- 결과는 다음과 같습니다. 실제로 쥬피터 노트북에서 위 코드를 실행하면, 현재 말이 어디있는지도 잘 보여줍니다만, 여기서는 텍스트만 있다보니, 아무래도 부족한 부분이 있군요. 

```
  (Right)
SFFF
FHFH
FFFH
HFFG
  (Right)
SFFF
FHFH
FFFH
HFFG
  (Down)
SFFF
FHFH
FFFH
HFFG
  (Down)
SFFF
FHFH
FFFH
HFFG
  (Down)
SFFF
FHFH
FFFH
HFFG
  (Right)
SFFF
FHFH
FFFH
HFFG
done, reward: 1.0
```

### Q learning algorithm 

- 그럼, AI는 어떻게 가장 좋은 path를 찾을 수 있을까요? 
    - 일단은 마구잡이로 막 돌아다닙니다. 알아서 막 움직입니다. 우리는 라이프가 많으므로 죽어도 또 하면 됩니다. 
    - 그러다가 G에 도달했다고 합시다. G에 도달하면 Reward가 발생하게 됩니다. 그렇다면 이 아이는 G에 도달하기 직전 위치를 기억해야 겠죠(여기를 G-1이라고 해봅시다). 
    - 그럼, 목적은 G-1으로 바뀌게 됩니다. G-1에 도달해도, reward가 발생하도록 세팅합니다. 
    - 다시 막 돌아다니다가, 이제 G-1에 도달했습니다. 그렇다면 다시 G-1에 도달하기 이전에 어디서 도착했는지를 기억해야 겠죠. 이를 G-2라고 합시다. 
    - 이렇게 반복하다보면, G-n이 start가 되는 지점이 발생합니다. 
- 이제 우리는 start에서 리워드를 얻으려면 어디로 가야하는지 알아요. 그리고 그 다음 위치에서도 어디로 가야 리워드를 얻는지 알게 되었구요. 자, 이게 사실 Q-learning algorithm입니다. 아주 간단한 알고리즘이죠. 

- 하지만, 문제가 발생합니다. 
    - 길이 여러 가지라면 더 짧은 길을 사용하도록 세팅해야겠죠. 
    - 하지만, 현재는 reward가 한번 전달되고 나면, 그 길이 고정되고, 다른 길로 진행되지 않습니다. 

- 따라서, 몇 가지를 추가하게 되는데요. 
    - 우선, reward가 앞으로 전달될수록 decay되도록 합니다.
    - 랜덤하게 계속 가보지 않은 길로 간다. 

```python
"""
- 사실 이런 형태의 미로에서는 reward를 끝나봐야 얻습니다. 끝날때까지 reward가 어디있는지 모른다는 이야기죠. 
- 비슷하게, 장기 바둑도 마찬가지입니다. 이전의 어떤 수가 reward를 결정했는지는 알기가 어려우니까요.
- 아무튼, 그러므로, dummy Q-learning algorithm에서는 t+1 state의 reward의 max값을 t state의 reward의 max 값으로 정합니다. 
    - 미래의 리워드를 현재의 리워드로 가져온다는 말이 이상하지만, 이걸 정리하면, "이번 게임에서 t+1 스텝
"""
env = gym.make("FrozenLakeNotSlippery-v1")
observation = env.reset()

"""
- Q는 개별 observation(현재 말의 위치)와 해당 obs에서 취할 수 있는 action별로 이득이 표현된 테이블입니다. 
- 뒤쪽에서 다시 설명되겠지만, 게임이 종료되었을 때 얻을 수 있는 reward가 앞으로 전달되어, 각 값을 업데이트해줍니다. 
"""
Q = np.zeros([env.observation_space.n, env.action_space.n])

num_episodes = 800 # 일종의 epoch, 혹은 라이프.
decay_rate = 0.99 
# reward는 전달 과정에서 누가 계속 까먹기 때문에, decay rate가 발생함. 
# 사실 맨 끝에서 얻은 Reward가 앞가지 전달되는데 아무런 변화가 없어야 한다는 것도, 직관적으로 이상하지 않나요? 
# 또한, 이렇게 모델링 해야, 짧은 path를 거쳐 지나온 놈의 경우에 step에서 높은 Q(partial reward)를 가짐 

rlist = []
for i in range(0, num_episodes):
    state = env.reset()
    e = 1. / ((i//100)+1)
    """
    goal에 이르는 답이 여러가지일 수 있는데, 어느 정도의 랜덤성을 통해서 탐험을 하지 않을 경우, 초기의 답만을 가지게 됨. 
    사실 미로의 경우는 탐험을 통해 더 짧은 길을 찾을 수도 있습니다. 
    따라서, 여기서는 이미, 최적의 path를 찾았다고 해도 다시 더 좋은 path를 찾을 수 있도록 exploration을 보장합니다. 
    """
    #env.render()
    rAll = 0 # 한 episode 별로 얻을 수 있는 reward의 총합
    done = False # hole에 빠지거나, Goal에 도달하면 True
    while not done:
        if np.random.randn(1) < e: # 탐험을 통해 더 좋은 길을 확보
            # np.random.randn 은 norm(0, 1)
            # 즉, 에피소드가 반복되어 e가 감소되어도, 대략 0.5 정도의 확률로 탐험을 하는 것이 가능해야 함. 
            action = env.action_space.sample()
        else:
            action = np.argmax(Q[state, :])
        new_state, reward, done, _ = env.step(action)
        # 다음 단계로 가서 리워드를 얻는 다면, 이전단계까지 잘 온 것이므로 이전 단계에도 리워드를 준다. 
        Q[state, action] = reward + decay_rate*np.max(Q[new_state, :])
        rAll+=reward
        state = new_state # state update
    rlist.append(rAll)
print('complete')

"""
- 처음에는 잘 못 맞추다가, 한 두번 맞추기 시작하면서 부터는 슥슥 매우 잘 맞춤
- 그냥 random으로 시행할 경우에는, 1.3%의 확률로 reward 획득
"""
plt.figure(figsize=(12, 2))
plt.scatter(range(0, len(rlist)), rlist, marker='^', s=1, color='red')
plt.savefig('../../assets/images/markdown_img/180625_reinforcement_base.svg')
plt.show()

"""
0: left, 1: down, 2: right, 3: up 
"""
#print(Q)
Q_df = pd.DataFrame(Q, index = [(i//4, i%4) for i in range(0, Q.shape[0])], 
                    columns=['left', 'down', 'right', 'up'])
print(Q_df)



```

- 아래 그림에서 보는 것처럼, 처음에는 잘 맞추지 못하다가 나중에는 잘 맞추기 시작합니다. 이후에도 계속 reward가 0인 경우가 있는 것은, 계속 탐험을 하기 때문에, reward가 0인 경우가 발생하는 것이죠. 

![](/assets/images/markdown_img/180625_reinforcement_base.svg)


```
            left      down     right        up
(0, 0)  0.941480  0.950990  0.950990  0.941480
(0, 1)  0.941480  0.000000  0.960596  0.950990
(0, 2)  0.950990  0.970299  0.950990  0.960596
(0, 3)  0.960596  0.000000  0.950990  0.950990
(1, 0)  0.950990  0.960596  0.000000  0.941480
(1, 1)  0.000000  0.000000  0.000000  0.000000
(1, 2)  0.000000  0.980100  0.000000  0.960596
(1, 3)  0.000000  0.000000  0.000000  0.000000
(2, 0)  0.960596  0.000000  0.970299  0.950990
(2, 1)  0.960596  0.980100  0.980100  0.000000
(2, 2)  0.970299  0.990000  0.000000  0.970299
(2, 3)  0.000000  0.000000  0.000000  0.000000
(3, 0)  0.000000  0.000000  0.000000  0.000000
(3, 1)  0.000000  0.980100  0.990000  0.970299
(3, 2)  0.980100  0.990000  1.000000  0.980100
(3, 3)  0.000000  0.000000  0.000000  0.000000
```
## wrap-up

- 매번 포스트가 약간 쓸데없이 길어지는 것 같아서, 일단 여기서 마무리하려고 합니다. 
- 이제 `is_slippery`를 `False`에서 `True`로 바꾸고, stochastic world에서 어떤 변화가 발생하는지를 보려고 합니다. 

## reference 

- <https://hunkim.github.io/ml/RL/rl02.pdf>

## raw code 

```python
```