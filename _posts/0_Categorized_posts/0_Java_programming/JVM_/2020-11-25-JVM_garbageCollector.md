---
title: JVM - Garbage Collector
category: java
tags: java programming JVM
---

## JVM - Garbage Collector

- C나 C++에서는 직접 `free`를 통해 메모리를 직접 해제해야 하지만, JVM에서는 Garbage Collector가 직접 알아서 메모리를 해제해줍니다. Java에서는 JVM의 heap memory에 `new`에 의해 생성되는 Object를 올려서 관리합니다. 그런데, 메모리를 효율적으로 사용하기 위해서, 더이상 Object가 필요없다는 판단이 들면 알아서 처리해주죠. 따라서, Java 개발자는 보통은 직접 GC를 관리할 필요가 없기는 한데, 더 잘 쓰기 위해서는 GC가 어떻게 메모리를 제거하는지, 언 정도 알고 있는 것이 좋습니다.
- 직접 GC를 호출하는 방법은 다음과 같은 두 가지가 있습니다.

```java 
System.gc()
Runtim.getRuntime().gc()
```

## Simpla Garbage Collector

- `System.gc()`를 통해 쓰지 않는 객체들을 모두 삭제하는 간단한 코드를 만들었습니다.

```java
import java.lang.Integer;

class Main {
    public static void main(String[] args) throws Exception {
        Runtime thisRuntime = Runtime.getRuntime();

        System.out.printf("Runtime Used Memory: %d\n", thisRuntime.totalMemory() - thisRuntime.freeMemory());
        for (int i = 0; i < 1_000; i++) {
            // 무의미하게 객체를 마구 생성해둡니다. 
            // 사실 Integer Constructor를 통해 Object를 만들었고, 얘는 Heap에 올라가게 되죠.
            // 그러나, 사실 쓸모없는 아이이기 때문에 gc를 call하게 되면 모두 deallocation됩니다.
            new Integer(i);
        }
        System.out.printf("Runtime Used Memory: %d\n", thisRuntime.totalMemory() - thisRuntime.freeMemory());
        System.gc();
        System.out.printf("Runtime Used Memory: %d\n", thisRuntime.totalMemory() - thisRuntime.freeMemory());
    }

}
```
