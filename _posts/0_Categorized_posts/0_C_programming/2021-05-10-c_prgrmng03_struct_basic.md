---
title: C - Struct(구조체)
category: C_programming
tags: C programming C_programming C vscode struct
---

## C - Struct(구조체)

- 간만에 C 언어의 struct를 복습해봤습니다.
- struct는 다음과 같이 정의합니다. 아래는 `book1`이라는 변수를 만들어줬는데, 얘는 하위 변수로 `id`, `title`을 가지고 있다는 것을 의미하죠.

```c
struct {
    int id;
    char title[10];
} book1;
```

- 다만, 아래에서 보는 것과 같이, 이렇게 struct를 정의할 경우에는 아래와 같이 매번 변수를 사용할 때마다 정의해줘야 합니다.
- 그리고 자세히 보면, `book1`, `book2`의 하위 변수가 조금 다른 것을 알 수 있죠. 사실 구조체를 각각 저렇게 따로 정의해줘도 상관없기는 한데, 이렇게 할 경우에는 일관성이 없어집니다.

```c
#include <stdio.h>
#include <string.h>

int main(void) {
    struct {
        int id;
        char title[10];
    } book1;
    struct {
        int id;
        char title[20];
        int num;
    } book2;

    book1.id = 20;
    book2.id = 30;

    strcpy(book1.title, "title1");
    strcpy(book2.title, "title2");

    printf("ID: %d, TITLE: %s \n", book1.id, book1.title);
    printf("ID: %d, TITLE: %s \n", book2.id, book2.title);
    // ID: 20, TITLE: title1 
    // ID: 30, TITLE: title2 

    return 0;
}
```

- 따라서, 다음처럼 `typedef`를 사용해서 처리해주는 것이 좋습니다.

```c
#include <stdio.h>
#include <string.h>

typedef struct {
    int id;
    char title[10];
} Book;

int main(void) {
    Book book1;
    Book book2;

    book1.id = 20;
    book2.id = 30;

    strcpy(book1.title, "title1");
    strcpy(book2.title, "title2");

    printf("ID: %d, TITLE: %s \n", book1.id, book1.title);
    printf("ID: %d, TITLE: %s \n", book2.id, book2.title);
    // ID: 20, TITLE: title1 
    // ID: 30, TITLE: title2 

    return 0;
}
```

## Wrap-up

- 사실 이해를 돕기 위해서 위와 같이 작성했지만, 사실은 아래와 같이 `struct` 다음에 `Book`과 같은 단어를 써주는 것이 좋습니다. 그래야 linked list를 만들기에 좋거든요.

```c
typedef struct Book {
    int id;
    char title[10];
    struct Book* next;
} Book;
```
