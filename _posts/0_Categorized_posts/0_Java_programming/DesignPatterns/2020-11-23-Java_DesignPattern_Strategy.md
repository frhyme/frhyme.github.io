---
title: Java - Design Pattern - Strategy
category: DesignPattern
tags: DesignPattern Strategy java programming class 
---

## Java - Design Pattern - Strategy

- Strategy Pattern은 객체지향적 설계에서 가장 많이 사용되는 패턴이죠.
- 하나의 예를 들어 보겠습니다. 클래스 `Clustering`이 있을 때, 점간의 거리를 측정하는 `GetDistance` 클래스가 내부에 있겠죠. 거리 측정은 조금씩 다를 수 있는데, 필요에 따라 내부의 `GetDistance`를 다른 클래스들로 정의할 수 가 있겠죠. 이렇게 클래스 내부에 다른 class instance가 있는 경우, 그리고 내부 class instance를 필요에 따라 여러 class의 instance로 변경해주는 경우를 strategy라고 하죠. 여기서 strategy는 보통 behaviour를 정의하죠.

### Strategy Pattern의 장점

- compileTime이 아니라, runTime에 클래스의 behaviour를 바인딩합니다.
- 클래스의 행동을 분리(isolation)함으로써, 조합에 따라 새로운 클래스를 정의할 수 있도록 해줍니다.

### Strategy Pattern 예제

- 보통 다음 그림처럼 정의되죠.
  - java interface를 통해서 공통의 behavriour를 선언해주고.
  - behaviour에 class instance를 바인딩해줍니다. 이 때 이 behaviour도 interface로 정의한 다음 여러 behaviour를 상속받는 형태로 정의합니다.

![strategyPattern_example](https://i2.wp.com/www.e4developer.com/wp-content/uploads/2018/10/strategy-pattern.png?resize=669%2C344&ssl=1)

### Java - Strategy Implementation 

- Strategy pattern을 간단하게 java로 구현해보면 다음과 같습니다.

```java
// Algorithm Class의 부품으로 사용될 수 있는 Distance의 상위 interface를 정의합니다.
interface Distance {
    public double calcDistance(int x1, int y1, int x2, int y2);
}

// Distance를 implement해주는 두 Class를 정의해줍니다.
class EuclideanDistance implements Distance {
    @Override
    public double calcDistance(int x1, int y1, int x2, int y2) {
        return 0.0;
    };
}
class ManhattanDistance implements Distance {
    @Override
    public double calcDistance(int x1, int y1, int x2, int y2) {
        return 0.0;
    };
}

// 여러 class들에서 사용되는 field를 모아서 abstract class를 정의해줍니다.
abstract class abstractAlgorithm {
    int field1;
    Distance distance;
}

// abstractAlgorithm를 상속받아 Constructor에서 Distance 를 주입해줍니다.
public class Algorithm extends abstractAlgorithm {
    public Algorithm (Distance distance) {
        this.distance = distance;
    }
}
```
