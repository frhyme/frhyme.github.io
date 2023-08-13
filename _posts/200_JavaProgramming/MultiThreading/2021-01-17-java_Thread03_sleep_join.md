---
title: Java - Thread - Sleep, Join
category: java
tags: java thread programming parallelism concurrency MultiThreading
---

## Java - Thread - Sleep

- `Thread.sleep()`, `TimeUnit.SECONDS.sleep()`를 사용해서 현재 Thread를 일정 시간 정지시켜 둘 수 있습니다.

```java
package com.company;

import java.lang.*;
import java.util.Date;
import java.util.concurrent.TimeUnit;

public class Main {
    public static void main(String[] args) throws Exception {
        /*
        - 현재 Thread는 mainThread입니다.
        Thread.sleep(), TimeUnit.SECONDS.sleep()를 사용해서
        현재 Thread를 일정 시간 정지시켜 둘 수 있습니다.
        */
        // main Thread
        Date startDate = new Date(System.currentTimeMillis());
        System.out.printf("Start Time: %s \n", startDate);
        // Thread의 instance를 sleep하는 것이 아니라,
        // Thread class의 static function에 접근하여 sleep을 사용합니다.
        // 1000 millis = 1 sec
        System.out.println("== Thread.sleep(3000) ==================");
        Thread.sleep(3000);
        Date midDate1 = new Date(System.currentTimeMillis());
        System.out.printf("midDate1:   %s \n", midDate1);

        System.out.println("== TimeUnit.SECONDS.sleep(2) ===========");
        // TimeUnit에는 MINUTES, HOURS 등 다양하게 있습니다.
        TimeUnit.SECONDS.sleep(2);
        Date midDate2 = new Date(System.currentTimeMillis());
        System.out.printf("midDate2:   %s \n", midDate2);

        Date endDate = new Date(System.currentTimeMillis());
        System.out.printf("end Time:   %s \n", endDate);
    }
}
```

- 결과를 보면 다음처럼 일정 시간동안 멈췄다가 실행되는 것을 알 수 있습니다.

```plaintext
Start Time: Sun Jan 17 14:31:41 KST 2021 
== Thread.sleep(3000) ==================
midDate1:   Sun Jan 17 14:31:44 KST 2021 
== TimeUnit.SECONDS.sleep(2) ===========
midDate2:   Sun Jan 17 14:31:46 KST 2021 
end Time:   Sun Jan 17 14:31:46 KST 2021 
```

## Java - Thread - Join

- `threadA`에서 `threadB.join()`를 실행하면, threadB가 종료될때까지, `threadA`의 실행이 멈추게 됩니다.
- 우선 `ThreadA`라는 class를 만들어줍니다. 시작되면 시작 시간을 출력하고, 2second동안 sleep한 다음 종료 시간을 출력해줍니다.

```java
// ThreadA.java
import java.util.Date;

public class ThreadA extends Thread {
    private String name;
    @Override
    public void run(){
        Date startDate = new Date(System.currentTimeMillis());
        System.out.printf("ThreadA     starts at %s \n", startDate);
        try {
            // .sleep()에서 InterruptedException가 발생할 수 있으므로
            // 예외처리를 해줍니다.
            Thread.sleep(2000);
            Date endDate = new Date(System.currentTimeMillis());
            System.out.printf("ThreadA       ends at %s \n", endDate);
        } catch (Exception InterruptedException) {
            System.out.println("InterruptedException");
        }
    }
}
```

- 그리고 main Thread는 다음과 같이 정의해줍니다. 현재는 `.join()`을 사용하지 않았기 때문에, 실행하면 `MainThread`와 `ThreadA`가 그냥 개별적으로 수행되죠. 따라서, 

```java
package com.company;

import java.lang.*;
import java.util.Date;

public class Main {
    public static void main(String[] args) throws Exception {
        Date startDate = new Date(System.currentTimeMillis());
        System.out.printf("Main Thread starts at %s \n", startDate);
        ThreadA threadA = new ThreadA();
        threadA.start();
        // threadA.join()을 실행하면, 
        // threadA가 종료될 때 까지, 이 뒷부분의 코드는 실행되지 않습니다.
        // 하지만, 마냥 기다릴 수는 없으니까요, 만약 threadA.join(100)과 같이 처리하면
        // 기다리다가 100을 넘기면 그냥 무시하고 뒤 부분의 코드가 실행됩니다.
        // threadA.join();

        Date endDate = new Date(System.currentTimeMillis());
        System.out.printf("Main Thread   ends at %s \n", endDate);

    }
}
```

- 아래에서 보시는 것처럼, Main Thread가 먼저 종료되고, 그 다음에 `ThreadA`가 실행되고 종료되죠.

```plaintext
Main Thread starts at Sun Jan 17 15:07:11 KST 2021 
Main Thread   ends at Sun Jan 17 15:07:11 KST 2021 
ThreadA     starts at Sun Jan 17 15:07:11 KST 2021 
ThreadA       ends at Sun Jan 17 15:07:13 KST 2021 
```

- comment 처리한 `threadA.join()` 부분을 넣어서 실행해주면 다음과 같이, ThreadA가 종료된 다음 Main Thread가 종료되는 것을 알 수 있습니다.

```plaintext
Main Thread starts at Sun Jan 17 15:08:32 KST 2021 
ThreadA     starts at Sun Jan 17 15:08:32 KST 2021 
ThreadA       ends at Sun Jan 17 15:08:34 KST 2021 
Main Thread   ends at Sun Jan 17 15:08:34 KST 2021 
```
