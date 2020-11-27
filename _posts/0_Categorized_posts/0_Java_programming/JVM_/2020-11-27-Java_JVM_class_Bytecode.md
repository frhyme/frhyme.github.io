---
title: Java - JVM, Class, Bytecode
category: java
tags: java JVM class bytecode programming
---

## Java Virtual Machine(JVM)

- JVM은 컴파일된 자바 프로그램을 실행하는 가상환경을 말합니다. JVM은 컴퓨터의 OS위에서 돌아가고, Java Program은 JVM 위에서 돌아가죠.
- JVM은 여러 종류가 있고 대부분 JVM Specification에 따라서 개발되었습니다(물론, JVM을 공부하기 위해서 이런 Spec을 읽을 필요는 없죠). 그 중에서는 보통 HotSpot이라는 JVM 구현체를 주로 사용합니다. 얘는 오라클에서 관리하는 Oracle Java와 OpenJDK에서 사용하죠.

## Class and Bytecode

- Bytecode는 `.class` file을 말하며, java source code인 `.java`를 컴파일하면 생성됩니다. 보통 소스 코드를 그대로 실행한다고 생각하지만, 그렇지 않고요. `.java` 파일을 컴파일하여 `.class`로 변환하게 되면 JVM에서는 `.class` 파일을 실행합니다. 그러면 프로그램이 실행되는 것이죠.
- 간단하게 저에게 다음의 소스 코드가 담긴 `test.java` 파일이 있다고 하겠습니다.

```java
package com.company;

class Main {
    public static void main(String[] args) {
        System.out.println("Hello, World and Bytecode!");

        // End of the code
    }
}
```

- 얘는 `.java` 파일이죠. 그럼 이제 컴파일을 해줘야 합니다. 
- 컴파일하고 나면 `Main.class`라는 byteCode 파일이 생깁니다.

```plaintext
javac test.java
```

- 그럼 이제 다음 명령어를 통해서 실행합니다. 그럼, 우리가 원했던 프로그램이 실행되죠.

```plaintext
java Main.class
```

### Java ByteCode 분해하기

- 그냥 텍스트 편집기에서 `.class`를 읽으면 깨진 문자들이 나오는 것을 알 수 있습니다. 얘를 잘 읽어주려면 JDK에 들어 있는 `javap`를 사용해야죠.
  - `-c`는 읽어서 그대로 프린트해서 보겠다는 이야기입니다.

```plaintext
javap -c Main.class
```

- 읽어보면 다음과 같이 나옵니다. 뜯어봐도 되기는 한데, 일단 저는 필요하지는 않아서 더 뜯어보지는 않겠습니다.
- Java ByteCode에 대한 자세한 내용은 [여기에서](https://dzone.com/articles/introduction-to-java-bytecode) 자세하게 알 수 있습니다.
- 그냥 지금 stack memory에 뭐가 올라갔고, 뭐가 로드되었고, 어떤 메소드를 실행했는지 등에 대해서 가 나와 있는거죠.

```plaintext
Compiled from "test.java"
class com.company.Main {
  com.company.Main();
    Code:
       0: aload_0
       1: invokespecial #1                  // Method java/lang/Object."<init>":()V
       4: return

  public static void main(java.lang.String[]);
    Code:
       0: getstatic     #7                  // Field java/lang/System.out:Ljava/io/PrintStream;
       3: ldc           #13                 // String Hello, World and Bytecode!
       5: invokevirtual #15                 // Method java/io/PrintStream.println:(Ljava/lang/String;)V
       8: return
}
```

## Wrap-up

- 이전에는 Java Code, Java ByteCode가 조금씩 헷갈렸는데, 이제는 그정도 레벨에서의 구분은 헷갈리지 않을 것 같네요. 그리고, Java ByteCode를 어떻게 뜯어볼 수 있는지도 알게 되었죠.
- 만약 제가 Java Code를 짠 다음에 제 코드가 어떻게 돌아가는지에 대해서 정확하게 알고 싶다면, 혹은 제가 알수없는 다른 오류가 나온다면 ByteCode로 변환한 다음 해석해보면 더 잘 알 수 있지 않을까 싶네요.
