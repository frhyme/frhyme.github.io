---
title: chart.js로 차트를 그려 봅시다. 
category: javascript
tags: chart javascript data-visualization 
---

## chart.js를 사용합니다. 

- 최근에는 d3.js를 사용하다가 갑자기 chart.js로 넘어왔습니다. 
- 늘 그랬듯이, 대단한 이유는 없고요. 데이터를 활용해서 일반적인 차트를 그려야 하는데, chart.js를 사용하는 것이 손쉽게 할 수 있는 방법인 것 같습니다. 그래서 결정했어요. 
- 이 글은 언제나 그랬듯이, chart.js를 사용해서 그림을 어떻게 그릴 수 있는지 정리되어 있습니다. 

## what is chart.js 

- [chart.js](https://www.chartjs.org/)에 들어가면 다음처럼 설명되어 있습니다. 

> Simple yet flexible JavaScript charting for designers & developers

- 간단하면서도, 유연한 자바스크립트 차트 그리는 라이브러리. 정도로 번역할 수 있겠네요. 
- chart.js를 이용해서 그림을 그릴때, 우선 알아두면 좋은 것은 html5에서 새로 나온 canvas라는 태그입니다. 

## what is canvas. 

- chart.js로 그림을 그릴때, 그려지는 요소는 모두 `canvas`라는 요소 안에 들어가 있게 됩니다. 흔히 쓰던 `div`같은 태그 내에서는 그림을 그릴 수 없어요. 
- 따라서, 우선은 canvas가 무엇인지, 어떠한 이유로 나왔는지를 알면 좋습니다. 물-론, 몰라도 그림을 그리는데는 아무 상관이 없습니다. 

- [영문 위키피다에서 canvas의 개념을 보면](https://en.wikipedia.org/wiki/Canvas_element) 다음처럼 표현되어 있습니다. 

> The canvas element is part of HTML5 and allows for dynamic, scriptable rendering of 2D shapes and bitmap images. It is a low level, procedural model that updates a bitmap and does not have a built-in scene graph; however through WebGL allows 3D shapes and images and so-on.

- canvas 요소는 html5부터 동적이고, 프로그래밍을 통해 구현되는(scriptable을 대충 번역했습니다), 2D shape, bitmap image를 말합니다. 물론, WebGL 등을 사용하면 3D 그림도 그릴 수 있다고 하네요. 
- 흠, 일단 읽어 보니, 대충 과거에 MFC를 사용해서 그림을 슥삭슥삭 그리는 것처럼, 여기서도 html5에 요소를 박아두고, javascript를 사용해서 그림을 그릴 수 있다는 말처럼 보입니다. 뭐 대략 그런거겠죠? 

## simple drawing in canvas

- 자, 그렇다면 한번 간단한 것을 그려보도록 합니다. [영문 위키피다 canvas](https://en.wikipedia.org/wiki/Canvas_element)에서 가져온 샘플 코드입니다. 

- 아래 html 코드를 보면, 안에 무의미한 텍스트가 있는 것을 알 수 있습니다. 해당 브라우저에서 html5를 지원하지 않을때, 이 텍스트가 보인다는 것이죠. 또한, id가 지정되어 있습니다. 
- javascript 코드에서는 해당 id를 가진 태그를 찾고, 
- `getContext` 속성을 통해서 2d로 세팅해주고 
- 색깔을 칠하는 등의 일들을 합니다. 뭐 대충 그런거에요. 

```html
<canvas id="example" width="200" height="200">
    This text is displayed if your browser does not support HTML5 Canvas.
</canvas>
<script>
    var example = document.getElementById('example');
    var context = example.getContext('2d');
    context.fillStyle = 'red';
    context.fillRect(30, 30, 50, 50);
</script>
```

- 즉, canvas란, 그림판에서 그림을 마우스로 슥삭슥삭 그리는 것처럼, javascript를 이용해서 그림을 그려줄 수 있는 요소를 말합니다. 

## do chart.js 

- 이제 canvas의 개념은 됐고, chart.js를 사용해서 그림을 그려보겠습니다. [모든 내용은 여기에서 가져왔습니다](https://www.chartjs.org/docs/latest/getting-started/)
- 우선, 대부분의 javascript library들이 그렇듯이, CDN을 통해서 라이브러리를 가져옵니다. 

```html
<script src="https://cdnjs.cloudflare.com/ajax/libs/Chart.js/2.4.0/Chart.min.js"></script>
```

- html 문서는 다음처럼 표현하죠. 
    - 여기서 canvas 태그가 div 안에 있는 것을 알 수 있습니다. 
    - chart.js로 그려지는 그림은 해당 요소를 포함한 부모 요소에 꽉 차게 그려집니다. 
    - 맨 끝에 `maintainAspectRatio`의 값이 `true`로 되어 있는데, 이는 해당 요소의 비율을 유지한채 그림이 그려지도록 한다는 이야기죠.
    - 따라서 지금은, 부모 요소에서 너비를 결정했고, 그 밑에 canvas가 비율을 유지한채로 그려지기 때문에, 800px에 맞추서 그려진다고 생각하면 되겠네요. 

```html
<div style="width:800px">
    <canvas id="myChart"></canvas>
</div>

<script>
// 우선 컨텍스트를 가져옵니다. 
var ctx = document.getElementById("myChart").getContext('2d');
/*
- Chart를 생성하면서, 
- ctx를 첫번째 argument로 넘겨주고, 
- 두번째 argument로 그림을 그릴때 필요한 요소들을 모두 넘겨줍니다. 
*/
var myChart = new Chart(ctx, {
    type: 'bar',
    data: {
        labels: ["Red", "Blue", "Yellow", "Green", "Purple", "Orange"],
        datasets: [{
            label: '# of Votes',
            data: [12, 19, 3, 5, 2, 3],
            backgroundColor: [
                'rgba(255, 99, 132, 0.2)',
                'rgba(54, 162, 235, 0.2)',
                'rgba(255, 206, 86, 0.2)',
                'rgba(75, 192, 192, 0.2)',
                'rgba(153, 102, 255, 0.2)',
                'rgba(255, 159, 64, 0.2)'
            ],
            borderColor: [
                'rgba(255,99,132,1)',
                'rgba(54, 162, 235, 1)',
                'rgba(255, 206, 86, 1)',
                'rgba(75, 192, 192, 1)',
                'rgba(153, 102, 255, 1)',
                'rgba(255, 159, 64, 1)'
            ],
            borderWidth: 1
        }]
    },
    options: {
        maintainAspectRatio: true, // default value. false일 경우 포함된 div의 크기에 맞춰서 그려짐.
        scales: {
            yAxes: [{
                ticks: {
                    beginAtZero:true
                }
            }]
        }
    }
});
</script>
```

- 그림은 다음과 같죠. 

<script src="https://cdnjs.cloudflare.com/ajax/libs/Chart.js/2.4.0/Chart.min.js"></script>
<div style="width:800px">
    <canvas id="myChart"></canvas>
</div>

<script>
// 우선 컨텍스트를 가져옵니다. 
var ctx = document.getElementById("myChart").getContext('2d');
/*
- Chart를 생성하면서, 
- ctx를 첫번째 argument로 넘겨주고, 
- 두번째 argument로 그림을 그릴때 필요한 요소들을 모두 넘겨줍니다. 
*/
var myChart = new Chart(ctx, {
    type: 'bar',
    data: {
        labels: ["Red", "Blue", "Yellow", "Green", "Purple", "Orange"],
        datasets: [{
            label: '# of Votes',
            data: [12, 19, 3, 5, 2, 3],
            backgroundColor: [
                'rgba(255, 99, 132, 0.2)',
                'rgba(54, 162, 235, 0.2)',
                'rgba(255, 206, 86, 0.2)',
                'rgba(75, 192, 192, 0.2)',
                'rgba(153, 102, 255, 0.2)',
                'rgba(255, 159, 64, 0.2)'
            ],
            borderColor: [
                'rgba(255,99,132,1)',
                'rgba(54, 162, 235, 1)',
                'rgba(255, 206, 86, 1)',
                'rgba(75, 192, 192, 1)',
                'rgba(153, 102, 255, 1)',
                'rgba(255, 159, 64, 1)'
            ],
            borderWidth: 1
        }]
    },
    options: {
        maintainAspectRatio: true, // default value. false일 경우 포함된 div의 크기에 맞춰서 그려짐.
        scales: {
            yAxes: [{
                ticks: {
                    beginAtZero:true
                }
            }]
        }
    }
});
</script>


## wrap-up

- 저는 원래 python에서 matplotlib을 사용해서 주로 그림을 그렸습니다. 그래서 결과는 보통, svg등으로 뽑아서 첨부하는 일이 많았죠. 
- 그런데, chart.js를 사용하면, flask로 데이터만 전달하면 웹브라우저에서 그림을 알아서 그려줍니다. 
- 즉, 백엔드에서는 python으로 데이터를 전처리해서 저장하고, flask에서 render_template를 사용해서 데이터를 보내고 나면 chart.js에서는 그림을 그려주는 것이죠. 
- 하핫. 대략 이렇습니다. 다음 포스팅에서는 여러 그림을 그려보겠습니다.

