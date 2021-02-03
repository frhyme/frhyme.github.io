---
title: d3 transition 이용하기. 
category: others
tags: d3js javascript transition 
---

## transition을 이용해봅시다.

- 뭐, 딱히 길게 설명할 것이 없을 것 같으니, 바로 코드로 넘어가겟습니다. 

```html
<div>
    <!-- d3js -->
    <svg>
        
    </svg>
</div>
<script src="https://d3js.org/d3.v5.min.js"></script>
<script>
    // data를 임의로 만들고, 
    var circle_lst = [];
    for(var i=0;i<10;i=i+1){
        circle_lst.push(
            {
                "cx": Math.random() * 800,
                "cy": Math.random() * 500,
                "r": Math.random() * 100,
            })
    }
    console.log(circle_lst);
    
    var svg = d3.select("svg");
    svg.attr('height', function (d){ return 500});
    svg.attr('width', function (d) { return 1000 });

    svg.selectAll('circle').data(circle_lst).enter().append("circle")
        .attr('cx', function (d) { return d['cx']})
        .attr('cy', function (d) { return d['cy']})
        .attr('r', function (d) { return d['r'] })
        .attr('fill', function (d) { return 'black' })
        .attr('stroke', function (d) { return 'black' })
        .attr('stroke-width', function (d) { return 5 });

    // transition
    var circle = d3.selectAll("circle");
    circle
    .transition().style("fill", "red").duration(1000)
    .transition().style("fill", "green").duration(1000)
    .transition().style("r", "20").duration(1000)
    .transition().style("fill", "blue").duration(1000)
    //아래처럼 함수로 넘겨주는 것 또한 가능함.
    .transition().style("r", function(d) {return d['r']}).duration(1000)
</script>
```

## wrap-up

- 함수로 넘겨주는 것이 가능합니다. 순서는 transition, style, duration 이죠. 