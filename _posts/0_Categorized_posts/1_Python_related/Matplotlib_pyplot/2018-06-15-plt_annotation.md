---
title: plt annotation하기 
category: python-lib 
tags: python python-lib annotation matplolib
---

## 그림에 주석을 달아 봅시다. 

- histogram, scatter plot 등에서 파워포인트처럼 설명을 달아보고 싶을 때가 있습니다. 

- `plt.text`: 그냥 텍스트를 좌표 상에 올리는 식인데, 
    - `bbox` argument를 함께 넘겨서, 글상자를 만들어줄 수도 있고
- `plt.annotate`: 텍스트를 화살표와 함께 넘겨주는 형시인데, 
    - `arrowprops` argument를 함께 넘겨서 화살표를 함께 만들어줄 수도 있습니다.
- 아래는 각각을 대충 만들어본 결과물입니다. 

```python
import matplotlib.pyplot as plt
import numpy as np 
import pandas as pd

sample_size = 1000
x = list(np.random.normal(0, 1, sample_size))+[5]
y = list(np.random.normal(0, 1, sample_size))+[5]

plt.figure(figsize=(12, 6))
#plt.scatter(x, y, alpha=0.5)

plt.xlim(min(x), max(x)+3)
plt.ylim(min(y), max(y)+3)

plt.text(5, 5, s='outlier', fontsize=20, fontweight='bold')
"""
- what is the shrink meaning? 
"""
plt.annotate('annotate with bbox and arrow', xy=(5, 5), xytext=(-3, 6), fontsize=30,
             bbox=dict(boxstyle='square', color='grey'), 
             arrowprops=dict(facecolor='black')
            )
plt.annotate('annotate with arrow', xy=(5, 5), xytext=(2, 4), fontsize=30,
             arrowprops=dict(facecolor='black')
            )
plt.text( 5, 0, 'text with bbox', bbox=dict(boxstyle='square', color='grey'))
plt.text( 4, -2, 'text with round4 bbox', fontsize=30, bbox=dict(boxstyle='round4', color='grey'))
plt.savefig('../../assets/images/markdown_img/180615_1652_annotation_with_bbox_and_arrow.svg')
plt.show()
```

![](/assets/images/markdown_img/180615_1652_annotation_with_bbox_and_arrow.svg)

## wrap-up 

- histogram, scatter에서 개별 좌표, 바에 대해서 설명을 다는 것이 좋을 때가 있다. 
- [이 블로그](http://www.futurile.net/2016/03/13/complex-text-formatting-in-matplotlib-using-latex/)에서는 latex를 이용해서 annotation하는 방법도 함께 알려주고 있는데, 지금 내가 당장 이것이 필요한건 아니니까 넘어간다 하하핫. 

## reference

- <http://www.futurile.net/2016/03/01/text-handling-in-matplotlib/>