---
title: Java - stream - Collectors.groupingBy
category: java
tags: java programming stream Collectors groupingBy
---

## Java - stream - Collectors.groupingBy

- `Collectors.groupingBy(function)`은 stream의 각 요소에 `function`을 적용하고 적용 결과를 key에 원소를 value에 넣어서 Map으로 리턴하는 방법을 말합니다.

```java
import java.util.*;
import java.util.function.Function;
import java.util.function.Predicate;
import java.util.stream.*;

class Main {
    public static void main(String[] args) throws Exception {
        // Collectors.groupingBy(function)
        // function의 결과를 key에 넣고, 대응되는 원소를 value에 list로 모아서 넣습니다.
        List<Integer> integerLst = List.of(1, 2, 3, 4, 5, 6, 7, 8, 9);

        Function<Integer, Integer> moduloByFive = (Integer x) -> x % 3;

        Map<Integer, List<Integer>> remainderToInteger;
        remainderToInteger = integerLst.stream()
                .collect(Collectors.groupingBy(moduloByFive));

        for ( Integer key : remainderToInteger.keySet() ) {
            System.out.printf("== key: %s\n", key);
            System.out.println(remainderToInteger.get(key));
        }
        /*
        == key: 0
        [3, 6, 9]
        == key: 1
        [1, 4, 7]
        == key: 2
        [2, 5, 8]
        */
    }
}
```

- 또한 모아진 애들별로 operation을 추가로 적용할 수도 있습니다.

```java
import java.util.*;
import java.util.stream.*;

class Main {
    public static void main(String[] args) throws Exception {
        // Collectors.groupingBy(function)
        // function의 결과를 key에 넣고, 대응되는 원소를 value에 list로 모아서 넣습니다.
        List<Integer> integerLst = List.of(1, 2, 3, 3, 3, 3);

        integerLst.stream()
                .collect(
                        Collectors.groupingBy(
                                // 첫번째 argument에는 key function을 넣고
                                (Integer x) -> x % 3,
                                // 첫번째 argument에는 value accumulator를 넣어줍니다.
                                Collectors.reducing(0, (x, y) -> x + y)
                        )
                ).entrySet().stream()
                .forEach(
                        (Map.Entry e) ->  {
                            System.out.printf("key: %d, value: %d \n", e.getKey(), e.getValue());
                        }
                );
                /*
                key: 0, value: 12
                key: 1, value: 1
                key: 2, value: 2
                * */
        integerLst.stream()
                .collect(
                        Collectors.groupingBy(
                                // 첫번째 argument에는 key function을 넣고
                                (Integer x) -> x % 3,
                                // 첫번째 argument에는 value accumulator를 넣어줍니다.
                                Collectors.counting()
                        )
                ).entrySet().stream()
                .forEach(
                        (Map.Entry e) ->  {
                            System.out.printf("key: %d, value: %d \n", e.getKey(), e.getValue());
                        }
                );
                /*
                key: 0, value: 4
                key: 1, value: 1
                key: 2, value: 1
                * */
    }
}
```
