---
title: Java - Iterable, Iterator, ListIterator
category: java
tags: java programming interface collection Iterable Iterator
---

## Java - Iterable

- Java에서 for-each loop 혹은 forEach method를 사용하려면, 자료 구조의 요소들을 순회(Iterate)해야 합니다. 순차적으로 원소에 접근하는 것이 가능할 경우, "for-each loop이 사용한 경우"에는 Iterable하다고 하죠.
- Java에는 이미 `Iterable` Interface가 존재합니다. 다음 그림처럼 `Iterable` Interface를 Implement하는 경우 `Iterator()`가 되고, `Collection`은 `Interface`를 Extend합니다. 그리고 `List`, `Set`, `Queue` 또한 `Collection` Interface를 Extend하기 때문에, 모두 Iterable한 성향을 가지죠.

```java
// Iterable Interface Variable @iterableIntegers 를 만듭니다.
Iterable<Integer> iterableIntegers = List.of(1, 2, 3);

// For-each loop: Iterable can be used
// Iterable이므로 for-each loop에서 순차적으로 원소에 접근할 수 있죠.
for (Integer x: iterableIntegers) {
    System.out.println(x);
}

// forEach method도 binding되죠.
iterableIntegers.forEach(System.out::println);
```

## Java - Iterator 

- `Iterator`도 순차적으로 원소를 순회한다는 점에서 `Iterable`와 동일하지만, 지금 어디까지 읽었는지 저장해둔다는 면에서 차이가 있습니다. 그리고 다음과 같은 메소드들을 가져야 하죠.
  - `boolean hasNext()`: 이 다음에 원소가 또 있는지 확인합니다. 만약 `false`라면, iterator가 자료 구조의 끝까지 다 온것이죠.
  - `T next()`: 현재 위치에서 다음 요소를 리턴합니다.
- `Iterator`는 `Iterable`한 개체의 method로부터 리턴됩니다.

```java
// ArrayList
List<Integer> integerArrLst = new ArrayList<>();
integerArrLst.add(3);
integerArrLst.add(4);
integerArrLst.add(5);

// ArrayList의 .iterator()로부터 Iterator를 리턴합니다.
Iterator<Integer> integerIterator = integerArrLst.iterator();

// .hasNext()로 원소가 더 있는지 확인하고,
// .next()로 해당 원소에 접근합니다.
while(integerIterator.hasNext()) {
    System.out.println(integerIterator.next());
}
```

## Java - ListIterator

- `ListIterator`는 다음(Next), 이전(Previous)로 순회할 수 있습니다.

```java
List<Integer> integerArrLst = new ArrayList<>();
integerArrLst.add(3);
integerArrLst.add(4);
integerArrLst.add(5);

ListIterator<Integer> integerListIterator = integerArrLst.listIterator();
// hasNext(); 현재 위치의 다음 원소에 값이 있는가
// nextIndex(): 다음 원소의 주소 값
// next(): 다음 값
while(integerListIterator.hasNext()) {
    System.out.printf("Index: %d, Value %d\n",
            integerListIterator.nextIndex(),
            integerListIterator.next()
    );
}

// hasPrevious(); 현재 위치의 이전 원소에 값이 있는가
// previousIndex(): 이전 원소의 주소 값
// previous(): 이전 값
while(integerListIterator.hasPrevious()) {
    System.out.printf("Index: %d, Value %d\n",
            integerListIterator.previousIndex(),
            integerListIterator.previous()
    );
}
```
