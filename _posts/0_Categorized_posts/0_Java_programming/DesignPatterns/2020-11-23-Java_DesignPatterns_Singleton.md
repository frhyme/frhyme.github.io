---
title: Java - Design Pattern - Singleton
category: DesignPattern
tags: DesignPattern Singleton java programming class 
---

## Design Pattern - Singleton

- 개발을 하다 보면 딱 하나의 Class Instance만 정의해서 사용해야 할 때가 있습니다. 이런 종류의 설계를 Singleton이라고 하죠. 
  - Singleton은 딱 하나의 Class Instance만 생성하도록 제한됩니다.
  - 그리고 어플리케이션에서 전역변수로 선언됩니다. 정확히 말하면 global access가 가능하다는 얘기죠.
- 즉, 어떤 기능이 "어플리케이션 전체에서 접근 가능해야 하고, 딱 하나만 만들어져도 된다"라면, Singleton으로 정의된다는 이야기죠.

## Java - Singleton Implementation 

- Java에서 Singleton 패턴으로 정의되는 클래스는 다음과 같은 규칙을 따라야 합니다.
  - **private static instance**: class 내부에 static을 사용해서 class 변수로 만들고, private으로 외부에서 접근할 수 없도록 합니다.
  - **private constructor**: constructor를 private으로 정의합니다. public으로 정의할 경우 외부에서 접근해서 새로운 instance를 생성할 수도 있으니까요.
  - **public static method to return instance**: 싱글톤은 단 하나의 인스턴스만 내부에 private으로 존재합니다. 따라서, 외부에서 해당 변수에 다이렉트로 접근할 수는 없죠. 하지만, 동시에 global access가 가능해야 하므로, 해당 변수에 접근할 수 있는 static method를 선언해줍니다.
- 위를 코드로 작성하면 다음과 같습니다.

```java
class SingletonClass {
    // private static으로 instance를 정의해줍니다.
    // static으로 정의했으므로, class에 귀속된 하나의 SingletonClass 만이 생성되죠.
    // 그리고 static은 프로그램이 시작되면 즉시 메모리에 로딩됩니다.
    // private으로 정의했으므로, 외부에서 직접 접근할 수는 없습니다.
    private static SingletonClass instance = new SingletonClass();

    // private으로 constructor를 정의합니다.
    // private으로 정의했기 때문에, 외부에서 생성자를 접근할 수 없죠.
    // 따라서, 딱 하나의 class Instance만 만들어질 수 있습니다.
    private SingletonClass() { }

    // 외부에서 instance를 접근할 수 있는 method를 정의해줍니다.
    public static SingletonClass getInstance() {
        return instance;
    }
}
```

- 위처럼 작성하는 경우, 해당 instance를 사용하든 사용하지 않든 프로그램이 시작되면 바로 메모리에 올려 버리죠. 물론, 이게 더 효율적인 경우도 있습니다. 하지만 우리는 필요할 때, 인스턴스를 생성해서 메모리에 올리는 식으로 진행해보죠.

```java
class SingletonClass {
    // private static으로 instance를 정의하고, 초기값은 null로 정의합니다.
    // 프로그램이 시작되자마자 메모리에 올리는 것이 아니라, 필요할 때 올린다는 이야기죠.
    private static SingletonClass instance = null;

    private SingletonClass() { }

    // 만약 현재 instance가 null이라면, object를 생성하여 넣어줍니다.
    // null이 아니라면 존재하는 object를 그대로 리턴해주죠.
    public static SingletonClass getInstance() {
        if (instance == null) {
            instance = new SingletonClass()
        } else {
            return instance;
        }
        
    }
}
```

## Wrap-up

- 싱글톤은 꽤나 유명한 패턴이기는 한데, 찾아보면 안티패턴이라고 나오는 경우들이 있습니다. 패턴은 "써야 하는 패턴", 안티패턴은 "쓰지 말아야 하는 패턴"이죠. 즉, 이거 구린데 쓰지말자~ 라고 주장한다는 이야기입니다.
- 솔직히, 그럴지도 모르죠. 그러니, 싱글톤을 사용하기 전에는 "이 아이가 정말 싱글톤 패턴으로 만들어야만 하는가?"를 진지하게 생각해봅시다.
