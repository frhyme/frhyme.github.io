---
title: Java - Design Pattern - Factory Pattern
category: DesignPattern
tags: DesignPattern Factory java programming class 
---

## Design Pattern - Factory

- 지금까지는 늘 `new` operator를 사용하여 Class Instance를 생성해 왔습니다. 이것도 딱히 틀린 방법이 아니기는 하지만, 관련된 코드를 좀 더 합쳐버리는 방법(Encapsulation)이 있죠.
- 아래 코드에서 보는 것과 같이, "외부에서 어떤 class를 생성할지 전달받고, 내부에서 만들어서, 다시 외부로 Class Instance를 전달하는 것"것을 Factory Pattern이라고 합니다.

```java
// Existing Way
// 이렇게 해도 됩니다만, 새로운 Class Instance를 생성하는 코드를 좀더 응축하는 게 좋겠습니다.
BaseClass obj1 = new DerivedClass1();
BaseClass obj2 = new DerivedClass2();

// Better Way by Factory.
// 외부에서 생성한 Class의 type을 전달받고 내부에서 생성하여 Return
BaseClass obj1 = ObjectFactory("DerivedClass1");
BaseClass obj2 = ObjectFactory("DerivedClass2");
```

## Wrap-up

- 좀 더 괜찮은 예제를 찾을 수 있을 것 같은데, 다음에 시간이 나면 추가로 보완해보도록 하겠습니다.
