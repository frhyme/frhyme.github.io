---
title: d3 이용해보기 - make three circle
category: others
tags: d3js d3 javascript html animation
---

## d3js를 이용해서 간단하게 그림을 좀 그려보려고 합니다. 

- 기본적으로는 d3js의 tutorial에 있는 [이 포스트](https://bost.ocks.org/mike/circles/)를 참고하였으나, 애니메이션을 넣었다는 점에서 차이가 있습니다. 
- 아무튼, 기본 html 페이지에 내용이 다음과 같이 있다고 합시다. 
    - `svg`라는 태그에서는 너비와 높이, 즉, 해당 태그가 페이지 내에서 차지하는 영역을 표시해주고, 
    - `circle`라는 태그는 각각 원을 의미합니다. 더 명확하게는 안에 attribute들이 모두 포함되어 있어야 하지만, 지금은 아무것도 포함되어 있지 않죠. 
- circle은 javascript 혹은 html에서 이미 기본적으로 알고 있는 소스입니다. 
- 제가 여기서 javascript를 이용해서 하려는 것은 circle의 속성들, xy좌표, 색깔, 반지름 등을 변경해주는 것이죠. 

```html
<html>
    <head>
        <script src="https://d3js.org/d3.v5.js"></script>
    </head>
    <body>
        <!--그림이 그려지는 부분-->
        <svg width="720" height="720">
            <circle></circle>
            <circle></circle>
            <circle></circle>
            <circle></circle>
        </svg>
    </body>
</html>
```

### use d3 

- 이를 위해서 script내에 코드를 작성해줍니다. 
- 다음처럼 작성하고 코드를 실행해주면, 뭐 잘 그려집니다. 

```html
<html>
    <head>
        <script src="https://d3js.org/d3.v5.js"></script>
    </head>
    <body>
        <!--그림이 그려지는 부분-->
        <svg width="720" height="720">
            <circle></circle>
            <circle></circle>
            <circle></circle>
            <circle></circle>
        </svg>
        <script>
            // tag selection: 변경할 태그를 선택합니다. 
            var svg = d3.selectAll('svg');
            var circle = svg.selectAll("circle");
            // 데이터를 다른 곳에서 가져오는 것보다, 이미 가져온 태그에 그대로 묶어주는 것이 좋음. 
            // 이를 data binding이라고 하며, 우선 묶어줄 데이터를 만들어줍니다. 
            var circle_data_lst = []
            for (var i = 0; i < circle.size(); i++) {
                circle_data_lst.push({
                    'cx': Math.random() * svg.attr('width'),
                    'cy': Math.random() * svg.attr('height'),
                    'r': Math.random() * 100,
                    'color': "hsl(" + Math.random() * 360 + ",100%,50%)"
                })
            }
            // d3 요소에 데이터를 바인딩합니다. 
            circle.data(circle_data_lst);
            // 바인딘됭 데이터(d)로부터 데이터를 이용해서 attribute를 변경할 수 있습니다. 
            // 한번에 모두 바꿀 수 있다는 것이 특이점이죠. 
            circle.attr("cx", function (d) { return d['cx'] });
            circle.attr("cy", function (d) { return d['cy'] });
            circle.attr("r", function (d) { return d['r'] });
            circle.attr("fill", function (d) { return d['color'] });
        </script>
    </body>
</html>
```

### make animation 

- 이제 animation을 만들겁니다. 애니메이션을 만들기 위해서는 d3의 interval이라는 메소드를 이용해야 하는데요, 이게 구조가 조금 특이합니다.
    - 저는 당연히, interval에 어떤 값으로서 예를 들어서, `until`과 같은 값을 넘기는 것이라고 생각했는데, 그게 아니라, 콜백함수로서 새로운 것을 넘겨줘야 하는 것 같습니다. 
    - `d3.interval()`함수의 첫번째 argument로 함수를 넘겨주는데, 해당 함수는 `elapsed`라는 argument를 전달받아서 이 값에 따라서 수행하거나, 시간이 넘을 경우 멈추는 식의 제어를 해주어야 합니다. 
    - 두번째 argument로는몇 milesecond에 한번씩 앞서 나온 펑션을 수행할 것인가? 를 정의하는 것이죠. 

```javascript
var interval1 = d3.interval(
    function(elapsed){
        if (elapsed<2000){
            animate_circle();//interval 마다 수행될 함수
        }else{
            interval1.stop();//이 function이 해당된 
        }
    }, 500)
```

- 만약 헷갈린다면 다음처럼 표현하는 것이 나을 수도 있습니다. 

```javascript
var circle_interval = new d3.interval(
    function(elapsed){
        if (elapsed<5000){
            animate_circle();//console.log(elapsed);
        }else{
            this.stop();
        }
    }, 1000)
```

## 결과 코드

- 아무튼, 이런식으로 만든 최종 코드는 다음과 같습니다. 

```html
<html>
    <head>
        <script src="https://d3js.org/d3.v5.js"></script>
    </head>
    <body>
        <!--그림이 그려지는 부분-->
        <svg width="720" height="720">
            <circle></circle>
            <circle></circle>
            <circle></circle>
            <circle></circle>
        </svg>
        <script>
            // 매 animation 시에 그려지는 그림. 
            function animate_circle(){
                var svg = d3.selectAll('svg');
                var circle = svg.selectAll("circle");
                // change color
                // data binding: 딕셔너리의 형태로 넘길 수도 있음. 
                // binding할 데이터를 생성 
                var circle_data_lst = []
                for (var i = 0; i < circle.size(); i++) {
                    circle_data_lst.push({
                        'cx': Math.random() * svg.attr('width'),
                        'cy': Math.random() * svg.attr('height'),
                        'r': Math.random() * 100,
                        'color': "hsl(" + Math.random() * 360 + ",100%,50%)"
                    })
                }
                // d3 요소에 데이터를 바인딩함. 
                circle.data(circle_data_lst);
                // 바인딘됭 데이터(d)로부터 데이터를 이용해서 attribute를 변경할 수 있음. 
                circle.attr("cx", function (d) { return d['cx'] });
                circle.attr("cy", function (d) { return d['cy'] });
                circle.attr("r", function (d) { return d['r'] });
                circle.attr("fill", function (d) { return d['color'] });
            }
            // 아래 구조는 좀 특이합니다. 
            var circle_interval = new d3.interval(
                function(elapsed){
                    if (elapsed<5000){
                        animate_circle();//console.log(elapsed);
                    }else{
                        this.stop();
                    }
                }, 1000)
        </script>
    </body>
</html>
```

## wrap-up

- 정리하자면, 다음과 같습니다. 
    - html 문서 상에서 이후 그림이 추가될 부분을 요소로서 만들어두고, 
    - 이 요소에 발생한 변경사항 들을 script를 이용해서 만들어두고 
    - 필요할 경우 애니메이션 기능을 사용해서 적용한다. 