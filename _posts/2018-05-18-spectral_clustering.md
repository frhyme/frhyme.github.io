---
title: spectral clustering에 대해서 정리해보겠습니다. 
category: data-science
tags: data-science python python-lib clustering gaussian-mixture-model spectral-clustering not-yet

---

## 일반적인 clustering

- 클러스터링을 하기 위해서는 개체 간의 거리를 재는 것이 중요합니다. 이 때, **이 개체 간의 거리를 무엇으로 재는가?** 가 중요한데, 데이터가 `pd.DataFrame()`이라면, `index`는 개체의 이름, `column`은 개체가 가진 특성의 이름이 되겠죠. 
    - 예를 들어, 야구선수라면 칼럼의 이름들은 (타율, 안타 수, 출루율 등등)이 되죠. 
    - 클러스러팅을 할 때는 개체간의 거리를 재야 하고, 이 값들을 가지고 거리를 재게 되죠. 
- 그런데, 야구선수들의 특성을 가지고 야구선수간의 거리를 잰 다음 `weighted undirected network`를 만들 수도 있겠죠. 그리고 이 네트워크를 가지고 `adjancency matrix`를 만들 수도 있습니다. 
    - 어찌보면, `index`는 개체의 이름, `column`은 특성의 이름 인 경우와 다르지 않다고 볼수도 있습니다. `index`와 `column`이 다른 경우는 `bipartite graph`라고 볼 수 있을 것 같네요. 
    - 새롭게 만들어낸 `adjancency matrix`sms bipartite graph를 일종의 projection한 것이라고 볼 수 있을 것 같네요. 
- 이렇게 생성된 adjacency matrix의 경우는 '의미적으로는' 각 노드가 다른 노드들과 얼마나 가깝게 있느냐 얼마나 멀리 있느냐를 의미합니다. 그리고, 이러한 거리도 앞서 말했던 '타율', '안타수'처럼 특성으로 고려할 수 있겠죠. 

## 그래서, spectral clustering 

- 그래서, spectral clustering은 개체간의 거리를 가지고 만든 `adjancency matrix`를 활용해 클러스러팅하는 것을 말합니다. 
- 보통, 거리를 재었을때, 완전히 똑같아서 거리가 0이 되는 경우는 잘 없으니까, 만들어진 `adjancency matrix`로부터 만들어지는 네트워크는 `fully connected network`가 되겠네요.

### standardization using gaussian kernel

- 혹시나 해서 말하지만, 값들이 표준화되어 있지 않을 수 있습니다. 만약 해당 network의 weight가 '빈도'라면 이 값들이 널뛸텐데, minmaxscaling도 좋지만, gaussian kernel을 이용해서 값을 변환 것이 더 적합할 것 같습니다. 
    - `gaussian kernel`을 이용하여 변환해준다는 것: 이 말은, 해당 데이터들이 모두 gaussian dist.를 따르고 있고 그렇기 때문에 norm(0, 1)의 형태로 변환해줄 수 있다는 것을 의미합니다. 
    - 이렇게 했을 경우에, 값이 평균으로부터 얼마나 멀리 떨어져 있는지를 파악할 수 있기 때문에, 아웃라이어들을 판단하고 필터링할 수 있음. 

## anyway, cut and cut for clustering

- 그렇습니다. 아무튼 머리 속에서 상상을 해보면, 개체 간의 거리를 특정한 방법으로 측정하였고, 개체 to 개체 adjacency matrix를 만들었고, 값을 standardization하고, 네트워크를 생성하였습니다
- 이제, 이 네트워크를 쪼개서 n 개 이상의 클러스트로 만들려면 어떻게 해야 할까요? 아마도 가장 간단하게 머리 속에 생각나는 방법은 가장 의미없는 edge를 잘라내는 것이라고 생각됩니다(weight가 작거나, distance가 크거나). 

### 그럼, 어떤 edge들을 잘라야 하나요? 

