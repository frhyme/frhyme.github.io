---
title: PaperSummary - Learning with local and global consistency
category: paper-summary
tags: paper-summary node-clasification 
---

## 2-line summary 

- 사실, harmonic function과의 차이점은, `alpha`라는 parameter로 localness와 globalness에 대해 가중치를 다르게 고려하여, semi-supervised learning을 수행했다, 라는 것이 가장 큰 차이점으로 보입니다.
- 그리고, alpha는 클수록 localness를 고려하게 되며, 본 연구에서는 "데이터마다 다른데, 우리는 0.99로 세팅했다"라고 말하고 있죠.
- harmonic function과 코드는 거의 유사하나, `alpha`를 통해 특히, 범용성을 확장했다는 것, manifold에 잘 작동한다는 것 정도가, 본 논문의 의의라고 할 수 있겠네요.

## Learning with local and global consistency

- 2004년에 NIPS에 나온 논문입니다. 네, NIPS, 매우 유명한 학회죠 호호호.
- 해당 논문은 [여기에서 보실 수 있습니다](https://papers.nips.cc/paper/2506-learning-with-local-and-global-consistency.pdf).

## Abstract 초월 번역 

- 본 논문에서는 "세상에 labeled data가 너무 적다"로부터 출발하여, "조금만 labeling이 되어있을 때, label data로부터 unlabeled data를 마저 labeling하여, 학습하는 semi-supervised learning을 다루고 있습니다". 
- 이를 비슷하게 [transductive inference](https://en.wikipedia.org/wiki/Transduction_(machine_learning))라고 표현하기도 하죠. 이 표현이 좀더 명확합니다. 저는 semi-supervised learning이라는 말이 더 헷갈리게 하는 것 같아요. 
- 아래 그림이 "transductive inference"을 좀 더 명확하게 표현하는데, 데이터에, 충분히 label이 되어 있지 않을때, 나머지를 어떻게 잘 labeling할 것인가? 를 이야기하고 있죠.

![transductive inference img in wikipedia](https://upload.wikimedia.org/wikipedia/en/1/19/Labels.png)

- 기본적인 접근 방법은 이미 알려진 labeled data과 unlabeled data간의 내재적인 관계를 파악하는 것인데, 결국 "가까운 놈을 따를 것인가(localness)", "manifold에 맞는 놈을 볼 것인가(globalness)의 관점으로 나뉩니다. 이를 `alpha`라는 파라미터로 조정하여, 어느 한쪽을 더 반영할 수 있죠. 
    - localness: 가깝게 자주 만나는 사람들을 중심으로 구분함.
    - globalness: 행정 구역상으로 사람들을 구분함
- 다만, alpha는 엄밀하게 이를 의미하지는 않고요 "relative amount that an instance should adopt the information from its neighbors as opposed to its initial label", 즉, neighbor로부터 주어지는 정보와 초기에 주어진 initial label의 정보 중에서 무엇을 우선시할것인가? 라는 의미로 쓰입니다. 
    - 따라서, alpha=0이면, "neighbor의 정보를 완전히 무시하고, initial label만 반영"하고 
    - alpha=1이면, "neighbor의 정보만 반영하고, initial label은 완전히 무시"하게 되죠.

## other things..

- 여기서 말하는 semi-supervised learning(즉, 모든 data가 label되어 있지는 않지만 몇 개는 되어 있다)의 핵심적인 가정은 'consistency'인데, 이는 다음을 의미합니다.
    1) 주위의 point들(nearby point)들은 비슷한 label을 가진다(localness)
    2) 같은 구조(same cluster, or manifold)는 같은 라벨을 가지는 경향성을 가진다(globalness)
- 즉, 이 시점에서 발생하는 일종의 trade-off는 "nearby point"를 더 고려할 것인가? 아니면 "구조"를 더 고려할 것인가? 로 나뉘게 되죠. 

### About algorithm.

- `W`는 adjacency weight matrix를 의미하며, diagonal element는 0으로 세팅하였습니다(이를 통해, self-reinforcement가 없어지죠). 또한, `W`는 normalization 되어 있습니다.
- `G = (V, E)`의 관점에서 볼 때, iteration이 진행되면서, node는 그들의 이웃으로부터 label에 대한 정보를 전달받게 됩니다. 
- "nbr로부터 정보를 전달받는 정도", 즉, "주위의 point들과 비슷한 label을 가진다"를 의미하는 localness는 alpha에 의해서 결정됩니다. alpha는 `(0.0, 1.0)`의 범위를 가지며, 1.0에 가까울소록 localness를 적극적으로 반영하게 되죠. 따라서, 1.0에 가깝다면, 주위의 node의 label에 따라서 현재 label이 결정되는 label-propagation 방법과 유사해집니다.
- alpha에 따른 node classification의 진행과정을 그림으로 정리하여 [유튜브에 동영상으로 올렸습니다.](https://www.youtube.com/watch?v=8kDuoALw3TM) 영상을 보시면, alpha가 올라갈수록, 주위의 node의 label에 영향을 많이 받게 되는 것을 알 수 있습니다. 
- 또한, 딱히, optimal parameter가 무엇인지는 알 수 없다, 라고 말하고, 그냥 "우리는 0.99를 사용했다"라고 말합니다. 이는, 어찌보면, "데이터에 따라서 적합한 모델은 달라, 그러니까, alpha를 조정하면서 가장 잘 맞는 parameter를 튜닝하는게 제일 맞지"를 말하고 있는 것이죠. 네, 뭐, 사실 이렇게 parameter만으로 학습의 방향을 결정할 수 있다는 것 자체도, 중요하기는 하죠.

## reference

- [Learning with local and global consistency](https://papers.nips.cc/paper/2506-learning-with-local-and-global-consistency.pdf)
- [VIDEO: graph node classification(by local and global consistency with varying alpha)](https://www.youtube.com/watch?v=8kDuoALw3TM)