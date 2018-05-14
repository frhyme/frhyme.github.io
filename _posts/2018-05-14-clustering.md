---
title: clustering을 해봅시다. 
category: python-lib
tags: python-lib python sklearn clustering

---

## how to cluster 

- 키워드 분석 중. 키워드를 활용해서 키워드 네트워크를 만들었고, 따라서 여기서 adjancency matrix or bi-adjancency matrix를 만들 수 있다. 여기까지는 됐고, 이 말은 다시 말하면, 개별 키워드를 벡터로 표현할 수 있다는 건데, 그렇다면 여기서 차원을 축소하거나, 혹은 clustering을 할 수 있다는 것을 의미함. 
- 따라서, 저는 만들어낸 매트릭스를 가지고 클러스터링을 해보려고 합니다. 또한 t-sne를 통해 2차원 화면에 뿌려서 클러스터링이 잘 되었는지도 확인해보면 좋을 것 같습니다. 


### K-means 

- 가장 간단한 클러스터링 기법이며, 처음에 몇 개의 클러스터로 나눌 것인지를 `argument`로 입력해줘야 합니다. 그 이후, n 개의 중심점을 잡은 다음, 간 군집간의 중심점이 최소화되는 방향으로 클러스터링합니다. 
- 즉, `n_cluster`의 수에 따라 달라집니다. 그래서 적합한 `n_cluster`를 찾는 방법이 중요한데, 이는 inertia value를 사용해서 찾습니다. 
    - 아래 그림을 보면, 대략 inertia의 변화 폭이 대략 4-5사이에서 감소하는 것을 알 수 있습니다. 클러스터를 더 많이 했을 때에 비해서 얻는 이득이 크지 않다고 말할 수 있으므로 4가 적당한 클러스터 수라고 할 수 있겠네요. 
![](/assets/images/markdown_img/kmean_clustering_20180513.svg)

```python
import networkx as nx
import matplotlib.pyplot as plt 
from sklearn import cluster

G = nx.karate_club_graph() # non weight degree 
feature = nx.adj_matrix(G).toarray()

inertias = []
ks = [i for i in range(1, 7)]
for k in ks:
    model = KMeans(n_clusters=k)
    model.fit(feature)
    inertias.append(model.inertia_)
    
# Plot ks vs inertias
plt.plot(ks, inertias, '-o')
plt.xlabel('number of clusters, k')
plt.ylabel('inertia')
plt.xticks(ks)
plt.savefig('../../assets/images/markdown_img/kmean_clustering_20180513.svg')
```

### AgglomerativeClustering

- `Kmeans`의 경우 처음에 몇 개로 나눌 지에 따라서 클러스터링된 결과가 달라지는데, `AgglomerativeClustering`은 그렇지 않습니다. 가장 가까운 node pair를 찾고, 다시 그 node pair 그룹에서 가장 가까운 node를 찾는 식으로 반복하여 dendrogram을 그려줍니다. 따라서, dendrogram을 보고, 적당한 clustering_num을 찾아서 넣어주면 됩니다.
- 아래 코드를 사용해서 그려주면 됩니다. 

![](/assets/images/markdown_img/agg_clustering_20180513.svg)

```python
import matplotlib.pyplot as plt
from sklearn.cluster import AgglomerativeClustering

G = nx.karate_club_graph() # non weight degree 
feature = nx.adj_matrix(G).toarray()

plt.figure(figsize=(15, 5))
nx.draw_networkx(G, nx.spring_layout(G),
    node_color=AgglomerativeClustering(n_clusters=3).fit_predict(feature),
                 cmap=plt.cm.rainbow
)
plt.axis('off')
plt.savefig('../../assets/images/markdown_img/agg_clustering_20180513.svg')
```

## draw dendrogram 

- dendrogram 을 그리는 방법은 다음과 같음. 해당 function은 `sklearn`이 아닌 `scipy`에 있는 것에 유의. 

- dendrogram with ward method

![](/assets/images/markdown_img/ward_dendrogram_20180513.svg)

- dendrogram with jaccard metric 

![](/assets/images/markdown_img/jaccard_dendrogram_20180513.svg)

```python
from scipy.cluster.hierarchy import dendrogram, linkage
from scipy.spatial.distance import euclidean, jaccard

G = nx.karate_club_graph() # non weight degree 
feature = nx.adj_matrix(G).toarray()

"""
method: 
linkage의 경우는 cluster와 가장 가까운 node or cluster를 찾을 때 어떻게 찾는지를 의미한다. 
예를 들어서 cluster 둘을 비교할 때, 가장 가까운 거리를 활용할 수도 있고, 가장 먼 거리를, 평균 거리를 활용할 수도 있다. 
이를 method라고 한다. 'ward'의 경우는 metric이 euclidean으로 고정됨. 
"""
plt.figure(figsize=(16, 8))
dendrogram(
    linkage(feature, method='ward')
    #linkage(feature, metric=jaccard)
)
plt.savefig('../../assets/images/markdown_img/ward_dendrogram_20180513.svg')
plt.show()

plt.figure(figsize=(16, 8))
dendrogram(
    linkage(feature, metric=jaccard), orientation='right'
)
plt.savefig('../../assets/images/markdown_img/jaccard_dendrogram_20180513.svg')
plt.show()
```


## reference

- <http://scikit-learn.org/stable/modules/clustering.html>
- <https://www.learndatasci.com/tutorials/k-means-clustering-algorithms-python-intro/>