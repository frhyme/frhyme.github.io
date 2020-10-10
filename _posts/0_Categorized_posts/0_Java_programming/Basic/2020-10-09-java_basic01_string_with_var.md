---
title: Java - 문자열에 변수를 넣어서 함께 출력
category: Java
tags: java programming IntelliJ String
---

## Java 기본 출력

- 이번에는 값을 출력할 때 변수와 함께 출력하는 방법을 알아보겠습니다.
- C에서는 다음과 같이 하고.

```C
int a = 10;
printf("%d", a);
```

- python에서는 다음과 같이 하죠.

```python
a = 10
printf(f"{a}")
```

- java에서는 다음과 같이 합니다.

```java
public class Main {
    public static void main(String[] args) {
        // System.in(시스템 기본 입력)으로부터 값을 읽어오는 놈
        String myName = "frhyme";
        System.out.println(
                // String.format() 을 만들어서, parameter를 넣어줌.
                // 사실 이 아이는 새로운 sentence라는 변수를 만들어서 값을 넣어주고 출력하는 것과 비슷하죠.
                // String sentence = String.format("My name is %s", myName);
                String.format("My name is %s", myName)
        );
    }
}
// End of Code
```

- 개념적으로 같은 코드이지만, 이해를 돕기 위해 다음처럼 풀어서 설명하겠습니다.
  - 변수 `myName`을 문자열에 넣는 것이기 때문에, 변수를 넣어줄 새로운 문자열인 `mySentence`를 만들고, 
  - `mySentence`의 format을 정의해서 어느 부분에 `myName`을 넣어줄지 정합니다.

```java
public class Main {
    public static void main(String[] args) {
        // System.in(시스템 기본 입력)으로부터 값을 읽어오는 놈
        String myName = "frhyme";
        String mySentence = String.format("My name is %s", myName);

        System.out.println(mySentence);
    }
}
```
