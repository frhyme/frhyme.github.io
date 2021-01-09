---
title: Java - Regular Expression - Set, Range, Except
category: java
tags: java programming string regex
---

## Java - Regular Expression - Set, Range, Except

- Regex를 사용하여 유효한 문자들에 대해서 범위를 지정하는 방법을 정리합니다.
  - `[]`: 유효한 문자 그룹을 지정합니다.
    - ex) `[abc]`: a, b, c 유효
  - `[1-9]`: `-`를 사용하여 유효한 문자들을 범위로 지정합니다. 1부터 9까지 허용
  - `[^abc]`: `^`를 사용하여 유효하지 않은 문자를 지정합니다. 이 regex는 abc 말고 다른 문자들을 허용한다는 표현이죠.
  - `(m|t|sh)`: 문자가 아니라 여러 문자에 대해서 유효하도록 지정하는 방식입니다.

```java
import java.util.*;

class Main {
    public static void main(String[] args) throws Exception {

        /*
        유효한 캐릭터를 개별적으로 허용
        []: []안에 있는 char만 허용한다는 것을 의미합니다.
        ex) [ab]: a 혹은 b가 있는 경우 true로 판정한다는 이야기죠.
        * */
        String pattern1 = "[abc]xxx";
        System.out.println("axxx".matches(pattern1)); // true
        System.out.println("bxxx".matches(pattern1)); // true
        System.out.println("cxxx".matches(pattern1)); // true
        System.out.println("dxxx".matches(pattern1)); // false

        String pattern2 = "[ab]x[yz]";
        System.out.println("axz".matches(pattern2)); // true
        System.out.println("axw".matches(pattern2)); // false

        System.out.println("========================");
        System.out.println("========================");

        /*
        유효한 캐릭터를 범위로 지
        - [1-9]와 같이 범위로 지정할 수도 있습니다.
        - [a-z], [a-zA-Z]도 가능하죠.
        * */
        String pattern3 = "[0-9][a-z][A-Z]";
        System.out.println("0aA".matches(pattern3)); // true
        System.out.println("9aZ".matches(pattern3)); // true
        System.out.println("9zZ".matches(pattern3)); // true
        System.out.println("9Zz".matches(pattern3)); // false
        System.out.println("========================");

        String pattern4 = "[0-9][a-z.?][A-Z]";
        System.out.println("0.A".matches(pattern4)); // true
        System.out.println("0?A".matches(pattern4)); // true
        System.out.println("========================");

        /*
        유효하지 않은 캐릭터를 지정하기
        ^ 를 사용해서 유효하지 않은 것을 지정할 수 있습니다.
        [^abc]: a, b, c의 경우 유효하지 않다는 것을 의미합니다.
        [^0-8]: 0 - 8 까지 모두 유효하지 않다고 정의합니다.
        */
        String pattern5 = "[^abc]XX";
        System.out.println("aXX".matches(pattern5)); // false
        System.out.println("dXX".matches(pattern5)); // true
        System.out.println("========================");
        String pattern6 = "[^1-8]XX";
        System.out.println("1XX".matches(pattern6)); // false
        System.out.println("9XX".matches(pattern6)); // true
        System.out.println("0XX".matches(pattern6)); // true
        System.out.println("========================");

        /*
        | : 여러 문자열에 대해 OR 조건을 걸 수 있습니다.
        (m|t|sh): m, t, sh 중 하나라도 속하면 됨.
        문자열이 들어가는 경우에는 []가 아니라, ()를 사용해야 합니다.
        */
        String pattern7 = "(m|t|sh)ake";
        System.out.println("make".matches(pattern7)); // true
        System.out.println("shake".matches(pattern7)); // true
        System.out.println("cake".matches(pattern7)); // false
        System.out.println("========================");
    }
}
```
