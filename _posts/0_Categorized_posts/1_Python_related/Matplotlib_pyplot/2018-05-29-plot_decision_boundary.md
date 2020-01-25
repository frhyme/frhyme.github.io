---
title: decision boundary를 그려 봅시다.
category: python-lib 
tags: python python-lib matplotlib numpy

---

## Decision Boundary가 뭔가요? 

- 예를 들어봅시다. classification 문제를 해결하기 위해 데이터를 이용해 학습을 시켰습니다. 간단히, score를 보니까 꽤 높은 편이고, 딱히 오버피팅인 것 같지도 않긴 합니다만, 2차원에 뿌려서, 어떤 평면이 **classifying line** 을 생성하는지, 직접 보고 싶을 때가 있습니다. 

![](https://www.cs.princeton.edu/courses/archive/fall08/cos436/Duda/PR_Figs/regions3.gif)

- 이 decision boundary를 그려 보고 싶어서 그렸습니다. 

## 그립니다. 

```python
import numpy as np
import matplotlib.pyplot as plt

"""
x, y를 각각의 평균과 분산에 따라서 생성해주는 함수를 만들었습니다. 
np.vstack은 세로로 쌓아줍니다.
(1, nrow)
(1, nrow)
"""
def normal_sampling(mu1, v1, mu2, v2, nrow):
    x = np.random.normal(mu1, v1, nrow)
    y = np.random.normal(mu2, v2, nrow)
    return np.vstack([x,y])
"""
다양한 평균과 분산에 대해서 샘플링하여 쌓아줍니다. 
np.hstack은 가로로 붙여줍니다. 
그래서 마지막에 Transpose 했습니다. 
"""
sample_size = 500
cluster_num = 3
X = np.hstack([
    normal_sampling(0, 1, 0, 1, sample_size),
    normal_sampling(2, 1, 2, 1, sample_size), 
    normal_sampling(3, 1, 7, 1, sample_size),
    normal_sampling(8, 1, 4, 1, sample_size),
    normal_sampling(6, 1, 5, 1, sample_size),
    normal_sampling(6, 3, 0, 1, sample_size),
    normal_sampling(0, 3, 6, 2, sample_size)
]).T
Y = []
for i in range(0, X.shape[0]//sample_size):
    Y+=[i for j in range(0, sample_size)]
Y = np.array(Y)

plt.figure(figsize=(15, 6))
plt.scatter(X[:, 0], X[:, 1], c=Y, cmap=plt.cm.rainbow, alpha=0.2)

"""
대충 학습을 시키고요...
"""
from sklearn.neural_network import MLPClassifier
clf = MLPClassifier(hidden_layer_sizes=[50, 50, 10], activation='relu')
clf.fit(X, Y)
#print(clf.score(X, Y))

"""
grid_size를 대충 잡고, 인공적으로 값들을 만들어줍니다. 
이를 활용해서 np.meshgrid를 만들고, 이 값들별로 class를 에측하고, 컨투어를 그려줍니다. 
"""
grid_size = 500
A, B = np.meshgrid(np.linspace(X[:, 0].min(), X[:, 0].max(), grid_size),
                   np.linspace(X[:, 1].min(), X[:, 1].max(), grid_size))
C = clf.predict( np.hstack([A.reshape(-1, 1), B.reshape(-1, 1)]) ).reshape(grid_size, grid_size)
plt.contourf(A, B, C, alpha=0.3, cmap=plt.cm.rainbow)
plt.axis('off')
plt.savefig("../../assets/images/markdown_img/decision_boundary_180529_1807.svg")
plt.show()
```

![](/assets/images/markdown_img/decision_boundary_180529_1807.svg)


## wrap-up 

- 단, 여기서 문제는 우리가 가진 X 값의 칼럼이 2가지만 있을때, 이렇게 decision boundary를 그리는 것이 가능합니다. 
    - 우리는 X의 구간, Y의 구간을 잡고, meshgrid를 만든 다음, 그 값들을 가질 경우 어떻게 분류되는가? 를 우리가 만든 classifier를 활용해 학습합니다. 이렇게 예측된 값을 색깔로 뿌리게 되고, 그 방식이 컨투어인 것이죠. 
    - 즉, 원래 우리가 가지고 있는 데이터의 feature의 개수와, 인공적으로 만들어내는 feature의 수가 같아야 한다는 말인데, 만약 feature의 개수가 4개라고 생각해봅시다. 
- 만약 feature의 개수가 3개 이상이라면, 일단 `meshgrid`를 사용할 수 없습니다. 2차원 그림에 직접 그릴 수도 없고, tsne를 통해 차원축소를 한 다음에 해야 하죠. 
    - hyperplane 자체에 대해서 너무 울퉁불퉁하지 않은지, 뭐 그런걸 볼 수 있을수도 있을텐데, 요건 제 상상의 범위를 벗어나네요. 