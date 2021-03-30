---
title: Excel - VBA - Data type - Variant
category: MS_Office
tags: MS_Office excel vba macro macOS basic
---

## Excel - VBA - Data Type

- Macro 내에서 다음처럼 Integer 변수를 선언해주고, 계산을 할 수도 있습니다.

```vb
Sub FirstFunction()
    ' a, b를 Integer 변수로 선언 및 정의
    Dim a As Integer
    Dim b As Integer
    a = 10 
    b = 5
    ' & 를 사용해서 문자열(등)을 연결할 수 있음.
    MsgBox ("a + b = " & (a + b))
End Sub
```

### Data Type - String 

- 다음처럼 String type 변수를 선언해줄 수도 있습니다.

```vb
Sub FirstFunction()
    Dim s As String
    s = "myFirstString"
    MsgBox (s)
End Sub
```

### Data Type - Variant 

- 위의 코드에서는 두 변수를 모두 Integer로 선언해주었습니다. 그러나, 혹시 변수 타입(type)이 변경될 수도 있을 경우, 그냥 아래처럼 Variant로 선언해줄 수도 있습니다. 보통 변수 type이 명시되지 않은 경우 Variant로 정의됩니다. "해당 변수는 데이터 타입이 정의되어 있지 않고 상황에 따라서 바뀐다"라고 이해하시면 됩니다.

```vb
Sub FirstFunction()
    Dim a As Variant
    Dim b As Variant
    ' a에는 Double의 데이터가 들어갔고
    ' b에는 Integer의 데이터가 들어갔다.
    a = 10.5
    b = 3
    ' 둘의 연산 결과는 Double으로 추론된다.
    MsgBox ("a + b = " & (a + b))
End Sub
```

- 따라서, 다음처럼 해당 변수 자체에 담기는 데이터가 여러 종류여도 상관없죠. 처음에는 `10`이라는 Integer를 담았다가, `"aaaa"`라는 String을 담아도 에러가 발생하지 않습니다.

```vb
Sub FirstFunction()
    Dim a As Variant
    a = 10
    MsgBox (a)
    a = "aaaa"
    MsgBox (a)
End Sub
```

## Reference 

- [microsoft - docs - variant data type](https://docs.microsoft.com/en-us/office/vba/language/reference/user-interface-help/variant-data-type)
