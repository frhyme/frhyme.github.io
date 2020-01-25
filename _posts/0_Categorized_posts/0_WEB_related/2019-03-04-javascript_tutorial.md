---
title: javascript를 좀 파보고 있습니다. 
category: others
tags: javascript html css
---

## why javascript suddenly

- 사실 javascript까지 해야 하나 싶기는 한데, 이유는 다음과 같아요. 
    - 웹 프로그램을 하나 만드는 중이다. 
    - 데이터를 긁어와서 시뮬레이션을 수행하고 시뮬레이션되는 상황을 웹에 그대로 보여주고 싶다. 
    - python의 라이브러리를 가지고 사용해봤는데 적당히 되지만, 너무 지나치게 느리다. 
    - 그래서 d3.js를 사용해보려고 하는데, 일단 기본적인 javascript는 사용할줄 알아야 할 것 같다. 
- 따라서, javascript를 좀 사용해보려고 합니다. 

## what is javascript

- html, css는 정적입니다. 예를 들어서, 사용자의 상호작용에 따라서 특정한 동작을 수행할 수 있도록 하는 것이 어렵죠(onclick 등으로 부분적으로는 가능하게 할 수 있는 것으로 알고 있습니다만).
- 이 부분을 보완하기 위해서 javascript는 웹 상의 요소들이 사용자와의 상호작용에 따라서 작동할 수 있도록 만들어주는 프로그래밍 언어라고 생각하면 좋습니다. 
- java라는 말이 붙어 있어서, 보통 사람들이 java와 유사한 언어인 것으로 생각하기 쉽지만, 문법적으로는 오히려 c와 유사하다고 느껴지는 부분이 많습니다. 

## basic 

- 다른 언어들에서, 예를 들어 파이썬의 경우는 `.py`라는 파일에 코드를 작성하고, 해당 코드를 컴파일 시키는 식으로 수행됩니다. 
- javascript의 경우도 `.js`라는 파일이 있지만, 이는 파이썬에서의 `import`로 가져오는 라이브러리의 개념에 좀 더 가깝고, 실제 코드는 `html` 파일 내에서 수행됩니다. 
- 아래와 같이 html 파일 내에 `<script>`로 묶인 태그 안에서 javascript가 포함되어 있어야 합니다. 

```html
<script type='text/javascript'>
</script>
```

```html
<!DOCTYPE html>
<html>
    <head>
        <meta charset="utf-8"/>
    </head>
    <body>
        <script type="text/javascript">
            var a = 3;
            document.write(a);
            // 함수 선언
            function print_something(n){
                for(var i=0;i<n;i++){
                    document.write("coding everybody"+String(i)+"<br>");
                }
            }
            print_something(3);
            // loop and array(or list)
            var b = "1234"
            for(var i=0;i<b.length;i++){
                document.write(b[i])
            }
            // define object 
            var test_class = {
                'attr_list':{'name':'frhyme', 'age':34}, 
                'show': function(){
                    for(var key in this.attr_list){
                        document.write(key+": "+this.attr_list[key]+"<br>")
                    }
                }
            }
            test_class.show();
            // define object better
            function Person(name){
                this.name = name;
                this.introduce = function(){
                    return "My name is"+this.name;
                }
            }
            p1 = new Person("frhyme")
            document.write(p1.introduce())
        </script>
    </body>
</html>
```

## wrap-up

- 문법 자체는 c와 유사하게 느껴집니다. for문도 그렇고요. 
- 다만, string format에서 좀 불편함이 있는 것 같네요. 물론 아마 다른 라이브러리를 추가로 가져오면 문제가 없다는 것.
- type을 명확하게 지정하지 않고, var을 사용해서 선언해주지만, 굳이 쓰지 않아도 알아서 먹힌다는 점에서는 Python과 유사하고. 
- 변수에 익명함수를 넘겨서 처리할 수 있다는 장점. 함수를 argument로 받아서 처리할 수 있다는 것. 
    - 또한 callback 함수라고 부르는 부분의 경우 higher-order function과 의미적으로 동일함. 
- string도 list 혹은 array로 인식됨.
- javascript에서 객체는 python에서의 dictionary와 동일
    - 또한 method로 사용하려면 key의 value에 익명함수를 넘겨주면 됨. 
    - 하지만 이 경우 매번 객체의 생성자가 따로 없게 되는데, 여기서 function으로 클래스를 정의하고 내부에 생성자를 만들어서 수행하면 됨. 