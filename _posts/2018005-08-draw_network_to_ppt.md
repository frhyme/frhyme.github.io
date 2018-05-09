---
title: graphviz를 이용하여 키워드 네트워크를 그려 봅시다(실패함)
category: project
tags: python-lib matplotlib networkx python graphviz not-yet
---

## 백업용으로 일단 업로드 해두었습니다. 

- 아래 내용은 graphviz를 이용해 그림을 그려보았으나, 생각보다 예쁘게 나오지 않았씁니다. 
- 원인은 다음들이라고 생각됩니다. 
    - dot language를 잘 모르고 주먹구구식으로 함
    - 체계적으로 코딩한 것이 아니고, 주먹구구식으로 코딩하여, 현재 총체저인 난구.
    - graphviz에서 ppt로 넘기는 것이 쉽지 않음 
- 등등이 있습니다. 

- 따라서 현재는 `matplotlib`를 이용하여 그림을 예쁘게 그리는 법을 다시 공부한 다음, `matplotlib`로 그림을 그릴 계획입니다. 일단 `graphviz`바로 바로 그리는 것은 잠깐 쉴 예정입니다. 

---

## 네트워크를 예쁘게 그려 봅시다. 

- [지난 번](https://frhyme.github.io/project/rnd-knowledge-map/)에 한 것은 결국 중요한 키워드들을 테이블로 표현한 것 뿐입니다. 그런데 그냥 테이블만 보고 말 것이라면 이렇게 네트워크 분석을 할 필요가 없습니다. 그림을 예쁘게 그려야죠. 
- 아무튼 그래서, 이번에는 그림을 그리려고 합니다. 그린 그림은 피피티로 바로 들어갈 거에요. 

## requirement 

- 엑셀로부터 읽어서, 네트워크를 구성하는 부분까지는 동일하게 진행합니다. 
- 개별 슬라이드에는 각각 다음 그림들이 들어갑니다. 
    - 전체 네트워크 그림(키워드 수를 제한해야 하는데 대략 50개 내외로 하면 좋을 것 같음)
    - 빈도 상위 10개 키워드에 대한 ego-network
- matplotlib로 그리는 것이 좋은지, graphviz로 그리는 것이 좋은지에 대해서는 좀 고민이 필요할 것 같아요. 우선 matplotlib로 그리고 그다음에 생각해볼게요. 

## just do it with graphviz, but not enough. 

- 어쨌거나, 코딩을 하기는 해서 아래에 올리기는 했지만 몇 가지 문제점들이 있었습니다. 
- `graphviz`를 이용하기로 한 것은 matplotlib에 비해서 그림이 더 선명하고 이쁘다고 생각했기 때문인데, 마음처럼 예쁘지는 않은 것 같아요. 제가 작은 데이터들을 가지고 테스트를 좀 더 해본다음에 다시 해보는 게 필요할 것 같습니다. 
- 어쨋거나, 아래 코드로도 그림이 그려지기는 하는데, 어려운게 빈도에 따라서 선의 굵기나, 그림 굵기를 어떤 값 분포로 두어야 지나치게 크거나, 지나치게 작은지 아닌지가 어려워요. 
- 아무튼, 요 글은 제가 다음에 다시 쓰는 게 좋을 것 같습니다. 

```python
# 필터링을 진행한 경우 
import networkx as nx
import pandas as pd
import matplotlib.pyplot as plt
import itertools
from collections import Counter
from inflection import singularize 
from textblob import TextBlob
from pptx import Presentation
from pptx.util import Inches

import graphviz
"""
일종의 main 함수입니다. 
raw_df를 넘기는데, 가능하면 해당 argument에서 복사해서 넘겨주는 게 좋을 것 같습니다. 혹시나 싶어서요. 
"""
def draw_and_export_ppt(raw_df, outputPPTname):
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
    def make_graph(input_df, column_name='Author Keywords'):
        # make edges: edge가 중복으로 생기지 않게 하려면, 
        def make_edges_from_lst(lst):
            if len(lst)>1:
                return [(lst[i], lst[j]) for i in range(0, len(lst)-1) for j in range(i+1, len(lst))]
            else:
                return []
        nodes = total_count(input_df)
        new_nodes = []
        for i in range(0, len(nodes)):
            name = nodes[column_name].iloc()[i]
            w = nodes['count'].iloc()[i]
            new_nodes.append( (name, {'weight':w}) )
        nodes = new_nodes
        edges = itertools.chain.from_iterable(input_df[column_name].apply(make_edges_from_lst))
        edges = ((uv[0], uv[1], w) for uv, w in Counter(edges).most_common())
        G = nx.Graph()
        G.add_nodes_from(nodes)
        G.add_weighted_edges_from(edges)
        # graph에 대한 데이터 필터링이 필요할 수 있는데. 여기서. 
        return G
    
    def make_ego_graph_from_inputG(inputG, target_n):
        newG = nx.Graph()
        edges = filter(lambda s: True if s[0]==target_n or s[1]==target_n else False, (e for e in inputG.edges(data=True)))
        edges = list(edges)
        nodes = itertools.chain.from_iterable([[e[0], e[1]] for e in edges])
        
    def nxG_to_dotG(nx_G):
        dot_G = graphviz.Graph(comment="this is what?")
        dot_G.attr(rankdir='LR')
        max_n_weight = max((n[1]['weight'] for n in nx_G.nodes(data=True)))
        min_n_weight = min((n[1]['weight'] for n in nx_G.nodes(data=True)))
        for node in nx_G.nodes(data=True):
            weight = (node[1]['weight'] - min_n_weight)/max_n_weight * 3 + 2
            dot_G.node(node[0], shape='circle', color='blue', height='{}'.format(weight), width='{}'.format(weight), 
                       fixedsize='true', fontcolor='blue', fontsize='{}'.format(20*weight))
        # edge normalization: 10이면 많이 굵은 편이고 1이면 얇은 편. 1-10 으로 표준화하자.
        max_e_weight = max((e[2]['weight'] for e in nx_G.edges(data=True)))
        min_e_weight = min((e[2]['weight'] for e in nx_G.edges(data=True)))
        for edge in nx_G.edges(data=True):
            weight = (edge[2]['weight'] - min_e_weight)/(max_e_weight - min_e_weight) * 20 + 5
            dot_G.edge(edge[0], edge[1], style='setlinewidth({})'.format(weight))
        return dot_G
        
    def save_graph(dot_string, output_file_name, file_format='svg'):
        if type(dot_string) is str:
            g = graphviz.Source(dot_string)
        elif isinstance(dot_string, (graphviz.dot.Digraph, graphviz.dot.Graph)):
            g = dot_string
        g.format=file_format
        g.filename = output_file_name
        g.directory = '../../assets/images/markdown_img/'
        g.render(view=False)
        return g
    """
    여기서는 우선 author keywords에 대해서만 진행함. 
    """
    new_df = raw_df[['Author Keywords', 'Year', 'Abstract']].dropna()
    new_df['Author Keywords'] = new_df['Author Keywords'].apply(lambda s: s.split(";"))
    new_df['Author Keywords'] = new_df['Author Keywords'].apply(lambda ks: [singularize(k).strip().lower() for k in ks])
    new_df['Author Keywords'] = new_df['Author Keywords'].apply(lambda l: sorted(list(set(l))))
    
    """
    전체 키워드의 경우는 상위 20개의 키워드에 대해서만 그린다. 따라서 50개에 대해서 필터링 해줌. 
    """
    new_df = filtering_auth_kwds(new_df, above_n = total_count(new_df)['count'][20])
    """
    전체 그래프 그리기 
    """
    content_lst = []
    G = make_graph(new_df)
    title_name = 'entire_network_180508'
    save_graph(nxG_to_dotG(G), title_name, 'png')
    content_lst.append((title_name, "", title_name+".png"))
    """
    ego-network 그리기. 
    """
    for k in list(total_count(new_df)['Author Keywords'])[:20]:
        egoG = nx.ego_graph(G, k)
        pic_title_name= 'ego_network_{}_180508'.format(k)
        save_graph(nxG_to_dotG(egoG), pic_title_name, 'png')
        content_lst.append((pic_title_name, "", pic_title_name+".png"))
    
    this_prs = Presentation()
    slide_layout = this_prs.slide_layouts[1] 
    for title, content, img_file_name in content_lst:
        this_slide = this_prs.slides.add_slide(slide_layout)
        shapes = this_slide.shapes
        shapes.title.text = title
        shapes.placeholders[1].text = content
        # placeholders는 개별 slide에 있는 모든 개체를 가져온다고 보면 됨. 
        #shapes.add_picture(img_stream, left, top, height=height)
        #shapes.add_picture(img_file_name, left=Inches(5), top=Inches(10))
        img_path = '../../assets/images/markdown_img/'
        shapes.add_picture(img_path+img_file_name, Inches(2.5), Inches(3.2))
        # 변환하지 않고 숫자로 넘기면 잘 되지 않는다. 
    this_prs.save(outputPPTname)
    #ego = nx.ego_graph(G, 'sme')
    #print(ego.nodes(data=True))
    #return G

excel_path_and_filename = "../../../Downloads/SMEs_Scopus_2013-2017.xlsx"
df = pd.read_excel(excel_path_and_filename)
df = df[['Author Keywords', 'Year', 'Abstract']]

draw_and_export_ppt(df.copy(), "sme_network.pptx")
print("complete")
```