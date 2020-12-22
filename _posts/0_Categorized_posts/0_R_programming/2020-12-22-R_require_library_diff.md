---
title: R - library와 require의 차이
category: R_programming
tags: R R_programming library require
---

## R - library와 require의 차이

- R에서는 library를 import하는 방법으로 `require`, `library`라는 두 가지 방법이 있습니다.
- 기본적으로 둘 다 필요한 라이브러리를 가져온다는 점에서는 같지만,
  - `library()`의 경우 만약 해당 라이브러리가 설치되어 있지 않다면 오류를 발생시키며 프로그램이 멈추고,
  - `require()`의 경우 설치되어 있지 않을 경우 Warning을 발생시키고 일단은 실행됩니다. 그리고 성공하면 `TRUE`를 실패하면 `FALSE`를 리턴하죠.
- 따라서 저는 보통 다음의 형식으로 코딩합니다. 패키지가 존재하지 않으면 `install.packages()`를 통해 패키지를 다운받습니다.

```R
if ( require("ggplot2") ) {
    # TRUE: The library Exists
    print("TRUE: The library Exists")
} else {
    # FALSE: The library Doesn't exist
    print("FALSE: The library Doesn't exist")
    install.packages("ggplot2")
}
```
