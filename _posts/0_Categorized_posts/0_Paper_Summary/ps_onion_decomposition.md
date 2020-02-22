---
title: PaperSummary - Multi-scale structure and topological anomaly detection via a new network statistic - The onion decomposition
category: paper-summary
tags: paper-summary k-shell decomposition anomaly-detection networks-statistic
---

## 1-line summary 

- k-core decomposition을 개선한 onion-spectrum을 제시하였다. 

## Multi-scale structure and topological anomaly detection via a new network statistic: The onion decomposition

- Nature scientific report에 2016년에 게재된 논문입니다. 
- 해당 논문은 [여기에서 볼 수 있습니다.](https://www.nature.com/articles/srep31708)


## Abstract 번역 

- 본 논문에서는, 네트워크의 구조적인 성질(structural property)를 다양한 층위에서(micro, meso, macro) 관찰할 수 있는 네트워크 지표를 제시하였다.
- 본 논문에서 제시한 지표인 "onion spectrum"은 onion decomposition에 기초하는데, 이는 기존에 있었던 k-core decomposition(표준적인 network fingerprinting)을 개선한 것이다. onion spectrum은 k-core처럼 쉽고 정확하게 계산해낼 수 있다. 
- 그러함에도, onion spectrum은 네트워크에 대해서 더 풍성한 정보를 제공하는데, 가령, node heterogenetiy, degree correlation, centrality, tree or lattice-likeness 와 같은 정보들을 제공한다. 
- 게다가, k-core decomposition과는 다르게, 혼합된 degree-onion spectrum은 "기존의 네트워크 조직과 특별히 다른 종류의 위상구조(topological structure)를 가지는 흥미로운 subgraph들을 발견할 수 있다.
- ?? This local description can also be leveraged to easily generate samples from the ensemble of networks with a given joint degree-onion distribution. 

- 본 논문에서는, onion spectrum을 실제 네트워크들과 표준적인 그래프 모델에 적용하여, 그 유용성을 증명했다.


## other things. 

### onion-decomposition의 필요성.

- 비록, 이미 많은 지표들이 있다고 해도, multi-scale metric에 대한 필요성은 여전히 존재한다. 
- 예를 들어, degree distribution과 local clustering은 매우 간단하고 동시에 많은 정보들을 담고 있지만, microscopic한 관점, 즉 network에 대한 지역적인 특성만을 담고 있다. 
- Modularity나, 다른 community structure에 대한 성질들은 네트워크에 대한 meso-scale을 담고 있지만, 여전히 조악한(ill-defined) 부분이 있으며, network community에 대한 공통적인 정의는 아직 증명되지 못했따. 
- 거시적인 관점(macroscopic)에서 betweenness centrality, eigenvector centrality, shortest path length의 경우, 전체 네트워크에 대해서 주어진 node의 역할을 특성화한다. 하지만, 여기에는 매우 높은 "계산 비용(computational effort)"이 발생하며, local understanding에 대해서는 거의 도움이 되지 못한다. 
- 따라서, 미시, 거시 관점등 다양한 관점에서 network의 특성을 바라볼 수 있는 새로운 지표와 도구의 필요성이 대두된다. 

- k-core decomposition을 개선한 알고리즘을 제시하였으며, 이를 통해, 특별한 subgraph들을 찾는 것에 성공했다. 본 연구에서는 undirected and unweighted network에 대해서 적용하였지만, 이훼 확장될 수 있을 것으로 본다. 

### onion-decomposition. 

- k-core decomposition은 degree가 작은 node들을 삭제해나가면서 network들을 구분하는 것을 말한다. 
- k-core는 maxiaml sub-network로, 모든 노드가 최소한 k 이상의 degree를 가지는 것을 말한다. 그리고 k-shell은 정확하게 모든 노드가 k의 degree를 가지는 것을 말합니다.
- 따라서, 보통 "낮은 값의 k-shell"은 "중심부가 아닐 수 있습니다(less central)". k가 높아질수록, 좀더 central core에 근접할 수 있게 되죠.
- 사실, 이처럼 k-core decomposition은 양파 껍질(shell)을 까는 것 같은 느낌이 듭니다. 처음에는 degree가 1인 shell을 까고, 순차적으로 까면서, 중심부에 접근하게 되는 것이죠. 
- 따라서, 우리는 여기서 `layer`라는 개념에 집중하여, 특정 node에 도달하기 위해서 몇번의 껍질 까는 과정(peeling passes)가 필요한지를 활용했습니다. 
- 다만, 아래 그림에서 보듯이 차이가 있다면, 순차적으로 하나씩 잘라나간다는 것이죠. 1-shell, 2-shell로 딱딱 구분하는 것이 아니라, 1-shell일지라도 먼저 잘라지는 아이들과, 나중에 잘라지는 아이들이 있으므로 이를 구분하여 처리하겠다는 것이, onion-decomposition의 목적입니다.

![onion-decomposition figure](https://media.springernature.com/lw685/springer-static/image/art%3A10.1038%2Fsrep31708/MediaObjects/41598_2016_Article_BFsrep31708_Fig1_HTML.jpg?as=webp)







## reference

- [Multi-scale structure and topological anomaly detection via a new network statistic: The onion decomposition](https://www.nature.com/articles/srep31708)
- [networkx.algorithms.core.onion_layers](https://networkx.github.io/documentation/stable/reference/algorithms/generated/networkx.algorithms.core.onion_layers.html#networkx.algorithms.core.onion_layers)