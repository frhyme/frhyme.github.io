---
title: 클러스터링을 다시 공부해봅시다. 
category: python-lib
tags: python python-lib clustering matplotlit sklearn tsne silhouette_score

---

## 클러스터링을 다시 공부합니다. 

- unsupervised learning인 클러스터링은 쉽게 생각하면, 비슷한 놈들끼리 묶어 준다는 이야기가 됩니다. 우선, '비슷한'을 정의해야 하는데, 개별 instance가 numerical vector로 표현된다고 하면, 그 값들간의 거리를 측정할 수 있겠죠(물론 이 거리를 측정하는 방법도 아주 다양합니다). 우선, 서로 다른 인스턴스간의 거리를 어떻게 계산할지를 정해야 합니다. 
- 정한 다음에는 이들을 묶어줘야 겠죠. 다양한 방식이 있습니다만, 다음과 같은 분류가 있다고 합니다. 
    - **hard clustering** : 한 개체가 하나의 분류에만 속할 수 있는 경우 
    - **soft clustering** : 한 개체가 여러 분류에 속할 수 있는 경우 
    - **patitional clustering** : 전체 개체를 한번에 군집화하는 방법입니다. 쉽게 설명하려면 반대를 설명하면 좋은데, hierarchical clustering의 경우는 가까운 집단부터 하나씩 묶어 나가는 반면, partitional clustering은 기준에 의해서 연속으로 여러 개체를 구분할 수 있습니다. 일반적인 **K-means**를 이 방법에 속한다고 할 수 있구요. 
    - **hiarchical clustering** : 개체들을 가까운 놈들부터 묶어 나갑니다. n개가 있으면 n*n의 거리를 잰 다음, 가까운 놈들부터 하나씩 하나의 집단으로 묶어 줍니다. 이 과정에서 Dendrogram이 생성되며, 덴드로그램을 확인하여 적당하다고 생각되는 clustering의 수를 확인할 수도 있습니다. 
    - **Self-Organizing Map** : 뉴럴넷 기반의 군집화 알고리즘이라고 하는데, 이건 제가 모르는 내용이라서, 나중에 공부해서 다시 정리해보겠습니다. 
    - **Spectual clustering** : 그래프 기반의 군집화 방법론이라는데, 이것도 제가 잘 모르는 내용이라서 나중에 정리해서 한번 해보도록 하겠습니다. 

## clustering 하고 evaluation 하기

- 파이썬의 sklearn덕분에 삶이 편해졌지만, 이제 어려운 것은 '그래서 이게 잘 된거야 안된거야'를 평가하는 것이죠. 이건 아직 인간이 해줘야 하는 부분이거든요. '오버피팅이야 언더피팅이야 뭐가 어떻게 되는거야'는 거죠. 무한의 굴레. 
    - 된다 ==> 왜 되는거지?
    - 안된다 ==> 왜 안되는거지? 
- 어쨌거나, 클러스터링이 잘 된건가, 안된건가, 적합한 클러스터링의 수는 몇 개인가 등을 파악해보려고 합니다. 
- 네, 그래서, 분류까지 완료한 다음에, 이 아이들이 정말 분류가 잘 되었구나! 를 어떻게 파악할 수 있을까요? 그 지표도 다음과 같은 지표들이 있습니다.

### Dunn index

- 표준화된 값이라고 할 수는 없지만, 만약 이 값이 1이상이라면, **가장 작은 클러스터 간의 거리**가 **클러스터 내의 가장 먼 거리**보다 길다고 할 수 있으므로 꽤 잘된 클러스터라고 할 수 있겠네요. 
    - 분자: 클러스터링 간 거리들 중 최소값 
    - 분모: 클러스터링 내 개체 간 거리의 최대값
- 단, 여기서 남아있는 문제라면, '거리'를 어떻게 측정하는 것이 좋은가? 이겠죠. '유클리디안'인가, '자카드'인가 등이 이슈가 될 수 있습니다. 

### Silhouette

- `Dunn index`의 경우는 클러스터링의 유효성을 검증하기 위한 하나의 값이 있는데, `Silhoutte`의 경우는 개체별로 그 적합성이 평가됩니다. 즉, 모든 개체의 `Silhoutte`값을 확인하고, 클러스터별로 그 값의 분포에 문제가 없는지 확인하는 방식으로, 해당 클러스터의 유효성이 검증됩니다. 

- s(i) = (b(i)−a(i)) / max{a(i),b(i)}
    - a(i) = i 개체와 같은 군집에 속한 요소들 간 거리들의 평균입니다,
    - b(i) = i 개체와 다른 군집 내 개체들간의 거리를 군집별로 구하고, 이중 가장 작은 값

- 개체별로 (가장 가까운 외부와의 거리 - 평균적인 내부와의 거리 ) / (외부와의 거리와 내부와의 거리 중 큰 놈 )을 계산합니다. 
- 당연하지만, 해당 개체와 내부와의 거리가 짧을수록, 해당 개체와 외부와의 거리가 길수록 s(i)는 커집니다. 
- 또한 당연하지만, 해당 개체와 내부와의 거리 > 해당 개체와 외부와의 거리가 이면, 분자가 -가 됩니다. 

- **일반적으로는 모든 개체의 silhoutte 값이 0.5보다 크면, 클러스터링이 잘 된거라고 평가한다고 합니다.**


## do it by test example 

