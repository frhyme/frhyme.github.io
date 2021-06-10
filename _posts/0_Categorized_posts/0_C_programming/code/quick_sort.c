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