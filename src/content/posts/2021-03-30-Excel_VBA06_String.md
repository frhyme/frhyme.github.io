---
title: "Excel - VBA - String"
date: 2021-03-30
category: "MS_Office"
tags: ["MS_Office", "excel", "vba", "macro", "macOS", "basic", "String"]
permalink: "/ms_office/Excel_VBA06_String/"
---

## Excel - VBA - String

- VBA에서는 `Left`, `Mid`, `Right` 함수를 사용하여 String 내의 특정 구간을 잘라낼 수 있습니다.
- `Len`함수를 사용하면 문자열의 길이를 확인할 수 있습니다.

```vb
Sub FirstFunction()
    Dim inputStr As String
    inputStr = "ABCDEFG"
    MsgBox (Left(inputStr, 2))
    ' AB
    MsgBox (Mid(inputStr, 1, 3))
    ' ABC
    MsgBox (Right(inputStr, 3))
    ' EFG
    MsgBox (Len(inputStr))
    ' 7
End Sub
```