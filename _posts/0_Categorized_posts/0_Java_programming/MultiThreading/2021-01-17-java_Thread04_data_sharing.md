---
title: Java - Thread - Thread 간 데이터 불일치, volatile
category: java
tags: java thread programming parallelism concurrency MultiThreading volatile
---

## Java - Thread - Thread 간 데이터 불일치

- 다음과 같은 ThreadA가 있다고 합시다. ThreadA를 실행하면, `start_i`부터 3개를 `lstOfInteger` 집어넣고 그 결과를 출력합니다.

```java
import java.util.*;

public class ThreadA extends Thread {
    private String name;
    private List<Integer> lstOfInteger;
    private int start_i;

    public ThreadA(String name, List<Integer> lstOfInteger, int start_i) {
        this.name = name;
        this.lstOfInteger = lstOfInteger;
        this.start_i = start_i;
    }
    @Override
    public void run(){
        // this.start_i부터 1씩 증가하며 3개를 
        // this.lstOfInteger에 넣어 줍니다.
        for (int i=this.start_i; i < this.start_i + 3; i++) {
            this.lstOfInteger.add(i);
            System.out.printf("Name: %s, %s \n", this.name, this.lstOfInteger);
        }
    }
}
```

- 아래 main thread에서는 `ThreadA`를 2개 만들었습니다. 그릐고 둘다 `.start()`해보면 두 코드의 실행 결과가 완전히 뒤섞여 있죠.

```java
import java.lang.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws Exception {
        List<Integer> lstOfInt = new ArrayList<>();
        ThreadA threadA = new ThreadA("A", lstOfInt, 0);
        ThreadA threadB = new ThreadA("B", lstOfInt, 10);

        /*
        * threadA, threadB는 각각 동시에 실행됩니다.
        * lstOfInt는 두 thread에 의해 공유되는 상태이기 때문에,
        * A에서 lstOfInt를 출력했을 때, 이미 B의 결과가 반영된 상황이곤 하죠.
        * 즉, non-atomic하다는 이야기입니다.
        * .join()을 통해서 실행할 수도 있지만, */
        threadA.start();
        threadB.start();
    }
}
```

- 보시는 것처럼, A에서 값을 집어넣고 출력했는데, 이미 B에서 집어넣은 결과가 들어와 있는 경우들이 있죠. 이건 각 Thread가 non-atomic하게 실행되기 때문이죠.
- 물론 그냥 main Thread 내에서 `threadA.join()`을 처리해버리면 `threadA`가 종료된 다음에 `threadB`가 실행되니까, 각각 atomic하게 처리되기는 합니다.

```plaintext
Name: A, [0, 10] 
Name: A, [0, 10, 1] 
Name: A, [0, 10, 1, 2] 
Name: B, [0, 10, 1, 2] 
Name: B, [0, 10, 1, 2, 11] 
Name: B, [0, 10, 1, 2, 11, 12] 
```

---

## Solution - volatile 

- 이걸 해결하려면, `volaitle` 키워드를 사용해야 합니다. 보통 변수의 값들은 효율을 위해서, CPU cache에 저장되는데, 이렇게 할 경우 multi-thread 환경에서는 이렇게 처리할 경우 두 thread에서 업데이트되지 않은 값을 읽게 되는 결과가 발생할 수 있습니다.
- 따라서, CPU cache에서 읽도록 하지 않고, Read, Write를 Main Memory에서 가능하도록 하는 것이 바로 `volatile` 키워드죠.

---

## Wrap-up

- 괜찮은 예제를 만들어 보려고 했는데, 잘 안 만들어지네요.
