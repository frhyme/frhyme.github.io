---
title: Java - Collection - Set Interface
category: java
tags: java programming interface collection set
---

## Java - Collection - Set Interface

- `Set`는 우리가 흔히 아는 '집합'을 말하는 것이죠. 이 자료 구조 내부에는 중복값이 존재할 수 없습니다. 가령 Array, List등에서는 1을 원소로 넣고, 또 넣을 수 있는 반면, Set에서는 이게 안되요. 그럼 List가 더 좋은 것 아니냐? 그렇지 않습니다. 용도가 다른데, 중복을 허용하지 않는 경우에는 `.contain` method가 List에 비해서 훨씬 빠르게 수행됩니다. 이 또한 당연한 것이, list의 경우는 중복을 허용하기 때문에, 특정한 값이 존재하는지 확인하기 위해서는 모든 원소를 다 읽어야 하는 거죠. 반면, Set는 중복을 허용하지 않으므로 hashing을 해서 처리할 수 있다는 강점이 있죠.

## Immutable Set

- 가장 간단한 `Set<T>`를 사용해서 SET를 사용해봅니다.
- 얘는 기본적으로 Immutable이며 `add()` 메소드가 정의되어 있지 않습니다. 처음에 값을 정해주고 나면 고칠 수 없고, `size()`, `contains()`, `isEmpty()` 라는 세 가지 메소드만을 사용할 수 있죠.
- 출력 결과를 보시면 출력되는 결과가 집어넣는 순서와 동일하지 않게 나오는 것을 알 수 있습니다. 

```java
import java.util.Set;

class Main {
    public static void main(String[] args) throws Exception {
        // Immutable Set
        // 한번 초기화 하고 나면 수정할 수 없습니다.
        Set<Integer> integerSet = Set.of(1, 2, 3, 4, 5);
        // 따라서, add() 메소드가 이미 정의되어 있지 않고, 
        integerSet.add(6); // UnsupportedOperationException
        // 출력 결과를 보시면 아시겠지만, 순서가 집어넣은 순서대로 되어 있지 않죠.
        System.out.println( integerSet ); // [1, 5, 4, 3, 2]
        System.out.println( integerSet.size() ); // 5
        System.out.println( integerSet.contains(3) ); // true
        System.out.println( integerSet.isEmpty() ); // false
    }
}
```

## HashSet

- `HashSet`는 Hash table을 사용하여 효율적으로 Set의 원소를 관리하죠. 
- mutable하고(`add()` 메소드를 사용할 수 있다는 거죠), hashtable을 사용해서 원소를 관리하기 때문에 `contains` 메소드를 사용할 때, 성능이 더 좋죠. 그리고 얘도 순서가 안 지켜지는 것은 마찬가지입니다.

```java
import java.util.Set;
import java.util.HashSet;

class Main {
    public static void main(String[] args) throws Exception {
        Set<String> names = new HashSet<>();

        names.add("Lee");
        names.add("Kim");
        names.add("Park");
        names.add("Hwang");
        // 얘도 순서를 안 지켜주는 것은 마찬가지죠.
        System.out.println(names); // [Hwang, Lee, Kim, Park]
        System.out.println(names.contains("Lee")); // true
    }
}
```

## TreeSet

- TreeSet의 경우는 순서를 유지해줍니다. 
- 따라서, `Set<T>` 인터페이스를 사용하지 않고, `SortedSet<T>` 인터페이스를 사용합니다. 그리고 당연히 몇 개의 method들이 추가되죠.

![java_Set_SortedSet_TreeSet](https://cdn.programiz.com/sites/tutorial2program/files/java-sortedset-implementation.png)

- `Contains`과 같은 메소드를 사용할 때는 TreeSet에 비해서 HashSet이 더 빠릅니다. TreeSet은 log-time이 소요되고, HashSet은 constant time이 소요되죠.

```java
import java.util.SortedSet;
import java.util.TreeSet;

class Main {
    public static void main(String[] args) throws Exception {
        SortedSet<Integer> sortedSet = new TreeSet<>();
        sortedSet.add(1);
        sortedSet.add(4);
        sortedSet.add(3);
        sortedSet.add(5);
        sortedSet.add(2);
        // SortedSet의 경우는 들어온 순서와 상관없이 값의 비교를 통해 순서가 정해집니다.
        // Integer의 경우는 기본적인 비교연산자가 정의되어 있어서
        System.out.println(sortedSet); // [1, 2, 3, 4, 5]
        // 비교연산자에 따른 2보다 작은 subSet
        System.out.println(sortedSet.headSet(2)); // [1]
        // 비교연산자에 따른 3보다 크거나 같은 subSet
        System.out.println(sortedSet.tailSet(3)); // [3, 4, 5]
        // 비교연산자에 따른 가장 작은 값
        System.out.println(sortedSet.first()); // 1
        // 비교연산자에 따른 가장 큰 값
        System.out.println(sortedSet.last()); // 5
        System.out.println(sortedSet.contains(3)); // true
    }
}
```

## LinkedHashSet

- `LinkedHashSet`은 set에 값이 들어온 대로 순서가 유지됩니다. 그냥 Linked List를 생각하셔도 된다는 이야기죠. 다만, 얘는 list가 아니라, Set이고, 원래 있던 값을 다시 집어넣는다고 새로 들어간 값이 제일 뒤에 오거나 하지는 않습니다.

```java
class Main {
    public static void main(String[] args) throws Exception {
        Set<String> lastNameSet = new LinkedHashSet<>();
        lastNameSet.add("Lee");
        lastNameSet.add("Kim");
        lastNameSet.add("Park");

        // LinkedHashSet는 삽입된 순서를 그대로 유지해줍니다.
        System.out.println(lastNameSet); // [Lee, Kim, Park]
    }
}
```

## Set Equallity 

- Set별로 순서가 있는 경우도 없는 경우도 있지만, Set간의 Equality를 비교할 때는 순서가 고려되지 않습니다. 어떤 Set든 원소만 동일하다면 동일한 Set로 결론을 내리게 되죠.

```java
import java.util.Set;
import java.util.HashSet;
import java.util.SortedSet;
import java.util.TreeSet;

class Main {
    public static void main(String[] args) throws Exception {
        // 네 가지 Set를 만들어봅니다.
        // 이 네 Set의 equality의 결과가 어떻게 나오는지 보려구요.
        Set<Integer> set = Set.of(1, 2, 3);
        Set<Integer> hashSet = new HashSet<>();
        Set<Integer> treeSet = new TreeSet<>();
        Set<Integer> linkedHashSet = new LinkedHashSet<>();

        // 모든 Set에 동일한 원소들을 넣어줍니다.
        for (Integer x: set) {
            hashSet.add(x);
            treeSet.add(x);
            linkedHashSet.add(x);
        }
        /*
        * set는 순서가 중요하지 않기 때문에,
        * 내부 원소가 같다면 항상 equals method는 true를 리턴합니다.*/
        System.out.println(set.equals(hashSet)); // true
        System.out.println(set.equals(treeSet)); // true
        System.out.println(set.equals(linkedHashSet)); // true
        System.out.println(hashSet.equals(treeSet)); // true
        System.out.println(hashSet.equals(linkedHashSet)); // true
        System.out.println(treeSet.equals(linkedHashSet)); // true
    }
}
```
