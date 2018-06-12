---
title: RNN을 사용해봅시다. 
category: machin-learning
tags: python neural-network python-lib RNN
---

## RNN을 사용해보려고 합니다. 

- CNN은 이제 대충 써볼 수 있는데, RNN을 몰라요. 공부합시다!
- 간단하게, RNN을 이용하면, sequential data의 흐름을 예측할 수 있습니다. sequential data에 속하는 것들로는 주식, 글, 말 등이 있겠네요. 아주 간단하게는 연속된 데이터의 흐름이 바로 앞의 데이터에 영향을 많이 받는다면, 그것을 sequential data라고 할 수 있습니다. 
- 다르게 표현하면, 어떤 시점의 값을 예측하기 위해서, 바로 앞의 놈, 바로 앞의 앞의 놈, 바로 앞의 앞의 놈들을 feature로 사용하는 것이라고 할 수 있겠네요. 어떻게 생각하면, 그냥 regression의 일종으로 생각되기도 합니다. 

## what is LSTM network

- LSTM network는 Long and Short Term Memory Network의 약자입니다. 개별 neuron으로 네트워크를 만드는 것이 아니라, neuron으로 만들어낸 새로운 component 를 활용하여 network를 구성하는 경우를 말합니다. 이 component는 말 그대로, short term context와 long term context를 모두 활용할 수 있는 형태로 사용됩니다. 
- 개별 component unit 내부에는 다음 세 가지 종류의 gate들이 다시 포함되어 있습니다. 
    - Forget gate: 조건에 따라서 어떤 정보를 버릴지 결정
    - Input gate: 조건에 따라서 어떤 정보를 내부로 가져올지 결정
    - Output gate: 조건에 따라서 어떤 정보를 외부로 가져갈지 결정
- 뭐....저는 멍청하기 때문에 그냥 그대로 따라하면서 잘 되는지 안되는지 활용하겠습니다 하하하하하핫

## wrap-up 

- stateful 과, non-stateful의 차이는 무엇인가? 
- 근데, 이렇게 간단한 값을 regression하는 경우에, rnndl randomforestregresor같은 것 보다 더 낫다고 할 수 있나? 

## reference

- <https://machinelearningmastery.com/time-series-prediction-lstm-recurrent-neural-networks-python-keras/>