---
title: jQuery - Add Class
category: jQuery
tags: jQuery javascript html web css html
---

## jQuery - Add Class

- jQuery를 사용해서 class를 추가하고 삭제하는 방법을 정리하였습니다.

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
            .blue {
                background-color: blue;
                color:white;
            }
            .red {
                background-color: red;
                color:white;
            }
            .green {
                background-color: green;
                color:white;
            }
        </style>
        <script>
            $(document).ready(function() {
                $("#btn1").click(function() {
                    // #div1 내에 새로운 class를 추가해줍니다.
                    $("#div1").addClass("blue")
                })
                $("#btn2").click(function() {
                    // #div1 내에 새로운 class를 추가해줍니다.
                    $("#div1").addClass("red")
                })
                $("#btn3").click(function() {
                    // #div1 내에 class를 삭제해줍니다.
                    $("#div1").removeClass("blue")
                })
                $("#btn4").click(function() {
                    // #div1 내에 class를 삭제해줍니다.
                    $("#div1").removeClass("red")
                })
                $("#btn5").click(function() {
                    // #div1 내에 class가 없으면 추가하고, 
                    // class가 있으면 삭제해줍니다.
                    $("#div1").toggleClass("green")
                })
            });
        </script>
    </head>
    <body>
        <button id="btn1">Add Blue Class</button>
        <button id="btn2">Add Red Class</button>
        <button id="btn3">Remove Blue Class</button>
        <button id="btn4">Remove Red Class</button>
        <button id="btn5">Toggle Green Class</button>
        <div id="div1">Target Text</div>
        
    </body>
</html>
```
