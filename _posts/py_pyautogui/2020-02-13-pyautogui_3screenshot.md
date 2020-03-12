---
title: PyAutomation - pyautogui - Screenshot
category: python-libs
tags: python python-libs automation pyautogui
---

## 1-line summary 

- [pyautogui](https://pyautogui.readthedocs.io/en/latest/mouse.html)를 이용하여, 화면의 스크린샷을 파일로 저장하고, 필요에 따라, 이미지가 화면에서 어디에 위치하는지를 찾을 수 있음. 
- 다만, 어떤 방식으로 찾는지 정확도는 어떠한지에 대해서는 확인이 필요함.

## Cheat sheet for pyautogui - Screenshot and Find img on screenshot

- `pyautogui.screenshot`를 사용해서 화면을 캡쳐할 수 있고
- `pyautogui.locateOnScreen`를 사용해서, 화면에 내가 원하는 이미지가 어디에 있는지도 찾을 수 있음. 

```python
import pyautogui
#-------------------------------------------------------
# pyautogui.screenshot()
# screenshot 저장.
img = pyautogui.screenshot()
pyautogui.screenshot('screenshot_capture.png', region=None)
#-------------------------------------------------------
# pyautogui.locateOnScreen(target_img_file_name)
# target_img_file_name이 화면에서 어디에 있는지를 파악하여,
# (left, top, width, height)를 리턴함.
# 적합한 이미지가 여러 개 있을 경우, 여러개를 리턴함.

# image는 file_name으로 넘겨져야 함.
target_img_file_name = "GoogleLogo.png"
# 찾은 img의 left, top, width, height
print("== pyautogui.locateOnScreen(target_img_file_name)")
left, top, width, height = pyautogui.locateOnScreen(target_img_file_name)
print(left, top, width, height)
# 찾은 img의 center_x, center_y를 리턴함.
print("== pyautogui.locateCenterOnScreen(target_img_file_name)")
center_x, center_y = pyautogui.locateCenterOnScreen(target_img_file_name)
print(center_x, center_y)

# program이 종료되었음을 알림.
pyautogui.alert(text='Complete', title='Alert', button='OK')
```


## reference

- [puautogui - screensho](https://pyautogui.readthedocs.io/en/latest/screenshot.html)