---
title: R&D 지식지도를 만들어봅시다. 
category: project
tags: python-lib python networkx matplotlib scopus

---

## scopus 데이터를 이용한 저자 키워드 데이터 자동화하기 

- 물론 '텍스트'를 다루는 대부분의 분석의 경우는 자동화가 어렵습니다. 다양한 이유가 있겠으나, 제가 아는 범주에서의 문제는 '예외처리'죠. 텍스트는 예외가 많습니다. 특히, 키워드 분석을 해야 하는 경우에는 같은 키워드가 다르게 표현되어 있는 경우들이 있다는 것이 문제입니다.
- 예를 들어서, 'systems'와 'system'은 사람 눈으로는 너무도 당연히 같은 의미죠. 이럴때는 'systems'를 'system'으로 변환해주는 것이 필요합니다. 사람 눈으로는 이를 하나하나 파악하면서 진행할 수 있기는 한데, '사람의 눈'으로 보니까 아무래도 일관성이 떨어질 수 있다는 한계를 가집니다. 
    - 특히, 여기서 단지 `syntatic`한 형식이 아니라 `semantic`한 관점에서 보자면, `information system`과 `management information system`이라는 두 가지 키워드는 어떻게 해석해야 할까요? 어떤 사람은 이 두 키워드를 `information system`으로 통일하는 경우가 있을 것이고, 어떤 사람은 이 둘을 다른 개념으로 두고 진행할 수 있을 것입니다. 
    - 사람마다도 다르지만, 한 사람이 다른 분야에 대해서 데이터를 필터링하는 수준도 상이할 수 있습니다. 잘 아는 분야에 대해서는 개별 개념을 크게 잡기 때문에 가급적 통일하는 것을 지양하는 반면, 잘 모르는 분야에 대해서는 키워드별 개념의 범위를 좁게 잡아서 너무 단순화할 수 있죠. 
    - 결과적으로 말하자면 저는 인간을 믿지 않습니다. 이를 객관적이고 일관적으로 진행하기 위해서는 결국 기계의 힘을 빌리는 것만이 답이 아닌가!! 라는 생각을 해봅니다만, 어떻게 해야 할지 모르겠네요. 
- 아무튼 제가 하려는 것은 비교적 단순합니다. 다시 말하면 제한적입니다. 

## program specification

- input: scopus에서 다운 받은 엑셀 파일(columns name: `Author Keywords`, `Year`, `Abstract`)
- output-1: 결과를 담은 엑셀 파일 
    - 기본 통계
    - 키워드 빈도 분석
        - 전체 기간 빈도 상위 키워드 
        - 연도별 빈도 상위 키워드
    - 논문 초록 분석
        - 초록에서 뽑아낸 빈도 상위 명사구(noun phrase)
    - 키워드 centrality 분석 
        - 비고) 여기서는 해당 graph가 단일 graph인지, 혹시 연결되지 않은 작은 edge들이 있다면 무시하고 가장 큰 놈만으로 해주는 것이 필요할수도 있음. 이 부분을 자동화할 수 있느냐? 가 궁금하기는 함.
        - 전체 기간 centrality별 상위 키워드
            - 칼럼별로 개별 centrality 상위 키워드 출력
        - 연도별 weighted degree centrality 상위 키워드 변화 
        - 연도별 closeness centrality 상위 키워드 변화
        - 연도별 betweeness centrality 상위 키워드 변화
        - 연도별 pagerank 상위 키워드 변화
- output-2: 결과를 담은 ppt 파일
    - 기본 통계
    
- required module
    - keyword filtering: 

## 소프트웨어 엔지니어링 혹은 코딩 잘하기 

