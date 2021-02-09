---
title: jQuery - focus, blur
category: jQuery
tags: jQuery javascript html web
---

## jQuery - focus, blur

- jQuery를 사용해서 input에 커서가 들어왔을때(focus), 나갈때(blur) input의 배경색을 변경해줍니다.

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
            
        <script>
            $(document).ready(function() {
                // input 창에 커서가 가면 배경을 blue로
                $("#name").focus(function() {
                    $(this).css("background-color", "blue");
                })
                // input 창에서 커서가 나가면 qoruddmf Red로
                $("#name").blur(function() {
                    $(this).css("background-color", "red");
                })
            });
        </script>
    </head>
    <body>
        <label for="name">Name: </label>
        <input type="text" id="name">
    </body>
</html>
```
