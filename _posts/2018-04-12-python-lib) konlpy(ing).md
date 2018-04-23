---
title: python-lib) MacOS에서 `konlpy` 설치하고 사용하기(실패기)
category: python-lib
tags: python python-lib konlpy macOS jpype not-yet

---

## intro

- 더 진행하기 전에, 현재로서는 실패한 상황입니다.
- 'programmer.co.kr'에서 다른 분께서 해결했다는 것 같아서, 이를 다시 해보기 위해서 시도했지만, 여전히 실패했습니다. 
    - 만약 이후에 konlpy가 필요하다면, 부트캠프로 윈도우를 설치하거나, 아무튼 다른 방식으로 시도하고 싶습니다.
    - 따라서, 앞으로 맥북에 다시 konlpy를 설치할 일이 없을 것 같기는 하지만, 일단 이 상처를 기억해놓자는 마음에 정리해둡니다. 
- 아래 내용을 참고하였습니다. 
    - https://programmers.co.kr/learn/courses/21/lessons/951



```python
import konlpy
```


    ---------------------------------------------------------------------------

    ModuleNotFoundError                       Traceback (most recent call last)

    <ipython-input-3-32cb478bd821> in <module>()
    ----> 1 import konlpy
    

    ~/anaconda3/lib/python3.6/site-packages/konlpy/__init__.py in <module>()
         13 from . import data
         14 from . import internals
    ---> 15 from . import tag
    

    ~/anaconda3/lib/python3.6/site-packages/konlpy/tag/__init__.py in <module>()
          2 import warnings
          3 
    ----> 4 from ._hannanum import Hannanum
          5 from ._kkma import Kkma
          6 from ._komoran import Komoran


    ~/anaconda3/lib/python3.6/site-packages/konlpy/tag/_hannanum.py in <module>()
          5 import re
          6 
    ----> 7 import jpype
          8 
          9 from .. import jvm


    ModuleNotFoundError: No module named 'jpype'


## 시작은 항상 에러 앤 에러 앤 에러 

- `ModuleNotFoundError: No module named 'jpype'`라는 에러가 발생했습니다. 
    - 찾아보니, `jpype`는 파이썬 프로그램이 java 클래스 라이브러리에 접근할 때 필요한 라이브러리입니다. 
    - 내가 쓰고 싶은 것은 `konlpy`인데 왜 jpype를 필요로 하는가? 라는 생각이 듭니다만, 무엇인가를 설치할 때, 호기심은 인간을 고통스럽게 만들 뿐이므로 잠시 멈춥니다. 
    
- 아무튼 모듈이 없다고 하니 마법의 주문 pip 를 써보기로 합니다. 
    - 터미널 창에서 `pip install jpype`을 해보았으나, 다음과 같은 오류가 발생합니다. 
    - "Could not find a version that satisfies the requirement jpype (from versions: ) No matching distribution found for jpype"
    - 적합한 jpype가 없다는 것이겠죠..
        - 돌이켜보니, 여기서 만약 아래 설치파일을 가져와서 다운 받는 것이 아니라, conda에 설치되어 있는 jpype를 설치했으면 어땠을까? 하는 생각이 들지만, 안되었을 겁니다. 저는 안되는 놈이에요. 
            - 혹시나 싶어서. `conda install -c conda-forge jpype1`

- pip로 되지 않아서, 설치파일을 가져와서 다운 받았습니다. 
    - https://pypi.python.org/pypi/JPype1 에서 파일을 다운 받는다. 
    - 다운받은 파일이 tar.gz 파일인데, 압축을 풀기 위해 터미널에서 다운 파일이 있는 폴더로 이동한 다음, `tar -zxvf filename` 을 입력한다. 
    - 그 다음, 해당 압축이 풀린 폴더로 가서, `python setup.py build`를 해준다.


```python
import konlpy
```


    ---------------------------------------------------------------------------

    ModuleNotFoundError                       Traceback (most recent call last)

    <ipython-input-5-32cb478bd821> in <module>()
    ----> 1 import konlpy
    

    ~/anaconda3/lib/python3.6/site-packages/konlpy/__init__.py in <module>()
         13 from . import data
         14 from . import internals
    ---> 15 from . import tag
    

    ~/anaconda3/lib/python3.6/site-packages/konlpy/tag/__init__.py in <module>()
          2 import warnings
          3 
    ----> 4 from ._hannanum import Hannanum
          5 from ._kkma import Kkma
          6 from ._komoran import Komoran


    ~/anaconda3/lib/python3.6/site-packages/konlpy/tag/_hannanum.py in <module>()
          5 import re
          6 
    ----> 7 import jpype
          8 
          9 from .. import jvm


    ModuleNotFoundError: No module named 'jpype'


