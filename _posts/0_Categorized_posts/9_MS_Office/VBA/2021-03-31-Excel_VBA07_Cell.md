---
title: Excel - VBA - Cell
category: MS_Office
tags: MS_Office excel vba macro macOS basic
---

## Excel - VBA - Cell

- 보통 VBA는 Excel의 Cell들과 상호작용하려고 사용합니다. 본 글에서는 Cell의 사용법에 대해서 정리합니다.

## Get, Update Cell Value

- `Cells(RowIntegerIdx, ColumnIntegerIdx)`를 사용해서 엑셀 시트 상에서 `RowIntegerIdx` 행, `ColumnIntegerIdx` 열에 존재하는 Cell에 접근하고, `.Value` 프로퍼티에 접근하여 해당 Cell에 존재하는 값을 가져옵니다.
- 해당 Cell의 값을 업데이트해줄 때도 해당 `Cells(RowIntegerIdx, ColumnIntegerIdx).Value`에 그대로 값을 assign해주면 됩니다.
- 원래는 `WorkSheets("SheetName").Cells`과 같이 `SheetName`도 작성해주는 것이 좋지만, 여기서는 굳이 적지 않고 생략하였습니다.

```vb
Sub FirstFunction()
    Dim existing_value As Variant
    ' Cells(RowIntegerIdx, ColumnIntegerIdx)
    ' 시트 이름을 따로 입력하지 않으면, 매크로가 존재하는 기본 시트의 Cell
    ' 1, 2이므로 B1의 값을 가져옴
    existing_value = Cells(1, 2).Value 
    ' 값을 업데이트해줄 때도, 다음과 같이 .Value에 그대로 assign
    Cells(1, 2).Value = existing_value + "AAA"
End Sub
```

## Get, Update Cell Address

- 해당 Cell의 주소값이 무엇인지(`.Address`), 몇 번 째 행에 위치해 있는지(`.Row`), 몇 번째 column에 위치해 있는지(`.Column`)도 알 수 있습니다.

```vb
Sub FirstFunction()
    Dim cell_address As String
    Dim row_index As Integer
    Dim col_index As Integer

    cell_address = Cells(1, 2).Address
    row_index = Cells(1, 2).Row
    col_index = Cells(1, 2).Column

    MsgBox (cell_address) 
    ' $B$1
    MsgBox (row_index) 
    ' 1 
    MsgBox (col_index) 
    ' 2
End Sub
```
