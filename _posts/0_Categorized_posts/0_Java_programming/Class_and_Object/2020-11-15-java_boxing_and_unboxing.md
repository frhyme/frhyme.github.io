---
title: Java - boxing and unboxing
category: java
tags: java boxing class unboxing
---

## Java - boxing and unboxing

- Java에서 primitive type(`int`, `double` 등)은 모두 해당되는 class를 가지고 있습니다. 이런 클래스들을 모두 wrapper라고 부르죠. 그리고, wrapper는 기본적으로 immutable의 성질을 가지고 있습니다.
- 우선, primitive type은 class가 아니죠. 그냥 메모리에 value가 그대로 들어 있는 변수이고, reference type들에 비해서 속도 측면에서는 장점이 있죠. 하지만, 필요에 따라서 primitive type이 아니라 Object로 표현하는 것이 편할 때가 있죠. 대략 다음과 같은 경우들이 있습니다.
  - variable이 `null`값을 가지는 것이 필요할 때
  - generic collection에 값을 저장할 때(primitive type은 generic으로 표현되어 질 수 없습니다).
  - class의 method를 사용하고 싶을 때(값과, 값과 관련된 method들을 함게 관리할 수 있죠)
- 모든 primitive type은 해당하는 Class를 가지고 있습니다. 다음과 같죠. 그냥 앞 글자만 대문자로 바꿔버리면 됩니다. 그리고 얘네들을 보통 Wrapper type이라고 합니다.

![wrapperClassInJava](https://media.geeksforgeeks.org/wp-content/cdn-uploads/20200806191733/Wrapper-Class-in-Java.png)

- 다음처럼 boxing 혹은 unboxing을 할 수 있ㅅ브니다.

```java
class Main {
    public static void main(String[] args) {
        int a = 10;
        Integer aInteger = Integer.valueOf(a); // Boxing
        int b = aInteger.intValue(); // UnBoxing
        int c = aInteger; // autoBoxing
    }
}
```

- 한 가지 유의할 사항은, 값을 비교할 때 `==`를 사용해서는 안된다는 거죠. `==` operator는 primitive의 값을 비교하는 연산자이고, object들은 `.equals` method를 사용해서 비교해줘야 합니다.
  - 아래 코드를 보면, 이례적으로 큰 Integer값을 대입해주었는데, 이는 Object Interning을 피하기 위해서입니다. Object interning은 메모리를 효율적으로 사용하기 위해서 빈번하게 사용되는 객체들은 동일한 객체를 가리키도록 만드는 것을 말하죠.
  - 만약 아래 코드에서 값을 `100`으로 대입해주었다면 `==`인 경우에도 `true`를 만들어주게 됩니다. 이는 `aInteger`와 `bInteger`가 가리키는 객체가 동일하기 때문이죠.

```java
class Main {
    public static void main(String[] args) {
        // 이례적으로 큰 Integer값을 대입해주었는데, 이는 Object Interning을 피하기 위해서입니다.
        Integer aInteger = 10000000;
        Integer bInteger = 10000000;
        
        System.out.println(aInteger == bInteger); // false
        System.out.println(aInteger.equals(bInteger)); // true
    }
}
```
