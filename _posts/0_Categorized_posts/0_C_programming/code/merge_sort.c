#include <stdio.h>
#include <stdlib.h>

#define N 21 


void print_arr(int* arr, int arr_size) {
    printf("arr: ");
    for (int i=0; i < arr_size; i++) {
        printf("%d ", arr[i]);
    }
    printf("\n");
}

void swap_int(int* a, int*b) {
    // a, b에 들어 있는 값을 교환하는 함수
    int temp;
    temp = *a;
    *a = *b;
    *b = temp;
}

void merge(int* arr, int l1, int r1, int l2, int r2) {
    /*
    - l1부터 r1까지는 정렬된 array 
    - 마찬가지로, l2부터 r2까지 정렬된 array
    - 이 en array를 함께 읽으면서 가장 작은 놈을 찾고 얘를 temp_arr에 잠시 넣어준 다음
    다시 arr에 넣어준다. 따라서, array의 길이 만큼의 메모리 공간이 필요하다.
    */
    int temp_arr_size = r2 - l1 + 1;
    int* temp_arr = (int*) malloc(sizeof(int) * temp_arr_size);
    int i = l1;
    int j = l2;
    int k = 0;
    while(1) {
        if (i <= r1) {
            if (j <= r2) {
                if (arr[i] < arr[j]) {
                    temp_arr[k] = arr[i];
                    i++;
                } else {
                    temp_arr[k] = arr[j];
                    j++;
                }
            } else {
                temp_arr[k] = arr[i];
                i++;
            } 
        } else {
            if (j <= r2) {
                temp_arr[k] = arr[j];
                j++;
            } else {
                break;
            } 
        }
        k++;
    }
    for (k = 0; k < temp_arr_size; k++) {
        arr[l1 + k] = temp_arr[k];
    }
    free(temp_arr);
}
void merge_sort(int* arr, int l, int r) {
    int size = r - l + 1;
    if (size > 2) {
        /*
        - 왼쪽 정렬 > 오른쪽 정렬 > 합체 의 순으로 진행되어야 함.
        */
        int p = (r + l) / 2;
        merge_sort(arr, l, p);
        merge_sort(arr, p + 1, r);
        merge(arr, l, p, p+1, r);
    } else {
        if (size == 2) {
            if (arr[l] > arr[r]) {
                swap_int(&arr[l], &arr[r]);
            }
        }
    }

}
int main(void) {
    int arr[N];
    
    for (int i=0; i < N; i++) {
        arr[i] = rand() % 100;
    }
    printf("Before sorting \n");
    print_arr(arr, N);
    merge_sort(arr, 0, N);
    printf("After sorting \n");
    print_arr(arr, N);


    return 0;

}