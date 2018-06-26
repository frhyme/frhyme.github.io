---
title: 강화학습을 공부해봅시다. 1편 
category: machine-learning
tags: reinforcement-learning python python-lib 
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
- 저는 여기서, 간단한 미로? 의 게임을 사용합니다. 

## just do it. 

- 늘 그랬던 것처럼, 바로 시작하겠습니다. 
- 아래 코드는 그냥 바로 치고 시작하시는 게 좋습니다. 필요한 라이브러리들과, 몇 가지 상황을 세팅합니다. 
    - 만약, 이름이 중복된다고 하면 `id`를 변경해주시면 좋아요. 
    - 또한, `is_slippery`를 `False`로 변경하지 않으면, 방향키가 제대로 먹지 않습니다. 정확히 말을 하자면, 해당 게임은 얼음판 위에서 목적까지 도달하는 게임인데, 얼음판 위이기 때문에 자꾸 미끄러집니다. 이게 기본세팅이고, 이 세팅을 바꾸어야 좀 deterministic하게 게임을 할 수 있습니다. 

```python
import pandas as pd
import tensorflow as tf 
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

```python

```

## reference 

- <https://hunkim.github.io/ml/RL/rl02.pdf>

## raw code 

```python
```