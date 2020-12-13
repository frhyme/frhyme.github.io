---
title: Java - Function Composition
category: java
tags: java programming function 
---

## Java - Function Composition

- Java에서 Function들은 `.andThen`, `.compose`라는 두 메소드를 가지고 있는데, 이 메소드를 사용해서 새로운 함수를 만들어낼 수 있습니다.

```java
import java.util.function.*;

class Main {
    public static void main(String[] args) throws Exception {
        //--------------------------------------------------------
        // Function의 andThen, compose method를 사용하여
        // 함수들을 조합하여 새로운 함수를 만들 수 있습니다.
        Double x = 2.0;
        Function<Double, Double> squareFunc = (Double d1) -> ( d1 * d1 );
        Function<Double, Double> square2Func = squareFunc.compose(squareFunc);
        Function<Double, Double> square3Func = squareFunc.compose(squareFunc).andThen(squareFunc);

        // 만들어진 함수는 동일하게 .apply 메소드를 사용해서 값을 출력합니다.
        System.out.println(squareFunc.apply(x)); // 4.0
        System.out.println(square2Func.apply(x)); // 16.0
        System.out.println(squareFunc.compose(squareFunc).apply(x)); // 16.0
    }
}
```
