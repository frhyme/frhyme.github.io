---
title: html - table 만들기
category: html
tags: html table
---

## html - table 만들기

- 간단한 table을 만들었습니다.
  - `<table>`: 테이블 요소를 의미하는 tag
  - `<tr>`: row를 의미하는 tag
  - `<td>`: `<tr>` 내 각 cell을 의미하는 tag
  - `<th>`: table header를 의미하는 tag
  - `<caption>`: 테이블 제목을 의미하는 tag

```html
<table border="10">
    <caption>Student Table</caption>
    <tr>
        <th></th>
        <th>Student Name</th>
        <th>GPA</th>
    </tr>
    <tr>
        <th>First Row</th>
        <td>LSH</td>
        <td>2.00</td>
    </tr>
</table>
```
