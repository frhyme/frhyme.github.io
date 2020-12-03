---
title: Java - Inner Class에서 Outer Class 접근하기
category: java
tags: java programming class shadowing InnerClass
---

## Java - Inner Class에서 Outer Class 접근하기

- Class 안에 InnerClass를 만들었습니다.
- 그리고 InnerClass의 method인 `printAllName()`에서 OuterClass의 field인 `OuterName`과 InnerClass의 field인 `InnerName`을 모두 출력하죠.
- OuterClass의 field인 `OuterName`이 private이지만 InnerClass에서는 접근 가능하기 때문에 다음처럼 쉽게 접근할 수 있죠.

```java
public class OuterClass { 
    private String OuterName;
    public OuterClass(String OuterName) {
        this.OuterName = OuterName;
    }
    public class InstanceInnerClass {
        public String InnerName;
        public InstanceInnerClass(String InnerName) {
            this.InnerName = InnerName;
        }
        // In this method, accessing field in outer and inner class is possible. 
        // when they have different name.
        public void printAllName() {
            System.out.printf("OuterName: %s, InnerName: %s\n", OuterName, InnerName);
        }
    }
}
```

- 그러나, 만약 두 field의 이름이 같다면 어떻게 될까요? OuterClass의 field도 `name`이고, InnerClass의 field도 `name`이라고 합시다.
- 이 때는 Shadowing으로 인하여 InnerClass의 field `name`이 OuterClass의 field인 `name`을 가려버리기 때문에, 이전과 같은 방식으로는 OuterClass의 field에 접근할 수 없습니다.
- 그렇다면 어떻게 해야 접근할 수 있을까요?

```java
public class OuterClass { 
    private String name; // field which has same name
    public OuterClass(String name) {
        this.name = name;
    }
    public class InstanceInnerClass {
        public String name; // field which has same name
        public InstanceInnerClass(String name) {
            this.name = name;
        }
        public void printAllName() {
            // What should be written in this code 
            // to print both name fields from OuterClass and InnerClass
            System.out.printf("OuterName: %s, InnerName: %s\n", name, name);
        }
    }
}
```

## Solution - Use OuterClass.this

- 간단하게 말하자면, InnerClass 내에서 `OuterClass.this.name`를 사용하여 OuterClass의 field에 접근할 수 있습니다.
- 생각해보면, Class Scope 안에서 새롭게 생성된 Class Instance의 method이므로 `OuterClass.name`로 접근할 수 없고, `this`를 통해 내부의 내 instance에 대해서 접근할 수 있도록 해주는 거죠. 늘 그렇지만 결과를 보면 매우 타당합니다. instance method이기 때문에, `this`를 사용하지 않으면 안되는 거죠.
- 즉, 다음처럼 만들어버리면 됩니다.

```java
public class OuterClass { // 외부 클래스
    private String name;
    public OuterClass(String name) {
        this.name = name;
    }
    public class InstanceInnerClass { // 내부 클래스
        private String name;
        public InstanceInnerClass(String name) {
            this.name = name;
        }
        public void printAllName() {
            // OuterClass.this.name 을 사용해서 외부 클래스의 instance field에 접근합니다.
            System.out.printf("OuterName: %s, InstanceInnerName: %s\n", OuterClass.this.name, this.name);
        }
    }
}

```

## Use OuterClass.name with static

- 그렇다면 다음처럼 static method로 만들면 `OuterClass.name`로 접근할 수 있는 걸까요? 
- 아니요. 얘는 Static Class에 속한 Static Method죠. 즉 Class에 종속적입니다. 그런데, OuterClass의 name은 Static이 아닙니다. 즉, Instance에 종속적이죠.
- Static한 method가 Instance에 종속적인 field에 접근한다? 말이 안되죠. Instance는 한 개가 아니니까요. 결론적으로, 안된다는 이야기입니다. 만약 어떻게든 OuterClass.name를 쓰고 싶다면 name도 static으로 만들어버리면 됩니다.

```java
public class OuterClass { // 외부 클래스
    private static String name;
    public OuterClass(String name) {
        this.name = name;
    }
    public static class StaticInnerClass {
        private static String name;
        public static void printAllName() {
            // 컴파일 자체가 안됩니다.
            System.out.printf("OuterName: %s, StaticInnerName: %s\n", OuterClass.name, name);
        }
    }
}
```

## wrap-up

- 얼마전까지만 해도, InnerClass를 만드는 것이 무슨 의미가 있나 싶었는데, 이렇게 내부에서 외부 field를 접근할 수 있도록 함으로써 정보를 응축하고(encapsulation), 외부에서 접근할 수 없도록 하는 게 꽤 유용할 수 있을 것 같습니다. 다만 아직도 좀 더 분명한, "반드시 InnerClass를 사용해야 하는 사례"를 알게 되면 좋겠네요.

## reference

- [stackoverflow - How Can I access outerClass field from inner Class](https://stackoverflow.com/questions/65091717/how-can-i-access-outerclass-field-from-innerclass#65091827)
