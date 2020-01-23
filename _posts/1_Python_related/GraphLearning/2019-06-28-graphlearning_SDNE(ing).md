---
title: Structural Deep Neural Embedding
category: machine-leanring
tags: deep-leanring machine-learning ML graph networkx
---

## Structural Deep Neural Embedding(SDNE)

- 최근에 네트워크의 노드를 벡터로 변환하는 작업을 수행하고 있습니다. 
- "왜 잘 있는 노드를 벡터로 변환해?"라고 말씀하실 수도 있는데, 이건, 기존의 많은 ML/DL 라이브러리들이 숫자에 기반하기 때문이죠. 
- 즉, Graph를 숫자로 변환했을때, 더 많은 라이브러리나 방법론에 사용될 수 있다는 이야기입니다. 
- 여기서, 기존에는 node2vec이나 deepwalk를 사용해서 네트워크를 벡터로 학습했습니다만, 앞서 말한 둘 방법론의 경우는 우선 그래프로부터 발생할 수 있는 시퀀스를 샘플링하고, 그 다음에 학습을 시킵니다. 
    - 그래프로부터 발생할 수 있는 시퀀스들은, 해당 그래프의 어떤 특성을 가지고 있습니다. 
    - 또한 "그래프의 어떠한 특성을 볼 것이냐"에 따라서 그래프의 어떤 특성이 학습되는지가 결정되죠. 
    - 다만, 따라서 샘플링을 어떻게 하느냐에 따라서 결과가 달라질 수 있습니다. 
- 반대로 SDNE의 경우, 그래프로부터 시퀀스를 샘플링하는 부분이 없습니다. 이게 가장 큰 차이이기는 하지만, 이 또한 어떤 부분을 볼 것이냐를 학습시킬 때 parameter로 수정을 하죠. 
    - 시퀀스를 샘플링하는 방법이 없을 뿐, 어떻게 학습시키는지에 따라서 반영되는 그래프의 특성이 달라진다는 사실은 변화가 없습니다. 

## SDNE summary

- 자, 그럼 이제 SDNE에서 어떻게 그래프를 학습시키는지를 정리해보겠습니다. 
- SDNE의 논문은 [여기에서](https://www.kdd.org/kdd2016/papers/files/rfp0191-wangAemb.pdf) 확인할 수 있습니다. 칭화대에서 연구했고, 데이터마이닝 분야의 탑 학회인 KDD(Knoweldege Discovery and Data mining)에서 발표된 논문입니다.

### summary 

- 해당 논문에서 제시하는 방법론은 first-order proximity와 second-order proximity를 보존하면서 임베딩합니다(It is designed so that embeddings preserve the first and the second order proximity)
- first-order proximity: 
    - 네트워크의 두 노드가 서로 연결되어 있다면(edge가 있다면) 이 둘은 서로 비슷하다고 가정함(local pairwise similarity between nodes linked by edges(local network structure), Two nodes in the network are similar if they are connected with the edge)
    - first-order proximity는 supervised learning을 사용해서 학습됨.
- second-order proximity: 
    - 두 노드의 유사성은 각 노드의 이웃 노드를 통해서 학습됨. 만약 두 노드가 비슷한 이웃 노드를 많이 공유한다면, 이 둘은 비슷하게 위치하게 됨(second-order proximity: the similarity of the nodes’ neighborhood structures(global network structure) If two nodes share many neighbors, they tend to be similar)
    - second-order proximity는 Unsupervised Learning을 통해서 학습됨. 
- 대충 "실제 그래프에서 두 노드가 연결되어 있다면, 새로 만들어지는 벡터에서도 거리가 가깝게 위치될 수 있도록 학습"한다는 이야기죠. 
- 뭐 모든 논문이 그렇다고 말하지만. 테스트해보니까 “multi-label classification”, “link prediction”, “visualization 에서 모두 SDNE가 탁-월하다고 합니다. 

- 아래 그림에서 보는 것처럼, 
    - second-order proximity) auto-encoder 2개로 알아서 학습하고, 
    - first-order proximity) encoder된 벡터 간 거리를 활용해서 실제로 서로 연결되는지를 보면서 weight를 학습한다는 이야기죠. 

