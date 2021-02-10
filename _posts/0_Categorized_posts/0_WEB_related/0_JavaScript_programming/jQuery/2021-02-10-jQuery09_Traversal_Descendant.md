---
title: jQuery - Traversal - Descendant
category: jQuery
tags: jQuery javascript html web css html DOM
---

## jQuery - Traversal - Descendant

- jQuery를 사용해서 자식 element를 탐색하는 방법을 정리하였습니다.
  - `element.children()`: element의 바로 아래의 모든 자식 노드를 가리킵니다.
  - `element.find("#div1)`: element의 아래에 있는 모든 자식 노드들 중에서 `#div1`을 찾습니다.

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
                    // .children은 바로 아래에 있는 모든 node들을 가리킵니다.
                    $("#div1").children().css({
                        "border": "solid 10px"
                    })
                })
                $("#btn2").click(function() {
                    // .find()는 요소 아래에 있는 selector를 찾습니다.
                    $("#div1").find("#div2").css({
                        "border": "solid 10px"
                    })
                })
            });
        </script>
    </head>
    <body>
        <button id="btn1">button1</button>
        <button id="btn2">button2</button>
        <div id="div1">
            This is div1
            <div>
                <div>
                    <div id="div2">
                    </div>
                </div>
            </div>
            <div>
            </div>
        </div>
    </body>
</html>
```
