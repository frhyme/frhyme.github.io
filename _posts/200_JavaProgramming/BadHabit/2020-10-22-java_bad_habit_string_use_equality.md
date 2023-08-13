---
title: Java - String - 값을 비교할 때는 equals method를 사용해야 함
category: java
tags: java String equality comparison programming
---

## Java - String 값을 비교할 때는 equals method를 사용해야 함

- 두 변수를 비교할 때는 두 가지 방법이 있습니다.
  - `reference equality`: 두 변수의 주소 값이 같은지 확인하는 방법
  - `value equality`: 두 변수의 값이 같은지를 확인하는 방법.
- 읿반적으로 '객체'라면 기본 operator인 `==`가 value check로 사용되는 것이 아니라, reference check로 사용되고, primitive type이라면 `==`가 value check로 사용됩니다.
- 그리고 java에서는 보통 `==`를 사용하면 reference check로 사용됩니다.
- 따라서, 다음 코드에서는 두 String인 `str1`과 `str2`의 값이 같지만 `==`를 사용하는 경우는 `false`가 나오고, `.equals`를 사용하는 경우에는 `true`가 나오죠.

```java
String str1 = new String("abc"); 
String str2 = new String("abc"); 

System.out.println(str1 == str2); // false
System.out.println(str1.equals(str2)); // true
```

## Wrap-up

- 사실 이건 python에서도 종종 하는 실수이기는 합니다.
- python에서는 `is`로 값의 주소값을 비교하고, `==`로 값을 비교하죠.
