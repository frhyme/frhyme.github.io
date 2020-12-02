---
title: Java - Inner Class 
category: java
tags: java programming class 
---

## Java - Inner Class

- Inner Class(내부 클래스)는 클래스 안에 클래스가 또 있는 겁니다. 클래스 안에 Object(Class Instance)가 있는게 아니라, Class 안에서 새로운 Class를 정의하는 것을 말합니다. 대략 다음과 같은 형태로 정의하는 것을 말하죠.

```java
class OuterClass {
    class InnerClass {
    }
}
```

- 물론, 처음 InnerClass를 보면, 왜 굳이 이렇게 써야 하나? 라는 생각이 들 수 있습니다. 두 클래스를 각각 정의하면 되는것 아니야? 라는 생각이 들기는 합니다.
- 보통, 내부 클래스의 코드가 매우 간단하거나, 외부 클래스에 의해서만 사용될 경우 두 클래스는 하나의 클래스로 합쳐서 설계하는 것이 더 좋을 수 있죠. 즉, 논리적으로 두 클래스간의 관계를 표현한다는 것을 의미합니다. 하지만, 내부 클래스가 복잡한 경우 그리고 독점적이지 않게 변하게 된다면 내부 클래스를 빼내어 새로운 `InnerClass.java`파일로 만드는 것이 필요하죠. 음 글쎄요. 저는 이럴 바에는 처음부터 따로 만드는 것이 훨씬 좋지 않나 싶습니다. 그리고, 그 InnerClass의 Instance를 OuterClass의 내부 field로 설정하는 것이 훨씬 좋지 않나? 싶구요.
- 물론, 그 외에도 InnerClass의 존재가 OuterClass 내에서만 정의되므로 보안상 유리하다, 라는 말도 있는데 글쎄요 흠.

## Inner Class의 종류

- 다른 글에서는 InnerClass를 다음 4가지로 분류합니다.
  1. Instance Inner Class: 클래스 내부에 클래스를 선언한 것이며, Instance에 종속적
  2. Static Inner Class: static 키워드가 사용된 내부 클래스로 Class에 종속적, OuterClass Instance 없이도 사용가능
  3. Local Inner Class: 메소드 내부에서 클래스를 선언한 것 
  4. Anonymous Class: 이미 만들어진 클래스(혹은 인터페이스)를 메소드만 재정의하여 임시로 사용하는 것
- 이 글에서는 1번과 2번을 주로 설명합니다. 3번과 4번은 그냥 Inner Class라기보다는 그냥 뭔가....다른...개별적인...무엇...이라고 생각합니다 호호호.

## Simple Inner Class Example

- 우선 Class를 정의합니다. OuterClass 내부에 InnerClass를 정의하였죠. 하나는 Instance에 종속된 InnerClass로, 하나는 Static Instance Class로 만들었죠.

```java
public class OuterClass { // 외부 클래스
    public String name;
    public OuterClass(String name) {
        this.name = name;
    }
    public class InstanceInnerClass { // Instance 내부 클래스
        public String name;
        public InstanceInnerClass(String name) {
            this.name = name;
        }
    }
    public static class StaticInnerClass { // Static 내부 클래스
        public String name;
        public StaticInnerClass(String name) {
            this.name = name;
        }
    }
}
```

- 그리고 `OuterClass`와 `InstanceInnerClass`, `StaticInnerClass`를 생성합니다.

```java
class Main {
    public static void main(String[] args) throws Exception {
        // InnerClass 는 1) Static Inner Class를 만들거나, 2) Instance Inner Class 로 만들 수 있습니다.

        // Static Inner Class ------------------------------
        // InnerClass를 Static하게 선언한 경우에는
        // OuterClass Instance를 생성하지 않아도 사용할 수 있습니다.
        OuterClass.StaticInnerClass staticInnerClass = new OuterClass.StaticInnerClass("StaticInnerClass1");

        // Outer Class -------------------------------------
        // 외부 클래스를 선언하고 정의하는 것은 우리가 알고 있던 것과 동일합니다.
        OuterClass outerClass = new OuterClass("OuterClass1");

        // Instance Inner Class ----------------------------
        // 하지만, Instance InnerClass의 경우는 OuterClass Instance가 있어야 만들 수 있습니다.
        // 문법이 조금 낯설죠.
        OuterClass.InstanceInnerClass instanceInnerClass = outerClass.new InstanceInnerClass("InstanceInnerClass1");

        System.out.println(outerClass.name);
        System.out.println(staticInnerClass.name);
        System.out.println(instanceInnerClass.name);
    }
}
```

## Wrap-up

- 물론, Inner Class의 경우 Outer Class의 Field에 쉽게 접근가능하다는 장점이 있기는 합니다만, 흠, 그래도 이것만으로는 굳이 InnerClass를 만들어야 하는 때를 모르겠습니다. 혹시 누구 아시면 좀 알려주세요 하하하하.
