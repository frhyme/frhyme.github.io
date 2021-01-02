---
title: python - package and import 
category: python-basic
tags: python import python-basic package
---

## python - package and import 

- python으로 개발을 길게 하는 일이 종종 있는데, 귀찮아서 그냥 한 `.py` 파일 내에 모든 함수를 우겨넣고 진행하는 경우들이 많습니다. 뛰어난 개발자라면 어떤 짓을 해도 문제가 없습니다만, 보통의 사람들은 모두 그렇지 않고요, 그냥 저렇게 해버리면 함수가 겹친다거나 하는 자잘한 문제들이 발생하는 경우들이 있죠.
- 따라서, 관련된 함수들을 잘 묶어서 각각의 `.py` 파일로 처리하고, 또 그 `.py`파일들이 많아지면 폴더 안으로 넣어서 처리해준다거나 하는 것이 관리 측면에서 좋습니다. 
- 본 글에서는 python에서 보통 어떻게 package를 관리하고 그 package를 import하는지에 대해서 자세하게 정리합니다.ㄴ

## 같은 경로에 있는 .py 파일 import

- 우리가 실행하려는 파일은 `main.py`이고, import하려는 file은 ``입니다. 같은 폴더 내에 있는 상황이죠.

```plaintext
arithmetic_lib.py
main.py
```

- `arithmetic_lib.py`는 다음과 같이 작성되어 있습니다. 매우 간단한 몇 가지 함수들을 정의하였죠.
- python에는 다양한 내장변수들이 있는데요, `__name__`이 그중 하나입니다. 
  - 해당 `.py` 파일이 직접 실행되는 경우에는 `__name__`에는 `"__main__"`이 들어가고, `import`되었을 때에는 file 이름을 가지게 됩니다.
  - 따라서 그 두 상황을 구분하기 위해서 보통 `if __name__ == "__main__"`를 사용하죠.

```python
def plus(a, b):
    return a + b


def minus(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    return a / b

if __name__ == "__main__":
    print("arithmethic_lib is EXECUTED by python interpreter")
else:
    print("arithmethic_lib is Imported by other python file")
```

- `main.py`에서 `import arithmethic_lib`를 통해 해당 파일 내 function들을 그대로 가져올 수 있습니다.

```python
import arithmethic_lib

print(arithmethic_lib.plus(1, 3)) # 4
print(arithmethic_lib.multiply(4, 5)) # 20
```

---

## 다른 folder에 있는 .py 파일 import

- main.py에서 `frhyme_pkg/arithmethic_lib.py`를 import하려고 합니다. 

```plaintext
frhyme_pkg/
    arithmethic_lib.py
    math_lib.py
main.py
```

- 다음처럼 `import folder_name import library_name`을 통해 가져올 수 있습니다.

```python
from frhyme_pkg import arithmethic_lib
from frhyme_pkg import math_lib

print(arithmethic_lib.plus(1, 3)) # 4
print(arithmethic_lib.multiply(4, 5)) # 20
```

- 그러나, 만약 다음처럼 한번에 가져오고 싶다면 

```python
import frhyme_pkg
```

- `frhyme_pkg/` 폴더 내에 `__init__.py`를 만들어주어야 합니다.

```plaintext
frhyme_pkg/
    arithmethic_lib.py
    math_lib.py
    __init__.py
main.py
```

- 그리고 `__init__.py`는 다음과 같이 작성합니다. 
- 다른 파일에서 `import frhyme_pkg`를 수행할 때 문제없이 실행되려면 해당 폴더 내에 `__init__.py`이 있어야 하죠. 여기에 작성된 부분이 자동으로 실행되게 됩니다.

```python
"""
따라서, 외부에서 import frhyme_pkg와 같은 방식으로 폴더 내 전체를 import하는 경우가 있으면
여기서 다른 모든 file들을 import해서 작성해둬야 함.
. 는 현재 디레토리를 의미함.
"""
from . import arithmethic_lib
from . import math_lib

if __name__ == "__main__":
    print("frhyme_pkg is EXECUTED by python interpreter")
else:
    print("frhyme_pkg is Imported by other python file")
```

- 그 다음에는 다음처럼 그대로 import하고 실행할 수 있습니다.

```python
import frhyme_pkg

print(frhyme_pkg.arithmethic_lib.plus(1, 3)) # 4
print(frhyme_pkg.arithmethic_lib.multiply(4, 5)) # 20
```

---

## folder를 그대로 실행하기

- 만약 터미널에서 `python folder_name`을 실행하고 싶다면, 폴더 내에 `__main__.py`가 있어야 합니다.

```plaintext
frhyme_pkg/
    arithmethic_lib.py
    math_lib.py
    __init__.py
    __main__.py
main.py
```

- `__main__.py`는 다음처럼 작성되어 있구요.

```python
print("This is Main code in frhyme_pkg")
```

- 그 다음 터미널에서 아래를 실행하면 잘 되는 것을 확인할 수 있습니다.

```python
python frhyme_pkg
```

---

## sub_package and `__all__`

- 이번에는 folder 내에 새로운 folder를 만들어 보겠습니다.

```plaintext
frhyme_pkg/
    sub_pkg2/
        __init__.py
        arithmethic_lib.py
    sub_pkg1/
        __init__.py
        math_lib.py
    __init__.py
main.py
```

- 그리고 `sub_pkg1` 폴더 내의 `math_lib.py`에서 `arithmethic_lib.py`를 사용합니다.
- 이 때, `import *` 을 이용해서 다음과 같이 가져와서 사용한다고 합시다. 
- 잘 되야 할 것 같지만, 사실 오류가 나면서 `arithmethic_lib`를 인식하지 못합니다.

```python
from frhyme_pkg.sub_pkg2 import *


def sum_of_list(input_lst):
    r = 0
    for x in input_lst:
        r = arithmethic_lib.plus(r, x)
    return r


def produce_of_list(input_lst):
    r = 1
    for x in input_lst:
        r = arithmethic_lib.multiply(r, x)
    return r
```

- 이는, `import *`를 통해 가져올 때, 넘어가는 `Object`들의 이름이 명시적으로 작성되어 있지 않기 때문이죠.
- `from frhyme_pkg.sub_pkg2 import *`에서 `sub_pkg2` 내 `__init__.py`내에 어떤 Object가 넘어가는지에 대해서 명확하게 작성되어 있어야 하죠.
- 따라서,`frhyme_pkg/sub_pkg2/__init__.py` 내에 아래와 같이 작성합니다. 즉, `import *`을 할때 넘어가는 function의 이름들을 정해줘야 하죠. 이렇게 써 놔야, 넘어갑니다.

```python
__all__ = ["arithmethic_lib"]
```

## wrap-up

- 같은 경로에 있다면 그냥 `import file_name`을 통해서 가져오면 된다.
- 다른 폴더에 있다면 `from folder_name import file_name`을 사용해 가져오거나, folder 내에 `__init__.py`를 만들고 이 파일 내에서 `import` 문을 작성한다음, `import folder_name`를 통해 가져올 수 있습니다.
- `from folder_name import *`를 통해 가져오는 경우, folder_name 내 `__init__.py`내에 `__all__ = [module_name]`를 통해 `import *`를 사용했을 때 넘어가야 하는 module들이 정의되어야 합니다.
