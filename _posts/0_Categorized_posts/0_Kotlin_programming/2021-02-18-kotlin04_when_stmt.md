---
title: Kotlin - When statement
category: kotlin
tags: kotlin programming when
---

## Kotlin - When statement

- kotlin에서 `when`은 `switch`와 유사한 형태의 명령문입니다.
- `switch`의 경우 하나의 조건에 대해서만 일일이 matching할 수 있었떤 반면, `when`은 여러 조건을 동시에 한 줄에 작성할 수 있습니다.
- 우리가 흔히 아는 switch문과 유사하게는 다음처럼 작성할 수 있고요.

```kotlin
fun main() {
    var op_lst = arrayOf("+", "*", "plus", "minus", "-", "/");

    for (i in 0 until op_lst.size) {
        var op = op_lst.get(i);
        print("${op} :: ")
        when (op) {
            "+", "plus" -> println("Addition")
            "-", "minus" -> println("Substraction")
            "*", "times" -> println("Multiplication")
            else -> println("Not supported Operation")
        }
    }
    /*
    OUTPUT
    + :: Addition
    * :: Multiplication
    plus :: Addition
    minus :: Substraction
    - :: Substraction
    / :: Not supported Operation
    */
}
```

- 다음처럼 `println` 내에, 즉 함수 내에 parameter처럼 넘겨버릴 수도 있죠.

```kotlin
fun main() {
    var x:Int = 1;

    println(
        when (x) {
            1 -> "x = 1"
            2 -> "x = 2"
            else -> "x != 1 and !=2"
        }
    )
    // x = 1
}
```

- 다음처럼 범위로 지정해서 처리할 수도 있습니다.

```kotlin
fun main() {
    var x:Int = 10;
    println(
        when (x) {
            in  1..10 -> " 1 <= x <= 10"
            in 11..20 -> "11 <= x <= 20"
            else -> "21 <= x"
        }
    )
}
```
