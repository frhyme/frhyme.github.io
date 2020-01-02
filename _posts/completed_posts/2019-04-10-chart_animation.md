---
title: chart.js를 애니메이션을 사용해서 차트 업데이트하기. 
category: javascript
tags: chartjs d3js animation javascript
---

## chart를 주기적으로 변경하기. 

- 별거 아니고요. 주기적으로 데이터가 변하거나, 업데이트될 경우, 그에 맞춰서 차트도 변경될 수 있도록 하려고 합니다. 
- 비교적 간단하게, chart.js와 d3.js를 가지고 사용해봤습니다. 

## do it

- d3와 chartjs를 사용합니다. 
- 우선 chartjs를 사용해서 차트를 그립니다. 
- 그 다음 데이터가 변경된다면, 다음처럼 데이터를 변경해주면 됩니다. 
    - 그냥 딕셔너리와 리스트에 접근하는 것처럼 순차적으로 접근하고 assign operator를 사용해서 처리해주면 되죠. 
    - 그리고 끝에는 업데이트 해주는 것을 추가해줘야 합니다. 업데이트를 하지 않으면 다시 그려주지 않아요. 

```javascript
myChart.data.datasets[0].data = [1, 2, 3, 4, 5, 6];
myChart.update();
```

- 그리고, 우선 chart.js에서는 매번 차트를 그릴 때마다 애니메이션이 들어갑니다. 여기서 말하는 애니메이션은 그림이 바로 뜨는 것이 아니라 일종의 transition으로 뜬다는 것이죠. 
    - 그러나, 우리는 데이터를 변경해주면서 차트를 그릴 것이기 때문에, 이 트랜지션 부분을 삭제해주는 것이 좋습니다. 
    - 이를 위해서 `option.animation.duration = 0`으로 처리해줍니다. 
- 그리고 기존의 `d3.interval`에 관련 내용들을 넣어주면 됩니다. 

```html
<html>
    <head>
        <!-- d3.js -->
        <script src="https://d3js.org/d3.v5.min.js"></script>
        <!-- chart.js -->
        <script src="https://cdnjs.cloudflare.com/ajax/libs/Chart.js/2.4.0/Chart.min.js"></script>
    </head>
    <body>
        <canvas id="myChart" width="400" height="200"></canvas>
        <script>
        var ctx = document.getElementById('myChart').getContext('2d');
        var myChart = new Chart(ctx, {
            type: 'bar',
            data: {
                labels: ['Red', 'Blue', 'Yellow', 'Green', 'Purple', 'Orange'],
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
                        'rgba(255, 99, 132, 1)',
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
                animation: {
                    duration: 0
                }, 
                scales: {
                    yAxes: [{
                        ticks: {
                            beginAtZero: true
                        }
                    }]
                }
            }
        });
        // label 변경
        myChart.data.labels = ["R", "B", "Y", "G", "P", "O"];
        // 그냥 마치, 딕셔너리 리스트의 자료구조인 것처럼 접근해서 값을 변경해줘도 문제없습니다. 
        myChart.data.datasets[0].data = [1, 2, 3, 4, 5, 6];
        myChart.update();
        var frame_duration = 1000;
        var i=0;
        d3.interval(
            function(){
                if (i > 10) {
                    this.stop();
                }
                else {
                    myChart.data.datasets[0].data = [1 + i, 2 + i, 3 + i, 4 + i, 5 + i, 6 + i];
                    myChart.update(); // 데이터를 바꾼 다음, 이렇게 업데이트를 해야 적용된다.
                }
                i=i+1;
            }, 
            frame_duration
        );
        </script>
    </body>
</html>
```

## wrap-up

- 생각보다 매우 간단합니다. 
- 그리고 chart.js를 통해 만든 객체가 그냥 자료구조인것처럼 쉽게 assign될 수 있도록 처리 된 것이 매우 좋습니다. 아주 편하네요. 