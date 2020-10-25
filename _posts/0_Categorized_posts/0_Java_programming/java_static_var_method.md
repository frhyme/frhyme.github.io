---
title: java - Static variable, method
category: java 
tags: java programming static 
---

## java - static

- `staic`은 class instance에 종속되는 것이 아니라, class 자체에 종속되는 개념을 말합니다. 굳이 Instance를 만들지 않아도 접근할 수있는 아이를 말하죠.
- 가장 빈번하게 사용되는 경우는 아래 코드와 같이, 현재 "Instance가 몇 개나 만들어졌는지 확인하기 위해서"입니다.
- 아래 코드에서 `countA`는 static variable(class variable)이며, 특정 객체(instance)에 종속되는 것이 아니라, class에 종속됩니다. constructor가 호출될 때마다, 값을 증가시키는데, 이를 통해 instance가 몇 개나 생겼는지를 관리할 수 있죠.

```java
public class A {
    // @countA 는 모든 instance에게 공유되는 class variable
    public static int countA = 0;
    public int id;
    
    public A() {
        this.id = countA;
        // constructor가 call될 때마다, static variable인 countA의 값을 증가시킴.
        countA += 1;
    }
    public void print() {
        System.out.printf("@id: %d, @countA: %d \n", this.id, countA);
    }
    public static void printCountA() {
        System.out.printf("@countA: %d\n", countA);
    }
}
```

## static method

- static variable은 static method에 의해서도, instance method에 의해서도 접근 가능합니다.
- 하지만, static method는 class에 의해서만 접근가능합니다.
- 가령 위의 코드가 존재할 때, 아래 코드를 실행하면 문제가 발생합니다.
- `A.printCountA()`과 같이, class에서 접근해야 하죠.

```java
A a1 = new A();
// Error: .printCountA는 Static method이므로, instance에서 실행할 수 없다.
a1.printCountA();
// class에서는 static method에 접근가능.
A.printCountA();
```

## Wrap-up

- Memory는 크게 Static 영역과 Heap 영역으로 구분됩니다. 그리고, Garbage Collector("사용하지 않는 메모리를 알아서 해제하여 메모리 효율을 높여주는 아이")는 힙 영역에 대해서만 관리를 합니다. 다시 말하면, Static 영역은 GC의 관리를 받고 있지 않기 때문에, 프로그램이 실행되면 종료될 때까지 항상 메모리를 차지하고 있는 거라고 봐도 되겠죠.
- 즉, 만약 Static영역을 너무 많이 사용하게 된다면, 메모리 효율이 극단적으로 올라간다, 라고 말할 수 있다는 거죠. 물론, 그럴 일은 매우 적겠지만요.