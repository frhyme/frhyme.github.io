---
title: python에서 main function 활용하기 
category: python
tags: python python-lib
---

## intro

- python 코드파일을 보면, `if __name__=="__main__"`이라는 부분이 있는 코드를 보실 수 있습니다. c로 코딩을 해보신 분들은 아마도 이 부분을 보시면 `void main()`를 떠올리실 수 있죠. 
- 이 부분이 뭔지 모르겠어서, 간단하게 정리를 해봤습니다. 

## main function

- 간단하게 해당 코드를 직접 실행할 때와 코드를 import할 때가 구분됩니다. 
- 간단한 코드를 작성해서 파일을 만들었습니다. 이 코드파일을
    - import할 때와 
    - 직접실행할 때 결과가 달라집니다. 

```python
code = """
if __name__=="__main__":
    print("코드파일이 실행되었습니다.")
else:
    print("코드파일이 import되었습니다. ")
"""
f = open("main_test.py", 'wb')
f.write(code.encode())
f.close()

import main_test

print("="*20)

## jupyter notebook에서 파이썬 코드를 직접 실행하기 위한 magic command
%run main_test.py
```

- `import` 하면 `if __name__=="__main__":`부분에 있는 코드가 실행되지 않습니다. 

```
코드파일이 import되었습니다. 
====================
코드파일이 실행되었습니다.
```

## wrap-up

- 코딩을 할때, 이 코드 파일이 직접 실행될때와 `import`될 때를 구분해서 코딩하는 습관을 들이면 좋을 것 같습니다. 