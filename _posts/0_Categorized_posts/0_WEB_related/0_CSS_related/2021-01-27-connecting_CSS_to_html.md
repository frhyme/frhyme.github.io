---
title: html 내에 CSS 연결하기 
category: html
tags: html CSS
---

## html 내에 CSS 연결하기 

- 아래와 같이, html 문서 내 `<head>` 태그 내에 다음 부분을 넣어줍니다.

```html 
<link rel="stylesheet" href="style.css">
```

- 전체 html 문서를 보면 다음과 같죠.
- 사실 꼭 `<head>`에 들어갈 필요는 없습니다. 그냥 `<body>`에 넣어도 css가 적용되기는 해요.

```html
<!DOCTYPE html>
<html>
    <head>
        <meta charset="utf-8">
        <title>Test html</title>
        <!-- 이렇게 CSS를 연결합니다 -->
        <link rel="stylesheet" href="style.css">
    </head>
    <body>
        <p> This is p!!</p>
    </body>
</html>
```

- `test.html`과 같은 폴더 내에 `style.css`를 둡니다.

```css
/*
style.css
*/
p {
    color:blue;
}
```

- 혹은 그냥 다음처럼 내부에 바로 작성해도 문제는 없습니다.

```html
<!DOCTYPE html>
<html>
    <head>
        <meta charset="utf-8">
        <title>Test html</title>
        <!-- 이렇게 CSS code를 직접 넣어줍니다 -->
        <style>
            p {
                color:blue;
            }
        </style>
    </head>
    <body>
        <p> This is p!!</p>
    </body>
</html>
```
