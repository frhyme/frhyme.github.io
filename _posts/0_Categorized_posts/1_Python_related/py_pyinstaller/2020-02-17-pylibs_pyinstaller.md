---
title: PyInstaller - python code 실행 파일 만들기. 
category: python-libs
tags: python python-libs pyinstaller MacOS
---

## 3-line summary 

- [pyinstaller](https://pyinstaller.readthedocs.io/en/stable/operating-mode.html)를 이용하면, 간단한 python 프로그램을 실행파일(exe)로 만들수 있습니다. 
- 하지만, 어떤 파이썬 라이브러리를 import하느냐에 따라서 만들어지는 속도, 용량 차이는 물론, 실패할 가능성도 있습니다(저는 `numpy`를 사용했는데 패키징에 실패했습니다)
- 또한, cross-compiler가 아니며, 맥에서 만든 프로그램은 맥에서만, 윈도우에서 만든 프로그램은 윈도우에서만 실행됩니다

## intro

- 최근에 [pyautogui](https://pyautogui.readthedocs.io/en/latest/)라는, python을 이용해서 mouse, keyboard들을 자동으로 조작하는 automation 등을 정리하였습니다. 그런데, 이걸 알게 되고 나니, 이를 이용해서 프로그램 파일을 만들면 더 편할 것 같다는 생각이 드는 것이죠. 
- 그래서, 찾아보다가, [pyinstaller](https://pyinstaller.readthedocs.io/en/stable/operating-mode.html)라고 하는 python 코드를 프로그램 실행파일로 변환해주는 라이브러리를 찾았습니다. 
- 즉, 이 둘을 섞으면, 해당 컴퓨터에 파이썬 라이브러리들을 설치하지 않더라도, 실행파일만으로 쉽게 할 수 있지 않나? 하는 생각이 들더군요. 

## What is "Pyinstaller"

- [pyinstaller](https://pyinstaller.readthedocs.io/en/stable/operating-mode.html)는 python으로 작성된 코드와 그 코드가 참고하고 있는 다양한 라이브러리들을 하나의 패키지로 묶어 주는 파이썬 라이브러리입니다. 이렇게 실행파일을 만들고 나면, 다른 컴퓨터에 파이썬을 설치하지 않아도 그대로 실행할 수 있다는 장점이 있죠. 특히, 주요 라이브러리들인 `numpy`, `PyQt`, `Django` 등의 라이브러리에 대해서 잘 합쳐준다, 고 합니다만, 완벽하지는 않아요. 
- 저는 MacOS를 사용하고 있으며, `numpy`를 사용해서 간단하게 만들어준 프로그램이 마음처럼 작동하지는 않더군요.
- 이를 해결하기 위해서는 오히려 가상의 개발환경을 세팅하고, 각 폴더별로 필요한 라이브러리들을 묶어서 처리하는 것이 좋을 것 같습니다. 그중 하나로 `virenv`를 쓰거나, 혹은 docker 등을 쓰는 것도 대안이 될 수 있겠죠.
- 또한, cross-compiler가 아니므로, Windows에서 만든 파일을 윈도우에서만 돌아가고, 맥에서 만든 것은 맥에서만 돌아갑니다. 이 부분은 좀 크게 아쉽군요. 

## Simple program with `numpy`: failure

- `numpy` 라이브러리를 포함한 간단한 코드를 만들고, 이를 실행파일로 만들어봅시다.
- 일단 설치부터 합시다.

```plaintext
pip install pyinstaller
```

- 그리고, 아래처럼 간단한 코드를 만듭니다. 이 코드의 파일명은 `simple_program.py`입니다.

```python
import time
import numpy as np 

# 모든 코드는 아래 에 작성되어야 함.
if __name__ == "__main__" :
    print("Start")
    r = np.random.random(1)
    print(r)
    time.sleep(4)
    print(f"Complete")
```

- 그리고, `pyinstaller`를 이용해서 다음처럼 별개의 실행 파일로 만들어줍니다. 
  - `--onefile`는 "하나의 파일로 생성한다"는 것을 의미하는 parameter입니다. 

```plaintext
pyinstaller --onefile simple_program.py
```

- 이렇게 만들고 나면 `build`, `dist`라는 파일들이 생겨납니다. 다만, 시간이 오래 걸리고 용량 자체도 200메가가 나옵니다. 이는 제가 `numpy`라는 큰 라이브러리를 사용했기 때문이죠.

### ERROR: mkl-service failed to import 

- 그리고 실행을 해봤씁니다만, 다음과 같은 에러가 뜨는 것을 알 수 있습니다.

```plaintext
UserWarning: mkl-service package failed to import, therefore Intel(R) MKL initialization ensuring its correct out-of-the box operation under condition when Gnu OpenMP had already been loaded by Python process is not assured. Please install mkl-service package, see 
```

- 대충 해석을 해보자면, 다음과 같은데.
  - `mkl-service` 패키지를 임포트하는데 실패했다. 
  - 따라서, Gnu OpenMP가 이미 파이썬 프로세스에 의해 로드되었을 때, 올바른 작동을 보장해주는 Intel(R) MKL initialization 초기화가 보장되지 않습니다.
- 뭔 개소리인가 싶지만, 하나씩 살펴보자면, 
  - [`mkl-service`](https://github.com/IntelPython/mkl-service)는 "Python hooks for Intel(R) Math Kernel Library runtime control settings"라는데, Intel의 CPU에 적재된 math 관련 라이브러리들을 사용하기 위해서 필요한 것이 아닐까 싶습니다. 
  - 그리고, [OpenMP](https://ko.wikipedia.org/wiki/OpenMP)는 "공유 메모리 다중 처리 프로그램 API"입니다. 즉, 메모리에서 병렬처리를 하기 위해서 사용하는 인터페이스인데, 이는 보통 C/C++로 구현되죠. 
- 결론적으로, "C/C++로 메모리에 병렬처리를 하기 위해 OpenMP를 사용했는데, 이 때 interl memory 상에서 메모리를 사용하기 위한 방법과 연결이 안되었다"라는 말인데, 이는 다시 `numpy`를 패키지화하는 과정에서 문제가 생겼다는 것을 의미합니다. `numpy`는 C로 구현되었고, 이 때 메모리에 대해서 병렬처리를 하기 때문인 것이죠.

### Try to solve the error but failed

- 따라서, 일단은 mkl-service라는 패키지를 설치해봅니다. 그리고 다시 패키지를 만들어봤으나, 여전히 되지 않습니다.

```plaintext
conda install -c intel mkl-service
pyinstaller --onefile simple_program.py
```

- 즉, 이는 결국 모두 `numpy`를 패키지 내로 가져오는데 실패한 것이죠. 

## Simple program with only `python`: success 

- 따라서, `numpy`를 버리고, 매우 가벼운 코드를 만들어봅니다. 코드는 아래와 같습니다.

```python
import time

if __name__ == "__main__" :
    print("Start")
    time.sleep(4)
    print(f"Complete")
```

- 그리고 아래와 같이 커맨드를 실행해주면, 이전보다 훨씬 빠르고 가벼운 프로그램이 만들어집니다. 실행해봐도 에러없이 잘 실행되죠.

```plaintext
pyinstall --onefile simple_program.py
```

## wrap-up

- 앞서 보신 것처럼, 어떤 라이브러리를 어떤 버전으로 사용하느냐에 따라서 패키지화를 하는데 실패할 수 있습니다. 이건 사실 매번 일관적인 개발환경을 유지하는 것이 필요한데, 보통의 혼자 공부하는 사람들은 번거롭다는 이유로 이를 매우 게을리하죠. "아나콘다", "virenv", "docker"까지 이미 선택할 수 있는 다양한 툴이 있습니다. 앞으로는 가능하다면, 각 개발환경을 독립적으로 세팅하여 진행하는 것이 좋을 수 있습니다. 
- 오늘은 pyinstaller를 매우 간단하게나마 설치하고 실행파일로 만들어봤습니다. 여기서 제가 배운 것은 아주 얕게나마, "프로그램을 패키지로 만들어 배포한다는 것이 무엇인지" 이해하게 된 것이죠. 저는 이 감을 잡는 다는 것이 파이썬이 많은 대중들에게 주는 큰 힘이라고 생각합니다. 모든 것을 "블랙박스"화시키고, 매우 간단한 인터페이스로 한번 테스트하게 하는 것, 그렇게 큰 그림을 한번 보고 나면, 작은 그림들로 쪼개 보는 것이 쉬우니까요.

## reference

- [pyinstaller](https://pyinstaller.readthedocs.io/en/stable/operating-mode.html)
- [파이썬 실행파일 만들기(pyinstaller)](https://m.blog.naver.com/jwyoon25/221322775767)
- [OpenMP](https://ko.wikipedia.org/wiki/OpenMP)
