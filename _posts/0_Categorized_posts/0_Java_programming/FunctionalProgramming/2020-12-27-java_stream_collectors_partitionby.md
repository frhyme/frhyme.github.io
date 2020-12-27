---
title: Java - stream - Collectors.partitioningBy
category: java
tags: java programming stream Collectors partitioningBy
---

## Java - stream - Collectors.partitioningBy

- `stream`을 `collect`할 때, `Collectors.partitioningBy(Predicate)`를 사용하여 모으면 Predicate의 결과인 `true`, `false`를 key로, 그리고 원소는 각 value에 들어가는 Map이 생성됩니다.

```java
import java.util.*;
import java.util.function.Predicate;
import java.util.stream.*;

class Main {
    public static void main(String[] args) throws Exception {
        // Collectors.partitioningBy( Predicate )
        // Collectors.partitioningBy( Predicate)는 각 요소의 Predicate에 따라서
        // true, false로 나누어 줍니다.
        // true, false를 key로 가지고 value에 해당되는 원소들이 다 들어가 있죠.
        List<Integer> integerLst = List.of(1, 2, 3, 4, 5, 6, 7, 8, 9);
        // 적용할 Predicate
        Predicate<Integer> isDiviedByTwo = (Integer x) -> x % 2 == 0;
        // 결과는 Map<Boolean, List<Integer>>의 형태로 저장되죠.
        Map<Boolean, List<Integer>> boolIntegerMap = integerLst.stream().collect(
                Collectors.partitioningBy( isDiviedByTwo )
        );
        for (boolean k : boolIntegerMap.keySet()) {
            System.out.printf("==== Key: %b\n", k);
            System.out.println(boolIntegerMap.get(k));
        }
        /*
        ==== Key: false
        [1, 3, 5, 7, 9]
        ==== Key: true
        [2, 4, 6, 8]
        */
    }
}
```