- 어느 정도의 규모를 넘어가는 코드(특정한 라인을 중심으로 잡을 수도 있습니다, 예를 들어 몇 라인 수 넘는 경우 등) 혹은 프로그램의 경우 처음에 계획적으로 요구사항을 분석한다거나, 중복 문제를 해결하기 위해서 소프트웨어를 디자인한다거나 하지 않고 그냥 '일단 코딩부터 시작~'하다보면 코드는 늘어나고 따라서 고치는 것이 쉽지 않고(legacy), 중복을 없애고 효율적으로 짤 수 있을 것 같고, 더 제너럴하게 함수간의 관계를 설정할 수 있을 것 같은데, 어디부터 시작해야 할지 애매해지는 순간들이 옵니다. 
- 이럴때, 다시 원론으로 돌아가서 소프트웨어를 어떻게 설계하는 것이 좋을까? 에 대해서 돌이켜보는 습관이 필요한 것 같습니다. 굳이 '소프트웨어 엔지니어링 개론'같은걸 짤 필요는 없고, 지금까지 만든 코딩을 글이나 포스트잇 같은걸로 복기해보면 좋을 것 같네요. 
- 사실, 처음부터 빡세게 설계를 하고 들어가는 뭐, 이런걸 `waterfall`이라고 하던가요, 그런것도 좋지만 저는 하다가 막히면 다시 돌아가고 다시 돌아가고 뭐 그런 형태가 더 좋을 것 같아요. 실전에 들어가지 않으면 생각하지 못하다보니 하핫
- 아무튼 이미 만든 코드를 다시 복붙하고 수정하면서 좀 더 깔끔하게 만들었습니다. 

## just do it

- 아무튼 간에, 제일 중요한 것은 "기본 데이터 구조"를 무엇으로 잡을것인가? 가 될것 같아요. 다르게 말하면 일종의 `workflow` 혹은 `data flow`라고도 할 수 있겠네요. 개별 키워드를 바꾸는 일이 많기에 여러 함수에서 나누어서 바꾸어버리면 나중에 '무엇이 바꾸었는지' 헷갈리기 쉽습니다. 가능하면 기본이 되는 `pd.DataFrame`에 변화되는 것을 하나로만 저장하는 것이 좋습니다. 
- 현재는 `jupyter notebook`으로 돌리고 있습니다. 그런데 총 논문의 수는 15000개를 넘고, 개별 키워드가 5개씩이라고만 해도, 75000개, 여기서 유니크한 것만 고려해서 뭐 2만 개라고만 해도 4억개의 edge가 발생할 수 있습니다(물론 발로 계산했습니다만).
- 이렇게 해서는 시간이 너무 오래 걸려요. 특히 `jupyter notebook`에서는 시간 제한이나 메모리 제한이 걸려 있어서 더 오래걸립니다. 그래서 해당 코드를 복사해서 파이썬 쉘에서 돌리려고 합니다(별 차이 없으려나요? 흠)

## make it efficient

- jupyter notebook 과 python shell의 차이라기 보다 코딩을 효율적으로 하지 못한 것이 문제다. 10000개의 논문의 서지정보라면 저자 키워드가 개별적으로 5개만 있다고 해도 5만 개 여기서 중복을 제외한다고 해서  유니크한 키워드가 10000개라고 하면 네트워크 분석 시에 10000 * 10000 개의 계산이 들어가게 된다. 특히 `betweenness centrality`를 계산하려면 10000 * 10000 * 10000이 될테고, 
- 당연히 계산 시간이 폭발적으로 늘어나게 된다. 당연한것 아닌가. 그래서 임의로 빈도 수가 일정 이상을 넘는 키워드에 대해서만 처리해주는 것이 필요하다. 빈도 1개 짜리도 모두 고려하면 너무 많아지기 때문에 적은 것은 무시하는 식으로 하는 것이 그나마 계산 시간을 올리는 법이다. 


