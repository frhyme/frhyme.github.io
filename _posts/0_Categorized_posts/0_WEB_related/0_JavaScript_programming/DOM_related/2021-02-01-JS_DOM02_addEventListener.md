---
title: Javascript - addEventListener method
category: javascript
tags: javascript programming selector DOM event
---

## Javascript - addEventListener method

- html의 특정 요소에 특정한 event(ex: 마우스 클릭)가 발생했을 때 특정한 동작이 수행되도록 하는 방법을 정리합니다.
- 다음은 `element`에 마우스 클릭이 발생하면 `console.log`를 해주는 코드입니다.

```javascript
element.addEventListener(
    "click", 
    function() {
        console.log("Mouse Clicked");
    }
)
```

## DOM Events

- 다음과 같은 Event들이 있습니다. 자세한 건 [mozilla - developer - Web events](https://developer.mozilla.org/en-US/docs/Web/Events)에서 볼 수 있습니다.
- mouse event는 다음과 같습니다.
  - `click`: 마우스 왼쪽 버튼을 눌렀을 때 
  - `contextmenu`: 마우스 오른쪽 버튼을 눌렀을 때
  - `dblclick`: 왼쪽 마우스 버튼을 두 번 눌렀을때
- Keyboard event는 다음과 같습니다.
  - `keydown`: 키보드의 어떤 버튼이라도 눌렀을 때
  - `keyup`: 버튼을 눌렀다가 뗄 때

## Example

- 아래는 `#p1` 개체에 click하면 파란색으로 색깔이 바뀌도록 설정한 html 문서입니다.

```html
<!DOCTYPE html>
<html>
    <head>
        <meta charset="utf-8"/>
    </head>
    <body>
        <p id="p1">This is Paragraph</p>
        <script>
            document.querySelector("#p1").addEventListener(
                "click", 
                function() {
                    this.style.color = 'blue';
                }
            );
        </script>
    </body>
</html>
```