- `dunn index`의 경우는 `sklearn`에 있는 것 같지 않고, 검색해보니 `silhouette`만 나오는 것 같네요. 둘 다 계산법은 복잡하지 않으니 직접 할 수도 있겠지만, 귀찮기 때문에 있는걸 씁니다 하하핫. 


## silhouette score

- `silhouette score`의 경우는 개별 개체에 대해서 값을 도출할 수 있습니다. sklearn은 각 sample에 대해서 계산할 수 있게도 하고, 평균 값을 내는 것도 지원함. 
- 우선 노멀 분포에 따라서 랜덤한 어레이를 만들어주고, 클러스터링한 결과를 scatter하여 뿌려준다. 그리고 각 결과마다 `silhouete score`가 어떻게 변화하는지를 정리하였다. 
- 그림에서 보는 것처럼, 두 집단이 멀리 있을 수록 해당 스코어는 1과 가까워지는 것을 알 수 있다. 

```python
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import AgglomerativeClustering

def make_n_dim_norm_array(dim=2, sample_size=100, mu1=1, mu2=5):
    xy1 = np.array([np.random.normal(mu1, 1, sample_size)]*dim) # shape: 
    xy2 = np.array([np.random.normal(mu2, 1, sample_size)]*dim)
    xy = [xy1, xy2]
    """
    horizontally stack: 현재 xy는 2 by 10의 리스트가 row로 쌓여있는 형태임. 
    이를 hstack(horizontally stack)해주면, 수평선 방향으로 쌓아준다는 것이니까, 
    xy1 의 오른쪽에 xy2가 붙는다고 생각하면 됨. 따라서 2*10 + 2*10 이므로 2*20이 됨. 
    """
    xy = np.hstack(xy)# shape: 2*20 
    """
    그 다음 shape을 바꿔서 각 row에 xy가 있도록 변경
    """
    xy = xy.reshape(sample_size*2, dim) 
    return xy

from sklearn.metrics import silhouette_score, silhouette_samples
from sklearn.decomposition import PCA
from sklearn.manifold import TSNE

f, axes = plt.subplots(1, 5, sharex=True, sharey=True)
f.set_size_inches(15, 3)
for i, ax in enumerate(axes):
    xy = make_n_dim_norm_array(dim=5, sample_size=500, mu1=1, mu2 = 2+i*5)
    cluster_nums = AgglomerativeClustering(n_clusters=2).fit_predict(xy)
    sil_score = silhouette_score(xy, cluster_nums, metric='euclidean')
    # [‘cityblock’, ‘cosine’, ‘euclidean’, ‘l1’, ‘l2’, ‘manhattan’]
    n_xy = PCA(n_components=2).fit_transform(xy)
    #n_xy = TSNE(n_components=2).fit_transform(xy)# tsnes는 너무너무너무 오래 걸림. 
    ax.scatter(n_xy[:, 0], n_xy[:, 1], c=cluster_nums, alpha=0.2, cmap=plt.cm.rainbow)
    ax.set_title("silhouette_score: {}".format(round(sil_score, 2)))
plt.savefig('../../assets/images/markdown_img/silhouette_20180517.svg')
plt.show()
```

![](/assets/images/markdown_img/silhouette_20180517.svg)

## silhouette samples 

- 평균만으로는 숨겨지는 부분들이 있으므로 그 분포를 보다 정확하게 보려고 한다. 
- 이를 위해서 실제 데이터는 너무도 명확하게 cluster가 두 개인 것을 육안으로 확인이 가능하지만, clustering을 세 집단으로 해본다. 
- 결과를 확인하고, 너무 작은 값들이 많지 않은지 확인하는 것이 필요하다. 

```python
from sklearn.metrics import silhouette_score, silhouette_samples

f, axes = plt.subplots(1, 5, sharex=True, sharey=True)
f.set_size_inches(15, 3)
for i, ax in enumerate(axes):
    xy = make_n_dim_norm_array(dim=5, sample_size=500, mu1=1, mu2 = 1+i*2)
    cluster_nums = AgglomerativeClustering(n_clusters=3).fit_predict(xy)
    sil_samples = silhouette_samples(xy, cluster_nums, metric='euclidean')
    sil_score = silhouette_score(xy, cluster_nums, metric='euclidean')
    ax.plot(sorted(sil_samples), color='red',linestyle='dashed', linewidth=2)
    ax.set_title("silhouette_score: {}".format(round(sil_score, 2)))
plt.savefig('../../assets/images/markdown_img/sil_samples_20180517_clus3.svg')
plt.show()
```

- 아래 그림에서 보는 것처럼, 분포가 중간에 급변하는 구간이 생기며, 실루엣 값이 작은 경우가 많은 것을 알 수 있다. 따라서 이런 경우에는 cluster의 수가 적합하지 않음을 도출해낼 수 있다. 

![](/assets/images/markdown_img/sil_samples_20180517_clus3.svg)


## reference

- <https://ratsgo.github.io/machine%20learning/2017/04/16/clustering/>
- <http://blog.naver.com/PostView.nhn?blogId=samsjang&logNo=221017639342&categoryNo=0&parentCategoryNo=0&viewDate=&currentPage=1&postListTopCurrentPage=1&from=postView>
- <http://blog.naver.com/PostView.nhn?blogId=samsjang&logNo=221017639342&categoryNo=0&parentCategoryNo=0&viewDate=&currentPage=1&postListTopCurrentPage=1&from=postView>
- <http://scikit-learn.org/stable/modules/generated/sklearn.metrics.silhouette_score.html>