---
title: Java - Boolean 값과 int는 다르다.
category: java
tags: java programming boolean int
---

## Java - Boolean이과 int는 다르다

- C로 코딩을 해본 적 있으신 분들은 아시겠지만, C에서는 `True`, `False`의 값이 따로 존재하지 않습니다. 0이면 False, 1이면 True죠.
- 딱히 문제가 없다고 느낄 수도 있지만, Boolean은 logical한 값이고, 0이나 1은 integer입니다. 이 둘을 명확히 구분해서 프로그래밍하지 않으면, error-prone한 상황이 발생할 수 있어요.
- 따라서, java에서는 이것이 구분되어 있죠. 가령 다음과 같은 코드가 실행될 수 없습니다.

```java
// java: incompatible types: int cannot be converted to boolean
if (1) {
    System.out.println("dd");
}
```

- 아래처럼, `true`, `false`가 들어와야죠.

```java
if ( true ){
    System.out.println("dd");
}
```

## Wrap-up

- 쓰고 나니 별거 없지만, 이 구분은 매우 중요합니다. 논리값(logical value)와 정수 값은 아예 다른 개념입니다. 접근 법 자체가 다르죠.
- C에서 아쉬운 점이 이 점인데, 이 둘의 구분이 미묘해서, 잘못하면 `if(1)`와 같은 형태로 프로그래밍을 하게 되죠. "에이 누가 이런 실수를 하냐?"싶지만, 그런 작은 실수조차 허용되지 않도록 하는 것이, 좋습니다. 생각보다 빡빡하게 프로그래밍 하도록 강제할수록 프로그래머는 좋은 코딩 습관을 가지게 되니까요.