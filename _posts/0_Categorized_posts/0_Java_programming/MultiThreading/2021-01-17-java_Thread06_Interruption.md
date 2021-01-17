---
title: Java - Thread - Interruption
category: java
tags: java thread programming parallelism concurrency MultiThreading Interruption
---

## Java - Thread - Interruption

- 실행되고 있는 Thread를 `.interrupt()`를 사용해서 종료시킬 수 있습니다. 단, 이때 Thread가 `.join()`이나, `.sleep()`를 실행하고 있는 상황이어야 하죠.

```java
// MyThread.java
import java.util.Date;

public class MyThread extends Thread {
    @Override
    public void run()  {
        try {
            Date startDate = new Date(System.currentTimeMillis());
            System.out.printf("MyThread starts    at %s \n", startDate);
            // .interrupt()가 실행되었을때, 
            // 현재 Thread가 .sleep, .join 중 하나인 상태에 있어야, 종료됩니다.
            Thread.sleep(6000);
            Date endDate = new Date(System.currentTimeMillis());
            System.out.printf("MyThread ends      at %s \n", endDate);
        } catch (Exception e) {
            Date exceptionDate = new Date(System.currentTimeMillis());
            System.out.printf("Exception occurred at %s \n", exceptionDate);
        }
    }
}
```

- 다음처럼 `.interrupt()`를 사용해서 Thread를 종료시킬 수 있습니다.

```java
import java.lang.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws Exception {
        Thread thread1 = new MyThread();
        thread1.start();
        thread1.interrupt();
        /*
        MyThread starts    at Sun Jan 17 22:21:44 KST 2021 
        Exception occurred at Sun Jan 17 22:21:44 KST 2021 
        */
    }
}
```

## Java - interruption - isInterrupted

- `.interupt()`를 실행했을 때 해당 Thread가 종료되려면, `sleep`, `join` 상태에 있어야 합니다.
- 아니면, 현재 interruption 상태인지 확인해주는 `.isInterrupted()`를 사용해서 처리해줄 수도 있죠. 
- 아래 코드는 MyThread에서, `isInterrupted()`를 통해 특정 부분을 실행하지 않도록 처리해주었습니다.

```java
// MyThread.java
import java.util.Date;

public class MyThread extends Thread {
    @Override
    public void run()  {
        try {
            Date startDate = new Date(System.currentTimeMillis());
            System.out.printf("MyThread starts    at %s \n", startDate);
            //Thread.sleep(6000);
            for(int i=0; i < 100000; i++) {
                // 현재 interruption 인지 상태를 확인하며 맞을 경우 thread를 종료합니다.
                if (isInterrupted()) {
                    break;
                } else {
                    Date iterDate = new Date(System.currentTimeMillis());
                    System.out.printf("Thread iter %d     at %s \n", i, iterDate);
                }
            }
            Date endDate = new Date(System.currentTimeMillis());
            System.out.printf("MyThread ends      at %s \n", endDate);
        } catch (Exception e) {
            Date exceptionDate = new Date(System.currentTimeMillis());
            System.out.printf("Exception occurred at %s \n", exceptionDate);
        }
    }
}
```

- 이렇게 처리한 다음, main code를 실행하면 다음과 같습니다. 

```plaintext
MyThread starts    at Sun Jan 17 22:25:36 KST 2021 
MyThread ends      at Sun Jan 17 22:25:36 KST 2021 
```
