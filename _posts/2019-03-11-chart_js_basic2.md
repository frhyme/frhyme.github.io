---
title: chart.js로 여러 그림을 그려봅시다. 
category: javascript
tags: javscript chart.js data-visualization visualization 
---

## chart.js로 그림을 그립니다. 

- 지난번에도 그림을 그렸듯이, 웹에 그림을 그리기 위해서는 다음 세가지가 필요합니다. 
    - html 페이지에서 CDN을 사용해서 chart.js를 가져옵니다. 
    - 두번째로 그려질 canvas를 그려줍니다. 
    - javascript를 사용해서 차트를 만들어줍니다. 
- 이 그림은 [여기에서](https://www.chartjs.org/docs/latest/charts/radar.html) 자세한 내용을 볼 수 있습니다. 

### line chart. 

```html
<script src="https://cdnjs.cloudflare.com/ajax/libs/Chart.js/2.4.0/Chart.min.js"></script>
```

- 그 다음으로는 필요한 데이터를 넘겨줍니다. 
- 데이터에는 우선, `type`, `data`, `options`라는 세 가지 key가 들어갑니다. 
    - `type`에는 만들려고 하는 차트의 종류가 들어가고
    - `data`에는 그림을 그려줄 데이터들이 들어갑니다. 
        - 그 안에는 다시 `labels`는 x축의 label들이 들어가고 
        - `datasets`에는 그려질 데이터들이 들어갑니다. 여러 개가 그려질 수도 있습니다. 리스트 오브 딕셔너리로 들어가죠. 
            - 우선, data의 `label`이 들어가고 
            - `backgroundColor`, `borderColor`등 차트의 색까들, 
            - 그리고 `data`가 들어갑니다. 즉, `labels`의 수와 같아야겠죠. 
    - 그다음으로 `options`에 여러 값들이 들어가면 됩니다. 

```html 
<script src="https://cdnjs.cloudflare.com/ajax/libs/Chart.js/2.4.0/Chart.min.js"></script>
<div>
    <canvas id="myChart">
    </canvas>
</div>
<script>
    var ctx = document.getElementById('myChart').getContext('2d');
    var data = {
        // The type of chart we want to create
        type: 'line',
        // The data for our dataset
        data: {
            labels: ["January", "February", "March", "April", "May", "June", "July"],
            datasets: [{
                label: "My First dataset",
                backgroundColor: 'rgb(255, 99, 132)',
                fill:false, // line의 아래쪽을 색칠할 것인가? 
                borderColor: 'rgb(255, 99, 132)',
                lineTension:0.1, // 값을 높이면, line의 장력이 커짐.
                data: [0, 10, 5, 2, 20, 30, 45],
            }]
        },
        // Configuration options go here
        options: {}
    }
    var chart = new Chart(ctx, data);
</script>
```

- 아래처럼 그려집니다. 

<script src="https://cdnjs.cloudflare.com/ajax/libs/Chart.js/2.4.0/Chart.min.js"></script>
<div>
    <canvas id="myChart">
    </canvas>
</div>
<script>
    var ctx = document.getElementById('myChart').getContext('2d');
    var data = {
        // The type of chart we want to create
        type: 'line',
        // The data for our dataset
        data: {
            labels: ["January", "February", "March", "April", "May", "June", "July"],
            datasets: [{
                label: "My First dataset",
                backgroundColor: 'rgb(255, 99, 132)',
                fill:false, // line의 아래쪽을 색칠할 것인가? 
                borderColor: 'rgb(255, 99, 132)',
                lineTension:0.1, // 값을 높이면, line의 장력이 커짐.
                data: [0, 10, 5, 2, 20, 30, 45],
            }]
        },
        // Configuration options go here
        options: {}
    }
    var chart = new Chart(ctx, data);
</script>

### drawing chart with flask 

- 원래는 모든 차트를 다 써보려고 했는데, 굳이 그럴 필요가 없을 것 같습니다. 
- [chart.js sample](https://www.chartjs.org/samples/latest/)에 들어가면 이미 충분히 많은 종류의 차트가 있습니다. 이걸 참고해서 필요할때 그려주는 것이 좋을 것 같아요. 
- 아무튼, 저는 flask를 이용해서 데이터를 전달해주고, 차트를 그려주는걸 해봅니다.

- 우선 python으로 다음처럼 마이크로서버를 만들고, 데이터를 넘겨줍니다. 

```python
app = Flask(__name__)

@app.route("/chart_js")
def chart_js():
    import numpy as np
    xs = np.random.random(1000)
    xys = [{'x':i, 'y':xs[i]} for i in range(0, 1000)]
    return render_template('chart_js.html', xys=xys)
```

```html
<h1>This is H1</h1>
<div style='width:800px;'>
    <canvas id="myChart" width="10" height="4"></canvas>
</div>

<script src="https://cdnjs.cloudflare.com/ajax/libs/Chart.js/2.4.0/Chart.min.js"></script>
<script>
    var ctx = document.getElementById('myChart').getContext('2d');
    var scatterChart = new Chart(ctx, {
        type: 'scatter',
        data: {
            datasets: [{
                label: 'Scatter Dataset',
                data: {{ xys| tojson }}, 
                //data: [{ x: -10, y: 0},{ x:  10, y: 0 },{ x: 10, y: 5 },],
                backgroundColor: 'rgb(255, 99, 132)',
                fill: false, // line의 아래쪽을 색칠할 것인가? 
                borderColor: 'rgb(255, 99, 132)',
            }]
        },
        options: {
            scales: {
                xAxes: [{
                    ticks: {
                        suggestedMin: 0,
                        suggestedMax: 100
                    }
                }], 
                yAxes: [{
                    ticks: {
                        suggestedMin: -0.2,
                        suggestedMax: 1.2
                    }
                }]
            }
        }
    });
</script>
```

## wrap-up

- flask를 이용해서 데이터를 만들어주고 프론트엔드에서 chart.js를 사용해서 그려줍니다. 하하하. 잘되네요 하하하. 