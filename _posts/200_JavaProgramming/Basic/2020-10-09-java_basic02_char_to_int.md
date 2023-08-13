---
title: Java - Char를 Int로 변환하기
category: Java
tags: java programming IntelliJ Char Int
---

## Java - Char를 Int로 바꾸기

- python에서는 만약 string, char등을 숫자로 바꾼다면, 다음처럼 하면 끝납니다. 우선 '문자열(String)'과 '문자(char)'간 차이도 없죠.

```python
s1 = "4"
int(s1) // 4 
```

- java에서는 이런 방식의 형 변환이 되지 않습니다. 그리고 String, Char에 따라 방법이 다른데, 여기서는 Char을 Int로 변환하는 방법에 대해서만 정리하겠습니다. 

## Char to Int - Ascii code 사용

- 컴퓨터는 문자를 기억할 수 없기 때문에, 숫자 번호에 문자를 연결하여 기억합니다. 가령 숫자 0은 문자 A, 숫자 1은 문자 B 이런 식으로요.
- Ascii code는 초기에 만들어진 숫자 - 문자 매핑 테이블이라고 생각하시면 됩니다.
- 문자 `'0'`의 아스키코드는 48이고, 문자 `'9'`의 아스키코드는 57이죠. 하나씩 커지는 셈입니다.
- 즉, 다음처럼 아스키 코드를 이용해서 연산을 해버리면 char를 Int로 변환한 것과 동일한 결과가 나오게 되죠.

```java
char c1 = '9';
int i1 = c1 - '0'; // 57 - 48 = 9
```

- `Character.getNumericValue(c1)`를 사용해서 처리하는 방법도 있습니다.

```java
char c1 = '9';
Character.getNumericValue(c1) // 9 
```
