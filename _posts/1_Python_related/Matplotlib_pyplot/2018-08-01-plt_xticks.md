---
title: plt.xticks 조절하기 
category: python-lib
tags: python python-lib matplotlib tick
---

## 그림에 tick 표시하기 

- `matplotlib`에서 그림을 그릴 때, tick을 몇 개나, 또 어떤 label로 표현할지를 조절하고 싶을때 `plt.xticks()`를 사용합니다. 
- 간단하게 다음 코드를 보면 tick을 표시할 값, 그리고 해당 위치에 어떤 label을 작성할지 함께 넘겨줍니다.

```python
## plt.xticks()
plt.figure(figsize=(12, 4))
plt.plot(np.arange(0, 100, 1), np.random.normal(0, 1, 100), '*-', linewidth=1)
## 아래처럼 tick을 표시할 값을 먼저 넣어주고, 그 다음에 그 위치에 들어갈 값을 넣어줍니다. 
plt.xticks(np.arange(0, 100, step=5), ["x_{:0<2d}".format(x) for x in np.arange(0, 100, step=5)], 
           fontproperties=BMDOHYEON, 
           fontsize=20, 
           rotation=45
          )
plt.yticks([-2, 0, 2], 
           [ "y_{}".format(x) for x in [-2, 0, 2]], 
           fontproperties=BMJUA, 
           fontsize=15
          )
plt.savefig('../../assets/images/markdown_img/180801_plt_xticks.svg')
plt.show()
```

![](/assets/images/markdown_img/180801_plt_xticks.svg)

- 잘 되는군요 하하핫. 