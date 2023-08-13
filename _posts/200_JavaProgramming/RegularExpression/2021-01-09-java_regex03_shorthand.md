---
title: Java - Regular Expression - Shorthand
category: java
tags: java programming string regex string
---

## Java - Regular Expression - Shorthand 

- Regex를 만들 때 가령 숫자만 포함되어야 하는 경우 `[1-9]`처럼 정할 수도 있지만, `\d`와 같이 더 짧게 처리할 수 있는 방법도 있습니다. 그리고 대문자는 `not`을 의미하죠. 그리고, 정규표현식을 만들 때는 `\`를 1개 쓰는게 아니라 `\\`를 써야 인식됩니다.
  - `\d`: 모든 숫자를 말합니다. `[0-9]`와 동일합니다.
    - `\D`: 숫자가 아닌 것, 을 말합니다. `[^0-9]`와 동일합니다.
  - `\s`: tab, newline을 포함한 모든 공백을 말합니다.
    - `\S`: (tab, newline을 포함한 모든 공백문자)가 아닌 것을 말합니다.
  - `\w`: 알파벳과 digit를 모두 포함합니다. 즉 `\d`와 문자 그리고 `"_"`도 포함됩니다. 즉 `[a-zA-Z_0-9]`를 의미하죠.
    - `\W`: `\w`가 아닌 것만 허용합니다.
  - `\b`: 얘는 좀 특이한데, Word Boundary를 의미합니다. 애매한데, 단어와 단어 사이를 구분하는 구분점, 정도로 이해하시는 것이 좋습니다.따라서, `\ba`는 a로 시작하는 단어가 있는지 확인하는 정규표현식이 됩니다.
    - `\B`: 반대죠. 얘는 Word Boundary가 아닌 것을 의미합니다. 따라서, `a\B`는 a로 시작하는 단어가 되죠.

## Regex Example 

- 간단히 테스트를 수행해봤습니다.

```java
package com.company;

import java.util.*;

class Main {
    public static void main(String[] args) throws Exception {
        // \d: 숫자만 유효하다고 판정합니다.
        String pattern1 = "\\dAA";
        System.out.println("1AA".matches(pattern1)); // true
        System.out.println("0AA".matches(pattern1)); // true
        System.out.println("AAA".matches(pattern1)); // false
        System.out.println("=================================");

        // \s: tab, newline을 포함한 모든 공백문자를 말합니다
        // \S: 대문자로 처리하면 not을 의미하므로 공백이 아닌 모든 문자에 대해서 유효처리합니다.
        String pattern2 = "\\s123";
        System.out.println(" 123".matches(pattern2)); // true
        System.out.println("\t123".matches(pattern2)); // true
        System.out.println("\n123".matches(pattern2)); // true

        String pattern3 = "\\SAAA";
        System.out.println("#AAA".matches(pattern3)); // true
        System.out.println(".AAA".matches(pattern3)); // true
        System.out.println("=================================");

        // \w: 숫자, 알파벳, _를 의미합니다.
        String pattern4 = "\\wAA";
        System.out.println("1AA".matches(pattern4)); // true
        System.out.println("_AA".matches(pattern4)); // true
        System.out.println("zAA".matches(pattern4)); // true
        System.out.println("=================================");

        // \b: Word Boundary를 의미합니다.
        // "He is" 문자열에서 "He| |is" |가 있는 위치가 바로 word Boundary죠.
        // 공백도 아니고, 그냥 "구분선"정도로 이해하시면 됩니다.
        // targetStr에서 regex에 따라 is를 are로 바꾸려고 합니다.
        String targetStr = "This dish is, island of miss irish";
        // 첫번째 pattern에서는 \\b를 사용해서 페턴을 만들었고.
        String pattern_with_b = "\\bis\\b";
        // 두번째 pattern에서는 \\s를 사용해서 공백으로 구분하는 패턴을 만들었습니다.
        String pattern_without_b = "\\sis\\s";

        // \\b를 사용하는 경우에는 ,(comma)까지 워드의 구분선으로 이해하고 처리해주지만,
        System.out.println(targetStr.replaceAll(pattern_with_b, "are"));
        // This dish are island of miss irish
        // \\s를 사용하는 경우에는 공백만 이해하므로 구분해서 처리해주지 못하죠. 따라서 결과가 다릅니다.
        System.out.println(targetStr.replaceAll(pattern_without_b, "are"));
        // This dishareisland of miss irish
        System.out.println("=================================");
    }
}
```
