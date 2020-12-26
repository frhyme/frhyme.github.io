---
title: Java - StringBuilder를 사용하여 String Reverse
category: java
tags: java programming string StringBuilder
---

## Java - StringBuilder를 사용하여 String Reverse

- `StringBuilder`를 사용하여 `String`을 Reverse해줍니다.

```java
String targetStr = "abcde";
String reversedStr = new StringBuilder(targetStr).reverse().toString();

System.out.println(reversedStr); // edcba
System.out.println(targetStr.equals(reversedStr)); // false
```
