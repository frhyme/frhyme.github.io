---
title: Kotlin - Basic
category: kotlin
tags: kotlin programming
---

## Kotlin에 대한 사소한 것들

- 심심해서 코틀린을 공부하고 있는데 다른 언어들과의 차이점이라거나 하는 것들을 정리합니다.

### Varaible - val, var

- `val`: immutable variable을 의미합니다.
- `var`: mutable variable

```kotlin
// 다음처럼, type을 지정할 수 있으며, 
// 타입을 지정할 경우 값을 지정하지 않고도 변수를 선언할 수 있음.
var x:Int
x = 10
```

### Char and String

- java처럼 `'a'`는 char를 의미하고 `"a"`는: string을 의미합니다.

### Every function has return value

- kotlin에서는 모든 function이 return value를 가집니다.

```kotlin
fun main() {
    var result = println("Hello, Kotlin");
    // Hello, Kotlin
    println(result);
    // kotlin.Unit
}
```

### Standard Input

- `readLine()`을 사용해서 input을 받을 수 있습니다.

```kotlin
fun main() {
    val line = readLine()!!
    println(line)
}
```

- 다음처럼 `java.util.Scanner`를 사용해서 입력받을 수도 있죠.

```kotlin
import java.util.Scanner;

fun main() {
    val scanner = Scanner(System.`in`)
    val inputStr = scanner.nextLine();
    println(inputStr)
}
```

- 아래 코드를 보면 java와 매우 유사하죠.

```kotlin
val scanner = Scanner(System.`in`)
while(scanner.hasNext()) {
    var x = scanner.nextInt()
    println(x)
}
```

### Type Conversion

- type conversion은 아래 method로 `.toString()`등의 형태로 존재합니다.

```kotlin
fun main() {
    var x:Double = 100.0;
    var y:Int = x.toInt();

    println(y)
}
```

### String Template

- kotlin에서는 string formatting을 다음처럼 합니다.

```kotlin
fun main() {
    var s = "abc"
    var x = 1
    println("s= ${s.length}, x= ${x}")
    // s= 3, x= 1
}
```

### Declare Function

- kotlin에서는 다음과 같이 function을 선언해줍니다.
- input, output parameter의 type을 모두 정의해주고 있습니다.

```kotlin
import java.util.Scanner;

fun main() {
    fun add(x:Int, y:Int):Int {
        return x + y;
    }
    println(add(1, 3))
    println(add(5, 3))
}
```

### for loop 

- fr loop는 다음과 같습니다.

```kotlin
for(i in 0..2) {
    print(x.get(i))
}
/*
0
1
2
*/
```

### Array

- array는 다음처럼 만들 수 있습니다.

```kotlin
val nums = arrayOf(1, 2, 3, 4, 5)
```

### if Statemenbt

```kotlin
var x = 10

if (x == 10) {
    // stmt
} else if (x < 10) {
    // 
} else {
    // 
}
```

### Object

- kotlin에서는 `Int`를 포함하여 모든 것이 Object입니다.

### Equality

- Structural equality는 Object의 상태가 같은지를 비교하며 `==`, `!=`를 사용합니다.
- Reference equality는 두 variable이 같은 Object를 참조하는지를 비교하며 `===`, `!==`를 사용합니다.
