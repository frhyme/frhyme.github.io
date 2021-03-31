---
title: Excel - VBA - Offset
category: MS_Office
tags: MS_Office excel vba macro macOS basic 
---

## Excel - VBA - Offset

- `.Offset`은 특정 Cell에서 행으로 몇 칸, 열로 몇 칸 움직여서 그 위치에 해당하는 Cell을 가리킵니다.
- `Cells(1, 1)`: 1행 1열에 위치한 Cell을 말하므로 "A1"에 위치한 Cell를 가리키죠.
- `Cells(1, 1).Offset(0, 1)`: 1행 1열에 위치한 Cell에서 열로 1칸 움직였으므로 "A2"를 가리키고.
- `Cells(1, 1).Offset(1, 1)`: 1행 1열에 위치한 Cell에서 행 1칸, 열로 1칸 움직였으므로 "B2"를 가리킵니다.

## Offset with For loop 

- For loop문과 Offset을 이용하여 `Cells(1, 1)`부터 총 3행, 3열의 matrix에 값을 입력하는 코드를 만들었습니다.

```vb
Sub FirstFunction()
    Dim row_size As Integer
    Dim col_size As Integer
    
    Set start_cell = Cells(1, 1)
    row_size = 2
    col_size = 3

    For i = 0 To row_size
        For j = 0 To col_size
            start_cell.Offset(i, j).Value = 10 * i + j
        Next j 
    Next i
    '  0  1  2  3
    ' 10 11 12 13
    ' 20 21 22 23
End Sub
```
