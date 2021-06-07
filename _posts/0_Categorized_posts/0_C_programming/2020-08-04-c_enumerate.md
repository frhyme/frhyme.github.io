---
title: C에서 enum 사용하는 이유
category: C_programming
tags: C programming macOS C_programming
---

## Why Enum?

- 일반적으로 코드에서 상수를 정의할 때는 다음과 같이 사용하죠. `const`를 사용해서 해당 값이 바뀌지 않도록 선언해주고, 값을 정의해줍니다. 이렇게 쓰면, 프로그래밍 중에 늘 `3.141592`를 쓰는 것이 아니라, 그냥 `PI`만을 써서 처리해줄 수 있죠. 물론, 상수로 처리하지 않고 그냥 써도 되지만, 어느 쪽이 더 error-prone한지는 굳이 설명할 필요가 없을 것 같아요.

```c
const double PI = 3.141592;
```

- 상수는 단지 `PI`와 같은 복잡한 수를 정의하기위해서만 사용되는 것이 아니며, 코드를 좀 더 가독성을 높여서 작성하기 위해서도 쓰일 수 있습니다.
- 가령 4가지 방향(동서남북)에 따라서 서로 다른 명령을 수행해야 한다고 해보겠습니다. 코드는 대략 다음과 같아지겠죠. 
- 이 코드는 큰 문제는 없지만, 주석과 코드가 따로 존재한다는 점에서 좀 아쉬움이 있죠. 의미는 주석에 담겨 있고, 수행은 코드에 담겨 있으므로 잘못하다가 주석과 코드가 분리되면 혼동이 발생될 수 있습니다.

```c
/*
east = 0, west = 1, north = 2, south = 3
*/
int direction = 0;
switch (direction){
    case 0:
        printf("This is east");
        break;
    /* 생략 */
}
```

- 따라서 코드를 조금 고쳐 보겠습니다. 아래 코드에서는 방향에 지정될 수 있는 4가지 종류의 값을 모두 상수로 처리하여 만들어 두었습니다. 따라서, 값을 비교할 때, 상수와 직접 비교를 하면 되죠. 
- 이 코드는 이전 코드에 비해서 가독성은 좋아졌지만, 쓸데없이 코드가 4줄이나 추가되었죠. 더불어, 만약 방향뿐만이 아니라, 월(January, ..., ), 요일(Monday, ...) 등 다양한 분기점들이 늘어난다면, 그에 비례해서 코드의 줄 수가 증가합니다. 그리고 코드의 줄 수가 증가하면 당연히 비효율성이 증가하죠.

```c
#include <stdio.h>

int main(void){
    const int EAST  = 0;
    const int WEST  = 1;
    const int NORTH = 2;
    const int SOUTH = 3;

    int direction = WEST;

    switch (direction){
        case EAST:
            printf("This is east");
            break;
        case WEST:
            printf("This is west");
            break;
        /* 생략 */
        default: 
            printf("This is default");
            break;
    }
}
```

- `enum`을 사용해서 다음과 같이, 코드를 좀 더 간결하게 표현해 보겠습니다.
- 아래 코드를 통해서, 새로운 enum 변수 타입을 정의해줍니다. 이 변수타입은 `EAST, WEST, SOUTH, NORTH`라는 4가지 유형의 값들만을 가질 수 있습니다. 동시에, `EAST`, `WEST`, `SOUTH`, `NORTH`를 모두 상수로서 선언 및 정의했다고 봐도 됩니다. 즉 이전에 사용한 코드와 완벽하게 동일하다는 것이죠.

```c
// 열거형 타입을 정의: 순서대로 0, 1, 2, 3의 값이 지정됨
// 즉 모두 상수로서 표현되었다고 보면 됨.
enum DIRECTION {EAST, WEST, SOUTH, NORTH}; 
```

- 그 다음, 해당 타입에 속하는 변수를 선언하고, 적합한 값을 지정해줍니다.

```c
enum DIRECTION curr_direction; 
curr_direction = EAST; // //열거형 타입 변수에 값을 지정
```

- 전체 코드를 보면 대략 다음과 같아지죠. 어떤가요? 저는 이전에 비해서 코드가 더 깔끔해졌다고 생각합니다. 
- 관련 있는 상수들을 한번에 선언하여 코드의 줄 수가 짧아졌고, 해당 상수를 필요로 하는 변수 또한 정의하여 해당 변수가 어떤 값을 가지는지에 대해서 코드만으로 쉽게 이해할 수 있죠.

```c
#include <stdio.h>

int main(void){
    // 열거형 타입을 정의: 순서대로 0, 1, 2, 3의 값이 지정됨
    enum DIRECTION {EAST, WEST, SOUTH, NORTH}; 
    //열거형 타입 변수를 선언.
    enum DIRECTION curr_direction; 
    curr_direction = EAST; // //열거형 타입 변수에 값을 지정
    printf("%d", EAST);

    switch (curr_direction){
        case EAST:
            printf("This is east\n");
            break;
        case WEST:
            printf("This is west\n");
            break;
        default:
            printf("This is default\n");
            break;
        /* 생략 */
    }
}
```

### 하지만

- 그러나, C에서의 `enum`은 다른 문제점들을 가지고 있기도 합니다. `curr_direction`의 자료형에 따르면, 이 아이는 `EAST`, `WEST`, `SOUTH`, `NORTH` 4가지 값만 가져야 하지만, 다른 값을 넣어도(가령 4 혹은 5) 컴파일 단계에서 에러를 잡아주지 못합니다.
- 또한, 비슷한 이야기지만, C는 고유의 자료값을 가지는 것이 아니라, 0부터 순차적으로 증가하는 값을 그냥 넣어줍니다. 따라서, 서로 다른 열거자료형일지라도 첫번째 값이면 무조건 0이고, 이는 서로 다른 자료형을 비교해도 트루로 나온다는 것이죠.
- 즉, 다음과 같은 코드를 작성해도 문제없이 돌아갑니다(물론 warning 정도는 발생하기는 합니다).

```python
#include <stdio.h>

int main(void){
    // 열거형 타입을 정의: 순서대로 0, 1, 2, 3의 값이 지정됨
    enum DIRECTION {EAST, WEST, SOUTH, NORTH}; 
    enum DAY {MON, TUE, WED, THU, FRI, SAT, SUN};

    enum DIRECTION CurrDir = EAST;
    enum DAY CurrDay = MON;

    if (CurrDir==CurrDay){
        printf("This is True\n");
    }

    return 0;
}
```

## wrap-up

- 예전에는 `enum` 자료형을 써야 하는 이유를 잘 알지 못했는데, 이제는 약간은 알것 같네요.
- 다만, C에서는 앞서 말한 것처럼 몇 가지 문제점이 있습니다(물론 warning 단계에서 잡아주기는 합니다만, 그건 컴파일러 디펜던트).
- 찾아보니 언어별로 `enum`을 정의하는 방식이 조금씩 다른 것 같은데, 그건 제가 추후에 더 알아보도록 하겠습니다.
