---
title: distance를 비교해봅시다. 
category: python-lib scipy 
tags: python metric distance 

---

## 비슷한가 안 비슷한가!

- 데이터 분석을 하거나 해야할 때, 많이 쓰이는 measure 중 하나는 similarity(distance)라고 할 수 있습니다. 이 아이들은 비슷한가? 비슷하면 얼마나 비슷한가? 는 항상 직관적으로 궁금해지는 부분입니다. 
    - similarity와 distance는 서로 역수의 관계라고 생각하셔도 무방할 것 같은데요, similarity의 경우는 `range(-1,1)`라고 생각하면 됩니다. 완전히 같으면 1을 완전히 다르면 0을 가진다고 보면 됩니다. 약간 회귀분석(regression)에서 `r-square`와 비슷한 느낌이라고 생각하시면 될것 같습니다. 
    - distance는 사실 `range`가 따로 있지는 않습니다. 따라서 sample이 n개 가 있다면, n(n-1)/2 의 거리에 대해서 표준화를 진행하는 것이 필요합니다. 그냥 간단하게는 minmaxscaling을 해도 되는데, 이렇게만 해도 될까요? 흐음, 좀 크리어하지는 않군요. 
- 아무튼 예를 들어서 clustering을 해야 할때, 이 아이들의 거리는 어느 정도 떨어져 있다고 생각해야하나? 그 거리를 측정하는 방식에 따라서 cluster 들의 구성은 달라지게 됩니다.
- 우리가 고등학교 수학때 배운 일반적인 distance 측정은 `euclidean`방식입니다. 여전히 이게 많이 쓰이고 있기는 하지만, 다른 distance과의 차이점들이 있죠. 

### Euclidean distance

- 일반적인 두 점간의 직선거리를 측정한다.
- 
#### code


### Manhattan distance

- `manhattan distance`의 경우는 직선거리가 아닌 차원별 차이를 따로 측정해서 그 합을 계산한다고 보면 된다. 막힌 곳이 없는 평지에서는 `euclidean distance`가 의미가 있지만, `manhattan`처럼 건물이 많은 곳에서는 직선거리가 아닌 가로와 세로의 각각의 합이 더 정확한 거리를 의미할 수 있다. 
- 
### Minkowski distance

- generalized form of `Euclidean distance` and `manhattan distance`


### cosine distance

- 이는 두 벡터간의 실질적인 좌표간의 거리보다는 angle 차이를 본다. 만약 이 두 벡터가 `orthogonal`하다면 이 측정값은 0이 되고, 같은 방향을 가리킨다면 1이 된다. 반대로 반대 방향을 가리킨다면 -1이 된다. 

### jaccard distance

- `jaccard distance`의 경우는 서로 다른 fininite 한 set에 대해서 사용될 수 있다. 서로 다른 두 object가 만들 수 있는 union의 개수 대비 intersection이 얼마나 있는지를 사용해 그 유사도를 측정한다. 
- 이전의 distance들이 numeric vector 를 대상으로 했다면, 이 distance의 경우는 boolean vector를 대상으로 한다고 할 수 있다. 
- intersection / union 

## reference 

- http://dataaspirant.com/2015/04/11/five-most-popular-similarity-measures-implementation-in-python/
- https://docs.scipy.org/doc/scipy/reference/spatial.distance.html