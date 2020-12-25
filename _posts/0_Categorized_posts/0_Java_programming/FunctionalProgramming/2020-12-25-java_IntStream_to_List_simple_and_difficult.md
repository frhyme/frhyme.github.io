---
title: Java - stream - IntStream to List
category: java
tags: java programming stream IntStream Collectors
---

## Java - stream - IntStream to List

- 아래 코드를 봅시다. `IntStream`에 대해서 간단한 `.filter`를 처리하고 `Collectors.toList()`를 통해 List로 변환해서 넘겨주는 것이죠.
- 언뜻 보기에는 잘 되는 것처럼 보이지만, 그렇지 않습니다.

```java
import java.util.*;
import java.util.stream.*;

class Main {
    public static void main(String[] args) throws Exception {
        List<Integer> lst = IntStream.rangeClosed(1, 10)
                .filter( x -> (x % 3 == 0) | (x % 7 == 0) )
                .collect(Collectors.toList());
        System.out.println(lst); // [3, 6, 7, 9]
    }
}
```

- 다음과 같은 오류 메세지가 뜹니다. `java.util.stream.IntStream`의 `.collect`는 3가지 타입의 argument를 필요로 하는데, 위 코드에서는 1개만 넘겨줬죠. 먼저 말하자면 이는 `IntStream`의 type이 primitive type이기 때문입니다.

```plaintext
java: method collect in interface java.util.stream.IntStream cannot be applied to given types;
  required: java.util.function.Supplier<R>,java.util.function.ObjIntConsumer<R>,java.util.function.BiConsumer<R,R>
  found:    java.util.stream.Collector<java.lang.Object,capture#1 of ?,java.util.List<java.lang.Object>>
  reason: cannot infer type-variable(s) R
    (actual and formal argument lists differ in length)
```

## Simple Solution - IntStream to List

- 가장 간단하게는 그냥 `int`를 `Integer`로 바꿔버리면 되죠. `.boxed()`를 사용하면 됩니다.

```java
import java.util.*;
import java.util.stream.*;

class Main {
    public static void main(String[] args) throws Exception {
        // Expected 3 arguments but found 1
        List<Integer> lst = IntStream.rangeClosed(1, 10)
                .filter( x -> (x % 3 == 0) | (x % 7 == 0) )
                // int를 Integer로 변경해줍니다.
                .boxed()
                .collect(Collectors.toList());
        System.out.println(lst); // [3, 6, 7, 9]
    }
}
```

- 혹은  `.mapToObj()`를 사용하면 됩니다.

```java
import java.util.*;
import java.util.stream.*;

class Main {
    public static void main(String[] args) throws Exception {
        List<Integer> lst = IntStream.rangeClosed(1, 10)
                .filter( x -> (x % 3 == 0) | (x % 7 == 0) )
                // int를 Integer로 변경해줍니다.
                .mapToObj(x -> Integer.valueOf(x))
                .collect(Collectors.toList());
        System.out.println(lst); // [3, 6, 7, 9]
    }
}
```

## Not Recommended Solution - IntStream to List

- 추천하지 않는 방식입니다만, 궁금증을 해결하기 위해서 정리합니다.
- `IntStream`은 primitive type을 각 요소로 가지기 때문에, `.collect`에 대한 정의가 다르게 되어 있습니다. 따라서, [Oracle - Java 8 - IntStream](https://docs.oracle.com/javase/8/docs/api/java/util/stream/IntStream.html)를 참고해 봅니다.
- 공식 문서를 보면, `IntStream.collect()`는 다음과 같은 3가지 형태의 `function`을 argument로 넘겨 받아야 합니다.

```java
// Performs a mutable reduction operation on the elements of this stream.
.collect(Supplier<R> supplier, ObjIntConsumer<R> accumulator, BiConsumer<R,R> combiner)
```

- 따라서 위 형식에 맞게 argument를 넘겨 주도록 합니다.
  - `Supplier<R> supplier`: `R`은 `IntStream`의 요소들이 담길 Container를 말합니다. 우리는 `List` 변수로 정의했으므로 `ArrayList`를 생성해주는 함수를 만들어야겠죠.
  - `ObjIntConsumer<R> accumulator`: `Object`와 `int`를 모두 argument로 받아서 Object에 int 요소를 넣어주는 작업을 수행합니다. Object는 ArrayList가 되겠죠.
  - `BiConsumer<R,R> combiner`: 두 ArrayList를 합쳐주는 작업을 수행합니다.

```java
import java.util.*;
import java.util.stream.*;

class Main {
    public static void main(String[] args) throws Exception {
        // Expected 3 arguments but found 1
        List<Integer> lst = IntStream.rangeClosed(1, 10)
                .filter( x -> (x % 3 == 0) | (x % 7 == 0) )
                .collect(
                        // java.util.function.Supplier<R>,
                        () -> new ArrayList(),
                        // java.util.function.ObjIntConsumer<R>
                        (ArrayList arrList, int x) -> arrList.add(x),
                        // java.util.function.BiConsumer<R,R>
                        (ArrayList left, ArrayList right) -> left.addAll(right)
                );
        System.out.println(lst); // [3, 6, 7, 9]
    }
}
```

## Reference

- [Stackoverflow - why cant maptoint be used with collect tolist](https://stackoverflow.com/questions/50552258/why-cant-maptoint-be-used-with-collecttolist)
- [Stackoverflow - collectors tolist showing error expected 3 argument but found 1](https://stackoverflow.com/questions/60438117/collectors-tolist-showing-error-expected-3-argument-but-found-1)
