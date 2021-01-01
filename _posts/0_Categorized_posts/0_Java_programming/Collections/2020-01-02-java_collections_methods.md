---
title: Java - collections
category: java
tags: java programming collectiond 
---

## Java - collections

- java에서 `Collections`는 유용한 method들이 모여 있는 library로 이해하시면 됩니다. `Collection`과는 다릅니다. `Collection`은 Interface를 말합니다.

```java
import java.io.*;
import java.util.*;
import java.util.stream.*;
import java.util.Collections;
import java.util.HashSet;

class Main {

    public static void main(String[] args) throws Exception {
        // Collections의 method를 사용해서,
        // empty List, Set를 만들 수도 있구요.
        List<String> emptyList = Collections.emptyList();
        Set<String> emptySet = Collections.emptySet();

        // Collections.unmodifiableList
        // 값을 바꿀 수 없는 list
        List<String> lst1 = new ArrayList<>();
        lst1.add("1"); lst1.add("2");
        List<String> immutableLst = Collections.unmodifiableList(lst1);
        try {
            // immutableLst 는
            immutableLst.add("d");
        } catch (Exception e) {
            // java.lang.UnsupportedOperationException
            System.out.println(e);
        }
        List<Integer> lstOfInteger = new ArrayList();
        lstOfInteger.addAll(List.of(1, 2, 5, 4, 3));

        // Collections.sort(lst): 정렬
        Collections.sort(lstOfInteger); // 1 2 3 4 5
        // Collections.reverse(lst): 역순으로
        Collections.reverse(lstOfInteger); // 5 4 3 2 1
        // Collections.swap(lst, i, j): i, j의 원소를 변경
        Collections.swap(lstOfInteger, 0, 1); // 4 5 3 2 1
        // Collections.shuffle(lst): 섞기
        Collections.shuffle(lstOfInteger); // 4 5 1 2 3
        // Collections.rotate(lst, distance): 회전
        Collections.rotate(lstOfInteger, 1); // 3 4 5 1 2

        List<Integer> lstOfInteger1 = new ArrayList();
        lstOfInteger1.addAll(List.of(1, 2, 2, 3, 4, 1, 1, 1));
        // Collections.frequency: 원소의 빈도
        System.out.println(Collections.frequency(lstOfInteger1, 1)); // 4
        // Collections.min: 가장 작은 값
        System.out.println(Collections.min(lstOfInteger1)); // 1
        // Collections.max: 가장 큰 값
        System.out.println(Collections.max(lstOfInteger1)); // 4
        // Collections.disjoint: 공통인 원소가 없으면 true, 있으면 false
        Set<Integer> setOfInteger1 = new HashSet(Set.of(1, 2, 3));
        Set<Integer> setOfInteger2 = new HashSet(Set.of(4, 5, 6));
        Set<Integer> setOfInteger3 = new HashSet(Set.of(1, 2));
        System.out.println(Collections.disjoint(setOfInteger1, setOfInteger3)); // false
        System.out.println(Collections.disjoint(setOfInteger2, setOfInteger3)); // true


        List<Integer> lst11 = List.of(0, 1, 2, 3, 1, 2);
        List<Integer> lst12 = List.of(1, 2);
        // Collections.indexOfSubList(lst, subLst):
        // Lst 내에 subLst가 존재하는 첫번째 index를 찾아서 리턴
        Collections.indexOfSubList(lst11, lst12); // 1
        // Collections.lastIndexOfSubList(lst, subLst):
        // Lst 내에 subLst가 존재하는 마지막 index를 찾아서 리턴
        Collections.lastIndexOfSubList(lst11, lst12); // 4

    }
}
```
