---
title: paper-summary, Monitoring Newly Adopted Technologies Using Keyword Based Analysis of Cited Patents
category: paper-summary
tags: paper-summary patent 
---

## Monitoring Newly Adopted Technologies Using Keyword Based Analysis of Cited Patents

- IEEE access에 2017년에 게재된 논문 
- [link](https://ieeexplore.ieee.org/document/8085383)

## summary 

- adoption of existing technology(기존 기술의 도입?)에 대한 모니터링을 할 수 있는 방법론으로, 특허에 대해서 TF-IDF와 K-means clustering 방법을 사용하여 방법론을 구성함. 
- TF-IDF와 클러스터링 기법은 충분히 많은 특허 데이터로부터 특허 정보를 뽑아낼 수 있도록 사용됨. 
    - 그러나, 특허의 수가 적을 때는 이 방법론의 결과를 신뢰할 수 있다고 하기 어려움.
    - 따라서, 수집한 patent set이 인용하는 다른 patent 정보를 함께 활용하는 방법론을 제시함. 
- 이렇게, 기존 특허 데이터와 기존 특서 데이터가 인용한 데이터를 활용하여 분석을 수행함. 
- 케이스 스터디에서, 무인 자동차(automated driving)가 적용되었을 때, 농기계(agricultural tractor)에 대해서 수행함. 
- 기존의 방식(데이터가 적을 때)는 실패했지만, 데이터가 많을 때는 충분히 잘 적용되었다. 
- 따라서, 본 방법은 patent monitoring 측면에서 데이터가 적을 때도 충분히 괜찮게 작동하는 것 같다. 


## insight 

- 데이터 수집 측면에서 타겟 특허의 수가 너무 적기 때문에, 해당 특허들이 인용한 다른 특허 데이터를 함께 사용함. 
- TF-IDF로 Document-Term의 매트릭스를 구성하고, 클러스터링을 수행함. 
- 그리고 adopted new technology의 경우는 구별된 새로운 클러스터가 발생했을 때를 말하는 것 같음. 이건 약간 해석에 가까운 것 같기도 하고.
- 결론적으로 특허를 이용하여 특정한 패턴을 발견할 수 있다는 것을 하나의 방법론으로서 제시했다는 것이 유의미함. 
- 1) 타겟 필드를 정하고, 2) 타겟 필드에서 필요로 하는 기능을 서술하고, 3) 대단히 뛰어난 기술은 아니지만, TF-IDF, clustering의 기법을 이용하였고, 4) 현재 방법론의 유용성을 앞서 말한 다른 기술들과의 차이점을 들어서 설명함 이렇게 구성되었다는 점에서 유용한 논문이라고 생각됨.