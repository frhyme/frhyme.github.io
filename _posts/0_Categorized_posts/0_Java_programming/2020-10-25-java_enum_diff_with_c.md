---
title: Java - Enum(열거형)
category: java
tags: java programming enum enumeration C 
---

## Java - enum

- Java의 enum(열거형)은 '기정의된 Instance'라고 생각하면 됩니다. 오히려, 예를 들면 이해가 쉬운데요. 간단히 아래처럼 java의 enum을 정의할 수 있죠.

```java 
public enum Season {
    SPRING, SUMMER, AUTUMN, WINTER
}
```

### Complext Example like Class

- 이전에는 예시를 보여주기 위해서 매우 간단한 Enum class를 보여줬지만, 마치 Class처럼 복잡한 형태로 Enum 자료형을 정의하는 것도 가능합니다.
- 2개 이상의 field를 정의하고, 두 field에 대해서 값을 설정해주는 constructor를 만들어 줍니다. 그리고, 필요에 따라서, 해당 enum형태에서 사용할 수 있는 method들을 정의해서 사용할 수도 있죠. 

```java 
public enum DAY {
    MONDAY("Moon", 0),
    TUESDAY("Mars", 1),
    WEDNESDAY("Mercury", 2),
    THURSDAY("Jupyter", 3),
    FRIDAY("Venus", 4),
    SATURDAY("Saturn", 5),
    SUNDAY("Sun", 6);

    // enum field
    String engPlanet;
    int ordinalNum;

    // enum Constructor
    // public is not allowed in enum constructor
    DAY (String engPlanet, int ordinalNum) {
        this.engPlanet = engPlanet;
        this.ordinalNum = ordinalNum;
    }

    // class method
    public static DAY fromOrdinalNum(int ordinalNum) {
        // ordinalNum에 적합한 DAY
        for (DAY eachDay : DAY.values()) {
            if (eachDay.ordinalNum == ordinalNum) {
                return eachDay;
            }
        }
        // ordinalNum이 없으면 null
        return null;
    }

    // instance Method
    public void printDay() {
        System.out.printf("Planet: %s, ordinalNum: %d\n", engPlanet, ordinalNum);
    }
    public int getOrdinalNum() {
        return this.ordinalNum;
    }
    public String getEngPlanet() {
        return this.engPlanet;
    }
}
```

### Enum with Swtich 

- 정의한 enum의 값에 따라서 동작을 다르게 하기위해, `switch` statement를 사용해서 다음과 같은 코드를 작성할 수 있습니다.

```java
// Scanner를 통해 User로부터 다음 String을 입력받았다고 합시다.
String inputStr = "spring";

// Declare and Define enum Season.
// .valueOf 로 String을 사용해서 값을 정의해줄 수 있습니다.
Season currSeason = Season.valueOf("SPRING");

// swtich 를 통해서 다음처럼 사용할 수 있습니다.
switch (currSeason) {
    case SPRING:
        System.out.printf("This is SPRING\n");
        break;
    case SUMMER:
        System.out.printf("This is SUMMER\n");
        break;
    case AUTUMN:
        System.out.printf("This is AUTUMN\n");
        break;
    case WINTER:
        System.out.printf("This is WINTER\n");
        break;
    default:
        System.out.printf("What the SEASON?\n");
        break;
}
```

- 물론, `if` statement를 사용해서도 만들 수 있지만, case가 많을수록 switch 문이 if 문에 비해서 훨씬 빠릅니다.

### 왜 public constructor가 안되는가?

- 아래와 같이, enum의 내부 constructor에 대해서 `public` modifier를 사용하면 에러 `Modifier 'public' not allowed here`가 발생합니다.
- `enum`은 instance가 고정되어 있습니다. 요일이라면 7개, 월이라면 12개가 되겠죠. 이 아이들은 처음에 정의되고, 이후에는 새로운 instance가 생겨나서는 안됩니다. 
- 그런데, 만약, public, protected를 constructor에 사용해버리면, 새로운 instance가 생겨날 수 있고, 예기치 못한 오류가 발생할 수 있게 되는 것이죠. 따라서, `enum`의 constructor에는 public 을 쓸 수 없습니다.

