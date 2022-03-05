---
title: Javascript - Template literal
category: javascript
tags: js javascript
---

## Javascript - Template literal

- Javascript에서 String을 parameterized String형식으로 출력하는 방식은 다음과 같으며, 이를 Template Literal이라 한다.

```javascript
var name = 'frhyme';
// string 앞 뒤에 single quote 대신 backtick 사용
var letter = `Hi, I'm ${name}. My name is ${name}`;
// parameter안에 연산을 넣으면 연산 결과가 나옴.
var str_with_number_op = `1+1 = ${1 + 1}`;

console.log(name);
console.log(letter);
console.log(str_with_number_op);
```
