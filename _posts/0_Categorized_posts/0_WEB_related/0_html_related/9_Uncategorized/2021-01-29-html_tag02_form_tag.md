---
title: html - form tag
category: html 
tags: html a tag form label input
---

## html - form tag

- html에서 form tag를 사용해서 사용자로부터 입력을 받는 방식을 정리하였습니다.
- 입력받는 방식도 다양한 형식이 있고, 입력받은 값을 다른 html 문서로 GET 혹은 POST 방식을 사용해서 보낼 수 있습니다.
- 그리고 입력받은 값은 전달받은 html 문서에서 javascript 혹은 php를 사용해서 해체해서 사용할 수 있습니다.

```html
<!DOCTYPE html>
<html>
    <head>
        <meta charset="utf-8">
        <title>Test html for a form and input</title>
    </head>
    <body>
        <!--
            method: GET or POST
            - GET: 주소창에 data를 함께 넘기는 방법
            - POST: data를 html body에 함께 넣어 넘기는 방법
            action: data가 도달되어야 하는 주소를 말합니다.
        -->
        <form action="result.html" method="GET">
            <!--
                type: 값을 어떤 변수 타입으로 보낼 것인지 정의
                name: 변수의 이름을 무엇으로 해서 보낼 것인지 정의
            -->
            <p>First  Input:</p><input type="text" name="firstValue"></input>
            <p>Second Input:</p><input type="text" name="secondValue"></input>
            <!--
                type="password"로 정의하면,
                값을 입력할 때 값이 숨겨집니다.
            -->
            <p>Password:</p><input type="password" name="password">

            <!-- Radio Button -->
            <h3> RadioButton </h3>
            <input type="radio" name="gender" value="male"> male </input>
            <input type="radio" name="gender" value="female"> female </input>
            <!-- Check Box -->
            <h3> CheckBox </h3>
            <label><input type="checkbox" name="language" value="python">python</label>
            <label><input type="checkbox" name="language" value="java"> Java</label>
            <label></label><input type="checkbox" name="language" value="R"> R</label>
            <br>
            <button type="submit">Submit</button>
        </form>
    </body>
</html>
```

- 위에서는 저렇게 썼지만, 사실 `label`과 `input`를 나누어 작성해주는 것이 좀 더 좋다고는 써 있습니다. 
- 아래에서는 명시적으로 label, input이 함께 연결되어 있기 때문이죠.

```html
<form action="" method="post">
    <label for="input1">Name:</label>
    <input type="text" name="name" id="input1">
    <input type="submit" value="Sign Up">
</form>
```
