---
title: Java - Regular Expression - Quantifier
category: java
tags: java programming string regex string
---

## Java - Regular Expression - Quantifier

- 정규표현식에서 특정문자가 몇개 반복되는지 파악하는 방법을 설명합니다.

```java
import java.util.*;

class Main {
    public static void main(String[] args) throws Exception {
        /*
        + 는 1번 이상의 등장을 말하고,
        * 는 0번 이상의 등장을 말하고,
        {n}는 정확히 n번의 등장을 말하고,
        {n, m}는 n번 이상 m번 이하의 등장을 말하고,
        {n,}는 n번 이상의 등장을 말하고,
        {0, m}은 m번 이하의 등장을 말합니다.
        */

        String pattern1 = "a+";
        System.out.println("a".matches(pattern1)); // true
        System.out.println("aa".matches(pattern1)); // true
        System.out.println("aaa".matches(pattern1)); // true
        System.out.println("=================================");

        String pattern2 = "a*";
        System.out.println("".matches(pattern2)); // true
        System.out.println("a".matches(pattern2)); // true
        System.out.println("aa".matches(pattern2)); // true
        System.out.println("=================================");

        String pattern3 = "a{2}b";
        System.out.println("aab".matches(pattern3)); // true
        System.out.println("aaab".matches(pattern3)); // false
        System.out.println("=================================");

        String pattern4 = "a{1,3}b";
        System.out.println("ab".matches(pattern4)); // true
        System.out.println("aab".matches(pattern4)); // true
        System.out.println("aaab".matches(pattern4)); // true
        System.out.println("aaaab".matches(pattern4)); // false
    }
}
```
