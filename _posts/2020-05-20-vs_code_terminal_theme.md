---
title: VS-CODE - Terminal의 색깔 바꾸기
category: VS-CODE
tags: VSCODE terminal theme color-theme
---

## intro: vs-code terminal different color

- 저는 주 IDE로 vs-code를 사용하고 있습니다.
- 사용하면서 딱히 문제는 없는데, 쓰다보면서 점차 조금씩 테마라거나 바꾸고 싶은 마음이 생기죠.
- 대부분은 바꾸었는데, 요즘은 내부 Terminal의 Theme을 바꾸고 싶다는 생각을 하고 있습니다.
- 물론 바꾸지 않아도 딱히 문제는 없지만, 저는 "할 수 있는지 없는지"를 아는 것이 중요합니다.

## 그냥 색깔 바꾸기

- 간단하게는 `setting.json`에 값을 추가하여 덮어씌워주는 방법이 있습니다.
- `setting.json`을 열어야 하므로 `command + p`를 해주고 `setting.json`을 쳐주면 열리죠.
- 그리고 다음의 내용을 추가해줍니다.
- 이렇게 하는 것만으로도 색깔은 바뀝니다만, 저는 이렇게 바꾸는 것말고 좀 더 멋진 theme으로 바꾸고 싶다는 생각을 하고 있어요.

```json
"workbench.colorCustomizations": {
    "terminal.background":"#FEFBEC",
    "terminal.foreground":"#6E6B5E",
}
```

## themes: vscode-base16-term

- 다만, [Base16 Terminal Colors for Visual Studio Code](https://glitchbone.github.io/vscode-base16-term/#/)에 다양한 theme에 대한 json들이 정리되어 있습니다. 들어가서, 복사하고 `setting.json`에 그대로 넣어주면 깔끔하게 변경되죠.
- 저는 다양한 theme중에서, [3024](https://glitchbone.github.io/vscode-base16-term/#/3024)를 선정했습니다.

```json
"workbench.colorCustomizations": {
    "terminal.background":"#090300",
    "terminal.foreground":"#A5A2A2",
    "terminalCursor.background":"#A5A2A2",
    "terminalCursor.foreground":"#A5A2A2",
    "terminal.ansiBlack":"#090300",
    "terminal.ansiBlue":"#01A0E4",
    "terminal.ansiBrightBlack":"#5C5855",
    "terminal.ansiBrightBlue":"#01A0E4",
    "terminal.ansiBrightCyan":"#B5E4F4",
    "terminal.ansiBrightGreen":"#01A252",
    "terminal.ansiBrightMagenta":"#A16A94",
    "terminal.ansiBrightRed":"#DB2D20",
    "terminal.ansiBrightWhite":"#F7F7F7",
    "terminal.ansiBrightYellow":"#FDED02",
    "terminal.ansiCyan":"#B5E4F4",
    "terminal.ansiGreen":"#01A252",
    "terminal.ansiMagenta":"#A16A94",
    "terminal.ansiRed":"#DB2D20",
    "terminal.ansiWhite":"#A5A2A2",
    "terminal.ansiYellow":"#FDED02"
}
```

## wrap-up

- 일단은 바꿨습니다. 뭐 좀 더 써봐야 잘 알겠네요.

## reference

- [VS 코드 통합 터미널의 색상 테마](https://www.it-swarm.dev/ko/terminal/vs-%EC%BD%94%EB%93%9C-%ED%86%B5%ED%95%A9-%ED%84%B0%EB%AF%B8%EB%84%90%EC%9D%98-%EC%83%89%EC%83%81-%ED%85%8C%EB%A7%88/830099841/)
- [Base16 Terminal Colors for Visual Studio Code](https://glitchbone.github.io/vscode-base16-term/#/)
