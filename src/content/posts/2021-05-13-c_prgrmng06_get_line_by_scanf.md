---
title: "C - get line by scanf"
date: 2021-05-13
category: "c-programming"
tags: ["c", "programming", "c_programming", "scanf"]
permalink: "/c_programming/c_prgrmng06_get_line_by_scanf/"
---

- scanf를 사용하여 한 line을 그대로 입력받으려면 다음처럼 처리하면 됩니다.
- `%[^\n]`: `\n`이 아닌 char만 입력을 받겠다는 것을 의미합니다. 따라서, `\n`이 입력되면 입력을 멈추게 되죠.

```c
#include <stdio.h>

int main(void) {
    const int max_str_size = 100;
    char s[max_str_size];
    
    scanf("%[^\n]", s);
    
    printf("%s\n", s);
}
```