---
title: Java - Serialization
category: Java
tags: java programming Serialization Serializable class 
---

## Java - Serialization

- Serialization은 Object를 json, xml과 같은 binary data format으로 변환하는 것을 말하고, 반대로 json, xml로부터 Object로 변경하는 것을 Deserialization이라고 합니다.

### Student.java

- `Student` class를 다음과 같이 정의해줍니다.
- 내부에 static method로 `serialize`, `deserialize`를 각각 만들었습니다.
- `ObjectOutputStream`, `ObjectInputStream`을 사용하여 Object를 쓰고 읽습니다. 저는 이렇게 만들어진 stream을 File로 쓰도록 만들었습니다.
- 변수에 `trasient`를 선언하는 경우, serialization시에 해당 값이 null로 표시됩니다. 보안상 민감한 field의 경우 `transient`를 사용하여 포함되지 않도록 할 수 있죠.

```java
import java.io.*;

public class Student implements Serializable {
    // serialVersionUID는 무엇인가.
    private static final long serialVersionUID = 1L;
    private String name;
    // transient: Serialization시에 제외하고 싶을 경우 사용합니다.
    private transient double gpa;
    // Constructor
    public Student(String name, double gpa) {
        this.name = name;
        this.gpa = gpa;
    }
    public void printStudent() {
        System.out.println(
            String.format("Student{name='%s', gpa='%s'}", this.name, this.gpa)
        );
    }
    // Serialization
    public static void serialize(Student student, String fileName) throws IOException {
        /*
        * studnet를 serialization하여
        * File fileName에 Write해줍니다.
        * */
        FileOutputStream fos = new FileOutputStream(fileName);
        ObjectOutputStream oos = new ObjectOutputStream(fos);
        oos.writeObject(student);
        oos.close();
    }
    // De-serialization
    public static Student deserialize(String fileName) throws IOException, ClassNotFoundException {
        /*
         * File fileName을 읽고,
         * Student로 deserialization합니다.
         * */
        FileInputStream fis = new FileInputStream(fileName);
        ObjectInputStream ois = new ObjectInputStream(fis);
        Object obj = ois.readObject();
        ois.close();
        return (Student) obj;
    }
}
```

### Main.java

- Main.java는 다음과 같습니다.

```java
package com.company;

public class Main {
    public static void main(String[] args) throws Exception {
        Student student = new Student("LSH", 4.3);

        student.printStudent();
        String fileName = "a.student";
        System.out.println("== Serialization");
        Student.serialize(student, fileName);

        System.out.println("== De-serialization");
        Student deserializedStudent = Student.deserialize(fileName);
        deserializedStudent.printStudent();
    }
}
```

- 실행결과는 다음과 같습니다.

```plaintext
Student{name='LSH', gpa='4.3'}
== Serialization
== De-serialization
Student{name='LSH', gpa='0.0'}
```

### serialVersionUID

- `Student` class를 보면 `serialVersionUID`이 작성되어 있는 것을 알 수 있습니다. 
- 얘는 일종의 serialization에 대한 버전을 작성하는 놈이죠. 가령 `serialVersionUID`이 1일 때 object를 serialization하고, 이후 class를 새롭게 정의하고 `serialVersionUID`를 2로 변경했다고 하겠습니다. 그럼 `serialVersionUID`이 1일때 저장해놓은 object를 deserialization할 수 없습니다. 사실 그렇죠. class의 정의 자체가 다른데(변수가 추가되어었다거나), 동일한 방식으로 serialization, deserialization해서는 안되겠죠.
- 그러나, 사실 class의 정의가 달라질 경우 타 시스템에 영향을 많이 줄 정도로 민감한 class가 아니라면, 굳이 `serialVersionUID` 값을 작성해둘 필요도 없습니다. 어차피 컴파일러가 알아서 처리해주거든요. 일단은, 그냥 class에 대한 버전을 의미한다, 정도로만 이해하고 있어도 아무 문제가 없습니다.

```java
public static final long serialVersionUID = 1L;
```

---

## wrap-up

- java가 아닌 환경에도 객체가 사용될 경우에는 XML, json과 같은 다른 serialization방식을 사용하는 것이 좋을 수 있습니다. 요새 json은 거의 de-facto같은 느낌이기도 하구요.

## Reference

- [우아한 형제들 - 기술 블로그 - 자바 직렬화, 그것이 알고싶다. 실무편](https://woowabros.github.io/experience/2017/10/17/java-serialize2.html)
- 