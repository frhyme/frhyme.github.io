---
title: 한국 힙합씬 피쳐링 네트워크 분석 - 2편 - Data Collection Wisely
category: python-libs
tags: python python-libs selenium data-crawling networkx centrality
---

## 한국 힙합씬 피쳐링 네트워크 분석. 

- 저는 대상/현상을 네트워크로 모델링하고 네트워크 적인 분석 법을 사용하여 대상 네트워크를 분석하는 일을 주로 수행합니다. 그리고, 그러다보니, 세상의 많은 현상들을 결국 "네트워크"적으로 바라보게 되죠. 
- 동시에 저는, 한국 힙합의 오랜 팬이기도 합니다. 힙합음악의 흥미로운 점은, 여러 뮤지션들이 다른 뮤지션들의 음악에 협업의 이름으로 참가하는 일이 매우 활발하다는 것이죠. 
- 저는 궁금했습니다. 과연, 한국 힙합의 피쳐링은 어떤 형태로 구성되어 있을까? 만약 이를 네트워크로 구성한다면 어떻게 구성해야 할까? 구성된 네트워크는 어떤 분석을 하면 재미있는 결과가 나올 수 있을까? 와 같이요. 
- 그래서, 저는 그동안의 한국 힙합 데이터를 모두 웹에서 크롤링하여 네트워크를 구성하고 그 결과를 정리하였습니다. 
- 분석 결과는 [한국 힙합 피쳐링 네트워크 분석](https://docs.google.com/presentation/d/1zkOGBTD0UTaeoxYLxkPohNXaaKWYjVXfdbHgrli8xms/edit#slide=id.p) 에서 발표자료로 보실 수 있습니다.

## 한국 힙합씬 네트워크 분석하기 - 2편 - Scope of KOREAN HIPHOP

- 데이터를 수집하려고 보니, 조금 모호한 부분이 발생합니다. "한국 힙합"은 무엇일까요? 
- 즉, 제가 분석하려고 하는 대상인 "한국 힙합"은 무엇이며, 어디부터 어디까지를 포함한다고 생각하면 될까요? 
- 이즈음부터는 사람들에게 매우 다양한 층위의 답이 존재할 것이라고 생각합니다. 가령 "엠씨몽을 힙합으로 봐야 하는가?", "매드클라운은 요즘 발라드 랩을 하는데 힙합으로 봐야 하는가?"와 같은 질문들이 있을 수 있겠죠.
- 그런데, 저는 이 질문은 꽤 논쟁적이고 소모적이라고 생각합니다. 그리고 그 경계는 제가 임의로 한정짓는 것 또한 딱히 필요하다고 생각하지 않았죠. 

## 일단 모아보자: epic-fail 

- 그래서, 처음에는 그냥 제 머리속에서 생각나는 대로 "이 사람은 속한다고 봐야지"라고 하면서 대충 리스트를 만들기 시작했습니다. 뭐, "더콰이엇"을 넣고, "팔로알토"도 넣고 이런식으로 하나씩 막 집어넣은 것이죠. 그런데, 이를 반복하고 그리고 결과를 대략 분석하면서 보니, 데이터의 일관성이 무너지는 것 같았습니다. 
- 아무래도 제가 선호하는 아티스트들 중심으로 데이터를 모으게 되고, 이는 결국 "제 기준에 overfitting된 국내 힙합"이 되는 것이죠. 뿐만 아니라, 제가 빠짐없이 모든 랩퍼들을 채워넣었다는 확신이 들지 않았습니다. 
- 따라서, 좀 더 일관적인 규칙을 만드는 것이 필요해졌죠.

## Wise Data Collection: 가두리양식. 

- 그래서, 저는 조금 다른 방식을 선택했습니다. 제 마음대로 "가두리양식"이라고 이름을 붙였죠. 해당 알고리즘의 순서는 다음과 같습니다. 

1) **초기해 설정**: 가령, <MC Meta>, <더 콰이엇>, <저스디스> 라는 3명의 뮤지션가 있다고 하겠습니다. 그리고 이 3명은 매우 높은 확률로(100명 중 99명에게는) "국내 힙합 뮤지션"라고 인정을 받겠죠. 
2) **네트워크 구축**: 이 3명이 참여한 모든 음악과 참여자 정보를 가져와서 Collaboration 네트워크를 구축합니다. 
3) **최근접 Artist 추출**: 네트워크의 Artist 중에서 초기해들인 <MC Meta>, <더 콰이엇>, <저스디스>와의 "거리의 합"이 가장 작은 Artist를 찾습니다. 예를 들어 <빈지노>가 나온다고 해보겠습니다. 그리고 저의 경우는 이 거리를 측정할 때 weighted distance를 사용하여 거리를 측정하였습니다.
4) **초기해 재설정**: <MC Meta>, <더 콰이엇>, <저스디스>, <빈지노>를 초기해로 하여, 다시 2)로 돌아갑니다. 그러면, 이 4명과 가장 가까운 새로운 Artist가 나오겠죠. 이를 계속 반복하면서 네트워크의 변화 양상을 관찰합니다. 그리고 만약 이상한 뮤지션을 도출하는 것 같다, 라는 생각이 든다면 그 때 알고리즘을 종료합니다.

