---
title: Java - Standard Functional Interface
category: java
tags: java programming function interface FunctionalInterface
---

## Java - Standard Functional Interface

- 직접 interface와 `@FunctionalInterface` Annotation을 사용하여 Function을 정의하고 구현하여 사용할 수 있으나, 귀찮으므로 웬만하면 이미 Java에서 구현되어 `java.util.function` 패키지에 있는 놈들을 사용하기로 합니다.
- Java에는 다음과 같은 5 종류의 Functional Interface들이 존재합니다. 각 Interface를 extend하는 더 많은 interface들이 있구요.
  - **Function**: Input과 Ouput이 서로 다른 타입일 수도 있음
  - **Operator**: Input과 Outptu이 같은 타입임, Function의 Special Case
  - **Predicate**: input을 받아서, boolean만을 리턴하는 함수
  - **Supplier**: 아무것도 입력받지 않고, return만 하는 함수
  - **Consumer**: 입력만 받고 return하지 않는 함수
- 사실, `Function`하나 만으로도 다 구현할 수 있습니다. `java.util.function` 내에 보면 매우 자세한 FunctionalInterface들이 있는데, 이를 모두 굳이 설명하지는 않겠습니다. 

## Java Standard Functional Interface

- 간단한 예제는 다음과 같습니다.

```java
import java.util.function.*;

class Main {
    public static void main(String[] args) throws Exception {
        // ---------------------------------------
        // Function: inputType, outputType 모두 표시
        // BiFunction의 경우는 Input이 2개이므로 2 type을 모두 표시
        // .apply method를 사용하여 결과를 출력함
        Function<String, Integer> strToInt = Integer::parseInt;
        BiFunction<Integer, Integer, Integer> mult = (Integer x, Integer y) -> {
            // multiLine의 경우는 return을 표시.
            return x * y;
        };
        System.out.println(strToInt.apply("34"));// 34

        // ---------------------------------------
        // Operator: inputType, outputType이 같으므로 보통 하나만 표기함.
        // Unary, Binary 모두 Operator는 모두 타입이 같다고 생각하고 정의됨.
        // .apply method를 사용하여 결과를 출력함
        UnaryOperator<Integer> plusOne = (Integer x) ->  x + 1;
        BinaryOperator<Integer> substract = (Integer x, Integer y) -> x - y;
        System.out.println(substract.apply(10, 3)); // 7

        // ---------------------------------------
        // Consumer: ouput이 없으므로, inputType만 표시
        // .accept method를 사용하여 결과를 확인
        Consumer<String> printStr = (String s) -> System.out.printf("This is %s\n", s);
        printStr.accept("frhyme");// "This is frhyme"

        // ---------------------------------------
        // Supplier: input이 없으므로, outputType만 표시
        // .get()를 사용하여 값을 리턴
        Supplier<Integer> returnZero = () -> 0;
        System.out.println(returnZero.get()); // 0

        // ---------------------------------------
        // Predicate: outputType은 boolean이므로 inputType만 표기
        // .test()를 사용하여 확인
        // .negate  를 사용하여 true, false 결과를 반대로 출력하는 것도 가능함.
        Predicate<Integer> isPositive = (Integer x) -> x > 0;
        System.out.println(isPositive.test(10)); // true
        System.out.println(isPositive.test(-2)); // false
        System.out.println(isPositive.negate().test(10)); // false
    }
}
```
