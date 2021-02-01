---
title: Javascript - DOM methods - querySelector, getElementById
category: javascript
tags: javascript programming selector DOM
---

## Javascript - DOM methods - querySelector, getElementById

- javascript에서 문서 내에 존재하는 element들을 selector, id를 통해 탐색하고 해당 요소의 성질을 변경하는 코드를 작성하였습니다.

```javascript
// document.getElementById
// id가 "p1"인 요소를 1개 찾아서 리턴합니다.
document.getElementById("p1");

// document.querySelector
// 문서 내에서 가장 먼저 나오는 p element를 리턴합니다.
document.querySelector("p");
// 문서 내에 등장하는 class1 element를 리턴합니다.
document.querySelector(".class1");
// 문서 내에 등장하는 #id1 element를 리턴합니다.
document.querySelector("#id1");

// document.querySelectorAll
// 문서 내에 등장하는 p element들을 모두 모아서 list로 리턴합니다.
document.querySelectorAll("p");
```

## Example

- 간단하게 다음과 같은 코드를 작성하였습니다.

```html
<!DOCTYPE html>
<html>
    <head>
        <meta charset="utf-8"/>
    </head>
    <body>
        <h2>This is h2</h2>
        <p id="p1">This is p1</p>
        <p>This is paragraph</p>
        <p>This is paragraph</p>
        <p>This is paragraph</p>
        <p>This is paragraph</p>
        <!--
        script 문은 보통 head에 집어넣지만, 이 경우 head에 집어넣으면
        id가 "p1"인 element가 생성되기 전에 script가 돌아가므로 document_p1은 null이 됩니다. 
        따라서 뒤에 넣어줘야죠.
        -->
        <script>
            // get Element By its ID
            function changeElementByID(targetID) {
                var targetElement = document.getElementById(targetID);
                targetElement.style.color = 'blue';
                targetElement.style.fontSize = '20px';
                console.log("changeElementByID Done!")
            }
            // get Element By Select
            function changeElementBySelector(targetSelector) {
                var targetSelector = document.querySelector(targetSelector);
                targetSelector.style.color = 'red';
                console.log("changeElementBySelector Done!")
            }
            // get Elements(복수) By Select 
            // selector를 모두 모아서 list로 리턴합니다.
            function changeElementsBySelector(targetSelector) {
                var elements = document.querySelectorAll(targetSelector)
                for (i in elements) {
                    elements[i].style.fontSize = "30px"
                }
                console.log("changeElementsBySelector Done!")
            }
            
            // 2 초 뒤에 아래 함수들을 실행함.
            setTimeout(() => 
                {
                    changeElementByID("p1")
                    changeElementBySelector("h2")
                    changeElementsBySelector("p")
                }, 2000
            );
        </script>
    </body>
</html>
```
