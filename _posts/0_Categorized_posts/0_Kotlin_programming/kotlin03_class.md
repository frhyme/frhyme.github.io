---
title: Kotlin - class
category: kotlin
tags: kotlin programming class
---

## Kotlin - class

- kotlin에서 class를 정의하는 방법을 정리하였습니다.
  - kotlin에서는 Constructor를 내부 method로 정의하는 것이 아니라, `class Student(...)` 부분에 값을 넣어서 넘겨줍니다.
  - 내부에 `init` block으로 만들어 줄 수도 있긴 하죠.
  - method는 그냥 내부에 `fun`을 정의해주면 됩니다.

```kotlin
class Student(name:String = "unknown", studentID:String="20210000", gpa:Double = 0.0) {
    // 1) field에 값이 지정되고
    var name = name;
    var studentID = studentID
    // 2) 그 다음 init 부분이 실행됩니다.
    init {

        println("== new Student instance - ID: ${studentID}")
    }
    // 3) 또 지정되고

    var gpa = gpa;
    // 4) init 이 여러 개 있을 수도 있습니다.
    init {
        println("== init again")
    }

    fun print() {
        println("== name:${this.name}, ID: ${this.studentID}, GPA: ${this.gpa}")
    }
}
```

- main 함수를 실행해 보면 다음과 같습니다.

```kotlin
fun main() {
    var student1:Student = Student(studentID="1");
    var student2:Student = Student(studentID="2");
    student1.print()
}
/*
== new Student instance - ID: 1
== init again
== new Student instance - ID: 2
== init again
== name:unknown, ID: 1, GPA: 0.0
*/
```

## inheritance 

- 