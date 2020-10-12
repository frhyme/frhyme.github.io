---
title: 
category: 
tags: 
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