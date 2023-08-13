---
title: Java - Dynamic Array(동적배열)
category: DataStructure
tags: java array programming
---

## 왜 Dynamic Array가 필요한가?

- 일반적으로 Array를 사용할 때는 다음처럼 메모리의 크기를 처음에 잡아놓고 시작합니다. 다음의 코드에서는 3개의 `int` 크기의 메모리를 잡은 것이죠. 그 메모리에 우리는 3개의 int형 정수를 배치하여 사용할 수 있습니다.

```java
int[] intArr = new int[3];
```

- 다만, 문제는 우리가 Array의 크기를 단정하지 못할 때 발생합니다. 가령, 10개의 메모리를 잡아놨는데, 11개의 메모리가 필요하다거나, 혹은 훨씬 늘어나는 일이 발생한다거나 하면 어떻게 해야 할까요?
- "거 뭐 그냥 따로 메모리를 하나 더 잡으면 되는 거 아닌가요?" 라고 생각할 수 있습니다. 뭐, 딱히 틀린 말은 아니지만요.
- 아래 그림에서 보는 것처럼 Array는 연속된 memory들로 구성되어 있습니다. 가령 `arr[0]`의 메모리 바로 옆에 `arr[1]`이 붙어 있는 형식이죠. 만약 10개를 만들었다면, 이 10개의 memory는 모두 10개의 연속된 memory로 구성되어 있는 것이 기본입니다. 이렇게 할 경우 access 측면에서 훨씬 효율적이죠.
  
