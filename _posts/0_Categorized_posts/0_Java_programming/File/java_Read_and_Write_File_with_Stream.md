---
title: Java - Read and Write File
category: java 
tags: java programming File Stream
---

## Java - Read and Write File

- java에서 File을 읽거나 혹은 쓰는 방법을 정리합니다.

## java.io.File

- java에서 `File`을 읽거나 쓰려면, `java.io.File` class를 사용하면 됩니다.
- File을 읽은 다음에 간단한 meta 정보를 알고 싶다면 다음의 method들을 사용해서 처리할 수 있습니다.

```java
import java.io.File;

class Main {
    public static void main(String[] args) {
        File file = new File("test.txt");
        // method for File object
        System.out.println(file.getAbsolutePath());
        System.out.printf("File name    : %s \n", file.getName());
        System.out.printf("File Abs path: %s \n", file.getAbsolutePath());
        System.out.printf("File Rel path: %s \n", file.getPath());
        System.out.printf("Is file      : %s \n", file.isFile());
        System.out.printf("Is directory : %s \n", file.isDirectory());
        System.out.printf("File Exists  : %s \n", file.exists());
    }
}
```

## Writing File in Java 

- 다음처럼 `File(filePath)`를 통해 File에 대한 객체를 만들어주고, `FileWriter(File(filePath))`를 사용해서 해당 File 내에 새로운 내용을 수정하거나, 추가할 수 있씁니다.

```java
import java.io.File;
import java.io.FileWriter;

class Main {
    public static void main(String[] args) {
        File file = new File("test.txt");
        
        // method for FileWriter object
        try {
            // @Param: File outputFile, Boolean append
            FileWriter fileWriter = new FileWriter(file);
            fileWriter.write("ABC");
            fileWriter.close();
        } catch (Exception e) {
            System.out.println("File to Write not found");
        }
    }
}
```

## Reading File in java

- 동일하게 `FileReader(File())`를 사용해서 파일을 읽을 수 있습니다.
- 읽는 값은 `char`에 대한 `int`형태이며, 문자값으로 출력하기 위해서는 `char`로 컨버전해줘야죠.
- 만약 `File()` Object에서 더 이상 읽을 값이 없다면 `FileReader()`는 -1을 리턴합니다.

```java
import java.io.File;
import java.io.FileReader;

class Main {
    public static void main(String[] args) {
        File file = new File("test.txt");
        
        try {
            FileReader fileReader = new FileReader(file);
            // 만약 더 이상 읽을 값이 없으면 fileReader는 -1을 읽어들입니다.
            // -1은 EOF(End Of File)를 의미합니다.
            // 다만 읽어지는 값은 int이고, 아스키코드에 따라서 char로 변환해서 출력해야죠.
            int t = fileReader.read();
            while ( t != -1) {
                char c = (char) t;
                System.out.printf("ReadChar: %c\n", c);
                t = fileReader.read();
            }
            fileReader.close();
        } catch (Exception e) {
            System.out.println(e);
        }
    }
}
```

## java.io.InputStream 

- `java.io.InputStream`은 말 그대로 '연속된 값의 흐름'을 의미합니다.
- 아래 코드에서처럼 `System.in`을 사용해서 그대로 값을 하나씩 읽어서 출력할 수도 있습니다. 아래 코드를 실행하면, `char`를 읽어서 그대로 해당 char의 `int`형태를 출력합니다.

```java
import java.io.InputStream;

class Main {
    public static void main(String[] args) throws Exception {
        InputStream inputStream = System.in;
        
        int x = inputStream.read();
        while (x != -1) {
            System.out.print(x);
            x = inputStream.read();
        }
    }
}
```
