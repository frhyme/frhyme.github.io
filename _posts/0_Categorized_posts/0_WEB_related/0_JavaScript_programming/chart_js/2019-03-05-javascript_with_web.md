---
title: javascript를 웹에서 돌리기. 
category: others
tags: javascript web html 
---

## 간단한 인터랙션을 넣읍시다.

- 간단하게, 웹페이지에서 어떤 버튼을 눌렀을 때 웹페이지의 텍스트가 바뀌는 것을 수행해보려고 합니다. 

### just html

- html로만 할 경우에는 다음과 같습니다. 
- 일단은 특정 버튼을 누르면 alert가 뜨도록 한것이기는 한데, 이 경우에는 정보와 제어가 함께 있는 것이 됩니다. 향후 유지보수에서 문제가 발생하기 쉬울 수 있죠. 

```html
<!DOCTYPE html>
<html>
    <body>
        <!--
            아래처럼 html 소스에 그대로 넣을 수도 있으나, 이 경우 정보(html)와 제어(js)가 함께 있게 되어 문제가 발생할 수 있다.
        -->
        <input type="button" onclick="alert('Hello world')" value="Hello world" />
    </body>
</html>
```

### html and js 

- javascript를 html의 다른 페이지에 분리한 경우 다음처럼 됩니다.
- 복잡해보이지만, script상에서 해주는 것은 다음과 같습니다. 
    - 웹페이지 상에서 특정한 동작을 수행할 수 있도록 해주는 요소, 태그를 찾은 다음, 
    - `addEventListener`라는 메소드를 활용해서 특정 이벤트(`click`)에 대해서 수행하는 함수를 추가해주고, 
    - 그 함수에서는 전체 문서에서 `li` 태그를 가진 모든 요소의 내용을 변경해줍니다. 

```html
<!DOCTYPE html>
<html>
    <head>
        <meta charset="utf-8" />
    </head>
    <body>
        <ul id="list">
            <li>empty</li>
            <li>empty</li>
            <li>empty</li>
            <li>empty</li>
        </ul>
        <input id="execute_btn" type="button" value="execute" />
        
        <!-- javascript -->
        <script type="text/javascript">
            document.getElementById('execute_btn').addEventListener('click', 
                function(){
                    li_s = document.getElementsByTagName('li');
                    for(var i=0; i<li_s.length ;i++){
                        li_s[i].innerHTML = 'coding everybody';
                    }
                }
            )
        </script>
    </body>
</html>
```


### jquery

- 하지만 jquery를 사용하면 다음처럼 간단해집니다. 

```html
<html>
    <head>
        <meta charset="utf-8"/>
        <script src="https://code.jquery.com/jquery-1.11.0.min.js"></script>
    </head>
    <body>
        <!--
            - head 부분에서는 jquery resource를 가져오고, 
            - body 부분에서는 특정한 id에서 어떠한 이벤트가 발생했을때 동작하는 부분을 세팅해줌. 
        -->
        <ul id="list">
            <li>empty</li>
            <li>empty</li>
            <li>empty</li>
            <li>empty</li>
        </ul>
        <input id="execute_btn" type="button" value="execute" />
        <script>
            $('#execute_btn').click(
                function(){
                    $('#list li').text('coding everybody');
                }
            )
        </script>
    </body>
</html>
```

## what is jquery??

- [jquery 공식 홈페이지](https://jquery.com/)에 의하면 대략 다음으로 정의됩니다. 

> jQuery is a fast, small, and feature-rich JavaScript library. 
> It makes things like HTML document traversal and manipulation, event handling, animation, and Ajax much simpler with an easy-to-use API that works across a multitude of browsers. 
> With a combination of versatility and extensibility, jQuery has changed the way that millions of people write JavaScript.

- HTML document의 순회, 조작, 이벤트 핸들링, 애니메이션등을 쉽게 사용할 수 있도록 해주는 라이브러리라고 합니다. 많은 사람들이 사용하고 있기도 하구요. 
- 그런데, 여기서 제가 드는 궁금증은 jquery가 그다지 친절하지 않다는 것이죠. 가독성이 너무 떨어지는 것 같은 생각이 듭니다. pure javascript로 작성한 경우, 코드가 좀 길어지기는 해도 이해는 어렵지 않은데, 지금은 좀 ...

## wrap-up

- 아무튼 이 포스트는 아주 간단하게 웹페이지를 변형하는 것을 자바스크립트에서 어떻게 할 수 있는지를 정리하였습니다. 
- jquery를 쓰면 코드가 매우 간단해지기는 하는데, 가능하면 저는 그냥 퓨어 자바스크립트로 하고 싶네요. 