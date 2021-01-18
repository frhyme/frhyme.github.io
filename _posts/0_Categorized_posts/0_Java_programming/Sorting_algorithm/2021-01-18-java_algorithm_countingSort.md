---
title: Java - Counting Sort
category: java
tags: sort java programming sorting algorithm
---

## Java - Counting Sort

- CountingSort는 현재 array 내에 존재하는 원소의 빈도를 활용하여 sorting하는 방식을 말합니다. '빈도'를 고려하는 것처럼, 원소들이 중복되어 있을 수록 효율적이죠.
- 보통의 알고리즘들은 모든 원소들간의 값을 비교하여 정렬하는 반면, CountingSort의 경우는 값 자체가 제한적인 범위에 있다고 가정하고, 최소값, 최대값 사이의 모든 원소들에 대해서 빈도를 센 다음 순서대로 죽 정렬하는 형태를 가집니다.
- stable하게 만들 수도 있고, unstable하게 만들 수도 있는데, 당연히 stable이 더 구현하기 쉽겠죠. 아래에서 두 가지를 모두 구현하였습니다.

## Java - Unstable Counting Sort

- Unstable Counting Sort는 그냥, 빈도 array를 만든 다음 그 각 빈도만큼 그 값을 쭉쭉 넣어줍니다. 

```java
public static void countSortUnstable(int[] arrOfInt) {
    /*
    * arrOfInt에 대해서 count Sort*/
    int maxNum = Integer.MIN_VALUE;
    int minNum = Integer.MAX_VALUE;

    // Find min, max value
    // 현재 array에서 가장 작은 값(minNum), 가장 큰 값(maxNum)을 찾아줍니다.
    for (int i=0; i < arrOfInt.length; i++) {
        int x = arrOfInt[i];
        if (x < minNum) {
            minNum = x;
        }
        if (x > maxNum) {
            maxNum = x;
        }
    }
    // Count Array
    // 원소별로 등장빈도를 세줍니다.
    // idx: 원소, value: 빈도
    int[] countArr = new int[maxNum - minNum + 1];
    for (int i=0; i < arrOfInt.length; i++) {
        int x = arrOfInt[i];
        countArr[x - minNum] += 1;
    }
    // 원래 Array인 arrOfInt에
    // 빈도를 계산하여 순서대로 넣어줍니다.
    int i = 0;
    for (int x=minNum; x <= maxNum; x++) {
        for (int c=0; c < countArr[x]; c++) {
            arrOfInt[i] = x;
            i++;
        }
    }
    //printArray(arrOfInt);
}
```

## Java - Stable Counting Sort

- Stable Counting Sort는 다음의 순서에 따라 진행됩니다.
  1. `rawArray`를 읽어서, 각 원소의 빈도 array를 만들어줍니다.
  2. 그리고 빈도 array를 cumulative count array, `cumCountArray`로 만들어줍니다.
  3. 그 다음 기존 `rawArray`와 같은 크기의 array `sortedArray`를 만들어줍니다.
  4. `rawArray`의 뒤쪽부터 앞으로 읽어 나갑니다. 이 때, 값 `x`를 `sortedArray`의 `cumCountArray[x]` 위치에 넣어줍니다.
     - `cumCountArray[x]`의 값은 `x`와 같거나 작은 값들의 수를 말합니다. 따라서, `cumCountArray[x]` 값이 바로 정렬된 array에 들어가야 하는 `x`의 위치인 셈이죠. 
     - 또한, 뒤쪽부터 순차적으로 들어가기 때문에 stable하게 정렬되죠.
  5. 그리고, `cumCountArray[x]`는 값을 1 줄이고 다시 4로 돌아갑니다.

```java
public static void countSortStable(int[] arrOfInt) {
    int maxNum = Integer.MIN_VALUE;
    int minNum = Integer.MAX_VALUE;

    // Find min, max value
    // 현재 array에서 가장 작은 값(minNum), 가장 큰 값(maxNum)을 찾아줍니다.
    for (int i=0; i < arrOfInt.length; i++) {
        int x = arrOfInt[i];
        if (x < minNum) {
            minNum = x;
        }
        if (x > maxNum) {
            maxNum = x;
        }
    }
    // Count Array
    // 원소별로 등장빈도를 세줍니다.
    // idx: 원소, value: 빈도
    int[] countArr = new int[maxNum - minNum + 1];
    for (int i=0; i < arrOfInt.length; i++) {
        int x = arrOfInt[i];
        countArr[x - minNum] += 1;
    }
    // Cumulative Count Array
    for (int i=1; i < countArr.length; i++) {
        countArr[i] = countArr[i] + countArr[i - 1];
    }

    // 새로운 array를 만들어줍니다.
    int[] sortedArrOfInt = new int[arrOfInt.length];
    // 기존 array의 뒤에서부터 앞으로 순차적으로 읽어갑니다.
    for (int i = arrOfInt.length - 1; i >= 0; i--) {
        // x: 기존 array의 i위치에 존재하는 value
        int x = arrOfInt[i];
        // xCount: x의 누적 빈도 값
        // 가령, 3의 누적 빈도 값이 5라면, 작거나 같은 값이 현재 3을 포함하여 5개라는 것이죠.
        // 따라서, 이 때 3은 5-1, 4번째 위치에 값이 위치하게 됩니다.
        int xCount = countArr[x];
        // sortedArrIndexOfX:
        // x가 들어갈 sortedArr의 위치
        int sortedArrIndexOfX = xCount - 1;
        sortedArrOfInt[sortedArrIndexOfX] = arrOfInt[i];
        countArr[x] -= 1;
    }
    // copy sortedArrOfInt to arrOfInt
    for (int i=0; i < sortedArrOfInt.length; i++) {
        arrOfInt[i] = sortedArrOfInt[i];
    }
}
```

