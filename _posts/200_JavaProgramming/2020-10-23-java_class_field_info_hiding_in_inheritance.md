---
title: Java - Method Overridding, Field shadowing
category: java
tags: java overriding inheritance programming MethodOverridding
---

## Java - Method Overridding

- **Method Overridding**은 "기본 클래스(base class)에서 기정의된 method를, base class를 상속받는 derive class에서 새롭게 정의하여, 덮어씌워버리는 것"을 말합니다.
  - **Method Overloadring**은 "메소드 이름은 같지만, 메소드에서 필요로 하는 parameter 종류 혹은 개수가 다른 것"을 말합니다.
- Method Overridding은 같은 이름을 가진 서로 다른 객체들에 대해서 동일한 방식으로 호출될 수 있고, 객체의 class에 따라서 해당 객체의 클래스에 속하는 method가 호출되도록 해줍니다. 즉, 다형성을 지원하는 기능이죠.
- 설명이 어려웠는지 모르겠지만, 코드로 보면 다음과 같습니다.
  - `class A`도 `printName`라는 method를 가지고 있고, `class B`도 `printName`을 가지고 있습니다.
  - 따라서, A 객체에서 `printName` 메소드를 실행하면, A객체에 연결된 메소드가 실행되고, B 객체에서 `printName` 메소드를 실행하면, B객체에서 연결된 메소드가 실행됩니다.
  - 만약, base class의 method를 사용하려면, derived class 내에서 `super`를 사용하면 되죠.

```java
public class A {
    public void printName() {
        System.out.printf("This is Base Class\n");
    }
}

class B extends A {
    public void printName() {
        System.out.printf("This is Derived Class\n");
    }
}
```

## Java - field name shadowing

- 이전에는 method에 관한 내용이었습니다. 다만, field에서도 비슷하게 적용됩니다.
- 아래 코드를 보시면 `class A`는 `name`이라는 변수(field)를 가지고 있고, `class B` 또한 `name`라는 변수를 가지고 있습니다. 그리고 `class B`는 `class A`를 상속받은 클래스죠. 
- 그렇다면, "동시에 `name`이 두 개 존재하는 걸까요?" 아니면, "derive class의 `name`이 base class의 `name`을 덮어 씌우는 걸까요?".
- 답은, 동시에 존재하는 겁니다. base class의 `name`은 derived class에서 `super.`를 통해 접근할 수 있고, 그냥 `this.`를 통해 접근하는 아이들은 derived class의 `name`이죠.

```java
public class A {
    // base class A 가 가진 name, 
    public String name;
    public A() {
        this.name = "baseName";
    }
    public void printName() {
        System.out.printf("@name: %s \n", this.name);
    }
}

class B extends A {
    // derived class B 가 가진 name, 
    // B.name이 생긴다고 해서, A.name이 사라지는 것이 아님.
    public String name;
    public B() {
        this.name = "extendedName";;
    }
    public void printName() {
        System.out.printf("super @name: %s, extends @name: % \n", super.name, this.name);
    }
}
```

- 다음과 같이 간단한 코드를 실행하면, base class의 `name`과 derived class의 `name`에 모두 접근할 수 있는 것을 알 수 있습니다.

```java
B b1 = new B();
b1.printName(); // super @name: baseName, extends @name: extendedName 
```

## Wrap-up

- 물론, 이런 접근 방식이 가능하지만, 굳이 이렇게 해야 할 필요성은 없습니다. 굳이 base class와 derived class에 같은 이름의 변수를 넣어서 class를 설계하는 것이 필요할 때가 언제인지 잘 모르겠네요. 

## Reference

- [stackoverflow - having 2 variables with the same name in a class that extends another class in java](https://stackoverflow.com/questions/772663/having-2-variables-with-the-same-name-in-a-class-that-extends-another-class-in-j)
