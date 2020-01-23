---
title: plt.figure()의 parameter를 조정해봅시다. 
category: python-lib
tags: python python-lib matplotlib figure dpi numpy 
---

## plt.figure()의 파라미터 조정하기. 

- `matplotlib`를 사용할 때 사실 보통 `plt.figure()`만을 쓰기는 하는데, 내부에 보면 다양한 파라미터들이 있어요. 이걸 건드리면 그림을 조금 더 마음에 들게 뽑을 수 있습니다. 
- 사실 매번 그림을 `plt.savefig("")`로 처리하는 경우에는, plt.figure()에 파라미터를 설정해야 하는 일이 많지 않습니다. 그냥 svg로 저장하거나, 다른 이미지 포맷으로 저장할 때는 `dpi`값을 높이면 되는 거니까요. 
- 그런데 저처럼, 이미지를 `np.array`로 변환해야 할때는 figure에 dpi 값 자체를 저장하는 편이 좋습니다. 

```python
import matplotlib.pyplot as plt
import numpy as np 

def figure_to_array(fig):
    """
    plt.figure()를 np.array로 변환
    """
    fig.canvas.draw()
    return np.array(fig.canvas.renderer._renderer)

f1 = plt.figure(
    figsize=(8, 4), 
    facecolor='white', # background color
    edgecolor='red', 
    dpi=10, # dpi 값을 높게 설정해야, figure를 np.array로 변환했을 때 깨끗하게 나옴
)
x = np.random.normal(0, 1, 50)
plt.plot(range(0, len(x)), x, marker='o', linestyle='--')
#plt.savefig('../../assets/images/markdown_img/180702_plt_figure_parameter.png')
plt.close()

plt.figure(figsize=(16, 8))
plt.imshow(
    figure_to_array(f1)
)
plt.savefig('../../assets/images/markdown_img/180702_plt_figure_parameter.svg')
plt.show()
```

- 아래 보시는 것처럼 dpi에 따라서 그림이 다르게 나옵니다. 

![](/assets/images/markdown_img/180702_plt_figure_parameter.svg)

## wrap-up

- figure를 np.array로 변환하는 경우에는 dpi를 꼭 설정하도록 합시다 하하핳

## reference

- <https://matplotlib.org/api/_as_gen/matplotlib.pyplot.figure.html>