---
title: Java - Method Reference
category: java
tags: java programming method class function FunctionalProgramming
---

## Java - Method Reference

- Java에는 이미 수많은 Class들과 Method들이 있습니다. Java에서 Function을 이용해서 프로그래밍을 한다고 할때, Class 혹은 Object의 Method들을 가져와서 동일한 기능을 가지는 함수로 사용할 수 있다면, 좀 더 유영한 프로그래밍이 가능하겠죠.
- 이처럼 Method를 가져와서 Function에 넣어주는 것을 **Method Reference**라고 합니다. `::`로 구분하여 앞에는 메소드가 속한 것을, 뒤에는 메소드이름을 써주면 됩니다.

```java
class_or_instanceName::itsMethodName
```

## Method Reference Example

- `Consumer`, `Supplier`, `Function` 3가지 타입에 대해서 Method Reference를 사용해주었습니다.

```java
import java.util.function.*;

class Main {
    public static Integer multiFunc(Integer x, Integer y, Function<Integer, Integer> func) {
        // x, y에 각각 func를 적용한 다음 곱을 리턴하는 함수
        return func.apply(x) * func.apply(y);
    }
    public static void main(String[] args) throws Exception {

        // --------------------------------------------
        // Consumer: input은 있으나, output이 없는 함수
        // System.out.println 은 static method이므로
        // className::methodName으로 사용합니다.
        Consumer<String> justPrintFunc = System.out::println;
        // 사실 그냥 이렇게 만들어도 되는 것이긴 하죠.
        Consumer<String> justPrintFuncAlt = (String s) -> System.out.println(s);
        // .accept method를 사용해서 input을 받습니다.
        justPrintFunc.accept("This is justPrintFunction"); // "This is justPrintFunction"
        justPrintFuncAlt.accept("This is justPrintFunctionAlt"); // "This is justPrintFunctionAlt"

        // --------------------------------------------
        // Supplier: input은 없지만, output은 있는 함수
        // scanner.nextLine 은 instance method이므로 Object를 생성한 다음
        // Object::methodName 로 사용합니다.
        Scanner scanner = new Scanner(System.in);
        Supplier<String> justReadFunc = scanner::nextLine;
        // Supplier의 경우 input이 없지만, ()는 써줘야 하죠.
        Supplier<String> justReadFuncAlt = () -> scanner.nextLine();
        // .get method를 사용해서 결과를 받습니다.
        justPrintFunc.accept(justReadFunc.get());

        // --------------------------------------------
        // Function에 Math.sqrt를 Binding해줍니다.
        Function<Double, Double> sqrt = Math::sqrt;
        System.out.println(sqrt.apply(9.0));
    }
}
```
