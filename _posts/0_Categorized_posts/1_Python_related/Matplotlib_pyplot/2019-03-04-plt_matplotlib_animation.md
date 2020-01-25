---
title: matplotlib로 만든 그림 animation으로 만들기 
category: python-libs
tags: python python-libs matplotlib animation blit 
---

## python으로 animation을 만들려구요. 

- 저는 보통 그림을 matplotlib를 사용해서 그립니다. 많이 만들어서, 그리고 만들 수 있는 것들이 많아서 유용합니다. 
- 다만, 시뮬레이션이 수행되는 부분을 animation으로 처리할 수 없을까를 고민하다가 보니까, 찾아보니 가능한 것 같기는 해요. 
- 서론이 길 필요 없이, 바로 해보도록 합니다. 

## do it.

- 코드는 다음과 같습니다. 
    - `update`라는 함수에서 새로 그림을 그려주는 식으로 진행된다고 보면 됩니다. 
    - 그리고, 그 결과들이 `FuncAnimation`에 넘어가는데, 이때 `frames`는 그냥 각 frame별로 넘어가는 값들이라고 생각하면 되요. 예를 들어서, 아래 코드에서는 `frames`에 128이 들어있는데, 0부터 127까지 순차적으로 값이 `update` 함수에 넘어가는 것이죠.
    - 또 `FuncAnimation`에서 argument중 blit가 False인것이 중요합니다. 만약 True일 경우에는 `update` 함수에서 값이 매번 artist object를 넘겨줘야 합니다. 
        - `FuncAnimation`: Makes an animation by repeatedly calling a function func.

```python
@app.route('/matplot')
def mat_video():
    from matplotlib.animation import FuncAnimation
    from IPython.display import HTML # jupyter notebook에서 테스트할 때. 

    # set figure and axes 
    f, ax = plt.subplots(figsize=(12, 6))

    # data 
    x = np.linspace(0, 2*np.pi, 128)
    y = np.sin(x)

    def update(frame):
        """
        - frames에 따라서 매번 업데이트로 그림을 그려줌. 
        - frame은 FuncAnimation의 frame argument에 있는 값이 넘어가는 부분. 
        """
        ax.clear() # 일단 지금 그려진 부분을 다 지우고, 
        ax.set_xlim(0, 2*np.pi), ax.set_ylim(-2, 2)
        # 여기서처럼 그림을 새로 그려주면 됨. 
        plt.plot(x[:frame], y[:frame], 'ro-', 20)
    """
    - 아래 argument에서 blit가 False인 것이 중요합니다. 
    - True일 경우에는 update function에서 artist object를 넘겨줘야 합니다. 예를 들면 Line 같은 것들. 
    """
    ani = FuncAnimation(
        fig=f, func=update,
        frames=128, 
        blit=False, 
        )
    #HTML(ani.to_jshtml()) # jupyter notebook에서 사용할 때. 
    return ani.to_jshtml() # java script, html로 변환하여 넘겨줌 
```

## draw network 

- 마찬가지로 network도 그릴 수 있습니다. 여기서도 마찬가지로 blit가 False로 되어 있어야 하죠. 

```python
import numpy as np
import networkx as nx 
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from IPython.display import HTML

# set figure and axes 
f, ax = plt.subplots(figsize=(12, 4))
#plt.axis('off')


# data 

G = nx.karate_club_graph()

def update(frame):
    ax.clear()
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    pos = nx.random_layout(G)
    nx.draw_networkx(G, pos=pos)

ani = FuncAnimation(fig=f, 
                    func=update, 
                    frames=128,
                    blit=False,
                   )
HTML(ani.to_jshtml())    

```

## what is blit??

- blit를 False로 하느냐, True로 하느냐에 따라서 update function에 넣는 값이 달라지게 됩니다. 
- matplotlib에서 blit의 정의는 다음처럼 되어 있죠. 

> Controls whether blitting is used to optimize drawing. Note: when using blitting any animated artists will be drawn according to their zorder. However, they will be drawn on top of any previous artists, regardless of their zorder. Defaults to False.

- 즉, 그림을 그릴 때, 일종의 최적화 작업을 수행하기위해서 설정해주는 값이라고 생각하면 됩니다. 
- 위키피아의 정의에 따르면, bit block transfer라고 합니다. 의미적으로는 빈 공간만 채워줄 수 있도록 데이터를 통신하는 것이라고 하는데, 아무튼 뭐 비슷한 의미니까 대충 알고 넘어가겠습니다. 
- 애니메이션을 만들때, 특히 지금처럼 그림을 그릴때는 axis나 background 등은 변하지 않고, line, network만 변하게 됩니다. 즉, 매번 모든 것을 새롭게 그려줄 필요 없이, 필요한 부분만 그려주도록 세팅을 한다면, 애니메이션을 만들 때 소요되는 시간이 훨씬 단축될 수 있겠죠. 
- 저는, 편하게 하려고 그냥 매번 새로운 그림을 그려주었지만, 그렇게 그리지 않고 필요한 요소만 그려준다면 훨씬 편하게 그릴 수 있을 것 같기는 해요. 

## wrap-up

- 단, 현재도 만들어진 애니메이션을 javascript와 html로 바꾸어 줄 때는 아주 많은 시간이 소요됩니다. 지금의 목적으로는 좀더 빠르게 애니메이션이 될 수 있도록 만들고 싶은데 matplotlib를 변환하는 방식으로는 너무...너무 오래 걸려서 고민하고 있습니다. 아무래도 javascript로 직접 사용해야 할 것 같습니다. 



## reference

- <https://alexgude.com/blog/matplotlib-blitting-supernova/>