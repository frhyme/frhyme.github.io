---
title: matplotlib에서 axis를 제거해봅시다. 
category: python-lib
tags: python python-lib matplotlib axis
---

## 위쪽 오른쪽 등 일부분의 axis만 없애고 싶을때는? 

- axis때문에 그림이 별로 예쁘지 않게 보일 때가 있어요. 삭제해야 괜찮을 때가 있는데, 전부다 삭제하는 건 싫을 때도 있구요. 
- 간단하게 `axis('off')`를 해버리면, `ticklabels`까지 모두 없어지는 경우가 있어서, 부분적으로 없애고 싶을 때도 있구요. 
- 이것 또한 매우 간단합니다. 

## do it

- `plt.gca().spines['left'].set_visible(False)`를 사용하면 됩니다. left 대신, right/bottom/top 등을 사용하면 됩니다. 

```python
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 1, 100)
y = np.exp(x)

f, axes = plt.subplots(1, 4, figsize=(15, 3))
axes[0].plot(x, np.exp(x))
axes[0].set_title("default axis")

axes[1].plot(x, np.exp(x))
axes[1].set_title("remove right, top")
axes[1].spines['right'].set_visible(False)
axes[1].spines['top'].set_visible(False)

axes[2].plot(x, np.exp(x))
axes[2].set_title("remove left, bottom")
axes[2].spines['left'].set_visible(False)
axes[2].spines['bottom'].set_visible(False)

axes[3].plot(x, np.exp(x))
axes[3].set_title("axis off")
axes[3].axis('off')

plt.savefig('../../assets/images/markdown_img/180619_axis_off.svg')
plt.show()
```

![](/assets/images/markdown_img/180619_axis_off.svg)

## wrap-up

- `spine`을 없애도, `ticklabels`는 없애지지 않습니다. 단, `axis`를 없애면 다 날아가요. 

## reference 

- <https://stackoverflow.com/questions/925024/how-can-i-remove-the-top-and-right-axis-in-matplotlib>