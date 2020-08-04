---
title: python에서 main function 활용하기 
category: python
tags: python python-lib
---

## intro - main function

- python 코드파일을 특히, 라이브러리의 python 팡리들을 보면 다음 코드를 종봉 보실 수 있습니다. C로 코딩을 해보신 분들은 이를 보면 바로 `int main()`과 같은 코드가 떠오를 수 있죠.

```python
if __name__=="__main__":
    # CODE 
```

- 이 아이는 정확하게 무엇을 하는 아이인지, 정리합니다.

## main function in python

- python으로 작성된 코드 파일, 가령 `abc.py` 파일이 있다고 합시다. 우리는 이 파을 두 가지 방식으로 사용할 수 있습니다.
  1) `import abc`를 사용해서 python 코드를 현재 코드에 import
  2) 터미널에서 `python abc.py`를 통해 해당 코드를 그대로 실행
- 여기서, 만약 `import abc`를 하게 되면, `if __name__=="__main__":`에 있는 부분이 실행되지 않습니다.

## illustration

- 만약 우리가 가진 `abc.py`라는 파일에 다음과 같이 작성되어 있다고 하겠습니다.
- 각각, import이냐, 직접 실행이냐에 따라서 달라진다는 이야기죠.

```python 
if __name__ == "__main__":
    # 터미널에서 python abc.py 일 경우 이 부분이 실행됨
    print("코드파일이 실행되었습니다.")
else:
    # import abc => 이 부분이 싫행됨 
    print("코드파일이 import되었습니다.")
```

## wrap-up

- C로 코딩할 때를 생각해보면, header 파일이 따로 있었습니다. `#include <stdio.h>`와 같은 방식으로 header 파일을 현재 코드로 가져왔죠.
- 다만, python에서는 굳이 서로 다른 두 파일형식을 가지지 않고 하나로 통일한 다음, 그 방식을 코드 내부에서 규정할 수 있도록 만들었습니다. 따라서 가끔 헷갈릴 때가 있기는 하지만, 뭐 하라는 대로 해야죠 뭐 호호호