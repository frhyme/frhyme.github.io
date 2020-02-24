---
title: networkx - node classification - harmonic function
category: networkx
tags: paper-summary node-classification harmonic-function similarity
---

## 2-line summary

- 몇개만 label되어 있는 graph를 대상으로 node classification을 수행함. 
- 특히, similarity 기반 graph를 만들고 이로부터 node clasisfication을 수행하여 일종의 data preprocessing을 더 정확하게 할 수 있다는 강점이 있음.


## networkx - node classification - harmonic function 

- 사실, 쓰여있기는 "node-clasification"이라고 작성되어 있지만, "semi-supervised label propagation"이라고 봐도 될 것 같아요. 
- 기존의 정의된 "label-propagation"은 "모든 node에 unique한 label을 부여하고, 이웃의 최빈 label을 본인의 label로 지정하는 방법"을 말합니다. 즉, 아무 정보 없이 "학습"을 진행하기 떄문에, unsupervised learning이죠. 
- 그러나, 여기서 정의한 node classification은 몇 가지 label이 이미 기정의되어 있다고 보고 진행합니다. 즉, 만약 100개의 node가 주어졌는데, 우리가 가령 5개의 node가 어떤 label에 속하는지 압니다. 이를 통해서, 나머지 95개의 lable을 예측하려면 어떻게 해야할까? 를 해결하려고 한 것이죠.
- 위를 제시한 논문인 [Semi-Supervised Learning Using Gaussian Fields and Harmonic Functions](http://mlg.eng.cam.ac.uk/zoubin/papers/zgl.pdf)을 참고해보면, graph의 community-detection을 위해서 harmonic function에 기반한 node classification을 제시한 것이 아니라, unlabel된 이미지에 대해서 labeling하기 위해서 진행된 것입니다. 논문 내용을 간단하게 요약하자면, 다음과 같습니다.
    1) 이미지들이 너무 labeling이 되어 있지 않다. 
    2) 그래서, image similarity를 활용해서 similar graph를 만들었다. 
    3) 그리고, 이 graph에 대해서 labeled된 데이터로부터 확산하는 식으로 알고리즘을 만들었다 
    4) 그랬떠니, labeling이 잘 되더라, 
- 네 그렇습니다. 따라서, 이 방법론이 clustering이나, community 에 속하는 것이 아닌, classification에 속하는 것은, 해당 방법론이 아주 "supervised learning"이기 때문이죠. 

## node classification - harmonic function 