- 현재의 목적은 n개의 클러스터로 그래프를 쪼개는 것입니다. 음, n개가 아니라 2개라고 하는 것이 우선 좋겠네요(n개 이상으로 쪼갤 때는 2개로 쪼개는 것을 연속으로 해주는 것과 같습니다). **(그래프를 2개의 클러스터로 나누기 위한 수많은 방법)** 중에서 **(잃어버리는 weight가 가장 작은 방법)**을 선택하면 되는 것 같습니다. 
- 아주 간단하게는 node가 3개인 complete 그래프를 쪼개야 한다면, 어떤 edge를 없애야 할까요? edge의 weight를 고려해서 가장 작은 edge 둘을 쪼개면 됩니다. `spectral clustering`은 대략 이런 개념이에요. 

### cut method

- `minimum cut`: 가장 적게 weight를 잃어버리는 방식으로 그래프를 쪼개는 방식. 단, 이 경우, 하나의 클러스터의 크기가 너무 작아질 수 있음. 
- `ratio cut`: 쪼갰을 때 쪼개진 두 클러스터의 크기(노드의 수)가 비슷하게 유지되도록 컷하는 방식
- `minmax cut`: 쪼갰을 때 쪼개진 두 클러스터의 weight 합이 비슷하도록 컷하는 방식


## do it using python 

- 직접 코딩을 할 수도 있긴 합니다만, 싫어용 하하하핫. `sklearn.clustering`에 이미 아주 잘 되어 있기 때문에, 여기 있는 것을 씁니다. 
    - 다만, 왜 `networkx`에는 없는지 모르겠네요. 물론 코딩할 수는 있지만 별로 하고 싶지 않습니다 하하하핫. 

```python
import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt

"""
- radius 리스트를 입력받아서, 각 반지름의 원에 위치하는 n개의 샘플을 뽑아서 x, y 리스트들을 리턴해줍니다. 
"""
def return_circle_xy(rs, n):
    xs, ys = [], []
    for r in rs:
        for i in range(0, n):
            angle = np.pi * np.random.uniform(0, 2)
            xs.append( r*np.cos(angle) + np.random.random())
            ys.append( r*np.sin(angle) + np.random.random())
    return xs, ys

x, y = return_circle_xy([10, 5], 500)
df = pd.DataFrame({"x":x, "y":y})

from sklearn.cluster import SpectralClustering, AgglomerativeClustering

f, axes = plt.subplots(1, 2, sharex=True, sharey=True)
f.set_size_inches((10, 4)) 

# spectral clustering and scattering
CluNums = SpectralClustering(n_clusters=2, n_init=10).fit_predict(df)
axes[0].scatter(x, y, c=CluNums, cmap=plt.cm.rainbow, alpha=0.3)
axes[0].set_title("Spectral Clustering")

# agglomerative clustering and scattering
CluNums = AgglomerativeClustering(n_clusters=2).fit_predict(df)
axes[1].scatter(x, y, c=CluNums, cmap=plt.cm.rainbow, alpha=0.3)
axes[1].set_title("Agglomerative Clustering")

plt.savefig('../../assets/images/markdown_img/spec_agg_clustering_18051202105.svg')
plt.show()
```

- 아래 그림을 보시면, spectral clustering이 aggmolerative clustering에 비해서 훨씬 잘 되는 것을 알 수 있습니다. 결국 클러스터링은 기존 데이터들의 형태, convex or non-convex에 따라서 결과가 달라진다 라고 말할 수 있고요. 

![](/assets/images/markdown_img/spec_agg_clustering_18051202105.svg)

## but 3 circle?? 

- 하지만, 만약 원이 세 개라고 가정하고, 세 개의 원에 대해서 샘플링을 한 다음, 클러스터링을 해보면, 아름답게 나오지 않아요. 원 자체가 끊어져서 나옵니다. 사람 눈으로는 현재 클러스터링에 문제가 있다는 것을 인지할 수 있지만, 컴퓨터는 그렇게 하지 못하네요. 

![](/assets/images/markdown_img/spec_agg_clustering_18051202109.svg)

