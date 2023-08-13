---
title: Java - StringBuilder 사용하기
category: java
tags: java programming immutability mutability string
---

## Java - Mutable한 String 사용하기

- Java에서 String은 Immutable합니다(물론 python에서도 String은 Immutable하죠).
- Immutable하다는 것은 한 번 값이 assignment되고 나면, 값이 바뀔 수 없다는 것을 의미합니다.

### Immutable하면 뭐가 좋은가?

- 우선, 값이 Immutable하게 관리되면 Thread-safe가 보장됩니다. 중간에 값이 바뀔 수 없기 때문에 "서로 다른 Thread에서 독립적으로 수행이 되어도 문제가 없다"는 것이 보장되죠. 이게 가능하면, 병렬 프로그래밍으로 처리하는 것이 매우 손쉬워집니다.

### Mutable String은 언제 좋은가?

- 가령, String 여러 개를 하나로 연결한다고 해보겠습니다. 대략 다음 코드에서처럼, `"A"`, `"B"`, `"C"`를 연결해볼게요.
- 이 때, String이 Immutable하기 때문에, 원래 있던 메모리에 연결해서 새로운 스트링을 넣어주는 것이 아니라, 원래 있던 것을 그대로 두고 새로운 장소에 "AB"를 만들어서 집어넣고, 다시 "ABC"를 만들어서 새로운 메모리에 넣고 가 반복됩니다.
- 기존의 메모리 장소가 비워지지 않고 있으므로 나중에 Garbage Collector가 부지런하게 처리해야 함은 물론, 연산 속도 자체도 매우 오래 걸리게 되죠.
- 아래에서 보는 것처럼 매번 `str1`의 메모리 주소 값이 계속 바뀌게 됩니다.

```java
String str1 = "A";
System.out.println(str1.hashCode()); // Memory Adress: 65
str1 += "B";
System.out.println(str1.hashCode()); // Memory Adress: 2081
str1 += "C";
System.out.println(str1.hashCode()); // Memory Adress: 64578
```

### Mutable String - StringBuilder

- Java에서 mutable한 String을 사용하기 위해서는 `StringBuilder`를 사용해야 합니다.
- `.append()`를 사용해서 서로 다른 String을 연결할 수 있으며, 이 때는 memory address가 변하지 않습니다.

```java
StringBuilder strBuilder1 = new StringBuilder("A");
System.out.println(strBuilder1.hashCode()); // 258952499
strBuilder1.append("B");
System.out.println(strBuilder1.hashCode()); // 258952499
strBuilder1.append("C");
System.out.println(strBuilder1.hashCode()); // 258952499
```

### String Builder - Methods

- 주요 몇 가지 method들을 정리하면 다음과 같습니다.
- 그 외에도 다양한 method들이 있지만, 나머지는 필요할 때 찾아보면 될 것 같아요.

```java
StringBuilder strBuilder1 = new StringBuilder("ABCDEF");
strBuilder1.length(); // 길이 확인
strBuilder1.setCharAt(0, 'Z'); // 0번째 index의 원소를 'Z'로 변경함
strBuilder1.deleteCharAt(0); // 0번째 원소를 삭제
```

## Wrap-up

- 글에도 쓴 내용이지만, Immutability가 항상 좋은 것도 아니고, 반대로 Mutablity가 항상 좋은 것도 아니죠.
- 따라서 두 특성을 모두 가진 변수가 Java에 동시에 존재하고 필요에 따라 둘 중 하나를 정의해서 사용하면 되는 것이겠죠.

## Reference

- [stackoverflow - why we need mutable classes](https://stackoverflow.com/questions/23616211/why-we-need-mutable-classes)
