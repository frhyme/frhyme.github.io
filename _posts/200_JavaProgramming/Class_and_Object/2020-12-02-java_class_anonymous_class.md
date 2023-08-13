---
title: Java - Anonymous Class
category: java 
tags: java class OOP 
---

## Java - Anonymous Class

- python에서 필요에 따라 anonymous function을 정의해서 임시적으로 사용하는 것처럼, Java에서도 Anonymous Class 혹은 Anonymous Interface를 재정의해서 사용할 수 있습니다. 필요에 따라, 특정 method만을 바꾼 class를 넘겨주거나 할 필요가 있으니까요.
- 만약 익명 함수를 reference 변수에 저장하지 않고 바로 사용하려면 다음처럼 정의하고 바로 사용할 수 있습니다. 

```java
new AnonymousClass() {
    @Override
    public returnType OverridenMethod(inputType) {

    }
};
```

- 익명클래스(AnonymousClass)를 정의하기 위해서는 기존에 존재하는 Interface나 Class를 이용해야 합니다. 걔네를 Overridde해주는 것이죠. 가령, 저에게 다음과 같은 Interface가 있다고 하겠습니다. 매우 간단한 `printSimple()`라는 method만을 가지는 Interface죠.

```java
public interface SimpleInterface {
    public void printSimple();
}
```

- 아직 method가 정의되어 있지 않기에 필요에 따라 새롭게 정의해서 쓸 수 있습니다.
- 다음처럼 interface `SimpleInterface`를 implement하여 두 개의 익명 클래스를 만들 수 있죠. 두 클래스의 method는 다르게 정의되어 있습니다.

```java
class Main {
    public static void main(String[] args) throws Exception {
        SimpleInterface anonymousClass1 = new SimpleInterface() {
            @Override
            public void printSimple() {
                System.out.println("This is anonymousClass111111");
            }
        };
        SimpleInterface anonymousClass2 = new SimpleInterface() {
            @Override
            public void printSimple() {
                System.out.println("This is anonymousClass222222");
            }
        };
        anonymousClass1.printSimple();// This is anonymousClass111111
        anonymousClass2.printSimple();// This is anonymousClass222222
    }
}
```

## Wrap-up

- 중요한 것은, 기존에 정의되어 있는 interface나 class를 새롭게 정의하는 방식으로 익명 클래스를 정의한다는 것이죠. 컴퓨터도 내가 부르는 애가 대충 어떤 method를 가지고 있는지는 알아야 하잖아요? 즉, reference variable이 대충 어떤 식으로 구성되어 있고 어떤 메소드가 선언될 것인지는 알아야, 오른쪽에서 `new constructor()`를 통해 선언된 instance를 mapping시켜줄 수 있으니까요.
- 익명 클래스는 보통 Swing 이라고 하는 Java Library나, Google Web Toolkit에서 다양한 유저의 interface에 따라 작동하는 listener를 만들어주기 위해서 사용되곤 합니다. 잠깐 즉각적으로 사용되므로 그렇기는 한데, 사실 익명 함수와 마찬가지로 익명 클래스를 이곳저곳에 많이 뿌려놓으면 유지보수가 매우 어렵죠.
- 그래도, "왜 익명클래스가 필요하지?"싶으신 분들은, python에서 **lambda expression**으로 인해 받았던 도움을 기억해내시면 좋습니다 호호.