---
title: graphviz로 만든 그림을 jupyter notebook에 embed하기 
category: python-lib
tags: python python-lib networkx graphviz jupyter-notebook ipython display
---

## jupyter notebook에 그림을 넣고 싶어요. 

- graphviz로 그림을 만드는 함수를 다음처럼 정의했습니다. 
- 그런데, 저는 경우에 따라서 한 셀 내에서 여러 그림을 동시에 보여주려고 하고 있거든요. 따라서 다른 방법을 모색했습니다. 

```python
def render_nxG_to_graphviz(inputG):
    rG = graphviz.Graph()
    rG.graph_attr.update(size="12,2")## resize
    for e in inputG.edges():
        rG.node(e[0]), rG.node(e[1])
        rG.edge(e[0], e[1])
    """
    g_graphviz.format='svg'
    g_graphviz.filename = "180822_g_graphviz"
    g_graphviz.directory = '../../assets/images/markdown_img/'
    """
    rG.format = "svg"## 기본 file format은 pdf인데, 얘는 잘 못 읽더라구요. 
    rG.render(view=False)## rG.filename+'.'+rG.format 에 파일을 저장합니다. 
    ## 여기서 view를 True로 바꾼다고 해서 
    return rG
render_nxG_to_graphviz(R_net)
#print() jupytertnotebook의 셀의 마지막 부분에서 위 함수가 수행되어야 그림이 출력됩니다. 
```

## using iPython 

- 아래처럼 해줍니다. 간단하죠? 

```python
from IPython.display import display, IFrame

for i in range(0, 2):
    a = render_nxG_to_graphviz(R_net)
    display(IFrame(a.filename+"."+a.format, width=600, height=200))
    print()
```