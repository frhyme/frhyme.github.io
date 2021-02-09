---
title: jQuery - basic
category: jQuery
tags: jQuery javascript html web
---

## jQuery - basic

- jQuery는 아주 활발하게 사용되는 Javascript library로, 보통 DOM manipulation, AJAX 호출 등을 간편하게 처리할 수 있도록 해주는 라이브러리입니다.
- 기본적으로는 다음의 형태로 사용되죠. `selector`를 정하고, `action()`을 연쇄적으로 적용해줍니다.

```javascript
$(selector).action()
```

- `.ready()`를 사용하면 html 요소가 완전히 load될 때까지 기다렸다가 `function()`를 실행하게 됩니다.

```javascript
$(document).ready(function(){})
```

- 예를 들어, 다음 javascript 코드는 "document가 load되면, button element들에 대해서 click event가 발생하면, 해당 요소를 hide한다"를 의미합니다.

```javascript
$(document).ready(function() {
    $("button").click(function() {
        $(this).hide();
    });
});
```

## Example

- 앞서 말한 예제의 전체 코드는 다음과 같습니다.

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
                $("button").click(function() {
                    $(this).hide();
                });
            });
        </script>
    </head>
    <body>
        <button type="button">button1</button>
        <button type="button">button2</button>
        <button type="button">button3</button>
    </body>
</html>
```
