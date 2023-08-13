---
title: 왜 Java의 String은 Immutable하게 설계되었는가?
category: java
tags: java string 
---

## Java String is Immutable

- java에서 String은 Immutable합니다. 즉 한번 값을 지정했다면 그 값의 내부 원소를 수정할 수는 없다는 이야기죠.
- 물론, 아래처럼 변수에 들어 있는 값을 통째로 바꾸어주는 것이 가능하기는 한데, 엄밀히 따지면 이는 값을 수정했다기 보다, 원래 있던 값을 폐기하고 새로운 값을 지정했다고 보는게 맞겠죠.

```java
String s1 = "abc";
s1 = "def";
```

- "왜 번거롭게 이렇게 설계했지?"라는 생각이 들 수 도 있습니다만, 이렇게 설계함으로써 획득할 수 있는 장점이 있겠죠.
- 본 글에서는 Java의 String이 Immutable하여 획득할 수 있는 강점에 대해서 정리해보도록 하겠습니다.

## Java String Interning

### Same String have Same memory

- 아래 코드는 간단하게 같은 값을 가지는 문자열 `s1`, `s2`를 비교해주는 코드입니다. 이 때 String은 value type이 아니라, object type이므로 `==` 연산에서 값이 아닌 주소를 비교하게 됩니다.
- 따라서, false가 나와야 하는데 `true`가 나왔죠. 어찌된 일일까요?

```java
String s1 = "abc";
String s2 = "abc";

System.out.println(s1==s2); // true
```

### String Interning

- String Interning은 "같은 값을 가지면 굳이 다른 메모리에 분리해서 저장하지 않고 하나의 메모리 주소에 적어두고 서로 다른 변수들이 같은 메모리 주소를 가지도록 하는 것"을 말합니다.
- 반대로, 만약 `"abc"`라는 동일한 값을 여러 변수들이 함께 가지고 있다면, 이는 "같은 값을 굳이 여러 메모리에서 중복으로 저장함으로써 메모리를 낭비"하는 것이라고 볼 수도 있는 것이니까요.
- 따라서, String의 경우는 이전에 메모리에 저장된 값이 이후에 또 배정된다면, 새로운 메모리 공간을 확보해서 새로운 메모리 주소를 가리키도록 하는 것이 아니라, 원래 있던 메모리 주소를 가리키도록 합니다. 이 방법을 String Interning이라고 하죠.
- 그리고, 이때 "이미 만들어진 String을 위한 memory 공간"을 보통 **String Pool**이라고 부르며, 이 아이는 Java Heap Space에 존재해 있쬬.

### String Literal and String Object

- 다만, String Literal로 String을 만들었는지, String Object로 만들었는지에 따라서 Interning이 달라집니다.
- 아래에서 보시는 것처럼, String Literal `"abc"`로 넣으면 알아서 Interning이 처리되고 같은 메모리주소를 가리키도록 되죠.
- 하지만, `new String("abc")`으로 처리할 경우는 자동으로 interning이 되지 않습니다. 
- 이 경우에는 `.intern()`을 사용해서 Interning을 하도록 할 수 있죠.

```java
// String literal
String strLiteral1 = "abc";
String strLiteral2 = "abc";
// String Object
String strObj = new String("abc");
// String Object => Interning
String strObjInterned = new String("abc").intern();

// String literal으로 값을 넣은 경우에는 알아서 String Interning이 됨.
strLiteral1 == strLiteral2; // true
// 하지만, String Object로 새로운 String을 만들어서 집어넣은 경우는 Interning이 안됨.
strLiteral1 == strObj; // false
// 만약, 만들 때, .Intern() 메소드를 사용해서 넣어주었다면, 알아서 잘해줌.
strLiteral1 == strObjInterned; // true
```

## immutablity의 강점

- Security) 처음에 설정된 string이 중간에 바뀌게 되면, 이는 보안상의 문제가 발생할 수 있는 여지를 가지게 됩니다. 가령, 내가 비밀번호를 입력했는데, 프로그램이 돌아가면서 중간에 바뀐다? 이러면 문제가 심각하게 되는 것이죠. immutablity를 주입하고 이를 통해 프로그램 상에서 비밀번호가 바뀌면 에러가 발생하도록 함으로써, 보안상 강점을 획득할 수 있죠.
- Synchronization) 값이 한 번 정해지면 바뀌지 않는 다는 것은, 대략 함수형 프로그래밍 처럼 변수에 대해서 pipeline을 만들어서 처리하는 경우에, 병렬적으로 프로그래밍할 수 있도록 해줍니다. 만약 값이 중간에 바뀐다면 이 값으로 인해 다른 pipeline에 영향을 줄 수 있는데, 초기에 정해진 값이 이후에 바뀌지 않는다는 것이 확보된 상태면, 각 파이프라인들을 thread-safe하게 처리할 수 있거든요. 즉, 서로 다른 thread 간의 연산이 서로 독립적이라는 것이 확보된 상황이어서, 병렬적으로 파파팍 돌려버릴 수 있죠.

## Wrap-up

- python에서도 Interning이 자동으로 되는데, 기본적인 int에 대해서도 interning이 됩니다. 따라서, equality check를 할 때 유의해야 하는 부분들이 있죠.

---

## Reference

- [Why is String Immutable in Java](https://www.baeldung.com/java-string-immutable)
- [DZone - String : Why It is Immutable](https://dzone.com/articles/string-why-it-is-immutable)