---
title: Java - Regex - Replacing Patterns
category: java
tags: java regex programming String pattren 
---

## Java - Regex - Replacing Patterns

- Java에서 Regex를 사용해서 regex pattern에 속하는 string을 replace합니다.

```java
import java.util.*;
import java.util.regex.Pattern;
import java.util.regex.Matcher;

class Main {
    public static void main(String[] args) throws Exception {
        // 간단하게 숫자(digit)를 # 으로 바꿔 봅니다.
        // String에서 바로 사용할 수 있죠.
        String regexPattern = "\\d";
        String targetStr = "010-1234-5678";
        // .replaceAll 을 사용해서 바꿀 수 있습니다.
        String replacedStr = targetStr.replaceAll(regexPattern, "#");
        System.out.println(replacedStr);
        // .replace 를 사용해서 첫번째 regex만 바꿀 수도 있습니다.
        System.out.println(targetStr.replaceFirst(regexPattern, "#"));
        System.out.println("--------------------------------");

        // Pattern, Matcher를 사용해서 바꿀 수도 있죠.
        Pattern pattern = Pattern.compile("\\d"); // a regex to match a digit

        String targetStr1 = "010-9876-5432";
        Matcher matcher = pattern.matcher(targetStr1);

        System.out.println(matcher.replaceAll("#"));
        System.out.println(matcher.replaceFirst("#"));
        System.out.println("--------------------------------");
    }
}
```
