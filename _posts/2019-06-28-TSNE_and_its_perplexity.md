---
title: t-SNE와 perplexity 
category: machine-learing
tags: tsne machine-learning dimensionlaity-reduction perplexity parameter-tuning
---

## t-sne

- t-sne는 복잡한 차원의 데이터를 축소하는 기법을 말합니다. PCA와 유사한데, PCA의 경우 데이터를 오쏘고날한 선형 벡터의 합으로 표현하기 때문에, 잃어버려지는 정보의 양이 좀 많죠( 대신 속도는 t-sne에 비해서 훨씬 빠릅니다). 
- 아무튼, t-sne는 현재 데이터가 다차원일 때, 이를 2차원으로 축소해서 2차원 평면에 대략적으로 보기 위해서 많이 사용됩니다. 
- 일반적으로는 그냥 다음처럼 생각없이 쓰곤 하죠. 

```python
from sklearn.manifold import TSNE

X_2dim = TSNE(n_components=2).fit_transform(X)
```

## But perplexity

- 파라미터 튜닝, 이라는 것은 다 아실 것입니다. 머신러닝할때 결과가 생각만큼 잘 안 나오면, 이 값을 바꿔보고, 저 값을 바꿔보고 하면서, 잘 될때가지 적합한 파라미터를 찾아보죠.
- 당연한 이야기지만, t-sne와 같은 dimensionality reduction에서도 parameter를 잘 튜닝하는 것이 중요합니다. 특히, perplexity를 잘 맞추는 것이 필요하죠.

## do it

- 제가 요즘 귀찮아서 그림은 안 넣겠습니다만. 다음으로 코딩해서 테스트를 해봤씁니다. 
    - 간단하게 complete graph를 만들고, 
    - 각 edge의 weight는 random으로 주고 
    - 이 그래프를 Structural Deep Neural Embeddding(SDNE)를 사용해서 학습시키고, 
    - 그 결과를 t-sne를 사용해서 차원 축솔를 진행하는데, 이 때 perplexity를 조절합니다.

```python
# coding: utf-8

import time
import networkx as nx
import numpy as np
import pandas as pd
# customized lib
from SDLE_LIB import SDNE

from sklearn.manifold import TSNE
from sklearn.metrics.pairwise import euclidean_distances, cosine_similarity

import matplotlib.pyplot as plt

def draw_simple_graph():
    # the graph
    # 대충 complete graph를 만들고 
    N = 20
    np.random.seed(0)
    G = nx.complete_graph(N)
    for e in G.edges(data=True):
        e[2]['weight']=np.random.random()

    SDNE_start_time = time.time()
    model = SDNE(
        G, encode_dim=20, encoding_layer_dims=[128, 16],
        alpha=0.0, beta=20
    )

    model.fit(batch_size=10, epochs=20, steps_per_epoch=100, verbose=1)
    node_embeddings = model.get_node_embedding()
    for i in range(0, N):
        #print(node_embeddings[i])
        continue
    print("##"*20)

    print(f"SDNE complete during {time.time() - SDNE_start_time}")
    # perplexity 를 변경하면서 잘 되는지 봄.
    perplexities = [2, 5, 10, 20, 30]
    
    nrow, ncol = 1, len(perplexities)
    width = 5
    fig, axes = plt.subplots(
        nrow, ncol, figsize=(width * ncol, width * nrow)
    )
    for j, perp in enumerate(perplexities):
        ax = axes[j]
        pos = TSNE(n_components=2, perplexity=perp, n_iter=500).fit_transform(node_embeddings)
        ax.scatter(pos[:, 0], pos[:, 1])
    plt.savefig("figures/draw_simple/"+f"perp_{perp}"+".png", dpi=100)
    print("##"*20)

if __name__=='__main__':
    draw_simple_graph()

```

- 아무튼 해보면, perplexity가 너무 커지면, 다 비슷비슷한 것처럼 나오게 됩니다 하하


## wrap-up

- "왜 어떤 상황에서는 perplexity가 큰게 좋고 아닌게 좋냐"를 알아서 찾아서 처리해주면 좋지만, 아직은 그것까지는 안되는 것 같아요.