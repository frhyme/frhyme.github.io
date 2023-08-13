---
title: Java - Functional Stream - map, flatMap 
category: java
tags: java programming stream FunctionalProgramming map flatMap
---

## Java - Functional Stream - map

- `.map`은 list의 요소들을 각각 정의된 function대로 변경해주는 것을 말합니다.
- 가령 `[1, 2, 3]`이라는 리스트가 있을 때 얘를 모두 square로 변경하고 싶다면 다음처럼 하면 되죠.

```java
List<Integer> dbLst = List.of(1, 2, 3)
        .stream()
        .map( (Integer x) -> x * x)
        .collect(Collectors.toList());
System.out.println(dbLst); // [1, 4, 9]
```

## Java - Functional Stream - flatMap

- `flatMap`은 List 안에 또 List가 있는 경우 원소를 끄집어 내서 합쳐줄수 있도록 해줍니다.
- 가령 `[[1, 2], [3, 4]]`인 경우 `[1, 2, 3, 4]`로 변경해주도록 하는 것이죠.

```java
import java.util.List;
import java.util.stream.Collectors;

class Main {
    public static void printAll(List inputLst) {
        System.out.println("=====");
        inputLst.stream().forEach((x) -> System.out.printf("%d ", x));
        System.out.println();
        System.out.println("=====");
    }
    public static void main(String[] args) throws Exception {
        // list_2d: 2차원 List
        List<List<Integer>> list_2d = List.of(List.of(1, 2), List.of(3, 4));
        // list_3d: 3차원 List
        List<List<List<Integer>>> list_3d = List.of(
                List.of(List.of(1, 2), List.of(3, 4)), List.of(List.of(5, 6))
        );

        // list_2d Flatten
        List<Integer> lst1 = list_2d
                .stream()
                .flatMap((lst) -> lst.stream())
                .collect(Collectors.toList());
        printAll(lst1); // [1, 2, 3, 4]
        
        // list_3d Flatten
        List<Integer> lst2 = list_3d
                .stream()
                .flatMap( (lst) -> lst.stream() )
                .flatMap( (lst) -> lst.stream() )
                .collect(Collectors.toList());
        printAll(lst2); // [1, 2, 3, 4, 5, 6]
    }
}
```
