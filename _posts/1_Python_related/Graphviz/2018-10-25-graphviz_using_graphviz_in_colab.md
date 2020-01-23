---
title: google colab에서 graphviz 사용하기.
category: python-libs
tags: python-libs python graphviz google google-colab layout matplotlib networkx
---

## intro

- 이제는 `networkx`와 `matplotlib`를 너무 많이 사용해서, 이 둘을 사용해서 그림을 그릴 때가 편할때가 있습니다만, 가끔 `graphviz`의 layout을 이용해서 그림을 그려주고 싶을 때가 있습니다.

- 대략 아래 그림처럼 뭔가 binary tree같은 애들을 그려주기가 편하죠. root node부터 그려주고, level이 같은 애들은 같은 층에 그려주니까요. 

![](https://i.imgur.com/XmHZ3gv.png)

## install it in colab

- 전에도 얘기한 적이 있지만, 저는 이제 jupyter notebook을 쓰지 않고(정확히는 로컬에 서버를 돌려서 사용하지 않고), colab를 사용하고 있습니다. 
- 혹시 `virtualenv`를 사용하시는 분이 있는지 모르겠습니다만, 이걸 쓰는 목적은, 개별 프로젝트에 따라서 발생하는 의존성의 문제를 해결하기 위해서, 특정 폴더를 아예 별개의 환경으로 관리하기 위함이죠. 
- colab은 실행하기 전에 이미 깔려 있는 라이브러리들을 제외하고, 새로운 라이브러리를 설치해야 할 경우, 매번 라이브러리를 설치해야 합니다. 
- 처음에는 이게 꽤 불편하다고 생각했는데, 오히려 잡스러운 것들을 다 삭제해주고, 늘 환경을 바닐라 상태로 세팅할 수 있어서 더 좋은 것 같습니다. 저의 경우는요. 

### 아무튼 install 

- 아무튼 설치합니다. 아래를 사용하면 설치할 수 있습니다. 
    - `-q`는 설치하면서, output을 적게 출력한다는 것입니다. 큰 의미는 없어요. 


```bash
## using graphviz 
!apt-get -qq install -y graphviz && pip install -q pydot
import pydot
## 아래 있는것은 필수는 아닌데, 가끔 에러가 생길 때가 있어서, 그냥 같이 해줌. 
!apt-get install graphviz libgraphviz-dev pkg-config
!pip install pygraphviz
import pygraphviz
```

- 이제 아래의 코드를 사용해서 그래프를 그려주면 잘 그려지는 것을 알 수 있습니다. 

```python
plt.figure(figsize=(12, 6))
nx.draw_networkx(
    input_G
    pos=nx.drawing.nx_pydot.graphviz_layout(
        input_G, prog='dot'## prog='dot' 를 반드시 넣어야만 함. 
    )
)

plt.axis('off')
plt.show()
```

## wrap-up

- 앞서 비슷한 이야기를 했지만, 필요할 때마다, 패키지를 설치해서 돌리는 것이, 매번 노트북을 시작할때마다 조금 시간이 걸리는 문제는 있지만, 훨씬 효율적인 것 같습니다. 
- 매번 초기화해놓고 시작하니까, 이후에 문제가 생길 가능성도 확실히 줄어들고요 


## reference

- <https://stackoverflow.com/questions/49853303/how-to-install-pydot-graphviz-on-google-colab>
- <https://medium.com/deep-learning-turkey/google-colab-free-gpu-tutorial-e113627b9f5d>
- <https://stackoverflow.com/questions/15661384/python-does-not-see-pygraphviz/39976362#39976362>