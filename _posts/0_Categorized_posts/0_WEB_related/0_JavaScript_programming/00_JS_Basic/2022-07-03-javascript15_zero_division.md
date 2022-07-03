---
title: Javascript - Zero Division
category: javascript
tags: javascript programming ZeroDivisionError ZeroDivision
---

## Javascript - Zero Division

### python Zero Division Error

- 제가 알고 있는 프로그래밍 언어들에서는 보통 다음과 같이 0으로 나누는 경우 Zero division Error가 발생합니다. 아래는 python code이구요.

```python
a = 10
b = 0
"""
Traceback (most recent call last):
  File "a.py", line 4, in <module>
    print(a / b)
ZeroDivisionError: division by zero

"""
print(a / b)
```

- 물론, 수학적으로는 0을 나누면 infinity가 되니까, infinity로 처리해주는 게 맞을 수도 있습니다만, 그렇다면 (2 / 0) / (1 / 0) 의 연산의 결과는 뭐가 되어야 할까요? `(2 * Infinity) / (1 * Infinity)` 이므로 2가 되는게 맞을까요? 그렇다면 매번 저런 간단한 수식을 처리할 때마다 극한을 고려해서 값을 처리해주는 게 맞을까요? 뭐, 이건 선택의 문제라고 봅니다만, 저는 그렇게 하면 안된다고 봅니다. 비효율적이에요.

### Javascript goes to Infinity

- 하지만, 흥미롭게도 Javascript에서는 ZeroDivisionError 가 발생하지 않습니다.
- 0 으로 나누게 되면 Infinity 로 처리됩니다. 값을 정확히 계산하기가 어려울 경우에는 NaN으로 처리 되죠.

```javascript
console.log(1 / 0)
// Infinity
console.log((2 / 0) / (1 / 0))
// NaN
console.log((2 / 0) * (1 / 0))
// Infinity
console.log((2 / 0) * 0)
// NaN
console.log(0 / 0)
// NaN
```

- 왜 javascript는 Zero Division Error를 생성하지 않는지에 대한 분명한 문서는 아직 찾지 못했습니다만, [how does javascript handle divide by zero](https://www.educative.io/answers/how-does-javascript-handle-divide-by-zero)에서는 다음과 같은 두 가지 이유를 지적합니다.

1. Javascript는 동적 타입(dynamically typed) 언어이기 때문에 type conversion 을 사용하면 되니까. 하지만, python도 동적 타입언어죠. 0으로 나눌 수 있다는 것과 동적 타입언어 간에 무슨 관계가 있는지는 조금 모호합니다. 정적 타입언에서는 0으로 나누어졌을 때, 이를 None 혹은 Infinity와 같은 다른 타입으로 변경하는 것이 불가능한 반면 동적 타입언어에서는 이러한 방식이 가능하므로, 이를 허용한다, 정도로 해석해봅니다.
1. javascript 에서 runtime에서 Exception을 발생시키는 것은 비효율적이다. 이것도 좀 모호한데요, javascript의 경우 웹에서 주로 쓰이는 언어이고 엄밀성 보다는 효율성에 중심을 두고 성장해온 언어라고 생각합니다(제 생각입니다). 따라서 너무 빡빡하게 예외처리를 강요하는 방향보다는 일단 돌아갈 수 있도록 하는데 집중한 언어가 아닐까 싶어요. 만약 ZeroDivision 에 대해서 예외가 발생했다면 예외처리가 되어 있지 않다면 브라우저에서 코드가 동작하지 않는다거나 하는 이슈가 발생할 수 있으니까요. 네, 물론 제 생각입니다.

- 해결법...은 없고, javascript는 이렇게 동작한다는 사실을 그냥 알고 개발을 해야 할 것 같아요. 0으로 나누는 경우 다음과 같이 구분될 수 있으니, 항상 염두에 두고 개발을 해야 할 것 같습니다. 하하.

```javascript
var a = 1 / 1
console.log(a);

if (isFinite(a) == true) {
  console.log('a is finite');
} else {
  if (isNaN(a) === true) {
    console.log('a is NaN');
  } else if (a === Infinity) {
    console.log('a is Infinity');
  } else {
    console.log('a is what???');
  }
}
```

## Wrap-up

- 늘 느끼는 사실이지만, 역시 새로운 프로그래밍 언어를 공부하는 것은 참 즐거워요.

## Reference

- [how does javascript handle divide by zero](https://www.educative.io/answers/how-does-javascript-handle-divide-by-zero)
- [rosettacode - wiki detect division by zero - javascript](https://rosettacode.org/wiki/Detect_division_by_zero#JavaScript)
