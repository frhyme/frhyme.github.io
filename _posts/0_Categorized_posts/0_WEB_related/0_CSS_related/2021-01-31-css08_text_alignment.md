---
title: CSS - Text Alignment
category: css
tags: css text alignment
---

## CSS - Text Alignment

- CSS의 `text-align`은 텍스트의 정렬 을 정의합니다.
  - `text-align: left`: 왼쪽 정렬
  - `text-align: right`: 오른쪽 정렬 
  - `text-align: center`: 가운데 정렬
  - `text-align: justify`: 양쪽 정렬

```css
.left {
    text-align: left;
}
.right {
    text-align: right;
}
.center {
    text-align: center;
}
.justify {
    text-align: justify;
}
```

## Example - Text Alignment

- 예제로 만들어본 문서는 다음과 같습니다.

```html
<!DOCTYPE html>
<html>
    <head>
        <meta charset="utf-8"/>
        <style>
            p {
                width: 400px;
                border: 1px solid blue;
            }
            .left {
                text-align: left;
            }
            .right {
                text-align: right;
            }
            .center {
                text-align: center;
            }
            /*
            justify: 양쪽 정렬
            - left alignment, right alignment는 각각 오른쪽 왼쪽에 공간이 조금씩 남는데.
            justify는 양 쪽에 남는 공간 없이 모두 채워 넣습니다.
            */
            .justify {
                text-align: justify;
            }
        </style>
    </head>
    <body>
        <p class="left">
            <b>Left Alignment</b> <br>
            This is long text. This is long text. This is long text. This is long text. This is long text. This is long text. This is long text. 
        </p>
        <p class="right">
            <b>Right Alignment</b> <br>
            This is long text. This is long text. This is long text. This is long text. This is long text. This is long text. This is long text. 
        </p>
        <p class="center">
            <b>Center Alignment</b> <br>
            This is long text. This is long text. This is long text. This is long text. This is long text. This is long text. This is long text. 
        </p>
        <p class="justify">
            <b>Justify Alignment</b> <br>
            This is long text. This is long text. This is long text. This is long text. This is long text. This is long text. This is long text. 
        </p>
    </body>
</html>
```
