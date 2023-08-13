---
title: Java - Check class A is subClass of class B
category: java
tags: java programming class OOP TypeChecking
---

## Java - Check class A is subClass of class B

- java에서 class instance a가 class B의 instance인지 확인하려면 보통 `instanceof`를 사용합니다.
- `instanceof`의 경우 runtime 시에 발생하는 type checking이며, 아래와 같이, 사용할 수 있습니다.

```java 
Object x = Integer.valueOf(1);

System.out.println(x instanceof Number);  // true
System.out.println(x instanceof Integer);  // true 
System.out.println(x instanceof String);  // false
```

- 그러나, `instanceof`의 경우 앞서 말한 것과 같이, runtime시에 수행되는 typechecking입니다. 다시 말해, compile 시에 이미 type이 정해져 있는 경우에는 `false`를 출력하지 못하고 오류를 발생하게 됩니다.
- 아래를 보면, `x`는 이미 Integer로 type이 고정되어 있습니다. 이 때, `x instanceof String`를 수행하려고 하면, 오류가 발생하게 되죠.

```java
Integer x = 10;
System.out.println(x instanceof Number);  // true
System.out.println(x instanceof Integer);  // true  
// 다만, "x instanceof String"의 경우 
// java: incompatible types: java.lang.Integer cannot be converted to java.lang.String
System.out.println(x instanceof String);
```

## Class_A.isAssignableFrom(Class_B)

- 따라서, 저는 그냥 `Class_A.isAssignableFrom(Class_B)`를 사용해서 하위 클래스인지 확인합니다.
- static type의 경우에도 문제없이 결과를 출력해주고,

```java
Integer x1 = 4;
// Integer is Assignable from Number?
System.out.println(
        x1.getClass().isAssignableFrom(Number.class)
); // false
// Number is Assignable from Integer?
System.out.println(
        Number.class.isAssignableFrom(x1.getClass())
); // true
// Double is Assignable from Integer?
System.out.println(
        Double.class.isAssignableFrom(x1.getClass())
); // false
```

- runtime type binding에서도 문제없이 결과를 출력해주죠.

```java
Object x2 = Integer.valueOf(10);
// Integer is Assignable from Number?
System.out.println(
        x2.getClass().isAssignableFrom(Number.class)
); // false
// Number is Assignable from Integer?
System.out.println(
        Number.class.isAssignableFrom(x2.getClass())
); // true
// Double is Assignable from Integer?
System.out.println(
        Double.class.isAssignableFrom(x2.getClass())
); // false
```