- 다 했지만, 여전히 안된다. 여전히 `jpype`가 없다고 한다. 
    - warning 이 많아서 꼼꼼하게 보지는 못했는데, 해당 수업에서 한 것처럼 c++과 관계된 건 아닌것 같았고, 그래서 java를 전체를 다시 설치해보기로 한다. 

- jdk 를 다시 설치한다.
    - 현재 설치된 jdk 버전 확인 by `java version`
        `
        java version "1.8.0_144"
        Java(TM) SE Runtime Environment (build 1.8.0_144-b01)
        Java HotSpot(TM) 64-Bit Server VM (build 25.144-b01, mixed mode)
        `
    - `Library/Java/JavaVirtualMachines`에 jdk 파일이 있다. 
    - sudo rm -rf filname.jdk
        - https://docs.oracle.com/javase/8/docs/technotes/guides/install/mac_jdk.html#A1096903
- 이제 적합한 jdk 파일을 다시 설치해보도록 하자. 
    - 성공한 버전이 1.8.0_151 이라고 하길래 해당 버전을 설치하기로 한다. 
    - 해당 버전을 구할 수 없어서...그냥 다른 버전으로 다시 설치한다. 
    - 그래서 아직도 안된다 흠...


```python
from konlpy.tag import Kkma
```


    ---------------------------------------------------------------------------

    ModuleNotFoundError                       Traceback (most recent call last)

    <ipython-input-12-7aaa57e14720> in <module>()
    ----> 1 from konlpy.tag import Kkma
    

    ~/anaconda3/lib/python3.6/site-packages/konlpy/__init__.py in <module>()
         13 from . import data
         14 from . import internals
    ---> 15 from . import tag
    

    ~/anaconda3/lib/python3.6/site-packages/konlpy/tag/__init__.py in <module>()
          2 import warnings
          3 
    ----> 4 from ._hannanum import Hannanum
          5 from ._kkma import Kkma
          6 from ._komoran import Komoran


    ~/anaconda3/lib/python3.6/site-packages/konlpy/tag/_hannanum.py in <module>()
          5 import re
          6 
    ----> 7 import jpype
          8 
          9 from .. import jvm


    ModuleNotFoundError: No module named 'jpype'


- 짜증이 나지만, 좀 더 해보자. 
    - 정리를 해보면, konlpy는 jpype에 대한 디펜던시가 있다. 적합한 놈을 못찾고 있음. 
        - 이 때, jpype는 또 java에 대한 디펜던시가 있기 때문에 경우에 따라서 java도 다시 설치해줘야 하는 일들이 발생하고는 함.
    - setup.py로부터 설치를 했으나 잘 되지 않아서, pip로 다시 설치했으나 다음과 같은 에러메시지가 발생함
        - Command "python setup.py egg_info" failed with error code 1 in /private/tmp/pip-build-_pssfaui/JPype1-py3/
    - 그냥 `conda install -c conda-forge jpype1` 로 설치를 했음. 
        - http://jpype.readthedocs.io/en/latest/install.html
- 그러니까 이제 jpype 는 import 하는데 문제가 없음. 


```python
import jpype
```


```python
import konlpy # 오 이제 둘다 된다. 
```


```python
from konlpy.tag import Kkma
from konlpy.utils import pprint
kkma = Kkma()

print(kkma.sentences("JPype 설치 너무 까다로워요"))
# 그러나, 여전히 잘 되지 않는 것을 알 수 있습니다. 
```

- NameError: name 'jpype' is not defined

- python에서 설치한 라이브러리는 문제없는데, 이렇게 에러메시지가 뜨는 것을 보면, 이 경우는 java에 문제가 있었을 가능성이 있다. 

- java를 다시 설치하고 별일을 다 했지만, 잘 되지 않는다. 여기까지 하고 포기하기로 한다. 할 수가 없다. 
