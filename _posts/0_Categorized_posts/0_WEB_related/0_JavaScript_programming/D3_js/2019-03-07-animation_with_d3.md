---
title: flask에서 만든 데이터로 d3js 애니메이션 만들기. 
category: others
tags: python flask d3js animation 
---

## 애니메이션을 만듭시다. 

- python 에서 애니메이션, 즉 각 프레임별로 필요한 데이터를 전송하고, 각 프레임을 만드는 작업을 해보려고 합니다. 
- html 페이지를 만들어줍니다. 
    - 처음에는 어떻게 하나 싶었는데 그냥 `i`를 하나씩 올려주면서 진해하면 되더군요...

```html
<html>
    <head>
        <script src="https://d3js.org/d3.v5.js"></script>
    </head>
    <body>
        <svg id='chart1'>
        </svg>
        <script>
            var chart1 = d3.select('#chart1').attr('width', 750).attr('height', 750);
            var chart1_data_lst = {% raw %}{{ circle_data_lst| tojson}}{% endraw %};
            var i=0;
            // d3.interval를 이용해서 animation을 만들어주고, 
            var animation = d3.interval(
                function(elapsed){
                    // 종료조건을 설정해주고.
                    if(i==chart1_data_lst.length){
                        this.stop();
                    }else{
                        frame_data_lst = chart1_data_lst[i];
                        //console.log(frame_data_lst);
                        chart1.selectAll('circle').data(frame_data_lst)
                            .attr('cx', function (d) { return d['cx'] })
                            .attr('cy', function (d) { return d['cy'] })
                            .attr('r', function (d) { return d['r'] })
                            .attr('fill', function (d) { return d['fill'] })
                            .attr('stroke', function (d) { return d['stroke'] })
                            .attr('stroke-width', function (d) { return d['stroke-width'] })
                            .attr('fill-opacity', function (d) { return d['fill-opacity'] })
                            .enter().append("circle")
                            .attr('cx', function (d) { return d['cx'] })
                            .attr('cy', function (d) { return d['cy'] })
                            .attr('r', function (d) { return d['r'] })
                            .attr('fill', function (d) { return d['fill'] })
                            .attr('stroke', function (d) { return d['stroke'] })
                            .attr('stroke-width', function (d) { return d['stroke-width'] })
                            .attr('fill-opacity', function (d) { return d['fill-opacity'] })
                        // 아래처럼 i를 올리면서 진행해줍니다. 
                        i = i + 1;
                    }
                }, 100)
        </script>
    </body>
</html>

```

```python
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/random_animation')
def random_animation():
    import numpy as np

    circle_data_lst = []
    ## 30개의 프레임을 만듭니다. 
    for frame in range(0, 30):
        each_frame = []
        ## 각 프레임별로 들어가는 데이터, 즉 원은 총 200개이며, 200개에 필요한 데이터를 모두 넘겨줍니다.
        for i in range(0, 200):
            each_frame.append(
                {
                    "cx": np.random.random()*750,
                    "cy": np.random.random()*750,
                    "r": (np.random.random()+1)*20,
                    "stroke": "black",
                    "stroke-width": 3,
                    "fill": f"rgb({np.random.randint(0, 256)}, {np.random.randint(0, 256)}, {np.random.randint(0, 256)})",
                    "fill-opacity": 0.3,
                }
            )
        circle_data_lst.append(each_frame)
    ## 최종적으로 프레임 리스트, 그리고 프레임에는 프레임에 필요한 다양한 데이터들이 들어가 있는 딕셔너리를 html에 넘겨줍니다.
    return render_template('d3_animation.html', circle_data_lst=circle_data_lst)
```

## wrap-up

- 사실 좀 더 파볼 필요는 있습니다. 저는 한 페이지 내에 같은 타임축을 공유하는 여러 요소를 만들어야 하는데 흠...생각해보니 그냥 하면 될것 같군요. 
- 여담이지만, 이런식으로 랜덤하게 그림을 만드는데 생각보다 되게 예뻐요. 마음에 듭니다. 프레임을 한 20000개를 만들어봤는데 그래도 생각보다는 시간이 많이 걸리지 않습니다. 
- 그리고, 트랜지션을 좀더 정리해보면 좋을 것 같습니다 하하.

## reference

- <https://bl.ocks.org/pvernier/b00af256b014e2824bf48b481754ff78>