```python
# 필터링을 진행한 경우 
import networkx as nx
import pandas as pd
import matplotlib.pyplot as plt
import itertools
from collections import Counter
from inflection import singularize 
from textblob import TextBlob

"""
centrality를 계산하는 함수들입니다. 
사실 networkx에 있는 것과 큰 차이 없는데, 그래도 제가 편하려고 몇 개는 고치고, 
이름을 return 으로 시작하는 것으로 동일화해서 저장해두었습니다. 
"""
def return_weighted_degree_centrality(input_g, normalized=True):
    w_d_centrality = {n:0.0 for n in input_g.nodes()}
    for u, v, d in input_g.edges(data=True):
        w_d_centrality[u]+=d['weight']
        w_d_centrality[v]+=d['weight']
    if normalized==True:
        weighted_sum = sum(w_d_centrality.values())
        return {k:v/weighted_sum for k, v in w_d_centrality.items()}
    else:
        return w_d_centrality
def return_closeness_centrality(input_g):
    new_g_with_distance = input_g.copy()
    for u,v,d in new_g_with_distance.edges(data=True):
        if 'distance' not in d:
            d['distance'] = 1.0/d['weight']
    return nx.closeness_centrality(new_g_with_distance, distance='distance')
def return_betweenness_centrality(input_g):
    return nx.betweenness_centrality(input_g, weight='weight')
def return_pagerank(input_g):
    return nx.pagerank(input_g, weight='weight')

"""
일종의 main 함수입니다. 
raw_df를 넘기는데, 가능하면 해당 argument에서 복사해서 넘겨주는 게 좋을 것 같습니다. 혹시나 싶어서요. 
"""
def scopus_analysis(raw_df, outputExcelname):
    new_df = raw_df[['Author Keywords', 'Year', 'Abstract']].dropna()
    new_df['Author Keywords'] = new_df['Author Keywords'].apply(lambda s: s.split(";"))
    new_df['Author Keywords'] = new_df['Author Keywords'].apply(lambda ks: [singularize(k).strip().lower() for k in ks])
    new_df['Noun Phrases'] = new_df['Abstract'].apply(lambda s: TextBlob(s).noun_phrases)
    new_df['Noun Phrases'] = new_df['Noun Phrases'].apply(lambda ks: [singularize(k).lower().strip() for k in ks])
    # edge를 만들때 중복을 방지하기 위해서 sorting해둔다. 
    new_df['Author Keywords'] = new_df['Author Keywords'].apply(lambda l: sorted(list(set(l))))
    new_df['Noun Phrases'] = new_df['Noun Phrases'].apply(lambda l: sorted(list(set(l))))
    """
    여기 부분에서 토탈 키워드를 세었을 때, 최소한 2개 혹은 n개가 넘는 경우에 대해서만 해당 노드가 의미가 있다고 생각하고. 
    나머지 키워드는 무시하고 진행해야 노드의 수가 확연히 줄어들 수 있지 않을까? 
    """
    def total_count(input_df, column_name='Author Keywords'):
        # 'Author Keywords' or 'Noun Phrases'
        r = itertools.chain.from_iterable(input_df[column_name])
        r = Counter(r).most_common()
        return pd.DataFrame(r, columns=[column_name, 'count'])
    def filtering_auth_kwds(input_df,column_name='Author Keywords', above_n=3):
        """
        개별 node가 전체에서 1번 밖에 등장하지 않는 경우도 많은데, 이를 모두 고려해서 분석을 하면, 효율적이지 못한 계산이 된다. 
        따라서, 빈도가 일정 이상을 넘는 경우에 대해서만 고려하여 new_df를 수정하는 것이 필요하다. 
        """
        filtered_kwds = total_count(input_df)
        filtered_kwds = set(filtered_kwds[filtered_kwds['count']>=above_n][column_name])
        #return filtered_kwds
        input_df[column_name] = input_df[column_name].apply(lambda ks: list(filter(lambda k: True if k in filtered_kwds else False, ks)))
        return input_df
    def yearly_rank(input_df, column_name='Author Keywords', until_rank_n=50):
        r_dict = {}
        for year, year_df in input_df.groupby('Year'):
            r_dict[year] = list(total_count(year_df, column_name=column_name)[column_name])[:until_rank_n]
            if len(r_dict[year])<until_rank_n:
                for i in range(0, until_rank_n - len(r_dict[year])):
                    r_dict[year].append("")
        return pd.DataFrame(r_dict)
    #print(total_count('Noun Phrases'))
    """
    df로부터 그래프를 만ㄷ르어서 리턴해주는 함수입니다.
    """
    def make_graph(input_df, column_name='Author Keywords'):
        # make edges: edge가 중복으로 생기지 않게 하려면, 
        def make_edges_from_lst(lst):
            if len(lst)>1:
                return [(lst[i], lst[j]) for i in range(0, len(lst)-1) for j in range(i+1, len(lst))]
            else:
                return []
        edges = itertools.chain.from_iterable(input_df[column_name].apply(make_edges_from_lst))
        edges = ((uv[0], uv[1], w) for uv, w in Counter(edges).most_common())
        G = nx.Graph()
        G.add_weighted_edges_from(edges)
        # graph에 대한 데이터 필터링이 필요할 수 있는데. 여기서. 
        return G
    def total_centrality(input_df, centrality_func):
        inputG = make_graph(input_df)
        r = sorted(centrality_func(inputG).items(), key=lambda e: e[1], reverse=True)
        return pd.DataFrame(r, columns=['kwd', 'centrality'])
    def yearly_centrality_rank(input_df, cent_func, column_name = 'Author Keywords', until_rank_n=50):
        r_dict={}
        for year, year_df in input_df.groupby("Year"):
            r_dict[year] = list(total_centrality(year_df, cent_func)['kwd'][:until_rank_n])
            if len(r_dict[year])<until_rank_n:
                for i in range(0, until_rank_n - len(r_dict[year])):
                    r_dict[year].append("")
        return pd.DataFrame(r_dict)
    new_df = filtering_auth_kwds(new_df) # 빈도 n 개 이하의 키워드 삭제 
    writer = pd.ExcelWriter(outputExcelname)
    total_count(new_df, column_name='Author Keywords').to_excel(writer, '1. 전체 저자 키워드 빈도 상위 키워드')
    total_count(new_df, column_name='Noun Phrases').to_excel(writer, '2. 전체 noun phrase 빈도 상위')
    yearly_rank(new_df, column_name='Author Keywords').to_excel(writer, '3. 연도별 저자 키워드 순위 변화')
    yearly_rank(new_df, column_name='Noun Phrases').to_excel(writer, '4. 연도별 noun phrase 순위 변화')
    print("빈도 완료")
    total_centrality(new_df, return_weighted_degree_centrality).to_excel(writer, '5. 전체 저자 키워드 w. deg cent')
    total_centrality(new_df, return_closeness_centrality).to_excel(writer, '6. 전체 저자 키워드 closeness cent')
    total_centrality(new_df, return_betweenness_centrality).to_excel(writer, '7. 전체 저자 키워드 betweeness cent')
    print("전체 centrality 완료")
    yearly_centrality_rank(new_df, return_weighted_degree_centrality).to_excel(writer, '8. 저자 키워드 연도별 w. deg cent 순위 변화')
    yearly_centrality_rank(new_df, return_closeness_centrality).to_excel(writer, '9. 저자 키워드 연도별 close cent 순위 변화')
    yearly_centrality_rank(new_df, return_betweenness_centrality).to_excel(writer, '91. 저자 키워드 연도별 betw cent 순위 변화')
    yearly_centrality_rank(new_df, return_pagerank).to_excel(writer, '92. 저자 키워드 연도별 pagerank 순위 변화')
    writer.save()

# excel_path_and_filename = 
df = pd.read_excel(excel_path_and_filename)
df = df[['Author Keywords', 'Year', 'Abstract']]

a = scopus_analysis(df.copy(), 'simple_report_for_SME.xlsx')
print("complete")
```