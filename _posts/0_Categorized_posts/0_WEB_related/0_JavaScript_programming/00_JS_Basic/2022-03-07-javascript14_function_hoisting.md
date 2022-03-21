---
title: Javscript 13 - function hoisting
category: javascript
tags: javascript js function hoisting
---

## Javascript 13 - function hoisting

- Javascript에서 function을 정의하는 방법은 두 가지가 있습니다.
- 두 방법 모두 function을 정의하지만, 1번의 경우는 function hoisting이 발생하는 반면, 2번의 경우는 function hoisting이 발생하지 않습니다.

```javascript
// 1번 방법.
function funcA (value) {
  console.log(value);
}
// 2번 방법.
var funcA = function (value) {
  console.log(value);
}
```

## hoisting example

- Javascript는 함수를 실행하기 전에 함수 선언에 대한 메모리를 먼저 할당합니다. 따라서, 다음과 같이 함수 정의 부분보다 함수 실행 부분이 앞에 있을 경우에도 코드 자체는 문제없이 실행됩니다.
- 변수의 경우도 에러가 발생하지는 않고, `undefined`가 발생합니다. 즉 메모리는 할당되었지만, 값이 무엇인지는 알 수 없다는 것이죠. 아직 assignment되지 않았으니까요.
- 이러한 메커니즘을 'hoisting'이라고 합니다. 영단어의 의미는 '낚아올리다, 끌어올리다'를 의미하는데, 아래에 정의된 아이를 가져와서 위에서 쓰는 형태이므로 비슷한 의미를 가지죠.

```javascript
funcA('A');

function funcA(value) {
  console.log(value);
}
// A

console.log(varA);
// var 명령어가 없으면 ReferenceError가 발생합니다.
var varA = 10;
// undefined
```

## Avoid function hoisting

- 만약 function hoisting을 회피하고 싶다면, 아래와 같이 익명 함수를 만든 다음, 변수에 할당하는 형태로 function을 선언 및 정의해주면 됩니다.
- 이 경우 TypeError가 발생합니다. 신기하죠?

```javascript
funcA(10);

var funcA = function(value) {
  console.log(value);
}
// TypeError: funcA is not a function
```

## Summary

- 주요 내용을 정리하자면 대략 다음과 같습니다.

1. Javascript에서 function, var 은 모두 코드가 실행될 때 우선 메모리를 할당받는다.
1. Function은 메모리가 할당됨은 물론 정의까지 되어 사용부가 정의부보다 앞에 있어도 hoisting이 발생하게 됩니다.
1. 하지만 anonymous function을 만들어 변수에 assign하여 함수를 사용할 경우에는, hoisting이 발생하지 않습니다. 아직 해당 변수가 function인지 알수 없기 때문이죠.

- 따라서, 이러한 function hoisting은 회피하면서 개발해야 합니다. 쓰고 싶으면 써도 되겠지만, 굳이 이걸 써야 할만큼 중요한 순간은 없다고 생각되고요.
- [ESLint - rules - no use before define](https://eslint.org/docs/rules/no-use-before-define)이 hoisting을 막기 위한 rule이죠.

## Reference

- [mozilla - glossay - Hosting](https://developer.mozilla.org/ko/docs/Glossary/Hoisting)
