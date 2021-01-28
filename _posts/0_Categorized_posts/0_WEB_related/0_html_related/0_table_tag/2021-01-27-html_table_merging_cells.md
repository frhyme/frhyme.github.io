---
title: html - table 병합하기
category: html
tags: html table
---

## html - table 병합하기

- `rowspan`, `colspan` property를 사용해서 table의 cell의 병합해서 사용할 수 있습니다.

```html
<!DOCTYPE html>
<html>
    <head>
        <meta charset="utf-8">
        <title>Test html</title>
    </head>
    <body>
        <table border="1">
            <tr>
                <td rowspan="2">Cell-1-1 with rowspan 2</td>
                <td>Cell-1-2</td>
                <td>Cell-1-3</td>
            </tr>
            <tr>
                <td colspan="2">Cell-2-1 with colspan 2</td>
                <td rowspan="2">Cell-2-2</td>
            </tr>
        </table>
    </body>
</html>
```
