---
title: matplotlib 의 figure를 np.array로 변환합시다. 
category: python-lib
tags: python python-lib numpy matplotlib array matplotlib 
---

## 매우 간단합니다. 

- `matplotlib`로 그림을 그리다 보면, 가끔 figure를 `np.array`로 변환하고 싶을 때가 있습니다. 
- PIL이나 다른 라이브러리를 이용해서 이미지에 현재 figure에 손을 좀 보고 싶은데, 그러려면 `np.array`로 변환해야 하거든요. 
- 아무튼 그럴때 다음 코드로 아주 간단하게 해결할 수 있습니다. 

```python
# Figure to np.array 
# https://matplotlib.org/gallery/misc/agg_buffer_to_array.html
import numpy as np 
import matplotlib.pyplot as plt 

def figure_to_array(fig):
    """
    plt.figure를 RGBA로 변환(layer가 4개)
    shape: height, width, layer
    """
    fig.canvas.draw()
    return np.array(fig.canvas.renderer._renderer)

f = plt.figure()
s = 10000
plt.scatter(np.random.normal(0, 1, s), np.random.normal(0, 1, s), alpha=0.5)
#plt.margins(0, 0, tight=False)
plt.close() # 쥬피터 노트북에 그림이 자동으로 뜨는 것을 막으려고 사용. 

f_arr = figure_to_array(f)
print(f_arr.shape) # 이 RGBA로 변환됨. 
plt.figure()
plt.imshow(f_arr[:, :, :])
#plt.margins(0, 0, tight=False)
plt.savefig('../../assets/images/markdown_img/180629_figure_to_nparray.svg')
plt.show()
```

![](/assets/images/markdown_img/180629_figure_to_nparray.svg)



## reference

- <https://matplotlib.org/gallery/misc/agg_buffer_to_array.html>