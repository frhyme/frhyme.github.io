---
title: Java - Thread - Executors
category: java
tags: java thread programming parallelism concurrency MultiThreading
---

## Java - Thread - Executors

- Thread가 몇 개 되지 않을때는 관리가 어렵지 않지만, 가령 100개가 넘어간다면 관리가 배우 어려워지죠.
- Java의 `ExecutorService`는 multi-thread를 효과적으로 관리할 수 있도록 해줍니다. Task Queue를 만들어, 실행되어야 하는 Task를 대기하게 하고, Resource(Thread) Pool을 만들어서, 각 Task를 실행해줍니다.
- 그림으로 그린다면 대략 다음과 같죠.

<div class="mermaid">
    flowchart LR;
        nID1["Task Submitter__"]
        subgraph subG0["Executor Service__"]
            subgraph subsubG0["Task Queue__"]
                subsubG0n1["Task_1__"]
                subsubG0n2["Task_2__"]
                subsubG0n3["Task_3__"]
            end
            subgraph subsubG1["Thread Pool__"]
                subsubG1n1["Thread_1__"]
                subsubG1n2["Thread_2__"]
                subsubG1n3["Thread_3__"]
            end
            subsubG0 --> subsubG1n1
            subsubG0 --> subsubG1n2
            subsubG0 --> subsubG1n3
        end
        nID1 --> subsubG0
</div>

## Simple Example

- 간단한 예제를 만들어 봤습니다.

```java
package com.company;

import java.util.concurrent.Executors;
import java.util.concurrent.ExecutorService;

public class Main {
    public static void main(String[] args) throws Exception {
        // Thread Pool의 크기가 8인 Executor를 만들어 줍니다.
        int poolSize = Runtime.getRuntime().availableProcessors();
        System.out.printf("== poolSize: %d Cores\n", poolSize);
        ExecutorService executorService = Executors.newFixedThreadPool(poolSize);
        // .submit은 Thread, Runnable을 전달받습니다.
        // 즉 실행 가능한 놈을 전달해주는 것이죠.
        for (int i=0; i < 16; i++) {
            int taskNumber = i;
            // executorService에 새로운 thread를 등록해줍니다.
            executorService.submit(
                new Thread(
                    () -> {
                        String taskName = "task-" + taskNumber;
                        String threadName = Thread.currentThread().getName();
                        System.out.printf(
                            "%s is executed by %s \n", taskName, threadName
                        );
                    }
                )
            );
        }
        TimeUnit.MILLISECONDS.sleep(50);
        executorService.shutdown();
        System.out.println("Completed");
    }
}
```
