---
title: C programming - Double Linked List(양방향 리스트)
category: c_programming
tags: c c_programming programming linked_list pointer
---

## C programming - Double Linked List(양방향 리스트)

- 간단하게 Double Linked List를 구현해 봤습니다.
- linked list 를 구현할 때, 사람에 따라서 head 혹은 tail에 값을 넣는 경우가 있고 그냥 비어져 있는 노드를 위치하는 경우가 있습니다. 저는 처음부터 비워져 있는 empty_node를 넣는 편인데, 그렇게 해야 linked list operation 코드가 좀더 간결해지는 느낌이 있어요.

```c
#include <stdio.h>
#include <stdlib.h>

typedef struct NODE {
    int node_id;
    int value;
    struct NODE* prev;
    struct NODE* next;
} NODE;

typedef struct DoubleLinkedList {
    NODE* empty_head;
    NODE* empty_tail;
    int node_size;
} DoubleLinkedList; 

NODE* new_node(int node_id, int value) {
    NODE* return_node = (NODE*) malloc(sizeof(NODE) * 1);
    return_node->node_id = node_id;
    return_node->value = value;
    return_node->prev = NULL;
    return_node->next = NULL;
    return return_node;
}

DoubleLinkedList* init_dll() {
    DoubleLinkedList* return_dll = (DoubleLinkedList*) malloc(sizeof(DoubleLinkedList) * 1);
    return_dll->empty_head = new_node(-1, -1);
    return_dll->empty_tail = new_node(-1, -1);
    return_dll->empty_head->next = return_dll->empty_tail;
    return_dll->empty_tail->prev = return_dll->empty_head;
    return return_dll;
}

void add_dll(DoubleLinkedList* dll, int node_id, int value) {
    // 
    NODE* prev_tail = dll->empty_tail->prev;
    NODE* temp_node = new_node(node_id, value);
    prev_tail->next = temp_node;

    temp_node->prev = prev_tail;
    temp_node->next = dll->empty_tail;

    dll->empty_tail->prev = temp_node;
}

void delete_dll(DoubleLinkedList* dll, int node_id) {
    // dll에서 node_id를 가진 node를 삭제해줍니다.
    NODE* prev_pointer = dll->empty_head;
    NODE* pointer = dll->empty_head->next;

    while (pointer != dll->empty_tail) {
        if (pointer->node_id == node_id) {
            prev_pointer->next = pointer->next;
            prev_pointer->next->prev = prev_pointer;
            free(pointer);
            break;
        }
        prev_pointer = pointer;
        pointer = pointer->next;
    }
}

NODE* find_node_by_id(DoubleLinkedList* dll, int node_id) {
    // dll에서 node_id를 가진 NODE를 찾아서 리턴
    NODE* pointer = dll->empty_head->next;
    while (pointer != dll->empty_tail) {
        if (pointer->node_id == node_id) {
            break;
        }
        pointer = pointer->next;
    }
    return pointer;
}

void copy_node(NODE* src, NODE* dest) {
    dest->node_id = src->node_id;
    dest->value = src->value;
}

void swap_node(DoubleLinkedList* dll, int nid1, int nid2) {
    /*
    - node의 nid, value를 교환해줍니다.
    */
    printf("swap node: nid: %d, nid: %d \n", nid1, nid2);

    NODE* node1 = find_node_by_id(dll, nid1);
    NODE* node2 = find_node_by_id(dll, nid2);
    NODE* temp_node = new_node(-1, -1);

    copy_node(node1, temp_node);
    copy_node(node2, node1);
    copy_node(temp_node, node2);
}

void print_dll_from_head(DoubleLinkedList* dll) {
    // 머리부터 꼬리까지 순서대로 출력합니다.
    NODE* pointer = dll->empty_head->next;
    printf("== print_dll_from_head \n");
    while (pointer != dll->empty_tail) {
        printf("nodeid: %d, value: %d \n", pointer->node_id, pointer->value);
        pointer = pointer->next;
    }
}

void print_dll_from_tail(DoubleLinkedList* dll) {
    // 꼬리에서부터 머리까지 순서대로 출력합니다.
    NODE* pointer = dll->empty_tail->prev;
    printf("== print_dll_from_tail \n");
    while (pointer != dll->empty_head) {
        printf("nodeid: %d, value: %d \n", pointer->node_id, pointer->value);
        pointer = pointer->prev;
    }
}

int main(void) {
    DoubleLinkedList* dll = init_dll();
    add_dll(dll, 0, 1);
    add_dll(dll, 1, 2);
    add_dll(dll, 2, 3);
    add_dll(dll, 3, 4);
    add_dll(dll, 4, 4);
    print_dll_from_head(dll);
    delete_dll(dll, 2);
    print_dll_from_head(dll);
    swap_node(dll, 0, 1);
    print_dll_from_head(dll);

    swap_node(dll, 0, 4);
    print_dll_from_head(dll);
}
```
