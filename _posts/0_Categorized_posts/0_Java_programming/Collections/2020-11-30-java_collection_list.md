---
title: Java - Collection - List Interface
category: java
tags: java programming interface collection list
---

## Java - Collection - List Interface

- List Interface 밑에는 `ArrayList`와 `LinkedList`가 있습니다. 이 둘에 대한 설명은 굳이 하지 않겠습니다. 이 둘은 기본적으로 mutable입니다.
- 그리고 `List.of()`를 사용해서 List를 생성하는 경우 immutableList가 생성됩니다.

```java
class Main {
    public static void main(String[] args) throws Exception {
        /*
        * 상위 Interface인 List 변수를 사용해서
        * 하위 Class인 ArrayList, LinkedList를 가리킵니다.*/
        // class java.util.ArrayList
        List<Integer> integerArrLst = new ArrayList<>();
        // class java.util.LinkedList
        List<Integer> integerLinLst = new LinkedList<>();

        integerArrLst.add(1);
        integerArrLst.add(2);
        integerArrLst.add(3);

        integerLinLst.add(1);
        integerLinLst.add(2);
        integerLinLst.add(3);

        // 서로 다른 type이지만 아래 operation이 문제없이 진행됩니다.
        // 이는 두 type의 method들이 동일하기 때문이죠.
        System.out.println(integerArrLst.equals(integerLinLst)); // true

        ////////////////////////////////////////////////////////
        // class java.util.ImmutableCollections$ListN
        // 아래처럼 선언해서 사용하는 경우 ImmutableList가 생깁니다.
        List<Integer> immutableLst = List.of(4, 5, 6);
        // 따라서, 내부 원소를 변경하려고 하면 다음 오류가 발생하죠.
        // java.lang.UnsupportedOperationException
        // immutableLst.set(0, 1);
    }
}
```
