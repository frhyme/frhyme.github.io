---
title: Java - Stream - infinite Stream
category: java
tags: java programming stream
---

## Java - infinite Stream - generate, iterate

- `Stream.generate(supplier)`의 경우 전달받은 `supplier`에 따라 무한히 값을 생성해내는 stream입니다.

```java
import java.util.stream.*;

class Main {
    public static void main(String[] args) throws Exception {
        // Infinite Stream
        // Stream.generate(Supplier)
        // Supplier는 input은 없고, output만 있는 function이죠.
        // infStream_alwaysReturn10은 항상 10을 리턴하는 supplier를 전달받았습니다.
        Stream<Integer> infStream_alwaysReturn10 = Stream.generate( () -> 10);
        infStream_alwaysReturn10.limit(5).forEach(
                x -> System.out.printf("%d ", x)
        ); // 10 10 10 10 10
        System.out.println("====");

        // infStream_alwaysReturnRandom은 Random을 리턴하는 supplier를 넣어주었습니다.
        // Math.random()은 seed를 현재 시간을 사용해서 집어넣기 때문에 seed를 고정할 수 없습니다.
        Stream<Double> infStream_alwaysReturnRandom = Stream.generate( () -> Math.random());
        infStream_alwaysReturnRandom.limit(3).forEach(
                x -> System.out.printf("%f ", x)
        ); // 0.715705 0.227926 0.006454
        System.out.println("====");
    }
}
```

- `Streamd.iterate(seed, unaryOperator)`의 경우 seed로부터 출발해서, `unaryOperator`를 적용하여 순차적으로 값을 넣어주죠. 그냥 무한 등차수열 같은 애를 만들 수 있다, 라고 생각하시면 됩니다.

```java
import java.util.stream.*;

class Main {
    public static void main(String[] args) throws Exception {
        // Stream.iterate(seed, unaryOperator)는
        // seed부터 출발하여 unaryOperator를 적용하여 새로운 값을 생성해주죠.
        // .takeWhile(predicate)를 사용해서 해당 조건이 만족되지 않으면 Stream이 끝나도록 만들었습니다.
        Stream<Integer> infStream_iterate1 = Stream.iterate(1, x -> x + 3);
        infStream_iterate1.takeWhile( x -> x < 10).forEach(
                x -> System.out.printf("%d ", x)
        ); // 1 4 7
        System.out.println("====");
    }
}
```
