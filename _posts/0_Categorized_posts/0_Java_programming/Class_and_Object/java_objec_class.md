---
title: Java - Object
category: java
tags: java object class programming
---

## Java - Object

- Java에는 `Object`라고 하는 모든 Class의 BaseClass가 되는 Class가 존재합니다. 그냥 다음처럼 새로운 Class를 정의히면 자연스럽게 `Object`라는 클래스를 상속받게 되죠.

```java
class simpleObject { 
    simpleObject() {
    }
}
```

- 따라서 `Object` 객체인 `obj1`은 항위 class인 Integer 객체를 가리킬 수 있습니다. Integer class는 기본적으로 Object를 상속받기 때문이죠. OOP의 기본인 "상위 Reference Variable로 하위 Object를 가리킬 수 있다"를 따르는 것이고, 이를 통해 Polymorphism 또한 달성되죠.

```java
Object obj1 = Integer.valueOf(3);
```

### Object - Methods 

- 앞서 말한 바와 같이 java의 모든 class들은 `Object`를 상속받습니다. 그리고 Object는 다음과 같은 기본적인 method들을 가지고 있죠.
- threads synchronization: `wait`, `notify`, `notifyAll`
  - multithread 환경에서 각 객체들이 관리하는 method들입니다. 
- object identity: `hashCode`, `equals`
  - `hashCode`: 각 객체의 메모리 주소, 라고 일단은 생각하시면 됩니다. 이 값이 같으면 같은 메모리 공간에 값이 할당되어 있는 것이죠.
  - `equals`: 다른 Object와 같은지 Boolean을 리턴합니다.
- object management: `finalize`, `clone`, `getClass`
  - `finalize`: C++에서의 Destructor라고 생각하시면 되고, Java에서 garbageCollector에 의해서 해당 객체가 사라질 때, 호출되는 메소드입니다. 다만, JDK9에서는 이 메소드가 사라져 버렸죠.
  - `clone`: 현재 객체를 복사하여 리턴합니다.
  - `getClass`: 현재 객체가 어떤 class인지 리턴합니다. 아래 코드의 실행 결과와 같이 reference type을 리턴하는 것이 아니라, 해당 reference variable에 들어간 object의 class를 리턴합니다.

```java
Object obj1 = Integer.valueOf(3);
System.out.println(obj1.getClass()); // class java.lang.Integer
```

- human-readable representation: `toString`;
  - 현재 객체를 `String`으로 변환하여 리턴합니다. 
