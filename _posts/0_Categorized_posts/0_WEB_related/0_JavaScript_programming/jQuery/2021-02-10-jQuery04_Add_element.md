---
title: jQuery - Add Element
category: jQuery
tags: jQuery javascript html web
---

## jQuery - Add Element

- html 요소에 새로운 요소를 추가하거나, text를 변경하거나 하는 작업을 정리합니다.

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
                    // #div1의 내부 text의 끝에 "END"를 추가해줍니다.
                    $("#div1").append("END")
                })
                $("#btn2").click(function() {
                    // #div의 내부 text의 앞에 "HEAD"를 추가해줍니다.
                    $("#div1").prepend("HEAD")
                })
                $("#btn3").click(function() {
                    // body의 뒤에 새로운 요소를 추가해줍니다.
                    $("body").append("<div class='cls1'>New div</div>")
                })
                $("#btn4").click(function() {
                    // #div1 요소 앞에 새로운 html요소를 넣어줍니다.
                    $("#div1").before("<p>new Paragraph before div1</p>")
                })
                $("#btn5").click(function() {
                    // #div1 요소 뒤에 새로운 html요소를 넣어줍니다.
                    $("#div1").after("<p>new Paragraph after div1</p>")
                })

            });
        </script>
    </head>
    <body>
        <div id="div1"></div>
        <button id="btn1">Append Text</button>
        <button id="btn2">Prepend Text</button>
        <button id="btn3">Append New Div1</button>
        <button id="btn4">Add p Before div1</button>
        <button id="btn5">Add p After div1</button>
    </body>
</html>
```