---

## Raw Code

- 전체 코드는 다음과 같습니다.

```java
package com.company;

import java.lang.*;
import java.util.Random;
import java.util.*;

public class Main {
    public static void countSortUnstable(int[] arrOfInt) {
        /*
        * arrOfInt에 대해서 count Sort*/
        int maxNum = Integer.MIN_VALUE;
        int minNum = Integer.MAX_VALUE;

        // Find min, max value
        // 현재 array에서 가장 작은 값(minNum), 가장 큰 값(maxNum)을 찾아줍니다.
        for (int i=0; i < arrOfInt.length; i++) {
            int x = arrOfInt[i];
            if (x < minNum) {
                minNum = x;
            }
            if (x > maxNum) {
                maxNum = x;
            }
        }
        // Count Array
        // 원소별로 등장빈도를 세줍니다.
        // idx: 원소, value: 빈도
        int[] countArr = new int[maxNum - minNum + 1];
        for (int i=0; i < arrOfInt.length; i++) {
            int x = arrOfInt[i];
            countArr[x - minNum] += 1;
        }
        // 원래 Array인 arrOfInt에
        // 빈도를 계산하여 순서대로 넣어줍니다.
        int i = 0;
        for (int x=minNum; x <= maxNum; x++) {
            for (int c=0; c < countArr[x]; c++) {
                arrOfInt[i] = x;
                i++;
            }
        }
        //printArray(arrOfInt);
    }

    public static void countSortStable(int[] arrOfInt) {
        int maxNum = Integer.MIN_VALUE;
        int minNum = Integer.MAX_VALUE;

        // Find min, max value
        // 현재 array에서 가장 작은 값(minNum), 가장 큰 값(maxNum)을 찾아줍니다.
        for (int i=0; i < arrOfInt.length; i++) {
            int x = arrOfInt[i];
            if (x < minNum) {
                minNum = x;
            }
            if (x > maxNum) {
                maxNum = x;
            }
        }
        // Count Array
        // 원소별로 등장빈도를 세줍니다.
        // idx: 원소, value: 빈도
        int[] countArr = new int[maxNum - minNum + 1];
        for (int i=0; i < arrOfInt.length; i++) {
            int x = arrOfInt[i];
            countArr[x - minNum] += 1;
        }
        // Cumulative Count Array
        for (int i=1; i < countArr.length; i++) {
            countArr[i] = countArr[i] + countArr[i - 1];
        }

        // 새로운 array를 만들어줍니다.
        int[] sortedArrOfInt = new int[arrOfInt.length];
        // 기존 array의 뒤에서부터 앞으로 순차적으로 읽어갑니다.
        for (int i = arrOfInt.length - 1; i >= 0; i--) {
            // x: 기존 array의 i위치에 존재하는 value
            int x = arrOfInt[i];
            // xCount: x의 누적 빈도 값
            // 가령, 3의 누적 빈도 값이 5라면, 작거나 같은 값이 현재 3을 포함하여 5개라는 것이죠.
            // 따라서, 이 때 3은 5-1, 4번째 위치에 값이 위치하게 됩니다.
            int xCount = countArr[x];
            // sortedArrIndexOfX:
            // x가 들어갈 sortedArr의 위치
            int sortedArrIndexOfX = xCount - 1;
            sortedArrOfInt[sortedArrIndexOfX] = arrOfInt[i];
            countArr[x] -= 1;
        }
        // copy sortedArrOfInt to arrOfInt
        for (int i=0; i < sortedArrOfInt.length; i++) {
            arrOfInt[i] = sortedArrOfInt[i];
        }
    }
    public static void printArray(int[] arrOfInt) {
        for (int i=0; i < arrOfInt.length; i++) {
            System.out.printf("%d ", arrOfInt[i]);
        }
        System.out.println("");
    }
    public static void main(String[] args) throws Exception {
        Random randomGen = new Random();

        int sampleSize = 10;
        int maxNum = 5;
        int[] xs = new int[sampleSize];

        for (int i = 0; i < sampleSize; i++) {
            // 0 ~ maxNum(exclusive) 사이의 무작위 값을 리턴
            xs[i] = randomGen.nextInt(maxNum);
        }
        System.out.println("== Raw Array ================");
        printArray(xs);
        System.out.println("== Sorted Array =============");
        //countSortUnstable(xs);
        countSortStable(xs);
        printArray(xs);
    }
}
```
