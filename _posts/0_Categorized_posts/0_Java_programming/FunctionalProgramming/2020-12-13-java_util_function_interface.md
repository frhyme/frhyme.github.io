---
title: Java - Functional Interface
category: java
tags: java programming function interface AnonymousClass FunctionalInterface
---

## Java - Function

- 이전에 우리는 Method Reference 방식을 이용해서 `justPrintFunc`라는 `Consumer<String>`타입의 변수에 함수를 넣어주었습니다.

```java
Consumer<String> justPrintFunc = System.out::println;
```

- 그런데, 만들어진 함수를 보면 실행할 때 `justPrintFunc()`로 실행하는 것이 아니라, `justPrintFunc.accpet()`로 실행합니다. 마치 우리가 늘 쓰던 `classInstanceName.methodName`의 방식으로요. 아, 그렇다면 사실 우리가 지금 쓰고 있는 Function도 사실은 Class인 걸까요?

```java
// RIGHT
justPrintFunc.accept("PRINT_LIKE_THIS");
// WRONG: Insert .accept to call functional interface method
justPrintFunc("PRINT_LIKE_THIS");
```

## Java - Functional Interface

- 우리가 지금까지 Function처럼 쓰고 있는 온 애들, `Consumer`, `Supplier`, `Function` 모두 사실은 그냥 Function을 흉내낸 Interface였던 것이죠. 실제 우리가 사용하는 Standard Function Interface의 `Function<T, R>`은 다음과 같은 형태로 정의되어 있습니다. 우리는 이 Interface를 구현(Implement)하여 함수와 비슷하게 사용하는 것이죠. 다시 말하지만, 실제로 우리는 Function을 사용하는 것이 아니라, Object를 사용하여 Function 흉내를 내는 것입니다.

```java
@FunctionalInterface
    interface Func<INPUT, OUTPUT> {
        // Single Abstract Method(SAM)
        OUTPUT apply(INPUT x);
    }
```

- 다음 코드에서는 앞서 구현한 `FunctionalInterface`를 3가지 방법으로 구현하여, 사용해봅니다.
  1. **By AnonymousClass**: 익명클래스를 사용하여 FunctionalInterface를 구현해줍니다.
  2. **By Lambda Expression**: Lambda Expression을 사용하여, FunctionalInterface를 구현해줍니다. 
  3. **Method Reference**: 이미 존재하는 Class의 Method를 참조하여 구현합니다.
- AnonymousClass를 사용하는 경우, 코드에 Class를 설계한 부분이 담겨 있습니다. 하지만 Lambda Expression, Method Reference의 경우는 컴파일러가 Intermediate Class를 설계한 다음, Instance를 생성해주는 형식으로 구현되기 때문에, `.getClass` method를 사용해 보면 영 이상한 값이 출력되죠.

```java
class Main {
    // FunctionalInterfacea Annotation을 붙여주지 않아도
    // 본 코드에서는 딱히 오류가 나지 않습니다만,
    // 컴파일러에게, "이 아이는 FunctionalInterface"라는 것을 알려줍니다.
    // 따라서, 컴파일러는 FunctionalInterface의 조건을 충족하는지 확인한 다음,
    // 충족히지 않을 경우 compile-error를 발생하여 개발자에게 알려줄 수 있죠.
    // 특히, Single Abstract Method가 아닐 경우 컴파일에러를 발생시킵니다.
    @FunctionalInterface
    interface Func<INPUT, OUTPUT> {
        // Single Abstract Method(SAM)
        OUTPUT apply(INPUT x);
    }

    public static void main(String[] args) throws Exception {
        //--------------------------------------------------------
        // By Anonymous Class
        // Func Interface를 Anonymous Class를 사용해서 정의해줍니다.
        Func<Integer, Integer> func1 = new Func<Integer, Integer>() {
            @Override
            public Integer apply(Integer x) {
                return x + 1;
            }
        };
        System.out.println( func1.getClass() ); // class com.company.Main$1
        System.out.println( func1.apply(1) ); // 2

        //--------------------------------------------------------
        // By Lambda Expression
        // Lambda expression을 사용해서 다음처럼 정의해줄 수도 있죠.
        // 다만, 이 경우에는 해당 Interface가 반드시 SAM(Single Abstract Method)여야 합니다.
        // 2개이상 가질 경우에는 Lambda Expression이 아닌 다른 방법을 사용해야 하고, 
        // 동시에 그럼 Functional Interface를 충족하지 않게 됩니다.
        Func<Integer, Integer> func2 = ( Integer x ) -> x + 1;
        System.out.println( func2.apply(10) ); // 11
        // 다만 Lambda Expression을 사용해서 정의한 경우
        // getClass()를 사용했을 때 결과가 좀 이상하게 나옵니다.
        // ex) class com.company.Main$$Lambda$14/0x0000000800b8d840
        System.out.println(func2.getClass());

        //--------------------------------------------------------
        // By Method Reference
        Func<Double, Double> func3 = Math::sqrt;
        System.out.println( func3.apply(9.00) ); // 3.0
        // Method Reference를 사용하는 경우에도, className이 이상하게 나오죠.
        // ex) class com.company.Main$$Lambda$15/0x0000000800b8da60
        System.out.println(func3.getClass());
    }
}
```

## Wrap-up

- Functional Interface는 "반드시 1개의 Abstract Method를 가져야 합니다". Interface 상에서는 2개의 Abstract Method를 정의되어 있고 lambda expression 혹은 method reference를 사용하여  구현해주는 경우에는, `Multiple non-overriding abstract methods found in interface com.company.Main.Func`라는 오류를 띄워주죠.
- 그러나, AnonymousClass를 사용해서 정의해주는 경우에는 Interface 상에 2개의 Method가 정의되어 있고, 구현해줄 때 2개를 다 구현해줘도 상관없습니다. 오류가 생기지 않죠. 이렇게 되면 사실 Function이 아닌 것이죠. 그냥 익명클래스를 사용해서 마치 함수 흉내를 내는 것 뿐입니다.
- 하지만, `@FunctionalInterface`를 사용하게 되면, 2개 이상의 abstract method가 interface 정의 안에 포함될 경우 알아서 오류를 발생시켜 줍니다.
