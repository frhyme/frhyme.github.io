---
title: CSS - Pseudo Class
category: css
tags: css PseudoClass 
---

## CSS - Pseudo Class

- css에서 각 요소들의 property를 사용자의 동작에 따라 변하도록 할 수 있습니다.
- 가령 다음과 같이, `h1:hover`에 대해서 정의하면 `h1`요소에 마우스가 올라가면(hover), 빨간 색으로 바뀌도록 할 수 있죠.

```css
h1:hover {
    color: red;
}
```

## Test Example

- 간단하게 예제를 만들었습니다.

```html
<!DOCTYPE html>
<html>
    <head>
        <meta charset="utf-8"/>
        <style>
            a:hover {
                /* a에 mouse가 올라갈 때 */
                background: green;
                font-weight: bold;
            }
            li:first-child {
                /* li의 1번째 요소 */
                background: green;
            } 
            li:nth-child(2) {
                /* li의 2번째 요소 */
                background: black;
            } 
            li:nth-child(3n) {
                /* li의 3의 배수 번째 요소 */
                background: purple;
            } 
            li:last-child {
                /* li의 마지막 요소 */
                background: red;
            } 
            h1:hover {
                /* h1 요소에 마우스가 올라가면 */
                color: red;
            }
        </style>
    </head>
    <body>
        <h1> Test Page(h1) </h1>
        <a href="http://frhyme.github.io"> My Blog(frhyme.github.io)</a>
        <ul>
            <li>Item 1</li>
            <li>Item 2</li>
            <li>Item 3</li>
            <li>Item 4</li>
            <li>Item 5</li>
            <li>Item 6</li>
            <li>Item 7</li>
            <li>Item 8</li>
            <li>Item 9</li>
            <li>Item 10</li>
        </ul>
    </body>
</html>
```