![memory_address](https://miro.medium.com/max/497/1*-ImKrqrT14UlG6wMpAEIJQ.png)

- 따라서, 현재 배정된 memory를 증가시켜야 한다면, 다음과 같은 순서를 따라야 합니다.
  - **New Memory Allocation**: 확장된 메모리를 확보한다.
  - **Copy Array to New Memory**: 기존의 Array의 값들을 새로운 메모리에 복사해준다.
- 매우 번거로워보이지만, 어쩔 수 없어요. 아무튼, 이를 자동으로 지원해주는 아이를 Dynamic Array라고 하죠.

### Concepts of Dynamic Array

- Dynamic Array의 몇가지 주요 개념을 설명합니다.

![dynamic_array_size_capacity](https://www.algolist.net/img/arrays/dynamic-array.png)

- `Size`: 현재 값이 배정되어 있는 원소의 크기
- `Capacity`: 현재 배정된 메모리의 크기. 무조건 `Capacity` >= `Size`이어야 함.
- `Scaling factor`(Growth Factor): 새로운 원소가 들어와서 들어와서 Capacity가 모자라면, Capacity를 늘려야 합니다. 이 때 메모리를 기존 메모리 대비 몇 배나 확장하게 될 지 판단하게 되는데, 이 값을 Scaling Factor라고 합니다.
  - 당연하지만, 이 값이 엄청 크면, time 측면에서는 이득이 있으나, 메모리 공간에서는 손해를 봅니다.

## Dynamic Array - java implementation

- 이를 간단한 java 코드로 작성한다면 다음과 같습니다.
- `DynamicArr`이라는 class로 정의하였습니다.

```java
public class DynamicArr {
    int size ;
    int capacity;
    int growthFactor = 2;
    int[] arrPointer = null;

    DynamicArr() {
        // 현재는 아무 원소도 없으므로 0, capacity는 2로 잡음
        this.size = 0;
        this.capacity = this.growthFactor * 1;
        this.arrPointer = new int[this.capacity];
    }
    void add(int newElement) {
        /*
        * @newElement: 현재 array의 끝에 추가될 원소*/
        if (this.size < this.capacity) {
            // Size가 capacity보다 작을 때는 뭘 더 할 필요가 없음
            arrPointer[this.size] = newElement;
        } else {
            // Size가 capacity와 같아지므로, array의 크기를 더 크게 만들어서 잡아줘야 함.
            this.capacity = this.size * this.growthFactor;
            int[] newArrPointer = new int[this.capacity];
            for (int i=0; i < this.size; i++) {
                newArrPointer[i] = this.arrPointer[i];
            }
            this.arrPointer = newArrPointer;
            this.arrPointer[this.size] = newElement;
        }
        this.size += 1;
    }
    void print(){
        // 그냥 현재 size, capacity와 원소들의 값을 출력함.
        System.out.printf("Size: %d Capacity: %d\n", this.size, this.capacity);
        for (int i=0; i < this.arrPointer.length; i++) {
            System.out.printf("%d ", this.arrPointer[i]);
        }
        System.out.println("");
        System.out.println("===========================");
    }
}
```

- 그리고 다음 코드로 테스트를 해보면 잘 진행되는 것을 알 수 있습니다.

```java
class Main {
    public static void main(String[] args) {
        DynamicArr a = new DynamicArr();
        a.print();
        a.add(1);
        a.print();
        a.add(2);
        a.print();
        a.add(3);
        a.print();
        a.add(4);
        a.print();
        a.add(5);
        a.print();

    }
}
```

```plaintext
Size: 0 Capacity: 2
0 0 
===========================
Size: 1 Capacity: 2
1 0 
===========================
Size: 2 Capacity: 2
1 2 
===========================
Size: 3 Capacity: 4
1 2 3 0 
===========================
Size: 4 Capacity: 4
1 2 3 4 
===========================
Size: 5 Capacity: 8
1 2 3 4 5 0 0 0 
===========================
```

## Optimal Growth Factor?

- 앞서 말한 바와 같이, Dynamic Array에서 `Size`는 현재 값이 배정되어 있는 메모리의 크기이고, `Capacity`는 확보되어 있는 메모리의 크기를 말합니다. 항상 `Size`보다 `Capacity`가 크고, `Capacity / Size`는 Growth Factor 혹은 Scale Factor라고 불리죠.
- 그리고, 만약 새로운 값들이 어레이에 계속 들어와서 `Capacity`와 `Size` 값이 같아진다면, 기존의 메모리를 유지한 채 새로운 메모리를 추가하는 것이 아니라, `현재 Size * GrowthFactor`만큼의 메모리를 확보한 다음, 이 메모리에 기존 값을 모두 복사해줍니다. 
- 그러하므로, `Size`와 `Capacity`가 같아지는 상황이 빈번하게 발생한 다면 그만큼 원래의 메모리에서 새로운 메모리로 값을 복사해야 하는 일이 늘어나겠죠. 가령 `GrowthFactor`가 1.1이라면 size와 capacity간의 slack이 `10%`밖에 되지 않기 때문에, 꽤 자주 메모리의 값을 복사해줘야 합니다.
- 반대로, GrowthFactor가 너무 크다면, 값 전체를 복사해서 옮겨줘야 하는 빈도는 줄어들지 몰라도, 사용하지 않으면서도 잡아놓는 slack 메모리가 증가하게 됩니다. 가령 `GrowthFactor`가 2.0이라면 사용하지 않는 메모리를 현재 배열의 크기만큼 잡아두고 있는 셈이죠.
- 따라서, 메모리의 사용과 속도 측면에서 조율하게 적합한 GrowthFactor를 자는 것이 필요합니다. 절대적인 것은 없습니다. 만약 내 컴퓨터에서 하는 연산에서 배열의 크기가 매우 가변적이라면 GrowthFactor를 키우는 것이 좋겠죠. 상황에 따라서 조금 다릅니다.
- 프로그래밍 언어 별로 다음과 같이 차이가 있으나, 보통 다음처럼 1.5 혹은 2.0의 값을 가집니다.
  - Java ArrayList - 1.5
  - Python PyListObject - 1.25
  - Microsoft Visual C++ 2013 - 1.5
  - Rust Vec - 2
- 또한, Array는 아니지만, .Net의 `Dynamic Dictionary <, >`의 경우는 hash function을 사용하기 때문에, Size를 2배 한 다음 소수가 나올 때까지 Capacity 를 키운다고 하네요.

### Shrink Factor?

- Size와 Capacity와 같아지면 메모리를 증가한다면, 반대로 Size가 Capactiy에 비해서 턱없이 작다면, Shrink하는 것이 필요할 수도 있습니다.
- 상황에 따라 다른데, [stackoverflow - shrink factor for dynamic array](https://stackoverflow.com/questions/60827662/shrink-factor-for-dynamic-array)에 따르면, 대부분의 경우는 오히려 shrink factor를 정의하는 것이 새로운 오버헤드를 발생할 수 있다고도 하죠.
- 결국, 이 말도 이전에 한 말과 동일합니다. "내가 사용하는 목적에 맞춰서 해라"정도겠죠.

--- 

## Wrap-up

- python의 list 또한, dynamic array로 만들어져 있죠.
- 다른 대부분의 언어들 또한 기본적으로 dynamic Array는 가지고 있습니다.

## Reference

- [Wikipedia - Dyanmic Array](https://en.wikipedia.org/wiki/Dynamic_array)
- [Stackoverflow - What is the ideal growth rate for a dynamically allocated array](https://stackoverflow.com/questions/1100311/what-is-the-ideal-growth-rate-for-a-dynamically-allocated-array)
