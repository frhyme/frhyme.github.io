---
title: subplot의 사이즈를 각각 다르게 조절합시다!
category: python-lib
tags: python python-lib matplotlib subplot 

---

## subplot의 사이즈는 어떻게 조절할 수 있을까요? 

- 전체 figure에서 한번에 조절할 수있는 방법이 있는건가 싶었는데(아마도 있긴 있겠지만), grid로 한번에 넘겨주는 게 더 깔끔한 것 같아요. 네 여기서는 gridspec이라는 것을 사용해서 그립니다. 

```python
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import gridspec

# generate some data
x = np.arange(0, 10, 0.2)
y = np.sin(x)

# plot it
fig = plt.figure(figsize=(15, 6)) 
gs = gridspec.GridSpec(nrows=3, # row 몇 개 
                       ncols=2, # col 몇 개 
                       height_ratios=[3, 2, 1], 
                       width_ratios=[12, 3]
                      )
"""
앞에서 row, column의 수를 함께 넘겨줘서 gridspec에 인덱싱할 때, 
2차원 어레이에 접근하는 식으로 해야하는줄 알았는데 아닙니다. 
그냥 row size * column size 형태의 1차원 어레이라고 생각하고 하면 됩니다.
"""
ax0 = plt.subplot(gs[0])
ax0.plot(x, y)
ax1 = plt.subplot(gs[1])
ax1.plot(y, x)
ax1 = plt.subplot(gs[2])
ax1.plot(y, x)
ax1 = plt.subplot(gs[3])
ax1.plot(y, x)
ax1 = plt.subplot(gs[4])
ax1.plot(y, x)
ax1 = plt.subplot(gs[5])
ax1.plot(y, x)

plt.savefig('../../assets/images/markdown_img/change_subplot_size_20180516.svg')
plt.show()
```

![](/assets/images/markdown_img/change_subplot_size_20180516.svg)

## reference 

- <https://matplotlib.org/api/_as_gen/matplotlib.gridspec.GridSpec.html>