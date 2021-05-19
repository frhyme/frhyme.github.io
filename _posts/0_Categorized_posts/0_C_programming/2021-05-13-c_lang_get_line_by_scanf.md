---
title: C - get line by scanf
category: C_programming
tags: C programming C_programming C scanf
---

## C - get line by scanf

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
