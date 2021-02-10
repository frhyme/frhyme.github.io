---
title: jQuery - Remove Element
category: jQuery
tags: jQuery javascript html web
---

## jQuery - Remove Element

- jQuery를 사용하여 element를 추가하고 지우는 방법을 정리합니다.

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
            .cls1 {
                width: 300px;
                height: 30px;
                background-color: blue;
                color:white;
            }
        </style>
        <script>
            $(document).ready(function() {
                $("#btn1").click(function() {
                    // #div1 내에 새로운 p 요소를 추가해줍니다.
                    $("#div1").append("<p>new paragraph</p>")
                })
                $("#btn2").click(function() {
                    // #div1 내의 모든 요소를 삭제해줍니다.
                    $("#div1").empty()
                })
                $("#btn3").click(function() {
                    // #div1의 자식 요소들 중에 첫번째 p 요소를 삭제합니다.
                    $("#div1").children().first("p").remove()
                })
            });
        </script>
    </head>
    <body>
        <button id="btn1">Append new p in div1</button>
        <button id="btn2">Empty div1</button>
        <button id="btn3">Remove First p</button>
        <div id="div1">This is div1</div> 
    </body>
</html>
```
