---
title: datatable을 이용해서 웹페이지에 테이블을 예쁘게 만들어봅시다. 
category: others
tags: html datatable table jquery 
---

## 웹페이지의 테이블을 예쁘게 만들어봅시다. 

- bootstrap에서 지원하는 요소는 매우 간단해서 테이블을 적당히 예쁘게 보여줍니다. 
- 그런데, 필요에 따라서, 마치 엑셀처럼 칼럼을 오름차순/내림차순으로 정렬한다거나, 필요한 요소만 찾는다거나 하는 식의 기능이 추가되면 좋을 것 같다는 생각을 합니다. 

## datatable

- 찾아보니까 [datatable](https://datatables.net/)이라는 유용한 라이브러리들이 있습니다. 
- 순서는 다음과 같습니다. 

- 우선 CDN에서 필요한 라이브러리를 가져오고, 

```html
<!-- data table에서 jquery를 사용하기 때문에 가져옵니다.-->
<script type="text/javascript" src="https://code.jquery.com/jquery-3.3.1.js"></script>
<!-- data table -->
<link rel="stylesheet" type="text/css" href="https://cdn.datatables.net/1.10.19/css/jquery.dataTables.css">
<script type="text/javascript" charset="utf8" src="https://cdn.datatables.net/1.10.19/js/jquery.dataTables.js"></script>        
```

- `table`에 아이디를 추가하고요

```html
<table id="simulate_log" class="table table-bordered table-hover table-sm"
```

- javascript에서 해당 요소를 변형해줍니다. 
    - pure javascript로는 안되고, 아래처럼 jquery를 사용해야 합니다. 

```html
<script>
    // datatable에서 jquery를 사용함
    $(document).ready(function () {
        $('#simulate_log').DataTable();
    });
</script>
```

- 예시 code는 다음과 같습니다. 저는 flask를 이용하기 때문에 jinja 형식으로 템플릿이 구성되어 있습니다. 

```html
{% raw %}

<!-- data table에서 jquery를 사용하기 때문에 가져옵니다.-->
<script type="text/javascript" src="https://code.jquery.com/jquery-3.3.1.js"></script>
<!-- data table -->
<link rel="stylesheet" type="text/css" href="https://cdn.datatables.net/1.10.19/css/jquery.dataTables.css">
<script type="text/javascript" charset="utf8" src="https://cdn.datatables.net/1.10.19/js/jquery.dataTables.js"></script>        

<h2> This is h2! </h2>
<div style="height:100px">
    <table id="simulate_log" class="display">
        <thead class="thead-dark">
            <tr>
                {% for i in range(0, 4)%}
                <th scope="col">col_{{i}}</th>
                {% endfor %}
            </tr>
        </thead>
        <tbody>
            {% for i in range(0, 10) %}
            <tr>
                <td>{{i}}</td>
                <td>{{i}}</td>
                <td>{{i}}</td>
                <td>{{i}}</td>
            </tr>
            {% endfor %}
        </tbody>
    </table>
</div>
<script>
    // datatable에서 jquery를 사용함
    $(document).ready(function () {
        $('#simulate_log').DataTable();
    });
</script>
{% endraw %}
```

## wrap-up

- 세부적인 요소는 css 등을 이용해서 스타일링을 해주면 좋을 것 같습니다. 
- 또한 폰트를 수정하는 것도 필요할 것으로 생각되네요. 