### Limitation

- 다만, 처음에는 "오 합리적인 방식이다"라고 생각할 수도 있지만, 이 또한, "초기해"를 어떻게 넣느냐에 따라서 결과가 판이하게 달라지게 됩니다. 
- 가령 초기해를 극단적으로 <딥플로우>, <넉살>, <던밀스> 라고 정한다면, 초기에는 아주 빠르게 비스메이저에 있는 사람들이 추가되겠죠. 그리고 비스메이저에 가까운 많은 사람들이 다 추가된 다음에는 새로운 뮤지션을 탐색하는 것이 어려워집니다.
- 우리는 "거리"를 측정하죠. 따라서 만약 "서울"에 있는 사람들만으로 초기해를 구성한다면, 이후에는 "부산"에 있는 사람과 "광주"에 있는 사람들간의 거리의 합이 큰 차이가 없어집니다. 만약, 우리가 초기해를 "부산"에 있는 사람과 "서울"에 있는 사람들을 고르게 선택한다면, 해를 확장해가는 것이 유리하겠죠. 
- 따라서, 가능하면 이 "초기해"를 너무 촘촘하지 않게, 그러면서도 빈틈없이 설정해주는 것이 필요합니다. 
- 따라서, 저는 고민 끝에 초기해를 "한국 힙합씬에 있었던 각 레이블 혹은 크루의 대표들"이라고 정의해주고 알고리즘을 수행하였습니다. 그리고 이렇게 설정한 다음 알고리즘을 실행해보니 넓은 영역에서 대부분의 랩퍼들을 빠짐없이 포함해주더군요.


## CODE



### INIT MultiGraph

- 초기해로 설정한 ID들을 `INITIAL_IDs`으로 넘겨주고, 이를 우리가 이전에 크롤링하여 로컬에 json 파일로 저장해둔 것들을 읽어서, MultiGraph에 업데이트해줍니다. 해당 기능은 `UPDATE_MG_by_song_data_dict`에서 수행하는데, 이 부분은 다음 단락에서 설명드리겠습니다.

```python
def INIT_MG(MG, INITIAL_IDs):
    """
    - MG를 init_searchIDs에 속한 aID에 대해서 Node, Edge를 업데이트해줌 
    - 초기해를 설정해주기 위해서도 쓰이고, 이미 이전에 같은 config으로 실행한 결과가 있을 경우 
    그 정보를 그대로 업데이트해줌
    """
    for i, aID in enumerate(INITIAL_IDs):
        #print(f"== INIT PROCESS {i:3d} ::: READ DATA of {aID} ::: {aID_to_aNAME[aID]}")
        if aID+".json" in os.listdir("song_data/"):  # 무조건 TRUE여야겠지만
            song_data_dict = json.load(open(f"song_data/{aID+'.json'}", "r"))
            UPDATE_MG_by_song_data_dict(MG, song_data_dict)
            if i%10==0:
                print(f"== INIT PROCESS {i:3d} ::: MG - AFTER ::: NODE SIZE: {len(MG):5d}, EDGE SIZE: {len(MG.edges()):5d}")
        else:
            print("=== ERROR ===")
    print("== CONSTRUCT MG DONE by initial aIDs")
    #print("=="*40)
```

### UPDATE MultiGraph

- 우선, 저는 데이터를 MultiGraph로 표현하여 관리합니다. MultiGraph는 edge의 중복, 즉 node간에 여러 edge가 허용되는 Graph를 말하죠. 
- 이렇게 표현한 이유는 같은 관계라도, 여러번의 노래에서 작업을 했을 수 있기 때문이죠. 
- 함수는 각 노래에 대한 정보가 포함된 json 파일을 dictionary로 읽은 후에, 이를 `MG`라는 Graph에 업데이트해주는 기능을 가지고 있습니다.
- 그리고 관련된 정보들을 node attribute, edge attribute에 정리해서 넘겨주기도 합니다.

