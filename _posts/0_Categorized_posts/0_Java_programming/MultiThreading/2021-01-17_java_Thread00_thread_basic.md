---
title: Java - MultiThreading - Thread Basic
category: java
tags: java thread programming parallelism concurrency MultiThreading
---

## Java - MultiThreading - Threads

- java는 기본적으로 JVM 레벨에서 Multi Thread를 지원합니다. 사실 우리가 `main`이라는 이름으로 돌리는 코드가 이미 JVM에서 알아서 인식해서 만들어내는 Thread인 거죠. 물론 그 외에도 GC(Garbage Collector)도 기본적으로 생성되는 Thread죠.
- Java에서 현재 실행되고 있는 Thread에 접근하여, 기본적인 정보들을 찾는 방법을 정리하였습니다.
  - `Thread.currentThread()`: 현재 Thread를 가져옵니다.
  - `.getPriority()`: 현재 Thread의 우선순위를 파악합니다.
  - `.isAlive()`: Thread가 살아ㅣ 있는지 확인합니다.
  - `.isDaemon()`: 현재 Thread가 daemon인지 확인합니다. Daemon은 UNIX 용어에서 온 말인데, Garbarge Collection처럼 낮은 우선순위를 가지지만 BackGround에서 계속 돌아가는 Thread를 말하죠.보통 NonDaemon 쓰레드들은 Daemon 쓰레드들이 존재할 때만 존재합니다. 가령 Daemon Thread가 없는데, GC같은 게 있는건 아무 의미가 없으니까요.

```java
import java.lang.*;

public class Main {

    public static void main(String[] args) throws Exception {
        // main Thread
        // .currentThread():
        // 현재 실행되고 있는 Thread를 찾습니다.
        Thread thrd = Thread.currentThread();

        System.out.println("---------------------------------");
        System.out.println("thrd.getId(): " + thrd.getId());
        System.out.println("thrd.getName(): " + thrd.getName());
        // .getPriority(): 현재 Thread의 우선순위를 파악합니다.
        // 우선순위가 높으면, 낮은 Thread에 비해서 먼저 실행되죠.
        System.out.println("thrd.getPriority(): " + thrd.getPriority());
        // .isAlive(): Thread가 아직 살아 있는지 확인합니다.
        System.out.println("thrd.isAlive(): " + thrd.isAlive());
        // isDaemon(): 현재 Thread가 daemon인지 확인합니다.
        // Daemon은 UNIX 용어에서 온 말인데, Garbarge Collection처럼 낮은 우선순위를 가지지만,
        // BackGround에서 계속 돌아가는 Thread를 말하죠.
        // 보통 NonDaemon 쓰레드들은 Daemon 쓰레드들이 존재할 때만 존재합니다.
        // 가령 Daemon Thread가 없는데, GC같은 게 있는건 아무 의미가 없으니까요.
        System.out.println("thrd.isDaemon(): " + thrd.isDaemon());
        System.out.println("---------------------------------");
    }
}
```
