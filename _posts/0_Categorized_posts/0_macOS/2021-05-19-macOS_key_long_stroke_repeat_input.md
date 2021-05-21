---
title: macOS - 맥북에서 키를 누른 채로 유지할 때, 키 반복 입력 사용하기  
category: macOS
tags: macOS  
---

## macOS - 맥북에서 키를 누른 채로 유지할 때, 키 반복 입력 사용하기  

- 터미널에서 아래 명령어를 사용합니다.

```bash
defaults write -g ApplePressAndHoldEnabled -bool false
```

- 응용프로그램을 껐다가 키면 바로 적용됩니다. 
- 얼마나 빠르게 반복 키가 적용되는 지 등 세부적인 설정값은 맥북의 환경설정 > 키보드에 들어가서 변경할 수 있습니다.

## Reference

- [맥북에서 키를 누른 채로 유지할 때, 키 반복 입력 사용하기](https://macnews.tistory.com/2195)
