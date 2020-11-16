---
title: Java - Interface
category: java 
tags: java programming OOP interface class 
---

## Java - Interface

- C++을 공부해보신 적이 있으신 분들은 아시겠지만 보통 OOP에서는 Abstract class를 만들어 두고 이를 상속하도록 하는게 일반적이죠. Abstract Class에는 field와 Behaviour가 모두 정의됩니다.
- 하지만, "네가 누구인지는 네가 무엇을 하는지에 의해 결정된다"를 통해 대상을 결정할 수도 있겠죠. 이렇게 대상을 모델링하기 위해 java에서는 Interface 라는 것을 사용합니다.
- 아래 code에서 보는 것처럼 `abstract class`를 정의하는 것과 유사하죠. method의 body는 정의되어 있지 않죠.

```java
interface BattleCharacter {
    void fightMethod(); 
}
```

- 그리고 class에서 상속받습니다. 이 때는 `implements`를 사용해서 상속받아야 하죠. 그리고, abstractClass와 마찬가지로 method를 정의해주어야만 합니다.

```java
class KnifeCharacter implements BattleCharacter {
    void fightMethod() {
        // Use Knife;
    };
}
```

## Interface, Abstract Class

- Class는 여러 Interface를 상속받을 수 있습니다. 일종의 '다형성'을 지원하도록 만들어진 셈인데, '자아'를 여러 개 심어준다고 생각해도 됩니다. 가령, "남자", "직장인" 이라는 두 가지 interface를 설계한 다음, 저라는 class에 이를 상속받도록 해주면, 두 가지 자아가 가지고 있는 모든 메소드를 사용할 수 있게 되죠.
- 그리고, `interface`는 class뿐만 아니라, interface들이 상속받는 것도 가능합니다. 다만, interface가 interface를 상속받을 때는 `implements`가 아닌, `extends`를 사용합니다.

```java

interface A { }
interface B { }
// class implements interface
class C implements A, B { }
// interface extends interface
interface D extends A, B {}
```
