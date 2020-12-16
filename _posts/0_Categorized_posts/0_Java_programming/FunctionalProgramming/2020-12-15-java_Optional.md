---
title: Java - Optional 
category: java
tags: java programming optional NPE
---

## Java - Optional 

- 다음처럼 Object에 Null이 assign되어 있는 경우에는 `java.lang.NullPointerException`이 발생합니다.

```java
String x = null;
// java.lang.NullPointerException: Cannot invoke "String.equals(Object)" because "x" is null
if (x.equals("aaa")) {
    System.out.println(x.toUpperCase());
}
```

- 물론 다음처럼 `null`인지 체크하는 코드를 넣으면 더 좋기는 한데, 코드가 좀 지저분해지죠.

```java
String x = null;
if (!x.equals(null)) {
    System.out.println(x.toUpperCase());
} else {
    System.out.println("x is not null");
}
```

- 따라서, `Optional<T>` 클래스가 등장하게 됩니다. 물론 이 클래스에도 `null` 값을 대입할 수는 있기는 합니다만, 그렇게 코딩하려면 `Optional`을 사용하는 의미가 없죠.
- `Optional<T>`는 일종의 Wrapper Class로 NPE가 발생하지 않도도록, null에 해당하는 값을 `empty`에 매핑해버리는 것이죠. 따라서, 해당 변수에 아무 객체가 연결되어 있지 않더라도, NPE가 발생하지 않게 됩니다. 
- 헷갈릴 수 있는데, 보통의 변수들이 Null이거나 NotEmpty이거나 로 관리된다면, `Optional`의 경우는 Empty이거나, NotEmpty이거나로 관리된다, 그래서 NPE가 발생할 수 없다 라고 이해하시면 됩니다.

```java
// null 대신 .empty를 사용해서 비워져 있음을 표시해주는 것이 좋습니다.
Optional<String> strEmpty = Optional.empty();

// 그럼 그냥 ""이랑 같은거 아니야? 라는 생각이 들지만, 그렇지 않습니다.
// 즉, 아직 값이 지정되지 않고 타입만 지정된 변수에 대해서, null 값을 대입시키는 것이 아니라
// .empty()를 사용해서 대입해두는 것이죠.
// 만약 strEmpty에 null이 들어있다면 아래 코드에서 NPE가 발생하게 됩니다.
// 하지만, .empty()를 사용했고 여기서는 NPE가 발생하지 않죠.
System.out.println( strEmpty.equals("") ); // false
System.out.println( strEmpty.equals(null) ); // false
```

## Optional.ofNullable.orElse()

- 자, 그럼 우리에게 `String` 변수 `unknownStr`이 있습니다. 얘는 `null`이 될 수도 있는 값이죠. 
- 얘를 `Optional.ofNullable`으로 감싸서 가져옵니다.
- 그 다음, `optionalStr.get()`으로 들어 있는 값을 가져오려고 하면, `NoSuchElementException`이 발생합니다. null이 아니기는 한데, 그렇다고 값이 들어가 있는 것은 아니니까요.

```java
// String이 null이 될 수도 있다고 합시다.
String unknownStr = null;

// Nullable, 즉 "Null이 될 수도 있는 변수"로부터 값을 가져옵니다.
// Optional.of(unknownStr)를 사용하면 NPE가 발생합니다.
Optional<String> optionalStr = Optional.ofNullable(unknownStr);

// 여기서 값을 가져오려고 하면 java.util.NoSuchElementException 가 발생합니다.
System.out.println(optionalStr.get());
```

- 그렇다면, 만약 null이 들어온 경우는 default 값을 지정할 수 있도록 해주는 것은 어떨까요? 그리고, 우리는 `String`을 가져오려는 것이지, Optional을 가져오려는 것이 아니니까요. 
- 따라서, `ofNullable`을 통해 null이 될수도 있는 변수를 가져온 다음, `.orElse` 메소드를 통해 `null`일 경우 특정 String을 자동으로 넣어주도록 처리합니다.
- 코드로 보면 다음과 같이 됩니다.

```java
// String이 null이 될 수도 있다고 합시다.
String unknownStr = null;
// Nullable, 즉 "Null이 될 수도 있는 변수"로부터 값을 가져오고
String strOrDefault = Optional.ofNullable(unknownStr).orElse("Default");
System.out.println(strOrDefault); // "Default"
```

## Optional method

- 그외에도 `Optional`로 감싸면 다음과 같이 유용한 method들이 더 있습니다.

```java
Optional<String> strOptional = Optional.of("frhyme");

// .ifPresent는 Consumer를 넘겨받아야 하며,
// strOptional에 값이 존재하면, 그 값을 Consumer에 넘겨줍니다.
strOptional.ifPresent((String x) -> System.out.printf("Value: %s\n", x));

// .ifPresentOrElse 는 Consumer와 Runnable을 넘겨받아서
// 1) 값이 존재하는 경우, 2)값이 존재하지 않는 경우 로 나누어 각각 실행해주죠.
strOptional.ifPresentOrElse(
        (String x) -> System.out.printf("Value Exists: %s\n", x),
        () -> System.out.printf("Value Not Exists:\n")
);
```

## Wrap-up

- NPE(Null Pointer Exception)은 매우 성가신데, `Optional`은 NPE를 피하면서, 비슷한 식으로 관리할 수 있도록 만들어진 Class죠.
- 물론, `x == null`와 같은 방식으로 null을 일일이 체크하면서 코드를 작성할 수도 있지만, 매번 그런 식으로 코드를 작성해버리면 매우 복잡하고 더러운 코드가 되기 쉽습니다. 따라서, `Optional`을 이용해서 처리하는 게 가독성 측면에서 훨씬 좋죠.
- 또한, `Optional` class는 Null이 발생했을 때 효과적으로 처리하기 위한 다양한 메소드들을 가지고 있으므로 편리한 점들이 있죠.
