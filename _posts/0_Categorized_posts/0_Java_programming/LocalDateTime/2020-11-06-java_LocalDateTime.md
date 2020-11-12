---
title: Java - time package
category: java
tags: java programming time
---

## Java - time package 

- 

### time.LocalDate

- java에서 Data를 관리하기 위해서는 `time.LocalDate` 클래스를 사용합니다.
  - `LocalDate.of(year, month, day)`나, `LocalDate.parse("yyyy-mm-dd")`를 사용하여 LocalDate의 값을 초기화합니다.
  - `.equals(date2)`를 사용하여, 서로 다른 두 LocalDate가 동일한지 확인할 수 있습니다.
  - 날짜를 증가시키기 위해서는 `.plusDays(1)`등의 메소드를 사용하여 날짜를 증가시킵니다.

```java
import java.time.LocalDate;

class Main {
    public static void main(String[] args) {
        /*
        .of(year, month, day) method를 사용하여 2020년 11월 1일을 설정하는 방식과
        .parse("yyyy-mm-dd")에 String을 넘겨서 2020년 11월 01일을 설정하는 방식이 있습니다.
        "2020-11-1"과 같이 넘겨주면 java.time.format.DateTimeParseException 에러가 발생합니다.
        */
        LocalDate date1 = LocalDate.of(2020, 11, 1);
        LocalDate date2 = LocalDate.parse("2020-11-01");

        // 두 LocalDate를 비교할 때는 == 를 사용하면 안되고, .equals 를 사용해야 합니다.
        System.out.println(date1 == date2); // false
        System.out.println(date1.equals(date2)); // true

        /*
        현재 LocalDate에서 날짜를 증가 혹음 감소 시키기 위해서는 +, - 를 사용하는 것이 아니라, 
        .plusDays(), .minusDays(), plusYears() 등의 메소드를 사용해야 합니다.
        */
        LocalDate today = LocalDate.now();
        LocalDate tomorrow = today.plusDays(1);
        LocalDate yesterday = today.minusDays(1);
        LocalDate todayAfterTwoYears = today.plusYears(2);
    }
}
```

### time.LocalTime

- `time.LocalTime`은 날짜는 없이, '시각'만 관리하는 Class입니다.

```java
import java.time.LocalTime;

class Main {
    public static void main(String[] args) {
        /*
        * LocalTime은 @hour, @minute, @second, @nanoOfSecond 로 정의할 수 있습니다.
        * milliSecond = 1.0e-3
        * microSecond = 1.0e-6
        * nanoSecond  = 1.0e-9
        */
        LocalTime t1 = LocalTime.of(23, 59, 59, 111);
        // "23:59"로 넣어도 문제없습니다. 단 "23"은 안됩니디.
        LocalTime t2 = LocalTime.parse("23:59:59.000000111");

        // 현재 Time에서 Hour, Minute, Second, Nano 각각의 값을 뽑아내려면 다음 메소드를 사용합니다.
        t1.getHour();
        t1.getMinute();
        t1.getSecond();
        t1.getNano();

        // 현재 시간을 통째로 초로 변환할 경우
        t1.toSecondOfDay();

        // LocalTime을 비교하려면 다음의 방식을 통해 비교하면 됩니다.
        System.out.println(t1.equals(t2));
    }
}
```

### time.LocalDateTime

- 당연히, 날짜(`LocalDate`)와 시간(`LocalTime`)을 함께 정의하여 사용할 수도 있겠죠.
- 나머지 method는 모두 이전과 비슷하여 따로 작성하지 않았습니다.

```java
import java.time.LocalDate;
import java.time.LocalDateTime;
import java.time.LocalTime;

class Main {
    public static void main(String[] args) {
        // .of method에서는 ~minute까지는 모두 채워 넣어야 오류가 없다.
        LocalDateTime dt1 = LocalDateTime.of(2020, 11, 1, 12, 34, 56, 78);

        // LocalDate 객체와 LocalTime 객체를 혼합하여 만들 수도 있습니다.
        LocalDate d1 = LocalDate.of(2020, 11, 1);
        LocalTime t1 = LocalTime.of(12, 34, 56, 78);
        LocalDateTime dt2 = LocalDateTime.of(d1, t1);

        System.out.println(dt1); // 2020-11-01T12:34:56.000000078
        System.out.println(dt2); // 2020-11-01T12:34:56.000000078
    }
}
```

### 날짜, 시간 비교하기

- `LocalDate`, `LocalTime`, `LocalDateTime`에 대해서, 비교연산을 수행할 수도 있습니다.
  - `dt1.isEqual(dt2)`: 같으면 true 아니면 false를 리턴
  - `dt1.isBefore(dt2)`: dt1이 더 일찍이면 true를 리턴
  - `dt1.isAfter(dt2)`: dt2이 이후이면 true를 리턴.

```java
import java.time.LocalDate;
import java.time.LocalDateTime;
import java.time.LocalTime;

class Main {
    public static void main(String[] args) {
        // .of method에서는 ~minute까지는 모두 채워 넣어야 오류가 없다.
        LocalDate date1 = LocalDate.of(2020, 11, 05);
        LocalDate date2 = LocalDate.of(2020, 11, 05);
        LocalDate date3 = LocalDate.of(2020, 11, 06);

        // == 연산자로 날짜가 같은지 비교할 수 없다.
        System.out.println(date1 == date2); // false
        // .isEqual method를 사용해서 비교해야 한다.
        System.out.println(date1.isEqual(date2)); // true
        System.out.println(date1.isEqual(date3)); // false
        System.out.println(date1.isBefore(date3)); // true
        System.out.println(date1.isAfter(date3)); // false
    }
}
```
