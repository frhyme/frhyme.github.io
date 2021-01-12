---
title: Java - Double Brace Initialization
category: java
tags: java programming class HashMap
---

## Java - Double Brace Initialization

- Java에는 Double Brace Initialization이라는 것이 있습니다. 가령 HashMap을 만들고 그 즉시 값도 집어넣고 싶을 때, Double Brace Initialization을 사용할 수 있죠. 
- 아래 코드에서 보시면 `new HashMap<>(){{ ... }}` 사이에서 `put()` 메소드를 사용해서 `(key, value)`를 모두 넘겨줬죠. 이를 통해 선언하면서 바로 내부 요소들까지 집어넣어줄 수 있습니다.

```java
import java.util.*;

class Main {
    public static void main(String[] args) throws Exception {
        // Double Brace Initialization
        HashMap<String, String> hashMap2 = new HashMap<>() {{
            put("A", "1"); put("B", "2");
        }};
        System.out.println(hashMap1);
        // {A=1, B=2}
    }
}
```

- 아, 역시 그렇지, python처럼 java에서도 이렇게 깔끔하게 만들어주는게 필요해, 라고 생각하셨을 수 있지만, 사실 이렇게 만들 경우, class가 달라집니다. 아래에서 보시는 것처럼 결과는 같지만, class를 확인하면 class가 서로 다른 것을 알 수 있습니다.

```java
import java.util.*;

class Main {
    public static void main(String[] args) throws Exception {
        // hashMap1은 보편적인 방법으로 HashMap을 만들어 주고
        // .put method를 통해서 key, value를 넣어주죠.
        HashMap<String, String> hashMap1 = new HashMap<>();
        hashMap1.put("A", "1");
        hashMap1.put("B", "2");

        // hashMap2은 Double Brace Initialization을 통해 처리합니다.
        HashMap<String, String> hashMap2 = new HashMap<>() {{
            put("A", "1"); put("B", "2");
        }};

        // 들어온 값은 동일하지만, 
        System.out.println(hashMap1); // {A=1, B=2}
        System.out.println(hashMap2); // {A=1, B=2}

        // Class들이 서로 다른 것을 알 수 있죠. 
        // 사실, hashMap2은 anonymous class로 넘어오게 됩니다.
        System.out.println(hashMap1.getClass());
        // class java.util.HashMap
        System.out.println(hashMap2.getClass());
        // class com.company.Main$1
    }
}
```

## Summary 

- 정리하자면, Double Brace를 사용하면, 생성과 초기화를 한번에 할 수 있어서 코드의 가독성이 높아지죠.
- 그러나, 새로운 Class가 만들어지게 되고, Serialization이나 garbage collection에서 예기지 못한 문제가 발생할 수 있게 되죠.​

## Reference

- [Stackoverflow - What is double brace initialization in java](https://stackoverflow.com/questions/1958636/what-is-double-brace-initialization-in-java)
