---
title: R처럼 python에서도 pipeline을 사용합시다. 
category: python-lib
tags: python python-lib sklearn pipeline

---

## sklearn - pipeline 사용하기 

- R을 사용해보신 적이 있는 분들은 알겠지만, R은 `%>%`을 사용해서, pipeline을 구성할 수 있습니다(제가 R을 별로 좋아하지는 않는데, 이거 하나는 굉장히 좋아합니다). machine-learning이라는 것은 data가 지나가는 흐름을 만드는 것인데, 사실 비슷비슷한 작업을 반복해서 합니다. scaling을 하고, 이 모델에 넣어보거나, 저 모델에 넣어보거나 하는 식으로. 
- 이러한 작업을 좀 더 수월하게 할 수 없을까 생각합니다. 그래서 python에 pipeline이 없나 찾아봤는데, 있습니다 있어요!!
- 원활한 작업을 위해서는 pipeline과 mapt을 적절하게 사용하는 작업이 필요합니다. 필요하면 같이 이용하는 것도 좋구요. 

## 하지만. 

- 뭘 좀 해보려는데, 생각보다 오류가 아주 많이 발생합니다. component 별로 input, output이 다를 수 있고, 등등 문제가 있기 때문에 그냥 필요하다면, pipeline을 쓰지 않고, 직접 function을 만들어서 하는 게 더 효율적인 것 같습니다. 필요없어요. 

## reference
- 

