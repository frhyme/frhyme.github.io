

## what is structural holes? 

- [structural holes](https://en.wikipedia.org/wiki/Structural_holes)은 social network 연구 분야에서 주로 쓰이는 개념이며, "두 객체(individual)간의 정보 접근에 대한 차이"로 이해될 수 있다.
- 현실계에서 일어나는 대부분의 사회적 구조(social structure)는 강한 연결(strong connection)으로 구성된 밀집된 구조(dense cluster)로 특성화됩니다. 따라서, 보통 이 클러스터별로 비슷한 생각, 정보 등을 공유하게 되죠. 
- 그러나, 만약, 어떤 한 개인이 서로 밀집된 두 그룹(혹은 클러스터)의 중간에 위치하게 된어, 중개자(mediator)로 존재하게 된다면, 이 사람은 다른 사람들에 비해 비교적 높은 정보 획득에서의 이점을 가지게 됩니다. 이 사람은 일종의 '문지기(gatekeeper)'로서의 역할을 수행하게 되는 것이죠.
- 따라서, 양 클러스터에서 발생하는 모든 생각과 아이디어는 이 사람을 통하게 되고, 혁신적인 아이디어가 이로부터 나올 수 있게 됩니다. 
- 아래 그림을 보시면 이 것이 어떤 의미인지 보다 명확하게 아실 수 있을 것 같아요. 

![](https://upload.wikimedia.org/wikipedia/commons/thumb/0/05/Network_Structure.jpg/330px-Network_Structure.jpg)

## Measures: Structural holes.

### Bridge Count

- Bridge는 "두 노드 `u`, `v`간에 존쟇난 edge `(u, v)`가 끊어질 경우, graph `G`의 connected component가 증가하는 edge `(u, v)`"를 말합니다. 즉, 이 edge가 없어지면, `u`, `v`의 연결성이 없어지는 것이죠. 즉, 비교적 직관적인 지표로, bridge의 수를 고려항, structural hole의 존재를 파악할 수 있습니다. 
- 또한, node별로 bridge의 수를 세면, 각 node가 structural hole의 특성을 얼마나 가지는지도 알 수 있죠. 

### Constraint

- Constraint는 보통 "제약식"으로 많이 번역되죠. 즉, "강제력, 제한하는 힘" 정도로 번역하면 될것 같습니다. 앞서 본 것처럼 structural hole일수록 어느 한쪽에 치우쳐져서 정보등을 받아들이지 않습니다(이를 "강제력이 약하다, constraint가 약하다" 라고 번역할 수 있는 셈이죠). 
- Network의 constraint는 network에 존재하는 모든 연결의 `local constraint`, `c_uv`의 총합을 말합니다. 
- `c_uv`는 노드 `u`가 투자하는 모든 시간과 에너지(weight의 합) 중에서, `v`에 얼마나 투자하고 있는지, 그 정도를 의미합니다. 또한 이는 두 가지 측면에서 바라보게 되는데요. 
    - direct: node `u`가 `v`에게 "직접(direct)" 어느 정도 에너지를 소비하는지, 즉 edge(u, v)를 고려하고,
    - indirect: node `u`가 `v`에게 "간접(indirect)" 어느 정도 에너지를 소비하는지, 즉, `u`와 `v` 사이에 존재하는 모든 edge들을 고려하는 것 
- 따라서, 직접적(direct), 간접적(indirect) 영향력을 고려하여 `local_constraint(u, v)`를 측정하게 됩니다. 이 local_constraint는 u가 다른 노드에 비해서 v에게 지나치게 많이 쏠려 있을 경우(가령, u는 v라는 특정 노드에게만 상대적으로 많은 영향력을 주고 받게 되면 값이 커지게 되죠.

### Constraint implementation by python

- 말로만 하면 사실 무슨 말인지 이해가 어려우므로, 간단하게 코딩을 해봤습니다. 

#### mutual_weight(u, v) 

- `mutual_weight(u, v)`는 node `u`, `v`의 모든 edge의 weight의 합입니다. 기본적으로는 directed 라고 가정하여 양방향을 모두 계산해줍니다.

```python
def mutual_weight(G, u, v, weight='weight'): 
    # node u와 v간의 모든 edge의 weight합.
    # unweighted일 경우 1.0으로 가정. 
    # 단, 여기서는 항상 weighted라고 가정
    m_w = 0.0
    if G.has_edge(u, v): 
        m_w += G[u][v][weight]
    if G.has_edge(v, u): 
        m_w += G[v][u][weight]
    return m_w
```

#### normalized mutual_weight(u, v)

- `normalized mutual_weight(u, v)`는 u가 u의 모든 이웃 노드들에 대한 `mutual_weight`의 합으로 v에 대한 mutual_weight를 나누어주는 것을 말합니다. 즉 "u는 u가 투자할 수 있는 모든 weight 중에서 v에게 얼마나 투자하고(받고) 있는가?"를 의미하는 것이 되죠. 

```python
def normalized_mutual_weight(G, u, v, norm = sum, weight='weight'):
    # u가 속한 모든 edge의 mutual_weight의 sum으로 
    # mutual_weight(u, v)를 scaling
    # 즉, u가 가지고 있는 모든 '에너지'중에서 v로 투자하는 비율을 의미함.
    u_all_nbrs_m_w_sum = 0.0
    for w in nx.all_neighbors(G, u): 
        u_all_nbrs_m_w_sum += mutual_weight(G, u, w, weight)
    if u_all_nbrs_m_w_sum == 0:
        return 0 
    else: 
        return mutual_weight(G, u, v, weight=weight) / u_all_nbrs_m_w_sum
```

#### local constraint(u, v)

- 앞서 말한 바와 같이, 직접적인 mutual weight와, 간접적인 mutual weight를 고려하여 계산하게 됩니다.

```python
def local_constraint(G, u, v, weight='weight'): 
    # local constraint는 
    # direct: u의 v에 대한 normalized mutual weight
    # indirect: u와 v 사이에 존재하는 node w에 대한 mutual weight의 곱합
    # local_constraint = (direct+indirect)**2를 말함.
    direct = normalized_mutual_weight(G, u, v, weight='weight')
    indirect = 0 
    nmw = normalized_mutual_weight
    for w in nx.common_neighbors(G, u, v):
        indirect += nmw(G, u, w, weight=weight) * nmw(G, w, v, weight=weight)
    return (direct + indirect)**2
```

#### cosntraint(u) 







- local constraint

This indicator measures the extent to which time and energy is concentrated within a single cluster. It consists of two components: direct, when a contact consumes a large proportion of a network's time and energy, and indirect, when a contact controls other individuals, who consume a large proportion of a network's time and energy.


레이텍으로 쓰면 좋겠지만 저는 그냥 다음으로 풀어서 쓸게요. 
    - `mutual_weight(u, v)`: node `u`와 node `v`간에 존재하는 direct edge의 weight의 합. 즉, edge `(u, v)`, `(v, u)`를 모두 고려(unweighted일 경우 1.0) 
    - `norm_mutual_weight(u, v)`: `mutual_weight(u, v)`를 "node `u`의 모든 이웃(neighbor)들과의 `mutual_weight`의 합(sum)"으로 나누어 normalization한 것입니다. 따라서, 만약 node `u`가 `v`를 제외한 어떤 노드들과도 연결되어 있지 않다면, 이 값은 1.0이 되겠죠.
    - `local_constraint(u, v)`: `norm_mutual_weight(u, v)` 그리고 `u`, `v` 사이의 모든 node `w`들에 대해서 `norm_mutual_weight(u, w)`, `norm_mutual_weight(w, v)`를 더하고, 이를 제곱한 것.
- 즉, 보통은 bridge인 edge들이 constraint 값이 작게 나오게 됨.

This indicator measures the extent to which time and energy is concentrated within a single cluster. It consists of two components: direct, when a contact consumes a large proportion of a network's time and energy, and indirect, when a contact controls other individuals, who consume a large proportion of a network's time and energy.

- Network constraint는 "매니저의 동료들과의 네트워크가 매니저를 중심으로 한 "강압복(straitjacke)"과 얼마나 비슷한지를 측정합니다. 즉, 새로운 아이디어나, support를 얼마나 제한하는지를 말하게 되는 것이죠. 
- 또한, 이는 네트워크의 특성인 size, density, hierarchy에 의존하며, 작은 네트워크에서는 연결 자체가 적으므로, cosntraint가 작게 나올 수 있고, dense network에서도 높게 나올 수 있습니다.
Network constraint measures the extent to which the manager’s network of colleagues is like a straitjacket around the manager, limiting his or her vision of alternative ideas and sources of support. It depends on three network characteristics: size, density, and hierarchy. Constraint on an individual would be generally higher in case of a small network (he or she has just few contacts), and if contacts are highly connected between each other (either directly as in a dense network, or indirectly, through the mutual central contact as in a hierarchical network).[5]

#### Burt's formula

- Burt는 "네트워크의 중복(redundancy)"을 측정하는 지표를 제시했습니다. 그는 node j가 node i의 다른 node들과 얼마나 중복되어 있는지를 측정하려고 합니다. 

그는 `node_i`가 `node_j`간에 접촉(contact)가 어느 정도로 어느 범위로 중복되는지를 예측하는 것을 목적으로 합니다. 여기서 `Redundancy`는 


Burt introduced the measure of network’s redundancy. He aims to estimate to what extent contact j is redundant with other contacts of node i. Redundancy is understood as an investment of time and energy in a relationship with another node q, with whom node j is strongly connected.[2]

## Structural hole vs. Weak tie.

- structural hole theory에 대한 기본적인 아이디어는 weak tie theory과 유사합니다. 
- weak tie에서 주장하는 바에 따르면, 두 노드 u, v의 연결(tie)이 강할수록 그들의 접점(contact, 이웃들)이 중복되기 쉽고(overlap) 따라서 그들은 비슷한 사람들에 의해나 공통의 tie들을 소유하게 된다는 이야기죠. 
- 즉, weak tie theory에서도 동일하게, "강한 연결은 중요한 정보들(novel information)을 전송할 경향이 적다"라고 말합니다. 
- 두 개념은 모두 같은 모델에 기초하고 있지만, 차이점은 분명하게 존재합니다.
- weak tie에서는 서로 간의 contact가 해당 tie의 힘(strength)에 의한 다리의 역할을 한다고 주장했지만, 
- Burt는 

Both concepts rely on the same underlying model, however, some differences between them can be distinguished. While Granovetter claims that whether a contact would serve as a bridge depends on a tie’s strength, Burt considers the opposite direction of causality.[7] Thus, he prefers the proximal cause (bridging ties), while Granovetter argues in favor of the distal cause (strength of ties)

## Application 

- structural hole이 풍분한 네트워크의 경우는 보통 "entrepreneurial network"로 지치되며, structural hole로 인해서 혜택을 받는 개인은 보통 "기업가(entrepreneur)"로 간주됩니다. 
- st

The networks rich in structural holes were referred to as entrepreneurial networks, and the individual who benefits from structural holes is considered as an entrepreneur. Application for this theory can be found in one of Burt's studies of entrepreneurial network. He studied a network of 673 managers in the supply chain for the firm, and measured the degree of social brokerage. All the managers had to submit their ideas about the ways to improve supply chain management, which were then evaluated by judges.[1] The findings of this empirical study:

An idea's value corresponded to the degree that the individuals were measured as social brokers;
The wages of individuals corresponded to the degree that they were measured as social brokers;
Managers who discussed issues with other managers were better paid, better evaluated positively, and more likely to be promoted.

구조적 구멍이 풍부한 네트워크를 기업가 네트워크라고하며 구조적 구멍의 혜택을받는 개인은 기업가로 간주됩니다. 이 이론의 적용은 Burt의 기업 네트워크에 대한 연구 중 하나에서 찾을 수 있습니다. 그는 회사의 공급망에서 673 명의 관리자 네트워크를 연구하고 사회적 중개 정도를 측정했습니다. 모든 관리자는 공급망 관리를 개선하는 방법에 대한 아이디어를 제출해야했으며,이를 심사 위원이 평가했습니다. [1] 이 실험적 연구의 결과 :

아이디어의 가치는 개인이 소셜 중개인으로 측정 된 정도에 해당합니다.
개인의 임금은 사회적 중개인으로 측정 된 정도에 해당합니다.
다른 관리자와 문제를 논의한 관리자는 더 나은 급여를 받고 긍정적으로 평가하고 승진 할 가능성이 높습니다.


## referenc

- 