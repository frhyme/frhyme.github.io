---
title: C - Heap
category: C_programming
tags: C programming C_programming C heap
---

## C - Heap

- 간단하게 Heap을 구현해 봤습니다.

```c
#include <stdio.h>
#include <stdlib.h>

#define true 1
#define false 0

int* min_heap; 
int max_heap_size = 128 - 1;
int curr_heap_size = 0; 

int get_parent_index(int index) {
    if (index == 0) {
        return -1;
    } else {
        return (index + 1) / 2 - 1;
    }
}
int get_left_child_index(int index) {
    return index * 2 + 1;
}
int get_right_child_index(int index) {
    return index * 2 + 2;
}
int swap(int* a, int* b) {
    int temp;
    temp = *a;
    *a = *b;
    *b = temp;
}
void push_heap(int x) {
    min_heap[curr_heap_size] = x;
    
    int index = curr_heap_size;
    int parent_index = get_parent_index(index);
    while(parent_index != -1) {
        if (min_heap[index] < min_heap[parent_index]) {
            swap(&min_heap[index], &min_heap[parent_index]);
            index = parent_index;
            parent_index = get_parent_index(index);
        } else {
            break;
        }
    }
    curr_heap_size += 1;
}

int pop_heap() {
    int r = min_heap[0];
    swap(&min_heap[0], &min_heap[curr_heap_size-1]);
    curr_heap_size -= 1;

    int index = 0; 
    int left_child_index;
    int right_child_index;
    while (true) {
        left_child_index = get_left_child_index(index);
        right_child_index = get_right_child_index(index);
        if (left_child_index < curr_heap_size) {
            if (right_child_index < curr_heap_size) {
                // both
                if (min_heap[left_child_index] < min_heap[right_child_index]) {
                    // left smaller
                    if (min_heap[index] > min_heap[left_child_index]) {
                        swap(&min_heap[index], &min_heap[left_child_index]);
                        index = left_child_index;
                    } else {
                        break;
                    }
                } else {
                    // right smaller
                    if (min_heap[index] > min_heap[right_child_index]) {
                        swap(&min_heap[index], &min_heap[right_child_index]);
                        index = right_child_index;
                    } else {
                        break;
                    }
                }
            } else {
                // left
                if (min_heap[index] > min_heap[left_child_index]) {
                    swap(&min_heap[index], &min_heap[left_child_index]);
                    index = left_child_index;
                } else {
                    break;
                }
            }
        } else {
            break;
        }
        
    }
    return r;
}
void print_heap() {
    for (int i=0; i < curr_heap_size; i++) {
        printf("%d ", min_heap[i]);
    }
    printf("\n");
}

int main(void) {
    min_heap = (int*) malloc(sizeof(int) * max_heap_size);
    for(int i = 10; i > 0; i--) {
        push_heap(i);
        print_heap();
    }

    for (int i=0; i < 10; i++) {
        printf("%d \n", pop_heap());
        print_heap();
    }
    
    printf("DDD\n");
    return 0; 
}
```
