---
title: Java - Regex - Conditional 
category: java
tags: java regex condition programming String
---

## Java - Regex - Conditional 

- Regex에서도 문자열의 패턴에 따라 if statement를 구성할 수 있습니다.
- 아래 코드에서는 일반적인 시간 표시(`15:56`)과 같은 시간만 유효하도록 판단하는 regex를 만들었습니다.

```java
import java.util.*;

class Main {
    public static void main(String[] args) throws Exception {
        /*
        String regex = "^([0-1]{1}?[0-9]|2[0-3]):[0-5][0-9]";
        */
        /*
        regex 내에서 if를 사용하려면 다음처럼 사용해야 합니다.
        ^(<condition> ? <trueResult>|<falseResult>)
        - 일단 ^으로 시작하고 양쪽을 ()로 열고 닫아 줍니다.
        - <condition>: 넣고 싶은 조건을 넣습니다.
        - <trueResult>: 조건이 충족될 경우의 조건을 넣습니다.
        즉 이 경우에는 condition+trueResult pattern인지 확인하는 것이겠죠.
        - <falseResult>: 조건이 충족되지 않을 경우의 조건을 넣습니다.
        이 경우에는 falseResult pattern인지 확인하는 것이죠.
        */
        /*
        === Example1 ========================================
        - 시간을 표시하는 23:59와 같은 패턴인지 확인합니다.
        시간의경우 00부터 09, 10부터 19까지 모두 가능하지만,
        앞에 2가 나오게 되면 0-3까지만 가능하죠.
        - condition: [0-1]{1}, [0-1]이 1번 나오면
        - trueResult: [0-9], [0-9]까지 모두 가능하다.
        - falseResult: 아니면([0-1]이 1번 나오지 않으면)
        2[0-3] 패턴이 등장한다.
        */
        String regexConditional = "^([0-1]{1}?[0-9]|2[0-3])";
        String otherRegex = ":[0-5][0-9]";
        String pattern1 = regexConditional + otherRegex;

        System.out.println("00:01".matches(pattern1)); // true
        System.out.println("00:59".matches(pattern1)); // true
        System.out.println("23:01".matches(pattern1)); // true
        System.out.println("24:00".matches(pattern1)); // false
        System.out.println("24:00".matches(pattern1)); // false
    }
}
```
