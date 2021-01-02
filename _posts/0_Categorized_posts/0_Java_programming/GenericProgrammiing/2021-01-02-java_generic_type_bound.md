---
title: Java - Generic Programming - Type Bound
category: java
tags: java programming GenericProgramming TypeBound
---

## Java - Generic Programming - Type Bound

- Type Bound는 Generic Programming을 사용할 때, "특정 타입을 상속받는 객체"만 허용되도록 제한하는 것을 말합니다.
- 다음 코드에서 `<TS extends List>`는 type parameter인 TS가 "List를 상속받는다"라는 것을 의미하죠. List는 interface이므로 `implements`가 되어야 하는 것 아닐까? 싶지만, interface, class와 무관하게 항상 `extends`를 사용합니다.

```java
public static <TS extends List> void printList(TS ts) {
    // <TS extends List>는 TS가 List를 상속하는 Object라는 것을 말합니다.
    // 만약 List를 상속하지 않는 경우에는 이 method가 실행될 수 없는 것이죠.
    for (int i=0; i < ts.size(); i++) {
        System.out.println(ts.get(i));
    }
}
```

- 실제로 main code에서 다음과 같이 작성하고 실행해보면, List를 상속받는 `ArrayList`, `LinkedList`의 경우는 문제가 없습니다.
- 하지만 `HashSet`의 경우는 List를 상속(혹은 구현)하지 않기 때문에, `printList` method를 구현하려고 하면 에러가 발생하죠.

```java

import java.io.*;
import java.util.*;
import java.util.Collections;
import java.util.HashSet;

class Main {
    public static <TS extends List> void printList(TS ts) {
        // <TS extends List>는 TS가 List를 상속하는 Object라는 것을 말합니다.
        // 만약 List를 상속하지 않는 경우에는 이 method가 실행될 수 없는 것이죠.
        for (int i=0; i < ts.size(); i++) {
            System.out.println(ts.get(i));
        }
    }
    public static void main(String[] args) throws Exception {
        List<Integer> arrListOfInteger = new ArrayList<>(List.of(1, 2, 3, 4));
        List<String> linkedListOfString = new LinkedList<>(List.of("a", "b"));
        printList(arrListOfInteger);
        // 1 2 3
        System.out.println("-------------");
        printList(linkedListOfString);
        // a b

        // setOfInteger는 List를 상속받는(혹은 구현하는) 객체가 아닙니다.
        // 따라서 실행하게 되면 오류가 발생하죠.
        Set<Integer> setOfInteger = new HashSet<>(List.of(1, 2, 3));
        printList(setOfInteger);
        /*
        java: method printList in class com.company.Main cannot be applied to given types;
          required: TS
          found:    java.util.Set<java.lang.Integer>
          reason: inference variable TS has incompatible bounds
            lower bounds: java.util.List
            lower bounds: java.util.Set<java.lang.Integer>
        */
    }
}

```

## Multiple Type Bound

- 만약, "Type Parameter가 여러 interface와 class로 구성되어 있어야 한다"를 강제하고 싶다면 다음처럼 하면 됩니다.
- 다만, class가 존재한다면 가장 먼저 나와야 하죠.

```java
// 만약 A, B, C 중 class가 존재한다면 A가 class여야 함.
public static <TS extends A & B & C> void printList(TS ts) {
}
```
