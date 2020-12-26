---
title: DuckTyping - Example with python
category: python
tags: python OOP DuckTyping programming python java Interface
---

## Duck Typing

- "어떤 것이 오리(Duck)인지는 그의 행동을 통해 판단해야 한다"라는 개념이 바로 Duck Typing입니다.
- 달리 말하면, "처음부터 Type이 정해진 것이 아니라, "오리로서 갖춰야 하는 method들이 구현되어 있으면 걔도 오리야"라고 본다는 이야기죠.
- 즉, 처음부터 타입을 정해놓지 않고, Runtime 시에 해당 개체에 대한 typ이 정해지고 이를 활용해서 유연한 프로그래밍을 할 수 있도록 한다는 이야기입니다.
- 하지만, "유연함"과 "자유로움"은 늘 "예기치 못했던 Runtime Error"와 같은 말이어서, 실수가 발생하기 쉽죠.
- Java의 경우 DuckTyping을 지원하지 않고, python의 경우 DuckTyping을 지원합니다.

## Python - supporting Duck Typing

- 함수에서 argument type를 구분하지 않습니다.
- 따라서, 내부에 `.quack()`만 있다면 문제없이 실행되죠.

```python
class Duck:
    def __init__(self, name:str) -> object:
        self.name = name

    def quack(self):
        print(f"Duck  named {self.name} :: QUACK")


class Human:
    def __init__(self, name: str, age: int) -> object:
        self.name = name
        self.age = age

    def quack(self):
        print(f"Human named {self.name} :: QUACK")

    def self_introduce(self):
        print(f"Hi, My name is {self.name} and {self.age} years old")


def quack(each_duck: Duck):
    # duck을 전달받아서 .quack method를 실행합니다.
    # Duck Object가 넘어오든, Human Object가 넘어오든 상관없이
    # .quack() method만 있으면 실행되죠.
    each_duck.quack()


if __name__ == '__main__':
    # Duck Object와 Human Object를 하나씩 만들어줍니다.
    duck = Duck("AAA")
    human = Human("BBB", 10)

    # 분명히 두 Object의 type은 다릅니다만.
    print(type(duck))  # <class '__main__.Duck'>
    print(type(human))  # <class '__main__.Human'>

    # 내부에 둘다 .quack method가 있으므로 오류가 발생하지 않습니다.
    quack(duck)  # Duck  named AAA :: QUACK
    quack(human)  # Human named BBB :: QUACK
```

## Java - not supporting Duck Typing

- class는 다음과 같이 정의합니다.

```java
public class Duck {
    String name;
    public Duck(String name) {
        this.name = name;
    }
    public void quack() {
        System.out.printf("Duck named %s :: QUACK", this.name);
    }
}

public class Human {
    String name;
    public Human(String name) {
        this.name = name;
    }
    public void quack() {
        System.out.printf("Human named %s :: QUACK", this.name);
    }
}
```

- 실행해 보면, 오류와 함께 실행되지 않습니다. 사실 Java에서는 당연한 거죠.

```java
class Main {
    public static void quack(Duck inputDuck) {
        inputDuck.quack();
    }
    public static void main(String[] args) throws Exception {
        Duck duck = new Duck("AAA");
        Human human = new Human("BBB");

        quack(duck); // Duck named AAA :: QUACK
        // 다음 오류와 함께 실행되지 않죠.
        // java: incompatible types: com.company.Human cannot be converted to com.company.Duck
        quack(human);
    }
}
```

## Java - using Interface

- 다만, java에서는 `interface`를 이용해서 비슷한 짓을 할 수 있습니다.
- `quackable`이라는 `.quack` 메소드를 가진 interface를 만들어서, `Human`, `Duck`에서 구현해줍니다.
- 그럼, 잘 실행되죠 호호. 이게 Java의 Interface를 사용할 때의 강점입니다.

```java
public interface quackable {
    public void quack();
}

public class Duck implements quackable {
    String name;
    public Duck(String name) {
        this.name = name;
    }
    public void quack() {
        System.out.printf("Duck named %s :: QUACK", this.name);
    }
}

public class Human implements quackable {
    String name;
    public Human(String name) {
        this.name = name;
    }
    public void quack() {
        System.out.printf("Human named %s :: QUACK", this.name);
    }
}
```

- 잘 되죠. 

```java

class Main {
    public static void quack(quackable quackableObj) {
        quackableObj.quack();
    }
    public static void main(String[] args) throws Exception {
        Duck duck = new Duck("AAA");
        Human human = new Human("BBB");

        quack(duck); // Duck named AAA :: QUACK
        quack(human); // Human named BBB :: QUACK
    }
}
```

## Wrap-up

- DuckTyping은 "해당 개체의 type은 같은 메소드(그리고 변수)를 가지고 있는지에 따라서 판단한다"라는 개념입니다.
- python의 경우 DuckTyping을 지원하고, Java에서는 DuckTyping을 지원하지 않습니다.
- 그러나, Java에서는 Interface를 이용해서 비슷한 짓을 할 수 있습니다. 제가 보기에는 Java의 경우다 더 명확하고 좋은 것 같아요.
