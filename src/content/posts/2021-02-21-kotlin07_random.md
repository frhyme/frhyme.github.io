---
title: "Kotlin - Random"
date: 2021-02-21
category: "java"
tags: ["kotlin", "programming", "random"]
permalink: "/kotlin/kotlin07_random/"
---

- `kotlin.random.Random`을 통해 random을 사용할 수 있습니다.

```kotlin
import kotlin.random.Random;

fun main() {
    println(Random.nextDouble())
    // 0.8495425362538855

    println(Random.nextInt(0, 5))
    // 2
    
    // Random with Seed
    var randomGeneratorSeed0 = Random(0)
    println(randomGeneratorSeed0.nextInt())
    // -1934310868

    randomGeneratorSeed0 = Random(0)
    println(randomGeneratorSeed0.nextInt())
    // -1934310868

}
```