---
title: Java - Runtime Type Checking
category: java
tags: java programming class OOP 
---

## Java - Runtime Type Checking

- Java를 포함한 OOP 언어들에서는 BaseClass(혹은 Interface)의 reference Variable을 사용해서 DerivedClass의 Class Instance를 가리키게 할 수 있습니다. 대략 다음과 같죠.

```java
class BaseClass {
}
class DerivedClass extends BaseClass {
}

// BaseClass 변수인 obj가 DerivedClass Instance를 가리킵니다.
BaseClass obj = new DerivedClass();
```

- "왜 이런짓을 해야 하지?"라는 생각이 들 수 있으나. 이를 통해 코드 자체를 매우 유연하게 개발할 수 있습니다.
- 이런 짓을 Dynamic Typing 혹은 Runtime Type Binding이라고도 하죠. 
- 지금 해당 Variable에 묶여 있는 Object가 무엇인지 알기 위해서는 `instanceof`를 사용할 수 있죠. 그 외에도 몇 가지 방법이 더 있는데 아래 코드에 정리하였습니다.

```java
class Main {
    public static void main(String[] args) throws Exception {
        /*
        * stringObj는 Object Reference Variable이죠.
        * Java에서는 BaseClass의 Reference Variable을 사용하여,
        * Derived Class Instance를 가리키도록 할 수 있습니다.
        * 즉, 아래에서는 Java의 모든 Class의 BaseClass인 Object Reference Variable을 사용하여
        * String을 가리키도록 한 것이죠. */
        Object stringObj = String.valueOf("11");

        // Instanceof ---------------------------------------------
        // instanceof를 사용하여 Is-A Relationship을 확인할 수 있씁니다.
        // DerivedClass is BaseClass는 true이지만
        // BaseClass isn't DerivedClass 이죠.
        System.out.println(stringObj /*Is-A*/ instanceof String); // true
        System.out.println(stringObj /*Is-A*/ instanceof Object); // true
        System.out.println(stringObj /*Is-A*/ instanceof Integer); // true

        // getClass() ---------------------------------------------
        // Class Instance의 getClass() method를 사용해서 비교하는 것도 가능하죠.
        System.out.println(stringObj.getClass()); // class java.lang.String
        System.out.println(String.class); // class java.lang.String
        System.out.println(stringObj.getClass() == String.class);

        // isInstance() ---------------------------------------------
        // class의 method인 isInstance()를 사용해서 체크하는 것도 가능하죠.
        System.out.println(String.class.isInstance(stringObj));// true
        System.out.println(Object.class.isInstance(stringObj));// true
    }
}
```

## Wrap-up

- 다만, 내가 사용하려는 methodName이 Reference Variable에 이미 선언되어 있지 않으면 사용할 수 없습니다. 그런 경우에는 다음과 같이 typeConversion을 해줘야 사용할 수 있죠.

```java
BaseClass obj = new DerivedClass();
// Type Converstion
DerivedClass obj1 = (DerivedClass) DerivedClass;
```
