---
title: cairosvg 문제 해결하기 
category: python-lib
tags: python python-lib svg png cairosvg graphviz 
---

## svg를 png로 바꾸고 있습니다. 

- graphviz를 사용할 때, svg, png, pdf 로 모두 저장할 수 있지만, png로 저장할 때 dpi가 매우 낮게 설정되는 일들이 발생합니다. 
- 어떤 글에서는 `BP.graph_attr['rankdir'] = 'LR'`를 사용해서 dpi를 graph의 attribute로 넘기면 된다고도 하던데 저는 안되더군요. 
- 그래서 cairosvg라는 라이브러리를 이용해서 svg를 png로 바꿔 주기로 했습니다. 다음으로 실행하면 되는데. 

```python
import cairosvg
cairosvg.svg2png(url = , write_to = , dpi = )
```

- 에러가 뜹니다. 흠. 

```
OSError: dlopen() failed to load a library:
```

- 잘 몰라서 검색해보니 다시 깔라고 해서 다시 깔았는데 

```
pip install cairosvg
conda install cairosvg
```

- 그래도 안됩니다. 

- 그러다가 보니 [여기](https://github.com/mirumee/saleor/issues/1510)서는 아래를 해보라고 하더군요

```bash
brew install python3 cairo pango gdk-pixbuf libffi
```

- 아무거나 막 치는거 매우 위험한데, 그냥 했습니다. 시간이 좀 걸리는데. 
- 아무튼 그 다음부터는 잘 됩니다. 하핫. 

- 아래는 소스코드입니다. 

```python
def activity_lst_to_png(activity_lst, output_file_name):
    def save_graph_as_svg(dot_string, output_file_name):
        if type(dot_string) is str:## dot language string으로 들어올 때, 
            g = graphviz.Source(dot_string)
        elif isinstance(dot_string, (graphviz.dot.Digraph, graphviz.dot.Graph)):## 객체로 들어올 때 
            g = dot_string
        else:
            print("can't handle it"), 
            return None
        ### outputfile 
        g.filename, g.format = output_file_name.split('.')[0], 'svg'
        g.directory = '../../assets/images/markdown_img/'
        g.render(view=False)
        ## svg to png, requried import cairosvg
        if output_file_name.split('.')[1]=='png':
            cairosvg.svg2png(url=g.directory+g.filename+"."+'svg',
                             write_to=g.directory+output_file_name, dpi = 100)
        return g
    activity_lst = ["Source"]+activity_lst+['Sink']
    BP = graphviz.Digraph(comment='business process')
    BP.graph_attr['rankdir'] = 'LR'
    ## add node 
    for i, act in enumerate(activity_lst):
        if act in ['Source', 'Sink']: ## 처음이거나 끝일 때는 노드를 다르게 표시 
            BP.node(act, shape="doublecircle", color='red') if act=='Source' else BP.node(act, shape="doublecircle", color='blue')
        else:
            BP.node(act, shape='rectangle')
    ## add edge 
    for i in range(0, len(activity_lst)-1):
        BP.edge(activity_lst[i], activity_lst[i+1])
    save_graph_as_svg(BP, output_file_name)
    print("complete")
```