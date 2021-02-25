---
title: Kotlin - Array
category: kotlin
tags: kotlin programming array
---

## Kotlin - Array

- array는 다음처럼 정의할 수 있습니다.

```kotlin
var arr1 = arrayOf<String>("A", "B","C");

var arr2 = emptyArray<String>();
arrOfInt += "AA";

var arr3 = intArrayOf(1, 2, 3)
```

## Array Method - contentEquals

- `arr1.contentEquals(arr2)`를 사용하여 array의 내부 원소들이 동일한지 비교할 수 있습니다.

```kotlin
fun main() {
    val arrOfInt1 = intArrayOf(1, 2, 3, 4);
    val arrOfInt2 = intArrayOf(1, 2, 3, 4);
    val arrOfString = arrayOf("+", "*", "plus", "minus", "-", "/");

    println(arrOfInt1 == arrOfInt2) // false
    println(arrOfInt1 === arrOfInt2) // false
    println(arrOfInt1.equals(arrOfInt2)) // false
    // .contentEquals method는
    // 두 array의 내부 요소가 완전히 동일한지 비교해 줍니다.
    println(arrOfInt1.contentEquals(arrOfInt2)) // true
}
```

## Array Method - joinToString

- `.joinToString()`를 사용하면, String Array를 합쳐서 새로운 String으로 생성할 수 있습니다.

```kotlin
fun main() {
    var student1:Student = Student(studentID="1");
    var student2:Student = Student(studentID="2");
    student1.print()

    var arrOfStr = arrayOf("A", "B", "C");
    println(
        arrOfStr.joinToString("=")
    )
    // A=B=C
}
```

## Array - Count element 

- array의 element의 개수를 세기 위해서는 `.count(predicate)`를 사용하게 됩니다.

```kotlin
var arrOfInt = intArrayOf(1, 2, 3, 4, 5, 4, 3, 3);
println(
    // predicate은 true of false를 리턴하는 간단한 함수죠.
    // 내부에는 대명사로 it를 사용한다고 보면 됩니다.
    arrOfInt.count({ it==3 })
)// 3
```