```python
def UPDATE_MG_by_song_data_dict(MG, song_data_dict):
    """
    - song_data_dict를 MG에 업데이트함. 중복되지 않게, songID를 key로 해서 업데이트함.
    - MG: out-of-block 에 존재하는 MultiGraph
    """
    for songID, songATTR in song_data_dict.items():
        songTITLE = " ".join(songATTR['title'].split("]")[1:]).strip()
        songDATE = [x for x in songATTR['metadata'] if "공표일자" in x][0].split(":")[1]
        songDATE = songDATE.strip().split(" ")[0]
        # 작사, 작곡에 참여한 경우만 포함시키기로 함.
        artist_in_this_song = (
            aID for aROLE, aID in songATTR['artists'] if aROLE in {'A', 'C', 'CA'}  and aID != "")
        artist_in_this_song = (
            aID for aID in artist_in_this_song if aID.lower() != 'z9999900')
        artist_in_this_song = set(artist_in_this_song)
        artist_edges = itertools.combinations(artist_in_this_song, 2)
        MG.add_edges_from(
            [(u, v, songID, {'title': songTITLE, 'date': songDATE}) for u, v in artist_edges])
    # UPDATE MG node and its n_songs
    for u in MG:
        u_songs_set = set(itertools.chain.from_iterable([MG[u][v] for v in MG[u]]))
        MG.nodes[u]['n_songs'] = len(u_songs_set)
```


### MG to G and filtering

- `MG_to_G_and_FILTER`는 만들어진 MG(MultiGraph)를 Graph로 변환해주고 몇 가지 전처리를 수행해주는 함수입니다.
- 굳이 MultiGraph로 잘 관리되고 있는 데이터를 Graph로 변경해준 이유는, Node들간의 거리를 계산해주기 위함이죠. 
- 서로 작업을 많이 했을 수록 거리적으로 가깝다, 라고 생각하고 Graph를 만든 다음 거리를 계산하였습니다. 그리고 발매한 곡들의 수가 적거나, 협업의 수가 적거나 하는 등, 적합하지 않은 뮤지션들을 제외하는 전처리를 이 함수에서 수행합니다.

```python
def MG_to_G_and_FILTER(MG, N_SONGs_Threshold=1, EDGE_Threshold=1, NODE_DEG_Threshold=5):
    """
    - MG를 전달받아서, G를 FILTERING하여 리턴한다.
    """
    subMG = MG.subgraph((nID for nID in MG if MG.nodes[nID]['n_songs'] >= N_SONGs_Threshold))
    subG = nx.Graph()
    subG.add_nodes_from([(nID, nATTR)for nID, nATTR in MG.nodes(data=True)])
    for u, v in subMG.edges():
        if subG.has_edge(u, v) == True:
            subG[u][v]['weight'] += 1
        else:
            subG.add_edge(u, v, weight=1)
    # UPDATE distance
    nx.set_edge_attributes(
        subG, {(u, v): 1.0/e_attr['weight'] for u, v, e_attr in subG.edges(data=True)}, name='distance')
    subG = subG.edge_subgraph([
        (u, v) for u, v, e_attr in subG.edges(data=True) if e_attr['weight'] >= EDGE_Threshold])
    # degree가 NODE_DEG_Threshold보다 작은 노드 삭제
    subG = subG.subgraph([nID for nID, deg in nx.degree(subG) if deg >= NODE_DEG_Threshold])
    return  subG.copy()
```


### SEARCH_ID_TRAVERSAL_WEIGHTED_DISTANCE

- 앞서 만든 함수들을 포함하여, 아래와 같이 하나의 함수에 정리하였습니다. 
- 초기해(`INITIAL_IDs`)로부터, 주어진 방식으로 필터링을 진행하면서, `N`번 새로운 아티스트를 찾아가고 그 결과를 리턴하는 함수입니다.
- 거리는 weighted distance를 사용해서 측정하게 되죠.

