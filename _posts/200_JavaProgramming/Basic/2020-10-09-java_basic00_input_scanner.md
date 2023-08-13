---
title: Java - Scanner를 이용해서 기본적인 값 입력받기.
category: Java
tags: java programming IntelliJ scanner
---

## Java 기본 입력 - Scanner를 이용해서 값 입력받기

- C에서는 사용자로부터 값을 입력받기 위하여 다음과 같은 코드를 사용합니다.

```C
#include <stdio.h>

int main(void){
    int a;
    // 값을 입력받는 String의 형태를 정의하고
    // 입력받는 String에서 %decimal로 입력받은 값을 변수 a의 주소에 넣어줌.
    scanf("%d", &a);
}
```

- 하지만 java에서는 `java.util.Scanner` 객체를 만들어줍니다. 이 아이는 말 그대로 Stream을 읽어들이는 아이죠.

```java
import java.util.Scanner;

class Main {
    public static void main(String[] args) {
        // 새로운 Scanner 개체를 만들어주고, 
        // 초기화 할때 System.in 을 넣어줌으로써 시스템 기본 입출력에서 값을 가져온다는 것을 명확하게 한다.
        Scanner scanner = new Scanner(System.in);
        // .next() 는 단어 하나를 읽는 경우
        String w1 scanner.next(); 
        // .nextLine() 는 줄을 읽는 경우
        String w1 scanner.nextLine(); 
    }
}
```

## Java 기본 입력 - Scanner를 이용해서 정수 값 입력받기

- 이전에는 `java.util.Scanner`의 method인 `.next()`를 사용했는데, 이렇게 할경우 입력받는 값이 무조건 "문자열"이 됩니다.
- `.nextInt()`를 이용하면, 정수를 입력받을 수 있습니다.
  - 물론, 그냥 문자열을 입력받은 다음, 이 아이를 정수로 바꾸어주는 형태도 가능하죠.

```java
package com.company;

import java.util.Scanner;

public class Main {

    public static void main(String[] args) {
        // System.in(시스템 기본 입력)으로부터 값을 읽어오는 놈
        Scanner scanner = new Scanner(System.in);
        int myAge = scanner.nextInt();
        System.out.println(
                String.format("My age is %d", myAge)
        );
    }
}
// End of Code
```
