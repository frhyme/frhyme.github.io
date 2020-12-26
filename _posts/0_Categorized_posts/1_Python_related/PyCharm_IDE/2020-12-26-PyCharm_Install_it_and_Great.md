---
title: PyCharm - Install PyCharm
category: python
tags: python PyCharm IDE 
---

## PyCharm - Why Install PyCharm

- 기존에는 VScode를 사용해서 python 개발을 진행했습니다. 사실 그동안 큰 불편함없이 개발을 해오기는 했는데요, 굳이 PyCharm을 설치하기로 한 이유는 대략 다음과 같습니다.
  - Java 개발을 위해서 IntelliJ를 사용해봤는데, IDE가 매우 깔끔하고 자잘한 불편함들을 해결해줬습니다. 따라서 JetBrain의 제품들에 대한 호감도가 대폭 상승했구요.
  - 개발을 하면서 발생하는 이슈들과 LessonLearned들을 블로그에 올리기 위해서 VScode를 항상 실행해 둡니다. 그런데, python으로 코딩할 때가 되면 켜져 있는 VScode 창 두 개 중에서 어느 것이 블로그용이고, python 용인지 구별이 헷갈릴 때가 있더라구요.
- 따라서, VScode는 앞으로 텍스트 에디터로 고정을 하고, python은 PyCharm을 사용해서 개발하려고 합니다.

## Install PyCharm

- [JetBrains - PyCharm](https://www.jetbrains.com/ko-kr/pycharm/download/)에서 다운받아서 설치합니다. 설치 자체는 어려운 게 없죠.
- 새로운 프로젝트를 실행하게 되면, `Add Python Interprete`라는 메뉴가 뜨게 됩니다. 즉, "당신 프로젝트에서 사용할 python 버전이 무엇이냐?"라는 것이죠.
- 저는 Conda - python 3.8을 선택했습니다. 그리고 실행하게 되면, 해당 프로젝트는 `Conda python 3.8`에 맞는 독립적인 환경이 갖추어지게 되죠. 
- PyCharm 내에서 Terminal을 실행해 보면, 다음처럼 되어 있는 것을 알 수 있습니다. 이 앞에 `(pythonProject)`가 바로 현재 프로젝트에 맞는 가상 환경이 구축되었다는 말이죠.

```plaintext
(pythonProject) seunghoonlee@seunghoonui-MacBookAir pythonProject % 
```

- 아, 저는 이걸 딱 보고, 아 존나 잘 설치했다 라는 생각을 했습니다. 사실 파이썬에서 각 프로젝트 별로 필요로 하는 라이브러리들이 다름에도 불구하고, 귀찮기 때문에 그냥 항상 Global로 설치해버리거든요. 버전을 업데이트할 때도 그냥 Global로 처리해버리는데, 이럴 경우 "과거에는 되던 코드가 안되는 경우"들이 매우 많이 존재합니다. 물론, 그냥 제가 귀찮아서 저지른 일이기는 하지만요.
- 이를 방지하기 위해서 `virtualenv`라거나, `pipenv` 또 `Conda`에서도 지원하는데, 존나 귀찮아서 사실 사용하지 않았습니다. 
- 어우 그런데, PyCharm은 프로젝트단위로 가상환경을 구축해주네요. 이거 존나 편한겁니다. 존나 찬양해요.
- 그리고 코드를 실행하려면 `Ctrl + R` 누르면 됩니다.

## Wrap-up

- 원래는 VScode에서 모든 코딩을 다 하려고 했는데, 이제 다 구분해서 쓰기로 했습니다. 
  - Python: PyCharm
  - Java: IntelliJ
  - R: Rstudio
  - Markdown: VScode
  - C: CLion을 쓰고 싶은데...유료라서 일단은 VScode로 사용합니다...

## Reference

- [JetBrains - PyCharm](https://www.jetbrains.com/ko-kr/pycharm/download/)