```python
def SEARCH_ID_TRAVERSAL_WEIGHTED_DISTANCE(INITIAL_IDs=["W0625700"], N=10, N_SONGs_Threshold=2, NODE_DEG_Threshold=2, EDGE_Threshold=2):
    """
    INITIAL_IDs 들을 초기해로 잡고, 여기서부터 필터링하고, 점차 가장 가까운 Node들을 탐색하면서 
    다양한 ID를 탐색하고 그 결과를 리턴하는 함수입니다.
    """
    def FIND_NEXT_by_distance(MG, TARGET_IDs=[], SEARCHED_IDs=[]):
        """
        - 현재 MG에 대해서 NODE_Threshold, EDGE_Threshold 기준을 충족하는 subG에 대해서 
        - SEARCH_IDs 내 모든 노드들까지의 거리가 가장 짧고, SEARCH_IDs에 속하지 않는, 노드를 찾아서 리턴. 
        -----
        TARGET_IDs: 초기해. 대상이 되는 target등의 ID. 
        SEARCHED_IDs: 이미 이전에 탐색했던 IDs. 
        """
        G = MG_to_G_and_FILTER(
            MG, N_SONGs_Threshold=N_SONGs_Threshold, EDGE_Threshold=EDGE_Threshold, NODE_DEG_Threshold=NODE_DEG_Threshold)
        print(f"---- COMPUTE ::: G -  NODE SIZE: {len(G):5d}, EDGE SIZE: {len(G.edges()):5d}")
        distance_dict = {}
        for u in G.nodes():
            if u not in SEARCHED_IDs:
                u_distance_sum = 0 
                for v in TARGET_IDs:
                    try:
                        u_distance_sum+=nx.shortest_path_length(subG, u, v, weight='distance')
                    except:# 연결되어 있지 않을때는 다음처럼 매우 큰 값을 집어넣음.
                        u_distance_sum+=10
                distance_dict[u] = u_distance_sum
            else: 
                continue
        return min(distance_dict, key=lambda k: distance_dict[k])
    
    MG = nx.MultiGraph()
    INIT_MG(MG, INITIAL_IDs)
    SEARCHED_IDs = list(INITIAL_IDs)
    #ALREADY_SEARCHED_IDs = set()
    for i in range(len(INITIAL_IDs), N):
        next_aID = FIND_NEXT_by_distance(MG, INITIAL_IDs, SEARCHED_IDs)
        SEARCHED_IDs.append(next_aID)
        #print(f"== ADD PROCESS {i:3d} ::: MG - BEFORE ::: NODE SIZE: {len(MG):5d}, EDGE SIZE: {len(MG.edges()):5d}")
        print(f"== ADD PROCESS {i:3d} ::: {next_aID}    ::: {aID_to_aNAME[next_aID]} will be UPDATED")

        if next_aID+".json" in os.listdir("song_data/"):
            song_data_dict = json.load(open(f"song_data/{next_aID+'.json'}", "r"))
        else:  # 이전에 데이터를 수집한 적이 없으므로 새로 읽음.
            options = Options()
            options.headless = True
            browser = webdriver.Firefox(options=options)
            song_data_dict = extract_info_from_artistID(
                browser=browser, artistID=next_aID)
            browser.quit()
        # UPDATE MG edge.
        UPDATE_MG_by_song_data_dict(MG, song_data_dict)
        print(f"== ADD PROCESS {i:3d} ::: MG - AFTER  ::: NODE SIZE: {len(MG):5d}, EDGE SIZE: {len(MG.edges()):5d}")
        print("--"*40)
    return {
        'N_SONGs_Threshold': N_SONGs_Threshold, 
        'NODE_DEG_Threshold': NODE_DEG_Threshold, 
        'EDGE_Threshold':EDGE_Threshold, 
        'INITIAL_IDs': list(INITIAL_IDs), 
        'SEARCHED_IDs':{aID:aID_to_aNAME[aID] for aID in SEARCHED_IDs}
    }
```

## wrap-up

- 결론적으로는 초기해를 설정하고, 현재 초기해에서 가장 가까운 노드들을 찾아나가는 방식으로 "한국힙합"을 정의하였습니다. 보다 정확하게 말하자면, "한국힙합씬에 속해 있는 사람들"을 추려낸 것이죠. 
- 다만, 처음부터 이렇게 했던 것은 아니며, 다음의 방식들을 약간 heuristic으로 사용하였습니다.
    1) 뮤지션 A의 작업물들을 모두 데이터로 가져오고, 이 데이터에 포함된 새로운 뮤지션들을 정리하면서, 적합한 뮤지션들만 남기는 방식. 
    2) 초기해를 1명으로만 정하고 데이터를 긁어와서 뮤지션 네트워크를 구성하고, 현재 네트워크에 대해서 centrality, pagerank등이 높은 아이에 대해서 다시 데이터를 탐색하는 방식. 
    3) 전체 네트워크에서 closeness-centrality가 가장 높은 아이를 선택해서 데이터를 재 탐색해주는 방식. 