![](https://www.researchgate.net/profile/Xiaohan_Li/publication/332351429/figure/fig4/AS:746531271479296@1554998333090/Overview-of-SDNE-Image-extracted-from-39.ppm)


## do it

- 그럼, 이제 얼마나 잘 되는지 대충 확인해봅시다. 
- 저는 허접이기 때문에, 직접 구현을 하지는 않았고, [다른 사람이 만든 리퍼지토리](https://github.com/xiaohan2012/sdne-keras)를 가져와서 테스트 해봤습니다. 
- 여기에 있는 [20newsgroup](https://github.com/xiaohan2012/sdne-keras/blob/master/20newsgroup_train.py)라는 테스트케이스를 정리해봤습니다. 이 데이터는 SDNE 원래 논문에서도 참고하고 있습니다.

### 코드 설명 

- 코드는 대략 다음으로 구성됩니다. 
    - sklearn에서 제공하는 document data를 가져옵니다. 
        - 3가지 카테고리에 속하는 document만을 가져오며, document의 카테고리는 label로 사용됩니다. 
    - document를 TF-IDF를 사용해서 벡터화합니다.
    - document간의 거리를 cosine distance를 사용하셔 계산합니다. 
    - 이 거리를 바탕으로 graph를 만들어줍니다. 당연히 여기서 만들어준 그래프는 complete graph가 되겠죠
    - 만든 complete graph를 가지고, SDNE로 학습합니다. 
        - epoch은 적은데, 한번에 학습하는 데이터의 양이 많습니다(당연하지만)
    - 각 document에 대해 표현된 벡터를 가지고 tsne를 사용해서 2차원으로 축소합니다. 
        - 여기서, tsne의 perplexity를 변경하면서 다양하게 봅니다. 
    - 그렇게 해서 2차원에 시각화해보면, label별로 적절하게 멀리 위치해 있는 것을 알 수 있습니다.

```python
# coding: utf-8

from SDLE_LIB import SDNE
import matplotlib.pyplot as plt 
from tqdm import tqdm

from sklearn.manifold import TSNE
from sklearn.neighbors import kneighbors_graph
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.datasets import fetch_20newsgroups

from itertools import product
import pickle as pkl
import networkx as nx
import math

import time
import os
#import matplotlib as mpl
#mpl.use('Agg')


def embedding_for_newsgroup():
    print("##"*10+"start"+"##"*10)

    """
    - 아래 코드는 sklearn에서 기본적으로 제공되는 데이터를 가져옵니다. 
    - dataset.data에는 list of string이 있습니다. tokenize된 워드 리스트가 아니라, string이 그대로 들어가 있죠. 
    """
    categories = ['comp.graphics', 'rec.sport.baseball', 'talk.politics.guns']
    dataset = fetch_20newsgroups(categories=categories)
    """
    - 각 document에 대해서 TFIDF로 변환해줍니다. 
        - 저는 워드 리스트로 토크나이즈한 다음 넣어줘어야 하는줄 알았는데, 그렇게 하지 않아도 되는 것 같아요.
        - 또한, 다른 parameter를 수정하지 않고 그냥 사용했네요. 뭐 상관없습니다만.
    """
    tf_idf_time = time.time()
    print("TF-IDF start")
    vectorizer = TfidfVectorizer()
    vectors = vectorizer.fit_transform(dataset.data)
    print(f"TF-IDF done during {time.time() - tf_idf_time }")

    # build the graph
    """
    - 그 결과 vector의 shape는 (1727, 36064)입니다. 매우 크군요 허허허.
    """
    #print(vectors.shape)
    N = vectors.shape[0]

    """
    - sklearn.neighbors 에 있는 kneighbors_graph 라는 함수는 주어진 2차원 벡터들을 활용해서 노드간의 adjancency matrix를 리턴해주는 함수입니다. 
    - n_neighbors
        - 여기서, n_neighbors라는 파라미터는 각 노드별로 가까운 노드를 몇개나 서로 연결되어 있는 것으로 인식할지를 의미하죠. 
        - 즉, 여기서 N을 사용했다는 이야기는 이를 통해 만들어낼 adjancency matrix는 complete graph가 된다는 것을 의미합니다.
    - mode
        - mode는 connectivity거나 distance로 구분되는데, connectivity는 0 or 1, 즉, 연결만 의미하게 되고, 
        - distance의 경우는 floating number를 의미하죠, 즉 weight가 됩니다.
            - ? 그렇다면 클수록 서로 유사하지 않은 것이 되나???
    - metric 
        - 두 벡터를 어떻게 계산할지를 의미하며, 여기서는 cosine을 사용해서 처리했습니다. 
        - 보통 cosine similarity만 알고 있지만, cosine distance도 있습니다.
            - cosine distance = 1 - cosine similarity 
    """
    kneighbors_graph_start_time = time.time() 
    print("make kneighbors graph start")
    mat = kneighbors_graph(X=vectors, n_neighbors=N, metric='cosine', mode='distance', include_self=True)
    mat.data = 1 - mat.data  # to similarity
    g = nx.from_scipy_sparse_matrix(mat, create_using=nx.Graph())
    print(f"make kneighbors graph end during {time.time() - kneighbors_graph_start_time}")


    parameter_grid = {'alpha': [2],
                    'l2_param': [1e-3],
                    'pretrain_epochs': [0],
                    'epochs': [5]}


    parameter_values = list(product(*parameter_grid.values()))
    parameter_keys = list(parameter_grid.keys())

    parameter_dicts = [dict(list(zip(parameter_keys, values)))
                    for values in parameter_values]


    def one_run(params):
        SDNE_start_time = time.time()
        print("SDNE Training Start")
        #plt.clf()
        batch_size = 32
        alpha = params['alpha']
        l2_param = params['l2_param']
        pretrain_epochs = params['pretrain_epochs']
        epochs = params['epochs']

        model = SDNE(g, encode_dim=100, encoding_layer_dims=[1720, 200],
                    beta=2,
                    alpha=alpha,
                    l2_param=l2_param)
        model.pretrain(epochs=pretrain_epochs, batch_size=32)

        n_batches = math.ceil(g.number_of_edges() / batch_size)
        # n_batches is 46629
        print(f"n_batches: {n_batches}")

        model.fit(epochs=epochs, log=True, batch_size=batch_size,
                steps_per_epoch=n_batches)

        embedding_path = 'embeddings/20newsgroup/alpha{}-l2_param{}-epochs{}-pre_epochs{}.pkl'.format(
            alpha, l2_param, epochs, pretrain_epochs
        )

        embeddings = model.get_node_embedding()
        labels = dataset.target
        pkl.dump((embeddings, labels), open(embedding_path, 'wb'))
        print(f"SDNE Training End during {time.time() - SDNE_start_time}")


    for params in tqdm(parameter_dicts):
        one_run(params)
    print("##"*10+"train complete"+"##"*10)

def visualization_for_newsgroup():
    path = "embeddings/20newsgroup/"
    for file_i, f in enumerate(os.listdir(path)):
        print("##"*20)
        print(f"{file_i} ==> {f}")
        embeddings, labels = pkl.load(open(path+f, 'rb'))
        """
        TSNE는 parameter를 어떻게 설정하는지에 따라서 결과가 달라집니다. 
        - perplexity:
            - number of nearest neighbors that is used in other manifold learning algorithms
        - n_iter:
            - Maximum number of iterations for the optimization. Should be at least 250.
        """
        parameter_names = ['perplexity', 'n_iter']
        parameter_values = [[10, 20], [500, 1000]]
        # product를 value에 대해서 수행했기 때문에, 총 4가지의 조합이 생성됨.
        # 또한 starrred 로 처리되었음.
        value_combinations = list(product(*parameter_values))
        parameter_dict_lst = []
        for values in value_combinations:
            parameter_dict_lst.append(
                dict(list(zip(parameter_names, values)))
            )
        # TSNE를 여러 파라미터에 따라서 보여줌. 
        nrow, ncol = len(parameter_values[0]), len(parameter_values[1])
        width = 5
        fig, axes = plt.subplots(nrow, ncol, figsize=(width * ncol, width * nrow))

        for i, perp in tqdm(enumerate(parameter_values[0])):
            for j, n_iter in enumerate(parameter_values[1]):
                tsne_start_time = time.time() 
                #print(f"perp: {perp}, n_iter: {n_iter} start")
                ax = axes[i, j]
                pos = TSNE(n_components=2, perplexity=perp, n_iter=n_iter).fit_transform(embeddings)
                print(f"perp: {perp}, n_iter: {n_iter} done during {time.time() - tsne_start_time}")
                ax.scatter(pos[:, 0], pos[:, 1], c=labels, alpha=0.5)
        plt.savefig("figures/20newsgroup/"+f"file_{file_i}"+".png", dpi=100)
        print("##"*20)

embedding_for_newsgroup()
visualization_for_newsgroup()

```


## wrap-up

- 다시 정리해보자면, 
    - document 간의 거리를 TF-IDF 벡터간의 거리로 계산하여 그래프를 생성하고, 
    - 이 방법을 통해서 생성된 complete graph(weight는 TF-IDF에 기반한 유사도)를 SDNE를 사용해서 학습을 시키고 
    - 만든 벡터를 perplexity를 변화시키면서 t-SNE로 차원을 축소하여 2차원 평면에 뿌립니다. 
- 결과를 보면, 어느 정도 뭉쳐져 있는 것을 볼 수 있기는 합니다만, 흐음....
- 다음과 같은 몇 가지 의문사항이 남아있기는 합니다. 

### question 

- complete graph를 굳이, 벡터로 변화시킬 필요가 있는가? 
    - complete graph는 사실 이미 서로 다른 도큐먼트간의 거리가 명확하게 존재합니다. 모든 노드 페어에 대해서요.
    - 즉, 이 상태에서 spectral clustering을 사용해서 진행을 하면 알아서 잘 잘라주는데, 이걸 굳이 다시 벡터를 확장하고(여기에 파라미터 튜닝하는 것도 들어가고, 학습시간이 훨씬 많이 걸리는 문제점도 있고), 다시 클러스터링을 해줄 필요가 있는지에 대해서 좀 의문이 듭니다. 
- 그래서 graph embedding을 사용한 다음에, 뭘 할수 있는가? 
    - graph embedding의 효과를 명확하게 보여주려면, graph를 벡터로 변형 한 다음, 적용해서 유의미한 성과를 거둔 분석 시나리오 같은 것이 필요하다고 생각됩니다만, 현재 여기서는 그러한 부분이 부각되어 있지 않습니다. 
    - 가령, graph를 벡터로 표현한 다음, 이를 RNN 구조를 함께 사용해서 학습을 시켰고, 이를 통해, Graph가 어떤 식으로 변화할지에 대해서 알 수 있었다. 라는 언급이 더 명확하게 있으면 좋을 것 같기는 합니다. 
    - 뭐 물론, link prediction에서 기존보다 더 잘된다는 것이 증명되기는 했습니다만. 기존의 네트워크구조에서는 link prediction을 "공통되는 neighbor의 수" 정도로 jaccard 값을 가지고 사용했던것 같습니다만, 그보다는 지금처럼 벡터로 만들어서 처리하는 것이 훨씬 효과적이기는 하죠.