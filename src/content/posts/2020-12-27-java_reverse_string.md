---
title: "Java - StringBuilder를 사용하여 String Reverse"
date: 2020-12-27
category: "java"
tags: ["java", "programming", "string", "StringBuilder"]
permalink: "/java/java_reverse_string/"
---

- `StringBuilder`를 사용하여 `String`을 Reverse해줍니다.

```java
String targetStr = "abcde";
String reversedStr = new StringBuilder(targetStr).reverse().toString();

System.out.println(reversedStr); // edcba
System.out.println(targetStr.equals(reversedStr)); // false
```