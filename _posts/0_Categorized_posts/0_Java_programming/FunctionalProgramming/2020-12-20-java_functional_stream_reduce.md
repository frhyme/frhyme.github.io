---
title: Java - functional stream - reduce
category: java
tags: java programming optional reduce
---

## Java - reduce

- `reduce`는 list 내의 원소들에 대해서 binary 연산은 순차적으로 수행하도록 해주는 것을 말하죠.

```java

import java.util.stream.IntStream;

class Main {
    public static void main(String[] args) throws Exception {
        // 1 + 2, 2 + 3, 5 + 4 와 같은 순으로 연산이 이어지죠.
        // reduce의 경우 초기값(identity)가 없는 경우 Optional로 리턴됩니다.
        // 따라서, 여기서 값을 끄집어내고 싶다면, get, orElse를 사용하면 되죠.
        int plusSum = IntStream.range(1, 100)
                .reduce((x1, x2) -> x1 + x2).orElse(1111);
        System.out.println(plusSum); // 4950

        // 위랑 비슷하지만,
        // 이번에는 초기 값을 2로 넣어줍니다.
        // 그 다음, 2 * 3, 6 * 4 로 연산이 진행되죠.
        int factorial = IntStream.range(3, 5)
                .reduce(2, (x1, x2) -> x1 * x2 );
        System.out.println(factorial);
    }
}
```
