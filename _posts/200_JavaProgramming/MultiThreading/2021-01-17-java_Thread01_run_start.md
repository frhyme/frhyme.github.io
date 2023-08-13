---
title: Java - MultiThreading - Make Thread
category: java
tags: java thread programming parallelism concurrency MultiThreading
---

## Java - MultiThreading - Make Thread

- 이제 직접 Thread를 만들어보겠습니다.
- Thread를 만드는데는 다음과 같은 두 가지 방법이 있습니다. 둘다 내부에서 `run()`을 Override 해줘야 하는 것은 동일하죠.
  1. Thread를 extends하여 새로운 Thread를 만들기
  2. Runnable을 implements하여 Runnable하기 만들기.
  3. Lambda expression을 사용하여 즉석으로 Thread만들기.

```java
// FirstThread.java
// 1) Thread를 extends하여 새로운 Thread를 만들기
public class FirstThread extends Thread {
    @Override
    public void run() {
        System.out.println(
            String.format("This is FirstThread Extends Thread: %s", this.getName())
        );
    }
}

// FirstRunnable.java
// 2) Runnable을 implements하여 생성
public class FirstRunnable implements Runnable {
    @Override
    public void run() {
        String thisName = Thread.currentThread().getName();
        System.out.println(
                String.format("This is FirstRunnable implements Runnable: %s", thisName)
        );
    }
}
```

- 그 다음 main code에서 각 Thread를 만드는 방법은 다음과 같습니다.
- 언뜻 보면, "Thread는 그냥 한 번에 만들 수 있으니까 더 좋은 것 아닌가?"싶지만, Java는 multi-inheritance를 지원하지 않습니다. 즉, Thread를 그대로 extends를 하는 경우 OOP의 중요한 성질인 polymorphism을 효과적으로 구현할 수 없다는 이야기죠. 따라서, 가능하다면 `Runnable`을 사용하는 게 코드의 재사용적인 측면이나, 일관성 측면에서 더 좋다고 말할 수 있겠습니다.

```java
import java.lang.*;

public class Main {
    public static void main(String[] args) throws Exception {
        // 1) Thread를 extends한 경우는 그냥 다음처럼 만들면 됩니다.
        Thread threadExtendsThread = new FirstThread();
        // 2) runnalbe을 사용한 경우 다음처럼 처리해줘야 하죠.
        Runnable runnable = new FirstRunnable();
        Thread threadByRunnable = new Thread(runnable);

        // 3) 다음처럼 lambda expression을 사용해서 바로 만들 수도 있죠.
        Thread threadByLambda = new Thread(
            () -> {
                String s = String.format("Thread By Lambda Expression: %s", Thread.currentThread().getName());
                System.out.println(s);
            }
        );

        // .run(): run은 Thread에서 정의해준 해당 method를 바로 실행해주는 것을 말합니다.
        // .start(): 얘는 Thread를 시작해주는 의미죠. 
        // start()도 결과적으로 run()을 실행해주기는 하는데, 즉시 실행되지는 않는다는 것이 run()과의 차이죠. 
        threadExtendsThread.run();
        runnable.run();
        threadByRunnable.run();
        threadByLambda.run();
        /*
        This is FirstThread Extends Thread: Thread-0
        This is FirstRunnable implements Runnable: main
        This is FirstRunnable implements Runnable: main
        Thread By Lambda Expression: main
        */
    }
}
```

## run, start

- Thread를 실행할 때는 `.run()`, `.start()`라는 두 가지 방법이 있습니다.
  - `.run()`의 경우는 해당 Thread의 method를 직접 실행한다는 말이죠. 따라서, `.run()`을 통해 보면, 코드의 라인 순서와 실행 순서가 동일한 것을 알 수 있습니다.
  - `.starts()`의 경우는 코드 순서와 실행 순서가 다른 경우들이 있습니다. 이는 즉시 메소드가 실행되는 것이 아니라, 새로운 스레드에 대한 call stack을 만들고, 이 call stack에 method를 적재한 다음, 실행하기 때문이죠. 따라서, thread가 start한 시점과, 메소드가 실행되는 시점에는 약간의 시차가 존재하게 됩니다.

```java
System.out.println("-- run() ---------------------------------");
threadExtendsThread.run();
threadByRunnable.run();
threadByLambda.run();
System.out.println("-- start() -------------------------------");
threadExtendsThread.start();
threadByRunnable.start();
threadByLambda.start();
System.out.println("-- Finished ------------------------------");
```

- 아래 결과를 보시면, `run()`을 실행한 경우에는 code의 순서와 실행된 순서가 동일한 것을 알 수 있죠. 하지만, `.start()`의 경우는 그 순서가 섞여 있습니다. 앞서 말한 것처럼, 메소드를 직접 실행한 것이 아니라, Thread에 대해서 호출 스택을 만들어준 다음 실행하기 때문에 시차가 존재하죠.
- 또한, `.run()`의 경우는 `FirstRunnable`와 `threadByLambda`의 경우 현재 Thread로 `"main"`를 출력합니다. 즉, Thread가 만들어진 것이 아니라, 그냥 method를 출력하는 것 뿐이기 때문에, 이렇게 되는 것이죠. 반면. `.start()`를 사용하는 경우, 정상적으로 Thread가 만들어져서 처리됩니다.

```plaintext
-- run() ---------------------------------
This is FirstThread Extends Thread: Thread-0
This is FirstRunnable implements Runnable: main
Thread By Lambda Expression: main
-- start() -------------------------------
-- Finished ------------------------------
This is FirstThread Extends Thread: Thread-0
This is FirstRunnable implements Runnable: Thread-1
Thread By Lambda Expression: Thread-2
```

## Wrap-up

- 보통 `Main.java`는 Main Thread(Thread-0)를 의미합니다. 만약 새롭게 정의한 Thread를 `start()`하는 경우에는 main thread와 동시에 돌아가기 때문에, 두 프로그램의 실행 결과가 뒤섞여서 실행되죠. 

---

## Raw Code

```java
// Main.java
import java.lang.*;

public class Main {
    public static void main(String[] args) throws Exception {
        Thread threadExtendsThread = new FirstThread();
        Runnable runnable = new FirstRunnable();
        Thread threadByRunnable = new Thread(runnable);
        Thread threadByLambda = new Thread(
            () -> {
                String s = String.format("Thread By Lambda Expression: %s", Thread.currentThread().getName());
                System.out.println(s);
            }
        );

        System.out.println("-- run() ---------------------------------");
        threadExtendsThread.run();
        threadByRunnable.run();
        threadByLambda.run();
        System.out.println("-- start() -------------------------------");
        threadExtendsThread.start();
        threadByRunnable.start();
        threadByLambda.start();
        System.out.println("-- Finished ------------------------------");
    }
}
```
