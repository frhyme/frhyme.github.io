---
title: Excel - VBA - If Statement
category: MS_Office
tags: MS_Office excel vba macro macOS basic
---

## Excel - VBA - If Statement

- VBA에서 If statement는 다음처럼 사용할 수 있습니다.
- 아래 코드는 변수 `a`의 값이 2의 배수, 3의 배수 그리고 나머지에 대해서 각각 서로 다른 메세지를 출력해 주도록 합니다.

```vb
Sub FirstFunction()
    Dim a As Integer
    a = 5
    ' a Mod b => a를 b로 나눈 나머지
    ' ex) 5 % 2 => 1
    If (a Mod 2) = 0 Then
        MsgBox ("2의 배수!")
    ElseIf a Mod 3 = 0 Then
        MsgBox ("3의 배수!")
    Else
        MsgBox ("2의 배수도 3의 배수도 아님!!")
    End If
End Sub
```

- 문법 적으로 보면 `If` 뒤에 반드시 `Then`이 와야 하고, 또 If 를 끝내면 `End If`를 넣어 주어야 한다는 것이 조금은 특이하네요.
