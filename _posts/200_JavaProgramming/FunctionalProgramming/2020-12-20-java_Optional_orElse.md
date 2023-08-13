---
title: Java - Optional.orElse
category: java
tags: java programming optional NPE
---

## Java - Optional.orElse

- java에서 `Optional`은 "메서드의 반환 값이 '없음'을 의미적으로 표현할 필요가 있지만, null값으로 반환하고 싶지는 않은 경우"에 사용하기 위해서 만들어졌습니다.
- 이상하죠. 실제로 null은 아니지만, 의미적으로 아무 것도 반환되지 않았다! 라는 것을 확실하게 하기 위해서, null 비슷한 값을 리턴하도록 해준 것이죠.
- 아래 코드에서 보는 것처럼, List의 Stream, `.reduce`를 사용하는 경우 `Optional`을 리턴하게 됩니다. 

```java
// 결과 값이 Optional이죠.
Optional xxx = List.of(1, 2, 3, 4, 5).stream()
                .map((Integer x) -> x * x)
                .reduce((Integer x1, Integer x2) -> x1 + x2);
// Optional이므로 값을 확인하려면 .get()을 사용해야 합니다.
// 다만 이 경우 null이 리턴될 수도 있죠.
System.out.println(xxx.get());
// 따라서, orElse를 사용해서 null인 경우 매치되는 값이 무엇인지도 함께 표현해줍니다.
System.out.println(xxx..orElse(0));
```
