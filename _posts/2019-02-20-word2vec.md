---
title: word2vec을 다시 정리합니다 
category: others
tags: machine-learning word2vec word-embedding feature-representation 
---

## word2vec

- word2vec은 말 그대로 word를 vector로 표현해주는 것입니다. 간단하게는 feature representation이라고도 할 수 있습니다. 
- 이 측면에서 보면, 전체 document set에서 특정 word가 등장한 횟수를 기반으로 word-document Term-Frequency vector를 만든 것도 하나의 word2vec 방법이라고 할 수 있습니다. smooting을 하거나, 등장 유무 만으로 1, 0으로 값을 지정하거나 하는 것도 모두 word2vec의 방법 중 하나라고 할 수 있겠네요. 
- 즉, 원하려는 대상, 즉 텍스트의 경우 수치적으로 나타나지 않기 때문에 이를 수치적으로 변형해야 다른 방법론들과 연결할 수 있기 때문에 텍스트를 수치로 변형해서 진행하게 됩니다. 여기서, 변형된 feature representation이 기존의 데이터에서 정보의 손실 없이 얼마나 많은 정보를 담고 있느냐, 혹은 우리가 분석을 원하는 방향에 맞는 정보를 담고 있는지가 중요해집니다. 

## word feature representation: sparse or dense

- 앞서 말한 바와 같이 다양한 방식으로 vector로 표현할 수 있으나, 그 과정에서 간단히 위와 sparse한가, dense한가로 정보를 나누어서 처리할 수 있습니다. 흔히 말하는 one-hot encoding은 sparse representation에 속한다고 할 수 있구요. 
- 주성분 분석, 혹은 PCA라는 스킬에 대해서 들어보셨다면, 이제 말한 dense라는 개념이 좀더 친숙하게 다가올 수 있습니다. sparse하게 모인 정보는 각 column 혹은 attribute의 정보가 분절적이죠. 서로 연결된 attribute는 섞어서 새로운 특성으로 만들 수 있습니다. 이런 것들이 바로 새로운 attribute가 될 수 있죠. 
- 경우에 따라서 누군가는 sparse나, dense나 모두 정보를 담고 있다는 측면에서 큰 차이가 없지 않냐? 라고 말씀하실지도 모릅니다. 그런데 머신러닝 모델로 학습을 시킬 때 지나치게 column이 많은 데이터, 또한 0이 가득 있는 sparse한 정보를 그대로 넘기게 될 경우 학습이 잘 안되는 문제가 있습니다. 유식한 말로는 curse of dimensionality라고 하는데요. signal과 noise를 제대로 제거하지 못할 수 있는 문제가 발생합니다.
- '빅데이터', '빅데이터'라고 말하니까 많은 사람들은 특성이 많으면 일단 어떻게든 학습이 되는 것 아닐까? 라고들 말합니다. 음, 뭐 물론 뉴럴넷을 돌리면 학습이 엄청 느려지기는 하겠지만, PCA와 비슷한 부분을 진행해주기 때문에 커버가 될 것 같기는 합니다만, 그리고 랜덤포레스트를 돌리면 또 알아서 해줄 것 같기는 한데 아무튼, 무작정 칼럼을 때려박고 돌리는 것보다는 가장 영향을 미칠 것 같은 칼럼을 하나씩 정해서 늘려가면서 학습을 시키는 것이 훨씬 효율적입니다. generalization 측면에서도 이게 더 효율적이구요. 

## word2vec: how 2 represent word?

- 아무튼 그런 측면에서 word2vec은 dense representation에 속하는 방법론입니다. 단어의 정보를 단지 횟수와 같은 정보가 아니라 semantic information까지 포함하여 vector로 표현하는 방식이죠. word2vec말고도 glove도 있지만, 보통 word2vec이 제일 유명하기 때문에 'word2vec 방법론 집단'정도로 묶어서 생각하는 일이 많은 것 같습니다. 
    - 제가 종종 사용하는 모듈인 spacy의 경우 glove로 만들어진 벡터를 주로 사용하죠.
- word2vec와 glove는 방식이 조금 다르지만, 기본적인 것은 뉴럴넷을 사용해서 word의 vector정보를 뽑아낸다는 것은 동일합니다. 

