---
title: Javascript - setInterval
category: javascript
tags: javascript function setInterval setTimeout
---

## Javascript - setInterval

- `setInterval(function, intervalTime, argument)`은 `intervalTime` milliseconds 마다 argument를 function에 넘겨서 실행합니다.
- 아래 코드는 1000 milliseconds마다 `printThisTime`를 실행합니다. argument는 따로 넘기지 않았구요.

```javascript
function printThisTime() {
    var currentDate = new Date();
    console.log("Now is", currentDate.toString().substring(0, 25));
}
setInterval(printThisTime, 1000);
```

- 실행하면 아래와 같이 1초마다 결과가 출력되죠.

```plaintext
Now is Tue Feb 02 2021 21:39:02 
Now is Tue Feb 02 2021 21:39:03 
Now is Tue Feb 02 2021 21:39:04 
Now is Tue Feb 02 2021 21:39:05 
Now is Tue Feb 02 2021 21:39:06 
Now is Tue Feb 02 2021 21:39:07 
Now is Tue Feb 02 2021 21:39:09 
Now is Tue Feb 02 2021 21:39:10 
Now is Tue Feb 02 2021 21:39:11 
```

## SetInterval 종료하기

- 그러나, `setInterval`은 종료조건을 따로 정할 수 없습니다. 실행하면 그냥 브라우저가 종료될때까지 게속 출력된다는 말입니다.
- 따라서, 다음처럼 `setInterval`과 `setTimeout`을 함께 사용하면 해결할 수 있죠.

```javascript
<!DOCTYPE html>
<html>
    <head>
        <meta charset="utf-8"/>
    </head>
    <body>
        <!--
        - 이 요소는 3개의 class가 정의되어 있습니다.
        -->
        <script>
            console.log("== Start")

            // function printCurrentDate을 1초마다 실행하도록 setInterval
            // 다만, 이후에 종료할 수 있도록 setInterval의 ID를 저장해놓음
            function printCurrentDate() {
                var currentDate = new Date();
                console.log("Now is", currentDate.toString().substring(0, 25));
            }
            var setIntervalId = setInterval(printCurrentDate, 1000);

            // 5000 milliseconds 후에 
            // setIntervalId를 멈춤
            setTimeout(
                () => {
                    clearInterval(setIntervalId)
                    console.log("== Complete")
                }, 
                5000
            )
            
        </script>
    </body>
</html>
```

- 결과는 다음과 같습니다.

```plaintext
== Start
test.html:14 Now is Tue Feb 02 2021 21:49:14 
test.html:14 Now is Tue Feb 02 2021 21:49:15 
test.html:14 Now is Tue Feb 02 2021 21:49:16 
test.html:14 Now is Tue Feb 02 2021 21:49:17 
test.html:14 Now is Tue Feb 02 2021 21:49:18 
== Complete
```
