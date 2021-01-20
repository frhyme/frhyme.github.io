---
title: VScode - File Explorer의 font size를 줄여 봅시다.
category: VScode
tags: VScode FontSize
---

## VScode) File Explorer의 font size를 줄여 봅시다

- VScode로 문서를 편집할 때, Side에 있는 Explorer의 font가 너무 크다고 느껴질 때가 있습니다. 이 부분만 font 크기를 줄여보겠습니다.전체를 줄이지 않고, 
- 그러나, 아주 슬프게도, VScode는 File Explorer 부분의 폰트 크기만 별도로 줄일 수는 없습니다. 따라서, 약간 특이한 방법을 사용해야 하는데요.
- 우선, 전체 윈도우의 줌 레벨(`Window: Zoom Level`)을 낮춥니다. 저는 `-0.5`로 낮췄습니다.

```plaintext
Window: Zoom Level
Adjust the zoom level of the window. 
The original size is 0 and each increment above (e.g. 1) or below (e.g. -1) represents zooming 20% larger or smaller. 
You can also enter decimals to adjust the zoom level with a finer granularity.
```

- 그러나, 이렇게 Window Zoom Level을 낮추고 나면 Explorer 뿐만 아니라 모든 윈도우의 크기가 작아지게 되죠. 앞서 말한 것처럼 저는 윈도우의 크기를 줄이고 싶지는 않거든요.
- 따라서, font size를 좀 키워보겠습니다. 저는 13으로 세팅했습니다.

```plaintext
Editor: Font Size
Controls the font size in pixels.
```

- 결과적으로 다음 두 line이 `setting.json`에 추가되어 있습니다.

```json
"window.zoomLevel": -0.5,
"editor.fontSize": 13,
```

## Reference

- [stackoverflow - visual studio code change font size for file explorer tray](https://stackoverflow.com/questions/36040857/visual-studio-code-change-font-size-for-file-explorer-tray)
