---
title: PyAutomation - pyautogui - Mouse Control.
category: python-libs
tags: python python-libs automation pyautogui
---

## 1-line summary 

- [pyautogui](https://pyautogui.readthedocs.io/en/latest/mouse.html)를 이용하면, 마우스 위치 이동, 클릭, 스크롤, 드래그 등을 처리할 수 있음. 

## Cheat sheet for pyautogui - mouse

- `pyautogui`를 이용한, 마우스 동작을 아래 코드로 정리하였습니다.

```python
import pyautogui

#-------------------------------------------------------
# pyautogui.size():
# 현재 screen의 전체 너비와 높이를 각각 리턴함.
screenWidth, screenHeight = pyautogui.size()
#-------------------------------------------------------
# pyautogui.position()
# 현재 mouse의 position x,y를 리턴.
# 왼쪽 위를 (0, 0)으로 삼고 오른쪽, 아래로 갈 수록, 각각 +
currentMouseX, currentMouseY = pyautogui.position()
#-------------------------------------------------------
# pyautogui.moveTo(Absolute_X, Absolute_Y):
# mouse의 절대적 위치 이동, X, Y 좌표를 정확하게 넘겨야 함.
newMouseX = currentMouseX - 100
newMouseY = currentMouseY - 100
pyautogui.moveTo(newMouseX, newMouseY)
# None을 넘길 경우, 넘어간 좌표만 이동.
pyautogui.moveTo(None, newMouseY+100)
pyautogui.moveTo(newMouseX+100, None)
#-------------------------------------------------------
# pyautogui.move(delta_x, delta_y):
# mouse의 상대적 좌표 이동. 현재 위치에서 얼마나 이동할지
# 즉, delta_x, delta_y 를 넘긴다고 보면 됨.
pyautogui.move(0, 50)
#-------------------------------------------------------
# pyautogui.dragT(absolute_x, absolute_y, button=left):
# pyautogui.drag(delta_x, delta_y, button=left):
# 특정 좌표에서, 마우스를 누른 상태로 어떤 포지션까지 움직일때.
pyautogui.dragTo(0, 50, button=left)
pyautogui.drag(0, 50, button=left)
#-------------------------------------------------------
# pyautogui.click(button='right', clicks=3, interval=0.25):
# button: 'left', 'right', 'middle'
# clicks: 1, 2(double-click), 3
# interval: 매 클릭마다 시간 간격
# 3.0 초마다 왼쪽 마우스 버튼 더블클릭.
pyautogui.click(button='left', clicks=2, interval=3.0)
# pyautogui.doubleClick()
#-------------------------------------------------------
# pyautogui.scroll(delta_y)
# 기본적으로 수직 스크롤링만 존재함.
pyautogui.scroll(-10)
#-------------------------------------------------------
```


## reference

- [pyautogui - mouse](https://pyautogui.readthedocs.io/en/latest/mouse.html)