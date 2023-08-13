---
title: Java - Reflection - Basic
category: java 
tags: java reflection class reflection programming OOP 
---

## Java - Reflection - Basic

- Java의 Relfection은 Runtime시에 객체로부터 클래스의 정보를 가져오는 것을 말합니다. 
- 일반적으로는 다음과 같이 class instance를 만든 다음에는 내부 메소드에 직접 접근해서 변수를 처리하거나 해주죠.

```java
AAA a1 = new AAA();
```

- 하지만, Runtime에서 class에 접근하여, field, method, constructor에 접근 그리고 수정할 수 있도록 하는 것을 말합니다. 
- 사실 오늘 보여줄 에제에서는 딱히 장점이 보이지 않을 수 있지만, 외부에서 이미 만들어진 class Instance를 전달 받고 그 Instance를 직접 수정하거나 해야하는 경우에 유용하게 쓰일 수 있죠.
- 이를 위해서는 `java.lang.reflect` 패키지를 사용하게 되는데, 보통은 다음을 사용하게 됩니다.
  - `java.lang.reflect.Field`: 객체의 variable에 접근, 수정
  - `java.lang.reflect.Method`: 객체의 method에 접근, 수정
  - `java.lang.reflect.Constructor`: 객체의 생성자에 접근, 수정

## Example 

- 간단하게, `Field`, `Method`, `Constructor`를 사용해서 Instance에 접근하고 변경해주는 예제를 만들었습니다. 우선, `AAA`를 만들어줍니다.

```java
package com.company;

public class AAA{
    private int x;
    public AAA() {
    }
    public AAA (int x) {
        this.x = x;
    };
    public void setX(int x) {
        this.x = x;
    }
    public int getX() {
        return this.x;
    }
}
```

- 그리고, 내부에서 `Field`, `Method`, `Constructor`를 통해 객체에 접근해서 변수를 바꾸고, 메소드를 실행하고, 생성자를 실행하여 새로운 Instance를 실행하는 등의 일을 해봅니다.

```java
import java.util.*;

import java.lang.Class;
import java.lang.reflect.Field;
import java.lang.reflect.Method;
import java.lang.reflect.Constructor;

import com.company.AAA;

class Main {
    public static void main(String[] args) throws Exception {
        // Class를 통해 대상이 되는 class를 지정해줍니다.
        // 다음과 같은 두 가지 방법이 있죠.
        // 1) Class classRef = AAA.class;
        // 2) Class classRef = Class.forName("com.company.AAA");
        // 저는 첫번째로 하겠습니다.
        Class classRef = AAA.class;
        System.out.printf("class Name: %s \n", classRef.getName());
        // class Name: com.company.AAA

        System.out.println("====================================");
        // Constructor
        // Constructor 에 접근해 볼 수 있습니다.
        System.out.println("-- Constructor without argument ----");
        Constructor constructorWoArg = classRef.getDeclaredConstructor();
        AAA aWithoutArg = (AAA) constructorWoArg.newInstance();
        aWithoutArg.setX(777);
        System.out.printf("aWithoutArg.getX(): %d \n", aWithoutArg.getX()); // 777
        System.out.println("------------------------------------");
        System.out.println("-- Constructor with argument -------");
        Constructor constructorWithArg = classRef.getDeclaredConstructor(int.class);
        AAA aWithArg = (AAA) constructorWithArg.newInstance(555);
        System.out.printf("aWithArg.getX(): %d \n", aWithArg.getX());
        System.out.println("====================================");


        // Method
        // 당연히 Method에도 접근할 수 있습니다.
        System.out.println("====================================");
        System.out.println("-- Method --------------------------");
        Method setMethod = classRef.getDeclaredMethod("setX", int.class);
        Method getMethod = classRef.getDeclaredMethod("getX");
        AAA a3 = new AAA(333);
        setMethod.invoke(a3, 444);
        System.out.printf("getMethod.invoke(a3): %d \n", getMethod.invoke(a3));
        // 444
        System.out.println("====================================");

        // Field
        System.out.println("====================================");
        System.out.println("-- Field --------------------------");
        AAA a4 = new AAA(3);
        Field fieldX = classRef.getDeclaredField("x");
        fieldX.setAccessible(true);
        System.out.printf("fieldX.get(a4): %d \n", fieldX.get(a4)); // 10
        fieldX.set(a4, 999);
        System.out.printf("fieldX.get(a4): %d \n", fieldX.get(a4)); // 20
        System.out.println("====================================");
    }
}
```
