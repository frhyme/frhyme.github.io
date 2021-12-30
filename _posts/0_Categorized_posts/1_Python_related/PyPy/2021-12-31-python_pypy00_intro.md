---
title: pypy00 - Install PyPy
category: pypy
tags: pypy compiler python programming RPython macOS
---

## pypy00 - Before Install PyPy

- 우리가 일반적으로 윈도우에서 사용하고 있는 python은 사실상 CPython입니다. 우리는 python 명령어 등으로 프로그래밍을 한다고 생각하지만, 그 뒷단에서는 각 python 명령어를 C로 변환하여 혹은 해당 python code에 대한 해석이 C code로 진행된다는 이야기입니다. Cython이 아니라, Cpython입니다.
- 같은 방식으로 python 명령어를 다른 프로그램이 대신해주는 것도 가능하겠죠. Java가 대신 처리해줘서 JVM 위에서 구현되도록 만들어진 형태가 바로 Jython, .NET Framework를 사용하여 만들어진 경우가 바로 IronPython 등으로 불립니다. 이렇게 말하고 나면 마치 python은 그냥 일종의 interface 언어라거나, lua처럼 script 언어처럼 보이는데요, 뭐 일단은 그렇게 생각하셔도 문제가 없다고 생각됩니다.

### What is PyPy?

