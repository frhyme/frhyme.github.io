---
title: html - Ordered, Unordered, Definition List
category: html 
tags: html list 
---

## html - Ordered, Unordered, Definition List

- 간단하게, `<li>` tag를 사용해서 List를 만들어 줬습니다. 
- `<ol>`로 묶으면 Ordered List, `<ul>`로 묶으면 Unordered List가 되죠. 번호를 매기는 순서나, 형태, 모양 등을 변경할 수 있죠.
- 마지막에는 `dl`이라는 `Definition List`를 의미하는 tag도 있습니다. table의 형태처럼, `(term, defintion)`이 한 row에 오도록 만들어 집니다.

```html 
<!DOCTYPE html>
<html>
    <head>
        <meta charset="utf-8">
        <title>Test html for List</title>
    </head>
    <body>
        <h3> Order List start from 1(default)</h3> 
        <ol>
            <li>Order Element 1</li>
            <li>Order Element 2</li>
            <li>Order Element 3</li>
            <li>Order Element 4</li>
        </ol> 
        
        <h3> Order List start from a, b, c</h3> 
        <ol type='a'>
            <li>Order Element 1</li>
            <li>Order Element 2</li>
            <li>Order Element 3</li>
            <li>Order Element 4</li>
        </ol> 

        <h3> Order List reversed: 4, 3, 2, 1</h3> 
        <ol reversed>
            <li>Order Element 1</li>
            <li>Order Element 2</li>
            <li>Order Element 3</li>
            <li>Order Element 4</li>
        </ol> 

        <h3> UnOrdered List reversed with circle(default)</h3> 
        <ul>
            <li>Element 1</li>
            <li>Element 2</li>
        </ul> 

        <h3> UnOrdered List reversed with square</h3> 
        <ul type='square'>
            <li>Element 1</li>
            <li>Element 2</li>
        </ul> 

        <h3> Definition List</h3> 
        <dl>
            <dt>Term1</dt>
            <dd>Description of Term 1</dd>
            <dt>Term2</dt>
            <dd>Description of Term 2</dd>
        </dl> 
    </body>
</html>
```
