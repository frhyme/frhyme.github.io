---
title: 
category: 
tags: 
---

## Javascript - Promises 

- Promises는 "약속"을 의미하죠. 동일하게 javascript에서의 Promises 또한, "미래에 어떤 이벤트가 발생한다면, 무엇이 실행된다(혹은 실행되지 않는다)"를 정의하는 것을 말하죠. "미래를 가정한다"라고 말할 수도 있겠네요.
- 가령, 서버로부터 데이터를 전달받아야 할 때, 데이터를 전달 받을 때 까지 기다렸다가, 데이터가 넘어오면 실행하도록 하는 것, 그런게 바로 Promises로 인해서 가능해지는 것이죠.

```javascript
let promise = new Promise(function(resolve_func, reject_func) {
    /*
    - 실행될 코드.
    - resolve_func(value): 조건이 만족되었을 때 실행되며 value를 input으로 받는 함수
    - reject_func(err): 조건이 만족되지 않았을 때, err을 input으로 받는 함수
    */
});
```