---
title: Javascript - String format
category: javascript
tags: javascript function string format
---

## Javascript - String format

- javascripnt에서 String 내에 변수를 위치시키는 방법을 정리합니다.

```html
<!DOCTYPE html>
<html>
    <head>
        <meta charset="utf-8"/>
    </head>
    <body>
        <script>
            var x = "frhyme" // string
            var y = 10 // number
            var z = `${x} and ${y}` // string 

            console.log(`This is ${x}, ${y}, ${z}`);
            // This is frhyme, 10, frhyme and 10
            
            console.log("This is ${x}");
            // This is ${x}
        </script>
    </body>
</html>
```
