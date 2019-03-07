---
title: d3js에서 transition 이용하기. 
category: others
tags: d3js javascript transtion 
---

## d3js에서 transition 사용하기

- d3.interval을 이용하면, 비교적 간단한 애니메이션을 만들 수 있습니다. 
- 그런데, 이 경우, 개체의 움직임이 자연스럽게 움직이게 되지 않습니다. 간단하게 flash를 생각하시면, 플래쉬의 경우 움직일 때 개체가 자연스럽게 움직이게 되잖아요?, 그걸 d3js에서도 구현하고 싶은 것이죠. 

## do it

- 아래 코드를 사용하면 됩니다. 
- 길어보이지만, 결국 transtion, duration, delay만 이해하면 됩니다. 
    - transition: 개체의 어떤 특성을 어떻게 변환시킬 것이라는 것을 알림
    - duration: 해당 변환이 몇 밀리초 안에 진행되는가
    - delay: 해당 변환이 몇 초 뒤에 진행되는가
        - 특히, 여기서, 콜백함수의 경우 `d`, `i`를 모두 argument로 전달받습니다. 만약, 선택된 개체가 10개라면, 개체의 번호에 따라서, delay를 조절할 수 있다는 이야기입니다.

```html 
<html>
    <head>
        <script src="https://d3js.org/d3.v5.js"></script>
    </head>
    <body>
        <svg>

        </svg>
        <script>
            var data = [100, 200, 300, 400, 500, 600];
            var scale = 10;
            var svg = d3.select('svg').attr("width", "750px").attr("height", "750px");

            // 다음처럼 요소의 특성을 변환시킬 수 있습니다. 
            d3.select("body").transition().style("background-color", "red");
            
            // transition을 사용해서 변형할 요소를 문서 내에 추가해줍니다. 
            svg.selectAll("circle").data(data)
            .enter().append('circle')
            .attr("cx", function (d) { return d; })
            .attr("cy", function (d) { return 20; })
            .attr("r", function (d) { return 10; });
            
            svg.selectAll("circle")
            // transition
            // duration: 해당 transition이 어느 정도의 시간동안 진행되는지
            // delay: 선택한 요소가 n개 일때, 이를 i로 iterable하게 따라가면서, 언제 transition이 시작되는지 포인트를 잡음.
            .transition().duration(500).delay(function(d, i) { return i * 1000})
            .attr("fill", function (d) { return "hsl(" + Math.random() * 360 + ", 100%, 50%" })
            .attr("r", function (d) { return Math.sqrt(d * scale); })
            .attr("cy", function (d) { return d; })
            .attr("stroke", function (d) { return 'black'; })
            .attr("stroke-width", function (d) { return 10; })
            .on('mouseenter', function () {
                    d3.select(this)
                        .transition()
                        .attr('r', 10);
                })
                .on('mouseleave', function () {
                    d3.select(this)
                        .transition()
                        .attr('r', 6);
                })
        </script>
    </body>
</html>
```

## wrap-up

- 현재로서는 단 1번만 트랜지션할 수 있는 것으로 보입니다. 만약 여러 개의 트랜지션을 순차적으로 수행하고 싶다면, 어떤 식으로 해야 할지 모르겠네요. 
- 나중에 알아보도록 하겠습니다 하하하