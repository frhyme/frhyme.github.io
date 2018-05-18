---
title: spectral clustering에 대해서 정리해보겠습니다. 
category: data-science
tags: data-science python python-lib clustering not-yet

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

### scaling

- 혹시나 해서 말하지만, 값들이 표준화되어 있지 않을 수 있습니다. 만약 해당 network의 weight가 '빈도'라면 이 값들이 널뛸텐데, minmaxscaling도 좋지만, gaussian kernel을 이용해서 normalization해주는 것이 더 적합할 것 같습니다. 


## anyway, cut and cut



- 머릿 속에 상상을 해보면, 대략 개체간의 거리를 측정할 수 있는 네트워크를 그렸습니다. 어떤 놈은 값이 크고(거리가 멀고), 어떤 놈은 값이 작고(거리가 가깝고) 일텐데, 이 네트워크로부터 예를 들어, 2개의 서브클러스터를 만들어내려면 어떻게 하면 좋을까요/ 

## cut and cut

## reference 

- <https://ratsgo.github.io/machine%20learning/2017/04/27/spectral/>