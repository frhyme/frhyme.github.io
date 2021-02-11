---
title: Kotlin - Range
category: kotlin
tags: kotlin range for programming
---

## Kotlin - Range

- kotlin에서 Range를 정의하는 방법은 대략 다음과 같습니다.

```kotlin
println("\n==========================")
for (i in 1..5) {
    print("${i} ")
}

println("\n==========================")
for (i in 1..5 step 2) {
    print("${i} ")
}

println("\n==========================")
for (i in 1 until 6) {
    print("${i} ")
}

println("\n==========================")
```