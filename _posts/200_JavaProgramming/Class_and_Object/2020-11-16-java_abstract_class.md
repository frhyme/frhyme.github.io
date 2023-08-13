---
title: Java - abstract class
category: java
tags: java class programming abstract
---

## Java - Abstract class

- 필요에 따라서, 프로그램의 모든 class가 상속받는 baseClass를 정의할 때가 있습니다. 음, 이건 일종의 디자인 패턴인데요. 가령 RPG게임 같은 것에서 모든 캐릭터가 HP, MP를 가지고 또 비슷한 method 이름들을 가진다면 모든 character class가 상속받는 Abstract baseClass를 만들어서 코드를 중복으로 쓸 필요 없도록 할 수 있겠죠. 
- 그리고 동시에, baseClass는 Object로서 존재할 수는 없고, 그저 다른 class들이 상속받는 용도로만 사용한다고 할 때, 이럴 대는 abstract class로 설계해서 만들 수 있죠. 
- abstract class는 다음처럼, class 앞에 `abstract`만을 붙임으로써 선언 및 정의해줄 수 있습니다.

```java
public abstract class AbstractBaseClass {
    int id;
}
```

- 그리고 abstractBaseClass는 다음과 같은 주요 특징을 가집니다.
- abstract class는 Object로 만들어질 수 없습니다. 

```java
// 'AbstractBaseClass' is abstract; cannot be instantiated
AbstractBaseClass abc = new AbstractBaseClass();
```

- abstract class는 다음처럼, class 앞에 `abstract`만을 붙임으로써 선언 및 정의해줄 수 있습니다. 그리고, method 앞에 `abstract`를 붙이면, 해당 method가 abstract라는 것, 즉 정의되지 않았다는 것을 말하죠. abstract method는 "아직 정의되어 있지 않으며, 이후 abstract class를 상속받는 다른 class들이 정의해줘야만 한다"라는 표시입니다.

```java
public abstract class AbstractBaseClass {
    int id;
    // {}가 없어야 합니다. 있으면 "Abstract methods cannot have a body" Error가 뜨죠.
    public abstract void justMethod();
}

public class AAA extends AbstractBaseClass {
    AAA () {};
    // AbstractBaseClass를 상속받는 AAA에서 abstract method인 justMethod를 정의해줍니다.
    public void justMethod() {
        System.out.println("This is AAA");
    }
}
```

- abstract class는 다른 abstract class를 상속받을 수도 있습니다.
- abstract class도 상속자(constructor), field, non-abstract method를 가질 수도 있습니다.
