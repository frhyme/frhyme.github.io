---
title: Java - Generic Programming - Wild Card
category: java
tags: java programming GenericProgramming WildCard
---

## Java - Generic Programming - Wild Card

- Java에서 Abstract Class인 `Number`는 `Integer`에게 상속됩니다. 따라서, 아래와 같이, `Number` 변수가 `Integer`객체를 가리킬 수 있죠.

```java
// Number는 Integer의 상위 Class이기 때문에
// Number는 Integer instance를 가리킬 수 있죠.
Number.class.isAssignableFrom(Integer.class); // true
Integer.class.isAssignableFrom(Number.class); // false
```

- 그렇다면, `List<Number>` 변수로 `List<Integer>` Instance를 가리키는 것 또한 가능할까요?
- 아래 코드를 실행해 보면 그렇지 않은 것을 알 수 있습니다. `List<Integer>`는 `List<Number>`를 상속받지 않고, 아예 다른 type으로 이해하죠.
- 이를 해결하기 위해서, wildcard가 필요합니다.

```java
import java.util.*;
import java.util.stream.*;
import java.util.Collections;

class Main {
    public static void main(String[] args) throws Exception {
        // Number는 Integer의 상위 Class이기 때문에
        // Number는 Integer instance를 가리킬 수 있죠.
        Number.class.isAssignableFrom(Integer.class); // true
        Integer.class.isAssignableFrom(Number.class); // false

        // 따라서, List<Number> 또한 List<Integer>의 상위 class가 되는게 아닐까요?
        List<Integer> listOfInteger = List.of(4, 5, 6);
        // 하지만, "incompatibe types"라는 메세지와 함께 컴파일이 되지 않습니다.
        // 즉, Number가 Integer의 상위 Class이기는 해도
        // List<Number> 와 List<Integer> 간에는 상속 관계가 성립하지 않는다는 이야기죠.
        List<Number> listOfNumber = listOfInteger;
        // java: incompatible types:
        // java.util.List<java.lang.Integer> cannot be converted to java.util.List<java.lang.Number>
    }
}
```

## Upper Bound Wildcard - ? extends ReferenceType

- `<? extends Number>`를 사용하여, "무엇인지 몰라도, Number를 상속받는 어떤 class가 전달된다는 것을 컴파일러에게 알려줍니다.
- 이렇게 변경한 다음 실행하면, 

```java
List<Integer> listOfInteger = List.of(4, 5, 6);
List<Double> listOfDouble = List.of(3.0, 4.0, 5.5);

// <? extends Number>를 사용하여, type을 정의해줄 경우
// Number를 상속하는 Integer, Double 모두 상요할 수 있습니다.
List<? extends Number> listOfNumber1 = listOfInteger;
List<? extends Number> listOfNumber2 = listOfDouble;

System.out.println(listOfNumber1); // [4, 5, 6]
System.out.println(listOfNumber2); // [3.0, 4.0, 5.5]
```

---

## Lower Bound Wildcard - ? super ReferenceType

- `<? extends ReferenceType>`는 `ReferenceType`을 상속받는 Type에 대해서 허용해줍니다.
- `<? super ReferenceType>`는 `ReferenceType`가 상속하는 Type에 대해서 허용해줍니다.
- 귀찮으므로...따로 예시를 들지는 않겠습니다 하하하.

--- 

## Unbounded Wildcard - ? 

- `<?>`를 사용해새서 어떤 type도 상관없도록 처리할 수도 있습니다.
- 그리고 이는 `<? extends Object>`와 동일하죠.

```java
List<Integer> listOfInteger = List.of(4, 5, 6);
List<Double> listOfDouble = List.of(3.0, 4.0, 5.5);

// <?>를 처리하면 어떤 것도 집어넣을 수 있습니다.
List<?> listOfAnything1 = listOfInteger;
System.out.println(listOfAnything1); // [4, 5, 6]

listOfAnything1 = listOfDouble;
System.out.println(listOfAnything1); // [3.0, 4.0, 5.5]

listOfAnything1 = listOfString;
System.out.println(listOfAnything1); // [a, b, c]
```
