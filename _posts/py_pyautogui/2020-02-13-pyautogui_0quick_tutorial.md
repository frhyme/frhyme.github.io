---
title: PyAutomation - pyautogui - install.
category: python-libs
tags: python python-libs automation pyautogui
---

## 2-line summary 

- macOS에서 pyautogui를 설치하고 간단한 테스트를 실행해봄. 
- AI가 내 마우스와 키보드를 건드린다는 게 무서운데(만약, 프로그램이 멈추지 않을 수도 있으니까), 마우스를 스크린 4 꼭지점에 가져가면, 알아서 Exception을 발생시키고 멈춰줌

## intro: Difference with Selenium 

- 요즘 웹서핑을 하다보면, 꽤 자주 "python을 이용한 자동화"라는 말이 나오길래, 무엇인지 궁금해서 찾아보니, 보통 `pyautogui`라는 라이브러리를 사용하더군요. 이전에 저는 웹자동화 느낌으로 `selenium`을 사용해본 적은 있는데, `pyautogui`도 비슷하지 않을까 싶었지만, 접근 방식이 아예 다르더군요. 
- `selenium`의 경우는 웹의 소스들을 가져와서, 소스의 정보를 바꾸는 식으로 자동화를 처리합니다. 즉, 웹브라우저에서의 통신을 자동화하는 셈이죠. 
- 이와 다르게, `pyautogui`는 마우스와 키보드를 조작하면서, 즉, 마우스를 어디에 누를지, 키보드를 어디에 누를지, 조작할 수 있습니다. 어떤 의미로는, 훨씬 편한 부분이 있는 셈이죠. 
- 다만 "text"로 통신하는 것이 아니라, 마우스와 키보드로 통신하고, 스크린샷을 찍어서 스크린샷의 이미지 인식을 통해서 처리하므로, 정확도에서 차이가 발생할 수 있다, 정도가 다르죠.

## What is PyAutoGUI? 

- [PyAutoGUI Documentation](https://pyautogui.readthedocs.io/en/latest/)에 정리된 내용을 보면 다음과 같습니다. 
    - PyAutoGUI는 python을 활용하여, 키보드와 마우스를 조절하여, 다른 어플리케이션들과의 상호작용을 자동화해준다. 
    - Windows, macOS, Linux에서 모두 운영되며, python2, 3모두 문제없다.
    - 마우스와 키보드 조작,  스크린샷, 스크린에서 이미지 찾기, 메세지 박사 띄우기, 등등이 있는데 이외에도 많은 것들이 있다.

### What if out-of-control?

- 이렇게 쓰고 나면, 조금 무섭게 느껴질 수도 있습니다. "이거 뭐 거의 스카이네처럼 잘못 돌아가면 어떻게 하나?"라는 생각이 들 수 있으니까요. 가령, 제가 실수로 무한루프를 만들어둬서, 마우스와 키보드가 멈추지 않는다면 어떻게 해야 하나? 라는 생각이 들 수 있죠. 
- 따라서, `pyautogui`를 통해 프로그램이 구현될 때, 마우스를 모니터의 4 꼭지점 중 하나에 가져가면, `pyautogui.FailSafeException`이 발현되어, 프로그램이 강제종료됩니다. 또한, 모든 pyautogui function 사이에는 약간의 delay가 존재하므로, 프로그램 구동 중에도, Exception을 발생시키는 것이 가능하죠.

### install it and simple run it.

- 간단하게 다음과 같이 설치하고, 버전을 확인해봅니다.

```
>>> pip install pyautogui
>>> pip show pyautogui
```

- 제가 설치한 `pyautogui`의 버전은 다음과 같습니다. 

```shell 

Name: PyAutoGUI
Version: 0.9.48
Summary: PyAutoGUI lets Python control the mouse and keyboard, and other GUI automation tasks. For Windows, macOS, and Linux, on Python 3 and 2.
Home-page: https://github.com/asweigart/pyautogui
Author: Al Sweigart
Author-email: al@inventwithpython.com
License: BSD
Location: /Users/frhyme/anaconda3/lib/python3.6/site-packages
Requires: pymsgbox, mouseinfo, pygetwindow, PyTweening, pyobjc, pyscreeze, pyobjc-core
Required-by:
```

### Simple tutorial 

- 그냥, 매우 간단하게, 현재 mouse 위치를 인식하고, 마우스 위치를 1초에 한번씩 움직이는 코드를 만들었습니다.

```python
import pyautogui
import time

"""
- 그냥 pyautogui를 이용해서 mouse를 현재 마우스에서 1초마다 조금씩 왼쪽, 위로 옮기는 코드.
- 왼쪽 위가 (0, 0)
"""

print("--" * 30)
# Get the size of the primary monitor.
screenWidth, screenHeight = pyautogui.size()
print(f"screenWidth, screenHeight")
print(screenWidth, screenHeight)
print("--"*30)

# Get the XY position of the mouse.
currentMouseX, currentMouseY = pyautogui.position()
print(f"currentMouseX, currentMouseY")
print(currentMouseX, currentMouseY)
print("--" * 30)

for i in range(0, 20):
    time.sleep(1) # Delay a second.
    currentMouseX -= 100
    currentMouseY -= 100
    pyautogui.moveTo(currentMouseX, currentMouseY)
print("--" * 30)
```

- 아래는 보시면, 코드가 실행중에, Exception이 발생한 것을 알 수 있습니다. 이는 제가 프로그램을 강제 종료하기 위해서, 중간에, 마우스를 모서리에 가져가서 그런 것이죠.

```
------------------------------------------------------------
screenWidth, screenHeight
1440 900
------------------------------------------------------------
currentMouseX, currentMouseY
990 343
------------------------------------------------------------
Traceback (most recent call last):
  File "!pyautogui_1.py", line 26, in <module>
    pyautogui.moveTo(currentMouseX, currentMouseY)
  File "/Users/frhyme/anaconda3/lib/python3.6/site-packages/pyautogui/__init__.py", line 831, in moveTo
    failSafeCheck()
  File "/Users/frhyme/anaconda3/lib/python3.6/site-packages/pyautogui/__init__.py", line 1257, in failSafeCheck
    raise FailSafeException('PyAutoGUI fail-safe triggered from mouse moving to a corner of the screen. To disable this fail-safe, set pyautogui.FAILSAFE to False. DISABLING FAIL-SAFE IS NOT RECOMMENDED.')
pyautogui.FailSafeException: PyAutoGUI fail-safe triggered from mouse moving to a corner of the screen. To disable this fail-safe, set pyautogui.FAILSAFE to False. DISABLING FAIL-SAFE IS NOT RECOMMENDED.
```

## wrap-up

- 다음에는, 각 부분별로 좀 더 자세하게 정리해보겠습니다.


## reference

- [pyautogui - documentation](https://pyautogui.readthedocs.io/en/latest/)