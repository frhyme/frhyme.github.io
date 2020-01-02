---
title: jinja template에서 python function 더 사용하기
category: python-libs
tags: python jinja python-libs flask template enumerate zip
---

## jinja template에서 python의 다른 펑션을 사용해봅시다

- 음, 사실 간단한 겁니다. 예를 들어서, `enumerate`, `zip`등을 jinja template에서 사용해보고 싶다는 말입니다. 
- 기본적으로는 다음과 같은 것만 가능합니다. 

```html
{% raw %}
<div>
    {% for a in test_lst1 %}
        {{i}}, {{a}}<br>
    {% endfor %}
</div>
{% endraw %}
```

- 그런데, 필요에 따라서, `zip`, `enumerate`을 사용하고 싶을 때가 있습니다.
- 이럴 때는 그냥, `render_template`에서 변수로 함께 넘겨주면 됩니다. 
- 예를 들어서, 파이썬에서 `render_template`에서 변수들 넘기는 것처럼 모두 넘겨주고, 

```python
@app.route('/test')
def test():
    test_lst1 = [f"aa{i}" for i in range(0, 10)]
    test_lst2 = [f"bb{i}" for i in range(0, 10)]
    return render_template('test.html', 
        test_lst1=test_lst1, 
        test_lst2=test_lst2, 
        enumerate=enumerate, 
        zip=zip, 
        pd=pd,
        Markup=Markup
    )
```

- html에서는 다음처럼 그냥 모두 사용하면 됩니다.

```html
{% raw %}
<div>
    {% for i, a in enumerate(test_lst1) %}
        {{i}}, {{a}}
        <br>
    {% endfor %}
    {% for a, b in zip(test_lst1, test_lst2) %} 
        {{a}}, {{b}}
        <br> 
    {% endfor %}
    {{Markup(pd.DataFrame({"aa":test_lst1}).to_html())}}
</div>
{% endraw %}
```

- 만약, 매번 넘기는 것이 귀찮다면, 다음처럼 세팅을 하는 것이 더 좋을 수 있구요. 

```python
### jinja update 
app.jinja_env.globals.update(
    zip=zip, 
    enumerate=enumerate, 
)
########################
```


## wrap-up

- 처음에는 jinja template이 너무 할 수 있는게 없다라고 생각했는데, 생각보다 확장이 쉽게 됩니다. 
- 이렇게 확장이 되는 것이면, 사실 좀 지나치게 말해서 javascript의 많은 부분이 필요하지 않고, python으로 대부분을 처리할 수 있는 것이 아닐까? 싶기도 하네요.