---
title: PyAutomation - pyautogui - Keyboard Control.
category: python-libs
tags: python python-libs automation pyautogui
---

## 1-line summary 

- [pyautogui](https://pyautogui.readthedocs.io/en/latest/mouse.html)를 이용하면, 키보드의 버튼을 누르고(press) 누르고 있고(keydown), 떼고(keyup) 등을 할 수 있음. 

## Cheat sheet for pyautogui - Keyboard

- `pyautogui`를 이용한, 키보드 동작을 아래 코드로 정리하였습니다.

```python 
import pyautogui
"""
- pyautogui를 사용한 키보드 동작법들을 정리함.
"""

#-------------------------------------------------------
# pyautogui.write(target_text, interval)
# target_text: string or list
# interval target_text의 문자 하나하나 를 타이핑하는 간격
target_text = [chr(i) for i in range(ord('a'), ord('z')+1)]
target_text = "".join(target_text)
# taget_text의 문자 하나하나 사이에 1초의 간격을 두고 타이핑함.
pyautogui.write(target_text, interval=1)
#-------------------------------------------------------
# pyautogui.press('enter')
# 'enter'키를 잠깐 눌렀다가 뗌.
pyautogui.press('enter')
#-------------------------------------------------------
# pyautogui.keyDown('enter')
# 'enter'키를 누르고 있음.
pyautogui.keyDown('enter')
# pyautogui.keyUp('enter')
# 눌려 있던 'enter'키를 풀어줌.
pyautogui.keyUp('enter')
#-------------------------------------------------------
# pyautogui.hotkey(['button_A', 'button_B'])
# 다음의 동작을 따름.
# 1) pyautogui.keyDown(button_A)
# 2) pyautogui.keyDown(button_B)
# 3) pyautogui.keyUp(button_B)
# 4) pyautogui.keyUp(button_A)
pyautogui.hotkey(['button_A', 'button_B'])
```