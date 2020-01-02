---
title: matplotlib로 그린 그림에 text를 추가합시다. 
category: python-lib
tags: python-lib python matplotlib

---

## matplolib로 그림 그릴 때, text 표시하기. 

- `word-embedding`을 통해 만든 결과를 `plt.scatter`를 통해 2차원 공간에 표시하고 있는데, 이 때 각 위치에 text를 표시해주는 것이 좋아서 표시해주는 방법을 정리하기로 합니다. 
- `plt.text`말고도 `plt.annotate`도 있는데, `plt.annotate`의 경우는 폰트의 크기를 조절하는 부분이 좀 어려운 것 같습니다. `plt.annotate`의 경우는 대신, 화살표를 그릴 수있다는 강점? 같은 것이 있죠. 

## plt.text

- 간단하게 x, y 좌표, string을 넘겨주면 됩니다. customizing이 쉬워서 `plt.annotate`보다 예쁘게 꾸밀 수 있습니당.

```python
import matplotlib.pyplot as plt

plt.figure(figsize=(16, 4))
plt.margins(0.1, 0.1)
for x in range(0, 8):
    for y in range(0, 4):
        plt.scatter(x, y, c='b')
        plt.text(x+0.1, y, "point({}, {})".format(x, y), fontsize=10)
plt.savefig("../../assets/images/markdown_img/mat_text_180515.svg")
```

![](/assets/images/markdown_img/mat_text_180515.svg)

## plt.annotate

- matplotlib documentation에 있는 내용을 그대로 가져왔습니다. 
- 추가로 설명할 부분은 없고, 단 `plt.annotate`에서는 폰트 크기를 조절할 수 없습니다. 

```python
import numpy as np
import matplotlib.pyplot as plt

fig = plt.figure(figsize=(12, 4))
ax = fig.add_subplot(111)

t = np.arange(0.0, 5.0, 0.01)
s = np.cos(2*np.pi*t)
line, = ax.plot(t, s, lw=2)

ax.annotate('local max', xy=(2, 1), xytext=(6, 1.5),
            arrowprops=dict(facecolor='black', shrink=0.1),
            )

ax.set_ylim(-2,2)
plt.savefig('../../assets/images/markdown_img/plt_annotate_20180515.svg')
```

![](/assets/images/markdown_img/plt_annotate_20180515.svg)