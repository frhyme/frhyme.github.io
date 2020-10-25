
## Java - enum

- 

## C - enum


```c
#include <stdio.h>

int main(void){
    // 열거형 타입을 정의: 순서대로 0, 1, 2, 3의 값이 지정됨
    enum DIRECTION {EAST, WEST, SOUTH, NORTH}; 
    enum DAY {MON, TUE, WED, THU, FRI, SAT, SUN};

    enum DIRECTION CurrDir = EAST;
    enum DAY CurrDay = MON;

    // C에서는 enum 으로 자료형을 정의해도, 각 값에 Integer 값이 mapping됨.
    // CurrDir과 CurrDay는 서로 다른 enum 자료형에 존재하지만, 모두 0, 1의 값을 가지고 있음
    // 따라서, 의미적으로는 아래 코드에 문제가 있지만, logical value가 true로 나오게됨.
    if (CurrDir==CurrDay){
        printf("This is CurrDir==CurrDay\n");
    }

    printf("EAST: %d\n", EAST); // 0 
    printf("MON : %d\n", MON); // 0 
    

    return 0;
}
```