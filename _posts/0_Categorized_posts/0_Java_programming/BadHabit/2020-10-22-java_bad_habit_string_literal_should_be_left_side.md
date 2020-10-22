---
title: Java - String literal은 equality를 분석할 때 왼쪽에 위치해야 한다.
category: java
tags: java String equality comparison programming
---

## Java - String literal의 equality를 분석할 때는 왼쪽에 위치해야 한다

- 다음과 같은 java의 String을 비교해주는 간단한 코드가 있다고 하겠습니다.
- 언뜻 보기에는 아무 문제가 없어 보이죠.

```java
String str1 = "aa";
if (str1.equals("aa")) { 
    System.out.println("Same Equality");
}
```

- 사실 실제로 실행을 해도 딱히 문제는 없는데, 가끔 아래와 같은 Warning Message가 발생할 때가 있습니다.
- 번역을 하면 말 그대로, "String의 비교분석을 할 때 Literal은 왼쪽에 위치해야 한다"라는 말이죠.

```plaintext
Strings literals should be placed on the left side when checking for equality
```

- 아래와 같이, `null.equals("aa")`가 실행되면, `NullPointerException`이 발생하게 됩니다.

```java
String str1 = null;
if (str1.equals("aa")) {// Exception in thread "main" java.lang.NullPointerException
    System.out.println("dddd");
}
```

## Fixed Code

- 아래와 같이 바꿔 보겠습니다. 
- 이번에는 StringLiteral이 왼쪽에 있고, 오른쪽에는 `null` 값이 들어가게 되었죠.

```java
String nullString = null;
if ("stringLiteral".equals(nullString)) {
    System.out.println("");
} else {
    System.out.println("NullPointerException not occur");
}
```

- 위 코드를 실행하면, NullPointerException이 발생하지 않습니다.
- 방식은 이전의 코드와 동일하지만, 이번에는 Exception으로 인해 프로그램이 종료되지 않고, 문제없이 실행되죠.

## reference

- [sonarsource - java - badPractice](https://rules.sonarsource.com/java/tag/bad-practice/RSPEC-1132)
