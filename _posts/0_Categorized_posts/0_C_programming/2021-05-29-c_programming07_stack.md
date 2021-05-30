---
title: C programming - stack 을 구현해봤습니다. 
category: C_programming
tags: C programming C_programming c stack 
---

## C programming - stack 을 구현해봤습니다

- 간단하게, C로 stack을 구현해 봤습니다.
- 한방햔 linked list를 사용했고, head, last를 각각 기억합니다.

```c
#include <stdio.h>
#include <stdlib.h>

typedef struct NODE {
    int value;
    struct NODE* next;
} NODE;

NODE* new_node(int value, NODE* next) {
    NODE* temp_node = (NODE*) malloc(sizeof(NODE) * 1);
    temp_node->value = value;
    temp_node->next = next;
    return temp_node;
}

typedef struct STACK {
    NODE* head;
    NODE* prev_last;
    NODE* last;
    int size;
} STACK;

STACK* init_stack(STACK* stack) {
    stack->head = new_node(-1, NULL);
    stack->prev_last = stack->head;
    stack->last = stack->head;
    stack->size = 0; 
    return stack;
}

int get_size(STACK* stack) {
    return stack->size;
}

STACK* push_node(STACK* stack, int value) {
    stack->last->next = new_node(value, NULL);
    stack->prev_last = stack->last;
    stack->last = stack->last->next;
    stack->size += 1;
    return stack;
}

NODE* pop_node(STACK* stack) {
    NODE* return_node = stack->last;
    if (stack->size == 1) {
        init_stack(stack);
    } else {
        stack->last = stack->prev_last;
        stack->last->next = NULL;
        NODE* pointer = stack->head;
        while (1) {
            if (pointer->next == stack->last) {
                stack->prev_last = pointer;
                break;
            }
            pointer = pointer->next;
        }
        stack->size -= 1; 
    }
    return return_node;
}

void print_stack(STACK* stack) {
    NODE* pointer = stack->head->next;
    printf("stack size: %d \n", stack->size);
    while (pointer != NULL) {
        printf("%d ", pointer->value);
        pointer = pointer->next;
    }
    printf("\n");
}

int main(void) {
    STACK* stack = (STACK*)malloc(sizeof(STACK) * 1);
    stack = init_stack(stack);
    stack = push_node(stack, 1);
    stack = push_node(stack, 7);
    stack = push_node(stack, 3);
    print_stack(stack);
    printf("pop node: %d \n", pop_node(stack)->value);
    printf("pop node: %d \n", pop_node(stack)->value);
    printf("pop node: %d \n", pop_node(stack)->value);
    print_stack(stack);
    push_node(stack, 1);

    print_stack(stack);

    free(stack);
    return 0;
}
```
