---
title: Java - Infinity
category: java
tags: java programming infinity
---

## Java - Infinity 

- Java의 실수형 자료형(`double`, `float`)에는 Infinity가 존재합니다. 막연히, "큰 수"가 아니라, double 내의 어떤 수와 비교해도 절대적으로 큰 수인 `Double.POSITIVE_INFINITY`가 존재합니다. 그리고 음의 무한인, `Double.NEGATIVE_INFINITY` 또한 존재하죠.
- 정확한 이유는 모르겠지만, Int에는 Infinity가 존재하지 않고, float, double과 같은 실수형의 자료형에 속하는 값에만 Infinity가 존재합니다.
- 대략적인 사용법 및 Infinti의 특성은 다음과 같습니다.

```java
// 양의 무한대
double posDoubleInf = Double.POSITIVE_INFINITY;
// 음의 무한대
double negDoubleInf = Double.NEGATIVE_INFINITY;
double posDoubleMax = Double.MAX_VALUE; // 1.7E+308
double negDoubleMin = Double.MIN_VALUE; // 4.9E-324
        
// 0.0으로 나누었을 때 Zero division error가 발생하는 것이 아니라, 무한대로 인식함.
Double.POSITIVE_INFINITY == (2.0/0.0) // true

// 당연히 1.0/0.0 과 2.0/0.0은 같음
(1.0/0.0) == (2.0/0.0); // true

// Infinity에는 값을 더해도 그대로 Infinity임.
Double.POSITIVE_INFINITY == (Double.POSITIVE_INFINITY+1000); // true

// 다만 Infinity - Infinity 는 Double.NaN
Double.POSITIVE_INFINITY - Double.POSITIVE_INFINITY; // Double.NaN

// 0.0/0.0 또한 Double.NaN
0.0/0.0; // Double.NaN

Double.MAX_VALUE < Double.POSITIVE_INFINITY; // true
Double.POSITIVE_INFINITY == Float.POSITIVE_INFINITY // true
```

## python - Infinity

- python의 경우에도 `math.inf`를 사용하면 무한대의 개념을 상요할 수 있습니다.
- 하지만, java에서처럼 0을 분모로 가진다고 할때 알아서 Infinity로 인식하는 것이 아니라, `ZeroDivisionError`만이 발생하죠.

```python
import math

print(math.inf)
print(9999999999 < math.inf) # True
print(10 / 0) # ZeroDivisionError: division by zero
```
