---
title: matplotlib의 cmap을 알아봅시다. 
category: python-lib
tags: python python-lib matplotlib colormap numpy pandas itertools

---

## color map에서 색깔을 뽑아냅시다. 

- 급하면 'blue', 'red' 이렇게 색깔을 일일이 입력하기도 하지만, `color`에는 integer list를 넣어주고 보통은 `plt.cm`에 있는 칼라맵을 함께 넘겨줍니다. 예쁜 색 조합들이 이미 많이 있거든요. 
- 예를 들면 아래와 같은 방식이죠. 아래처럼, 색깔을 일일이 지정할 필요없이, 알아서 `c`에서 넘겨받은 값들을 `cmap`에 맞춰 변형해서 색깔을 적용해줍니다. `c`에서 색깔이 같다면, 같은 색, 비슷한 값을 가진다면 색깔별로 차이가 적도록 알아서 변형해줍니다. 

```python
X = np.random.normal(0, 1, 100)
Y = np.random.normal(0, 1, 100)
C = np.random.randint(0, 5, 100)
cmap_lst = [plt.cm.rainbow, plt.cm.Blues, plt.cm.autumn, plt.cm.RdYlGn]

f, axes = plt.subplots(1, 4, sharex=True, sharey=True)
f.set_size_inches((16, 4)) 
for i in range(0, 4):
    axes[i].scatter(X, Y, c=C, cmap=cmap_lst[i])
    axes[i].set_title("cmap: {}".format(cmap_lst[i].name))
plt.savefig('../../assets/images/markdown_img/180601_plt_cmap_variation.svg')
plt.show()
```

![](/assets/images/markdown_img/180601_plt_cmap_variation.svg)

## labeling, legend 

- 단, 이렇게 할 경우에 색깔별로 label을 만들어서 legend를 만드는 것이 어려워요. 이렇게 할 경우에는 보통 colorbar를 이용할 때도 있는데(만약 색깔이 너무 다양하면 colorbar가 더 좋을 수도 있지만) 저는 따로 따로 그려주는 것을 선호합니다. 
- 2 가지로 나누어, 색깔을 변경하려고 합니다. 
    - 색깔로 정도를 표현하고 싶은 경우(색깔이 다양한 경우)
    - 색깔로 서로 다름을 표현하고 싶은 경우(색깔이 적은 경우)

### 색깔로 정도를 표현하고 싶은 경우

- 색깔로 표현된 것이 정도일 경우, 즉, 다양한 값들이 존재하는 경우가 있습니다. 예를 들자면, x축으로는 키, y축으로는 몸무게, 색깔로는 BMI 지수 같은 것을 표현한다고 합시다. 이때, BMI의 값들은 매우 다양한데, 이러한 정도를 표현하고 싶을 때는 다음처럼 하면 됩니다. 
- 그냥 `plt.cm.rainbow`등을 cmap에 그대로 넘겨주고, `plt.colorbar()`를 하면 그대로 적용됩니다. 

```python
sample_size = 1000
color_num = 50

X = np.random.normal(0, 1, sample_size)
Y = np.random.normal(0, 1, sample_size)
C = np.random.randint(0, color_num, sample_size)

plt.figure(figsize=(12, 4))
plt.scatter(X, Y, c=C, s=20, cmap=plt.cm.Reds, alpha=0.5)
plt.colorbar(label='color')
plt.savefig('../../assets/images/markdown_img/180601_colorbar_numeric_data.svg')
plt.show()
```

![](/assets/images/markdown_img/180601_colorbar_numeric_data.svg)


### 색깔로 카테고리를 표현하고 싶은 경우

- 이 때는, 정도가 아니라, 구분을 위해서 칼라링을 하는 경우죠. 
- 이럴 때는 cmap에 `plt.cm.rainbow`를 넘기는 것이 아니라, `cmap=plt.cm.get_cmap('rainbow', color_num)`으로 원하는 종류의 색깔만 넘겨주는 것이 좋습니다. 그래야 `colorbar`가 continous한 색 조합으로 나오는 것이 아니라, discrete한 색깔 조합으로 나옵니다. 

```python
sample_size = 1000
color_num = 3

X = np.random.normal(0, 1, sample_size)
Y = np.random.normal(0, 1, sample_size)
C = np.random.randint(0, color_num, sample_size)

plt.figure(figsize=(12, 4))
plt.scatter(X, Y, c=C, s=20, cmap=plt.cm.get_cmap('rainbow', color_num), alpha=0.5)
plt.colorbar(ticks=range(color_num), format='color: %d', label='color')
plt.savefig('../../assets/images/markdown_img/180601_colorbar_categorical_data.svg')
plt.show()
```

![](/assets/images/markdown_img/180601_colorbar_categorical_data.svg)

### colorbar 말고 legend를 쓰고 싶으면

- colorbar가 미묘하게 마음에 들지 않고, legend를 쓰고 싶을때가 있을 수 있다.
- 이 때는 그룹별로 나누어, scatter 해줘야 하고, scatter시에 색깔도 다르게 먹여야 한다. 
- `plt.cm.rainbow(0.5)`를 사용하면, rainbow의 색 분포(0.0 - 1.0 사이)에서 0.5에 위치한 값을 rgba 의 형태로 뽑아낼 수 있다. 예를 들면 아래와 같다. 

```python
for a in np.linspace(0, 1.0, 5):
    print(plt.cm.rainbow(a))
```

- 이런 형태로 나오며, 이를 이용해서 colormap에 맞는 색깔을 찾아줄 수 있다. 

```
(0.5, 0.0, 1.0, 1.0)
(0.0019607843137254832, 0.70928130760585339, 0.92328910610548931, 1.0)
(0.50392156862745097, 0.99998102734872685, 0.70492554690614728, 1.0)
(1.0, 0.70054303759329106, 0.37841105004231035, 1.0)
(1.0, 1.2246467991473532e-16, 6.123233995736766e-17, 1.0)
```

- 이런 방식으로, 카테고리별로 색깔을 지정하고 이를 적용해서 다음처럼 그림을 그려줄 수도 있다. 나의 경우는 칼라바보다, 이 경우가 더 마음에 드는 것 같다. 

```python
import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt
import itertools

sample_size = 100
x = np.vstack([
    np.random.normal(0, 1, sample_size).reshape(sample_size//2, 2), 
    np.random.normal(2, 1, sample_size).reshape(sample_size//2, 2), 
    np.random.normal(4, 1, sample_size).reshape(sample_size//2, 2)
])
y = np.array(list(itertools.chain.from_iterable([ [i+1 for j in range(0, sample_size//2)] for i in range(0, 3)])))
y = y.reshape(-1, 1)

df = pd.DataFrame(np.hstack([x, y]), columns=['x1', 'x2', 'y'])

c_lst = [plt.cm.rainbow(a) for a in np.linspace(0.0, 1.0, len(set(df['y'])))]

plt.figure(figsize=(12, 4))
for i, g in enumerate(df.groupby('y')):
    plt.scatter(g[1]['x1'], g[1]['x2'], color=c_lst[i], label='group {}'.format(int(g[0])), alpha=0.5)
plt.legend()
plt.savefig('../../assets/images/markdown_img/180601_legend_instead_of_colorbar.svg')
plt.show()
```

![](/assets/images/markdown_img/180601_legend_instead_of_colorbar.svg)


## wrap-up

- 이제 color를 좀 마음대로 조합할 수 있을 것 같다. 매우 조쿤여!

## reference 

- <https://chrisalbon.com/python/basics/set_the_color_of_a_matplotlib/>