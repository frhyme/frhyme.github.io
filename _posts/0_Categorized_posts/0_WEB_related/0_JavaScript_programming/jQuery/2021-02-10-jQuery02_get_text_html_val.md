---
title: jQuery - Get text, val, attribute
category: jQuery
tags: jQuery javascript html web
---

## jQuery - Get text, val, attribute

- html 요소로부터 text, html, attribute 등을 가져오는 방법을 정리합니다.
  - `$("#p1").text()`: id가 "p1"인 요소로부터 text를 가져옵니다.
  - `$("#p1").html()`: id가 "p1"인 요소로부터 html을 가져옵니다.
  - `$("#name1").val()`: id가 "name1"인 input 요소로부터 입력된 값을 가져옵니다.
  - `$("#A").attr("href")`: id가 "A"인 요소의 href attribute를 가져옵니다.

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
                console.log(
                    $("#p1").text()
                ); // This is paragraph
                console.log(
                    $("#p1").html()
                ); // This is <b>paragraph</b>
                console.log(
                    $("#name").val()
                ); // Value1
                console.log(
                    $("#name").attr("type")
                ); // text
                console.log(
                    $("#A").attr("href")
                ); // http://frhyme.github.io
            });
        </script>
    </head>
    <body>
        <p id="p1">This is <b>paragraph</b></p>
        <label for="name">Name: </label>
        <input type="text" id="name" value="Value1">
        <a id="A" href="http://frhyme.github.io"></a>
    </body>
</html>
```
