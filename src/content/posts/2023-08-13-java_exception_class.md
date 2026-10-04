---
title: "Java - Exception class"
date: 2023-08-13
category: "java"
tags: ["java", "programming", "exception"]
permalink: "/java/java_exception_class/"
---

## Java - Exception

- Java는 객체 지향 언어입니다. 즉 모든 것이 객체로 받아들여진다는 것이며, "예외(exception)" 또한 객체로 인식됩니다. 그리고 이 객체들은 hierarchy(계층 구조)가 있습니다.
- 모든 예외의 기본이 되는, 최상위 클래스는 `java.lang.Throwable`이며, 다음과 같은 기본적인 method를 제공합니다.
  - `.getMessage()`: exception object에 대한 세부적인 문자 메시지를 리턴합니다.
  - `.getCause()`: 예외의 원인(Throwable)을 리턴합니다. 
  - `printStackTrace()`: standard error stream에 쌓여 있는 stack trace를 출력해줍니다. 어떤 예외(또는 에러)가 발생하면, 그 예외를 유발한 다른 예외들을 거슬러 올라가며 원인까지 추적할 수 있습니다.

## java.lang.Throwable

- `Throwable` class는 크게 `java.lang.Error`와 `java.lang.Exception`이라는 두 subClass로 나뉩니다.

### java.lang.Error

- `java.lang.Error`에는 JVM 측면에서 볼 때 좀 더 낮은 레벨(low-level)의 치명적인 상황들, 가령 `OutOfMemoryError`, `StackOverflowError`와 같은 것들이 담겨 있습니다. 하드웨어 리소스 고갈이나 시스템 레벨의 실패에 가깝습니다.

### java.lang.Exception

- `java.lang.Exception`에는 `RuntimeException`, `IOException` 등이 담겨 있습니다. `RuntimeException` 하위에는 `ArithmeticException`, `NumberFormatException`, `NullPointerException` 등이 있는데, 보시는 것처럼 개발 로직이나 애플리케이션 흐름과 직접적으로 연관된 문제들입니다.
  - **Checked Exception**: 컴파일 단계에서 컴파일러가 확인하는 예외 (`Exception` 상속, 단 `RuntimeException` 제외). `try-catch`로 잡거나 `throws`로 명시해야 컴파일이 가능.
  - **Unchecked Exception**: 런타임 시에 발생하는 예외 (`RuntimeException` 상속). 명시적인 예외 처리를 강제하지 않음.

---

## Issues & Questions

- 기본적인 개념은 알겠습니다만, 그래서 Exception의 hierarchy를 달달 외우고 있어야 하는지, 어떤 Exception이 어떤 종류의 Exception을 상속받는지 항상 외워야 하는지 의구심이 듭니다.
- 추가로, Error와 Exception이 다른 것도 꼭 알아야 하는지 의문이 듭니다.

---

## Summary & Best Practice

- **Error vs Exception을 구분해야 하는 이유:**
  - `Error`는 메모리 부족(OOM), 스택 오버플로우 등 **애플리케이션 계층에서 복구할 수 없는 심각한 시스템 문제**이므로 일반적인 `try-catch`로 잡으려 하지 않습니다 (잡아도 복구 불가능).
  - `Exception`은 로직 상 또는 외부 환경에서 발생할 수 있는 **복구 가능한 문제**이므로 상황에 맞게 적절히 핸들링하거나 사용자에게 명확한 메시지를 전달해야 합니다.
- **계층 구조를 외워야 하는가?**
  - 모든 예외 클래스의 상속 트리를 외울 필요는 없으며, **Checked Exception(컴파일 시점 검사, 예: `IOException`, `SQLException`) vs Unchecked Exception(런타임 예외, 예: `NullPointerException`, `IllegalArgumentException`)**의 차이와 특성만 명확히 이해하면 충분합니다.
  - 최근 Java/Spring 기반 실무에서는 불필요한 `throws` 선언 남발을 줄이고 계층 간 결합도를 낮추기 위해, Checked Exception을 커스텀 `RuntimeException`(Unchecked)으로 감싸서 던지는 패턴이 사실상 표준으로 자리 잡고 있습니다.