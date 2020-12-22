---
title: Java - Stream - limit, skip, takeWhile, dropWhile
category: java
tags: java programming primitive stream 
---

## Java - Stream - limit, skip, takeWhile, dropWhile

- `limit`, `skip`, `takeWhile`, `dropWhile`의 사용법을 정리하였습니다.

```java
import java.util.List;
import java.util.stream.*;

class Main {
    public static void main(String[] args) throws Exception {
        long xx = LongStream.rangeClosed(0, 0).filter( (long x) -> x % 2 != 0).sum();
        System.out.println(xx);

        List<Integer> integerLst = List.of(1, 2, 3, 4, 0, 5, 6, 7);
        // .limit(n): 처음부터 n까지의 원소만
        integerLst.stream()
                .limit(4).forEach(x -> System.out.printf("%d ", x));
        // 1 2 3 4
        System.out.println("----------------------------------------");
        // .skip(n): 처음부터 n개의 원소만 빼고
        integerLst.stream()
                .skip(5).forEach(x -> System.out.printf("%d ", x));
        // 5 6 7
        System.out.println("----------------------------------------");

        // .takeWhile(Predicate): Predicate(x)가 False이면 Stop.
        // 1 2 3 4
        integerLst.stream()
                .takeWhile( x -> x != 0).forEach(x -> System.out.printf("%d ", x));
        System.out.println("----------------------------------------");

        List<Integer> integerLst1 = List.of(0, 0, 0, 1, 2, 3);
        // .dropWhile(Predicate): Predicate(x)가 False 가 나오면 읽기 시작
        // 1 2 3
        integerLst1.stream()
                .dropWhile( x -> x == 0).forEach(x -> System.out.printf("%d ", x));
        System.out.println("----------------------------------------");
    }
}
```
