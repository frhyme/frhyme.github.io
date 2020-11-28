---
title: Java - Generic Programming vs Object
category: 
tags: 
---

## Java - Generic Programming vs Object

- 프로그래밍할 때, 타입을 고정하지 않고 Class를 추상화하여 표현할 수 있죠. 이게 불가능하다면 알고리즘의 작동방식이 동일하더라도 Integer, String등 각각의 데이터 타입에 따라서 여러 Class를 정의해두어야 합니다. 단지 데이터 타입만 다를 뿐인데, 비슷한 코드를 여러 번 작성하는 것은 매우 비효율적이죠.
- 따라서, Generic Programming을 사용해서 이런 중복성을 해결할 수 있습니다만, 사실 그냥 Object를 이용해서 해도 됩니다. 
- 다음 두 챕터에서 각각 두 방법을 정리해볼게요.

## Generic Programming 

- Generic Programming을 사용해서 임의의 데이터타입인 `T`에 대한 Generic Class를 정의하였습니다. 이를 통해 어떤 DataType에 대해서도 Class를 정의할 수 있죠.

```java
public class GenericClass<T> {
    public T t;
    public GenericClass (T t){
        this.t = t;
    }
    public T get() {
        return this.t;
    }
}
```

- 그럼 아래와 같이, `String`이든 `Integer`이든 어떤 Class에 대해서도 알아서 작동하는 Generic CLass를 사용할 수 있는 것이죠.

```java
class Main {
    public static void main(String[] args) throws Exception {
        // USE Integer
        GenericClass<Integer> integerObj = new GenericClass<>(10);
        System.out.println(integerObj.get()); // 10
        // USE String
        GenericClass<String> stringObj = new GenericClass<>("abc");
        System.out.println(stringObj.get()); // abc
    }
}
```

## Class with Object

- 이번에는 그냥 Object Reference Type을 통해서 Generic Programming을 구현합니다. Java의 모든 Class를 Object Class를 상속받습니다. 그리고, 상위 Class Reference Variable은 하위 Class의 Object를 가리킬 수 있죠. 따라서, 지금처럼 내부에 Object Reference Variable을 만들어 두면, Java의 모든 Object들을 가리키게 할 수 있죠.

```java
public class ClassWithObject {
    public Object obj;

    public ClassWithObject(Object obj) {
        this.obj = obj;
    }
    public Object get() {
        return this.obj;
    }
}
```

- 아래 코드를 실행하면 Generic Programming과 동일한 결과가 나오는 것을 확인할 수 있습니다.

```java
class Main {
    public static void main(String[] args) throws Exception {
        // USE Integer
        ClassWithObject objWithInteger = new ClassWithObject(10);
        System.out.println(objWithInteger.get()); // 10 
        System.out.println("================");

        // USE String 
        ClassWithObject objWithString = new ClassWithObject("abc");
        System.out.println(objWithString.get()); // abc
        System.out.println("================");
    }
}
```

## Difference with GenericProgramming and ClassWithObject

- 그러나, Generic Programming이 더 타입변환 측면에서 더 안정적입니다.
- Generic Programming의 경우는 굳이 type을 신경 쓸 필요가 없는데요. Object를 사용하는 경우, type conversion 측면에서 문제가 발생할 수 있씁니다.

```java
// GenericClass의 경우는 TypeConversion을 해도 문제가 없습니다.
GenericClass<String> stringObj = new GenericClass<>("abc");
String a = stringObj.get();

// 하지만, Object의 경우는 Object를 String으로 변환해야 하므로 문제가 발생하죠.
ClassWithObject objWithString = new ClassWithObject("abc");
// java: incompatible types: java.lang.Object cannot be converted to java.lang.String
String b = objWithString.get();
// 물론, 얘도 explicit conversion을 하면 아무 문제가 없기는 합니다만.
String c = (String) objWithString.get();
```

## Wrap-up

- 결국, Object로도 Generic Programming을 비슷하게 해줄 수 있지만, Type Conversion 측면에서는 Generic Programming을 사용하는 것이 더 안정적이라는 이야기입니다. Object를 사용하는 경우에는 explicit type-casting을 해줘야해서 error가 발생할 가능성이 있죠. 반면, Generic의 경우는 Java Compiler가 typed을 관리해주기 때문에, 좀 더 안정적인 코딩을 할 수 있죠.
