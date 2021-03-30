---
title: Excel - VBA - For Statement
category: MS_Office
tags: MS_Office excel vba macro macOS basic for
---

## Excel - VBA - For Statement

- excel에서 For 문은 다음처럼 정의해서 사용합니다.
- 코드 자체는 별 의미가 없습니다. 그냥 `Exit For`를 사용하려고 의미없는 If 문을 넣어주었어요.

```vb
Sub FirstFunction()
    Dim i As Integer
    For i = 1 To 5 Step 1
        If i Mod 4 = 0 Then
            ' Break 를 의미함
            Exit For
        Else
            MsgBox ("AAA" & i)
        End If
    ' For Block의 끝에는 Next가 있어야 함.
    Next
End Sub
```

- 역순으로 진행하고 싶다면 다음처럼 하면 됩니다. 5부터 1까지 순차적으로 감소하면서 진행되죠.

```vb
Sub FirstFunction()
    Dim i As Integer
    For i = 5 To 1 Step -1
        MsgBox ("AAA" & i)
    Next
End Sub
```

### Next i

- 위에서는 `Next` 다음에 아무것도 써주지 않았습니다. 하지만, 다음처럼 Next 뒤에 `i`, `j` 등을 붙여 주면 For 문을 길게 쓰는 경우 가독성이 조금 더 좋아지죠.

```vb
Sub FirstFunction()
    Dim i As Integer
    For i = 1 To 3 Step 1
        For j = 1 To 2 Step 1
            MsgBox (i & " * " & j & " = " & (i * j))
        Next j
    Next i
End Sub
```
