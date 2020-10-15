---
title: Java - 2진수, 8진수, 16진수 
category: Java
tags: java programming
---

## java에서 2진법, 8진법, 16진법 값 넣어주기

- 2진수는 값 앞에 `0b`를 넣어주고, 8진법은 `0`, 16진법은 `0x`를 넣어주면 됩니다.

```java
class Main {
    public static void main(String[] args) {
        // java에서는 0으로 시작하는 정수형을 집어넣을 경우 8진법으로 이해함
        int binNum = 0b10; // binary number
        int octalNum = 010; // octal number
        int hexaNum = 0x11; // hexadecimal number

        System.out.println("binNum: " + binNum);
        System.out.println("octalNum: " + octalNum);
        System.out.println("hexaNum: " + hexaNum);
        // End of the code
    }
}
```

- 똑같은 것을, python에서는 다음과 같이 합니다.

```python
binNum   = 0b10
octalNum = 0o10
hexaNum  = 0x11
```
