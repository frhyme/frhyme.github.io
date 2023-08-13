---
title: Java - 가변 Argument 선언하고 사용하기
category: java
tags: java programming argument array
---

## Java - 가변 Argument 선언하고 사용하기

- 대부분의 함수는 정해진 수의 argument를 넘겨받습니다. 그리고 디자인 측면에서도, 이게 훨씬 좋은 설계방식이라고 생각하고요.
- 다만, 경우에 따라, argument의 수가 여러 개 들어오도록 설계할 때도 있죠.
- 가령 `sum(a, b)`, `sum(a, b, c)`처럼, 2개의 합, 3개의 합 이런 식으로 처리해주는 함수를 만들고 싶을 수 있으니까요.
- 다음처럼 argument 자리에 `.` 3개를 추가해서, `int...`로 처리하면 됩니다.

```java
class Main {
    public static int sum(int... numbers) {
        int s = 0;
        for (int i=0; i < numbers.length; i++) {
            s += numbers[i];
        }
        return s;
    }
    public static void main(String[] args) {
        System.out.println(sum(1, 2, 3)); // 6
        System.out.println(sum(1, 2, 3, 4, 5, 6)); // 21
        // End of the code
    }
}
```

## python에서 variable argument

- python에서는 다음처럼 하면 되죠. 
  - java에서는 `int...`와 같이 정의하고,
  - python에서는 앞에 `*`를 붙여서 정의해주면 됩니다.

```python
def sum_func(*argv):
    s = 0
    for x in argv:
        s += x
    return s

print(sum_func(1, 2))
print(sum_func(1, 2, 3))
print(sum_func(1, 2, 3, 4))
```
