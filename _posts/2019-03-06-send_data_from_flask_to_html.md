---
title: flask에서 데이터를 html, javascript로 보내자. 
category: others
tags: d3js javascript csv python flask
---

## flask에서 데이터를 javascript로 보내자. 

- 저의 주력언어는 파이썬입니다. 파이썬으로 대부분의 데이터 처리를 하게 되는데, 데이터를 시각화하는 측면에서는 javascript, 특히 d3.js가 매우 편한 것 같아요. 
- 그 측면에서, 제가 지금 만들고 있는 시스템은 flask로 구축되어 있고, flask와 파이썬에서 데이터를 수정하고, 필요한 데이터를 html페이지, 특히, javascript에서 유용하게 쓸 수있도록 전송을 해주면, 데이터를 전달받아서 바로 javascript에서 쓸 수 있지 않을까? 하는 생각이 들었습니다. 
- 이를 위해 우선 간단한 flask 서버를 만들었습니다. 

```python
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/read_csv_and_vis')
def read_csv_and_vis():
    """
    - html 페이지에서는 자바스크립트를 이용해서 원을 그려주는데, 여기서는 원을 그리는데 필요한 데이터들을 만들어서 전송한다. 
    """
    import numpy as np 
    """
    - 리스트와 딕셔너리, 스트링과 숫자 로 구성된 데이터는 쉽게 json으로 변환될 수 있다. 
    """
    circle_data_lst = []
    for i in range(0, 100):
        circle_data_lst.append(
            {
                "cx":np.random.random()*750, 
                "cy": np.random.random()*750,
                "r": (np.random.random()+1)*20,
                "stroke": "black",
                "stroke-width":3, 
                "fill": f"rgb({np.random.randint(0, 256)}, {np.random.randint(0, 256)}, {np.random.randint(0, 256)})",
                "fill-opacity":0.5,    
            }
        )
    ## 아래처럼 render_template를 이용해서 해당 Html에 필요한 데이터를 전달해준다. 
    return render_template('d3_1.html', circle_data_lst=circle_data_lst)
```

- html 페이지는 다음과 같습니다. 
    - 중간에 대괄호가 들어가고, tojson이라는 부분도 있는 것을 알 수 있습니다. 
    - flask의 경우 jinja template engine를 이용해서 html 페이지를 변환해주는데, 여기서 이렇게만 간단하게 세팅해줘도 알아서 잘 변환해줍니다. 편하군요 하하핫.
- 물론 아쉽게도 이렇게 했을 경우에 대괄호 부분에 빨간줄이 가있기는 합니다만. 그냥 그러려니 합시다 하하핫

```html 
<html>
    <head>
        <script src="https://d3js.org/d3.v5.js"></script>
    </head>
    <body>
        <svg id='chart1'>
        </svg>
        <script>
            var chart1_data_lst = {% raw %}{{circle_data_lst|tojson}} {% endraw %};
            var chart1 = d3.select('#chart1').attr('width', 750).attr('height', 750);

            chart1.selectAll('circle').data(chart1_data_lst)
            .enter().append("circle")
            .attr('cx', function (d) { return d['cx'] })
            .attr('cy', function (d) { return d['cy'] })
            .attr('r', function (d) { return d['r'] })
            .attr('fill', function (d) { return d['fill'] })
            .attr('stroke', function (d) { return d['stroke']})
            .attr('stroke-width', function (d) { return d['stroke-width'] })
            .attr('fill-opacity', function (d) { return d['fill-opacity']})
        </script>
    </body>
</html>

```


## wrap-up

- 처음에는 csv 파일로 만들어서 다시 읽고 해야 하나 싶었는데, 생각보다 쉽게 되는 것 같습니다 하하핫.