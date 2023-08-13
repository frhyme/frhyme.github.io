---
title: Java - Array to Stream 
category: java
tags: java programming stream Array
---

## Java - Array to Stream

- Array를 Stream으로 변경하려면, `Array.Stream`을 사용하면 됩니다.
- 가령 Scanner를 사용해서 입력받은 String을 split하여 바로 Stream으로 처리하려면 다음처럼 하면 되죠.

```java
import java.util.*;
import java.util.stream.Stream;

class Main {
    public static void main(String[] args) throws Exception {
        // Input: 1, 2, 3, 4, 5, 6
        Scanner scanner = new Scanner(System.in);

        // String[]을 Array.stream으로 처리해주면 Stream<String>이 됩니다.
        Stream<String> stream_from_scanner = Arrays.stream(scanner.nextLine().split(", "));

        stream_from_scanner.map( x -> Integer.parseInt(x) )
                .filter( x -> x % 2 == 0)
                .forEach(x -> System.out.printf("%d ", x));
                // 2 4 6  
    }
}
```
