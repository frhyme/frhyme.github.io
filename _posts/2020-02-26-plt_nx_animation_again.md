---
title: network의 변화과정을 plt.animation으로 영상으로 만들자.
category: python-libs
tags: python python-libs networkx matplotlib animation 
---

## 2-line summary. 

- `matplotlib.animation.FuncAnimation`를 사용해서 figure에 연속해서 그려지는 그림을 animation으로 표현하는 방법을 정리하였습니다. 
- `animation.FuncAnimation(fig=fig,func=func,frames=frames)`: `func`에 "그리는 방법"을 정의하고, `frames`로 매 그림마다 필요한 데이터는 iterator의 형식으로 넘겨줍니다.

## intro. 

- 예전에, matplotlib을 사용해서 만들어지는 그림들을 모아서 animation을 만들어주는 코드를 정리한 적이 있습니다. 하지만, 저도 여러분도 그렇듯, 우리는 망각의 동물이죠. 그래서 다시 공부하고 정리하기로 했습니다. 
- opencv를 이용하는 방법도 있지만, 생각보다 오류가 많이 나서, 제외하였습니다(그리고, 이 방법은 아예 매번 numpy.array로 이미지를 인식해서 처리해야 하기 때문에 시간도 매우 오래 걸리게 되죠.)
- 추가로, 이전에는 매번 figure를 변경하고 figure를 `np.array`로 변경하여, 전체 그림의 픽셀 단위에서 변경을 했던 반면, 이번에는 요소의 특성만 변경하는 식으로 훨씬 가볍게 처리하였습니다. 전에는 이해가 안되어서 저렇게 했던것 같은데 지금 보니, 왜 이걸 이해못했는지 모르겠네요.

## plt.animation 으로 그림 저장하기.

- 우선은, plt.animation이 무슨 짓을 하는지 집고 넘어갑시다. 
- 아래와 같이 간단한 코드가 있다고 하죠. 딱 보면 알겠지만, `fig`라는 도화지에 scatter plot을 그려주고, 보여주는 코드죠.

```python
import matplotlib.pyplot as plt 
fig = plt.figure() 
plt.scatter([1, 2, 3], [4, 5, 6])
plt.show() 
```

