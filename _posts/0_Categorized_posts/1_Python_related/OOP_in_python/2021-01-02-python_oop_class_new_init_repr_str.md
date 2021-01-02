---
title: python - OOP - new, init, repr, str
category: python-basic
tags: python python_basic, class OOP 
---

## python - OOP - new, init, repr, str

- python class 정의시 다음 4가지 method를 설명합니다.
  - `__new__`: 보통 `__init__`을 생성자라고 알고 있지만, 사실 메모리를 확보해주는 진짜 생성자는 `__new__`입니다. 아래 코드에서는 이 부분에서 생성될 수 있는 Object의 개수를 제한하고, 추가로 생성해야 할 경우 `None`을 리턴하도록 하였습니다.
  - `__init__`: 보통 `__new__`의 경우 암묵적으로 실행되기 때문에, 이후 생성된 변수들에 대해서 값을 초기화해줍니다.
  - `__str__`: 객체를 string으로 변환하게 될 경우 표시되어어야 하는 문자열을 의미합니다.
  - `__repr__`: `__str__`과 같은 역할을 수행하지만, 우선순위가 낮습니다.

```python
class AA(object):
    # class_variable
    n_object = 0

    def __new__(cls, *args, **kwargs):
        # 사실 __init__ method가 생성자라고 알려져 있으나,
        # __new__가 생성자이며,
        # 이 단계에서 메모리를 확보한 다음 바로 __init__이 수행됨
        # 즉, __init__은 초기화 method라고 해주는 것이 더 적합함.
        if cls.n_object < 2:
            # 2개 이상 instance가 생겨날 수 없도록 제한함.
            cls.n_object += 1
            return super().__new__(cls)
        else:
            return None

    def __init__(self, name):
        # instance var에 값을 할당함.
        self.name = name

    def __repr__(self):
        # Reprensentation of Instance
        # __str__가 없는 경우 실행됨
        # 따라서 보통 개발자가 __str__ 메소드 정의전에 테스트하기 위해서 사용함.
        return f"AA instance: {self.name}"

    def __str__(self):
        # __str__가 있으면 __repr__을 덮어씌워버린다고 보면 됨.
        return f"{self.name}"
```

- 다음을 실행해보면, 
  - `__new__` 메소드에서 1개만 만들기로 하였기 때문에, `a2`에는 None이 할당됩니다.
  - 그리고, 해당 class Instance가 String으로 변환되어야 할 때는 `__repr__` 혹은 `__str__` method를 사용하게 되는데 `__str__`의 우선순위가 더 높습니다.

```python
a1 = AA("A1")
a2 = AA("A2")

# __new__ 에서 생성 개수를 제한하였으므로
# a2 에는 None이 할당됨.
print(a2)  # None

# __str__ method가 실행됨.
print(a1)  # A1
print(str(a1))  # A1
```
