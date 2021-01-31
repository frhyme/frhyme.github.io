---
title: html - a tag
category: html 
tags: html a tag hyperlink
---

## html - a tag

- html 문서 내에서 hyperlink를 표현할 수 있는 `<a>` tag를 사용하는 방법을 정리합니다.
- href attribute에 `URL`을 그대로 넣을 수도 있고 혹은 `#<id>`를 넣어줌으로써 해당 요소가 있는 곳으로 움직이도록 할 수도 있죠.

```html 
<!DOCTYPE html>
<html>
    <head>
        <meta charset="utf-8">
        <title>Test html for a tag</title>
    </head>
    <body>
        <a href="https://frhyme.github.io/" target="_self">Open My Blog in this browser tab</a>
        <!-- a 는 inline element이기 때문에 <br>을 사용해서 줄바꿈을 해줘야 합니다.-->
        <br>
        <a href="https://frhyme.github.io/" target="_blank">Open My Blog in new browser tab</a>

        <!--
        - 내부의 특정한 id를 가진 element로 움직이고 싶다면 다음처럼 하면 됩니다.
        -->
        <br>
        <a href="#bottom">Move to the Bottom</a>
        <br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br>
        <br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br>
        <br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br>
        <p id="bottom">This is BOTTOM</p>
    </body>
</html>
```