```java
// public을 쓰면 `Modifier 'public' not allowed here`가 발생!!
public DAY (String engPlanet, int ordinalNum) {
    this.engPlanet = engPlanet;
    this.ordinalNum = ordinalNum;
}
```

- 자세한 내용은 [이 링크](https://stackoverflow.com/questions/3664077/why-cant-enum-constructors-be-protected-or-public-in-java)에서 읽을 수 있습니다.

---

## C - enum

- C에서도 `enum`을 정의할 수 있습니다. 
- 아래 코드에서 `DIRECTION`과 `DAY`라는 서로 다른 자료형을 정의하였지만, `EAST`와 `MON`의 값은 모두 첫번째 값이며 0이라는 값을 가지게 됩니다.

```c
enum DIRECTION {EAST, WEST, SOUTH, NORTH}; 
enum DAY {MON, TUE, WED, THU, FRI, SAT, SUN};
```

- 따라서, 다음처럼, 서로 다른 자료형 간에 비교했을 때, 1, 즉 `True`가 나온다는 단점이 있죠.

```c
printf("%d\n", EAST == 0); // 1
printf("%d\n", MON == 0); // 1
printf("%d\n", MON == EAST); //1 
```

### Full Code

```c
#include <stdio.h>

int main(void){
    // 열거형 타입을 정의: 순서대로 0, 1, 2, 3의 값이 지정됨
    enum DIRECTION {EAST, WEST, SOUTH, NORTH}; 
    enum DAY {MON, TUE, WED, THU, FRI, SAT, SUN};

    enum DIRECTION CurrDir = EAST;
    enum DAY CurrDay = MON;

    // C에서는 enum 으로 자료형을 정의해도, 각 값에 Integer 값이 mapping됨.
    // CurrDir과 CurrDay는 서로 다른 enum 자료형에 존재하지만, 모두 0, 1의 값을 가지고 있음
    // 따라서, 의미적으로는 아래 코드에 문제가 있지만, logical value가 true로 나오게됨.
    if (CurrDir == CurrDay){
        printf("This is CurrDir==CurrDay\n");
    }

    printf("EAST: %d\n", EAST); // 0 
    printf("MON : %d\n", MON); // 0 
    printf("%d\n", EAST == 0); // 1
    printf("%d\n", MON == 0); // 1
    printf("%d\n", MON == EAST); //1 

    // 심지어 그냥 값에 +1을 하는 것만으로 값이 바뀌기도 합니다.
    printf("%d\n", (MON + 1) == TUE); // 1, True
    
    return 0;
}
```

## Wrap-up

- 어찌 보면 별것 아니지만, 저는 이 사소한 잘못은 이후 에러를 만들 수 있는 여지를 발생시킨다고 생각해요. 
- Java는 서로 다른 enum 자료 형간에 값을 비교하게 되면 절대로 True가 나오지 않습니다. 이 측면에서는 Java가 C에 비해 좀 더 안정적이라고 생각되네요.
- 또한, 이러한 형태로 데이터를 만드는 건 그냥 python에서 `dictionary`나, `json`을 사용해서 정의하는 것도 가능합니다만, java에서는 `enum`도 class여서 내부에 method를 정의할 수 있다는 것이 강점입니다.
- java는 객체지향 언어이기 때문에, 필요한 메소드를 하나의 객체 안에 정리해두죠. 이러한 추상화, 추상화를 잘 해두면 프로그래밍을 일종의 메타적으로 할 수 있어서, 훨씬 효과적으로 프로그래밍을 할 수 있으니까요.
- 신기하네요, 나이를 먹으니까 점차 객체지향프로그래밍의 강점이 조금씩 보이는 것 같아요.