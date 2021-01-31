---
title: html의 select 로 정해진 값 javascript로 가져오기. 
category: web
tags: html web select javascript
---

## select로 정해진 값 가져오기. 

- html에서는 다양한 요소를 통해서 사용자가 원하는 input을 정의할 수 있습니다. 
- 이 때, `select`라는 드롭다운형태의 박스를 정의할 수도 있죠. 
- 이것을 정의하고, 값이 변경되었을때(정확히는 input이 발생했을 때) 값을 javascript로 넘기는 동작을 수행합니다. 
- 매우 간단합니다만, 아무튼 이걸 수행합니다. 

## do it. 

- 코드는 다음과 같습니다. 
    - select 요소에서 선택된 index를 찾고
    - select.options 어레이에 해당 index를 넘겨주고, value를 가져옵니다. 

```html
<html>
    <!--
        select를 만들고, 이 값이 변경되었을 때마다, 적절한 처리를 수행함.
    -->
    <head>
    </head>
    <body>
        <!--ID를 정의하기는 했으나, -->
        <select id="select1" onchange="alert_select_value(this);">
            <option value="volvo">Volvo</option>
            <option value="saab">Saab</option>
            <option value="mercedes">Mercedes</option>
            <option value="audi">Audi</option>
        </select>
    </body>
    <script>
        var alert_select_value = function (select_obj){
            // 우선 selectbox에서 선택된 index를 찾고 
            var selected_index = select_obj.selectedIndex;
            // 선택된 index의 value를 찾고 
            var selected_value = select_obj.options[selected_index].value;
            // 원하는 동작을 수행한다. 여기서는 그냥 alert해주는 식으로만 처리함. 
            alert(selected_value);
        };
    </script>
</html>
```

## wrap-up

- 비교적 간단합니다. 
- 물론 저는 자바스크립트를 잘 몰라서, 하면서 계속 배우는 느낌이네요 하하핫.