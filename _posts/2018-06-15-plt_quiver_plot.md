---
title: quiver plot을 사용해봅시다. 
category: python-lib
tags: python python-lib matplotlib sympy numpy
---

## quiver plot으로 gradient vector 표현하기 

- 찾다보니, quiver plot이라는 것이 matplotlib에 있더군요.
- quiver의 뜻은 '화살통'...'진동 등이 떨리는 것'이라고 나와 있는데...무슨 말인지는 잘 모르겠고, 아무튼 2차원 평면 상에서 좌표마다 scaled된 화살표를 그릴 때 사용합니다.....설명 개구리네요. 개굴
- 아무튼 이걸 보니까 왠지 gradient vector를 그리기 좋을 것 같다는 생각이 들었고, 그래서 그려 봅니다 하하핫. 

## 해보죠

- 전에 만들어두었던 sympy를 이용해서 gradient vector를 계산하는 코드를 사용하고, 이 코드를 이용해서 개별 좌표에서의 gradient vector를 계산해줍니다. 
- quiver plot이 편한 이유 중 하나는 화살표를 알아서 scaling해준다는 거죠(직접 스케일리을 잘하는거, 매우 어렵더라고요)

```python
import sympy 
import numpy as np 
import matplotlib.pyplot as plt

# gradient vector를 구하기 위해서, symbolic formula로 표현해줌
x, y = sympy.symbols('x y')
#f = x**2 + y**2 +x*y
f = x**2 + y**2 + x*y - sympy.sin(x)*5
f_diff_by_x = sympy.diff(f, x)
f_diff_by_y = sympy.diff(f, y)

# make meshgrid with xs, ys 
sample_size = 100
xs, ys = np.meshgrid(np.linspace(-10, 10, sample_size), np.linspace(-10, 10, sample_size))

# make zs 
zs = [float(f.subs(x, xv).subs(y, yv)) for xv, yv in zip(xs.ravel(), ys.ravel())]
zs = np.array(zs).reshape(sample_size, sample_size)

plt.figure(figsize=(16, 8))
plt.contour(xs, ys, zs, 50, levels = np.logspace(-1.2, 2.3, 20), cmap=plt.cm.rainbow)

# gradient vector는 조금 덜 촘촘하게 meshgrid를 그려줌
xs_q, ys_q = np.meshgrid( np.linspace(-10, 10, 10), np.linspace(-10, 10, 10) )

# gradient vector 계산 
xs_q_grad = [-float(f_diff_by_x.subs(x, xv).subs(y, yv)) for xv, yv in zip(xs_q.ravel(), ys_q.ravel())]
ys_q_grad = [-float(f_diff_by_y.subs(x, xv).subs(y, yv)) for xv, yv in zip(xs_q.ravel(), ys_q.ravel())]
"""
간단하게,
scale: 길이, 값을 키울수록 화살표의 길이는 작아짐. 
width: 너비(화살표의 너비)
"""
plt.quiver(xs_q, ys_q, xs_q_grad, ys_q_grad, width=0.005, scale=500, color='red')
plt.savefig('../../assets/images/markdown_img/180615_1602_quiver_plot_with_grad.svg')
plt.show()
```

![](/assets/images/markdown_img/180615_1602_quiver_plot_with_grad.svg)

## wrap-up

- 막상 그리고보니, 물리학 하는 사람들이 아니면, 별로 쓸모 없을 것 같기도하고...그냥 gradient vector를 그리는 것 빼고 무슨 의미가 있나 싶기도 하네요....