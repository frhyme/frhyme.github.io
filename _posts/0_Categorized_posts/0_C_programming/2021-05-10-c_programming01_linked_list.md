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

- linked list에 대한 다양한 operation을 다음과 같이 만들어 봤습니다.

```c
#include <stdio.h>
#include <stdlib.h>

#define true 1
#define false 0

typedef int bool;

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

void append_node(Node* firstNode, int id) {
    // firstNode의 끝(tail)까지 가서 id를 가진 node를 연결함.
    Node* pointer = firstNode; 
    while (pointer->next != NULL) {
        pointer = pointer->next;
    }
    pointer->next = new_node(id);
}

bool delete_node(Node* firstNode, int id) {
    // firstNode로부터 순차적으로 찾으면서, id가 있는 node를 찾아서 삭제
    // 그리고 가장 첫번째 node를 리턴함.
    Node* prev_pointer;
    Node* pointer = firstNode;

    while (pointer != NULL) {
        if (pointer->id == id) {
            // find it 
            prev_pointer->next = pointer->next;
            pointer = NULL;
        } else {
            prev_pointer = pointer;
            pointer = pointer->next;
        }
    }
    return false;
}
Node* find_node(Node* firstEmptyNode, int id) {
    Node* pointer = firstEmptyNode->next;
    while (pointer != NULL) {
        if (pointer->id == id) {
            return pointer;
        }
        pointer = pointer->next;
    }
    return NULL;
}

void print_node(Node* firstEmptyNode) {
    Node* pointer = firstEmptyNode->next;
    while (pointer->next != NULL) {
        printf("id: %5d \n", pointer->id);
        pointer = pointer->next;
    }
    printf("id: %5d \n", pointer->id);
}


int main(void) {
    Node* firstEmptyNode; 
    firstEmptyNode = new_node(-1);
    append_node(firstEmptyNode, 1);
    append_node(firstEmptyNode, 2);
    append_node(firstEmptyNode, 3);
    append_node(firstEmptyNode, 4);
    append_node(firstEmptyNode, 5);

    print_node(firstEmptyNode);
    /*
    id:     1 
    id:     2 
    id:     3 
    id:     4 
    id:     5 
    */
    printf("==========\n");
    delete_node(firstEmptyNode, 3);
    print_node(firstEmptyNode);
    /*
    ==========
    id:     1 
    id:     2 
    id:     4 
    id:     5 
    */
    printf("==========\n");
    delete_node(firstEmptyNode, 1);
    print_node(firstEmptyNode);
    /*
    ==========
    id:     2 
    id:     4 
    id:     5 
    */
    printf("xxx: %d\n", find_node(firstEmptyNode, 2)->id);
    printf("xxx: %d\n", find_node(firstEmptyNode, 2)->next->id);
    // xxx: 2
    // xxx: 4
}
```