- 여기서 흥미롭게도, python으로 만들어진 Code를 python으로 해석하는 프로젝트가 있습니다. 일명 [PyPy](https://en.wikipedia.org/wiki/PyPy)라는 프로젝트인데요. python code을 해석하는 python 프로그램, 이라고 해석하면 됩니다. 무슨 말인가? 싶죠. 저도 그렇습니다. 
- [namu.wiki - PyPy](https://namu.wiki/w/PyPy)에 따르면, PyPy는 다음의 과정으로 만들어졌다고 합니다.

1. 먼저 RPython이라고 하는, 파이썬 문법을 엄격하게 만들어 컴파일이 되게 만든 해석기(translate.py)를 Python 코드로 작성한다.
    - RPython은 "Restricted Python"을 의미합니다. 정적 컴파일이 되도록 dynamically typing이 제한된 python이라는 의미인데요, 일단은 그냥 "기능이 제한된 python 언어"라고 이해해도 큰 문제가 없습니다.
2. RPython의 효과적인 컴파일을 위해 다른 언어로 툴체인을 만든다.
    - RPython을 다른 저급언어(C, Java, ByteCode) 등으로 변환해줄 수 있는 해석기를 만듭니다. 이 단계에서는 python이 아닌 다른 언어가 사용될 수 있죠.
    - 만약 이 때 사용되는 중간언어가 C 라면, RPython으로부터 변환된 C code를 실행해 줄 수 있는, gcc와 같은 compiler 필요합니다.
3. Python 구현(런타임)를 RPython 문법으로 작성한다.
    - 여기서 "Python 구현"은 CPython, Jython처럼, Python을 실행할 수 있는 Interpreter를 말합니다.
    - Python Code를 "Python 구현"에 넘겨주면 Python code가 실행되는 것이죠.
4. 3에서 만든 구현을 1 또는 2에서 만든 RPython 해석기로 컴파일한다.
5. 4으로 만든 후보를 이전 또는 다른 구현과 비교(성능 측정), 만족스럽지 않으면 수정한다.(nightly builds)
6. 5에서 만족스러운 결과를 냈다면 출시하고 1 또는 2부터 다시 시작한다.(release)

- 무슨 말인가 싶죠? 정상입니다.
- 사용자 입장에서 본다면, 내가 쓴 Python Code(A)는 "RPython으로 구현된 구현체(B)"에 의해 돌아가고, B는 "다른언어(C, Java)로 변환될 수 있는 해석기(C)"에 의해 다른 언어로 변환되거나, "RPython을 해석할 수 있는 Python code(D)"에 의해서 돌아가게 됩니다. B를 C, D로 컴파일해서 돌려봤을 때, 얘가 충분히 괜찮은 성능을 보여준다면, B가 잘 구현된 것이겠죠. 즉, Python을 RPython으로 잘 변환하여, 코드가 잘 돌아가도록 하는 구현체가 개발된 것이기 때문에, 성공적이다, 라고 결론을 내리고 다시 시작하게 됩니다
- 결국 중요한 포인트는 B 입니다. 우리는 python을 돌려주는 (RPython으로 구현된) Interpreter에 관심이 있는 것이고, 얘를 잘 만든 다음 이 인터프리터가 실제로 속력이 빨라지도록 만드는 것이 중요 관심사라는 얘기죠.
- 이때, pypy에서는 자주 쓰이는 코드를 캐싱하여, 효율적으로 코드가 수행될 수 있도록 처리해주어, 전체 코드의 속도를 향상시켰다는 얘기죠.
- 뭔가, 이해한 것 같지만 조금 더 보면 이상한 부분이 있을 것 같습니다. 일단은 여기까지만 하고 넘어가도록 할거에요.

## Install PyPy

- 이제 PyPy를 설치해보도록 합니다.
- 저는 macOS에 설치하므로, `brew`를 이용해서 설치해보기로 합니다.
- `brew search pypy`를 실행해 보면 "pypy"와 "pypy3"가 나오는 것을 알 수 있습니다. python2와 python3가 구분되어 있어서 그런것인데요, 둘다 설치해주기로 합니다
- 마지막 즈음에, pypy에 python lib를 설치하고 싶으면 어떻게 해야 하는지도 설명이 되어 있네요.

```bash
$ brew search pypy
==> Formulae
pypy                                                                                                   pypy3
$ brew install pypy
$ brew install pypy3
...
If you install Python packages via "pypy setup.py install", easy_install_pypy,
or pip_pypy, any provided scripts will go into the install-scripts folder
above, so you may want to add it to your PATH *after* /usr/local/bin
so you don't overwrite tools from CPython.

Setuptools and pip have been installed, so you can use easy_install_pypy and
pip_pypy.
To update setuptools and pip between pypy releases, run:
    pip_pypy install --upgrade pip setuptools
```

- python, pypy2, pypy3의 버전을 비교해보면 다음과 같습니다.
- Anaconda를 사용해서 설치한 Python의 경우는 CPython으로 C로 변환된 다음 Clang에 의해 수행는 반면, 다른 아이들은 PyPy 인터프리터를 사용해 RPython으로 변환된 다음, LLVM 을 사용해서 처리된다, 라고 보시면 될 것 같습니다.

```bash
# pypy
Python 2.7.18 (b89256933b0b12169977295224730039a58a1815, Oct 25 2021, 16:28:36)
[PyPy 7.3.6 with GCC Apple LLVM 13.0.0 (clang-1300.0.29.3)] on darwin
# pypy3 
Python 3.7.12 (44db26267d0a38e51a7e8490983ed7e7bcb84b74, Oct 28 2021, 14:16:15)
[PyPy 7.3.7 with GCC Apple LLVM 13.0.0 (clang-1300.0.29.3)] on darwin
# python
Python 3.7.6 (default, Jan  8 2020, 13:42:34) 
[Clang 4.0.1 (tags/RELEASE_401/final)] :: Anaconda, Inc. on darwin
```

## Compare Performance

- 다음과 같은 간단한 코드를 만들어서 테스트 해봅니다.

```python
import time

start_time = time.time()

s = 0
N = 1000000
for i in range(0, N):
    s += i

end_time = time.time()

print(f"time_duration: {end_time - start_time}")
```

- 비교해 보면 pypy의 경우가 훨씬 빠르다는 것을 알 수 있죠.

```python
$ python test_code_for_pypy_python.py
time_duration: 0.1011807918548584
$ pypy3 test_code_for_pypy_python.py
time_duration: 0.004225969314575195
```

## wrap-up

- 물론, 이렇게 정리하고 나면 pypy가 python보다 훨씬 좋은것 아닌가? 싶지만, 아직 pypy에서는 실행되지 않는 python library들도 있습니다. 간단한 코드의 경우, 그리고 본인이 python native하게 code를 작성했다면, python보다는 pypy를 사용하는 것이 더 효율적일 수 있따, 정도의 이야기는 할 수 있겠네요.

## Reference

- [wikipedia - PyPy](https://en.wikipedia.org/wiki/PyPy)
- [wikipedia - ko - RPython](https://ko.wikipedia.org/wiki/RPython)
- [알파희 - PyPy/RPython으로 20배 빨라지는 아희 JIT 인터프리터](https://www.slideshare.net/YunWonJeong/pypyrpython-20-jit)
