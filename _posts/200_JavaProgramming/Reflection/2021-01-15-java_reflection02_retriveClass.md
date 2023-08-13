---
title: Java - Reflection - Retrieving Class
category: java 
tags: java reflection class reflection programming OOP 
---

## Java - Reflection - Retrieving Class

- `java.lang.Class`를 통해, Class에 접근할 수 있는 다양한 방법을 정리하였습니다.

```java
import java.util.*;
import java.lang.Class;
import java.lang.*;

class Main {
    public static void main(String[] args) throws Exception {
        // Class에서 .class 메소드를 사용해서 바로 가져올 수도 있구요.
        Class classRef0 = String.class;
        Class classRef1 = int.class;
        /////////////////////////////////////////////////////////

        // Class.forName():
        // class의 경로를 사용해서 가져올 수도 있구요.
        Class classRef2 = Class.forName("java.lang.String");
        /////////////////////////////////////////////////////////

        // Instance.getClass()를 사용해서 가져올 수도 있습니다.
        Class classRef3 = "AAA".getClass();
        /////////////////////////////////////////////////////////

        // Array
        // 만약 Array를 가져오고 싶다면 앞에 '['를 붙이면 됩니다.
        // [I: int array
        // [F: float array
        // [Z: boolean
        // [B: byte
        // [C: char
        // [L<className>: class나 interface
        // [D: double
        // [J: long
        // [S: short
        // Class intArrClass = int[].class;
        Class intArrClass = Class.forName("[I");
        // primitive type이 아니라, class에 대해서 만들고 싶다면,
        // 시작할때 [L 을 붙이고, 끝에는 ; 을 붙여주면 됩니다.
        Class StringArrClass = Class.forName("[Ljava.lang.String;");
        // .componentType()을 사용해서 내부 원소의 type을 확인할 수 있죠.
        System.out.println(intArrClass.componentType()); // int
        System.out.println(StringArrClass.componentType());
        // java.lang.String
        /////////////////////////////////////////////////////////

        // Super Class
        // .getSuperclass()를 사용해서 상위 클래스에 접근할 수도 있습니다.
        System.out.println(String.class.getSuperclass());
        // class java.lang.Object
    }
}
```
