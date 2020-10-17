---
title: Java - Array의 크기를 변수로 정의해주는 것이 가능합니다.
category: Java
tags: java programming array
---

## Java에서는 변수로 Array의 크기를 잡아줄 수 있어요

- 가령, 사용자의 입력 값에 따라서, Array의 크기를 다르게 잡아줄 수 있도록 하려면, 중간에 사용자로부터 값을 전달받아야 합니다.
- 코드로 보면 대략 다음과 같죠.

```java
import java.util.Scanner;

class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        // 사용자가 원하는 Array의 크기를 직접 입력하고 
        int arrSize = scanner.nextInt();
        // 그만큼 변수 공간을 확보해줌.
        char[] b = new char[arrSize];
        // 그만큼 사용자로부터 
        for (int i=0; i)
        // End of the code
    }
}

```

## C의 경우 

- C로 코딩을 하신 분들은 처음에 array의 크기를 잡아주어야 합니다.
- java처럼 변수의 값을 통해서 array의 크기를 잡아줄 수 없습니다. 

```c
int main(void){
    int arrSize = 10; 
    scanf("%d", &arrSize);
    int arr[arrSize]; // 여기서 error남
}
```

- 물론 아래 코드에서처럼 `malloc()`를 사용해서 동적할당을 할 수 있기는 합니다만, javac처럼 편하지는 않죠.

```c
int main()
{
    int arrSize;
    scanf("%d", &arrSize);
    int intArr = malloc(sizeof(int) * arrSize);

    // array를 다 쓰고 나면, free를 통해서 메모리를 해제해줘야 함.

    free(intArr);

    return 0;
}
```

## python의 경우 

- python은 전혀 신경 쓸 필요 없습니다 호호. 
- 그냥 만들어진 list에 데이터를 쭉 집어넣어주면 되죠.

```python
lst = []
```
