#include <stdio.h>
#include <time.h>
#include <stdlib.h>

int main(void) {
    // time.h에 정의되어 있음.
    // clock_t는 unsigned long
    clock_t start1;
    clock_t end1;

    // CLOCKS_PER_SEC: 1000000
    printf("CLOCKS_PER_SEC: %d \n", CLOCKS_PER_SEC);
    start1 = clock();
    int r = 0; 
    printf("start: %lu \n", start1);
    for (int i=0; i < 1000000; i++) {
        r += i;
    }
    end1 = clock(); 
    printf("end  : %lu \n", end1);
    printf("== elapsed time: %lu clocks \n", end1 - start1);
    printf("== elapsed time: %f seconds \n", (float)(end1 - start1) / CLOCKS_PER_SEC);
}