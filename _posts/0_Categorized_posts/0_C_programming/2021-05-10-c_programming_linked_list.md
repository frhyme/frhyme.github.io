---
title: C - linked list example
category: C_programming
tags: C programming C_programming C malloc linked_list
---

## C - linked list example

- 간단하게 linked list를 만들어 봤습니다.

```c
#include <stdio.h>
#include <stdlib.h>

typedef struct Node {
    int id;
    struct Node* next;
} Node;

Node* new_node(int id) {
    Node* node = malloc(sizeof(Node) * 1);
    node->id = id;
    node->next = NULL;
    return node;
}

int main(void) {
    Node* firstNode; 
    Node* secondNode;

    firstNode = new_node(1);
    secondNode = new_node(2);

    printf("%d \n", firstNode->id);
    // 1
    printf("%d \n", secondNode->id);
    // 2
    printf("connected\n");
    firstNode->next = secondNode;
    printf("%d \n", firstNode->next->id);
    // 2
}
```