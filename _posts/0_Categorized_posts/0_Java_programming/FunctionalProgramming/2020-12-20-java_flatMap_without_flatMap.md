---
title: Java - Functional Stream - Without flatMap
category: java
tags: java programming stream FunctionalProgramming map flatMap
---

## Java - Functional Stream - Without flatMap

- `flatMap`은 `List<List<Integer>>`와 2차원으로 되어 있는 List를 1차원 List로 변형해줄 때 쓰입니다. 말 그대로, 평평하게 해주는 애들이죠.
- 가령 `[[1, 2], [3, 4]]`를 `[1, 2, 3, 4]`로 바꿔준다.

```java
package com.company;

import java.util.stream.Collectors;
import java.util.Comparator;

class Main {
    public static void printAll(List inputLst) {
        System.out.println("=====");
        inputLst.stream().forEach((x) -> System.out.printf("%d ", x));
        System.out.println();
        System.out.println("=====");
    }
    public static void main(String[] args) throws Exception {
        // list_2d: 2차원 List
        //List<List<Integer>> list_2d = List.of(List.of(1, 2), List.of(3, 4));
        // list_3d: 3차원 List
        List<List<List<Integer>>> list_3d = List.of(
                List.of(List.of(1, 2), List.of(3, 4)), List.of(List.of(5, 6))
        );

        // list_2d Flatten
        List<List<Integer>> list_2d = List.of(List.of(1, 2), List.of(3, 4));

        List<Integer> lst1 = list_2d
                .stream()
                .flatMap(arr -> arr.stream())
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

- 물론, `flatMap`을 쓰면 되는 건데, 이걸 안 쓰고 다른 방법으로 `flatMap`과 비슷하게 코딩할 수는 없는지 고민했고, 그 코드는 다음과 같습니다.
- `.reduce`를 사용했고, list간의 연산을 연속으로 해준 것이죠.

```java
package com.company;

import java.util.List;

class Main {
    public static void main(String[] args) throws Exception {

        List<List<Integer>> list_2d = List.of(List.of(1, 2), List.of(3, 4));

        // list_2d Flatten
        // .reduce는 원소들에 대해서 연속적인 연산을 해줍니다.
        // 가령 [1, 2, 3].reduce( (x1, x2) -> x1 + x2) 이라면 1 + 2 + 3으로 6이 됩니다.
        // reduce는 Optional을 리턴하는데, Optional을 해체하고 값을 리턴하려면
        // (의미저으로) null애 해당하는 값을 정의해주면 됩니다.
        // 즉, 다음처럼 orElse를 통해 null에 해당되는 값을 넣어주면 Optional이 해체되죠.
        List<Integer> flatLst = list_2d.stream()
                .reduce(
                (l1, l2) -> {
                    ArrayList<Integer> concat_Lst = new ArrayList<>(l1);
                    concat_Lst.addAll(l2);
                    return concat_Lst;
                })
                .orElse(List.of());
        System.out.println(flatLst);
    }
}
```

## Wrap-up

- 처음에는 python에서 처럼 List안에 `List`, `int`가 섞여 있을 때 flat하게 해주기 위해서 굳이 flatMap이 아닌 다른 방법을 찾았던 것인데, 생각해보니 그럴 필요가 없습니다. java는 type이 빠빡하게 관리되기 때문에 서로 다른 타입이 List 안에 공존할 수 없죠. 물론 하려면 할수는 있는데, 매우 지저분해지고요, 그냥 안하겠습니다 하하하.
