---
title: d3에서 애니메이션 내에 애니메이션을 넣어보자. 
category: javascript
tags: javascript d3js 
---

## animation 내에 애니메이션 넣기. 

- 그냥, 애니메이션 내에 새로운 애니메이션을 또 넣어서 진행해도 되는지 알아봅니다. 
- 귀찮으니 그냥 코드를 그대로 넣어볼게요. 

## do it. 

- 그냥 같은 형식의 코드를 그대로 넣어주면 잘 굴러갑니다. 

```html
<html>
    <head>
        <script src="https://d3js.org/d3.v5.min.js"></script>
    </head>
    <body>
        <span id="ccc"></span>
        <div>
            <svg id="aaa" width="1000px" height="600px">

            </svg>
        </div>
    </body>
    <script>
        d3.select("#aaa")
        .append("circle")
        .attr("id", "bbb")
        .attr("cx", 500).attr("cy", 300)
        .attr("r", 20)
        .attr("fill", "red")
        .attr("stroke", "blue")
        .attr("stroke-width", 10)

        var r_lst = [100,6,70,20, 3, 10, 9]
        var i = 0;
        frame_duration = 3000
        // animation 
        d3.interval(
            function(){
                if(i > r_lst.length){
                    this.stop();
                }else{
                    var r_added = r_lst[i]
                    // 값에 따라서 frame의 간격을 조절합니다. 
                    var each_frame_duration = frame_duration/r_added
                    var j=0;
                    // nested animation 
                    d3.interval(
                        function(){
                            if(j>r_added){
                                this.stop();
                            }else{
                                d3.select("#bbb")
                                .attr("r", d3.select("#bbb").attr("r") * 1.0 + 1)
                            }
                            j=j+1
                        }, 
                        each_frame_duration
                    )    
                    d3.select("#ccc").text(i);
                }
                i=i+1;
            }, frame_duration
        )
    </script>
</html>

```

## wrap-up

- 참 쉽죠 하하하.