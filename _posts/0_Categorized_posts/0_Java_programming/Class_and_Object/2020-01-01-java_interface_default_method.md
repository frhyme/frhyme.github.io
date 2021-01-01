---
title: Java - interface - default method
category: java
tags: java programming class OOP default interface
---

## Java - interface - default method

- interface에서는 method를 선언만 할 수 있고 정의할 수는 없지만, `default`를 사용하면 정의할 수도 있습니다.

```java
// Interface를 정의하고,
// default method도 선언 및 정의합니다.
public interface InterfaceWithDefault {
    default void printDefault() {
        System.out.println("This is InterfaceWithDefault");
    }
}


// 위 Interface의 구현체인 InterfaceWithDefaultImpl에서
// constructor를 제외한 어떤 method도 만들어주지 않았죠.
public class InterfaceWithDefaultImpl implements InterfaceWithDefault{
    public InterfaceWithDefaultImpl() {
    }
}

// 하지만, main class에서 
// 다음과 같이 default method를 그대로 사용할 수 있습니다.
class Main {
    public static void main(String[] args) throws Exception {
        InterfaceWithDefault a = new InterfaceWithDefaultImpl();
        // default method
        a.printDefault();

        
    }
}
```

## Wrap-up

- interface의 모든 구현체에 동일하게 포함되는 method임에도, interface에서는 method를 정의할 수 없기 때문에 매번 각 구현체에서 모두 새롭게 작성을 해줘야 하는 경우들이 있습니다. 이럴때면 같은 코드가 여러 번 중복되는 셈이죠. 따라서, 그런 경우에 해당 method를 위의 interface의 default method로 정의함으로써, 코드가 효율적으로 변하게 되죠.