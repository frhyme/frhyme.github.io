---
title: Excel - VBA - Range
category: MS_Office
tags: MS_Office excel vba macro macOS basic 
---

## Excel - VBA - Range

- `Range`를 사용하여 Cell의 범위에 한번에 값을 지정해줄 수 있습니다.
- 시트의 특정 범위에 값을 하나씩 입력하는 것 보다는 한번에 입력해주는 것이 시간상 훨씬 효율적입니다.

```vb
Sub FirstFunction()
    Dim range1 As Range
    ' Range("A1", "C3")와 Range("A1:C3")와 같습니다.
    Set range1 = Range("A1", "C3")
    
    ' range1과 같은 크기의 Array를 만듭니다.
    ' range1에 들어갈 값을 미리 계산하여 vArr에 넣어두고
    ' 이후에 값을 Range에 한 번에 다 넣어둡니다.
    Dim vArr(3, 3) As Variant
    For i = 0 To 2 Step 1
        For j = 0 To 2 Step 1
            vArr(i, j) = 100 * i + j + 3
        Next j 
    Next i 
    ' Range에 Array를 한번에 넣어줍니다.
    ' 이렇게 한번에 넣어주는 경우가 하나씩 넣는 것에 비해 속도 면에 월등히 빨라요.
    range1.Value = vArr()
End Sub
```
