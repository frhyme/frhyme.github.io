---
title: Java - Annotation 
category: java
tags: java Annotation programming 
---

## Java - Annotation

- java에서 Annotation은 프로그램에 대한 정보가 담긴 "Comment"라고 생각해도 일단은 무방합니다.
- 하지만 그냥 유저만 보는 것을 목적으로 하는 게 아니라, 컴파일러 혹은 IDE, 프레임워크 들에게 정보를 전달하는 측면에서 Comment와는 다르죠.
- 그 기능을 정리하면 다음과 같습니다.
  1. 컴파일러에게 필요한 정보를 전달한다.
  2. 개발 도구들에게 정보를 전달하고,
  3. Framework나 Library들에게 정보를 전달합니다.
- Annotation은 Class, Variable, function 등 대부분의 개체들에 붙여서 쓸 수 있습니다.

## Depreceated

- `@Depreceated`는 이 메소드를 사용할 경우 혹은 컴파일을 할때 컴파일러 단에서 "이 함수는 가급적 사용을 자제해야 되는구나"라는 것을 알 수 있습니다. 따라서 Warning을 주거나 할 수 있죠.

```java
@Deprecated
public static void simpleFunc(){
    System.out.println("ddd");
}
```

## Overriding

- Class를 상속받으면서 Method Overriding이 발생할 때, `@Override` Annotation을 써주기도 하죠.

```java
class BaseClass {
    int id;
    BaseClass () {
        this.id = 0;
    }
    public void print() {
        System.out.printf("This is BaseClass %d\n", this.id);
    }
}
class DerivedClass extends BaseClass{
    int id;
    DerivedClass () {
        this.id = 0;
    }
    // 아래와 같이 Override되는 경우도 Annotation으로 표시해줄 수 있죠.
    @Override
    public void print() {
        System.out.printf("This is DerivedClass %d\n", this.id);
    }
}
```