- 사실 개념만 보면 "labelled node와 가까울 수록 해당 label이 되기 쉽다. 그러나, labelled node가 너무 많은 이웃이 있을 경우, 그 이웃을 labeling시키는 영향력을 반비례로 감소한다"가 다입니다. 심플하죠. 
- 따라서, 이를 "labelled node로부터 시작하는 random walk(depth-first)를 만들고, 이로부터 다른 이웃노드들에 도달하는 비율"을 바탕으로 예측해도 아마 어느 정도 비슷한 결과가 나올 것 같습니다.
- 아무튼 같은 짓을 matrix method를 사용해서 할 수 있죠. 
- 그리고 [networkx.algorithms.node_classification](https://networkx.github.io/documentation/stable/_modules/networkx/algorithms/node_classification/hmn.html#harmonic_function)와 코드는 의미적으로는 동일합니다. 
    - 다만, 예외처리를 전혀 하지 않았고, 
    - 계산 속도 문제를 전혀 고려하지 않았죠(sparse-matrix를 사용하지 않고 그냥 numpy.matrix를 사용함) 

### Algorithm description

- 우선 다음 3가지를 아셔야 합니다. 결국, 마코브체인에서처럼 어디에 수렴하는지를 찾는 것이 본 알고리즘의 목적인 것이죠.
- 이 다음 코드가 전체의 메인 줄기인 것이죠. 나머지는 뭐 그냥 별 거 없습니다.

```python 
# F: sample_i가 class_i에 담길 확률을 의미하는 matrix
F = np.zeros((n_samples, n_classes))

# P: 매 iteration마다 F에 곱해지는 matrix 
# labelled node의 degree 역수를 영향력으로 파악하여, 주위에 전파. 
# 그냥 diagonal 이 1.0/node degree인 square matrix라고 생각해도 됨.
P = build_propagation_matrix(X, node_to_label_dict)

# B: (n_samples, n_classes)로 구성되어 있음. 
# unlabelled의 경우 그냥 0으로 비어 있고, 
# labeled의 경우 적합한 class의 위치에 1로 채워져 있음 
B = build_base_matrix(X, node_to_label_dict, n_classes)

# F에 P를 반복적으로 곱해가면서 수렴하는 포인트를 찾음.
    for i in range(0, max_iter):
        print(f"== trial {i}")
        F = P.dot(F) + B
    return list(predict(F))
```

- 나머지 코드는 다음과 같습니다. 죽죽 읽으시면 되고 별로 어려운 것은 없을 것 같아요 호호.

```python
def harmonic_function(G, label_name='label', max_iter=30):
    """
    harmonic_function에 기반한 node-classification은 
    local-structure를 기반으로, 가장 강하게 연결되어 있는 node의 label을 따라간다
    라는 특성을 가짐.
    - 코드의 간결성을 위해서, node와 label은 모두 interger를 가진다고 설정함. 
    """
    def build_propagation_matrix(X, node_to_label_dict):
        """
        - 복잡해보이지만, node의 degree의 역수를 바탕으로 영향력이 전파되면서 측정된다고 보면 됨. 
        - 즉, 어떤 node가 만약, 많은 사람들과 연결되어 있을 경우, 해당 label이 다른 노드로 전파되기 어렵고 
        - 적게 연결되어 있을 경우에는 전파되기 쉬움. 
        """
        n_node = X.shape[0]
        # degrees: degree가 클수록 이웃 노드에 대한 전파력이 작아진다고 가정.
        degrees = 1.0/X.sum(axis=0)
        # D: 각 node의 degree의 역수
        # diaognal에 해당 node의 역수로 세팅 
        D = np.zeros([n_node, n_node])
        diagonal_x = [i for i in range(0, n_node)]
        diagonal_y = [j for j in range(0, n_node)]
        D[diagonal_x, diagonal_x] = degrees

        # P: propagation matrix.
        P = D.dot(X)
        # normalization.
        # labeled noded의 경우, Base_matrix를 더할 때마다, 값이 커진다. 
        # 따라서, 이 값은 0으로 세팅해야 문제가 생기지 않음.
        P[[k for k in node_to_label_dict]] = 0
        return P

    def build_base_matrix(X, node_to_label_dict, n_classes):
        """
        B: Base matrix. 
        B.shape = (n_samples, n_classes)
        - 1 if sample_i is lable_j else 0 
        - propagation은 결국 labeled node로부터 시작됨. 
        - 진행되면서, 각 node의 영향력이 작아지므로 매번 더해줌
        (사실 그냥 random walk를 만들고 있따, 라고 봐도 됨)
        """
        n_samples = X.shape[0]
        B = np.zeros((n_samples, n_classes))
        for node, label in node_to_label_dict.items():
            B[node, label] = 1
        return B

    def get_label_info(G, label_name='label'):
        """
        node_to_label_dict: {node_id:label_id}
        - 그냥 {node: 해당 노드가 속한 label_id} 로 구성된 dictionary 
        - unlabeled node의 경우 key도 존재하지 않음.
        """
        node_to_label_dict = {}
        for n, n_attr in G.nodes(data=True):
            if label_name in n_attr: # labeled node
                node_to_label_dict[n] = n_attr[label_name]
            else: # unlabeled node
                continue
        return node_to_label_dict

    def predict(F):
        """
        F.shape: (n_sample, n_class)
        즉, 각 sample별로 가장 가능성이 높은 n_class를 가지는 값을 찾아서 위치를 pos를 리턴.
        """
        predicted_label_ids = np.argmax(F, axis=1)
        return predicted_label_ids
    # X: adjacency matrix
    X = nx.to_numpy_array(G)
    node_to_label_dict = get_label_info(G, label_name='label')

    n_samples = X.shape[0]
    n_classes = len(set(node_to_label_dict.values()))

    # F: label_matrix, shape: (n_sample, n_classes)
    F = np.zeros((n_samples, n_classes))
    P = build_propagation_matrix(X, node_to_label_dict)
    B = build_base_matrix(X, node_to_label_dict, n_classes)

    # F를 update해가면서 수렴하는 포인트를 찾음.
    for i in range(0, max_iter):
        print(f"== trial {i}")
        F = P.dot(F) + B
    return list(predict(F))
```

## wrap-up 

- 다시 정리해보겠습니다. 
- 보통 graph에 기반한 분석에서는 community detection, k-shell decomposition, onion decomposition, clustering, 등의 기법을 사용하게 되죠. 이게 일반적입니다. 
- 그리고 보통 일반적인 classification 문제들에서는 그냥 svm, 뭐 아무튼 그런것들을 쓰거나, 단편적인 방식으로 진행해 나갑니다.
- 그런데, 여기서 제시하는 node classification 방법은 일종의 혼종이죠. 그리고 이 문제는 graph 분야에서의 필요성보다는, 다른 분야, 특히 image classification 분야에서 필요해서 만들어졌죠. 
- 몇 개의 노드에 대해서만 label을 알고 있을 때, 그리고 G가 구축되어 있을때, 이를 사용해 남은 모든 node에 대한 prediction을 수행합니다. 이를 통해 graph가 가지는 특성을 그대로 반영하여 더 정확하게 classification이 가능하다, 라는 것이 이 방법의 강점이 되겠네요.


## reference 


- [networkx.algorithms.node_classification.hmn.harmonic_function](https://networkx.github.io/documentation/stable/reference/algorithms/generated/networkx.algorithms.node_classification.hmn.harmonic_function.html#networkx.algorithms.node_classification.hmn.harmonic_function)
- [Semi-Supervised Learning Using Gaussian Fields and Harmonic Functions](http://mlg.eng.cam.ac.uk/zoubin/papers/zgl.pdf)