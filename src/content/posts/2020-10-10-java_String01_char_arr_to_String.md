---
title: "java - Char array를 String으로 변환하기"
date: 2020-10-10
category: "java"
tags: ["java", "String", "char", "array"]
permalink: "/java/java_String01_char_arr_to_String/"
---

## java - char array를 String으로

- char array를 String으로 변환하기 위해서는 아래와 같이 `String.valueOf()` 메소드를 사용해야 합니다.

```java
char[] charArr = {'1', '2', '3'};
// String.valueOf
String str1 = String.valueOf(charArr); // "123"
```