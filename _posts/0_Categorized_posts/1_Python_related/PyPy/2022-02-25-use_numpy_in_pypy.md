---
title: pypy에서 numpy 설치 및 사용하기
category: pypy
tags: pypy compiler python programming RPython macOS
---

## pypy에서 numpy 설치 및 사용하기

- python으로 개발하고 `python3`로 돌리는데 속도가 너무 느리더군요. 그래서 `pypy3`를 사용해서 돌리려고 보니, 다음과 같은 오류와 함께 돌아가지 않았습니다.
- python에는 `numpy`가 설치되어 있지만, pypy에는 `numpy`가 설치되어 있지 않기 때문이죠.

```plaintext
Traceback (most recent call last):
  File "a.py", line 1, in <module>
    import numpy as np
ImportError: No module named numpy
```

- [pypy에서 pip 설치하기](https://wikidocs.net/13979)를 확인해보니, pypy에서 `numpy`를 설치하려면 따로, pypy에서 pip를 사용해야 하는 것으로 보입니다.

```sh
$ pypy3 get-pip.py
$ pypy3 -m pip install numpy
```

## back to Pip

- pip는 "Pip Install Packages"의 약자로 파이썬 package 관리자를 의미합니다. 
- pip는 보통 python을 설치하면 자동으로 깔려 있는데요, 만약 설치되어 있지 않다면, 아래를 사용해서 설치하면 됩니다. 
- curl은 커맨드라인에서 사용하는 통신 툴로서, URL에 있는 소스를 그대로 가져오기 위해 사용합니다. 즉, 아래 경로의 파일을 그대로 가져와서 python에서 실행해주는 역할을 담당하죠.

```bash
$ curl https://bootstrap.pypa.io/get-pip.py | pypy3
```

- 뭐...그냥 저걸 그대로 사용하면 될텐데, 한번 해당 python 파일을 까보기로 합니다.

### get-pip

- 내부 코드 자체는 별로 길지 않고, binary data 나열되어 있는 것이 보입니다. binary data만 약 3만 줄이 넘네요. 의심스럽지만, comment를 확인해 보면 그냥 pip 를 압축하여 encoding한 것으로 보입니다.
- 내부 코드를 대략 보면 다음처럼 흘러가는데요.
  1. 임시 파일을 만들어서, binary data를 써주고, 
  2. 해당 파일을 다른 python에서도 사용할 수 있도록 `sys.path.insert`를 진행해 주고,
  3. 만들어진 pip code를 현재 local에 설치된 python환경에 맞도록 bootstrapping하고,
  4. 임시 파일을 삭제한다.
- 중간에 갑자기 "bootstrap"이라는 말이 들어가서 무슨 말인가 할 수 있는데요. [wikipedia - Bootstrapping](https://en.wikipedia.org/wiki/Bootstrapping)을 참조해보면, "컴퓨터 프로그램을 설치하는 중에, installer, package manager 자체를 업데이트한 다음 real installation을 시작하는 것"을 의미하는 것으로 보입니다.
- bootstrap은 boot + strap을 합친 말로, 부츠 뒤에 붙어 있는 작은 고리를 의미합니다. 이 고리를 사용하면 부츠를 벗기가 편하죠. 이처럼 "스스로 알아서 해결하는 무언가"를 의미하기 위해 다양한 곳에서 사용됩니다. 즉, 여기서 말하는 bootstrap도 "필요하면 알아서 updater를 업데이트하고 설치를 끝내는 일련의 과정"을 의미한다, 라고 생각하셔도 됩니다. 오히려, 이제는 너무 단어가 남용되는 느낌이 있어서 좀 지양해야 하지 않나 싶기도 하고요.
- 어쨋거나, 다음 명령어를 사용해서 pypy3에서도 pip를 사용할 수 있도록 해줍니다.

```bash
$ curl https://bootstrap.pypa.io/get-pip.py | pypy3
```

### pip with pypy3

- pypy3에서 pip를 사용하기 위해서는 다음 command를 실행해 줘야 합니다. pip가 자동으로 등록되어 있는 형태가 아닌 것인지, `pypy3`로 pip를 실행시키고, 그 다음 numpy를 설치하는 것처럼 보이네요.
  - `-m`: 주어진 모듈(ex: 'pip')을 시스템 경로에서 검색한 다음, 해당 모듈을 사용합니다.
- 그리고, 설치가 잘 되었는지 확인해봅니다. mac 기준으로는 `/usr/local/Cellar/pypy3/7.3.7/libexec/site-packages` 경로 내에 numpy가 설치된 것으로 보이네요.
- python관련 패키지들이 어디에 설치되었는지 확인하려면, `python -m site`를 사용하면 됩니다.

```sh
$ pypy3 -m pip install numpy
$ pypy3 -m pip list
```


## Use numpy on pypy3

- 그럼 numpy로 코드를 작성하고, pypy3로 돌려보겠습니다. code는 대강 다음과 같습니다. numpy를 쓰는 경우에는 `np.arange(0, n)`으로 변경되겠죠.

```python
import numpy as np
import time

n = 10**8
s = 0

start_time = time.time()
for i in range(0, n):
    s += i

print(s)
print(time.time() - start_time)

```
- 0 ~ 100000 아무튼 대충 큰수를 합하는데, 다음 4가지 경우로 나누어서 계산해봅니다.
  1. pure python with python3
  2. pure python with pypy3
  3. numpy with python3
  4. numpy with pypy3
- pure python을 pypy3로 실행했을 때의 속도가 다른 코드에 비해서월등히 빠릅니다.
- 굳이 pypy3에서 numpy를 가져와서 처리했을 때, 속도가 그냥 python에 비해서 월등이 느려지는 모습을 보이네요. 
- 물론, 사실 이 실험이 "numpy를 사용하는 것보다 pypy로 pure하게 짜는게 낫다"라는 것을 증명할수는 없습니다. 이 코드에서 사용한 numpy는 numpy의 장점을 살린 코드가 아니기 때문에, 별로 유의미하지 않죠. 그저, "pypy에 numpy를 가져와서 사용해야 할 때는 속도가 오히려 늦어질 수도 있으니 조심하자" 정도의 교훈은 준다고 할 수 있겠네요.

```sh
$ python3 a_pure_python.py                                                                                       
10.358957052230835
$ pypy3 a_pure_python.py                                                                                        
0.1467421054840088
$ python3 a_numpy.py                                                                                           
21.09306311607361
$ pypy3 a_numpy.py                                                                                            
88.31825709342957
```

## Wrap-up

- pypy에서 numpy를 사용하기 위해 pypy용 numpy를 설치하고, 간단한 코드를 사용해서 실험을 해봤으나, numpy를 사용하지 않고 않고 pure python과 pypy를 사용하는 경우에 속도가 더 빠를 수 있다, 정도의 교훈을 얻었습니다. 

## Reference

- [tutorialspoint - python bootstrapping the pip installer](https://www.tutorialspoint.com/python-bootstrapping-the-pip-installer)
- [wikidocs - pypy에서 pip 설치하기](https://wikidocs.net/13979)
- [wikipedia - boostrapping](https://en.wikipedia.org/wiki/Bootstrapping#Software_loading_and_execution)
- [python - cmdline](https://docs.python.org/ko/3/using/cmdline.html)
