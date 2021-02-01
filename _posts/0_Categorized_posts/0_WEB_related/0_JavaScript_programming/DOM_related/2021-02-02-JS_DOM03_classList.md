---
title: Javascript - class List
category: javascript
tags: javascript programming selector DOM class
---

## Javascript - class List

- html 특정 요소에게 속한 class들을 수정하는 방법을 정리하였습니다.

```html
<!DOCTYPE html>
<html>
    <head>
        <meta charset="utf-8"/>
    </head>
    <body>
        <!--
        - 이 요소는 3개의 class가 정의되어 있습니다.
        -->
        <p id="p1" class="c1 c2 c3">This is Paragraph</p>

        <script>
            let pElement = document.querySelector("#p1");
            console.log(pElement.classList);
            // DOMTokenList(3) ["c1", "c2", "c3", value: "c1 c2 c3"]
            
            // .contains: 특정 class가 있는지 확인
            console.log( pElement.classList.contains("c1") )
            // true
            
            // .remove: 특정 class를 삭제
            pElement.classList.remove("c1")
            console.log(pElement.classList);
            // DOMTokenList(2) ["c2", "c3", value: "c2 c3"]
            
            // .add: 특정 class를 추가
            pElement.classList.add("c1")
            console.log(pElement.classList);
            // DOMTokenList(3) ["c2", "c3", "c1", value: "c2 c3 c1"]
        </script>
    </body>
</html>
```