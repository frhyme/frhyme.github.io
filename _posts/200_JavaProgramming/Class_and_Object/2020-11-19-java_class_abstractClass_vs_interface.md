---
title: Java - Abstract Class vs. Interface
category: java
tags: java programming class Interface Abstract OOP
---

## Java - Abstract Class vs. Interface

- Abstract Class와 Interface는 "아직 구현되지 않은, 추상화된 클래스"를 의미합니다. 직접 Object로 구현되어질 수는 없고, 이후 얘네를 다른 Class가 상속받아서 virtual method들을 새롭게 정의해줘야 하죠. 이렇게 쓰고 보면 이 둘이 매우 비슷해 보이죠.
- 그렇다면, 이 둘의 차이점은 무엇일까요?(물론 Java의 버전이 업데이트 됨에 따라서 조금씩 달라지기는 합니다만).
  - Abstract Class의 경우는 abstract method와 non-abstract method를 모두 가질 수 있습니다. 즉, 몇몇 method들은 abstract class에서 정의되어서 사용할 수 있다는 이야기죠.
  - Abstract Class는 다른 Abstract Class는 물론 regular class를 extend할 수 있습니다. 하지만, 오직 한 개의 class만을 extend할 수 있습니다. 두 개의 class를 동시에 extend하는 것은 불가능하죠. 또한, final, non-final, non-static variable을 모두 field로 가질 수 있죠.
  - Interface는 오직 Interface만을 extend할 수 있습니다. 여러 Interface를 동시에 extend할 수 있죠. 그리고 단지 static, final variable만을 가질 수 있습니다.
  - Abstract Class는 Constructor를 가지고 있지만, interface는 Constructor를 가지고 있지 않죠.
  - interface는 보통 class의 interface 부분과 구현된 부분을 분리(Decouple)하기 위한 목적으로 사용되는 반면, abstract class는 subclass들로부터 공유되는 공통 field들을 뽑아내는 목적으로 사용됩니다.
- 사실 결론부터 말하면 형식적인 것보다는 "목적"이 가장 다릅니다. 마지막에 한 말, interface는 "기능에 대한 선언부와 구현 부분을 분리하기 위한 목적"으로 사용되는 반면, abstract class는 많은 subclass들이 공통으로 가지고 있는 field를 뽑아내서 중복을 줄이기 위해 사용되죠. 이 목적을 분명하게 알고 있으며, 오히려 덜 헷갈립니다.
- 따라서, interface > abstract base class > class 의 순으로 상속받는다, 처럼 생각하면 더 편하죠.

## Simple class by ABC and Interface

- Interface와 Abstract Class를 사용해서 간단한 클래스를 만들면 다음과 같습니다.

```java
interface ObjectBehaviour {
    // 공통이 되는 행동부를 선언
    void walk();
    void run();
}

abstract class ObjectClass implements ObjectBehaviour{
    // 모든 subClass들의 field를 뽑아냄
    protected double walkSpeed;
    protected double runSpeed;
}

class OurObject extends ObjectClass {
    public OurObject(double walkSpeed, double runSpeed) {
        this.walkSpeed = walkSpeed;
        this.runSpeed = runSpeed;
    }
    public void walk(){
        System.out.println("Walk");
    }
    public void run(){
        System.out.println("Run");
    }
}
```
