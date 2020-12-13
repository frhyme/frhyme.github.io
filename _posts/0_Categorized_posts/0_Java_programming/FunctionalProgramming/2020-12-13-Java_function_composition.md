---
title: Java - Function Composition
category: java
tags: java programming function 
---

## Java - Function Composition

- Java에서 Function들은 `.andThen`, `.compose`라는 두 메소드를 가지고 있는데, 이 메소드를 사용해서 새로운 함수를 만들어낼 수 있습니다.
- 다만, 적용 순서가 조금 다릅니다.
  - `f.andThen(g).apply(x)`: g(f(x))
  - `f.compose(g).apply(x)`: f(g(x)) 

```java
import java.util.function.*;

class Main {
    public static void main(String[] args) throws Exception {
        Function <Integer, Integer> plusOne = (Integer x) -> x + 1;
        Function <Integer, Integer> square = (Integer x) -> x * x;

        // andThen 의 경우 
        // 순서대로 함수를 적용함 즉 square(plusOne(x))
        System.out.println(
                plusOne.andThen(square).apply(10)
        ); // 121
        
        // compose의 경우
        // 안쪽부터 적용함. pluseOne(square(x))
        System.out.println(
                plusOne.compose(square).apply(10)
        ); // 101
    }
}
```
