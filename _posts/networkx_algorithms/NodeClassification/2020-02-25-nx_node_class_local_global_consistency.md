---
title: networkx - node classification - local and global consistency.
category: python-libs
tags: python python-libs networkx node-clasification 
---

## 2-line summary 

- 이전에 언급했던, harmonic function과 유사합니다만, localness(가까운 이웃들과의 관계), globalness(네트워크 전체를 봤을때, 지역적인 구분)에 대한 관점을 `alpha`를 통해 결정할 수 있따, 라는 것이 다릅니다. 
- 계산방법도 거의 비슷합니다. 


## node classification - local and global consistency.

- 이 내용은 [networkx - local and global consistency](https://networkx.github.io/documentation/stable/reference/algorithms/generated/networkx.algorithms.node_classification.lgc.local_and_global_consistency.html#networkx.algorithms.node_classification.lgc.local_and_global_consistency)를 참고하여 작성되었으며, 해당 내용에 대한 논문은 - [Learning with local and global consistency](https://papers.nips.cc/paper/2506-learning-with-local-and-global-consistency.pdf)에서 볼 수 있습니다
- harmonic function과 유사하게, "label data가 너무 적으므로, labeled data로부터 패턴을 파악하여, unlabeled data의 label을 유추하는, semi-supervised learning을 수행하는 알고리즘"을 만들었고, 그 유효성을 증명하였는데, 사실 이는 [transductive inference](https://en.wikipedia.org/wiki/Transduction_(machine_learning)로 보는 것이 좀 더 명확하다고 생각합니다.
- 아무튼, graph적으로 봤을 때, unlabelled data의 경우 다음의 두 관점에 따라서, 다르게 labeling할 수 있습니다.
    - localness: 사람에게 가깝게 존재하는 이웃들로 그 노드의 label을 유추
    - globalness: 행정구역상 속하는 곳으로 그 노드의 label을 유추. 
- 다만, 이 둘다 타당하므로 데이터마다 약간씩 다르게 처리할 수 있겠죠. 따라서, `alpha`라는 parameter를 사용해서 이 둘의 밸런스를 맞출 수 있도록 합니다. 네, 이게 다에요.


## Implementation by pyhon. 

- [networkx - local and global consistency](https://networkx.github.io/documentation/stable/reference/algorithms/generated/networkx.algorithms.node_classification.lgc.local_and_global_consistency.html#networkx.algorithms.node_classification.lgc.local_and_global_consistency)에 이미 구현되어 있으나, 내용을 참고하여 공부하려고 새롭게 만들었습니다. 

### Back-bone: local and global consistency 

- back bone만 보면 다음과 같죠. 즉, propagation_matrix인 `P`와 base_matrix인 `B`를 다르게 설정하고(alpha에 따라서 변할 수 있도록 설정하고) `F = P.dot(F) + B`를 반복하면서, 결과를 찾습니다. 
- harmonic function과의 차이라면, 다음이죠. 
    - `B`: 1 => 1-alpha
    - `P`: alpha multiplication + normalization
- 엄밀히 따지면, alpha는 "이웃에게서 전달되는 정보를 initiali label보다 얼마나 더 중요하게 생각할 것인가?"를 의미합니다. 높을수록, neighbor의 정보를 소중히 하므로, localness라고 정의해도 딱히 문제는 없을 수 있지만. 아무튼 약간 다릅니다. 
    - alpha=0 : "neighbor의 정보를 완전히 무시하고, initial label만 반영"하고 
    - alpha=1이면, "neighbor의 정보만 반영하고, initial label은 완전히 무시"하게 되죠.
- 이는 사실 base matrix, propagation matrix를 정의한 것과도 유사합니다. alpha가 0에 가까우면, `B`의 값이 커지므로, 초기 label의 영향을 많이 받게 되고, alpha가 커지면, `B`가 작아져서, 초기 label이 큰 의미가 없어지고, 반대로 `P`가 커지므로, 주위의 neighbor의 영향을 많이 받게 되죠

```python 
# F: label_matrix, shape: (n_sample, n_classes)
F = np.zeros((n_samples, n_classes))
# P: propagation_matrix
P = build_propagation_matrix(X, alpha, node_to_label_dict)
# B: alpha가 클수록, 
B = build_base_matrix(X, node_to_label_dict, alpha, n_classes)

# F를 update해가면서 수렴하는 포인트를 찾음.
for i in range(0, max_iter):
    #print(f"== trial {i}")
    F = P.dot(F) + B
#print(F)
return list(predict(F))
```

### Base matrix

- 간단합니다. 그냥 해당 sample의 label을 `1-alpha`으로 설저해주면 됩니다.

```python 
def build_base_matrix(X, node_to_label_dict, alpha, n_classes):
    """
    B: Base matrix. 
    B.shape = (n_samples, n_classes)
    - 1-alpha if sample_i is lable_j else 0 
    - alpha가 클수록, B의 값은 작아짐. 
    - 즉, alpha가 0에 가까울 경우, inital label에 강하게 영향을 받게 됨. 
    - 다만, 해당 논문에서는 주로 0.99로 설정.
    """
    n_samples = X.shape[0]
    B = np.zeros((n_samples, n_classes))
    for node, label in node_to_label_dict.items():
        B[node, label] = 1-alpha
    return B
```

### propagation matrix 

- normalization을 진행하고, 추가로 alph를 곱해줌 

```python
def build_propagation_matrix(X, alpha, node_to_label_dict):
    """
    그냥 degree의 역수만큼 값을 반복적으로 약화시키고, alpha에 대해서도 그런거라고만 보이는데 
    """
    n_node = X.shape[0]
    degrees = 1.0 / X.sum(axis=0)
    # D: diagonal line에 각 node의 degree역수로 채워져 있는 matrix
    # `sparse.diags((1.0 / degrees), offsets=0)`와 동일하지만,
    # linear algebra에 익숙하지 못한 사람들이 있을 수 있어서 풀어서 정리함.
    D = np.zeros([n_node, n_node])
    diagonal_x = [i for i in range(0, n_node)]
    diagonal_y = [j for j in range(0, n_node)]
    D[diagonal_x, diagonal_x] = degrees
    D_sqrt = np.sqrt(D)
    S = alpha * D_sqrt.dot(X).dot(D_sqrt)
    return S
```


### node classification with varying alpha 

- alpha를 변형할 때, node classification이 어떻게 달라지는지를 파악하기 위하여, alpha를 변형하며, node의 label을 에측하고, 그 결과를 animation으로 만들었습니다. 
- 해당 animation은 영상으로 구현하여 유튜브에 업로드하였습니다. 
    - [VIDEO: graph node classification(by local and global consistency with varying alpha)](https://www.youtube.com/watch?v=8kDuoALw3TM)

```python
import networkx as nx
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# karate_club graph를 가져와서, 
G = nx.karate_club_graph()

# 몇개의 노드에 대해서 임의로 labeling을 하고, 
labeled_nodes_dict = {
    0: 0,
    33: 1,
    32: 2,
    5: 3
}
# node_attr에 label을 입력해주고,
for n, class_id in labeled_nodes_dict.items():
    G.nodes[n]['label'] = class_id

# label별로 색깔을 지정해주고,
label_color_dict = {
    0: 'red',
    1: 'blue',
    2: 'green',
    3: 'purple'
}


# initialize figure
fig = plt.figure()
pos = nx.fruchterman_reingold_layout(G, seed=2)

# animation 중에 변하지 않는 요소들은 먼저 그려주고
nx.draw_networkx_edges(G, pos=pos)
nx.draw_networkx_labels(G, pos=pos, labels=labeled_nodes_dict)

def animate(alpha):
    """
    - animation 중에 변하는 요소들은 이 함수 내에서 그려줌.
    - 사실 매번 새로 그려줘도 되지만, 가능하면 요소의 특성들만 바꾸는 것이 훨씬 가벼움.
    """
    title = plt.title(f"node_classification_lgc - alpha: {alpha:4f}")
    label_preds = local_and_global_consistency(G, alpha=alpha)
    # draw node without label.
    # Node의 color만 변경해줌
    node_color_lst = [label_color_dict[lbl] for lbl in label_preds]
    NodeCollection = nx.draw_networkx_nodes(G, pos=pos, node_color=node_color_lst)
    NodeCollection.set_color(node_color_lst)
    print(f"== alpha: {alpha:0.6f} complete")


frame_num = 200
frames = np.linspace(0.00001, 0.999, frame_num)
my_animation = animation.FuncAnimation(fig,
                                       animate,
                                       frames=frames,
                                       interval=500)

writer = animation.writers['ffmpeg'](fps=25)
my_animation.save(f"animation_frame{frame_num}.mp4", writer=writer, dpi=512)
```

- 해당 코드를 실행하거나, 유튜브 영상 [VIDEO: graph node classification(by local and global consistency with varying alpha)](https://www.youtube.com/watch?v=8kDuoALw3TM)을 보시면, alpha에 따라서 어떤 결과가 나오는지 알 수 있습니다. 1.0에 가까워질수록, 초기 initial label보다는 주변 neighbor의 영향을 많이 받게 되죠. 

## wrap-up

- 이는 사실 node2vec에서도 동일하게 나타나는 현상입니다. graph라는 것은 local의 관점으로 볼 것이냐, global의 관점으로 볼 것이냐에 따라서 그 결과가 달라지죠. 물론 그 둘을 잘 고려해서 합치는 것이 보통 graph-learning에서 하려고 하는 것이기는 합니다만.


## reference

- [Learning with local and global consistency](https://papers.nips.cc/paper/2506-learning-with-local-and-global-consistency.pdf)
- [VIDEO: graph node classification(by local and global consistency with varying alpha)](https://www.youtube.com/watch?v=8kDuoALw3TM)
- [networkx - local and global consistency](https://networkx.github.io/documentation/stable/reference/algorithms/generated/networkx.algorithms.node_classification.lgc.local_and_global_consistency.html#networkx.algorithms.node_classification.lgc.local_and_global_consistency)
- [sklearn.semi_supervised.LabelSpreading](https://scikit-learn.org/stable/modules/generated/sklearn.semi_supervised.LabelSpreading.html)


## raw-code

- 전체 코드는 다음과 같습니다.

```python
def local_and_global_consistency(G, alpha=0.99, max_iter=300, label_name='label'):
    """
    alpha: 0.0 혹은 1.0일 경우 각각 propagation matrix가 0이 되거나, base matrix가 0이 되어 무쓸모해짐. 
    """
    def build_propagation_matrix(X, alpha, node_to_label_dict):
        """
        그냥 degree의 역수만큼 값을 반복적으로 약화시키고, alpha에 대해서도 그런거라고만 보이는데 
        """
        n_node = X.shape[0]
        degrees = 1.0 / X.sum(axis=0)
        # D: diagonal line에 각 node의 degree역수로 채워져 있는 matrix
        # `sparse.diags((1.0 / degrees), offsets=0)`와 동일하지만,
        # linear algebra에 익숙하지 못한 사람들이 있을 수 있어서 풀어서 정리함.
        D = np.zeros([n_node, n_node])
        diagonal_x = [i for i in range(0, n_node)]
        diagonal_y = [j for j in range(0, n_node)]
        D[diagonal_x, diagonal_x] = degrees
        D_sqrt = np.sqrt(D)
        S = alpha * D_sqrt.dot(X).dot(D_sqrt)
        return S

    def build_base_matrix(X, node_to_label_dict, alpha, n_classes):
        """
        B: Base matrix. 
        B.shape = (n_samples, n_classes)
        - 1-alpha if sample_i is lable_j else 0 
        - alpha가 클수록, B의 값은 작아짐. 
        - 즉, alpha가 0에 가까울 경우, local consistencty를 주로 반영하게 되므로 
        harmonic function을 이용한 node-classification과 큰 차이가 없게 됨.
        """
        n_samples = X.shape[0]
        B = np.zeros((n_samples, n_classes))
        for node, label in node_to_label_dict.items():
            B[node, label] = 1-alpha
        return B

    def get_label_info(G, label_name='label'):
        """
        node_to_label_dict: {node_id:label_id}
        - 그냥 {node: 해당 노드가 속한 label_id} 로 구성된 dictionary 
        - unlabeled node의 경우 key도 존재하지 않음.
        """
        node_to_label_dict = {}
        for n, n_attr in G.nodes(data=True):
            if label_name in n_attr:  # labeled node
                node_to_label_dict[n] = n_attr[label_name]
            else:  # unlabeled node
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
    P = build_propagation_matrix(X, alpha = 0.99, node_to_label_dict)
    B = build_base_matrix(X, node_to_label_dict, alpha, n_classes)

    # F를 update해가면서 수렴하는 포인트를 찾음.
    for i in range(0, max_iter):
        #print(f"== trial {i}")
        F = P.dot(F) + B
    #print(F)
    return list(predict(F))

```