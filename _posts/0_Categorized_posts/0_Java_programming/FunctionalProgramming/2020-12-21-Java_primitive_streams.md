---
title: Java - Primitive Stream
category: java
tags: java programming primitive stream 
---

## Java - Primitive Stream

- 보통 `Stream<T>`는 `Integer`, `Double`, `String`과 같은 reference type등을 담습니다. 가끔 int, double 등을 사용해서 프로그램을 짜다가, `Stream<T>`으로 변경하고 싶은 경우에는 각각 Integer, Double으로 변형해서 처리해줘도 됩니다만, 아무래도 좀 비효율적이죠. 
- 따라서, Java에는 이미 `int`, `double`, `long` 3가지 primitive type에 대해서 Stream으로 처리해주는 `IntStream`, `LongStream`, `DoubleStream`이 있습니다. int를 Integer로 변형해주는 Boxing 필요없이 처리할 수 있습니다.

```java
package com.company;

import java.util.stream.IntStream;

class Main {
    public static void main(String[] args) throws Exception {

        // IntStream.range(start, end)
        // start부터 end까지의 int Stream을 만들어주지만, end는 포함하지 않습니다.
        // IntStream.range(1, 5) -> [1,2,3,4]
        IntStream intStream = IntStream.range(1, 5);
        intStream.forEach((int x) -> System.out.printf("%d ", x));
        // 1 2 3 4

        // LongStream.rangeClose(start, end)
        // start부터 end를 포함한 Stream을 만들어 줍니다.
        LongStream longStream = LongStream.rangeClosed(7, 9);
        longStream.forEach((long x) -> System.out.printf("%d ", x));
        // 7 8 9
    }
}
```
