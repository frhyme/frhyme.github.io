---
title: CSS - List Style
category: css
tags: css unit width height
---

## CSS - List Style

- html 요소인 `list`들에 대해서 스타일을 적용하는 방법을 정리하였습니다.
- 한 줄로 표현하려면 다음과 같이 정의하면 됩니다.

```css
ul {
    /*
    순서대로 type position image를 의미합니다.
    */
    list-style: circle outside none;
}
```

- 저는 각 스타일별로 하나씩 적용해주는 것을 더 좋아하는 편이라서, 다음처럼 처리합니다.

```html
<!DOCTYPE html>
<html>
    <head>
        <meta charset="utf-8"/>
        <style>
            ul {
                /*
                list-style-type: 다음중 
                - disc(default), circle, decimal, upper-roman
                */
                list-style-type: circle;
                /*
                list-style-position: marker의 위치를 조절합니다.
                - outside(default), inside
                */
                list-style-position: outside;
                /*
                list-style-image: marker를 image로 사용합니다.
                - marker의 url를 표시해줍니다.
                */
                list-style-image: url(https://findicons.com/files/icons/1715/gion/24/list_add.png);
            }
        </style>
    </head>
    <body>
        <ul>
            <li> item 1 </li>
            <li> item 2 </li>
        </ul>
    </body>
</html>
```
