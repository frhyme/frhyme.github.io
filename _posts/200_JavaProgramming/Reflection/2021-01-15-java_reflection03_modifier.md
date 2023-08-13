---
title: Java - Reflection - Modifier
category: java 
tags: java reflection class reflection programming OOP modifier
---

## Java - Reflection - Modifier

- class 내 field, method등의 Modifier(`public`, `static` 등)을 확인하는 방법을 정리하였습니다.
- `AAA`는 다음과 같은 field를 가지고 있습니다. 이때, 각 field의 Modifier를 확인하는 방법을 정리하였습니다.
- 그리고, 이 글에서는 field에 대해서만 처리했지만, constructor를 포함한 모든 method에 대해서도 modifier를 확인할 수 있습니다.

```java
public class AAA{
    private int privateX;
    protected int protectedY;
    public int publicZ;
    public static int publicStaticX;

    public AAA() {
    }
}
```

- `Field`는 `.getModifiers()` 메소드를 사용해서 해당 `Field`에 속한 `Modifier`들을 확인할 수 있습니다. 다만, 이 값은 `int`죠. 엄밀히 따지면, 32bit로 구성되어있고, 각 bit의 값에 따라서, static인지, public인지 등을 확인할 수 있는데, 그냥 `Modifer.isStatic()`과 같은 방법으로 편하게 처리하였습니다.

```java
import java.lang.*;
import java.lang.reflect.Field;
import java.lang.reflect.Modifier;

import com.company.AAA;

class Main {
    public static void main(String[] args) throws Exception {
        System.out.println("---------------------------");
        for (Field f: AAA.class.getDeclaredFields()) {
            String fName = f.getName();
            // Modifier가 int형인 것에 유의하세요.
            // 사실 각 Modifier에는 대치되는 정수값이 있지만,
            // 뭐 몰라도 딱히 상관없습니다.
            int fModifier = f.getModifiers();
            String resultStr = "";
            if (Modifier.isStatic(fModifier)) {
                resultStr += "Static ";
            }
            if (Modifier.isPrivate(fModifier)) {
                resultStr += "Private ";
            }
            if (Modifier.isPublic(fModifier)) {
                resultStr += "Public ";
            }
            if (Modifier.isProtected(fModifier)) {
                resultStr += "Protected ";
            }

            System.out.printf("== Name: %s -> %s \n", fName, resultStr);
        }
        System.out.println("---------------------------");
        /*
        ---------------------------
        == Name: privateX -> Private  
        == Name: protectedY -> Protected  
        == Name: publicZ -> Public  
        == Name: publicStaticX -> Static Public  
        ---------------------------
        */
    }
}
```
