---
title: Java - Covariant Return Type
category: java
tags: java programming class OOP TypeChecking
---

## Java - Covariant Return Type

- Covariant Return Type은 "함께 변하는 Return Type"이라고 해석할 수 있습니다.
- 기존의 java에서는 subClass에서 Method Overriding이 발생할 때, superClass에서의 Method와 Return type은 같아야 했습니다.

```java
class A {
    // A에서 Integer를 리턴하므로
    public Integer get() {};
}
class B extends A {
    // B에서 method를 Override하더라도
    // Integer를 리턴해야 합니다.
    @Override
    public Integer get() {};
}
```

- 그러나, java 1.5부터는 이 부분이 유연해졌는데요.
- A의 method에서 `superType`을 리턴한다면, B에서 Override하는 method에서는 `subType`을 리턴해도 된다는 이야기입니다. 
- 만약, A에서 `Number`를 리턴한다면, B에서는 `Integer`를 리턴하도록 해도 된다는 이야기죠.

```java
class A {
    // A에서 Integer를 리턴하므로
    public superType get() {};
}
class B extends A {
    // B에서 method를 Override하더라도
    // Integer를 리턴해야 합니다.
    @Override
    public subType get() {};
}
```
