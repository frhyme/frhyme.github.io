---
title: jinja에서 variable 선언하기. 
category: python-libs
tags: python flask jinja python-libs variable
---

## jinja에서 직접 변수를 선언해봅시다. 

- 보통 jinja에서는 `for`와 `if`만을 사용합니다 변수는 `render_template`에서 함께 넘어온 것들 뿐이죠. 
- 그러나, 경우에 따라서는 직접 내부에서 값을 선언해주는 것이 필요할 때가 있습니다. 
- 어떻게 할 수 있을까요? 

## do it 

- 언제나 그렇듯 매우 쉽습니다. 하하하. 
- 앞에 `set`을 붙여주면 끝납니다. 

```html
{% raw %}
<div>
    {% set a = 3 %}
    {{a}}    
</div>
{% endraw %}
```

- 비슷하게, 리스트를 선언하고 값을 넣어줄 수도 있습니다.
- 그러나, `a.append(i)` 부분이 statement가 아니라, statement with print로 되어 있는 것을 알 수 있습니다. 즉, 해당 부분이 실제 Html에서 출력이 된다는 것이죠. 해당 부분이 따로 값을 리턴하지 않기 때문에, 그냥 `None`이 리턴되기는 합니다. 

```html
{% raw %}
<div>
    {% set a = [] %}
    {% for i in range(0, 10) %}
        {{ a.append(i) }}
    {% endfor %}
    {{a}}
</div>
{% endraw %}
```

- 사실, 이럴때는 그냥 이 부분을 script로 넘겨버리면 되기는 합니다. 

```html
{% raw %}
<div>
    <script>
        {% set a = [] %}
        {% for i in range(0, 10) %}
            {{ a.append(i) }}
        {% endfor %}
    </script>
    {{a}}
</div>
{% endraw %}
```

- 비슷하게, 딕셔너리에 대해서도 다음처럼 만들수 있죠. 

```html
{% raw %}
<div>
    <script>
        {% set a_lst = [] %}
        {% for i in range(0, 10) %}
            {{ a_lst.append(i) }}
        {% endfor %}

        {% set b_dict = {} %}
        {% for i in range(0, 10) %}
            {{ b_dict.update( {"key_"+i|string: i+10} )}}
        {% endfor %}
    </script>
    {{a_lst}}
    <br>
    {{b_dict}}
{% endraw %}
</div>

```


## wrap-up

- 생각보다, jinja template에서 Python을 돌리는 것이 크게 어렵지는 않습니다. 물론 렌더링할 때 시간이 좀 걸릴 수는 있겠지만요. 
- 필요한 함수, 라이브러리들은 `render_template`에서 함께 넘겨주고, 값을 처리할 때도 꽤 비슷한 방식으로 다 할 수잇는 것 같네요. 
- 이렇게 처리할 경우, backend, frontend가 합쳐지니까 꽤 편하게 코딩할 수 있는 장점도 있는 것 같습니다. 



## reference

- <https://stackoverflow.com/questions/3727045/set-variable-in-jinja>