---
title: Java - 길이를 모르는, 여러 값을 입력받기
category: Java
tags: java programming Scanner input
---

## Java - 값이 몇 개 들어올지 모를 때

- java에서 Scanner를 사용해서 값을 읽을 때, 값이 몇 개 들어올지모를 때가 있습니다.
- 가령 다음처럼 어떤 경우에는 3개를 받고, 어떤 경우에는 4개를 받고 그럴 수 있는 것이죠.

```plaintext
1 2 3 
4 5 6 7 8 9
```

- 이처럼 `Scanner.next()`를 통해서 값을 입력받을 때, 몇 개를 입력받을지 모른다면 `scanner.hasNext()`를 사용해서 현재 더 읽어들일 값이 있는지 확인할 수 있습니다.

```java
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        // String literal
        Scanner scanner = new Scanner(System.in);

        // scanner.hasNext()를 사용하면, 현재 읽어들일 놈이 있는지 확인해줍니다.
        while (scanner.hasNext()) {
            String temp = scanner.next();
            System.out.println(temp);
        }
    }
}
```
