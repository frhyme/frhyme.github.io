---
title: "C - malloc example"
date: 2021-05-10
category: "C_programming"
tags: ["C", "programming", "C_programming", "malloc"]
permalink: "/c_programming/c_prgrmng04_malloc/"
---

## C - malloc example

- `malloc`을 간단하게 사용해 봤습니다.
- 저는 사실 `malloc`보다는 `calloc`이 더 편해요 호호

```c
#include <stdio.h>
#include <stdlib.h>

int main(void) {
    int* p;
    int l = 5; 
    p = malloc(sizeof(int) * l); 
    for (int i = 0; i < l; i++) {
        *(p + i) = i;
    }
    for (int i=0; i < l; i++) {
        printf("%d\n", *(p + i));
    }
    printf("===\n");
    /*
    0
    1
    2
    3
    4
    ===
    */
}
```