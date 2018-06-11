---
title: RNN을 사용해봅시다. 
category: machin-learning
tags: python neural-network python-lib RNN
---

## RNN을 사용해보려고 합니다. 

- CNN은 이제 대충 써볼 수 있는데, RNN을 몰라요. 공부합시다!
- 간단하게, RNN을 이용하면, sequential data의 흐름을 예측할 수 있습니다. sequential data에 속하는 것들로는 주식, 글, 말 등이 있겠네요. 아주 간단하게는 연속된 데이터의 흐름이 바로 앞의 데이터에 영향을 많이 받는다면, 그것을 sequential data라고 할 수 있습니다. 
- 다르게 표현하면, 어떤 시점의 값을 예측하기 위해서, 바로 앞의 놈, 바로 앞의 앞의 놈, 바로 앞의 앞의 놈들을 feature로 사용하는 것이라고 할 수 있겠네요. 어떻게 생각하면, 그냥 regression의 일종으로 생각되기도 합니다. 



## wrap-up 

## reference

- <https://github.com/jskDr/keraspp>
- <http://adventuresinmachinelearning.com/keras-lstm-tutorial/>