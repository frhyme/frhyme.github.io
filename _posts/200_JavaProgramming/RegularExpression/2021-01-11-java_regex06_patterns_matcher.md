---
title: Java - Regex - Pattern, Matcher
category: java
tags: java regex programming String
---

## Java - Regex - Pattern, Matcher

- 사실 이미 java에서 `String`을 사용해서도 regex를 사용할 수 있긴합니다.

```java
String p1 = "abc";
String targetStr = "abc";
targetStr.matches(p1); // true
```

- 그러나, 의미적으로 다음과 동일하죠. 매번 String에서 `.matches`를 호출하는 순간 매번 `Pattern.compile()`를 사용해서 String을 compile하죠. 만약, 해당 pattern이 여러 번 사용된다면, 매번 compile이 발생하는 것이 되므로 매우 비효율적이 됩니다.
- 또한, `String`에서는 그냥 `.matches`를 사용해서 스트링이 완벽하게 같은지를 확인할 수만 있습니다. 그러나, `Matcher`를 사용하면, 좀더 다양한 종류의 method를 사용할 수 있죠.

```java
// pattern을 compile하고
String p1 = "abc";
Pattern pattern1 = Pattern.compile(p1);

// 만든 Pattern 을 Matcher에 넘겨줍니다.
String targetStr = "abc";
Matcher matcher = pattern1.matcher(targetStr);
matcher.matches(); // true;
```

## Example: Pattern, Matcher

- `Pattern`과 `Matcher`를 통해 정규표현식을 사용하는 방법을 정리하였습니다.

```java
package com.company;

import java.util.*;
import java.util.regex.Pattern;
import java.util.regex.Matcher;

class Main {
    public static void main(String[] args) throws Exception {
        // 다음처럼 Pattern, Matcher를 각각 만들어서 처리해도 됩니다만,
        Pattern p1 = Pattern.compile("[Jj]ava");
        String targetStr = "java";
        Matcher m1 = p1.matcher(targetStr);
        boolean result = m1.matches();
        System.out.println(result); // true
        System.out.println("================================");

        // 다음처럼 Pattern에서 바로 불러도 문제가 없습니다.
        // 하지만, 이 경우는 String.matches로 사용하는 것과 같으므로
        // 매번 compile을 하고 처리하기 때문에 비효율적이죠.
        result = Pattern.matches("[Jj]ava", targetStr);
        System.out.println(result); // true
        System.out.println("================================");

        // Pattern.compile을 할때
        // Pattern.CASE_INSENSITIVE 를 함께 넘겨주면
        // 대소문자 상관없이 처리하도록 할 수 있습니다.
        Pattern patternCaseInsensitive = Pattern.compile(
                "Java", Pattern.CASE_INSENSITIVE);
        System.out.println(
                patternCaseInsensitive.matcher("JAVA").matches()
        ); // true

        System.out.println(
                patternCaseInsensitive.matcher("JaVa").matches()
        ); // true
        System.out.println("================================");

        // 그 외로 Matcher의 경우 .find method도 가지고 있습니다.
        // .matches는 대상 문자열이 정확히 regex 패턴을 따르는지 확인하지만,
        // .find는 대상 문자열 내에 regex 패턴이 존재하는지를 확인하죠.
        String patterStr1 = "[Jj]ava";
        String targetStr1 = "This is Java";

        Pattern pattern2 = Pattern.compile(patterStr1);
        Matcher matcher2 = pattern2.matcher(targetStr1);

        // .matches()는 정확히 같은지 확인하므로 false가 나오지만,
        System.out.println(matcher2.matches()); // false
        // .find()는 regex pattern이 존재하는지 확인하므로 true가 나옵니다.
        System.out.println(matcher2.find()); // true

    }
}
```
