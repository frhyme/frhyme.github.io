---
title: Kotlin - Regex
category: kotlin
tags: kotlin programming regex
---

## Kotlin - Regex

- kotlin으로 regex를 다음처럼 사용할 수 있습니다.

```kotlin
fun main() {
    var s1: String = "abc";
    var regex1 = s1.toRegex();
    var regex2 = Regex("abc")

    println("abc".matches(regex1)) // true
    println(regex1.matches("abc")) // true
    println("== Complete")
}
```