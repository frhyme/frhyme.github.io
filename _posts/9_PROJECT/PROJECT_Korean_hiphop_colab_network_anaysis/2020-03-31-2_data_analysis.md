---
title: 한국 힙합씬 피쳐링 네트워크 분석 - 3편 - Data Analysis
category: python-libs
tags: python python-libs selenium data-crawling networkx centrality
---

## 한국 힙합씬 피쳐링 네트워크 분석. 

- 저는 대상/현상을 네트워크로 모델링하고 네트워크 적인 분석 법을 사용하여 대상 네트워크를 분석하는 일을 주로 수행합니다. 그리고, 그러다보니, 세상의 많은 현상들을 결국 "네트워크"적으로 바라보게 되죠. 
- 동시에 저는, 한국 힙합의 오랜 팬이기도 합니다. 힙합음악의 흥미로운 점은, 여러 뮤지션들이 다른 뮤지션들의 음악에 협업의 이름으로 참가하는 일이 매우 활발하다는 것이죠. 
- 저는 궁금했습니다. 과연, 한국 힙합의 피쳐링은 어떤 형태로 구성되어 있을까? 만약 이를 네트워크로 구성한다면 어떻게 구성해야 할까? 구성된 네트워크는 어떤 분석을 하면 재미있는 결과가 나올 수 있을까? 와 같이요. 
- 그래서, 저는 그동안의 한국 힙합 데이터를 모두 웹에서 크롤링하여 네트워크를 구성하고 그 결과를 정리하였습니다. 
- 분석 결과는 [한국 힙합 피쳐링 네트워크 분석](https://docs.google.com/presentation/d/1zkOGBTD0UTaeoxYLxkPohNXaaKWYjVXfdbHgrli8xms/edit#slide=id.p) 에서 발표자료로 보실 수 있습니다.


## 한국 힙합씬 네트워크 분석하기 - 3편 -Data Analysis. 

- 본 내용에서는 구성된 네트워크를 대상으로 분석을 수행합니다. 
- 보통 네트워크 분석이라고 한다면, 구축된 네트워크를 대상으로 중요한 Node(뮤지션)을 선정하고, 중요한 Edge(뮤지션)간의 관계를 선정하고, 비교적 밀접하게 연결되어 있는 Component/Community 등을 뽑고, 네트워크를 시각화하거나, 비디오로 만들어 그 양상을 관찰한다, 정도를 말합니다.
- 다만, 그 과정에서 다음과 같은 것들을 결정해야 합니다. 
    - **타당하지 않은 node, edge를 어떻게 걸러낼 것인가?:** 가령 node중에서 단 1곡만을 발표하였으나, 현재 네트워크에 포함된 경우도 있으며, edge의 경우도, "119REMIX"와 같은 단체 곡에서 단 한번 공동 작업한 edge들이 포함되어 있는 경우들이 있습니다. 어떤 사람은 이를 유효하게 둘 지 모르지만, 저는 걸러내었습니다.
    - **weightness**: 어떤 사람들은 단 5번 같이 작업을 했고, 어떤 사람들은 10번 같이 작업을 했다고 합시다. 그렇다면, 이 둘의 관계의 긴밀성이 같다고 할 수 있을까요? 혹은, 다르다고 해야 할까요? 
- 이러한 종류의 미묘한 결정으로 인해서 데이터 분석의 결과가 달라집니다. 그리고 그 설정을 변경하면서, 분석 결과에 어떠한 영향을 미치는지 직접 판단하면서 이러한 parameter들을 수정해줘야 합니다. 

### Graph Preporcessing 

- 우선, 아래의 ID들을 제외해줍니다. 전처리를 해줄 만큼 해줬다고 생각했는데, 여전히 조금 결과에 영향을 미치는 ID들이 있어서 제외하였습니다. 

```python
INVALID_aIDs = {
    'W0572100': "이단옆차기2",
    "10001724": "계범주",
    "U0000010": "재윤(솔리드)",
    "10001885": "이단옆차기1",
    "10002797": "서지음", 
    "10009925": "에스쿱스", 
    "10009926": "우지"
}
```

- 그리고 다음의 방식으로 edge의 attribute에서 `date`가 `'0000'`으로 표기되어 있는 경우를 제외했죠.

```python
MG = MG.edge_subgraph(
    [(u, v, k) for u, v, k, d in MG.edges(data=True, keys=True) if d['date'][:4] != '0000']
).copy()
```

- 그리고, "각 노드가 발표한 노래의 수"와 "뮤지션들의 관계의 수"를 사용하여 필터링을 하고, 그 다음 해당 graph를 k-core로 만들어줍니다. k-core는 "Graph의 모든 Node의 degree가 k보다 큰 graph"를 말합니다. 처음에는 그냥 `G.degree()`를 통해 일정 degree_threshold보다 작은 node들을 모두 삭제해주는 식으로 진행했는데, 한번 지운 다음에는 지웠기 때문에, 또 degree_threshold보다 작은 degree를 가진 node들이 남아있을 수 있습니다. 
- 따라서, 여기서는 k-core를 통해 너무 외곽에 존재하는 node들은 모두 없애고, 비교적 네트워크를 밀집해주죠. 


```python
def GRAPH_PREPROCESSING(MG, N_SONGs_Threshold=5, EDGE_Threshold=3, K_CORE_NUM=4):
    """
    전달받은 MG를 우선 G로 변경하고, 주어진 값에 따라서 전처리를 해준 
    전처리된 G를 리턴합니다.
    """
    print("== Graph Preprocessing START")
    print("---- MG to G")
    G = MG_to_G(MG)
    print("=="*40)
    print(f"---- REMOVE NODE n_songs <= {N_SONGs_Threshold}")
    print(f"---- REMOVE EDGE weight <= {EDGE_Threshold}")
    G = G_FILTERING(G, N_SONGs_Threshold=N_SONGs_Threshold, EDGE_Threshold=EDGE_Threshold)
    
    print(f"---- G to {K_CORE_NUM}-CORE")
    G = nx.k_core(G, k=K_CORE_NUM)

    if nx.is_connected(G) == False:
        print("== NOT CONNECTED NOW")
        for i, comm in enumerate(nx.connected_components(G)):
            print(f"---- COMMUNITY {i:2d} :: SIZE - {len(comm)}")
            #print([aID_to_aNAME[aID] for aID in comm])
        G = return_max_connected_comp(G)
        print(f"== CHOOSE BIGGEST COMMUNITY as NETWORK - {len(G)}")
    print("== Graph Preprocessing DONE")
    return G
```


### Centrality Analysis 

- 그 다음, 구축된 네트워크를 대상으로 centrality를 계산합니다. 가급적, weight, unweighted 인 경우를 모두 고려하여, 값이 어떻게 다른지를 비교해서 보시면 좀 더 의미있는 분석 결과를 담을 수 있을 것이라고 생각됩니다.
- 계산은 대부분 `networkx`에 있는 함수를 그대로 사용하였습니다만, 값이 정렬되어 나오는 것이 아니므로, 다음과 같이 조금 정리하여 사용하였습니다.

```python
def PRINT_DEGREE(G, TOP_N):
    deg_lst = [(aID, deg) for aID, deg in nx.degree(G)]
    deg_lst = sorted(deg_lst, key=lambda x: x[1], reverse=True)
    print("== DEGREE")
    for i, (aID, deg) in enumerate(deg_lst[:TOP_N]):
        print(f"RANK {i+1:3d} :: {aID_to_aNAME[aID]} ::: {deg:3d}")
    df = pd.DataFrame(
        [(aID, aID_to_aNAME[aID].strip(), deg) for (aID, deg) in deg_lst], 
        columns = ['aID', 'aNAME', 'DEGREE'])
    df.to_csv('CENTRALITIES/degree.csv')
    print("=="*40)
```

### Community Detection 

- `nx.algorithms.community.girvan_newman(G)`를 사용하여 community detection을 수행하였습니다. 
- 이 경우에도 weight를 고려하여 community detection을 하는 경우와 그냥 unweighted라고 고려하고 community detection을 하는 경우는 다릅니다. 가능하면 이 둘을 모두 수행해보고 비교하는 것이 더 좋겟죠. 
- 이 코드는 대략 다음과 같습니다. `nx.algorithms.community.girvan_newman(G)`는 generator이며, `next()`로 불러질 때마다, 새로운 community-set를 가져옵니다. 

```python
COMM_DETECT_GEN = nx.algorithms.community.girvan_newman(G)
for i, COMMs in enumerate(COMM_DETECT_GEN):
    COMMUNITY_LOG['COMMUNITIES'][i] = {}
    print(f"== GENERATION {i:3d} ================")
    for j, COMM in enumerate(COMMs): 
        COMMUNITY_LOG['COMMUNITIES'][i][j] = {
            'IDs': list(COMM), 'NAMEs': [aID_to_aNAME[aID] for aID in COMM]}
        if len(COMM)>1:
            print(f"---- COMMUNITY {j:2d}")
            print([aID_to_aNAME[aID] for aID in COMM])
            print("--"*60)
    print("=="*60)
```

## wrap-up 

- 대부분의 데이터 분석 과정이, 데이터 전처리와 초반 부분이 어렵지, 뒤쪽으로 가면 상대적으로 쉽습니다. 여기서 데이터의 분석 결과를 만들어내는 것은, "데이터 전처리가 잘 되었다는 전제하에" 매우 쉽게 진행되는 부분이죠. 
- 단, 동시에 그렇기 때문에 만약 "데이터 분석 과정"에서 문제가 생긴다면, 다시 처음인 "데이터 전처리"로 돌아가야 한다는 것을 말하기도 합니다. 잘못되었다면, 처음부터 다시 뜯어고쳐야 한다는 말이죠.


## raw-code 

```python
import json
import itertools
import os
import pickle
import datetime

import networkx as nx

from collections import Counter

import pandas as pd 

import matplotlib.pyplot as plt
import matplotlib.animation as animation
import matplotlib.font_manager as fm

## GLOBAL VARIABLE ########################################
aID_to_aNAME = json.load(open(f"artist_data.json", "r"))
aNAME_to_aID = {v: k for k, v in aID_to_aNAME.items()}
############################################################


def READ_MG(file_name=None):
    if file_name is None: 
        file_name = sorted([fileName for fileName in os.listdir("GRAPH_pkl/")])[-1]
    print(f"== FILE READ {file_name}")
    with open(f"GRAPH_pkl/{file_name}", 'rb') as f:
        MG = pickle.load(f)
    print("---- REMOVE edge with DATE")
    # 날짜가 0000으로 표기된 노래들이 있음. 가령 다이나믹 듀오의 '아리따움'같은 경우인데 
    # 많지 않지만 귀찮으므로 제외하고 진행함.
    MG = MG.edge_subgraph(
        [(u, v, k) for u, v, k, d in MG.edges(data=True, keys=True) if d['date'][:4] != '0000']).copy()

    INVALID_aIDs = {
        'W0572100': "이단옆차기2",
        "10001724": "계범주",
        "U0000010": "재윤(솔리드)",
        "10001885": "이단옆차기1",
        "10002797": "서지음", 
        "10009925": "에스쿱스", 
        "10009926": "우지"   
    }
    print("---- REMOVE InValid aIDs")
    MG.remove_nodes_from(INVALID_aIDs.keys())
    print("== MG read COMPLETE")
    return MG

def MG_to_G(MG):
    """
    - MG는 nxMultiGraph이며, 여러 edge들을 동시에 가질 수 있음 
    - 하지만, 이렇게 되어 있을 경우, 다른 networkx의 알고리즘들에 적용하기 어려워진다는 문제가 있음 
    - 많은 알고리즘들이 multigraph에 적용가능하도록 설게되어 있지 않음. 
    - 따라서, edge의 수를 weight로 처리하여 G로 변경해주는 함수가 필요함. 
    """
    G = nx.Graph() 
    G.add_nodes_from([(n_ID, n_attr)for n_ID, n_attr in MG.nodes(data=True)])
    for (u, v) in set(MG.edges()): 
        edge_key_attr_lst = [(edge_key, edge_attr['date']) for edge_key, edge_attr in MG[u][v].items()]
        dates = [y for x, y in edge_key_attr_lst]
        G.add_edge(u, v, weight=len(edge_key_attr_lst), dates=dates)
    nx.set_edge_attributes(
        G, {e: 1.0/G.edges[e]['weight'] for e in G.edges()}, name='distance')
    return G

def return_max_connected_comp(G):
    """
    - G가 connected가 아닐 때, 가장 큰 connected component를 리턴
    """
    if nx.is_connected(G)==True:
        return G
    else:
        max_node_set = None
        for sub_node_set in nx.connected_components(G):
            if max_node_set is None: 
                max_node_set = sub_node_set
            else: 
                if len(sub_node_set) > len(max_node_set):
                    max_node_set = sub_node_set
                else:
                    continue
        return G.subgraph(max_node_set).copy()

def G_FILTERING(G, N_SONGs_Threshold=5, EDGE_Threshold=3):
    G.remove_nodes_from([n for n, n_attr in G.nodes(data=True) if n_attr['n_songs'] <= N_SONGs_Threshold])
    G.remove_edges_from([(u, v) for u, v, e_attr in G.edges(data=True) if e_attr['weight'] <= EDGE_Threshold])
    return G


def GRAPH_PREPROCESSING(MG, N_SONGs_Threshold=5, EDGE_Threshold=3, K_CORE_NUM=4):
    """
    전달받은 MG를 우선 G로 변경하고, 주어진 값에 따라서 전처리를 해준 
    전처리된 G를 리턴합니다.
    """
    print("== Graph Preprocessing START")
    print("---- MG to G")
    G = MG_to_G(MG)
    print("=="*40)
    print(f"---- REMOVE NODE n_songs <= {N_SONGs_Threshold}")
    print(f"---- REMOVE EDGE weight <= {EDGE_Threshold}")
    G = G_FILTERING(G, N_SONGs_Threshold=N_SONGs_Threshold, EDGE_Threshold=EDGE_Threshold)
    
    print(f"---- G to {K_CORE_NUM}-CORE")
    G = nx.k_core(G, k=K_CORE_NUM)

    if nx.is_connected(G) == False:
        print("== NOT CONNECTED NOW")
        for i, comm in enumerate(nx.connected_components(G)):
            print(f"---- COMMUNITY {i:2d} :: SIZE - {len(comm)}")
            #print([aID_to_aNAME[aID] for aID in comm])
        G = return_max_connected_comp(G)
        print(f"== CHOOSE BIGGEST COMMUNITY as NETWORK - {len(G)}")
    print("== Graph Preprocessing DONE")
    return G

    
def PRINT_DEGREE(G, TOP_N):
    deg_lst = [(aID, deg) for aID, deg in nx.degree(G)]
    deg_lst = sorted(deg_lst, key=lambda x: x[1], reverse=True)
    print("== DEGREE")
    for i, (aID, deg) in enumerate(deg_lst[:TOP_N]):
        print(f"RANK {i+1:3d} :: {aID_to_aNAME[aID]} ::: {deg:3d}")
    df = pd.DataFrame(
        [(aID, aID_to_aNAME[aID].strip(), deg) for (aID, deg) in deg_lst], 
        columns = ['aID', 'aNAME', 'DEGREE'])
    df.to_csv('CENTRALITIES/degree.csv')
    print("=="*40)
    
def PRINT_WEIGHTED_DEGREE(G, TOP_N):
    print("== WEIGHTED DEGREE")
    weighted_deg_dict = {n: 0 for n in G}
    for u, v, e_attr in G.edges(data=True):
        weighted_deg_dict[u] += e_attr['weight']
        weighted_deg_dict[v] += e_attr['weight']
    weighted_deg_lst = [(k, v) for k, v in weighted_deg_dict.items()]
    weighted_deg_lst = sorted(
        weighted_deg_lst, key=lambda x: x[1], reverse=True)
    for i, (aID, deg) in enumerate(weighted_deg_lst[:TOP_N]):
        print(f"RANK {i+1:3d} :: {aID_to_aNAME[aID]} ::: {deg:3d}")
    df = pd.DataFrame(
        [(aID, aID_to_aNAME[aID].strip(), deg) for (aID, deg) in weighted_deg_lst], 
        columns = ['aID', 'aNAME', 'WEIGHTED_DEGREE'])
    df.to_csv('CENTRALITIES/weighted_degree.csv')
    print("=="*40)

def PRINT_CLOSENESS(G, TOP_N):
    close_lst = [(aID, v) for (aID, v) in nx.closeness_centrality(G,).items()]
    close_lst = sorted(close_lst, key=lambda x: x[1], reverse=True)
    print("== CLOSENESS")
    for i, (aID, v) in enumerate(close_lst[:TOP_N]):
        print(f"RANK {i+1:3d} :: {aID_to_aNAME[aID]:20s} ::: {v:0.4f}")
    df = pd.DataFrame(
        [(aID, aID_to_aNAME[aID].strip(), deg) for (aID, deg) in close_lst], 
        columns = ['aID', 'aNAME', 'CLOSENESS_CENTRALITY'])
    df.to_csv('CENTRALITIES/closeness.csv')
    print("=="*40)

def PRINT_WEIGHTED_CLOSENESS(G, TOP_N):
    close_lst = [(aID, v) for (aID, v) in nx.closeness_centrality(
        G, distance='distance').items()]
    close_lst = sorted(close_lst, key=lambda x: x[1], reverse=True)
    print("== WEIGHTED_CLOSENESS")
    for i, (aID, v) in enumerate(close_lst[:TOP_N]):
        print(f"RANK {i+1:3d} :: {aID_to_aNAME[aID]:20s} ::: {v:0.4f}")
    print("=="*40)

def PRINT_BETWEENNESS(G, TOP_N):
    bet_lst = nx.betweenness_centrality(G)
    bet_lst = [(n_ID, v) for n_ID, v in bet_lst.items()]
    bet_lst = sorted(bet_lst, key=lambda x: x[1], reverse=True)
    print("== BETWEENNESS")
    for i, (aID, v) in enumerate(bet_lst[:TOP_N]):
        print(f"RANK {i+1:3d} :: {aID_to_aNAME[aID]:20s} ::: {v:0.4f}")
    df = pd.DataFrame(
        [(aID, aID_to_aNAME[aID].strip(), deg) for (aID, deg) in bet_lst], 
        columns = ['aID', 'aNAME', 'BETWEENNESS_CENTRALITY'])
    df.to_csv('CENTRALITIES/betweenness.csv')
    print("=="*40)


def PRINT_WEIGHTED_BETWEENNESS(G, TOP_N):
    bet_lst = nx.betweenness_centrality(G, weight='distance')
    bet_lst = [(n_ID, v) for n_ID, v in bet_lst.items()]
    bet_lst = sorted(bet_lst, key=lambda x: x[1], reverse=True)
    print("== WEIGHTED_BETWEENNESS")
    for i, (aID, v) in enumerate(bet_lst[:TOP_N]):
        print(f"RANK {i+1:3d} :: {aID_to_aNAME[aID]:20s} ::: {v:0.4f}")
    print("=="*40)

def PRINT_COMMUNICABILITY_BETWEENNESS(G, TOP_N):
    comm_bet_lst = nx.communicability_betweenness_centrality(G)
    comm_bet_lst = [(n_ID, v) for n_ID, v in comm_bet_lst.items()]
    comm_bet_lst = sorted(comm_bet_lst, key=lambda x: x[1], reverse=True)
    print("== COMMUNICABILITY BETWEENNESS")
    for i, (aID, v) in enumerate(comm_bet_lst[:TOP_N]):
        print(f"RANK {i+1:3d} :: {aID_to_aNAME[aID]:20s} ::: {v:0.4f}")
    df = pd.DataFrame(
        [(aID, aID_to_aNAME[aID].strip(), deg) for (aID, deg) in comm_bet_lst],
        columns = ['aID', 'aNAME', 'COMMUNICABILITY_BETWEENNESS_CENTRALITY'])
    df.to_csv('CENTRALITIES/communicability_betweenness.csv')
    print("=="*40)

def PRINT_PAGERANK(G, TOP_N):
    print("== PAGERANK ")
    pagerank_lst = nx.pagerank(G, weight='weight')
    pagerank_lst = [(n_ID, v) for n_ID, v in pagerank_lst.items()]
    pagerank_lst = sorted(pagerank_lst, key=lambda x: x[1], reverse=True)
    for i, (aID, v) in enumerate(pagerank_lst[:TOP_N]):
        print(f"RANK {i+1:3d} :: {aID_to_aNAME[aID]:20s} ::: {v:0.4f}")
    df = pd.DataFrame(
        [(aID, aID_to_aNAME[aID].strip(), deg) for (aID, deg) in pagerank_lst],
        columns = ['aID', 'aNAME', 'PAGERANK'])
    df.to_csv('CENTRALITIES/pagerank.csv')
    print("=="*40)
    return df


def EXTRACT_YEARLY_MULTIGRAPH(MG, NODE_SET=None):
    """
    - NODE_SET을 기본 노드세트로 하고, {Year: YearG}의 형태로 연도별 Graph를 담은 딕셔너리를 리턴한다.
    """
    subMG = MG.subgraph(NODE_SET).copy()
    YearSet = sorted(set([d['date'][:4]
                          for u, v, d in subMG.edges(data=True)]))
    Year_EDGEs_dict = {Year: [] for Year in YearSet}

    for u, v, k, d in subMG.edges(data=True, keys=True):
        Year_EDGEs_dict[d['date'][:4]] += [(u, v, k)]
    return {Year: subMG.edge_subgraph(EDGEs) for Year, EDGEs in Year_EDGEs_dict.items()}

def EXTRACT_YEARLY_GRAPH(MG, NODE_SET=None):
    """
    - NODE_SET을 기본 노드세트로 하고, {Year: YearG}의 형태로 연도별 Graph를 담은 딕셔너리를 리턴한다.
    """
    Year_MG_Dict = EXTRACT_YEARLY_MULTIGRAPH(MG, NODE_SET=None)
    return {Year: MG_to_G(YearMG) for Year, YearMG in Year_MG_Dict.items()}


## DEFING FUNCTION DONE ################################################

def MAIN():
    MG = READ_MG()

    # BEST PRACTICE
    N_SONGs_Threshold = 5
    EDGE_Threshold = 3
    K_CORE_NUM = 4


    G = GRAPH_PREPROCESSING(
        MG, 
        N_SONGs_Threshold=N_SONGs_Threshold, 
        EDGE_Threshold=EDGE_Threshold, 
        K_CORE_NUM=K_CORE_NUM
    )
    print(f"NODE size: {len(G)}")
    print(f"EDGE size: {len(G.edges())}")
    
    print(f"EDGE WEIGHT SUM: {sum([e_attr['weight'] for u, v, e_attr in G.edges(data=True)])}")
    print(f"DIAMETER: {nx.diameter(G)}")
    print(f"DENSITY: {nx.density(G)}")
    print(f"AVG. Short Path Length: {nx.average_shortest_path_length(G)}")
    DATE_LST = [e_attr['dates'] for u, v, e_attr in G.edges(data=True)]
    DATE_LST = set(itertools.chain.from_iterable(DATE_LST))
    DATE_LST = sorted(DATE_LST)
    print(DATE_LST[:5])
    print(DATE_LST[-5:])
    
    print("=="*40)
    # CENTRALITY ANALYSIS 
    if False:
        TOP_N = 10
        if False: 
            TOP_N = 50
            PRINT_DEGREE(G, TOP_N=TOP_N)
            PRINT_WEIGHTED_DEGREE(G, TOP_N)

            PRINT_CLOSENESS(G, TOP_N=TOP_N)
            PRINT_WEIGHTED_CLOSENESS(G, TOP_N=TOP_N)
            
            PRINT_BETWEENNESS(G, TOP_N=TOP_N)
            PRINT_WEIGHTED_BETWEENNESS(G, TOP_N=TOP_N)
            PRINT_COMMUNICABILITY_BETWEENNESS(G, TOP_N)

            PRINT_PAGERANK(G, TOP_N=TOP_N)
        
    # EXTRACT COMMUNITY DETECTION RESULT
    if False: 
        print("== COMMUNITY DETECTION START")
        def most_valuable_edge_weight_ebc(inputG):
            ebc = nx.edge_betweenness_centrality(inputG, weight='distance')
            return max(ebc, key=ebc.get)

        def most_valuable_edge_ebc(inputG):
            ebc = nx.edge_betweenness_centrality(inputG)
            return max(ebc, key=ebc.get)
        STRATEGY_DICT = {
            'weight_ebc': most_valuable_edge_weight_ebc, 
            'just_ebc': most_valuable_edge_ebc
        }
        for STRATEGY, FUNC in STRATEGY_DICT.items():
            print(f"== COMMUNITY DETECTION START ::: {STRATEGY}")
            COMMUNITY_LOG = {
                'METADATA': {
                    "N_SONGs_Threshold": N_SONGs_Threshold, 
                    "EDGE_Threshold": EDGE_Threshold, 
                    "K_CORE_NUM": K_CORE_NUM, 
                    "STRATEGY": STRATEGY
                }, 
                'COMMUNITIES': {}
            }
            COMM_DETECT_GEN = nx.algorithms.community.girvan_newman(G, FUNC)
            for i, COMMs in enumerate(COMM_DETECT_GEN):
                COMMUNITY_LOG['COMMUNITIES'][i] = {}
                print(f"== GENERATION {i:3d} ================")
                for j, COMM in enumerate(COMMs): 
                    COMMUNITY_LOG['COMMUNITIES'][i][j] = {
                        'IDs': list(COMM), 'NAMEs': [aID_to_aNAME[aID] for aID in COMM]}
                    if len(COMM)>1:
                        print(f"---- COMMUNITY {j:2d}")
                        print([aID_to_aNAME[aID] for aID in COMM])
                        print("--"*60)
                print("=="*60)
            with open(f"COMMUNITIES/communities_log_{datetime.datetime.now()}.json", 'w') as f: 
                json.dump(COMMUNITY_LOG, f, indent=4, ensure_ascii=False)

    # DRAW COMMUNITY DETECTION 
    if False: 
        #COMMUNITY_JSON_FILE_NAME = "communities_log_2020-03-24 03:39:31.960301.json"
        # UNWEIGHT로 Community detection을 한 것이 훨씬 좋음
        # 우선 그림을 그리자 그림 저장 폴더이름 COMMUNITIES_FIGURES
        #pos = nx.kamada_kawai_layout(G, dist='weight')
        # iteration을 높일수록 좀더 깔끔하게 보이는 것 같은 느낌이 있음.

        def EXTRACT_GENERATION_COMMUNITIES(Generation=0):
            """
            - 특정 Generation에 속하는 Communities들만 가져온다.
            """
            COMMUNITY_JSON_FILE_NAME = "communities_log_2020-03-26 14:46:57.856437.json"
            COMM_DICT = json.load(
                open(f"COMMUNITIES/{COMMUNITY_JSON_FILE_NAME}", 'r'))
            if False:
                print("== METADATA ====== ")
                print(COMM_DICT['METADATA'])
                print("=="*30)
                print("== COMM DICT ====== ")
            return COMM_DICT['COMMUNITIES'][str(Generation)].values()

        def DRAW_COMMUNITIES_FIGURE(inputG, communities, pos, fig_file_name=None):
            """
            또한, inter-edge는 그리지 않는다.
            ------------------------------
            - parameter 
            communities는 [each_community]로 구성되어 있으며, 
            each_community: [ID] 로 구성되어 있다.
            """
            # 1명인 경우에는 그려주지 않음.
            communities = [comm for comm in communities if len(comm)>1]
            node_comm_dict = {}
            for i, comm in enumerate(communities):
                for node in comm: 
                    node_comm_dict[node]= i 
            # remove inter-communities edge 
            all_possible_intra_edges = []
            for comm in communities: 
                all_possible_intra_edges+=list(itertools.combinations(comm, 2))
            inputG = inputG.edge_subgraph(all_possible_intra_edges)
            ########################
            # Draw
            plt.figure(figsize=(30, 15))
            nx.draw_networkx_edges(
                inputG, pos=pos, edge_color='gray', width=2.0, alpha=0.5)
            nx.draw_networkx_nodes(
                inputG, pos=pos, node_size=300, 
                node_color=[node_comm_dict[aID] for aID in inputG], 
                cmap=plt.cm.rainbow)
            plt.xticks([]), plt.yticks([])
            plt.axis('off')
            # xlim의 경우 node가 짤리는 경우가 있어서 변경해주는 것이 필요함.
            plt.xlim(-1.01, 1.01), plt.ylim(-1.1, 1.1)
            #plt.tight_layout()
            if fig_file_name is None: 
                fig_file_name = f"COMM_GENERATION_{generation:03d}.png"
            plt.savefig(f"COMMUNITIES_FIGURES/{fig_file_name}", dpi=100)
            plt.close()
        ### DEFINE FUNTION DONE ##########

        # DRAW FIGURE
        if False:
            pos = nx.spring_layout(G, iterations=50)
            # COMMUNITY를 나누지 않았을때의 그림을 그림.
            DRAW_COMMUNITIES_FIGURE(G, communities=[[n for n in G]], pos=pos, fig_file_name="Entire_G.png")
            for generation in range(0, 200): 
                print(f"== GENERATION {generation}")
                GENERATION_COMMs = EXTRACT_GENERATION_COMMUNITIES(Generation=generation)
                GENERATION_COMM_IDs = [COMM["IDs"] for COMM in GENERATION_COMMs]
                GENERATION_COMM_NAMEs = [COMM["NAMEs"] for COMM in GENERATION_COMMs]
                for comm_i, COMM_NAME in enumerate(GENERATION_COMM_NAMEs):
                    print(f"---- {comm_i}")
                    if len(COMM_NAME)>1:
                        print(COMM_NAME)
                # 이제 COMMs 에는 community별 ID가 들어있음. 
                # 그림을 그릴 때, 없어진 edge들은 그려주지 않도록 하자. 
                if True: 
                    DRAW_COMMUNITIES_FIGURE(inputG=G, communities=GENERATION_COMM_IDs, pos=pos)
                print("======"*20)

    #====== COMMUNITY DETECTION DONE ==================================
    # YEARLY CHANGE TRACKING
    if True: 
        # 여기서, 연도별 centrality의 변화 
        # 연도별 connected_component의 변화 등을 뽑아서 피피티에 정리할 것.
        NODE_SET = [aID for aID in G]
        YearMG_DICT = EXTRACT_YEARLY_MULTIGRAPH(MG, NODE_SET=NODE_SET)
        print(f"YEARS: {YearMG_DICT.keys()}")
        
        Year = 2019

        print("--"*30)
        if True: 
            Year = str(Year)
            YearMG = YearMG_DICT[Year]
            YearG = MG_to_G(YearMG)
            print(f"== Year {Year} ===============")
            print(
                f"Node Size: {len(YearMG)} ::: Edge Size: {len(YearG.edges())} ::: Density: {nx.density(YearG)}")
            print("--"*30)
            # PRINT COMPONENT 
            if False: 
                CONN_COMPONENTS = nx.connected_components(YearMG)
                CONN_COMPONENTS = sorted(CONN_COMPONENTS, key=lambda x: len(x), reverse=True)
                for i, component in enumerate(CONN_COMPONENTS):
                    component = sorted(component, key=lambda aID: YearMG.degree(aID), reverse=True)
                    componentMG = YearMG.subgraph(component)
                    componentG = YearG.subgraph(component)
                    print(f"---- component {i:2d} :: NODE SIZE: {len(componentMG)}:: DIAMETER: {nx.diameter(componentMG)}")
                    componentIDs = sorted([aID for aID in component], key=lambda aID: componentG.degree(aID), reverse=True)
                    print([aID_to_aNAME[aID] for aID in componentIDs])

                    if True: 
                        if i==0:
                            for generation, COMMs in enumerate(nx.algorithms.community.girvan_newman(componentG)):
                                print(f"== GENERATION {generation:2d}")
                                for j, commIDs in enumerate(COMMs):
                                    commG = componentG.subgraph(commIDs)
                                    sorted_commIDs = sorted(commIDs, key=lambda x: componentG.degree(x), reverse=True)
                                    sorted_commNAMEs = [aID_to_aNAME[aID]for aID in sorted_commIDs]
                                    if len(sorted_commNAMEs)>2:
                                        print(f"---- COMMUNITY :: {j:2d} :: Density : {nx.density(commG)} :: Diameter: {nx.diameter(commG)}")
                                        print(sorted_commNAMEs)
                                print("=="*30)
                                if generation > 70:
                                    break
            # PageRank의 상위권 멤버들의 ego-multi-graph를 구성하여 주요 곡들 살펴보는 기능
            if True: 
                pagerank_df = PRINT_PAGERANK(YearG, TOP_N=20)
                print("=="*30)
                if True: 
                    for i, row in pagerank_df.iterrows():
                        centerID, centerNAME = row['aID'], row['aNAME']
                        EGO_MG = nx.ego_graph(YearMG, centerID)
                        EGO_MG.remove_edges_from([e for e in EGO_MG.edges() if centerID not in e])

                        print(f"---- {centerNAME}")
                        print(f"Neighbours: ")
                        print([aID_to_aNAME[nbrID] for nbrID in EGO_MG.nodes()])
                        print(f"Songs: ")
                        songs_dict = {}
                        for u, v, k, d in EGO_MG.edges(keys=True, data=True):
                            songs_dict[k] = d['title']
                        for j, (k, v) in enumerate(songs_dict.items()):
                            print(v)
                            if j>10:
                                break
                        print("=="*50)
                        if i>20:
                            break 
    # DRAW ALL
    if False: 
        # 그림 그릴 때는 Edge_Threshold를 몇 개 더 줄여도 좋을것 같은데 
        # 최소한 position 잡을 때만 이라도, 좀 더 큰 값으로 정해서 잡아줘도 좋을듯. 
        # 다만, 이 그름의 경우는, 그린 다음, COMMUNITY DETECTION을 수행하여, 그 변화를 보여주는 것이 좋을듯. 
        if False: 
            print(f"== NODE SIZE: {len(G)}")
            print(f"== EDGE SIZE: {len(G.edges())}")
            pos_dict = {
                'spring': nx.spring_layout(G), 
                'fruchterman': nx.fruchterman_reingold_layout(G), 
                'kamada': nx.kamada_kawai_layout(G, weight='distance')
            }
            for k, pos in pos_dict.items():
                plt.figure(figsize=(40, 40)) 
                # DRAW EDGEs
                EDGE_weight_lst = [ e_attr['weight'] for u, v, e_attr in G.edges(data=True)]
                EDGE_weight_lst = [w/max(EDGE_weight_lst) for w in EDGE_weight_lst]
                nx.draw_networkx_edges(
                    G, pos=pos, edge_color='red', 
                    width=2.0, alpha=0.5
                )
                # DRAW NODEs
                MAX_NODE_SIZE, MIN_NODE_SIZE = 1000, 500
                degree_lst = [G.degree(n) for n in G]
                NODE_SIZEs = [(G.degree(n) - min(degree_lst))/(max(degree_lst) - min(degree_lst))for n in G]
                NODE_SIZEs = [x*(MAX_NODE_SIZE - MIN_NODE_SIZE)+MIN_NODE_SIZE for x in NODE_SIZEs]
                nx.draw_networkx_nodes(
                    G, pos=pos, node_size=500, 
                    node_color=[deg/max(degree_lst) for deg in degree_lst], 
                    cmap=plt.cm.Blues, 
                    vmin=0.5
                )
                # DRAW NODES LABELs
                labels = {aID: aID_to_aNAME[aID] for aID in G.nodes()}
                nx.draw_networkx_labels(
                    G, pos=pos, labels=labels, 
                    font_family='BM JUA_OTF', font_size=10)
                # 
                plt.axis('off'), plt.xticks([]), plt.yticks([])
                plt.xlim(-1, 1), plt.ylim(-1, 1)
                plt.savefig(f"figures/G_{k}.png", dpi=50)
                plt.close()
            print(f"== DRAW GRAPH DONE")
        ##########################################
        
        if False:
            # 연도별 변화.
            # 이 아이는 다만, 변화를 봐야 하니까, k_core를 좀 더 높이자.
            NODE_SET = [aID for aID in G]
            # fig: 반복해서 그려주는 도화지.
            fig = plt.figure(figsize=(6, 6))
            pos = nx.kamada_kawai_layout(G, weight='distance')
            frames = []
            subMG = MG.subgraph(NODE_SET).copy()
            for Year in range(1999, 2021):
                for Month in range(1, 13):
                    Month = f"{Month:02d}"
                    print(f"== {Year} - {Month}")
                    year_month_edge = []
                    for u, v, k, d in subMG.edges(data=True, keys=True): 
                        if d['date'][:7]==f"{Year}-{Month}":
                            year_month_edge.append((u, v, k))
                    YearMonthG = subMG.edge_subgraph(year_month_edge).copy()
                    frames.append((Year, Month, YearMonthG))
            ## MAKE VIDEO 
            
            def animate_func(each_frame):
                """
                매 frame마다 요소의 attribute만 업데이트해주는 경우
                """
                Year, Month, YearMonthG = each_frame
                plt.clf()
                nx.draw_networkx(YearMonthG, pos=pos, node_size=300)
                plt.axis('off')
                plt.title(f"{Year}-{Month}")
                plt.xticks([]), plt.yticks([])
                # FIX xlim, ylim
                plt.xlim(-1, 1), plt.ylim(-1, 1)
                print(f"{Year}-{Month}")
                #plt.close()
            plt.figure(figsize=(10, 10))
            writer = animation.writers['ffmpeg'](fps=25)
            my_animation = animation.FuncAnimation(fig,
                                                   animate_func,
                                                   frames=frames,
                                                   interval=200)
            my_animation.save("NetworkChange.mp4", writer=writer, dpi=256)

            print(f"== DRAW Year-GRAPH DONE")

## DEFING MAIN FUNCTION DONE ################################################


MAIN()

```
