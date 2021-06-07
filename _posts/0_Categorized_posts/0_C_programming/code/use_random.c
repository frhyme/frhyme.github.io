#include <stdio.h>
#include <stdlib.h>

int main(void) {
    int seed = 10;
    srand(seed);
    for (int i=0; i < 10; i++) {
        printf("%d \n", rand());
    }

    return 0;
}