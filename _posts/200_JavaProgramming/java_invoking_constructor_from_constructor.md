---
title: Java - Invoking base constructor from derived class
category: java
tags: java programming constructor inheritance
---

## Java - Invoking base constructor from derived class

- Base Class와 Derived Class가 있을 때 내부에서 constructor를 구성하는 방법은 다음과 같은 두 가지가 있습니다.
- 첫번째로는 다음처럼 `super()`를 통해 BaseClass의 Constructor를 직접 호출하는 방법이 있구요.
- 단, 이 때 `super()`는 첫번째 statement가 되어야 합니다. 그렇지 않을 경우 `Call to 'super()' must be first statement in constructor body` 에러가 발생하죠.

```java
class BaseClass {
    int id;
    BaseClass () {
        this.id = 0;
        System.out.printf("Base class is created\n");
    }
}

class DerivedClass extends BaseClass {
    String name;
    DerivedClass () {
        super(); // DerivedClass에서 BaseClass의 Constructor를 Call
        this.name = "Unknown";
        System.out.printf("DerivedClass is created\n");
    }
}
```

- 두번째로는 `BaseClass()`에서 정의된 것을 `DerivedClass()`에서도 동일하게 처리해주는 방식이 있죠.

```java
class BaseClass {
    int id;
    BaseClass () {
        this.id = 0;
        System.out.printf("Base class is created\n");
    }
}

class DerivedClass extends BaseClass {
    String name;
    DerivedClass () {
        // super(); // DerivedClass에서 BaseClass의 Constructor를 Call
        this.id = 0;
        this.name = "Unknown";
        System.out.printf("DerivedClass is created\n");
    }
}
```

- 두 방식이 코드적으로는 다르지만, 실행 결과는 다음과 같이, 동일합니다.

```plaintext
Base class is created
========================
Base class is created
DerivedClass is created
```

## 정말 똑같은가? 

- 두 가지 방식은 정말 똑같을까요? 

- 


## Reference

- [stackoverflow - how do I call one constructor from another in java](https://stackoverflow.com/questions/285177/how-do-i-call-one-constructor-from-another-in-java)
- [stackoverflow - invoking constructor in java](https://stackoverflow.com/questions/13805191/invoking-constructor-in-java)
- [stackoverflow - java is invoking super constructor in derived constructor name with set field](https://stackoverflow.com/questions/64511235/java-is-invoking-super-constructor-in-derived-constructor-same-with-set-field)
