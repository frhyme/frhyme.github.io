---
title: graph2vec) Graph를 어떻게 vector로 표현할 수 있을까? 
category: machine-learning
tags: graph2vec graph machine-learning
---

## graph2vec??

- graph2vec이라는 말보다는 word2vec이 더 익숙할 것이라고 생각됩니다. word2vec은 말 그대로 단어를 벡터로 표현하는 것을 말하죠. word는 수치로 나타나는 값이 아니고, 수치로 값을 나타내지 못하면 머신러닝 알고리즘에 적용할 수 없기 때문에 이를 vector로 표현해내는 작업이 필요합니다.
- graph2vec도 마찬가지입니다. graph로 표현된 것을 vector로 표현하는 작업을 말하죠. 이렇게 표현하고 나면, 해당 값을 다른 머신러닝 알고리즘에 집어넣는 것이 쉬워지니까요.
    - 비교적 간단하게, 사실 adjacency matrix도 graph2vec과 유사한 표현(representation)이 아닌가? 라고 할 수도 있을 것 같습니다. 사실 맞는 이야기죠. 이것도 graph를 vector로 표현한 방식이기는 합니다. 
    - 그러나, 이 경우는 row, column의 순서가 어떻게 되어야 하는지에 대한 의문이 남아있기는 합니ㄷ. node의 순서가 A, B, C인 것과 B, C, A인 것은 서로 다른 매트릭스로 표현되는데, 같은 그래프가 다른 매트릭스로 표현될 수 있다면 이는 효과적인 Graph2Vec이라고 하기 어렵지 않을까요? 만약 convolution 등을 통해서 해당 매트릭스를 변환하다고 하더라도, 순서가 다르면 filter가 다 다르게 업데이트되기 때문에 적용하는 것이 어려워집니다. 즉, adjancency matrix들 같은걸로는 어렵다는 이야기죠.

## paper) graph2vec: Learning Distributed Representations of Graphs

- [2017년 7월에 올라온 논문](https://arxiv.org/abs/1707.05005)의 초록을 정리해봅니다. 
- 논문의 초록은 대략 다음과 같구요. 

> Recent works on representation learning for graph structured data predominantly focus on learning distributed representations of graph substructures such as nodes and subgraphs. 
> However, many graph analytics tasks such as graph classification and clustering require representing entire graphs as fixed length feature vectors. While the aforementioned approaches are naturally unequipped to learn such representations, graph kernels remain as the most effective way of obtaining them. However, these graph kernels use handcrafted features (e.g., shortest paths, graphlets, etc.) and hence are hampered by problems such as poor generalization. 
> To address this limitation, in this work, we propose a neural embedding framework named graph2vec to learn data-driven distributed representations of arbitrary sized graphs. graph2vec's embeddings are learnt in an unsupervised manner and are task agnostic. 
> Hence, they could be used for any downstream task such as graph classification, clustering and even seeding supervised representation learning approaches. Our experiments on several benchmark and large real-world datasets show that graph2vec achieves significant improvements in classification and clustering accuracies over substructure representation learning approaches and are competitive with state-of-the-art graph kernels.

- 이를 한글로 번역하면 대략 다음과 같습니다. 
    - graph structured data의 representation learning에 관한 최근의 연구들은 node, edge와 같은 graph substructure의 distributed representation에 집중되고 있다. 
    - 그러나, 기존의 많은 graph classification, clustering 기술들은 fixed length feature vector에 대해서 수행된다는 한계가 있고 동시에 poor generalization 문제를 가지고 있다는 한계가 있다. 
    - 고정된 길이가 아니라 변동성이 있는(arbitrary) graph에 대해서도 학습을 할 수 있는 graph2vec 이라는 neural embedding framework를 제시하였다. 이는 unsupervised learning에 속한다. 
    - graph2vec을 통해서 향후 graph classification, clustering 등의 supervised learning에도 유용하게 사용될 수 있다. 
    - 실제 data들에 대해서 수행을 해 봤고, 의미있었다.
- 즉, 어떤 길이의 graph들이든 상관없이 representation learning을 수행할 수 있도록 했다는 것이 해당 연구가 가지는 가장 큰 학문적 공헌인 것으로 보이네요.
    - 이미지라고 생각하는 것이 편하니까



## curious thing

- 