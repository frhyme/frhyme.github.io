---
title: javascript - function
category: javascript
tags: javascript function
---

## javascript - function

- javascript에서 function을 정의하는 방법을 정리합니다.

```javascript
function multiply(a, b) {
  return a * b;
}
```

- 다음처럼 한 줄로 정의할 수도 있죠.

```javascript
multiply = (a, b) => a * b

// 괄호와 함께 사용되는 경우에는 return을 명시해줘야 합니다.
multiply = (a, b) => { return a * b }
```
