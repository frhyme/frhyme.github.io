---
title: Excel - VBA - 변수 선언 및 정의
category: MS_Office
tags: MS_Office excel vba macro macOS basic 
---

## Excel - VBA - 변수 선언 및 정의

- VBA에서는 `Dim`을 사용하여 변수를 선언합니다.
- 그리고 변수를 값(Value)를 정의해줄 때는 `=`를 사용하지만, 객체(Object)를 정의할 때는 `Set`를 사용합니다.

```vb
Sub FirstFunction()
    ' Value type의 변수는 다음처럼 선언 및 정의하고
    Dim var1 
    var1 = 10

    ' Object type의 변수는 다음처럼 선언 및 정의합니다. 
    Dim var2
    ' Set를 사용하지 않으면 오류가 발생
    Set var2 = Cells(1, 2) ' B2
    var2.Value = 10
End Sub
```

- 개체를 정의해줄 때 `Set`를 사용하지 않으면 다음 오류가 발생합니다.

```plaintext
런타임 오류 '424' 
개체가 필요합니다.
```

- 또 사실 다음처럼 `Dim`은 굳이 사용쓰지 않아도 큰 문제는 없습니다.

```vb
Sub FirstFunction()
    ' Value type의 변수는 다음처럼 선언 및 정의하고
    var1 = 777

    ' Object type의 변수는 다음처럼 선언 및 정의합니다. 
    Set var2 = Cells(1, 2) ' B2
    var2.Value = var1
End Sub
```
