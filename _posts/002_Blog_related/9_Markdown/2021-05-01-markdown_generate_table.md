---
title: Markdown - Generate table by python
category: markdown
tags: markdown python table
---

## Markdown - Generate table by python

- markdown에서는 table을 다음과 같이 표현합니다.

```plaintext
| colA  |colB|
|-------|----|
|  1    | 2  |
|  a    | b  |
| abc   | abc|
```

- 이걸 자동으로 만들어주는 python code를 만들었습니다. 어려운 코드가 아닌데, 지금 제가 필요해서 대충 짜서 사용하려고요 호호

```python
row_lst = [
    ['colA_name', 'colB_name', 'colC_name'], 
    [1, 2, 3],
    ["A", "B", "C"]
]

markdown_table_str = ""
for i, row in enumerate(row_lst):
    str_row = [str(x) for x in row]
    row_str = "|" + "|".join(str_row) + "|" + "\n"
    markdown_table_str += row_str
    if i == 0: 
        markdown_table_str += '|' + '-|' * len(str_row) + '\n'

print(markdown_table_str)
```
