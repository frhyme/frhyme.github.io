---
title: CSS - margin, padding, border
category: css
tags: css margin padding border
---

## CSS - margin, padding, border

- html의 각 요소는 모두 content, padding, border, margin이라는 값을 가집니다.
  - `content`: 일반적으로 각 요소에 정의하는 `width`, `height`는 content의 너비, 높이를 의미합니다. 이 값은 padding, border, margin에 따라 줄어들거나 커지지 않습니다. 고정되어 있죠.
  - `padding`: content와 border 사이의 간격을 의미합니다.
  - `border`: 테두리의 굵기를 의미합니다.
  - `margin`: border 밖의 간격을 의미합니다. 이 값이 커지면 다른 요소들과의 border 밖의 간격이 커지게 되죠.

```css
p {
    /*
    - 각 요소는 content > padding > border > margin으로 구성됩니다.
    - 일반적으로 width, height는 content의 너비, 높이를 말합니다.
    */
    width: 300px;
    height: 30px;
    border: 4px black solid;
    /*
    padding: top right bottom left
    - content와 border 사이의 간격을 의미합니다.
    - %로 정의하거나 음의 값을 넣는 것도 가능합니다.
    */
    padding: 50px 1px 3px 100px;
    /*
    margin: top right bottom left
    - border 외부의 간격을 의미합니다. 
    - 아래와 같이 모두 0으로 설정해버리면, 다른 요소들과 딱 붙게 되죠.
    - %로 정의하거나 음의 값을 넣는 것도 가능합니다.
    - auto 로 설정하는 경우 자동으로 여백을 동일하게 적용하여 중간 정렬하게 되죠.
    */
    margin: 0px 0px 0px 0px;   
}
```

- 간단하게 html 요소로 만들어봤습니다.

```html
<!DOCTYPE html>
<html>
    <head>
        <meta charset="utf-8"/>
        <style>
            p {
                background-color: blue;
                color: white;
                font-weight: bold;
                /*
                - 각 요소는 content > padding > border > margin으로 구성됩니다.
                - 일반적으로 width, height는 content의 너비, 높이를 말합니다.
                */
                width: 300px;
                height: 30px;
                border: 4px black solid;
                /*
                padding: top right bottom left
                - content와 border 사이의 간격을 의미합니다.
                - %로 정의하거나 음의 값을 넣는 것도 가능합니다.
                */
                padding: 50px 1px 3px 100px;
                /*
                margin: top right bottom left
                - border 외부의 간격을 의미합니다. 
                - 아래와 같이 모두 0으로 설정해버리면, 다른 요소들과 딱 붙게 되죠.
                - %로 정의하거나 음의 값을 넣는 것도 가능합니다.
                - auto 로 설정하는 경우 자동으로 여백을 동일하게 적용하여 중간 정렬하게 되죠.
                */
                margin: 0px 0px 0px 0px;   
            }
        </style>
    </head>
    <body>
        <p>Test Paragraph1</p>
        <p>Test Paragraph2</p>
        <p>Test Paragraph3</p>
    </body>
</html>
```