```python
x, y = return_circle_xy([10, 7, 4], 500)
df = pd.DataFrame({"x":x, "y":y})

from sklearn.cluster import SpectralClustering, AgglomerativeClustering

f, axes = plt.subplots(1, 2, sharex=True, sharey=True)
f.set_size_inches((10, 4)) 

CluNums = SpectralClustering(n_clusters=3, n_init=10).fit_predict(df)
axes[0].scatter(x, y, c=CluNums, cmap=plt.cm.rainbow, alpha=0.3)
axes[0].set_title("Spectral Clustering: cluster_num=3")

CluNums = AgglomerativeClustering(n_clusters=3).fit_predict(df)
axes[1].scatter(x, y, c=CluNums, cmap=plt.cm.rainbow, alpha=0.3)
axes[1].set_title("Agglomerative Clustering: cluster_num=3")

plt.savefig('../../assets/images/markdown_img/spec_agg_clustering_18051202109.svg')
plt.show()
```

- 단, 그 이유는 아마도 distance를 측정해주는 metric을 euclidean으로 세팅해서 그런 것일 가능성이 큽니다. 원과 원 사이에는 데이터들이 거의 없는데(sparse) 이런 경우에는 실제 유클리디안 거리보다 훨씬 멀도록 값을 변화해주면, 이 차이를 구별해낼 수 있을 것 같습니다. 이를 위해서 `mahalanobice distance`가 필요하죠. 
- 찾아보니,` GaussianMixtureModel` 이 거리를 사용한다고 하니, 이걸 사용해보도록 합시다. 

## SpecClustering(nearest_neighbor), GMM


- 결과적으로, Spectral Clustering은 가까운 노드들의 영향을 많이 받도록 바꾸었더니, 좀 괜찮아지지지만, `GMM`은 딱히 달라지는 것 같지는 않습니다. 왜 그런지에 대해서는, 좀 더 공부가 필요할 것 같습니다 흠. 
 
![](/assets/images/markdown_img/spec_agg_clustering_18051202122.svg)

```python
x, y = return_circle_xy([10, 7, 4], 500)
df = pd.DataFrame({"x":x, "y":y})

from sklearn.cluster import SpectralClustering, AgglomerativeClustering
from sklearn.mixture import GaussianMixture

f, axes = plt.subplots(1, 2, sharex=True, sharey=True)
f.set_size_inches((10, 4)) 

CluNums = SpectralClustering(n_clusters=3, affinity='nearest_neighbors', n_init=10).fit_predict(df)
axes[0].scatter(x, y, c=CluNums, cmap=plt.cm.rainbow, alpha=0.3)
axes[0].set_title("spectral clustering, affinity='nearest_neighbors")

CluNums = GaussianMixture(n_components=3, covariance_type='spherical').fit(df).predict(df)
#covariance_type : {‘full’, ‘tied’, ‘diag’, ‘spherical’},
axes[1].scatter(x, y, c=CluNums, cmap=plt.cm.rainbow, alpha=0.3)
axes[1].set_title("GaussianMixture, covaiance_type: spherical")

plt.savefig('../../assets/images/markdown_img/spec_agg_clustering_18051202122.svg')
plt.show()
```


## wrap-up

- spectral clustering은 개체간의 거리를 사용해서 클러스터링을 해줍니다. 여기서, 해당 거리를 어떤 방식으로 측정하느냐, 가 중요한데, 저는 가능하다면, 분포를 고려한 mahalanobice distance가 가장 효과적이지 않을까 싶습니다. 
- spectral clustering은 KMM, AGGClustering에 비해서 특정 데이터 세트에 대해서 잘 워킹하는 것 같아요(원형 분포 등). 
- 찾아보면 자료 중에 클러스터링간을 비교해 놓은 자료들이 많습니다. 요 비교도 나중에 한번 해보면 재밌을 것 같네요. 

## reference 

- <https://ratsgo.github.io/machine%20learning/2017/04/27/spectral/>
- <http://scikit-learn.org/stable/modules/generated/sklearn.cluster.SpectralClustering.html>