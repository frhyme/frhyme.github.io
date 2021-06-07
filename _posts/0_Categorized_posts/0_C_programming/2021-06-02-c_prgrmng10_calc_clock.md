---
title: C - 연산 시간을 계산해봅시다 
category: C_programming
tags: C programming C_programming C time clock_t
---

## C - 연산 시간을 계산해봅시다 

- C에서 특정 코드의 연산 시간을 계산하려면, `time.h`에 있는 함수 `clock()`를 사용하면 됩니다.

```c
#include <stdio.h>
#include <time.h>
#include <stdlib.h>

int main(void) {
    // time.h에 정의되어 있음.
    // clock_t는 unsigned long
    clock_t start1;
    clock_t end1;

    // CLOCKS_PER_SEC: 1000000
    printf("CLOCKS_PER_SEC: %d \n", CLOCKS_PER_SEC);
    start1 = clock();
    int r = 0; 
    printf("start: %lu \n", start1);
    for (int i=0; i < 1000000; i++) {
        r += i;
    }
    end1 = clock(); 
    printf("end  : %lu \n", end1);
    printf("== elapsed time: %lu clocks \n", end1 - start1);
    printf("== elapsed time: %f seconds \n", (float)(end1 - start1) / CLOCKS_PER_SEC);
}
```
