---
title: 다른 파이썬 코드 import하기 
category: python-basic
tags: python python-lib
---

## intro

- 예전에 작성해둔 파이썬 코드를 가져오고 싶을 때가 있습니다. 이걸 어떻게 할 수 있는지 정리했습니다. 

## import code

- 일단 해당 코드 파일이 현재 코드파일과 같은 경로에 있어야 합니다. 
- 코드 파일명을 그대로 import 하면 됩니다. 
    - 변수, 함수, 클래스, 그리고 해당 코드에서 import한 다른 라이브러리까지 모두 긁어옵니다. 

```python
code = """
import numpy as np 

test_int = 10
test_str = "test string"

def test_func():
    print('test function executed')

class RandomNumberGen:
    def __init__(self, size):
        self.size = size
    def gen_normal(self):
        print(np.random.normal(0, 1, self.size))
"""

f = open('import_test.py', 'wb')
f.write(code.encode())
f.close()

import import_test

import_test.test_func()
print('='*20)
print(import_test.test_int)
print('='*20)

import_test.RandomNumberGen(5).gen_normal()
print('='*20)
```

```
test function executed
====================
10
====================
[-0.78813035 -0.15400503  1.42679214 -0.03665077 -0.02774182]
====================
```

## 다른 경로에 있는 코드 파일 가져오기 

- 다른 경로에 있는 파일을 가져오려면 sys에 **절대경로**를 넣어두어야 합니다.

```python
f = open('../../assets/import_from_another_file.py', 'wb')
f.write("""
def test_func():
    print('import code in another file')
""".encode()), f.close()

import sys
## 상대경로를 넣으면 안되고 절대 경로만 넣어야 함 
sys.path.append('/Users/frhyme/frhyme.github.io/assets/')

import import_from_another_file
import_from_another_file.test_func()
```

```
import code in another file
```

## 하위 폴더에 있는 코드 가져오기 

- 큰 프로그램을 만들어야 할때는 폴더 안에 새로운 폴더가 생겨나고 폴더별로 코드를 관리하게 되는데, 하위폴더에 있는 코드를 가져오고 싶을때가 있습니다. 
- 하위 폴더 내부에 `__init__.py`파일만 있으면 잘 동작합니다. 해당 파일에는 아무 값이 없어도 상관없습니다. 
    - 단, 이 경우 `import test_folder.test_code`와 같은 형태로 표현하거나, `from test_folder import test_code`로 표현해주어야 합니다. 

```python
f = open('test_folder/test_code.py', 'wb')
f.write("""
def test_func():
    print("="*30)
    print("test function executed")
    print("="*30)
""".encode()), f.close()

## 그냥 __init__.py가 있어야 함
f = open('test_folder/__init__.py', 'wb')
f.close()

"""
import test_folder 로는 test_code까지 읽어들이지 못하므로 다음으로 명확하게 표현해줘야 함
아니면 from test_folder import * 도 괜찮음 
"""
import test_folder.test_code
test_folder.test_code.test_func()
```

```
==============================
test function executed
==============================
```

## reference

- <http://oniondev.egloos.com/9753808>