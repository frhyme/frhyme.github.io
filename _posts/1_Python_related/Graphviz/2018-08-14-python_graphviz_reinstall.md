---
title: graphviz 다시 설치하기 
category: python-lib
tags: python graphviz python-lib macOS 
---

## runtimerror 

- 예전에도 맥에서 graphviz를 잘 실행했는데 오늘은 뭐가 잘 안되더군요. 에러는 다음과 같았습니다. 

```
RuntimeError: failed to execute ['dot', '-Tpdf', '-O', 'test'], make sure the Graphviz executables are on your systems' path
```

- 잘 모를 때는 그냥 검색을 해보면 되는데, 검색해보면 [스택오버플로우에서 아주 잘 정리된 답변](https://stackoverflow.com/questions/35064304/runtimeerror-make-sure-the-graphviz-executables-are-on-your-systems-path-aft)이 있습니다. 

- 아래를 순서대로 실행하시면 됩니다. 

```bash
pip install graphviz
conda install graphviz 
```

- 일단 이렇게 하고 나니 잘 되네요. 
- 아래는 예제 코드입니다. 

```python
import graphviz 

def save_graph_as_svg(dot_string, output_file_name):
    if type(dot_string) is str:
        g = graphviz.Source(dot_string)
    elif isinstance(dot_string, (graphviz.dot.Digraph, graphviz.dot.Graph)):
        g = dot_string
    g.format='svg'
    g.filename = output_file_name
    g.directory = '../../assets/images/markdown_img/'
    g.render(view=False)
    return g
dot_graph = """
graph graphname {
    rankdir=LR;
     a -- b -- c;
     b -- d;
}"""
save_graph_as_svg(dot_graph, 'simple_dot_example1')
```