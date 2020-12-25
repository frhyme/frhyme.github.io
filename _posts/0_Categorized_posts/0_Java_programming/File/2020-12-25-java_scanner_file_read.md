---
title: Java - Read File by Scanner
category: java 
tags: java programming File Scanner
---

## Java - Read File by Scanner

- 흔히 시스템 입출력(`System.in`)에서 사용하는 `Scanner`에 `File`을 넘겨서 사용할 수도 있습니다.
- `test.txt`에는 다음과 같이 데이터가 담겨 있다고 하고요.

```plaintext
Word
This Is Text File
```

- 아래 코드에서처럼 `File`을 `Scanner`에 넘겨주면. 

```java
import java.io.File;
import java.util.*;

class Main {
    public static void main(String[] args) throws Exception {
        File fileToRead = new File("test.txt");
        Scanner scanner = new Scanner(fileToRead);

        while ( scanner.hasNext() ) {
            System.out.println(scanner.nextLine());
        }
    }
}
```

- 결과가 잘 나옵니다.

```plaintext
Word
This Is Text File
```
