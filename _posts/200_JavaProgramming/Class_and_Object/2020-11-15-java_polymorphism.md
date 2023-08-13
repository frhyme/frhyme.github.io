---
title: Java - Polymorphism
category: java
tags: java OOP programming Object polymorphism overloading overridding
---

## Java - polymorphism

- polymorphism은 다음과 같은 다양한 종류로 나뉩니다.
- **Ad-hoc polymorphism**: 엄밀한 의미에서 polymorphism은 아니지만, `methodName`이 같고 `argument`가 다른 경우에 대해서 작동하는 것을 말하며, method overloading이 여기에 속합니다. run-time에 결정되는 것이 아니라, compile-time에 결정되기 때문에 그냥 Compile-Time polymorphism이라고 하기도 하죠.
- **Subtype polymorphism**: 그냥 subtyping이라고도 하는데, 상위 class의 reference variable로 하위 class의 Object를 가리키는 경우를 말합니다. 즉, 상위 class의 reference variable을 사용해서 여러 객체들을 담을 수 있기 때문에 polymorphism 적인 성격을 가지게 되죠. dynamic polymorphism이라고 하기도 합니다.
- **parametric polymorphism**: 정확하게 type을 선언하지 않아도 여러 유형의 변수를 input으로 처리할 수 있는 함수를 만들 수 있는 것을 말하며, generic programming에 여기에 속합니다. 

## Subtyping

- superclass의 reference variable은 subtype의 object를 가리킬 수 있습니다.
- 그리고 superclass의 method는 subclass의 method에 의해서 overridding될 수 있죠.
- 가령 아래와 같이 `BaseClass`와 BaseClass를 상속받는 `DerivedClass`가 있다고 하겠습니다. 그리고, `BaseClass`의 `print()`는 `DerivedClass`에서 `Override`되었죠. 이를 표시하기 위해서 Annotation을 달아 주었습니다.

```java
class BaseClass {
    BaseClass () {
    }
    public void print() {
        System.out.printf("This is BaseClass\n");
    }
}
class DerivedClass extends BaseClass{
    DerivedClass () {
    }
    @Override
    public void print() {
        System.out.printf("This is DerivedClass\n");
    }
}
```

- 위와 같이 선언되어 있는 경우에는 `BaseClass` reference variable를 사용해서 subClass의 객체를 가리킬 수 있고, 또 subClass의 method를 call해서 사용할 수도 있습니다.
- 다만, 이렇게 되기 위해서는 반드시 해당 method의 이름이 baseClass에도 있어야 합니다. 즉, Override해야만 사용할 수 있는 것이지, 만약 baseClass에서 `print`라는 이름의 method가 없다면 `c1` 객체에서 `print()`를 call하여 사용할 수 없죠.

```java
BaseClass c1 = new DerivedClass();
c1.print();
```
