---
title: jQuery - Traversal - Filter
category: jQuery
tags: jQuery javascript html web css html
---

## jQuery - Traversal - Filter

- jQuery를 사용하여, 요소를 filter하는 방법을 정리합니다.
  - `.first()`: 요소중에서 첫번째 요소를 리턴
  - `.last()`: 요소중에서 마지막 요소를 리턴
  - `.eq(i)`: 요소중에서 i번째 요소를 리턴(0부터 시작)
  - `.filter(".class1")`: 요소 중에서 class가 `class1`인 애들만 남깁니다.
  - `.not(".class1")`: 요소 중에서 class가 `class1` 아닌 애들만 남깁니다.

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
                    // first(0): first 요소
                    $("div").first().css({
                        "border": "solid 10px"
                    })
                })
                $("#btn2").click(function() {
                    // last(0): last 요소
                    $("div").last().css({
                        "border": "solid 10px"
                    })
                })
                $("#btn3").click(function() {
                    // eq(0): 0번째 요소
                    $("div").eq(3).css({
                        "border": "solid 10px"
                    })
                })
                $("#btn4").click(function() {
                    // filter(".cls1"): ".cls1"인 요소들만 filter
                    $("div").filter(".cls1").css({
                        "border": "solid 10px"
                    })
                })
                $("#btn5").click(function() {
                    // not(".cls1"): cls1이 아닌 것들만
                    $("div").not(".cls1").css({
                        "border": "solid 10px"
                    })
                })
            });
        </script>
    </head>
    <body>
        <button id="btn1">first div</button>
        <button id="btn2">last div</button>
        <button id="btn3">4th div</button>
        <button id="btn4">div with cls1</button>
        <button id="btn5">div not cls1</button>
        <div>div1</div>
        <div>div2</div>
        <div class="cls1">div3 class="cls1"</div>
        <div>div4</div>
        <div>div5</div>
        <div>div6</div>
    </body>
</html>
```
