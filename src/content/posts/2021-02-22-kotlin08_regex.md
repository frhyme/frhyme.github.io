---
title: "Kotlin - Regex"
date: 2021-02-22
category: "kotlin"
tags: ["kotlin", "programming", "regex"]
permalink: "/kotlin/kotlin08_regex/"
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