---
title: Java - Stream - Parallel Stream
category: java
tags: java programming stream parallel
---

## Java - Stream - Parallel Stream

- 말 그대로 stream을 병렬로 수행해주는 아이를 말하는데, 어렵지 않고 그냥 Stream에서 `.paralle()`를 호출한 다음 그냥 죽 이어서 하면 됩니다. 보통은 그냥 `.sequential()`로 생각하고 진행하게 되죠.
- 아래에서는 간단히, 1부터 1000000000(billion)까지 3의 배수들의 합을 구하는 연산을 수행하였는데, 첫번째에서는 `.parallel()`를 사용해서 병렬연산을 수행하였고, 두번째에서는 `.sequential()`(기본값)을 통해 그냥 실행했죠.
- 결과를 보시면 알겠지만, 병렬이 훨씬 빠릅니다.

```java
import java.util.stream.*;

class Main {
    public static void main(String[] args) throws Exception {
        // Parallel Stream
        // 아래 코드에서 보는 것처럼 그냥 기존 stream에 .parallel()
        // 를 붙여주기만 하면 됩니다.
        // Milli Seconds mean 0.001 sec
        long start_time = System.currentTimeMillis();
        // CODE START
        long s_parallel = LongStream
                .rangeClosed(1, 10_000_00000)
                .parallel()
                .filter(x -> x % 3 == 0)
                .sum();
        System.out.println(s_parallel); // 166666666833333333
        // CODE END
        long end_time = System.currentTimeMillis();
        System.out.println(end_time - start_time); // 657 milli seconds


        // Sequential Stream
        // 기본 실행이 sequential stream인데,
        // 굳이 강조하려고 아래애세, .sequential()를 사용하였습니다.
        start_time = System.currentTimeMillis();
        // CODE START
        long s_single = LongStream
                .rangeClosed(1, 10_000_00000)
                .sequential()
                .filter(x -> x % 3 == 0)
                .sum();
        System.out.println(s_single); // 166666666833333333
        // CODE END
        end_time = System.currentTimeMillis();
        System.out.println(end_time - start_time); // 2216 milli seconds
    }
}
```

- 다만, `filter`, `map`과 같이 StateLess한 연산의 경우는 다연히 서로 다른 요소 간에 겹치지 않으니까 parallel로 실행했을 때 이점이 있지만, `limit`, `sorted`, `distinct`, `reduce` 등은 다른 원소들의 값에 영향을 받게 되므로 병렬적으로 수행하기 어렵습니다.
- 그리고, 일반적으로 병렬처리를 하려면, job을 분배해줘야 하는 일이 생기기 때문에 고정적인 비용이 소요되죠. 따라서, 데이터가 크지 않다면, sequential로 처리해주는 것이 훨씬 이롭습니다.

## Paralle Sorting

- 정렬(Sorting)의 경우 순서가 지켜져야 합니다. 그러나, 만약 병렬로 처리를 하게 되면 순서가 지켜지기 어렵죠.
- 따라서, 이 때는 `forEachOrdered`를 사용해야 합니다.

```java
import java.util.*;
import java.util.stream.*;

class Main {
    public static void main(String[] args) throws Exception {
        List<Integer> numbers = List.of(6, 5, 4, 3, 2, 1);

        // parallel, sorted 순으로 처리하게 되면
        // 병렬처리된 stream에 대해서 정렬한 다음 조합하게 되므로
        // 우리의 예상과는 다른 결과가 나오게 됩니다.
        numbers.parallelStream()
                .sorted()
                .forEach( x -> System.out.printf("%d ", x));
                // 4 5 2 3 6 1
        
        // 따라서, forEachOrdered 를 써야 하죠.
        // forEachOrdered는 Stream간의 기존 순서를 유지해준다는 것을 의미합니다.
        numbers.parallelStream()
                .sorted()
                .forEachOrdered(x -> System.out.printf("%d ", x));
                // 1 2 3 4 5 6
    }
}
```
