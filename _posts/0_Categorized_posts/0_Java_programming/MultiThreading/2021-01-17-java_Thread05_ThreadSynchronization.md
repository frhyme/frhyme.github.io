---
title: Java - Thread - Thread Synchronization
category: java
tags: java thread programming parallelism concurrency MultiThreading Synchronization
---

## Java - Thread - Thread Synchronization

- Java에서 Thread 간 동기화(Synchronization)을 하는 방법을 정리합니다.
  1. `Critial Section`: Thread들에 DB, variable, object, file 와 같은 shared resource에 접근하는 코드를 말합니다. 이 부분은 동시에 여러 thread가 접근하도록 하면 안되니까요.
  2. `Monitor`: object에 대해 concurrent access가 가능하도록 하는 mechanism을 말합니다. 일단은 '독점권한'이라고 생각하면 되는데, threadA가 monitor를 획득한 상황이라면, 다른 thread들은 monitor를 획득할 수 없죠. threadA가 monitor를 release할 때까지, 사용할 수 없죠.

## Synchronized Instance Method 

- `synchronized` 키워드를 사용해서, 각 instance가 독점적으로 사용될 수 있도록 처리할 수 있습니다.
- `SharedResource`라는 class를 정의합니다. 그리고, `printThis` 메소드 앞에 `synchronized` 키워드를 붙여줍니다. 이렇게 처리할 경우에, 이 메소드는 한 번에 한 Thread에 의해서만 접근이 가능합니다.

```java
// SharedResource.java
public class SharedResource {
    // 이 곳에 synchronized가 없으면, 서로 다른 Thread에서 동시에 접근이 가능해집니다.
    // 그러나, synchronized가 있을 경우,
    // 하나의 Thread에서 접근이 종료되지 않으면, 다른 Thread에서 접근이 불가하도록 할 수 있습니다.
    public synchronized void printThis() {
        String threadName = Thread.currentThread().getName();
        System.out.println(String.format("%s starts occupying this resource", threadName));
        // do something
        System.out.println(String.format("%s  stops occupying this resource", threadName));
    }
}
```

- 이제 Thread를 만들어줍니다. `Thread`를 상속받는 MyThread를 만들었죠. 얘는 `SharedResource`를 내부 변수로 가지죠.
- 그리고 `run()`메소드에서는 `SharedResource`의 `printThis` 메소드를 사용하죠. 

```java
// MyThread.java
public class MyThread extends Thread {
    private SharedResource shrdR;
    public MyThread(SharedResource shrdR) {
        this.shrdR = shrdR;
    }
    public void run() {
        shrdR.printThis();
    }
}
```

- 그리고 main function에서는 다음처럼 MyThread Instance를 3개 만들어줍니다. 3 instance는 모두 동일한 `SharedResource` Instance를 공유합니다.
- 그리고, 모든 Thread를 start해 보면, SharedResource가 동시에 두 개 이상의 Thread가 사용되지 않는 것을 알 수 있죠.

```java
// Main.java
import java.lang.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws Exception {
        SharedResource sharedR1 = new SharedResource();
        //SharedResource shrdR2 = new SharedResource();

        MyThread thread0 = new MyThread(sharedR1);
        MyThread thread1 = new MyThread(sharedR1);
        MyThread thread2 = new MyThread(sharedR1);

        thread0.start();
        thread1.start();
        thread2.start();
        /*
        Thread-0 starts occupying this resource
        Thread-0  stops occupying this resource
        Thread-2 starts occupying this resource
        Thread-2  stops occupying this resource
        Thread-1 starts occupying this resource
        Thread-1  stops occupying this resource
        */
    }
}
```

## Synchronized Block

- 아래처럼 전체 method를 `Sychronized`로 설정하는 것이 아니라, 특정 부분만 설정할 수도 있습니다.

```java
public class SharedResource {
    public void printThis() {
        String threadName = Thread.currentThread().getName();
        System.out.println(String.format("%s starts occupying this resource", threadName));

        // 이 부분만 synchronized로 처리합니다.
        synchronized (this) {
            System.out.println(String.format("%s  stops occupying this resource", threadName));
        }
    }
}
```

- 그 다음 main method를 실행하면 다음 결과가 나옵니다.

```plaintext
Thread-1 starts occupying this resource
Thread-0 starts occupying this resource
Thread-2 starts occupying this resource
Thread-1  stops occupying this resource
Thread-2  stops occupying this resource
Thread-0  stops occupying this resource
```

## Synchronized static method

- multiThread에서 `ClassA`를 생성한다고 합시다. 이 때, ClassA의 생성자에서 class instance를 생성할 때마다 `classCount`의 값을 1씩 증가해주다고 하겠습니다.
- `ClassA`를 정의해주고요.

```java
// ClassA.java
public class ClassA {
    private static int classCount = 0;
    public ClassA() {
        // synchronized block으로 처리했습니다.
        // 이 부분의 블록을 해제하면, 여러 Thread에서 ClassA.classCount가 증가되기 전에
        // ClassA Instance를 만들기 때문에, 모두 0으로 출력되죠.
        synchronized (ClassA.class) {
            System.out.printf("ClassA instance %d made \n", ClassA.classCount);
            ClassA.classCount += 1;
        }
    }
}
```

- `MyThread`에서는 `run()`에서 새로운 ClassA를 만들어주죠.

```java
package com.company;

public class MyThread extends Thread {
    private SharedResource shrdR;
    private ClassA aaa;
    public MyThread() {
    }
    public void run() {
        this.aaa = new ClassA();
    }
}
```

- main 을 다음과 같이 정의하고 실행해주면 다음과 같습니다.

```java
package com.company;

import java.lang.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws Exception {
        MyThread thread0 = new MyThread();
        MyThread thread1 = new MyThread();
        MyThread thread2 = new MyThread();

        thread0.start();
        thread1.start();
        thread2.start();
        /*
        ClassA instance 0 made 
        ClassA instance 1 made 
        ClassA instance 2 made 
        */
    }
}
```
