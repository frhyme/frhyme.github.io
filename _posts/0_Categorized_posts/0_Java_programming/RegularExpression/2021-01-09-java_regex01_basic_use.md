---
title: Java - Regular Expression - Basic
category: java
tags: java programming string regex
---

## Java - Regular Expression - Basic

- 정규표현식은 "특정한 패턴을 사용해서 문자를 검색하는 방식"이죠. 
- Java에는 String에서 정규표현식(Regular Expression)을 기본적으로 지원합니다.
- 다음과 같이 아주 간단하게 pattern을 찾는 방법을 정리하였습니다.
  - `.`: 공백을 포함한 character
  - `<char>?`: `char`가 있거나 없거나

```java
class Main {
    public static void main(String[] args) throws Exception {
        System.out.println("===============");

        // .matches: 전체 문자열이 정확하게 일치하는지 확인함.
        // str1.matches(regex_str2):
        // str1이 regex_str2에 표현된 정규 표현식을 의미하는지 찾아서
        // 정확히 같으면 true, 아니면 false를 리턴합니다.

        System.out.println("== Pattern 1 ==============");
        // .: 공백을 포함한 character
        String pattern1 = "al.";
        // "al." 패턴은 al과 문자 1개(공백 포함)이 있는 경우를 찾습니다.
        System.out.println("Pale".matches(pattern1)); // false
        System.out.println("ale".matches(pattern1)); // true
        System.out.println("alx".matches(pattern1)); // true
        System.out.println("al ".matches(pattern1)); // true

        System.out.println("== Pattern 2 ==============");
        // <char>?: char이 있거나, char이 없거나.
        // 아래 pattern2에서 u?는 u가 있거나 없거나 모두 true라고 결론을 내린다는 이야기죠.
        String pattern2 = "colou?r";
        System.out.println("colour".matches(pattern2)); // true
        System.out.println("color".matches(pattern2)); // true

        System.out.println("== Pattern 3 ==============");
        // \\<specialChar>: . ? 와 같이 특수문자가 있는지 확인
        String pattern3 = "abc\\.";
        System.out.println("abc.".matches(pattern3)); // true
        System.out.println("abcd".matches(pattern3)); // false

        System.out.println("== Pattern 4 ==============");
        // \ backsalsh가 있는지 확인하려면 다음과 같이 regex에서 4개 써줘야 합니다.
        // string 자체에서도 1개로 쓰지 않고 2개로 쓰기 때문에, regex에서는 4개를 써야 하는 거죠.
        String pattern4 = "..\\\\";
        System.out.println("ab\\".matches(pattern4)); // true
        System.out.println("ab".matches(pattern4)); // false
    }
}
```
