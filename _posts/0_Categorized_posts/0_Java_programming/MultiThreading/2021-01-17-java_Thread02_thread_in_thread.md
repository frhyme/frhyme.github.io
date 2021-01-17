---
title: Java - MultiThreading - Thread in Thread
category: java
tags: java thread programming parallelism concurrency MultiThreading
---

## Java - MultiThreading - Thread in Thread

- Thread 안에 Thread가 있는 경우를 한번 만들어보도록 하겠습니다.

```java
public class FirstThread extends Thread {
    private String name;
    // 생성자. 
    public FirstThread(String name) {
        this.name = name;
    }

    @Override
    public void run() {
        // 현재 Thread의 이름을 출력하고,
        System.out.println(
            String.format("This is FirstThread: %s", this.name)
        );
        // lambda expr를 사용해서 새로운 Thread를 만들어 줍니다.
        Thread threadByLambda = new Thread(
                () -> {
                    String s = String.format("This is subThread in FirstThread: %s", this.name);
                    System.out.println(s);
                }
        );
        // 그리고 .start()를 통해 실행해줍니다.
        threadByLambda.start();
    }
}
```

- `Main.java`는 다음과 같이 구성하였습니다.
  - `"Main Thread Start"`는 Thread가 생성되기 전이므로 가장 먼저 출력되겠죠.
  - Thread는 해당 Thread의 subThread보다는 무조건 먼저 출력되겠죠.
  - 다만, `"A"`가, 먼저 출력될지, `"B"`가 먼저 출력될지는 모릅니다. Concurrent하게 수행되니까요.
  - `"Main Thread End"` 또한 언제 출력될지 모릅니다. 얘 또한 Main Thread에서 돌아가는 것이니까요.

```java
import java.lang.*;

public class Main {
    public static void main(String[] args) throws Exception {
        System.out.println("Main Thread Start");
        Thread thread1 = new FirstThread("A"); // Thread A
        Thread thread2 = new FirstThread("B"); // Thread B
        thread1.start();
        thread2.start();
        System.out.println("Main Thread End"); // Main Thread
    }
}
```

- 결과를 보시면 위에서 말한 것과 같이 실행되는 것을 알 수 있습니다.

```plaintext
Main Thread Start
Main Thread End
This is FirstThread: A
This is FirstThread: B
This is subThread in FirstThread: A
This is subThread in FirstThread: B
```
