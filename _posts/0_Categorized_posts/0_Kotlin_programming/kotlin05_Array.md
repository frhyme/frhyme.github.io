---
title: Kotlin - Array
category: kotlin
tags: kotlin programming array
---

## Kotlin - Array

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
