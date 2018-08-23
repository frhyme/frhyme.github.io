---
title: nx의 graph를 pygraphviz로 변경해서 그리기 
category: python-lib
tags: python python-lib graphviz networkx graph 
---

## 간단합니다. 

- 보통 때는 상관이 없는데, tree 구조를 그릴 때는 graphviz의 레이아웃이 그림이 더 이쁘거든요. 
- 그래서 간단하게 변경하는 코드를 추가합니다. 

## 두잇 

- 간단합니다. 
- 밑에 주석처리한 코드는 그림을 원하는 곳에 저장하고 싶을 때 씁니다. 원래 그냥 `render`자체가 그림을 저장하는 방법이기는 해서, 아래 코드를 실행하면, 그림이 현재 폴더내에 자동으로 저장됩니다. 

```python
def render_nxG_to_graphviz(inputG):
    rG = graphviz.Graph()
    rG.graph_attr.update(size="12,2")## resize
    for e in inputG.edges():
        rG.node(e[0]), rG.node(e[1])
        rG.edge(e[0], e[1])
    rG.render()
    return rG
g_graphviz = render_nxG_to_graphviz(R_net)
"""
g_graphviz.format='svg'
g_graphviz.filename = "180822_g_graphviz"
g_graphviz.directory = '../../assets/images/markdown_img/'
g_graphviz.render(view=False)
"""
```

![](/assets/images/markdown_img/180822_g_graphviz.svg)

## wrap-up

- 제가 요즘 느끼는 건데, 에전에 만들어둔 코드들이 이후에 생각보다 쓸모가 없어요. 여러가지 이유가 있겠지만
    1) documentation을 내가 제대로 해두지 않아서
    2) 범용성이 너무 떨어져서
    3) 코드 관리를 제대로 안해서
- 생각해보니 다 맞네요.....흠...