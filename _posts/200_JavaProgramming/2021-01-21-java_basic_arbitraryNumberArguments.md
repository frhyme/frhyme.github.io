---
title: Java - Arbitrary Number of Argument
category: java
tags: java java_basic argument function parameter
---

## Java - Arbitrary Number of Argument

- java에서 method를 정의할 때, 변수가 몇 개 들어오더라도 문제없이 처리해주도록 하려면 `...`을 이용하면 됩니다.
- 가령 다음처럼 `String...`로 정의할 경우 String argument가 몇 개 들어올지 정해주지 않아도 됩니다. 즉, 1개 들어오든 2개 들어오든 다 array로 생각하고 처리해주게 되죠.

```java
public static void method1(String... ss){
}
```

- 간단히 다음처럼 몇 개의 String이 들어오더라도 다 출력해주는 코드를 만들었습니다.

```java
public class Main {
    public static void printArbitraryStrings(String... ss) {
        for (int i=0; i < ss.length; i++) {
            System.out.printf("String %d: %s \n", i, ss[i]);
        }
    }
    public static void main(String[] args) throws Exception {
        printArbitraryStrings("a");
        System.out.println("====================");
        printArbitraryStrings("a", "b");
        System.out.println("====================");
        printArbitraryStrings("a", "b", "c");
    }
}
```

- 결과는 다음과 같죠. 

```plaintext
String 0: a 
====================
String 0: a 
String 1: b 
====================
String 0: a 
String 1: b 
String 2: c 
```

## Reference

- [Stackoverflow - what do 3 dots next to a parameter type mean in java](https://stackoverflow.com/questions/3158730/what-do-3-dots-next-to-a-parameter-type-mean-in-java)
