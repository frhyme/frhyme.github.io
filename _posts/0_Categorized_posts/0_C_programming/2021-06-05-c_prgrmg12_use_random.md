---
title: C - random 
category: C_programming 
tags: C_programming c random 
---

## C - random

- c에서는 `rand()` 함수를 사용해서, 랜덤 값을 가져올 수 있습니다.
- `srand()`를 사용하면 난수를 만드는 첫번째 값을 조정할 수 있죠. 그냥, seed 값이 같으면, '난수 발생 순서가 같다'라고 이해하셔도 됩니다.

```c
#include <stdio.h>
#include <stdlib.h>

int main(void) {
    int seed = 10;
    srand(seed);
    for (int i=0; i < 10; i++) {
        printf("%d \n", rand());
    }

    return 0;
}
```
