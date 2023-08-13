---
title: Java - Generic Programming
category: java
tags: java programming GenericProgramming
---

## Java - Generic Programming

- Generic Programming은 변수의 타입과 상관없이 프로그래밍할 수 있도록 하는 것을 말합니다. 아주 간단하게 '정렬'을 예로 들자면, 변수타입이 Int이든, Double이든, String이든 간에, 비교 연산자만 제대로 설정되어 있다면 동일한 메커니즘을 제공하는 함수를 만들어준다는 이야기죠. 즉, 알고리즘의 추상화 라고 말할 수 있겠습니다.
- C++에는 Template을 사용해서 이걸 할 수 있고, python은, 뭐 그냥 웬만하면 될겁니다. 처음부터 타입이 정해져 있지 않기 때문에, 기본적으로 어느 정도 generic programming을 지원하는 거죠.

## Simple Example

- 아래와 같이 추상화하려는 변수, argument, returnType 등을 `T`로 정의해줍니다.

```java
public class GenericArray<T> {
    private T[] lst;

    GenericArray(T[] inputLst) {
        this.lst = inputLst;
    }
    public T getLast() {
        return lst[lst.length - 1];
    }
    public T getFirst() {
        return lst[0];
    }
}
```

- 그리고, 아래와 같이, 

```java
import java.lang.Integer;

class Main {
    public static void main(String[] args) throws Exception {
        /*
        * Primitive type은 T로 쓰일 수 없습니다.
        * 아래와 같이, var로 표현해서 사용해도 됩니다.
        * var IntegerArr = new GenericArray<Integer>(new Integer[] {1, 2, 3});
        * 아래처럼 <> 를 사용해서 그냥 넘겨 버려도 되구요.
        * var IntegerArr = new GenericArray<>(new Integer[] {1, 2, 3});
        * */
        GenericArray<Integer> IntegerArr = new GenericArray<Integer>(new Integer[] {1, 2, 3});

        System.out.println(IntegerArr.getLast());
        System.out.println(IntegerArr.getFirst());

        GenericArray<String> StringArr = new GenericArray<String>(new String[] {"a", "b", "c"});

        System.out.println(StringArr.getLast());
        System.out.println(StringArr.getFirst());
    }
}
```
