---
title: jQuery - Traversal - Siblings
category: jQuery
tags: jQuery javascript html web css html DOM
---

## jQuery - Traversal - Siblings

- jQuery를 사용해서 형제 element를 탐색하는 방법을 정리하였습니다.
  - `.next()`: 현재 element의 다음에 있는 형제 node를 1개 찾아서 리턴합니다.
  - `.siblings("div")`: 형제 노드 중에서 div인 애들만 찾아서 리턴합니다.

```html
<html>
    <head>
        <!--
        CDN을 통해서 jquery를 가져옵니다.
        -->
        <script 
            src="https://code.jquery.com/jquery-3.5.1.js" 
            integrity="sha256-QWo7LDvxbWT2tbbQ97B53yJnYU3WhH/C8ycbRAkjPDc=" 
            crossorigin="anonymous">
        </script>
        <style>
            div {
                padding: 10px;
                margin: 10px;
                border: solid 1px;
            }
        </style>
        <script>
            $(document).ready(function() {
                $("#btn1").click(function() {
                    // .next(): 현재 element의 다음에 있는 형제 node를 1개 찾아서 리턴합니다.
                    $("#div1").next().css({
                        "border": "solid 10px"
                    })
                })
                $("#btn2").click(function() {
                    // .siblings("div"): 형제 노드 중에서 div인 애들만 찾아서 리턴합니다.
                    $("#div1").siblings("div").css({
                        "border": "dashed 10px"
                    })
                })
            });
        </script>
    </head>
    <body>
        <button id="btn1">next()</button>
        <button id="btn2">all div siblings</button>
        <div id="div1">
            This is div1
        </div>
        <h2>H2 Sibling</h2>
        <div></div>
        <div></div>
        <div></div>
        <div></div>
    </body>
</html>
```
