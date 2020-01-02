---
title: 야구) 상황에 따른 기대 득점 분포
category: baseball 
tags: baseball sabermetrics RE
---

## scoring distribution 

- [링크의 가운데 표](https://www.fangraphs.com/blogs/more-fun-with-markov-custom-run-expectancies/)를 보면, Base, Out으로 구분된 각 상황부터 이닝 종료까지의 득점 확률 분포를 보여주고 있다. 
    - [여기서](https://gregstoll.dyndns.org/~gregstoll/baseball/runsperinning.html)는 계산도 직접 해줌. 
- 이전에는 마코브 체인을 이용해서, 각 상황에서 이닝 종료까지 얻을 수 있는 Run Expectancy는 구했는데, 위 링크의 테이블처럼, 0점을 얻을 수 있는 확률, 1점을 얻을 수 있는 확률 등으로 표현되지는 않았다. 
    - 상황별로 득점의 확률 분포를 알 수 있다면, 상황에 적합하도록 작전을 활용할 수 있다. 

## 상황별 점수 확률 분포를 어떻게 계산하지? 

- 사실 그냥, 이미 기존 데이터에 매 이닝 별 상황부터 종료까지 취득한 총 득점을 뽑아낼 수 있으므로, 이를 이용해 확률을 계산해주면 된다. 데이터만 있으면, 크게 어려운 것은 아닌 것으로 보임. 
    - 이런걸 모수 추정 비슷하게 말했던 것 같은데 흠...
- 다만, Tom Tango의 경우 이 점수 확률 분포를 마코브체인을 활용해서 했다고 하는데, 마코브체인을 이용해서 계산한 상황별 점수 확률 분포는 아직 관련 포스트를 찾지 못했다. 마코브체인을 어떻게 모델링했는지도 찾지 못하였고. 

## 상황별 점수 확률 분포는 어떤 분포를 따르는가? 

- 단, 마코브체인을 이용하지 않고, 이닝 별 득점 확률 분포는 [negative binomial dist를 따를다고 하고, 해당 분포와 모수를 찾아주는 경우](https://stats.seandolinar.com/mlb-run-distribution-neg-binomial/)는 발견했다. 
    - 이전에 마코브체인으로부터 상황별 Run Expectancy를 찾았고, 이를 모수로, 넘겨주면, discrete 한 득점별 확률 분포가 나올 수 있지 않을까? 하고 생각해보는데.  
    - 또한, 반드시 negative binomial dist를 써야 하는지는 약간 의문이다. 해당 포스트에서는 negative binomial distribution이 더 좋다고 했지만, posission distribution의 경우는 모수를 평균 하나만 넘겨주면 되기 때문에, 마코브체인에서 계산한 상황별 Run Expectancy를 그대로 넣어주면 되서, 더 편한 것 같음. 

## 실제로 돌려봅시다. 

- MLB 1998 - 2002 까지의 실제 데이터를 활용해 계산한 Run Expectancy 값을 활용하여, 득점별 poission distribution을 구하고 그림으로 그려주었습니다. 
    - 사실, [다른 블로그](https://gregstoll.dyndns.org/~gregstoll/baseball/runsperinning.html#about)에서 계산해준 득점 확률 분포와는 흐름은 비슷하지만, 정점이 달라요. 예를 들어서 무사 3루에서 1득점이 나올 확률이 저의 경우 30% 대라면, 저 블로그에서는 50%이상. 
    - 하지만, 귀찮으니까요 저는 더 안합니다. 이렇게~~하는거다 만 알고 나중에 심심할 때 다시할래여 헤헤 

![poission dist, pmf](/assets/images/markdown_img/poisson_dist_pmf_180528.svg)

![poission dist, cdf](/assets/images/markdown_img/poisson_dist_cdf_180528.svg)

```python
import matplotlib.pyplot as plt 
from scipy.stats import poisson

plt.figure(figsize=(12, 6))
for mu in [0.555, 1.189, 1.573, 2.052, 2.417]:    
    x = [i for i in range(0, 11)]
    y = [poisson.pmf(xx, mu) for xx in x]
    plt.plot(x, y, marker='o', linestyle='--', label='mu={}'.format(mu))
plt.legend(loc='upper right', frameon=True, fontsize='x-large')
plt.xticks([i for i in range(0, 11)])
plt.yticks([i*0.1 for i in range(0, 7)])
plt.savefig('../../assets/images/markdown_img/poisson_dist_pmf_180528.svg')
plt.show()

plt.figure(figsize=(12, 6))
for mu in [0.555, 1.189, 1.573, 2.052, 2.417]:    
    x = [i for i in range(0, 11)]
    y = [poisson.cdf(xx, mu) for xx in x]
    plt.plot(x, y, marker='o', linestyle='--', label='mu={}'.format(mu))
plt.legend(loc='lower right', frameon=True, fontsize='x-large')
plt.xticks([i for i in range(0, 11)])
plt.yticks([i*0.1 for i in range(0, 11)])
plt.savefig('../../assets/images/markdown_img/poisson_dist_cdf_180528.svg')
plt.show()
```

## wrap-up 

- 데이터들이 어떤 분포를 가지는 지, 추정하는 것이 매우 중요함. 그리고 어떤 분포를 가진다고 가정했다면, '모수', 평균 등 을 어떻게 도출할 것인가 도 매우 중요하고.
    - 내 기억이 맞다면 아마도 이런 내용을 패턴인식개론에서 다루었던 것 같은데, 내가 공부를 제대로 안했으니 헤헤헤. 
- 아무튼, 이 득점 분포를 활용하면, 현재 상대방과 나의 득점 차를 고려하여 효율적인 작전 수행을 할 수 있습니다. 
    - 만약 전체 리그 데이터로부터 모수를 추정하여 보니, 대부분의 경우 1점을 내는 것도 어렵다 => 스몰볼, 적극적인 번트 야구 
    - 대부분의 경우 점수를 많이 내더라 => 빅볼 ㄱㄱ