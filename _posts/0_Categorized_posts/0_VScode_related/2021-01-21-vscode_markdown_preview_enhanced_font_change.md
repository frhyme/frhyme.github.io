---
title: VScode - Markdown Preview Enhanced - Font Change
category: VScode
tags: VScode markdown markdownPreview extension font
---

## VScode - Markdown Preview Enhanced - Font Change

- [VScode: markdown-preview-enhanced](https://github.com/shd101wyy/markdown-preview-enhanced)의 font를 바꿀 때는 `setting.json`이 아니라, markdown-preview-enhanced에 대한 `.css`파일을 바꾸어줘야 합니다.
- `command + shift + P`를 눌러서 command Pallete로 가서 "markdown preview enhanced"를 치고, "Markdown Preview Enhanced: Customize CSS"로 갑니다.
- 그리고 아래 부분을 추가해주면 font가 변경됩니다.

```css
/* Please visit the URL below for more information: */
/*   https://shd101wyy.github.io/markdown-preview-enhanced/#/customize-css */

.markdown-preview.markdown-preview {
    /*
    - modify your style here
    - eg: background-color: blue;
    */
    font-family:"D2Coding";
}
```
