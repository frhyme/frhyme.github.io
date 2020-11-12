---
title: java - 예외처리(try, catch, finally)
category: java
tags: java programming exception exceptionHandling
---

## java - Simple exception Handling

- java에서 예외처리 하는 방법을 간단하게 다음과 같이 정리하였습니다.
- 기정의된 예외(Exception)들은 프로그래밍 과정에서 발생하고 그 예외상황을 처리하는 방식이 보통 다음과 같죠
  - `try`: 예외가 포함될 수 있는 코드
  - `catch`: 특정 예외 `e`에 대한 동작방식을 정의함
  - `finally`: 어떤 예외가 발생했든 항상 실행되는 코드.

```java
import java.util.Scanner;
import java.util.InputMismatchException;

class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        try {
            int a = scanner.nextInt();
            int b = scanner.nextInt();
            System.out.println(a / b);
        } catch (ArithmeticException e) {
            // if b == 0, throws ArithmeticException
            System.out.printf("This is Arithmetic Exception:: %s \n", e);
        } catch (InputMismatchException e) {
            // Int가 들어와야 하는데 6.0 처럼 Double 혹은 string이 들어오면.
            System.out.printf("This is InputMismatchException:: %s \n", e);
        } catch (Exception e) {
            // ArithmeticException, InputMismatchException가 아닌 다른 Exception
            System.out.printf("This is Exception:: %s\n", e);
        } finally {
            System.out.println("================================");
            System.out.println("finally statement always executes");
        }
    }
}
```

## 함수 내에서 Exception이 발생

- 아래 처럼 함수 내에서 exception이 throw되더라도, 최종적으로 `catch`되는 곳 까지 넘어갑니다.

```java
import java.util.InputMismatchException;

class Main {
    public static void simpleFunc() {
        Scanner scanner = new Scanner(System.in);
        int a = scanner.nextInt();
        int b = scanner.nextInt();
        System.out.println(a / b);
    }
    public static void main(String[] args) {
        try {
            simpleFunc();
        } catch (ArithmeticException e) {
            // if b == 0, throws ArithmeticException
            System.out.printf("This is Arithmetic Exception:: %s \n", e);
        } catch (InputMismatchException e) {
            // Int가 들어와야 하는데 6.0 처럼 Double 혹은 string이 들어오면.
            System.out.printf("This is InputMismatchException:: %s \n", e);
        } catch (Exception e) {
            // ArithmeticException, InputMismatchException가 아닌 다른 Exception
            System.out.printf("This is Exception:: %s\n", e);
        } finally {
            System.out.println("================================");
            System.out.println("finally statement always executes");
        }
    }
}
```

## new Exception

- 함수 내에서 새로운 Exception을 정의하여 throws하고 싶다면 다음의 형태로 함수를 정의해줘야 합니다.
- 함수 선언 뒤에 `throws Exception`이 붙죠.

```java
public static void simpleFunc() throws Exception {
}
```

- 코드로 보면 다음과 같죠.

```java
class Main {
    public static void simpleFunc() throws Exception {
        Scanner scanner = new Scanner(System.in);
        int a = scanner.nextInt();
        int b = scanner.nextInt();
        if (b == 0) {
            throw new Exception("Exception: b == 0");
        }
        System.out.println(a / b);
    }
    public static void main(String[] args) {
        try {
            simpleFunc();
        } catch (Exception e) {
            // ArithmeticException, InputMismatchException가 아닌 다른 Exception
            System.out.printf("This is Exception:: %s\n", e);
        } finally {
            System.out.println("================================");
            System.out.println("finally statement always executes");
        }
    }
}
```
