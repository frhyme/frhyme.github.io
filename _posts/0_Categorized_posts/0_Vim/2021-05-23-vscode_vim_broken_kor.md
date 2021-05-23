---
title: vscode - vim - 한글 삭제시 글자가 2개 지워지는 현상  
category: vscode
tags: vscode vim markdown 
---

## vscode - vim - 한글 삭제시 글자가 2개 지워지는 현상  

- vs code에서 vim 을 설치했는데, 한글을 지울 때 덜 지워지고 남아 있는 경우가 있습니다. 이게 설명하기는 조금 어려운데, 모음 하나만 남아 있는 경우 지웠는데 지워지지 않아서 한 번 더 지우면 지워진다거나, 하는 등의 문제가 있다는 이야기죠. 
- 조금 더 구체적으로 설명하자면, "각ㅇ"를 타이핑한 상황에서 backspace를 누르면, "ㅇ" 남습니다. 글자가 자음 하나 있는 상황에서 backspace를 눌렀는데, "ㅇ"가 지워지는 것이 아니라, "각"이 지워지는 이상한 상황이 발생하는 것이죠.
- 또한 이 문제는, 윈도우에서는 발생하지 않고, macO에서만 발생하는 이슈로 보입니다.

## 무엇이 문제인가? 

- 처음에는, [vscode에서 vim 플러그인 사용시 한글 입력 문제](https://www.clien.net/service/board/lecture/15827635)에서도 비슷한 경우가 있는 것으로 보여서, vs code vim plugin 문제인 것으로 보였습니다. 그런데, 흥미롭게도, 확장자명이 `.md`인 파일에서만 이런 일이 발생합니다. 다른 파일에서는 이런 일이 발생하지 않죠.
- `setting.json`에서는 특별한 문제를 발견하지 못하여서, 혹시나 싶어, extension인 markdown all in one을 해제했더니, 해당 이슈가 발생하지 않습니다.
- 또한, 저는 markdown preview로는 

## markdown env setting

- 저는 markdown 관련 extension으로 markdown preview enhanced, markdownlint를 사용합니다. 그래서 lint, preview에는 별 문제가 없으나, markdown All in One을 비활성화하니까, list(`-`)의 형식으로 글을 쓸때 다음 줄도 자동으로 `-`으로 인식하고 다음 줄에 `-`을 넣어주는 자동완성 기능이 활성화되지 않습니다. 따라서, 매번 `-`을 타이핑 해줘야 하는 작은 번거로움이 있죠.
- markdown all in one extension을 유지한 상태로, 한글 삭제 시 발생하는 문제를 해결하려고 `setting.json`을 수정해보았으나, 마음 같이 되지 않아서 그냥 안하기로 합니다 하하.
