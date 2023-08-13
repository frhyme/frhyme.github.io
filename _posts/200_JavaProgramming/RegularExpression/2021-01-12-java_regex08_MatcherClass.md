---
title: Java - Regex - Matcher Class
category: java
tags: java regex programming String pattren Matcher
---

## Java - Regex - Matcher Class

- Java에서 `Pattern`, `Matcher`를 사용해서, String 내에 존재하는 pattern은 순차적으로 찾고 출력하는 방법을 정리하였습니다.

```java
package com.company;

import java.util.*;
import java.util.regex.Pattern;
import java.util.regex.Matcher;

class Main {
    public static void main(String[] args) throws Exception {
        String targetStr = "superman batman spiderman ironman blackpanther";

        Pattern pattern = Pattern.compile("[\\w]+man", Pattern.CASE_INSENSITIVE);
        Matcher matcher = pattern.matcher(targetStr);

        // Matcher().find()는 존재하는지를 boolean으로 리턴합니다.
        // 보다 정확하게는 targetStr의 처음부터 읽어가면서, match하는 pattren이 나오면
        // 그 위치에서 멈추고 true를 리턴합니다.
        // 그 다음에 다시 .find()를 콜하면 그 뒤부터 읽는 것이죠.
        boolean patternExist = matcher.find();
        System.out.println(patternExist); // true

        // .start(): pattern의 첫번재 index를 리턴합니다.
        // .end(): 마지막으로 존재하는 index를 리턴합니다.
        int patternFirstIndex = matcher.start(); // 0
        int patternLastIndex = matcher.end(); // 8
        // 따라서, 아래와 같이 subString으로 출력하면,
        // 찾은 pattern이 어떤 string인지 나오게 되죠.
        String matchedStr = targetStr.substring(patternFirstIndex, patternLastIndex);
        System.out.println(matchedStr); // superman
        // 그냥 .group를 사용해서 찾아도 됩니다.
        String matchedStrByGroup = matcher.group();
        System.out.println(matchedStrByGroup); // superman

        // Iterating over Multiple Matches
        // 아래와 같이 순차적으로 찾을 수도 있죠.
        System.out.println("====================================");
        while(true) {
            // .find()를 통해 순차적으로 찾고
            if (matcher.find() == true) {
                // .group(()을 통해 찾아진 애를 String으로 만들어서 출력합니다
                String eachMatchStr = matcher.group();
                System.out.printf("Matched String: %s \n", eachMatchStr);
                // String: batman
                // String: spiderman
                // String: ironman
            } else {
                break;
            }
        }
        System.out.println("====================================");
    }
}
```
