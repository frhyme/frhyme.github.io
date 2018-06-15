---
title: optimization 기본 
category: optimization 
tags: python python-lib optimization matplotlib sympy numpy 

---

## gradient decent method and plotting with matplotlib 

- datascience school의 자료를 보다가 [최적화](https://datascienceschool.net/view-notebook/4642b9f187784444b8f3a8309c583007/)라는 포스트를 보고, 정리를 해야 할것 같았습니당. 계속 이어지는 자료이긴 한데, 여기서는 gradient descent만 우선 정리하였구요. 이후에는 `scipy`를 이용한 최적화 방법들을 정리합니다. 

- 학부시절에 최적화 수업도 듣고, 대학원 와서는 수리계획이라는 LP문제 푸는 수업도 들었습니다. duality니 어쩌고 저쩌고 많이 나왔던 것 같은데, 지금은 전혀 기억이 나지 않습니다. 수플렉스! 뭐 그런것만 기억나네요. 그래요...나는 유사 공대생...
- 아무튼, 기억나는 것은 **objective function을 정하고, 그것을 minimize 혹은 maximize 할 수 있는 값을 찾는 것** 이 최적화 다, 라는 것만 알고 있네요. 
- 이를 머신러닝 모델에 적용하여 말한다면, 보통 우리가 머신러닝 문제들에서 하는 것들은 에러를 최소화해주는 어떤 값들을 찾아주는 것입니다. 아주 간단하게, 우리가 가지고 있는 모델이 선형모델이고, `y_pred = w* x + b`라고 한다면, 우리가 최소화하려는 것은 아마도, `(y_true - y_pred)**2`가 되겠죠. 이 아이를 objective function으로 두고, 최소화할 수 있는 w와 b를 찾는 것이 우리의 숙제가 됩니다. 
- 이렇게 생각하니까, 그동안 gradient descent 등의 방법이 이제서야 이해가 되네요. 결국 최적화가 중요하다 이말이야

- 아무튼 그 생각을 하다보면, 다시 고등학교 수학 때 생각이 납니다. 최소값, 최대값 구하는 문제들. 그 문제들은 결국 미분을 일단 하고, 미분이 0이 되는 값을 찾아서 그 값을 비교해서 풀었던 것 같아요....맞겠죠??

## 그래서, 어떻게 찾습니까? 

- 만약, 1차원, 2차원 데이터일 경우에는 대충 그림을 그려보면 됩니다 하하핫. 아래처럼 그림을 그려서, plotting된 것을 보면, 아 대략 모수를 어느 정도로 맞춰야 우리가 원하는 objective function의 값이 제일 작아지겠구나를 알 수 있어요. 
- 아래 그림을 보면 대략 모수 `x`와 `y` 모두 0 근처에 있어야 우리가 원하는 objective function이 제일 작아지는 것을 알 수 있습니다. 

```python
import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt

x = np.linspace(-10, 10, 100)
y = np.linspace(-10, 10, 100)

x, y = np.meshgrid(x, y)
plt.figure(figsize=(15, 6))
plt.contour(x, y, x**2 + y**2 + x*y - np.sin(x)*5, 50, cmap=plt.cm.rainbow)
plt.colorbar()
plt.savefig('../../assets/images/markdown_img/180614_1926_contour_for_optm.svg')
plt.show()
```

![](/assets/images/markdown_img/180614_1926_contour_for_optm.svg)

## 다른 방법을 찾습니다. 

- 하지만, feature dimension이 굉장히 많아지면, 이렇게 plotting해서 볼 수 없습니다. 물론 Grid Search처럼 가능한 Grid에서 가장 작은 경우를 찾는 방식도 있습니다만(이 방식이 sklearn에 있는 `GridSearchCV`죠).
- 다른 방식이 필요해요. 아마도, 머신러닝을 조금이라도 공부해보셨다면 사실 이미 아시겠지만, `Gradient Descent method`라는 것이 있습니다. 
- 다시, 우리가 알아야 하는 것은 우리가 원하는 objective funtion을 최소로 만들어주는 어떤 모수들 입니다. 음 모수라는 말보다는 weight가 더 적합한 말일 수도 있습니다만. 아무튼, 그 weight를 찾으려면 다음 두 가지의 방식이 필요합니다. 
    - evaluation: 현재 objective function은 어느 정도 값을 가지나? 괜찮은 정도인가? 
    - update: weight를 어떻게 조정해야 하나? 

- objective function의 최소값은 무조건 기울기가 0이 됩니다. 당연한 사실이죠(기울기가 0이라고 최소값인 것은 아닙니다, 이걸 조심해야 합니다). 
- 아무튼 일반적인 2차함수에서 개별 좌표에서 기울기를 계산해주면 그 기울기는 최소/최대값을 향하게 됩니다. 이 기울기를 활용하여 그 방향으로 점차 update하는 것. 그 방식을 보통 gradient descent라고 합니다. 

## gradient descent. 

- sympy를 이용해서, gradient descent를 계산하고, 그 방향으로 나아가는 식으로 정리했습니다. sympy에 익숙하다면, 방정식을 만들고, 미분하여 반복하는 것이 더 적합할 수도 있을 것 같습니다. 
- 사실 tensorflow에서 계산할 때, 내가 미분을 잘 계산했나, 이게 맨날 헷갈려서 은근히 힘들었거든요. 

```python
import sympy 
import numpy as np 
import matplotlib.pyplot as plt

x, y = sympy.symbols('x y')
f = x**2 + y**2 +x*y
f_diff_by_x = sympy.diff(f, x) # x로 편미분 
f_diff_by_y = sympy.diff(f, x) # y로 편미분

sample_size = 100
xs = np.linspace(-10, 10, sample_size)
ys = np.linspace(-10, 10, sample_size)
xs, ys = np.meshgrid(xs, ys) # contour를 그리려면, meshgrid가 필요함 
zs = [float(f.subs(x, xv).subs(y, yv)) for xv, yv in zip(xs.ravel(), ys.ravel())]
# .ravel의 경우 한쪽으로 쭉 펴주는 것을 의미함. 
zs = np.array(zs).reshape(sample_size, sample_size)

plt.figure(figsize=(16, 6))
plt.contour(xs, ys, zs, 50, levels = np.logspace(-1.2, 2.3, 20), cmap=plt.cm.rainbow)

curr_p = np.array([8.0, 8.0]) # gradient descent 시작점
step = -0.1 # step size or learning rate 

for i in range(0, 5):
    #plt.scatter(curr_p[0], curr_p[1], marker='o', s=100, color='red')
    dx = float(f_diff_by_x.subs(x, curr_p[0]).subs(y, curr_p[1]).evalf())*step
    dy = float(f_diff_by_y.subs(x, curr_p[0]).subs(y, curr_p[1]).evalf())*step
    dxy = np.array([dx, dy])
    plt.arrow(curr_p[0], curr_p[1], dx=dx, dy=dy, head_width=1, head_length=0.5, fc='k', ec='k', lw=2)
    curr_p +=dxy
    #plt.scatter(curr_p[0], curr_p[1], marker='o', s=100, color='red')
plt.colorbar()
plt.savefig('../../assets/images/markdown_img/180614_2035_gradient_descent_arrow.svg')
plt.show()
```

![](/assets/images/markdown_img/180614_2035_gradient_descent_arrow.svg)

## wrap-up

- 요즘에 한 포스트에 내용이 너무 길어지는 일들이 많아서, 가능하면 좀 분리해서 쓰려고 합니다. 제 생각에 gradient descent method와 scipy를 이용한 optimization은 구분되어 작성되는 것이 더 좋을 것 같아요. 그래서 다른 포스트로 넘어갑니다. 

## reference

- <https://datascienceschool.net/view-notebook/4642b9f187784444b8f3a8309c583007/>