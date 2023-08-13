---
title: java - BaseClass의 Method가 Overriding되지 않게 하기
category: java
tags: java programming inheritance Overriding
---

## Java - Base Class Method가 오버라이딩 되지않게 하기

- BaseClass에서 정의한 method를 실수로라도 오버라이딩하지 않게 하려면 함수 선언부에 `final`을 붙여주면 됩니다.

```java
class BaseClass {
    int id;
    BaseClass () {
        this.id = 0;
    }
    // 아래처럼 final을 붙여버리면 
    // DerivedClass에서 Method를 오버라이딩할 수 없습니다.
    public final void print() {
        System.out.printf("This is BaseClass %d\n", this.id);
    }
}
class DerivedClass extends BaseClass{
    int id;
    DerivedClass () {
        this.id = 0;
    }
    public void print() {
        System.out.printf("This is DerivedClass %d\n", this.id);
    }
}
```