- 그런데, 뉴럴넷으로 학습시킨다고 하면 정해져야 하는 것은 다음과 같죠. 
    - input으로 들어오는 data는 무엇인가?(training set)
    - input data로 예측하려고 하는 것은 무엇인가? 혹은 objective function은 무엇인가. 
    - backpropagation을 통해서 업데이트 되는 weight는 무엇을 의미하는가? 
- image classification 과 같은 문제에서는 보통 뉴럴넷이 다음처럼 설계됩니다. 
    - input으로 들어오는 데이터는 image의 각 픽셀에 존재하는 값들
    - input으로 들어온 데이터를 활용해서 예측한 value와 실제 value와의 차이(뭐 다양한 방법으로 objective function을 설정할 수 있죠)
    - input에 곱해지는 값들이 weight이 되죠. 
- 그런데, word2vec에서는 이게 어떠한 방식으로 되는지에 대해서 제가 헷갈려서 이 글을 쓰게 되었습니다. 

### structural equivalence

- network theory에서는 structural equivalence라는 개념이 있습니다. 한국말로 구조적 등위성이라고 표현할 수 있으며 같은 위치에 있는 node의 경우 비슷한 의미 혹은 역할을 가지게 된다는 것이죠.
- 텍스트에서도 비슷합니다. 텍스트에서 반복적으로 비슷한 위치에 워드 A, 워드 B가 위치한다면 워드 A, B는 비슷한 의미를 가질 것이라고 유추할 수 있는 것이죠. 
- 이는 다시 CBOW 모델과 skig-gram 모델로 구분할 수 있습니다. 

### CBOW 모델 vs skip-gram 모델 

- CBOW 모델은 Continuous Bag of Word 모델을 말합니다. 맥락으로 단어를 예측하는 방식으로, 이는 input은 해당 단어의 주위 친구들, 즉 맥락이 되고, output은 해당 단어가 되죠. 
    - 앞 뒤 몇 단계의 친구들까지 볼지는 window size라고 표현되죠. 
- skip-gram의 경우는 반대로 단어로 맥락을 예측하는 방식을 말합니다. 비슷한 방식으로 보이지만 정반대의 방식이죠. 
- 비슷한 방식이지만, 실험적으로 skip-gram이 CBOW에 비해서 더 좋은 성능을 가진다고 합니다.

### 그래서 뭐가 input이고 뭐가 output인가? 

- CBOW 방식이라고 생각하고보면, 맥락을 의미하는 단어(window size를 2라고 합시다)로 앞 뒤 2 단어씩이 vector로 들어온다고 합시다. 반대로 Output으로는 해당 단어가 vector로 나가게 되겠죠. 
- 즉 4개의 vector를 input으로 받아서 fully-connected layer로 막 막들어서, 돌리는데, 이 때 output값과의 차이를 backpropagation해서 weight를 조정하게 되죠. 
- 여기서, 생기는 질문은 들어오는, input vector의 차원 수와 , output vector의 차원수는 모두 vocabulary size(이하 V)로 지정된 one-hot vector라는 것이죠. 
    - 뉴럴넷을 반복해서 학습을 하다보면, V 크기만큼의 벡터로 각 워드의 semantic vector를 구할 수는 있을텐데, 지나치게 vector의 사이즈가 커지는 문제가 있지 않나 싶습니다. 

### projection layer

- 이를 해결하기 위해서 word2vec 모델에는 project layer가 추가로 들어갑니다.
    - 간단하게 말하자면, 원래 V 크기의 벡터를 N(우리가 원하는 dense representation의 차원 크기)의 크기로 변환해주는 레이어죠. 반대로, 예측하는 값에는 N to V 레이어가 추가되게 됩니다. 
    - 그냥 곱해주는 놈인데 이게 무슨 의미가 있냐? 라고 생각할 수 있지만, 뉴럴넷이 원래 그렇습니다 하하핫. PCA를 뉴럴넷이 백프로패게이션을 통해서 해준다고 생각하면 쉽습니다. 
- 다르게 생각하면 뉴럴넷의 구조가 input layer와 output layer를 포함하여 [32, 16, 8, 2] 로 되어 있다고 합시다. 이 때, input 값이 3번째 레이어, 노드가 8개 있는 레이어까지 갔다고 하면, 이 레이어에서는 



## reference

- <https://shuuki4.wordpress.com/2016/01/27/word2vec-%EA%B4%80%EB%A0%A8-%EC%9D%B4%EB%A1%A0-%EC%A0%95%EB%A6%AC/>