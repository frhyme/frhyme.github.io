---
title: 네트워크 변화 비디오로 만들기 
category: python-lib
tags: networx python python-lib matplotlib image video numpy 
---

## 그래프의 변화를 video로 보려고 합니다. 

- 저는 네트워크를 분석하는 일을 연구실에서 많이 수행했습니다. 예전에는 netminer를 이용했는데, 요즘에는 `networkx`를 많이 이용합니다. 
- 아무튼, 네트워크가 어떻게 변하는지는 그림보다는 연속된 그림을 통해서 보는게 좋은데, 이게 또 비디오만한게 없죠. 
- 전에 제가 간단히 이미지를 비디오로 변환하는 과정을 포스팅한 적이 있는데, 이번에는 네트워크 변화를 그래프를 통해서 보여보려고 합니다. 


```python
import networkx as nx
import matplotlib.pyplot as plt
import numpy as np 

def figure_to_array(fig):
    """
    figure를 np.array로 변환하는 함수
    """
    fig.canvas.draw()
    return np.array(fig.canvas.renderer._renderer)
plt.style.use('default')
G = nx.complete_graph(20)# fully connected graph
pos = nx.shell_layout(G)# node의 위치를 고정해놓기 위해서, position을 그대로 유지함. 
#### image generation 
imgs = []## 영상으로 변경될 이미지들 
for i in range(0, 170):
    """
    - 랜덤하게 엣지를 골라서, 지웁니다. 
    """
    n1, n2 = list(G.edges())[np.random.choice(len(G.edges()))]
    G.remove_edge(n1, n2)
    f = plt.figure(figsize=(8, 8), dpi=512)
    ## 이미지를 넘길때, 그 이미지 자체가 고퀄리티여야 합니다. 그래서 dpi를 높게 유지한 상태로 넘깁니다. 
    ## default dpi는 100입니다. 또한 figure*dpi 가 출력 array의 shape이죠. 
    ## 여기서는 4096의 height, width가 리턴됩니다. 
    nx.draw_networkx(G, pos), plt.axis('off'), plt.close()
    imgs.append(figure_to_array(f))#normalization
#### image generation complete
```

```python
def show_video_in_jupyter_nb(width, height, video_url):    
    """
    jupyter notebook에서 영상을 보기 위한 함수
    """
    return HTML("""<video width="{}" height="{}" controls>
    <source src={} type="video/mp4">
    </video>""".format(width, height, video_url))

def make_video(input_imgs, output_file_path):
    ### make figure 
    fig = plt.figure(figsize=(8, 8))
    plt.axis('off'), plt.xticks([]), plt.yticks([])
    ### set init
    im = plt.imshow(input_imgs[0], interpolation='nearest')
    ### set update
    def update_img(f):#frame가 넘어옴
        tmp = input_imgs[f]
        im.set_data(tmp)# 데이터를 바꾸어주면서 그림을 그려야 함.
        return im
    plt.tight_layout()
    ani = animation.FuncAnimation(fig, func=update_img,
                                  frames=len(input_imgs),
                                  interval=500)
    writer = animation.writers['ffmpeg'](fps=25)
    ## 이 dpi는 이미지를 생성할때와 반대입니다. 
    ## 현재 넘어온 np.array의 shape이 (4096, 4096)인데, 
    ## 이를 여기서 주어진 dpi로 나누어서, output video 파일의 크기를 결정한다고 보면 되겠네요. 
    ## 단, 저는 그냥 항상 256으로 둡니다. dpi가 너무 크거나, 작으면 오류가 발생하는 것 같아요. 
    ani.save(output_file_path, writer=writer, dpi=256)
    return ani

video_url = "../../assets/images/markdown_img/180703_graph_variation.mp4"
make_video(imgs, video_url)
print("complete")
#show_video_in_jupyter_nb(400, 400, video_url)

```

## wrap-up

- 영상이 embeding이 안되서 일단 넘어갔습니다. 코드를 그대로 실행해보시고, 비디오 파일을 보시면 알수 있을 것 같아요. 
- 일단은, 그럭저럭 하고 있는데, 생각보다 이곳저곳에서 오류가 많이 발생합니다. 제가 모자란 탓이겠죠 .....
- 그리고, 현재는 이미지 자체를 변경하는 방식으로 하고 있는데, 시간이 오래 걸려서, 다른 방법도 고민을 해봐야 할것 같아요. 
    - 예를 들어서, `plt.plot`는 x, y 데이터만 업데이트하는 식으로 사용하기도 하던데, `networkx`에서도 비슷한 접근이 가능한지 확인이 필요할 것 같습니다. 


## raw-code

```python
import networkx as nx
import matplotlib.pyplot as plt
import numpy as np 

def figure_to_array(fig):
    """
    figure를 np.array로 변환하는 함수
    """
    fig.canvas.draw()
    return np.array(fig.canvas.renderer._renderer)
plt.style.use('default')
G = nx.complete_graph(20)# fully connected graph
pos = nx.shell_layout(G)# node의 위치를 고정해놓기 위해서, position을 그대로 유지함. 
#### image generation 
imgs = []## 영상으로 변경될 이미지들 
for i in range(0, 170):
    """
    - 랜덤하게 엣지를 골라서, 지웁니다. 
    """
    n1, n2 = list(G.edges())[np.random.choice(len(G.edges()))]
    G.remove_edge(n1, n2)
    f = plt.figure(figsize=(8, 8), dpi=512)
    ## 이미지를 넘길때, 그 이미지 자체가 고퀄리티여야 합니다. 그래서 dpi를 높게 유지한 상태로 넘깁니다. 
    ## default dpi는 100입니다. 또한 figure*dpi 가 출력 array의 shape이죠. 
    ## 여기서는 4096의 height, width가 리턴됩니다. 
    nx.draw_networkx(G, pos), plt.axis('off'), plt.close()
    imgs.append(figure_to_array(f))#normalization
#### image generation complete


#### video generation 
def show_video_in_jupyter_nb(width, height, video_url):    
    """
    jupyter notebook에서 영상을 보기 위한 함수
    """
    return HTML("""<video width="{}" height="{}" controls>
    <source src={} type="video/mp4">
    </video>""".format(width, height, video_url))

def make_video(input_imgs, output_file_path):
    ### make figure 
    fig = plt.figure(figsize=(8, 8))
    plt.axis('off'), plt.xticks([]), plt.yticks([])
    ### set init
    im = plt.imshow(input_imgs[0], interpolation='nearest')
    ### set update
    def update_img(f):#frame가 넘어옴
        tmp = input_imgs[f]
        im.set_data(tmp)# 데이터를 바꾸어주면서 그림을 그려야 함.
        return im
    plt.tight_layout()
    ani = animation.FuncAnimation(fig, func=update_img,
                                  frames=len(input_imgs),
                                  interval=500)
    writer = animation.writers['ffmpeg'](fps=25)
    ## 이 dpi는 이미지를 생성할때와 반대입니다. 
    ## 현재 넘어온 np.array의 shape이 (4096, 4096)인데, 
    ## 이를 여기서 주어진 dpi로 나누어서, output video 파일의 크기를 결정한다고 보면 되겠네요. 
    ## 단, 저는 그냥 항상 256으로 둡니다. dpi가 너무 크거나, 작으면 오류가 발생하는 것 같아요. 
    ani.save(output_file_path, writer=writer, dpi=256)
    return ani

video_url = "../../assets/images/markdown_img/180703_graph_variation.mp4"
make_video(imgs, video_url)
print("complete")
```