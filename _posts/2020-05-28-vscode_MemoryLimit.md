---
title: VScode - 용량 큰 파일 열기 위해 memory 크기 조정하기
category: VScode
tags: VScode 
---

## Intro

- VScode로 코딩을 하다 보면, 가끔 몇 기가가 넘는 용량의 파일을 열어야 할 때가 있습니다.
- 저의 경우는 이미 학습된 fasttext 벡터를 확인해보려고 그 값을 열어보려고 했는데, 해당 파일의 경우 용량이 8GB를 넘거든요. 

## Configure memory limit 

- 컴퓨터마다 다르겠지만, 저의 경우는 파일을 열때 최대 메모리 사용량이 4096으로 되어 있습니다.
- **"파일을 열때"**의 최대 용량을 말합니다. VScode에서 사용할 수 있는 최대 메모리 용량이 아님에 유의하세요.
- 이 값은, `Preference > Setting > Text Editor > Files > Max Memory for Large Files MB`로 가셔서 수정하면 됩니다.
- 혹은, 그냥 용량 큰 파일을 열려고 보면, 알아서 다음의 알림이 뜨게 되죠. 

> To open a file of this size you need to restart VS Code and allow it to use more memory.

- 이 때 다음의 두 버튼이 뜨게 되고, 각각의 선택 결과는 다음과 같습니다.
  - `The Relaunch button should be: "Restart with 4096 MB"`: 메모리 한계용량 조절 없이 그냥 VScode 재시작
  - `The Configure button should be "Configure Memory Limit"`: 메모리 한계용량 조절
- 또한, 메모리 한계용량을 변경하였으면 VScode 자체를 모두 껐다가 켜야 일괄적용됩니다.

## 그러나. crashed

- 사실, 이 값을 조절한다고 문제없이 열리는 것은 아닙니다. 
- 저는 8GB가 넘는 파일을 보기 위해, 메모리 용량을 8192MB 그리고 12288MB 까지 올려 봤지만, 열리는 것처럼 하다가, 결국은 Crashed라는 말과 함께 열리지 않더군요.
- 결과적으로는 그냥 못 열어봤다는 이야기입니다.
 