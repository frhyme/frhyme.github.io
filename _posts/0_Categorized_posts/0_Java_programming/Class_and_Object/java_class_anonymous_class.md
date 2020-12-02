---
title: Java - Anonymous Class
category: java 
tags: java class OOP 
---

## Java - Anonymous Class

- python에서 필요에 따라 anonymous function을 정의해서 임시적으로 사용하는 것처럼, Java에서도 Anonymous Class 혹은 Anonymous Interface를 정의해서 사용할 수 있습니다. 큰 class를 새로 정의하는 것은 매우 번거로운 일이니까요.
- Anonymous function처럼 Anonymous Class에도 name identifier가 없습니다. 한 번 쓰여지고 말거니까 다시 호출할 일이 없으니까, name identifier를 정의할 필요가 없죠.

```java
new AnonymousClass_or_AnonymousInterface() {
    // fields
    // overridden methods;
};
```

- 보통 다음과 같은 형태로 임시 class를 선언합니다. 이미 기존에 `AnonymousClass_or_AnonymousInterface`가 존재하는 상태에서, 필요에 따라 얘를 확장해서 새로운 class를 정의하는 것이 필요할 수 있죠. 

```java
// Existing Interface 
// Interface가 존재하지만, 아직 method는 Overriding되지 않아 사용할 수 없죠.
interface AnonymousClass_or_AnonymousInterface {
    void virtualMethod(){};
}

// reference Interface로 새롭게 정의되는 임시 클래스
AnonymousClass_or_AnonymousInterface tempObj = new AnonymousClass_or_AnonymousInterface() {
    // overridden methods;    
    @Overridde
    void virtualMethod() {
        System.out.println("This is AnonymousClass");
    }
};
```

## Class with AnonymousClass

- 보통은 다음처럼 Class 내에 InnerClass로 정의하여 사용됩니다.