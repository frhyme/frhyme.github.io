---
title: graphviz를 이용해서 그림을 그리고, flask로 웹으로 보냅시다. 
category: python-libs
tags: graphviz python flask python-libs svg
---

## graphviz로 그림 그리기. 

- 저는 보통 그냥 `networkx`로 그림을 그리지만, 경우에 따라서는 `graphviz`로 그림을 그릴때도 있습니다. 
- 여기서는, `graphviz`로 그림을 그리고, 이를 버퍼에 저장해서 바로 웹으로 보내주는 것을 정리하였습니다. 

## code 

- 다음처럼 간단하게 파이썬 코드를 만들구요. 

```python
from flask import Flask, render_template
from flask import Markup

from graphviz import Graph# Graph를 만들어줍니다.

app = Flask(__name__)

@app.route("/test")
def test():
    from graphviz import Digraph, Graph
    g = Digraph('hello', format='svg')
    g.edge('Hello', 'World')
    g_svg = g.pipe().decode("utf-8")
    g_svg = Markup(g_svg)
    return render_template("test.html", g_svg=g_svg
    )

if __name__ == '__main__':
    # debug를 True로 세팅하면, 해당 서버 세팅 후에 코드가 바뀌어도 문제없이 실행됨. 
    app.run(host='127.0.0.1', port=8001, debug = True)
```

- 다음처럼 Html 파일읆 만들면 끝납니다. 

```html
{% raw %}
<html>
    <head>
    </head>
    <body>
        {{g_svg}}
    </body>
</html>
{% endraw %}
```

## wrap-up

- 찾아보니, [graphviz를 웹에서 그릴 수 있도록 한 viz.js라는 자바스크립트 라이브러리](https://github.com/mdaines/viz.js)도 있습니다. CDN을 통해서 바로 사용할 수는 없고, 문법도 좀 다른 것 같기는 한데요. 아무튼 일단 나중에 시간이 나면 좀 더 정리해보도록 하겠습니다.
- [d3를 이용해서 만든 것도 있네요](https://github.com/magjac/d3-graphviz).
- 다양한 라이브러리들이 있지만, 대부분 node.js와 함께 사용했을 때 효과가 있을 뿐, 저처럼 python을 기반으로 사용했을 때는 그 효과가 덜한것 같습니다.