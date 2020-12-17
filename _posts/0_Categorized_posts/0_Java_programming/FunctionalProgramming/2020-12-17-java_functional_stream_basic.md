---
title: Java - Functional Stream - Basic 
category: java
tags: java programming stream list reduce map filter FunctionalProgramming
---

## Java - Functional Stream 

- Java에서 List와 같이 연속된 값들을 처리할 때는 두 가지 방식이 있습니다. `for`문을 사용하는 방법과, `.stream()`을 통해 method를 chaining해 가면서 쓰는 방법이 있죠.

```java
import java.util.List;
import java.util.function.*;
import java.util.stream.*;

class Main {
    public static void main(String[] args) throws Exception {
        // 다음과 같이 1부터 9까지 연속된 값들이 list에 들어 있다고 하겠습니다.
        List<Integer> integerLst = List.of(1, 2, 3, 4, 5, 6, 7, 8, 9);

        // LOOP를 쓰면 다음처럼 해야 합니다.
        for (Integer x: integerLst) {
            if (x % 2 == 0) {
                System.out.println(x);
            }
        }
        // Stream을 쓰니까 얼마나 예쁜지요?
        // .filter: Predicate(boolean을 리턴하는 function)을 사용하여 true인 애만 남김
        // .forEach: Consumer를 사용하여 각 원소에 대해서 function을 수행함
        System.out.println("==============================");
        integerLst.stream()
                .filter((Integer x) -> x % 2 == 0)
                .forEach( (Integer x) -> System.out.println(x) );
        
        // .count: 현재 list의 원소 개수를 셈
        integerLst.stream().count(); // 9
        System.out.println("----");
        // .skip: head부터 4개의 숫자를 제외함.
        integerLst.stream().skip(4)
                .forEach( (Integer x) -> System.out.println(x));

    }
}
```

- `Stream<T>`에 집어넣어서 처리해줘도 되는데, 이렇게 할 경우 한 번 읽어들인 다음, 또 읽으려고 하면 에러가 발생하죠.

```java
// 이렇게 Stream을 변수에 넣어놓고 진행할 경우 반복해서 수행할 수 없습니다.
Stream<Integer> integerLstStream = integerLst.stream();
System.out.println(integerLstStream.count());

// java.lang.IllegalStateException: stream has already been operated upon or closed
System.out.println(integerLstStream.count());
```

## Intermediate and Terminal method

- 여기서 method들은 Intermediate, Terminal로 구분됩니다. 
- Intermediate method에는 대표적으로 `.filter` 가 속합니다. Intermediate method는 lazy evaluation으로 수행되는데, 당장 값을 계산해주는 것이 아니라, intermediate method들이 나올 때까지 참다가 terminal method가 나오면 그 때 값을 계산해주는 것이죠. 
- terminal method의 경우는 값 자체를 가져와서 이전에 연결된 intermediate method를 모두 한번에 수행해 주게 되죠. `.forEach`나, `.count`가 여기에 속합니다. 당연하지만, stream에서는 terminal이 나온 다음에는 다시 intermediate method를 연결할 수 없습니다. 그 stream은 계산이 완료되었다, 라고 보는 것이죠. 만약, 여기서 계속 뭔가를 하려고 하면, `IllegalStateException`이 발생하게 됩니다.

```java
import java.util.List;

class Main {
    public static void main(String[] args) throws Exception {
        // size가 큰 Integer List를 만들었습니다.
        List<Integer> integerLst = new ArrayList<>();

        for (int i = 0; i < 10000; i++) {
            integerLst.add(i);
        }
        /*
        * 여러 조건을 걸어서 그 조건에 부합하지 않는 정수의 수를 센다고 해봅시다.
        * 아래처럼 stream().filter()....filter()로 조건을 걸게 되는데요
        * 이 때 만약, filter() 메소드마다 매번 전체 list를 훑고 또 훑는다면
        * 현재 filter의 수 * List의 수 만큼 계산을 해야 합니다.
        * 하지만, 모든 filter를 묶어서, 나중에 한 번만 연산을 해준다면
        * List의 수 만큼 한번만 연산해주면 되는 것이죠.
        * filter: Intermediate Method이므로 나중에 몰아서 연산되고
        * count: terminal method입니다. 사실, 얘는 리스트를 훑지 않으면 계산을 할수 없으니까요.
         * */
        long xx = integerLst.stream()
                .filter((Integer x) -> x % 2 != 0)
                .filter((Integer x) -> x % 3 != 0)
                .filter((Integer x) -> x % 5 != 0)
                .filter((Integer x) -> x % 7 != 0)
                .filter((Integer x) -> x % 11 != 0)
                .filter((Integer x) -> x % 13 != 0)
                .count();
    }
}
```

- Intermediate method에는 다음과 같은 것들이 있습니다.
- 또한, Intermediate method들은 terminal method를 만나기 전까지는 값을 evalute하지 않으므로, 출력한다고 해도 아직은 제대로 된 값이 출력되어 나오지 않습니다.

```java
List<Integer> integerLst = new ArrayList<>();

for (int i = 0; i < 100; i++) {
    integerLst.add(i);
}
// ================================================
// Intermediate Method
// .filter: Predicate function을 만족하는 원소만 남김
integerLst.stream().filter((Integer x) -> x % 7 == 0);
// .limit: 처음 N개의 원소만 남김
integerLst.stream().limit(10);
// .skip: 처음 N개의 원소를 건너뜀.
integerLst.stream().skip(10);
// .distinct: .equals method를 사용하여 unique한 원소만 남김
integerLst.stream().distinct();
// .sorted: 정렬함.
integerLst.stream().sorted();
// .map: 각 원소에 function을 적용함
integerLst.stream().map((Integer x) -> x * x);
```

- 몇몇 Terminal method의 경우 `Optional` type으로 리턴하는데, 이는 해당 stream이 비어 있을 때 NPE를 생성하는 것을 방지하기 위해서죠.

```java
// size가 큰 Integer List를 만들었습니다.
List<Integer> integerLst = new ArrayList<>();

for (int i = 0; i < 100; i++) {
    integerLst.add(i);
}

// ================================================
// Terminal Method

// .count: 현재 원소의 개수를 long type으로 리턴함.
System.out.println(integerLst.stream().count()); // 100

// .max/min: 넘겨 받은 Comparator에 따라서 가장 큰 값, 작은 값은 Optional type으로 넘겨준다.
integerLst.stream().max(Integer::compareTo); // 99

// .reduce: 두 변수 에 대한 binaryFunction 적용을 연속해서 합니다.
// (a, b, c)에 + 연산을 한다면 (a + b) + c 가 되겠죠.
integerLst.stream().reduce((Integer x, Integer y) -> x + y); // 4950\

// .foreach: stream의 모든 원소에 대해서 consumer function을 수행함
integerLst.stream().forEach((Integer x) -> System.out.println(x));
```
