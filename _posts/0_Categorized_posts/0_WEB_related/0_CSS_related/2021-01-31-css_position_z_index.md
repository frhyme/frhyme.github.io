---
title: CSS - z index
category: css
tags: css position
---

## CSS - z index

- z-index는 html 내에서 요소들이 서로 겹쳐졌을 때 머넞 보이는 순서를 말합니다. z-index값이 클수록 위에 있습니다. 즉 커야 가장 바깥 쪽에 위치한 다는 이야기죠. 아무 값도 설정하지 않았을 때는 가장 나중에 만들어진 요소가 가장 높은 우선순위를 가집니다.
- 다음 처럼 값을 설정해 줍니다.

```css
z-index: 0
```

## Example 

- 간단한 html 문서를 다음처럼 만들어 봤습니다.

```html
<!DOCTYPE html>
<html>
    <head>
        <meta charset="utf-8"/>
        <style>
            div {
                width: 200px;
                height: 200px;
                position: absolute;
                font-size: 40px;
            }
            .div1 {
                background-color: red;
                left: 0px;
                top: 0px;
                z-index: 0
            }
            .div2 {
                background-color: blue;
                left: 50px;
                top: 50px;
                z-index: 2
            }
            .div3 {
                background-color: green;
                left: 100px;
                top: 0px;
                z-index: 1
            }
        </style>
    </head>
    <body>
        <div>
            <div class='div1'>div1</div>
            <div class='div2'>div2</div>
            <div class='div3'>div3</div>
        </div>
    </body>
</html>
```
