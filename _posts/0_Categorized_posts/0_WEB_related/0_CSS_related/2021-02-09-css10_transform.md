---
title: CSS - transform
category: css
tags: css Transform html
---

## CSS - transform

- css의 `transform`를 사용해서 요소를 이동(translate), 기울이기(skew), 회전(rotate), 확대 혹은 축소(scale)하는 방법을 정리하였습니다.

## Define style.css

- css를 다음과 같이 정의합니다.

```css
.basic {
    position: absolute;
    top: 10px;
    left: 10px;
    background-color: mediumaquamarine;
    width: 200px;
    height: 200px;
}

.elem_translate {
    position: absolute;
    top: 10px;
    left: 10px;
    background-color: cornflowerblue;
    width: 200px;
    height: 200px;
    transform: translate(50%, 100px);
}

.elem_skew {
    position: absolute;
    top: 200px;
    left: 200px;
    background-color: rebeccapurple;
    width: 200px;
    height: 200px;
    transform: skew(-30deg)
}

.elem_rotate {
    position: absolute;
    top: 300px;
    left: 300px;
    background-color: green;
    width: 200px;
    height: 200px;
    transform: rotate(45deg)
}

.elem_scale {
    position: absolute;
    top: 400px;
    left: 400px;
    background-color: orange;
    width: 200px;
    height: 200px;
    transform: scale(0.5)
}
```

## define html

- html 요소는 다음과 같이 정의합니다.

```html
<!DOCTYPE html>
<html>
    <head>
        <meta charset="utf-8"/>
        <link rel="stylesheet" href="style.css" />
    </head>
    <body>
        <div class="basic">basic</div>
        <div class="elem_translate">translate</div>
        <div class="elem_skew">skew</div> 
        <div class="elem_rotate">rotate</div> 
        <div class="elem_scale">rotate</div> 
    </body>
</html>
```
