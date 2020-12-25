---
title: Java - Stream - IntStream vs. IntegerStream
category: java
tags: java stream IntStream programming int Integer sum
---

## Java - Stream - IntStream vs. IntegerStream

- 다음과 같은 간단한 코드가 있습니다. 간단히, `List<Integer>`의 요소들의 합을 모두 게산해주는 코드죠.
- 코드에 오류가 없을까요?

```java
import java.util.*;
import java.util.stream.IntStream;
import java.util.stream.Stream;
// import java.util.stream.*;

class Main {
    public static void main(String[] args) throws Exception {
        List<Integer> lstOfInteger = List.of(1, 2, 3, 4, 5, 5);
        System.out.println(
                lstOfInteger.stream().sum()
        );
    }
}
```

- 위 코드를 실제로 실행해 보면 다음과 같은 오류가 생깁니다.
- `Stream<Integer>`에 `.sum()`가 존재하지 않는다는 이야기죠.
- 사람은 `Stream<Integer>`가 정수로 구성되어 있으니, `.sum()` 메소드가 당연히 있는 것 아니야? 라고 생각할 수 있지만, 컴파일러는 그냥 Stream이라고만 생각합니다. 따라서, 애초에 `.sum()` 자체가 interface에 없는 것이죠.

```plaintext
java: cannot find symbol
  symbol:   method sum()
  location: interface java.util.stream.Stream<java.lang.Integer>
```

- 물론, 이런 경우에는 그냥 `Stream<Integer>`를 `IntStream`으로 변경해주면 끝나는 문제입니다. `IntStream`은 대놓고 `int`, 즉 정수로 구성되어 있기 때문에 Interface 자체에 `.sum()`가 존재하죠.
- 따라서 다음처럼 바꿔서 실행하면 오류 없이 잘 됩니다.

```java
List<Integer> lstOfInteger = List.of(1, 2, 3, 4, 5, 5);
// 얘는 Stream<Integer> 입니다.
// 컴파일러는 Integer는 신경쓰지 않고 Stream말 알고 있고,
// Stream Interface에는 .sum method가 없습니다.
Stream<Integer> streamOfInteger = lstOfInteger.stream();

// 얘는 IntStream입니다.
// IntStream은 정수형이므로 Interface에 .sum method가 존재합니다.
// streamOfInteger의 뒤에 .mapToInt를 사용해서 Integer 를 int로 변환해줬죠.
IntStream streamOfInt = lstOfInteger.stream().mapToInt(x -> x);

System.out.println(streamOfInt.sum()); // 20 
```

- 물론, 그냥 `.reduce()`를 사용해서 다음처럼 처리하는 것도 가능하죠.

```java
List<Integer> lstOfInteger = List.of(1, 2, 3, 4, 5, 5);
// 물론 이런 식으로 해줘도 됩니다만,
System.out.println( 
    lstOfInteger.stream()
            .reduce( (x, y) -> x + y )
            .orElse(0) 
);
```

## Reference

- [Stackoverflow - java 8 streams why cant I sum a stream of integers](https://stackoverflow.com/questions/51367853/java-8-streams-why-cant-i-sum-a-stream-of-integers)
