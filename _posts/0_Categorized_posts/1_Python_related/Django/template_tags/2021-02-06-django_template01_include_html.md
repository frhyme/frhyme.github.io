---
title: python - Django - include html
category: python
tags: python programming django web template tag
---

## python - Django - include html

- html 문서 내에 다른 html 문서를 집어 넣을 수 있습니다.
- 가령 아래와 같은 `table1.html`를 다른 문서에 집어넣고 싶다고 하겠습니다.

```html
<!-- table1.html -->
<h3> Table1 </h3>
<table>
    <tbody>
        <tr>
            <td>1</td>
            <td>2</td>
            <td>3</td>
        </tr>
        <tr>
            <td>A</td>
            <td>B</td>
            <td>C</td>
        </tr>
    </tbody>
</table>
```

- 이 때는 아래 처럼 `{% include html_file_path %}`를 사용해서 넣어주면 됩니다.

```html
<!DOCTYPE html>
<html lang="en">
  <head>
      <meta charset="UTF-8">
  </head>
  <body>
    <!--
    - 외부에 정의된 ./table1.html을 현재 html 문서에 넣어줍니다.
    -->
    {% raw %}{% include "./table1.html" %}{% endraw %}
  </body>
</html>
```
