---
title: Java - Simple Currying and example
category: java
tags: java programming function interface Currying
---

## Java - Currying

- Currying은 `n`개의 인자를 받는 함수로부터 `m(m < n)`의 인자의 값을 고정한 새로운 함수를 만들어내는 것을 말합니다.

```python
f(a, b, c) # Original Function
# 원래 함수로부터 a의 값을 고정 시킨 새로운 함수를 만듬.
g(a=10, b, c) # Curried Function
```

## Java - Currying Example

- Java에서도 `FuncalInterface`를 사용해서 currying을 수행할 수 있습니다.
- 사실, `Function<T, R>`을 사용해도 되지만, 글자가 너무 길어서 저는 `FunctionalInterface`인 `F`를 새로 만들었습니다.

```java
import java.util.function.*;

class Main {
    @FunctionalInterface
    public interface F<InputType, OutputType> {
        public OutputType apply(InputType x);
    }
    public static void main(String[] args) throws Exception {
        /*
        * polyEquation: 4개의 인자를 순차적으로 받는 3차 방정식
        * "a + b * x + c * x * x"를 의미하며,
        * a, b, c, x 의 순으로 인자를 받을 계획입니다.
        * */
        F<Double, F<Double, F<Double, F<Double, Double>>>> polyEquation;
        // a -> b -> c -> x 의 순으로 인자를 하나씩 입력받겠다고 정의합니다.
        polyEquation =  a -> b -> c -> x -> {
            return a + b * x + c * x * x;
        };
        // a, b, c를 순차적으로 적용했습니다.
        // 하지만, x는 아직 적용하지 않았죠. 따라서 얘는 아직도 function입니다
        F<Double, Double> poly_1_2_3 = polyEquation.apply(1.0). apply(2.0).apply(3.0);
        System.out.println( poly_1_2_3.apply(10.0) ); // 321.0
        System.out.println( poly_1_2_3.apply(1.0) ); // 6.0
    }
}
```
