---
title: python - auto formatter - autopep8, yapf
category: python-libs
tags: python python-libs formatter autopep8 pep8 yapf 
---

## PROBLEM: autopep8 not install

- 저는 vscode를 주 IDE로 쓰고 있습니다. 특별한 이유는 없고요 그냥 쓰다보니 쓰고있네요. 
- 아무튼, python을 주로 쓰고 있는데, python을 확장 프로그램으로 설치를 해야, 각 클래스들의 주요 method들을 preview해주는 기능이 지원되는 것 같아요. 모든 함수를 다 정확하게 외우고 있지는 못하니까, 이 기능이 없으면 코딩을 하기가 매우 어려워지거든요. 
- 여기까지는 좋은데, python을 확장프로그램으로 설치하고 나면, 다음의 메세지가 반복으로 뜹니다. `autopep8`을 직접 설치한 적은 없는데, 아마 python을 설치할 때 자동으로 설치되는 것이 아닐까 싶습니다. 

```plaintext
Formatter autopep8 is not installed.
```

- autopep8이 문제가 있나 싶어서, yapf를 설치해도 같은 결과가 나옵니다.

```plaintext
Formatter yapf is not installed.
```

- 왜 이런 일이 발생하는 것인지, 그 이유를 알기 위해서 천천히 공부해봅니다.

## What is YAPF?

- 우선 [yapf](https://github.com/google/yapf)가 무엇인지를 정리해봅니다. 해당 링크에 작성된 내용에 따르면, 현재 python formatter들인 autopep8이나, pep9ify의 경우 PEP에 따라서, 코드를 코드에 대한 가이드라인을 주는데, 이게 반드시 코드를 더 예쁘게 만드는 것만은 아니다.
- yapf는 약간 다르게, Daniel Jasper가 개발한 `clang-format`에 기반한다. 즉, "기존 코드가 스타일 가이드를 위반하지 않았더라도, 스타일 가이드에 가장 유사한 방식으로 코드를 수정한다"라는 이야기죠. 
- 이러한 아이디어는 Go programming language의 `gofmt`과 유사합니다.

## What is autopep8

- [autopep8](https://github.com/hhatto/autopep8) 또한 비슷한데, 유사하며, PEP8 style guide에 맞도록 자동으로 코드를 수정합니다.

## SOLUTION

- 뭐, 그래서, 저는 `yapf`를 설치해보기로 합니다. 뭘 써도 상관없기는 해요.
- 그냥 `pip`로 설치합니다. 

```plaintext
pip install yapf
```

- 그리고, 커맨드라인에서 다음처럼 `yapf aaa.py`를 치면, 해당 파이썬 파일에서 무엇을 고치면 되는지 말해줍니다.

## wrap-up

- 여담이지만, `yapf`에서 제공하는 방식이 미묘하게 마음에 들지 않아서, 지우고 `autopep8`을 설치해보기도 했습니다. 그러나, `autopep8`도 딱히 `yapf`와 큰 차이가 있지는 않더군요. 그래서 다시 `yapf`로 돌아왔습니다. 
- 다만, `pip install autopep8`이후 커맨드라인에서 각 파일별로 pep8을 어떻게 위배하는지 확인할 수 있다고 하는데, 다음과 같은 에러코드가 뜨고 더 진행되지 않았습니다. 

```plaintext
Traceback (most recent call last):
  File "/Users/frhyme/anaconda3/bin/autopep8", line 6, in <module>
    from autopep8 import main
  File "/Users/frhyme/anaconda3/lib/python3.6/site-packages/autopep8.py", line 61, in <module>
    import pycodestyle
ModuleNotFoundError: No module named 'pycodestyle'
```

- 이는 아마도 제가 `autopep8`을 pip로 설치했기 때문에, 서로 인식하지 못해서 발생한 것으로 보입니다.
- 따라서, `pycodestyle`을 다시 설치해주고 나니, 별 문제없이 진행되는 군요.

```plaintext
conda install pycodestyle
```

- 하여간 python 내에서 이런 library의 version으로 발생하는 문제는 매우 성가신데도, 아직도 그대로 인것 같아요.
