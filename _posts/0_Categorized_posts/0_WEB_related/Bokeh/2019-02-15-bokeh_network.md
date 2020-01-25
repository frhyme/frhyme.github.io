---
title: bokeh로 네트워크 그리기. 
category: python-libs
tags: python bokeh python-libs networkx data-visualization 
---

## bokeh로 network 그리기. 

- 저는 네트워크 분석을 주로 수행합니다. 따라서 네트워크를 시각화할 필요성이 많은데, `matplotlib`를 이용해서 그림을 그릴 때는 비교적 쉽게 그림을 그릴 수 있습니다. 이를 활용해서 png, svg의 형태로 그림을 뽑아내는 것 까지는 큰 무리없이 가능합니다. 
- 다만, 웹페이지를 만들때 이렇게 `matplotlib`를 이용해서 그림을 그리게 되면 정적인 이미지파일이 생겨나게 되고요 웹페이지에서 특정 이미지를 직접 source로 받아와서 그리는 것은 좀 문제가 있습니다. 
    - 우선, 브라우저레벨에서 캐쉬를 저장하기 때문에 이미지가 변경되어도 이전에 가져온 이미지(변경되기 전 이미지)를 그대로 가져올 수 있고
    - 웹에서의 동작에 따라서 이미지가 효과적으로 작동하지 않아요. 예를 들면 hover 시에 특정 텍스트가 뜨도록 처리하고 싶은데 이러한 부분이 잘 작동되지 않는 것이죠. 
- 결론적으로는 bokeh를 이용해서 네트워크를 새로 그리기로 했고, 마침 찾아보니, [Visualizing Network Graph](https://bokeh.pydata.org/en/latest/docs/user_guide/graph.html)에 자세한 내용이 나와 있습니다. 

## do it.

- 이미 있는 코드를 조금 변경해서 다음처럼 만들어 봤습니다. 
- 아래 코드와 같이 작성하고, `/bokeh_network`로 들어가면 네트워크가 그려지는 것을 알 수 있습니다. 

```python
@app.route('/bokeh_network')
def bokeh_network():
    import networkx as nx
    
    # from_networkx는 networkx에서 그래프를 가져와서 바로 그려주기 위해서 사용됨. 
    from bokeh.models.graphs import from_networkx
    # Spectral4는 색깔을 지정해주기 위해서 사용됩니다. matplotlib의 cmap과 유사하다고 생각하면 될것 같네요.
    from bokeh.palettes import Spectral4
    from bokeh.models import Plot, Range1d, MultiLine, Circle, HoverTool, BoxZoomTool, ResetTool
    # 아래 코드는 바로 html 파일로 변경하여 보내주기 위해서 만듬
    from bokeh.embed import file_html
    from bokeh.resources import CDN

    ### nx code
    """
    - Graph를 만들기는 귀찮아서, 기존에 있는 것을 그대로 가져옵니다. 
    - (0, {'club': 'somt string'})으로 각 노드가 정의되어 있습니다. 
    """
    G = nx.karate_club_graph()
    
    """
    - edge_color를 networkx의 edge attribute로 넘겨줍니다. 
    - 이를 이용해서, 이후 네트워크를 렌더링할 때 edge의 색깔을 결정할 수 있습니다.
    """
    SAME_CLUB_COLOR, DIFFERENT_CLUB_COLOR = "black", "red"
    for n1, n2 in G.copy().edges():
        if G.nodes[n1]['club']==G.nodes[n2]['club']:
            G.edges[(n1, n2)]['edge_color'] = SAME_CLUB_COLOR
        else:
            G.edges[(n1, n2)]['edge_color'] = DIFFERENT_CLUB_COLOR

    #############

    ### bokeh code 
    plot = Plot(plot_width=400, plot_height=400,
                x_range=Range1d(-1.1, 1.1), y_range=Range1d(-1.1, 1.1))
    plot.title.text = "Graph Interaction Demonstration"

    node_hover_tool = HoverTool(tooltips=[("index", "@index"), ("club", "@club")])
    plot.add_tools(node_hover_tool, BoxZoomTool(), ResetTool())

    graph_renderer = from_networkx(G, nx.spring_layout, scale=1, center=(0, 0))

    graph_renderer.node_renderer.glyph = Circle(size=15, fill_color=Spectral4[0])
    graph_renderer.edge_renderer.glyph = MultiLine(line_color="edge_color", line_alpha=0.8, line_width=1)
    plot.renderers.append(graph_renderer)
    return file_html(plot, CDN)
```


## wrap-up

- 그림의 너비, 높이 등을 조절하고, 원하는 노드만 색깔을 다르게 하거나 하는 등의 파인튜닝만 진행을 하면, 될것 같기는 합니다만. 이번주는 바쁘므로 다음에 더 자세하게 정리해서 업로드하도록 하겠습니다.