---
title: CSS - Relative Unit
category: css
tags: css unit width height
---

## CSS - Relative Unit

- `%`를 사용해서 요소를 해당 요소의 outer의 설정 값에 비례해서 선택하도록 할 수 있습니다.
- `vw`, `vh`를 사용하면 현재 브라우저의 width, height에 따라서 해당 요소의 크기가 변하게 되죠.
- `vmin`, `vmax`는 각각 "width, hegith 중에서 작은 값의 1%, 큰 값의 1%"를 의미합니다. 이 값에 비례해서 상대적인 값을 결정할 수 있죠.

```html
<!DOCTYPE html>
<html>
    <head>
        <meta charset="utf-8"/>
        <style>
            div {
                /* 
                - 1vw: 현재 브라우저의 width의 1%
                - 1vh: 현재 브라우저의 height의 1% 
                */
                width: 50vw;
                height: 50vh;
                background-color: red;
                font-size: 20px;
            }
            div p {
                width:75%;
                height:125%;
                font-size: 2em; /* 200%와 같음*/;
                background-color: blue;
            }
            /*
            - 1vmin: 현재 브라우저의 width, heigth 중에서 작은 값의 1%
            - 1vmax: 현재 브라우저의 width, heigth 중에서 큰 값의 1%
            */
            #id1 {
                width: 50vmin;
                height: 20vmax;
                background-color: green;
            }
        </style>
    </head>
    <body>
        <div>
            This is div
            <p>
                This is p in div
            </p>
        </div>
        <p id='id1'>This is id1</p>
    </body>
</html>
```
