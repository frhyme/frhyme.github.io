---
title: Java - BigInteger - 큰 수 표현하기
category: java
tags: java integer programming
---

## Java - BigInteger

- Java에서 `int`는 primitive type이며, 메모리에 주소를 저장하는 것이 아니라, 메모리에 값을 저장합니다.
- `int`는 4byte, 즉 32bit에 값이 저장되고 음수 표현을 위한 제일 앞 자리를 제외하면 31bit를 사용해서 크기를 표현하므로 2^31크기의 값을 표현할 수 있죠.
- 다만, 필요에 따라서 이 값보다 큰 값을 사용해야 하는 경우가 있습니다. 
- 그럴때는 `java.math.BigInteger`를 사용하면 됩니다.

```java
import java.math.BigInteger;

class Main {
    public static void main(String[] args) {
        // java에서는 int를 4byte, 32bit에 관리하며
        // 음수 양수 표현을 제외하면 31bit 2^31, 2147483647 크기의 숫자를 표현할 수 있음.
        int int1 = Integer.MAX_VALUE;
        // java.math.BigInteger 를 사용해서 큰 수를 표현할 수 있음
        // 다만 값을 넘겨줄 때 String으로 넘겨주는 것에 유의.
        BigInteger bigInt1 = new BigInteger("1000000000000000");
        // 값을 숫자로 넘겨주려면 valueOf 메소드 사용, 다만 이 때는 앞에 new가 붙지 않음.
        // 그리고 int 로 표현할 수 있는 최대 크기 2^31 보다 커지면 안됨.
        BigInteger bigInt2 = BigInteger.valueOf(1000000);

        // Arithmetic
        // +, -, *, / 등의 기본 연산을 사용할 수 없습니다.
        // 사칙연산의 경우 내부 method를 사용해서 처리해야 합니다.
        bigInt1.add(bigInt2); // 1000000001000000
        bigInt1.subtract(bigInt2); // 999999999000000
        bigInt1.multiply(bigInt2); // 1000000000000000000000
        bigInt1.divide(bigInt2); // 1000000000
        bigInt1.negate(); // -1000000000000000

        // Comparison
        // 같은지 비교.
        System.out.println(bigInt1.equals(bigInt1)); // true
        // 비교 왼쪽이 크면 1, 같으면 0, 오른쪽이 크면 -1
        BigInteger.valueOf(100).compareTo(BigInteger.valueOf(100)); // 0 
        BigInteger.valueOf(1000).compareTo(BigInteger.valueOf(100)); //1
        BigInteger.valueOf(100).compareTo(BigInteger.valueOf(1000)); // -1
    }
}
```

## python - BigInteger

- 파이썬에서는 기본 자료형 자체가 java의 BigInteger같은 아이입니다.
- 그래서 자리수를 고려하지 않고 값을 막 집어넣어도 알아서 다 인식합니다.
- 단, 당연하지만 memory에 값이 저장되는 primitive type에 비해서, 여러 메모리에 값이 나누어 저장되어 있는 이런 객체 형태는 값을 읽고 쓰는데 상대적으로 속도는 느립니다.
