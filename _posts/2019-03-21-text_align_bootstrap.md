---
title: 왜 table의 text가 align되지 않는가? 
category: others
tags: html bootstrap text-align
---

## 가운데 정렬!

- html에서 table의 header 부분을 가운데 정렬하려고 했는데, 이게 계속 안되더라고요. 
- 다음처럼 간단한 코드인데 계속 안되서, 왜 안되는지를 찾아봤더니, 

```html
{% raw %}
<thead class="thead-dark">
    <tr>
        {% for col_name in simulated_log%}
        <th scope="col" align="center">{{col_name}}</th>
        {% endfor %}
    </tr>
</thead>
{% endraw %}
```

- [여기서](https://stackoverflow.com/questions/42682942/th-aligncenter-not-working-on-a-bootstrap-table-what-might-be-the-reason) 해답을 찾았습니다. 

- 정리하자면, 
    - `text-align`은 html에서 제공하는 것이 아닌, css에서 제공하는 것임(원래는 되었는데 없어짐)
    - 따라서, 이걸 사용하기 위해서는 외부 css에서 정의해줘야 함.
    - 다행히도 bootstrap에서는 class로 이미 정의되어 있음. 
- 따라서, 다음처럼 사용하면 됩니다.

```html
{% raw %}
<thead class="thead-dark">
    <tr>
        {% for col_name in simulated_log%}
        <th scope="col" class="text-center">{{col_name}}</th>
        {% endfor %}
    </tr>
</thead>
{% endraw %}
```

