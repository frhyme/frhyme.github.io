---
title: 강화학습을 공부해봅시다. 2편 
category: machine-learning
tags: reinforcement-learning python python-lib gym matplotlib numpy sns heatmap learning-rate

---

## reinforcement learning - stochastic world: FrozenLake-v0

- 이제, stochastic world에서 학습해봅시다. 얼음판에서는 미끄러지기 때문에, 제가 가라는 대로 잘 가지 않아요. 그래서, 이전에는 일단, 간단하게 deterministic world에서 수행하기 위해서 `is_slippery`를 `False`로 만들고 진행했습니다. 코드는 아래와 같았구요. 

```python
import gym
from gym.envs.registration import register
"""
- 새로운 게임 형식을 만들어줌.
"""
register(
    id='FrozenLakeNotSlippery-v1',
    entry_point='gym.envs.toy_text:FrozenLakeEnv',
    kwargs={'map_name' : '4x4', 'is_slippery': False},
)
```

- 그런데, 말 그대로 FrozenLake 이므로, 미끄러지는 상황에서도 잘 학습되는지 궁금합니다. 이를 개선하기 위해서는 `learning_rate`라는 개념을 집어넣습니다. 
- 학습될 때, 학습을 그대로 다 하는 것이아니라, 반영비율을 줄여서, 일정 부분만 학습을 하게 되는 것이죠. 이렇게 하면, 만약 잘못 학습된 아이가 있더라도, 충분히 그 문제점을 개선할 수 있지 않을까? 하는 것이 `learning_rate`의 목적입니다. 

### slipperly_rate

- 우선, 그전에 얼마나 잘 미끄러지는지 확인해보겠습니다. 

```python
### how to get is_slippery prob??
env = gym.make("FrozenLake-v0")
is_slippery_lst = []
for i in range(0, 10000):
    env.reset()
    new_state, reward, done, _ = env.step(2)
    if new_state==1:
        is_slippery_lst.append(False)
    else:
        is_slippery_lst.append(True)
    #env.render()
print("slippery rate: {}".format(np.array(is_slippery_lst, dtype=int).mean()))
```

- 0.6의 확률로 미끄러지는군요. 너무 심하지 않나....싶은데...아무튼 뭐 그렇다고 하니 일단 넘어가겠습니다. 

```
slippery rate: 0.6708
```

### Q with learning rate

- 원래 코드는 다음과 같았습니다. 
- Q_state에 action을 통해 발생한 reward를 그대로 반영해주고, Q_newState의 값을 decay해서 반영해주죠. 

```python
Q[state, action] = reward + decay_rate*np.max(Q[new_state, :])
```

- 바뀐 코드는 다음과 같습니다. 
- 현재의 Q값을 100%의 비율 중에서 일정 비율(learning_rate)을 제외한 양만큼만 남겨주고 
- 새롭게 발생한 값(reward, Q_newState의 값)을 learning_rate만큼 더해서 넣어줍니다. 
    - learning rate가 크다면?: 액션의 결과가 빠르게 반영
    - learning rate가 작다면?: 액션의 결과보다는 기존 값을 더 많이 반영

```python
Q[state, action] = (1-learning_rate)*Q[state, action] 
Q[state, action] += learning_rate*(reward + decay_rate*np.max(Q[new_state, :]))
```

- 앞서 본 것처럼, 현재 slippery_rate는 0.66으로 매우 높습니다. 즉, 원하는 액션이 제대로 반영되지 않을 가능성이 높다는 것이죠. 
    - learning_rate를 낮게 둘 경우: 초기에 잘못된 Q값이 세팅되었을때(예를 들어, Action: 아래쪽, 실제 Action: 오른쪽, reward: 1.0), 계속 그 방향으로 세팅되기 쉽습니다. 초기의 오류를 고치기가 쉽지 않다는 것이죠. 
    - learning_rate를 높게 둘 경우: 현재 action에 따라서 지나치게 바뀌기 쉽습니다. 들쑥날쑥하기 쉽죠. 
- 아무튼,...이게 다 말 뿐인것 같은데, grid로 그려서 한번 비교해보는 게 좋을 것 같아요. 

### score with grid 

- Q update를 바꾸고, `learning rate`, `num_episode`에 따라서 score(episode중에서 reward를 획득한 비율)가 어떻게 달라지는지를 간단히 heatmap으로 그려보았습니다. 
- 생각보다, score가 높지는 않습니다. 제가 참고한 김성훈 교수님의 피피티에서는 0.635까지도 나왔다는 것 같은데, 저는 그정도는 나오지 않네요. 물론, 간혹 나오는 경우도 있습니다만. 

```python
import seaborn as sns 

def make_rlist_grid(lrs=[], num_eps=[]):
    """
    learning rate, num_episode 에 따라서, 시행한 결과값을 nested dictionary에 넣어줌
    - 
    """
    r_dict = {lr:{ep: [] for ep in num_eps} for lr in lrs}
    env = gym.make("FrozenLake-v0")
    Q = np.zeros([env.observation_space.n, env.action_space.n])
    
    decay_rate = 0.99 
    for lr in lrs:
        for ep in num_eps:
            for i in range(0, ep):
                state = env.reset()
                rAll = 0 # 한 episode 별로 얻을 수 있는 reward의 총합
                done = False # hole에 빠지거나, Goal에 도달하면 True
                while not done:
                    action = np.argmax(Q[state, :] + np.random.normal(0, 1, env.action_space.n)/(i+1))
                    new_state, reward, done, _ = env.step(action)
                    Q[state, action] = (1-lr)*Q[state, action] 
                    Q[state, action] += lr*(reward + decay_rate*np.max(Q[new_state, :]))
                    rAll+=reward
                    state = new_state # state update
                r_dict[lr][ep].append(rAll)
    return r_dict
lrs = [0.1, 0.4, 0.6, 0.8, 0.85, 0.9]
num_eps = [1000, 5000, 8000, 10000, 15000]

rlist_grid = make_rlist_grid(lrs=lrs, num_eps=num_eps)
rlist_grid_score = {lr: {ep: sum(rlist_grid[lr][ep])/len(rlist_grid[lr][ep]) 
                         for ep in rlist_grid[lr].keys()} for lr in rlist_grid.keys() }

plt.figure(figsize=(12, 8))
sns.heatmap(pd.DataFrame(rlist_grid_score), 
            annot=True, fmt=".3f",
            cmap=plt.cm.Blues, cbar=True,
            linewidths=3)
plt.tick_params(labelsize=13)
plt.savefig('../../assets/images/markdown_img/180627_reinforcement_lr_ep_heatmap.svg')
plt.show()
```

![](/assets/images/markdown_img/180627_reinforcement_lr_ep_heatmap.svg)


## wrap-up 

- 흠, 대략 저정도에서 가장 좋은 score가 된다는 건 일단 알겠는데, 왜죠? 어떻게 이걸 미리 알 수 있나요? grid로 마구잡이로 돌리는 건 좀 무식한 방법인것 같은데 흠. 어떻게 hyperparameter를 잘 세팅할 수 있을까요? 우리가 이미 알고 있는 `slippery_rate`로 값을 근사하게 세팅할 수는 없을까요? 라는 생각은 드네요. 

## reference

- <https://hunkim.github.io/ml/RL/rl-l05.pdf>