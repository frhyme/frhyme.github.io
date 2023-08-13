---
title: Java - Exception class
category: java
tags: java programming exception 
---

## Java - Exception

- Java는 객체 지향 언어입니다. 즉 모든 것이 객체로 받아들여진다는 것이며, "에외(exception)" 또한, 객체로 인식됩니다. 그리고 이 객체들은 hierarchy가 있죠.
- 모든 예외의 기본이 되는, 최상위 클래스는 `java.lang.Throwable`이며, 이 아이는 다음과 같은 기본적인 method를 가지고 있습니다.
  - `.getMessage()`: exception object에 대한 세부적인 문자 메세지를 리턴합니다.
  - `.getCause()`: 예외의 원인을 리턴합니다. 
  - `printStackTrace()`: standrad error stream에 쌓여 있는 stack trace를 출력해줍니다. 즉, 어떤 예외(혹은 에러)가 발생하면, 그 예외를 발생시킨 다른 예외, 다시 다른 예외 이렇게 이어서 그 원인까지 파고 들어간다는 이야기죠.

## java.lang.Throwable

- `Throwable` class는 다시, `java.lang.Error`이라는 subClass와 `java.lang.Exception`이라는 subClass로 확장되죠. 

### java.lang.Error

- `java.lang.Error`에는 JVM 측면에서 볼 때 좀 더 낮은 레벨(low-level)의 예외들, 가령 `OutOfMemoryError`, `StackOverflowError`와 같은 것들이 담겨져 있죠. 여기서, "낮은 레벨"이라는 말은 좀 더 하드웨어에 가까운 개념이라고 보시는 것이 좋을 것 같아요.

### java.lang.Exception

- `java.lang.Exception`에는, `RuntimeException`, `IOException`등이 담겨져 있습니다. `RuntimeException`에는 `ArithmeticException`, `NumberFormatException`, `NullPointerException`등이 담겨 있는데, 보시는 것처럼 좀 더 개발 logic에 관련된 문제로 보이죠.
  - Checked Exception: "Compile 단계에서 발생하는 Check" 
  - Unchecked Exception: "Runtime 시에 발생하는 Exception". 일단 그냥 `RuntimeException`라고 알고 있어도 문제가 없음.

---

## Issues

- 기본적인 개념은 알겠습니다만, 그래서 Exception의 hierarchy를 달달 외우고 있어야 하는지, 어떤 Exception이 어떤 종류의 Exception을 상속받는지 등에 대해서 항상 외우고 있어야 하는 건지 의구심이 듭니다.
- 추가로, Error와 Exception이 다른 것도 꼭 알아야 하는지 의문이 드네요. 흠흠흠. 