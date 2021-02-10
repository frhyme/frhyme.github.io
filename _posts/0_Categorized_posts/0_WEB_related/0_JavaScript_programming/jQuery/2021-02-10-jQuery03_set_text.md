---
title: jQuery - Set text
category: jQuery
tags: jQuery javascript html web
---

## jQuery - Set text

- jQuery를 사용해서 요소의 text, html, attribute를 바꿀 수 있습니다.
- 다음 코드는 `#btn1` 요소를 클릭했을 때, `#div1`의 text가 바뀌도록 설정하는 것을 말합니다. 구조는 대략 이런 형태인 것이죠.

```javascript
$("#btn1").click(function() {
    $("#div1").text("Button1 Click")
})
```

- 다음처럼 callback function을 사용해서 설정해줄 수도 있습니다.
- callback function의 인자는 `(i, originalText)`이며, 기존 요소의 순번과 원래 text를 참고해서 변형할 수 있죠.

```javascript
// callback 함수를 사용해서 변경해줄 수도 있습니다.
// callback 함수의 인자는 i, originalText인데
// i: 해당 요소 내에 있는 요소들의 순번
// originalText: 원래 작성되어 있는 text
$("#btn4").click(function() {
    $("#ol1").html(
        function(i, originalText) {
            return originalText + "<li>" + "text"+ + i + "</li>"
        }
    )
})
```

- 전체 코드는 다음과 같습니다.

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
                height: 100px;
                background-color: blue;
                color:white;
            }
        </style>
        <script>
            $(document).ready(function() {
                // text를 변경해줍니다.
                $("#btn1").click(function() {
                    $("#div1").text("Button1 Click")
                })
                // html을 변경해줍니다.
                $("#btn2").click(function() {
                    $("#div1").html("<b>Button</b> Click")
                })
                // attribute를 변경해 줍니다.
                // class도 attribute이므로 변경해줄 수 있죠.
                $("#btn3").click(function() {
                    $("#div1").attr({
                        "class": "cls1"
                    })
                })
                // callback 함수를 사용해서 변경해줄 수도 있습니다.
                // callback 함수의 인자는 i, originalText인데
                // i: 해당 요소 내에 있는 요소들의 순번
                // originalText: 원래 작성되어 있는 text
                $("#btn4").click(function() {
                    $("#ol1").html(
                        function(i, originalText) {
                            return originalText + "<li>" + "text"+ + i + "</li>"
                        }
                    )
                })
            });
        </script>
    </head>
    <body>
        <div id="div1"></div>
        <button id="btn1">Change Text</button>
        <button id="btn2">Change html</button>
        <button id="btn3">Change width, height</button>
        <button id="btn4">Add Text</button>
        <ol id="ol1">
        </ol>

    </body>
</html>
```
