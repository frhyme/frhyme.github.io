---
title: jQuery - set css property
category: jQuery
tags: jQuery javascript html web css html
---

## jQuery - set css property

- jQuery를 사용해서 특정 요소의 css property를 수정하는 방법을 정리하였습니다.

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
        </style>
        <script>
            $(document).ready(function() {
                $("#btn1").click(function() {
                    // #div1의 css property를 변경해줍니다.
                    $("#div1").css({
                        "background-color": "blue", 
                        "width": "300px",
                        "height": "100px",
                    })
                })
            });
        </script>
    </head>
    <body>
        <button id="btn1">button1</button>
        <div id="div1">This is div</div>
    </body>
</html>
```
