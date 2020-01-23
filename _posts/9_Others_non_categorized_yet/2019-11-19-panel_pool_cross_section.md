---
title: Panel, Pooled, Cross-sectional Data
category: others
tags: data statistics
---

## intro

- 요즘 통계 좀 개념들을 좀 사용해야 하는데, pooled data, panel data등이 좀 헷갈리더라구요. 그래서 생각난 김에 그냥 정리를 하기로 했습니다. 
- 내용은 모두 위키피디아를 기본으로 하구요. 

### panel data

- 내용은 [여기에서](https://en.wikipedia.org/wiki/Panel_data) 가져왔으며, panel data, longigudinal data라고도 합니다. 
- 사실 하나의 개체(회사, 개인 등)에 대해서 단 한 번의 측정만으로 정확한 값을 가져오는 것은 어렵죠. 따라서, 하나의 개체에 대해서 여러 번 반복적으로 측정하는 것이 필요합니다. 이와 같은 것을 보통 panel data라고 하죠.
- 즉 '시간'이라는 하나의 축과 '여러 개체'라는 또 다른 축으로 구성됩니다. 칼럼에는 개체명이, 행이름에는 시간이 써있다고 생각하시면 되겠네요.  

### time-series data

- 시간의 변화가 담겨 있는 데이터라는 말이죠. panel data 자체가 대상을 오랜 기간동안 추적하여 데이터를 수집했다는 것이 됩니다. 즉, 이를 통해서 시간의 변화도 파악할 수 있는 것인데, 보통 특정 개체만을 대상으로 그 데이터가 가진 값의 시간적 변화 등을 보려고 하는 경우를 보통 time-series data라고 합니다.

### cross-sectional data

- 특정 시점에 대한 데이터, 즉, n명을 대상으로 같은 설문을 일정 기간동안 m번 반복했을 때, 어떤 기간동안의 데이터만 따로 뽑아서 본다면 보통 이런것이 crosse-sectional data가 됩니다.
- 앞서 말한 바와 같이, panel data는 '시간'이라는 축과 '독립된 개체'를 통합한 테이블을 의미하는데, 여기서, '시간'에 집중하지 않고, '개체들'이 어떻게 구성되어 있는지를 보는 것을 말하죠. 

## example 

- 가령, 정부에서, 전국의 비만도를 측정하기 위해서, 20세 모든 사람들의 몸무게, 키를 1년동안 매월 측정했다고 합시다. 
- 이렇게 모인 데이터는 하나의 개체에 대해서 반복적으로 측정하여, 시간의 변화를 담고 있으며, 다양한 개체에 대한 것도 반응하고 있으므로, 이를 panel data라고 할 수 있습니다. 
- 만약, 이를 특정 시간대로 줄여서, 어떤 시점의 모든 사람들에 대한 데이터를 본다면 이건 cross-sectional data가 되고, 
- 충청도에 사는 사람들의 시간의 변화 데이터로 변경한다면, 이는 time-series data가 되겠죠. 

## pooled data vs. panel data

- 사실 가장 헷갈리는 것이 바로 pooled data입니다. 이건 아마도, panel data와 panel study가 혼재되어 있어서 그런 것일 수도 있어요. 
- 저는 [Reed colledge의 자료](https://www.reed.edu/economics/parker/s11/312/notes/Notes13.pdf)를 참고했습니다. 

> Panel data refers to samples of the same cross-sectional units observed at multiple points in time. A panel-data observation has two dimensions: x_it, where i runs from 1 to N and denotes the cross-sectional unit and t runs from 1 to T and denotes the time of the observation.
- Panel data는 같은 시간대에 관측된 같은 cross-sectional unit의 샘플을 가리킵니다. 패널 데이터는 '어떤 크로섹션에 속하는지'와 '어떤 시간대에 관측되었는지'ㅏ는 두 가지 차원을 가지게 되죠. 

> Pooled data occur when we have a “time series of cross sections,” but the observations in each cross section do not necessarily refer to the same unit.
- Pooled data는 '크로스 섹션의 시계열'이라고 말해집니다. 즉, 각 크로스 섹션들이 시계열 데이터를 가지고 있을 때를 말하죠. 하지만, 이 크로스 섹션에서의 관측된 것이, 같은 unit인 것을 가리키지는 않습니다. 인데, 사실상, Pooled data와 Panel data는 서로 혼재되어서 쓰이고 있다고 해도 상관없을 것 같아요. 

## conclusion

- 그냥 하나의 테이블을 생각합시다. 행은 시간에 따라서 구분되고, 열은 각 개체에 따라서 구분되죠(가령, 사람, 단체 등)
- 시간을 구분해서 보느냐, 개체를 구분해서 보느냐, 모두 보느냐 등은 서로 다르고, 이를 표현하기 위해서 사용하는 것이 이와 같은 데이터에 대한 구분이 아닐까 싶습니다.
- 이게 중요한 건, 일종의 'concept drift'때문인 것이죠. 우리가 관측하는 대상은 계속 바뀝니다. 올해의 우리의 생각이나 선호가 내일의 우리와 같지 않을 수 있으니까요. 따라서, 그 두 가지를 서로 다른 데이터로 구분해서 서로 다른 모델을 세우거나, 그 둘을 구분해서 그 차이를 하나의 변수로 새롭게 넣어서 모델을 세울 수 있습니다. 
- 즉, panel data를 잘 나누어서, 그런 모델을 세우고, 학습을 시켜야 한다 뭐 그런 이야기가 아닐까 싶어요. 