- `plt.animation`도 동일합니다. 단지, `fig`라는 도화지를 고정해두고, 매번 그림을 새롭게 그린다는 것이 다를 뿐이죠. 즉, "위에서 수행한 코드를 여러번 반복한다"라는 것만 다를 뿐이죠.
- [matplotlib.animation.FuncAnimation](https://matplotlib.org/3.1.3/api/_as_gen/matplotlib.animation.FuncAnimation.html)을 참고하면 다음과 같습니다. 세부적인 parameter가 더 있지만, 사실 `fig`, `func`, `frames` 이 세가지만 알면 끝납니다. 
    - `fig`: 그림을 그릴 도화지, 즉, 외부에서 선언해주면 됨. 
    - `func`: 그림을 반복해서 그릴 텐데, 이 "그리는 동작"을 선언해주는 부분이다. 보통 그림을 그리는 부분을 여기에 정의해주면 됨.
    - `frames`: 한장 한장 그릴 때마다, 필요한 데이터들, 따라서, len(frames)가 그려지는 그림의 수가 됨. generator를 넘겨도 상관없고, 순서대로 읽어들일 수 있는 iterable한, 아무거나 넘어오면 됨. 
- 대충 썼습니다.호호  호호. 코드로 보면 더 명확해요.


```python
import numpy as np 
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# fig: 반복해서 그려주는 도화지. 
fig = plt.figure() 
# frames: 매번 그림을 그릴때마다 넘어오는 값들.
frames = []
for i in range(0, 100): 
    x = np.random.random(100)
    y = np.random.random(100)
    frames.append((x, y))
# func: 그림을 그려주는 함수, 
# frames의 값이 순서대로 넘어옴.
def func(each_frame): 
    # each_frame: 만약 func 함수가 i번째 call 되었다면, 
    # frames[i]가 넘어옴.
    x, y = each_frame
    plt.scatter(x, y)

# 아래 코드를 실행하면 
# fig에 frames에 값에 맞춰서, func대로 그린 그림이
# my_animation에 저장됨.
my_animation = animation.FuncAnimation(fig=fig,
                                        func=func,
                                        frames=frames)
# 저장. 
writer = animation.writers['ffmpeg'](fps=25)
my_animation.save(f"test_animation.mp4", writer=writer, dpi=128)
```

- 즉, `func`가 제일 중요하죠. 하나하나의 그림을 어떻게 그릴지 `func`로 설계하고, 각 frame마다 필요한 데이터는 `frames`로 넘깁니다. 이게 다에요. 세부적인 파라미터는 필요할 때 그냥 쓰면 됩니다.
- 다만, 이 `func`를 어떻게 정의하느냐에 따라서 animation을 만들고 저장하는 속도가 판이하게 달라집니다.

### func: draw it all. 

- 우선, 가장 간단하게 매번 figure를 새로 그려주는 방식이 있습니다. 아래에서 보시는 것처럼, 그림을 매번 한장씩 그려주는 것이죠. 
- 다만, 이렇게 할 경우, 이전에 이미 `figure`에 그려져 있는 그림이 겹칠 수 있으므로 `plt.clf()`를 사용해서 기존에 그려진 그림을 지워주는 것이 필요합니다.

```python 
# initialize figure
fig = plt.figure()
pos = nx.shell_layout(G)

def animate_func_draw_all(each_frame):
    """
    매 frame마다 그림을 새로 그려주는 함수 
    """
    # 이미 그려진 figure를 clear
    plt.clf()
    selected_node = each_frame
    # 필요한 attribute를 정의하고
    node_color = ['red' if n == selected_node else 'white' for n in G]
    node_size = [1000 if n == selected_node else 100 for n in G]
    edge_color = ['red' if selected_node in e else 'black' for e in G.edges()]
    # 다시 그려줌.
    nx.draw_networkx(G,
                     pos=pos,
                     node_color=node_color,
                     node_size=node_size,
                     edge_color=edge_color)
```

### func: just attr update 

- 다만, 생각을 해보면 매번 그려주는 것이 좀 이상하다고 느껴지잖아요? 이미 그려진 부분들이 있는데, 왜 다 새로 그려줘야 하나? 라는 생각이 듭니다. 
- 따라서, 이미 그려진 요소들을 가져와서, 그 요소들의 attribute만 업데이트해주는 식으로 처리해도 됩니다.
- 다만, 이 경우에는 미리 figure내의 요소들을 외부에서 정의하여 가져와야 합니다. 대상이 되는 figure내의 객체가 무엇인지 이미 알고 있어야, `func`내에서 변경해줄 수 있는 것이죠.

#### matplotlib.collections.PathCollection

- figure 내에 그려지는 모든 것들은 각각 객체입니다. network를 그렸을 때, node, edge 모두 각각 object로 존재하죠. 
- 그리고, matplotlib은 관리의 용이성을 위해서, 동일한 특성을 가지는 object들은 하나의 container에 넣어서 관리합니다. 
- node, edge는 모두 같은 종류 객체이므로, 각각, `matplotlib.collections.PathCollection`, `matplotlib.collection.LineCollection`에 담겨서 figure에 표현됩니다.
- 그리고 이 둘은 각각 `nx.draw_networkx_nodes(G, pos=pos)`, `nx.draw_networkx_edges(G, pos=pos)`의 리턴값이죠. 
- 따라서, 매번 그림을 아예 새롭게 그릴 필요 없이, 가령 node의 특성을 변경하는 것이 필요하다면, node의 collection의 특성 값만 바꿔주면 되는 것이죠.

```python 
# NodeCollection: `matplotlib.collections.PathCollection`
NodeCollection = nx.draw_networkx_nodes(G, pos=pos)
# EdgeCollection: `matplotlib.collections.LineCollection`
EdgeCollection = nx.draw_networkx_edges(G, pos=pos)
```

- 혹은, 그냥 아래처럼 함수 내부에서 처리할 수도 있습니다. 

```
NodeCollection = plt.gca().collections[0]
EdgeCollection = plt.gca().collections[1]
```

#### code 

- 이를 코드로 정리하면 아래와 같습니다. 
- `func`에서는 현재 figure의 axis에서 `NodeCollection`, `EdgeCollection`을 찾아서, 각 요소의 attribute만 업데이트.

```python 

# initialize figure
fig = plt.figure()
pos = nx.shell_layout(G)

#******************************************************
# nx.draw_networkx_nodes(G, pos=pos) : 
# `matplotlib.collections.PathCollection`를 리턴함. 
# 이름이 `path`라서 헷갈릴 수 있지만, scatter plot에서 그려지는 점과 동일한 class 
# 관리의 용이성을 위해 `collections`으로 합쳐져 있으며, 
# 따라서, 모든 node의 attribute를 method를 통해 업데이트할 수 있음.
node_collection = nx.draw_networkx_nodes(G, pos=pos)
#-------------------------------------------------------
# nx.draw_networkx_edges(G, pos=pos) : 
# `matplotlib.collections.LineCollection`를 리턴함. 
# 관리의 용이성을 위해 해당 함수를 통해 그려진 figure내의 edge는 
# 모두 `collections`으로 합쳐져 있으며, 
# 따라서, 모든 edge의 attribute를 method를 통해 업데이트할 수 있음.
edge_collection = nx.draw_networkx_edges(G, pos=pos)
#******************************************************

def animate_func_set_attr(each_frame):
    """
    매 frame마다 요소의 attribute만 업데이트해주는 경우
    """
    selected_node = each_frame
    # 필요한 요소들을 찾아주고.
    NodeCollection = plt.gca().collections[0]
    EdgeCollection = plt.gca().collections[1].
    # draw nodes
    node_color = ['red' if n == selected_node else 'white' for n in G]
    node_size = [1000 if n == selected_node else 100 for n in G]
    # node attr upate
    NodeCollection.set_color(node_color)
    NodeCollection.set_sizes(node_size)
    # edges attr update
    edge_color = ['red' if selected_node in e else 'black' for e in G.edges()]
    EdgeCollection.set_color(edge_color)
```

### performance check.

- 성능 비교를 위해 다음의 코드를 실행해본 결과 
    - `animate_func_draw_all`: 11.5 second
    - `animate_func_set_attr`:  4.5 second
- 따라서, 가능하다면 `animate_func_set_attr`을 사용하는 것이 훨씬 빠릅니다.

```python 
frame_n = 100
frames = np.random.choice(len(G), frame_n, replace=True)
interval = 200
dpi = 128

writer = animation.writers['ffmpeg'](fps=25)

print("== draw all")
start_time = time.time()
my_animation = animation.FuncAnimation(fig,
                                           animate_func_draw_all,
                                           frames=frames,
                                           interval=interval)


my_animation.save("test_animation_draw_all.mp4", writer=writer, dpi=dpi)
print(time.time() - start_time)
############################################################
print("== set attr")
start_time = time.time()
my_animation = animation.FuncAnimation(
    fig,
    animate_func_set_attr,
    frames=frames,
    interval=interval
)
my_animation.save("test_animation_set_attr.mp4", writer=writer, dpi=dpi)
print(time.time() - start_time)

```

## wrap 

- `figure`내에 그려지는 요소들은 모두 객체이며, networkx에서 그림을 그리면 node는 `PathCollection`이라는 클래스로, edgesms `LineCollection`의 타입으로 구현된다는 것을 배웠죠. 
- 막연하게, `networkx`가 그림을 그릴 때, `matplotlib`를 참고하고 있다는 것을 막연하게는 알고 있었는데, 이제 좀 더 정확하게 알게 된 것 같습니다. 
- 뿐만 아니라, animation을 사용할 때, `func`에서 매번 새로 그림을 그려줄 필요 없이, 특정한 값만 업데이트하는 것이 훨씬 빠르다, 라는 교훈을 얻었죠. 

## reference

- [networkx.drawing.nx_pylab.draw_networkx_nodes](https://networkx.github.io/documentation/networkx-1.10/reference/generated/networkx.drawing.nx_pylab.draw_networkx_nodes.html)
- [networkx.drawing.nx_pylab.draw_networkx_edges](https://networkx.github.io/documentation/networkx-1.10/reference/generated/networkx.drawing.nx_pylab.draw_networkx_edges.html)




## raw-code 

```python
import time
import networkx as nx
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation


"""
set attr이 훨씬 빠를 줄 알았는데, 그냥 그리는 거랑 거의 차이가 없음.
"""

n = 10
G = nx.complete_graph(n)

# initialize figure
fig = plt.figure()
pos = nx.shell_layout(G)
# 필요한 요소를 이미 외부에서 저장해줌.
#NodeCollection = nx.draw_networkx_nodes(G, pos=pos)
#EdgeCollection = nx.draw_networkx_edges(G, pos=pos)

def animate_func_draw_all(each_frame):
    """
    매 frame마다 그림을 새로 그려주는 함수 
    """
    # 이미 그려진 figure를 clear
    plt.clf()
    selected_node = each_frame
    # 필요한 attribute를 정의하고
    node_color = ['red' if n == selected_node else 'white' for n in G]
    node_size = [1000 if n == selected_node else 100 for n in G]
    edge_color = ['red' if selected_node in e else 'black' for e in G.edges()]
    # 다시 그려줌.
    nx.draw_networkx(G,
                     pos=pos,
                     node_color=node_color,
                     node_size=node_size,
                     edge_color=edge_color)


def animate_func_set_attr(each_frame):
    """
    매 frame마다 요소의 attribute만 업데이트해주는 경우
    """
    NodeCollection = plt.gca().collections[0]
    EdgeCollection = plt.gca().collections[1]
    # 요소의 정보만 업데이트함.
    selected_node = each_frame
    # draw nodes
    node_color = ['red' if n == selected_node else 'white' for n in G]
    node_size = [1000 if n == selected_node else 100 for n in G]
    # node attr upate
    NodeCollection.set_color(node_color)
    NodeCollection.set_sizes(node_size)
    # edges attr update
    edge_color = ['red' if selected_node in e else 'black' for e in G.edges()]
    EdgeCollection.set_color(edge_color)


# frames: 각 frame(한장의 image)마다 필요한 데이터들.
# 즉 첫번째 image에는 frames[0]의 데이터가 넘어가고,
# 두번째 image에는 frames[1]의 데이터가 넘어감.



############################################################
frame_n = 100
frames = np.random.choice(len(G), frame_n, replace=True)
interval = 200
dpi = 128

writer = animation.writers['ffmpeg'](fps=25)

print("== draw all")
start_time = time.time()
my_animation = animation.FuncAnimation(fig,
                                           animate_func_draw_all,
                                           frames=frames,
                                           interval=interval)


my_animation.save("test_animation_draw_all.mp4", writer=writer, dpi=dpi)
print(time.time() - start_time)
############################################################
print("== set attr")
start_time = time.time()
my_animation = animation.FuncAnimation(
    fig,
    animate_func_set_attr,
    frames=frames,
    interval=interval
)
my_animation.save("test_animation_set_attr.mp4", writer=writer, dpi=dpi)
print(time.time() - start_time)

```