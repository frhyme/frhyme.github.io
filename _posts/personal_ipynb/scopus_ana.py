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
    def total_count(input_df, column_name='Author Keywords'):
        # 'Author Keywords' or 'Noun Phrases'
        r = itertools.chain.from_iterable(input_df[column_name])
        r = Counter(r).most_common()
        return pd.DataFrame(r, columns=[column_name, 'count'])
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

excel_path_and_filename = "../../../Downloads/SMEs_Scopus_2013-2017.xlsx"
df = pd.read_excel(excel_path_and_filename)
df = df[['Author Keywords', 'Year', 'Abstract']]

a = scopus_analysis(df.copy(), 'simple_report_for_SME.xlsx')
print("complete")