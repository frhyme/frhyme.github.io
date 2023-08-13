---
title: Java - Functional Programming - Lambda Expression
category: java
tags: java programming lambda function 
---

## Java - Functional Programming - Lambda Expression

- Java는 OOP, 객체지향 언어입니다. OOP 자체가 꽤나 올드한 패러다임이기는 하고 저도 오랫동안 "그거 옛날 패러다임이잖아?"라면서 무시했던 일들도 있는데, 장난감 레벨에서 뭔가를 만드는 것이 아니라, 거대한 시스템을 만들어야 하는 상황에서는 객체지향적인 접근이 훨씬 효과적일 때가 있습니다. 
- 그런데, 우리가 처음 프로그래밍을 배울 때를 생각해보면 class부터 생각하지 않습니다. 보통 Function의 단위로 접근하게 되는데, 이는 Class 자체가 처음 프로그래밍을 하는 사람의 입장에서, 그리고 아직 큰 규모의 프로젝트를 경험해본 적이 없는 살마의 입장에서는 매우 어려운 개념이 되기 때문이죠. 저 또한 처음 OOP 수업을 들었을 때, 이 내용이 코딩이라기보다는 '철학'에 가까운 느낌을 받아서 놀라기도 했었습니다.
- 아무튼, 그래도, 그냥 Function을 하나만 만들면 되는데, 그리고 Functional Programming을 하기 위해서 기존의 OOP는 약간의 충돌이 발생합니다. OOP는 "모든 것이 Object"다, 라는 접근을 가지고 있다면, Functional Programming(FP)은 "모든 것이 Function이다"라는 접근으로 문제를 풀어나가는 것이죠. 무엇이 옳다 그르다는 무의미하고 둘다 필요에 따라서 합당하게 쓰는 것이 필요합니다.

## python - Lambda Expression

- lambda expression은 익명함수, 라고 하기도 합니다. python에서 코딩할 때 많이 사용하긴 하는데, 음 별로 좋은 방식은 아닙니다. 갑자기 python얘기지만, 만약 다음처럼 lambda function을 만들게 되면, pylint가 바꾸라고 뭐라고 하죠.
- 또, 미묘하지만, [python - flake8 - e731 - Do not assign a lambda expression, use a def](https://frhyme.github.io/python-basic/python_flake8_e731/)에 그 차이를 정확하게 작성해두었습니다.

```python
# BAD Function Definition
func1 = lambda x: x + 10

# GOOD Function Definition
def func1(x): 
    return x + 10
```

- 물론, lambda function을 정의하고 어떤 변수에 지정하지만 않으면 문제가 되지 않습니다. 앞서 말한 것처럼, 얘는 원래 "익명함수"거든요. 그런데, 만약 얘를 variable에 집어넣을 것이라면, `def funcName`를 사용해서 정식으로 집어넣으라는 얘기죠.

## Java - lambda expression

- Java에서는 Lambda expression을 `(parameters) -> function_definition`으로 정의하고 사용합니다. `parameter`는 해당 함수에 들어가는 input을 말하고, `function_definition`에는 `parameter`를 통해 무엇이 수행되는지가 정의되죠.
- 함수의 type에는 여러 가지가 있는데, `java.util.function`에 보통 정의되어 있습니다. 아래 코드에서는 1개의 parameter를 전달받아서 1개의 output을 리턴하는 `Function`과, 2개의 parameter를 전달받아서 1개의 output을 전달하는 `BiFunction`을 사용하여 lambda expression을 정의하고, 해당 타입 변수에 assign해주었습니다.
- 그리고, 함수를 사용하려면 해당 함수의 `.apply` method를 사용해야 하죠.

```java
import java.util.function.Function;
import java.util.function.BiFunction;

class Main {
    public static void main(String[] args) throws Exception {
        // --------------------------------------------------
        // Function<InputType, ReturnType> funcName
        // 이 Function은 Integer를 입력받고 1을 더하고 String으로 변환하여리턴해주는 함수입니다.
        Function<Integer, Integer> plusOne = (Integer x) -> x + 1;
        // 실행할 때는 해당 function의 apply method를 사용해서 써야 합니다.
        System.out.println( plusOne.apply((1)) ); // 2

        // --------------------------------------------------
        // BiFunction<InputType1, InputType2, ReturnType> funcName
        // BiFunction은 2개의 Input을 받아서 처리해주는 함수죠.
        BiFunction<Integer, Integer, Integer> plusXY = (Integer x, Integer y) -> x + y;
        System.out.println( plusXY.apply(1, 3) ); // 4     

        // --------------------------------------------------
        // Multi Line function
        // Function을 multi-line으로 선언하려면 {}를 사용해야 합니다.
        // 그리고 아무 값도 반환하지 않을 때는 type은 Void로, 값은 null을 리턴해야 하죠.
        Function<Integer, Void> multiLineFunc = (Integer x) -> {
            for (int i = 1; i < 10; i++) {
                System.out.printf("%d * %d  %d\n", x, i, i * x);
            }
            return null;
        };
        multiLineFunc.apply(3);   
    }
}
```

## Passing Function to Method

- lambda expression은 `Function`, `BiFunction`등의 변수에 값을 저장해서 넣을 수 있습니다. 각 함수가 타입을 가지니까요.
- 그리고 method를 정의할 때는 해당 method에 어떤 변수타입이 parameter가 들어가는지 정의하죠.
- 정리하자면, **함수 또한 변수이므로, method에 함수를 그대로 넘겨줄 수 있다** 라는 말이 됩니다. 정말 그럴까요?
- 그렇습니다. 다음 코드를 보면 무슨 말인지 이해하실 거에요.

```java

import java.util.function.Function;
import java.util.function.BiFunction;

class Main {
    public static Integer multiFunc(Integer x, Integer y, Function<Integer, Integer> func) {
        // x, y에 각각 func를 적용한 다음 곱을 리턴하는 함수
        return func.apply(x) * func.apply(y);
    }
    public static void main(String[] args) throws Exception {
        // plusOne : 1을 더해서 리턴해주는 함수
        // minusOne: 1을 빼서 리턴해주는 함수
        Function<Integer, Integer> plusOne = (Integer x) -> x + 1;
        Function<Integer, Integer> minusOne = (Integer x) -> x - 1;
        
        System.out.println( multiFunc(10, 8, plusOne) ); // 99
        System.out.println( multiFunc(10, 8, minusOne) ); // 63
        // lambda expression을 바로 넘겨주는 것도 가능합니다.
        System.out.println( multiFunc(10, 8, (Integer x) -> x + 2) ); // 120
    }
}
```
