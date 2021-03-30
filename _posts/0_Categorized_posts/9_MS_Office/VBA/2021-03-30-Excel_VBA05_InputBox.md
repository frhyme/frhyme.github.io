---
title: Excel - VBA - InputBox
category: MS_Office
tags: MS_Office excel vba macro macOS basic for
---

## Excel - VBA - InputBox

- InputBox를 사용하여 사용자로부터 값을 입력받을 수도 있습니다.

```vb
Sub FirstFunction()
    Dim inputString As String 
    inputString = InputBox("이름을 입력해주세요")
    MsgBox ("Your Name is " & inputString)
End Sub
```

- 사용자로부터 전달받는 값은 기본적으로 `String`이기 때문에, 만약 `Integer` 등으로 받고 싶다면 `CInt` 함수 등을 사용해서 변환해줘야 합니다.

```vb
Sub FirstFunction()
    Dim inputInteger As Integer
    inputInteger = CInt(InputBox("MsgBox 출력 수: "))
    For i = 1 To inputInteger
        MsgBox ("MsgBox " & i)
    Next i
End Sub
```
