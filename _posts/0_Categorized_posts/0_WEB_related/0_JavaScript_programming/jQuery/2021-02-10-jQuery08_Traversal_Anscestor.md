---
title: jQuery - Traversal - Ancestor
category: jQuery
tags: jQuery javascript html web css html DOM
---

## jQuery - Traversal - Ancestor

- jQuery를 사용해서 부모 element를 탐색하는 방법을 정리하였습니다.
  - `element.parent()`: element의 바로 위 부모 element를 가리킵니다.
  - `element.parents()`: element의 바로 위, 그 위 부모등 모든 부모들을 가리킵니다.

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
                padding: 10px 10px 10px 10px;
                border: solid 1px;
            }
        </style>
        <script>
            $(document).ready(function() {
                $("#btn1").click(function() {
                    // .parent()는 바로 위의 부모 node만 가리키고
                    $("#div1").parent().css({
                        "border": "solid 5px"
                    })
                })
                $("#btn2").click(function() {
                    // .parents()는 부모, 할아버지 등 모든 노드를 가리킵니다.
                    $("#div1").parents().css({
                        "border": "solid 5px"
                    })
                })
            });
        </script>
    </head>
    <body>
        <button id="btn1">button1</button>
        <button id="btn2">button2</button>
        <div>
            <div>
                <div>
                    <div id="div1">
                        This is div1
                    </div>
                </div>
            </div>
        </div>
    </body>
</html>
```
