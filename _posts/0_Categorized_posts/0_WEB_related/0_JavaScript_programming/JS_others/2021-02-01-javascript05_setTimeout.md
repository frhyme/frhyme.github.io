---
title: Javascript - setTimeout
category: javascript
tags: javascript programming
---

## Javascript - setTimeout

- javascript에서 일정 시간이 지연된 다음 동작이 수행되게 하려면 `setTimeout(callback_func, delay, args)`를 사용하면 됩니다.
- 즉 `delay` milli-second가 경과된 다음 `callback_func`가 args를 넘겨 받아서 실행됩니다.

```javascript
/*
- callback_func: 익명함수를 정의하는 방식인 () => {} 를 사용해서 설정했습니다.
- delay는 2000으로 설정했습니다. 단위가 milliSecond 이므로 
2000 millisecond = 2 second가 됩니다.
*/
setTimeout(
    () => {
        console.log("After  setTimeout() at " + Date().toString().substring(0, 15))
    }, 2000
);
```

- 혹은 다음처럼 function을 미리 정의한 다음 사용할 수도 있습니다.

```javascript
// function을 미리 정의하고
function log_str(inputStr) {
    console.log("log_str: " + inputStr + " at " + Date().toString().substring(0, 15))
}
// function, delay, arg를 순서대로 넘겨주면 됩니다.
setTimeout(log_str, 1000, "a");
```

## Example 

- 간단하게 html code 내에 작성하였습니다.

```html
<!DOCTYPE html>
<html>
    <head>
        <meta charset="utf-8"/>
    </head>
    <body>
        <script>
            // 2 초 뒤에 아래 함수들을 실행함.
            console.log("Before setTimeout() at " + Date().toString().substring(0, 15))
            setTimeout(() => 
                {
                    console.log("After  setTimeout() at " + Date().toString().substring(0, 15))
                }, 2000
            );
            // output
            // Before setTimeout() at Mon Feb 01 2021
            // After  setTimeout() at Mon Feb 01 2021

            function log_str(inputStr) {
                console.log("log_str: " + inputStr + " at " + Date().toString().substring(0, 15))
            }
            setTimeout(log_str, 1000, "a");

        </script>
    </body>
</html>
```
