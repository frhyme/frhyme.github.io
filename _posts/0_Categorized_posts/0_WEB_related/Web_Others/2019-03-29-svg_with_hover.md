---
title: svg의 요소에 마우스를 올렸을때 내렸을 때 변화 넣기.
category: javascript
tags: javascript svg hover 
---

## svg의 요소에 마우스를 올렸을 때 변하는 것을 넣어보자

- png와 같은 그림이 아니라, svg와 같은 형태로 넘기게 될 경우, 해당 요소 내의 특정 부분에 마우스가 올라가거나 했을 때의 액션을 지정할 수 있습니다. 
- png에 비해서 훨씬 강력한 기능이죠. 
- 아무튼, 그걸 해봅니다.

## do it

- 생각보다 어렵지 않습니다. 
- 그냥 해당 요소에서 다음을 설정해주면 됩니다. 
  - 직관적이지만, `mouserover`는 마우스가 해당 개체 위에 올라왔을때, "mouseout"은 해당 개체가 마우스 밖으로 나갔을때를 의미합니다.

```javascript
svg.selectAll("circle")
.on("mouseover", function (d) {});
.on("mouseout", function (d) {});
```

- 간단하게 만들어본 코드는 다음과 같습니다.
  - 여러 원들을 임의로 만들고 
  - 해당 원 위로 마우스가 갔을때 특정한 텍스트를 새롭게 만들어서 추가해주고 
  - 해당 원 밖으로 마우스가 나가면, 그 텍스트를 삭제해줍니다.

```html
<html>
    <body>
        <div>
            <!-- d3js -->
            <svg id="aaa">
        
            </svg>
        </div>
        <script src="https://d3js.org/d3.v5.min.js"></script>
        <script>
            // data를 임의로 만들고, 
            var circle_lst = [];
            for (var i = 0; i < 10; i = i + 1) {
                circle_lst.push(
                    {
                        "id": "ID_"+String(i), 
                        "cx": Math.random() * 800,
                        "cy": Math.random() * 500,
                        "r": Math.random() * 100,
                    })
            }
            // svg를 선택하고 몇가지 특성을 정의해주고. 
            var svg = d3.select("#aaa");
            svg.attr('height', function (d) { return 500 })
            .attr('width', function (d) { return 1000 });
            // circle을 선택하고, 없기 때문에 넘치는 데이터의 수만큼 더 만들어주고, 
            // 또 각각의 요소의 특성을 설정해줍니다.
            svg.selectAll("circle").data(circle_lst).enter().append("circle")
                .attr('id', function (d) { return d['id'] })
                .attr('cx', function (d) { return d['cx'] })
                .attr('cy', function (d) { return d['cy'] })
                .attr('r', function (d) { return d['r'] })
                .attr('fill', function (d) { return 'blue' })
                .attr('fill-opacity', function (d) { return 0.2 })
                .attr('stroke', function (d) { return 'black' })
                .attr('stroke-width', function (d) { return 5 })
                // mouse가 해당 개체 위에 있을때 스타일 변화 
                .on("mouseover", function (d) {
                    // 마우스가 올라왔을 때 스타일 변화를 지정해주고, 
                    d3.select(this)
                        .transition()
                        .attr("fill-opacity", 1.0)
                        .duration(50);
                    // 마우스가 올라왔을때 텍스트가 새롭게 생성되도록 해줍니다.
                    var text_id = d["id"]+"_text";
                    // 아래처럼 현재 요소의 부모노드를 설정하도록 해도 되고, 
                    // 아니면, 해당 svg를 바로 찾아도 됩니다. 
                    d3.select(this.parentNode)// ex) d3.select("#aaa")
                        .append("text")
                        .attr("id", d["id"]+"_text")
                        .attr("x", d["cx"] + d["r"])
                        .attr("y", d["cy"] + d["r"])
                        .attr("font-size", "10px")
                        .text(function () { return [d["cx"], d["cy"]] })
                })
                // mouse가 해당 개체 를 벗어났을 때 스타일 변화 
                .on("mouseout", function (d) {
                    // 마우스가 해당 개체를 벗어났을 때의 스타일 변화를 지정해주고, 
                    d3.select(this)
                        .transition()
                        .attr("fill-opacity", 0.2)
                        .duration(50);
                    // 텍스트를 제거해줍니다.
                    var text_id = d["id"] + "_text";
                    d3.select("#"+text_id).remove();
                });
        </script>
    </body>
</html>
```

## wrap-up

- 생각보다 매우 간단하군요 하하하.
