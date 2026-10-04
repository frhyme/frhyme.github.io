---
title: "Excel - VBA - Function"
date: 2021-03-31
category: "dev-tools"
tags: ["ms_office", "excel", "vba", "macro", "macos", "basic", "function"]
permalink: "/ms_office/Excel_VBA11_Function/"
---

### Function with Return type

- 함수 내에서 리턴하는 값이 있는 경우는 다음처럼 작성합니다.
- 그리고 해당 함수를 호출할 때, 앞에 `Call`이라는 명령어를 작성하지 않습니다.

```vb
Function plus(a As Integer, b As Integer) As Integer
    Dim return_value As Integer
    return_value = a + b
    ' 함수에서 값을 리턴할 때는 다음처럼 처리해줍니다.
    ' FunctionName = ReturnValue
    plus = a + b
End Function

Sub FirstFunction()
    MsgBox (plus(1, 2))
End Sub
```

### Function without Return type

- 함수 내에서 리턴하는 값이 없는 경우에는 `Call`이라는 명령어를 써줘야 오류가 발생하지 않습니다.

```vb
Function plus(a As Integer, b As Integer) As Integer
    MsgBox (a + b)
End Function

Sub FirstFunction()
    ' plus 함수가 아무것도 리턴하지 않으므로
    ' 앞에 Call 명령어를 사용해줍니다.
    Call plus(1, 2)
End Sub
```