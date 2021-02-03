---
title: d3에서 enter, exit를 알아보쟈. 
category: others
tags: javascript d3js 
---

## enter, exit, update in d3.js

- 이해하고 나면 간단한 개념입니다. 그리고 이 개념은 사실 d3, Data-Driven Document의 철학과 일치한다고 생각합니다. 
- Data-Driven Document를 한국말로 변환하면, 데이터주도 문서, 정도로 할 수 있겠죠. 즉, 데이터가 먼저 오고, 이에 맞춰서 문서가 생성된다고 생각하면 됩니다. 
- 실제로 d3를 가지고 요소를 만들 때, 우선 data binding부터하는 것은 그러한 이유때문인 것으로 생각됩니다.

- 생각을 해봅시다. 데이터가 먼저, 데이터 퍼스트인 환경 속에서, html 문서 내에서 데이터가 몇 개가 들어올지 먼저 알 수 있을까요? 

- 예를 들어서, 아래와 같은 html 문서가 있다고 해봅시다. 
    - `chart1`에는 단 1개의 circle이 있습니다. 만약 1개 이상의 circle이 만들어져야 한다면, 아니 정확하게는 1개 이상의 데이터를 반영해야 한다면 어떻게 해야 할까요? 
    - `chart2`에는 6개의 circle이 있습니다. 그런데 만약 data의 수가 6개 미만이라서, 몇 개의 circle을 삭제하려면 어떻게 해야 할까요?

```html
<svg id='chart1'>
    <circle></circle>
</svg>
<svg id='chart2'>
    <circle></circle>
    <circle></circle>
    <circle></circle>
    <circle></circle>
    <circle></circle>
    <circle></circle>
</svg>
```

- data가 기존의 요소의 수보다 많을 때는 `enter` 메소드를 이용하고 `append`를 통해 넘치는 데이터의 수만큼 더 넣어주고
- data가 기존의 요소의 수보다 적을 때는 `exit` 메소드를 이용해서 `remove`를 통해 부족한 데이터의 수만큼을 지워줍니다. 
- 이 두가지가 다에요. 사실 쉬운 개념들입니다. 

## do it.

- 아래 코드에서는 임의의 데이터를 생성해주고, 
- 생성된 데이터를 바인딩해준다음
- 데이터가 기존 요소의 수보다 많을 때 와, 적을 때를 각각 `enter` ==> `append`, `exit` ==> `remove`로 처리해주었습니다. 

```html
<!DOCTYPE html>
<html>
    <head>
        <script src="https://d3js.org/d3.v5.js"></script>
    </head>
    <body>
        <svg id='chart1'>
            <circle></circle>
        </svg>
        <svg id='chart2'>
            <circle></circle>
            <circle></circle>
            <circle></circle>
            <circle></circle>
            <circle></circle>
            <circle></circle>
        </svg>
        
        <script>
            /*
            Enter
            - data가 기존 html 요소의 수보다 많을 때는, enter를 사용해서 남는 데이터들을 추가로 선택해주고 스타일을 변경해줍니다.
            - id로 찾을때는 샵을 쓴다. 아이디어샵낄낄
            */
            var chart1 = d3.select('#chart1').attr('width', 750).attr('height', 375);
            var chart1_data_lst = []
            for (var i = 0; i < 10; i++) {
                chart1_data_lst .push({
                    'cx': Math.random() * chart1.attr('width'),
                    'cy': Math.random() * chart1.attr('height'),
                    'r': Math.random() * 100,
                    'color': "hsl(" + Math.random() * 360 + ",100%,50%)"
                })
            }
            chart1.selectAll('circle')
                .data(chart1_data_lst) //data binding, 요소에 있는 circle의 수보다, 데이터의 수가 더 많습니다. 
                .attr('r', function(d){return d['r']})
                .attr('cx', function(d){return d['cx']})
                .attr('cy', function (d) { return d['cy'] })
                .attr('fill', function (d) { return d['color'] })
                .enter() // data의 수가 더 많기 때문에, enter를 사용하고 
                .append('circle') // 더 많은 수만큼 circle을 만들어주고, 더 생성된 circle의 특성을 변환시켜줍니다. 
                .attr('r', function (d) { return d['r'] })
                .attr('cx', function (d) { return d['cx'] })
                .attr('cy', function (d) { return d['cy'] })
                .attr('fill', function (d) { return d['color'] })
            /*
            Exit 
            - data가 기존 html의 요소보다 적을 때는 exit를 사용해서 넘치는 요소들을 선택해주고, remove를 사용해서 지웁니다. 
            - 이를 통해 기존 html 문서에 잉여로 남아있는 circle 요소를 지울 수 있음.
            */
           var chart2 = d3.select('#chart2').attr('width', 750).attr('height', 375);
           var chart2_data_lst = []
           for (var i = 0; i < 2; i++) {
               chart2_data_lst.push({
                   'cx': Math.random() * chart2.attr('width'),
                   'cy': Math.random() * chart2.attr('height'),
                   'r': Math.random() * 100,
                   'color': "hsl(" + Math.random() * 360 + ",100%,50%)"
                })
            }
            console.log(chart2_data_lst);
            chart2.selectAll('circle')
                .data(chart2_data_lst) //data binding, 요소에 있는 circle의 수보다, 데이터의 수가 더 많습니다. 
                .attr('r', function (d) { return d['r'] })
                .attr('cx', function (d) { return d['cx'] })
                .attr('cy', function (d) { return d['cy'] })
                .attr('fill', function (d) { return d['color'] })
                .exit().remove();//잉여 요소를 선택하고 지웁니다.
        </script>
    </body>
</html>
```

## wrap-up

- 이해하고 나면 매우 간단한 개념이고요, 중요한 것은, d3.js에서 바로 데이터에 기반해서 많으면 많은대로 적으면 적은대로 알아서 그림을 변경해줄 수 있다는 것이 강점이다, 라고 말할 수 있겠네요.

## reference

- <https://bost.ocks.org/mike/join/>