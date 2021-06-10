---
title: C programming - quick sort
category: c_programming
tags: c c_programming programming quick_sort sorting divide_and_conquer 
---

## C programming - quick sort

- 간단하게 quick sort를 구현해봤습니다.
- merge sort의 경우 왼쪽 array를 정렬하고 오른쪽 array를 정렬한 다음, 이 둘을 함께 읽으면서 가장 작은 애부터 순차적으로 뽑아서 정렬해주는 형식을 말합니다. 이 과정에서 추가적인 메모리 공간을 필요로 하지만, quick sort와 달리 stable하게 sort할 수 있다는 장점이 있습니다.
- 반면 quick sort의 경우는 하나의 원소값(pivot)을 기준으로 왼쪽에는 작은 값들, 오른쪽에는 큰 값들을 집어넣습니다. merge_sort에 비해서는 그 코드의 구조가 조금 복잡하게 느껴질 수 있죠. 순서를 정리하면 대략 다음과 같습니다.
  - array에서 pivot값을 정한다. 보통 0번째, 혹은 N - 1 번째로 정한다.
  - `i`는 왼쪽부터 읽고, `j`는 오른쪽부터 읽으면서, pivot보다 큰 놈, 작은 놈을 번갈아 교환해준다. 이를 반복하다 보면 pivot을 제외하면 왼쪽에는 pivot보다 작은 값, 오른쪽에는 pivot보다 큰 값이 위치하게 된다.
  - pivot을 현재 array에서 중간에 위치시켜준다.
  - 왼쪽에 대해서 `quick_sort`를, 오른쪽에 대해서도 `quick_sort`를 수행해 준다.
- 코드는 대략 다음과 같습니다.

```c
#include <stdio.h>
#include <stdlib.h>

void print_arr(int* arr, int size) {
    for (int i=0; i < size; i++) {
        printf("%d ", arr[i]);
    }
    printf("\n");
}

void swap_int(int* a, int* b) {
    int temp;
    temp = *a;
    *a = *b;
    *b = temp;
}

void quick_sort(int* arr, int left, int right) {
    if (left <= right) {
        int pivot_index = left; 
        int i = left + 1;
        int j = right;
        int pivot_value = arr[pivot_index];

        while (i <= j) {
            // find i bigger than pivot_value
            while (i <= j) {
                if (arr[i] <= pivot_value) {
                    i = i + 1;
                } else {
                    break;
                }
            }
            // find j smaller than pivot_value
            while (i <= j) {
                if (arr[j] <= pivot_value) {
                    break;
                } else {
                    j = j - 1;
                }
            }
            if (i <= j) {
                swap_int(&arr[i], &arr[j]);
            }
        }
        // pivot은 0 index에 있으며, 현재로는 정렬된 상태가 유지되지 않습니다.
        // 따라서, pivot을 중간에 위치시켜 정렬된 상태로 만들어줍니다.
        swap_int(&arr[i - 1], &arr[pivot_index]);
        
        quick_sort(arr, left, i - 2);
        quick_sort(arr, i, right);
    }
}


int main(void) {
    int n = 19;
    int* arr = (int*) malloc(sizeof(int) * n);

    for (int i=0; i < n; i++) {
        arr[i] = rand() % 30;
    }

    print_arr(arr, n);
    quick_sort(arr, 0, n - 1);
    print_arr(arr, n);

}
```
