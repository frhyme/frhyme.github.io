---
title: scipy를 이용하여 최적화를 해봅시다. 
category: python-lib
tags: python python-lib optimization scipy numpy matplotlib

---

## scipy를 이용한 optimization. 

- [제가 공부한 포스트](https://datascienceschool.net/view-notebook/4642b9f187784444b8f3a8309c583007/)에서는 `import scipy as sp`로 importing한 다음 `scipy`를 이용하는데, 요즘에는 이게 막혀 있는 것 같아요. 묘하게도 반드시 `from scipy.optimize import minimize`와 같은 방식으로 사용해야 합니다. 
- 아무튼, 이전에 포스팅한 sympy에 비해서 약간 편한데, 
    - np.array를 argument로 받아서 결과 값을 리턴해주는 함수를 만들고, 
    - 그 함수와 초기값을 argument로 `scipy.optimize.minimize`에 넣어주면 됩니다. 
        - 여기서, 반드시 `from scipy.optimize import minimize`로 사용해야 합니다. 

## just do it.

- 그래서, 일반적인 함수 `f`를 정의하고, 이를 `minimize`에 넣어주면 끝납니다 하하핫. 

```python
from scipy.optimize import minimize
import matplotlib.pyplot as plt
import numpy as np 

def f_xy(xy):# input should be ndarray 
    r = xy + np.array([-5, -1])
    return r.dot(r) + 10

sample_size = 100 
xs = np.linspace(-10, 10, sample_size)
ys = np.linspace(-10, 20, sample_size)

xs, ys = np.meshgrid(xs, ys)
zs = np.array([f_xy(np.array([x, y])) for x, y in zip(xs.ravel(), ys.ravel())]).reshape(sample_size, sample_size)

plt.figure(figsize=(15, 5))
plt.contour(xs, ys, zs, levels = np.logspace(1, 3, 20), cmap=plt.cm.rainbow) # draw

# optimization 
x0 = np.array([-7.5, 5])  # 초기값
result = sp.optimize.minimize(f_xy, x0) # optimization

if result['success']==True:
    x_opt, y_opt = result['x']
    plt.annotate('global optimum: {:.2f}'.format(result['fun']), xy=(x_opt, y_opt), xytext=(x_opt-2, y_opt+5), 
                 fontsize=20, arrowprops=dict(facecolor='black', shrink=0.05, linewidth=1),
                )
    plt.scatter(x_opt, y_opt, s=500, color='red')
    plt.arrow(x0[0], x0[1], x_opt-x0[0], y_opt-x0[1],
              head_width=1, head_length=0.4, fc='k', ec='k', lw=2)
#plt.colorbar() 
# plt.scatter를 쓸 경우에, plt.colorbar는 쓸 수 없음 
plt.savefig('../../assets/images/markdown_img/180615_1514_optimization_contour.svg')
plt.show()
```

![](/assets/images/markdown_img/180615_1514_optimization_contour.svg)

## wrap-up

- `scipy.optimize.minimize`에 이것말고도 뭐가 더 있을 것 같기는 한데, 그냥 이정도로 할래요. 만약 저는 추가로 해야하는 것들이 있다면 `sympy`를 쓰는 편이 더 좋을 것 같습니다. 

## reference 

- <https://datascienceschool.net/view-notebook/4642b9f187784444b8f3a8309c583007/>