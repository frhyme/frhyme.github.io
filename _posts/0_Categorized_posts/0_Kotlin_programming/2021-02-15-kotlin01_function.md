---
title: Kotlin - function
category: kotlin
tags: kotlin function 
---

## Kotlin - function

- Kotlin에서는 function 또한, Object로 사용되며 변수가 가리키도록 할 수도 있고, 함수에 넘겨주고 다시 함수에서 넘겨받는 것도 가능합니다. 보통 이런 걸, first-class citizen이라고 하는데, 뭐 그냥 "함수도 변수처럼 쓸 수 있다"라고만 알고 있어도 큰 문제는 없어요.

## Function Reference

- 다음처럼 변수가 함수를 가리키도록 할 수 있습니다.

```kotlin
fun main() {
    fun add(a:Int, b:Int):Int {
        return a + b;
    }
    // 다음과 같이 variable에 함수를 넘겨 줄 수 있습니다.
    var sum = ::add;
    // add 함수의 경우 
    // (Int, Int) -> Int 의 타입형을 가집니다.
    var Add: (Int, Int) -> Int = ::add

    // 이제 add, sum 모두 같은 함수에 대한 이름으로 사용하게 되죠.
    println(add(1, 2)) // 3
    println(sum(1, 4)) // 5
    println(Add(1, 4)) // 5
}
```

## Returning Function 

- 다음처럼 function이 function을 리턴하도록 할 수도 있습니다.

```kotlin
import java.util.Scanner;
//import java.util.Arrays

fun main() {
    fun func_return_func(func_type: String):(Int, Int) -> Int {
        if (func_type.equals("add")) {
            return {a:Int, b:Int -> a + b}
        } else if (func_type.equals("multiply")) {
            return {a:Int, b:Int -> a * b}
        } else {
            return {a:Int, b:Int -> a + b}
        }
    }

    var add_func = func_return_func("add");
    var multiply_func = func_return_func("multiply");
    println(add_func(3, 5)) // 8
    print(multiply_func(4, 6)) // 24
}
```

## Lambda Expression 

- 다음처럼 lambda expression을 정의할 수 있습니다.

```kotlin
// by lambda expression
var multiply:(Int, Int) -> Int = {a:Int, b:Int -> a * b}
println(multiply(3, 4))
```

- 다음처럼 정의할 수도 있죠.

```kotlin
fun(a: Int, b: Int): Int {
    return a * b
}
```
