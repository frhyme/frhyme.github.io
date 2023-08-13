---
title: Java - Object Interning
category: java
tags: java Object Class programming
---

## Java - Object Interning

- Object Interning은 여러 개의 Object가 동일한 값을 가질 때, 하나의 메모리의 값을 공유하도록 함으로써, 메모리를 적게 사용하도록 하는 기법을 말합니다.
- 아래, 코드를 보면 서로 다른 두 객체인 `aStr`와 `bStr`이 같은 메모리 값을 가지고 있음을 알 수 있죠.

```java
String aStr = "ABC";
String bStr = "ABC";

// Reference Variable 간에 ==의 경우는 memory address를 비교하게 됩니다.
// 즉, 결과가 true가 나왔다는 것은 두 Reference Variable이 가리키는 메모리주소가 같다는 것을 의미하죠.
System.out.println(aStr == bStr); // true
System.out.println(aStr.equals(bStr)); // true
```

- 다만, 아래처럼 새로운 Object를 생성해서 비교하는 경우에는 Object Interning이 되지 않습니다.

```java
String aStr = new String("ABC");
String bStr = new String("ABC");

// 이 경우 new Operator가 새로운 메모리를 확보하고 그곳에 값을 대입해주기 때문애,
// 서로 다른 객체를 가리키게 됨.
System.out.println(aStr == bStr); // false
System.out.println(aStr.equals(bStr)); // true
```

- 그리고, Double에 대해서는 Object Interning이 되지 않습니다.

```java
Double aDouble = 2.5;
Double bDouble = 2.5;

System.out.println(aDouble == bDouble); // false
System.out.println(aDouble.equals(bDouble)); // true
```

- 그리고 `Integer`의 경우는 기본적으로 -128부터 127까지의 값에 대해서만 Object Interning이 됩니다. 
- 아래 코드를 보시면 127은 되고, 128은 안되는 것을 알 수 있죠.

```java
Integer a = 128;
Integer b = 128;
Integer c = 127;
Integer d = 127;

System.out.println(a == b); // false
System.out.println(c == d); // true
```

## Wrap-up

- 결론은 그냥 객체에 대해서는 절대로 `==` operator를 사용하지 않는 것이죠. 알아서 Object Interning을 해주겠지 라는 안일한 생각으로 값을 비교하다가는 오류가 발생할 수 있습니다. 호호호.
