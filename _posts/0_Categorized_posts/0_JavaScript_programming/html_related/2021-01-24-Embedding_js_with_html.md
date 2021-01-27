---
title: JavaScript 코드 html에 연결하기
category: html
tags: html javascript 
---

## JavaScript 코드 html에 연결하기

## 1 - html 내에 javascript 코드 그대로 넣기

- 다음처럼 html 파일 내에 javascript 소스를 그대로 집어넣을 수도 있구요.

```html 
<!DOCTYPE html>
<html>
    <head>
        <meta charset="utf-8">
        <title>Connecting JavaScript to HTML</title>
        <script>
        for(x=1; x<20;x++) {
            console.log(x)
        }
        </script>
    </head>
    <body>
        <script>
        
        </script>
    </body>
</html>
```

## 2 - html 내에 javascript 파일 경로 넣기

- 아래처럼 `test.js` 파일에는 다음을 작성하고

```javascript
// test.js
for(i=0; i<25;i++) {
    console.log(i)
}
```

- `test.html`에는 다음을 작성합니다. javascript 코드를 그대로 넣어주는 것이 아니라, `<script src="test.js"></script>`로 경로만 설정해줍니다.
  - 아래에서는 js를 head에 작성해주기는 했지만, 보통 body에 넣어줘도 상관없습니다. 보통 브라우저는 head를 먼저 읽고 그 다음 body 부분을 읽는데, 만약 js가 용량이 커서 오래 걸린다면 body 부분이 늦게 뜨게 됩니다. 따라서 오히려 body에 넣어주게 되면 일단 바디 부분이 뜬 다음, js 부분이 실행되므로 화면ㄴ이 더 빨리 뜨게 되죠.

```html
<!DOCTYPE html>
<html>
    <head>
        <meta charset="utf-8">
        <title></title>
        <!-- javascript file path -->
        <script src="test.js"></script>
    </head>
    </head>
    <body>
        <script>
        
        </script>
    </body>
</html>
```
