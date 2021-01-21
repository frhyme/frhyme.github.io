---
title: Java - Thread - State of Thread
category: java
tags: java thread programming parallelism concurrency MultiThreading
---

## Java - Thread - State of Thread

- Thread 또한 life cycle을 가지며 state가 변하죠. 프로그래머가 Interruption 등으로 Thread의 state를 변경하는 경우도 있고, OS로 인해 바뀌는 경우도 있습니다.
- Thread의 상태는 enum type인 `Thread.state`으로 다음 6가지로 나뉘어 표현됩니다.
  - `NEW`: Thread가 생성되었지만, `.start()`는 실행되지 않은 상태
  - `RUNNABLE`: Thread가 JVM에서 실행되고 있거나, 혹은 OS의 Resource를 사용하기 위해서 기다리고 있는 상태
  - `BLOCKED`: Monitor lock을 기다리는 상황이어서 Thread에 락이 걸려 있는 상태
  - `WAITING`: Thread가 다른 Thread를 기다리는 상황을 말하며, `.join`에 의해 발생하죠.
  - `TIMED_WAITING`: Thread가 다른 Thread는 특정한 시간동안 기다리는 경우를 말합니다. `.sleep()`이나, `.join(timeout)`에 의해 기다리는 경우를 말합니다.
  - `TERMINATED`: Thread가 완전히 실행되었거나, 예외가 발생하여 종료된 경우를 말합니다. Thread가 `TERMINATED`된 상태로 오게 되면 절대로 다시 `RUNNABLE`로 돌아갈 수 없습니다.
- Thread의 현재 상태를 확인하려면, `.getState()`를 사용하면 됩니다.

## Simple State Change

- 간단히 Thread의 상태 변화를 보면 다음과 같습니다.
  - `.start()`이 호출되기 이전에는 `NEW` 상태이며
  - `.start()`이 호출되고, `.run()`이 호출되기 이전에는 `RUNNABLE` 상태. 아직 main Thread에서 `.run()`을 실행하지 않은 상황인 것이죠.
  - `.join()`을 통해 현재 main Trhead에서 `thread`를 기다리게 됩니다. 따라서, `.join()` 다음 statement가 실행되려면, thread가 `TERMINATED`여야 하죠.

```java
package com.company;

import java.lang.*;
import java.util.Random;
import java.util.*;

public class Main {
    public static void printState(Thread thread) {
        System.out.printf("State of Thread: %s \n", thread.getState());
    }
    public static void main(String[] args) throws Exception {
        Thread thread = new Thread();
        printState(thread);// NEW
        thread.start();
        // 아직 .run()이 호출되기 이전이므로
        // RUNNABLE이 출력됩니다.
        printState(thread);// RUNNABLE

        thread.join();
        printState(thread);// TERMINATED
        /*
        State of Thread: NEW
        State of Thread: RUNNABLE
        State of Thread: TERMINATED
        */
    }
}
```

## Thread State Diagram

- Thread의 state 변화를 보면 다음과 같습니다.
- 각 Node의 상태는 `StateInOS - StateInJava`로 구분됩니다. 즉, `Initialized - NEW`는 OS에서 볼 때는 Initialized지만, Java에서는 `NEW`의 상태인 것이죠. 일단은 대략, 이렇게 진행된다 정도로만 알고 계시면 됩니다.

<div class="mermaid">
    graph TD
        nID1([Initialized - NEW__])
        nID2([Ready - RUNNABLE__])
        nID3([Running - RUNNABLE__])
        nID4([Dead - TERMINATED__])
        nID5([Waiting - BLOCKED, WAITING___])
        nID1 -->|_Started__| nID2
        nID2 -->|_dispatched by scheduler__| nID3
        nID3 -->|_yield__| nID2
        nID3 -->|_finished or error__| nID4
        nID3 -->|_waiting for some event__| nID5
        nID5 -->|_an event has occurred__| nID2
</div>