- 확실히 점진적으로, 전에 비해서 좋아진 것은 사실입니다. 초기에는 좀 나이브하게 진행했던 것 같고, 두번째와 세번째에서 조금 나아졌지만, 네트워크 내 노드의 수가 커지면서, 탐색의 범위가 급증할 수 있다, 라는 사실을 간과했던 것이 문제였습니다. 
- 가령, 1)의 경우는 지나친 오버피팅 문제를 가지고 있습니다. 제 두뇌의 범주에서 "힙합"을 정의하고 거기에 속하는 뮤지션들만 검색하여 네트워크를 모으죠. 이 경우, 우리가 대상으로 하는 "전체 힙합"의 부분집합만을 대상으로 분석하게 됩니다. 
- 하지만, 2)와 3)의 경우는 네트워크를 구성하면서 그 과정에서 "기존에 검색하지 않았지만 뮤지션들과 관계 있는 새로운 뮤지션"들을 자동으로 탐색하게 됩니다. 1)에 비해서 탐색의 범위가 넓어졌으며, 보다 generalization에 가깝죠. 그리고 이제는 "과학적인 방식으로 탐색했다"라고 말할 수 있는 가능성이 생겨나기 시작합니다. 
- 그러나, 2), 3)에서 빈번히 등장하는 문제는 다시 underfitting이죠. 알고리즘이 진행되면서, 전체 네트워크에 포함된 노드의 수는 기하급수적으로 증가합니다. 새로운 노드가 계속 추가되고, 특히 그 과정에서 저는 노드에 대해서 "노드가 발표한 곡의 수"와 "노드간의 협업의 수"를 중심으로 그래프를 전처리한 다음 중요한 노드를 선정하기는 했지만, 그래도 일정 시간이 지나면 항상 '김도훈'이라거나, 하는 메이저한 음악 관련자들을 선택하게 되더군요. 
- 여기서, 제가 실수한 것은, 우선 node를 필터링할 때, degree 값을 고려하지 않고, "발표한 노래"나, "관계의 수"등에 집착했다는 것이죠. 어떤 노드가 확실히 하나의 네트워크 내에 포함되어 있다면, 사실 degree값이 높겠죠. 즉, 생각을 해보면 degree 값을 고려하는 것이 필터링하는 측면에서 매우 좋습니다만, 그때는 그 생각을 잘 하지 못했던 것 같아요. 
- 그리고, 필터링과 유사한 이야기겠지만, 전체 네트워크의 (필터링된) 모든 노드를 대상으로 centrality 등의 계산법을 사용하여 중요한 노드를 찾습니다. 따라서 초기에는 그 해를 잘 찾아주지만, 해가 진행되면서, 점차 그 범위가 확장되어 가고 결국에는 아예 다른 노드들을 찾는 여정을 떠납니다. 그러고는 돌아오지를 않죠. 
- 그래서, 전체 네트워크에 대해서 거리 등을 측정하는 것이 아니라, "명확한 초기해"들을 설정하고, 이 초기해를 벗어나지 않는 선에서 탐색하는 것이 좋겠다, 그리고 그 추이를 보면서 초기해를 변경하는 것이 좋겠다, 라는 생각을 하게 되었죠. 따라서, 여기서부터는 전체 네트워크에 대해서 값을 결정해주는 것이 아니라, "초기해들부터의 거리 합"이라는 기준으로 가장 가까운 노드들을 결정해줍니다. 그리고 이를 적용하여 알고리즘을 진행해본 결과, 이전에 비해서 훨씬 우수한 방식으로 
- 다만, 아직 적용하지 못한 하나의 아이디어는, voterank등을 이용하여, 네트워크를 커버할 수 있는 최대한의 노드를 선정한 다음, 그 노드들을 초기해로 설정하여 진행했다면 훨씬 효과적으로 진행할 수 있지 않았을까? 하는 아쉬움은 조금 있습니다. 즉, 저는 각 크루, 레이블의 대표를 사용하여 초기해를 설정하였습니다. 하지만, 그런 방법이 아니라, voterank를 사용하여, 전체 네트워크를 가장 잘 커버할 수 있는 노드집합을 정하고, 알고리즘을 진행하였다면 좀 더 효율적으로 "힙합씬에 속하는 노드"를 탐색할 수 있지 않을까? 하는 아쉬움이 조금 있어요.