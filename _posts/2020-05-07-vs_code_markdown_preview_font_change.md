---
title: VS-code에서 markdown-preview를 할때 font와 font크기를 변경하는 방법
category: vs-code
tags: vs-code font
---

## Intro

- 저는 대부분의 문서들을 markdown으로 관리합니다. 그리고 현재의 문서를 markdown preview를 사용해서 보구요. 이 때, 이 markdown 미리보기를 하려면 맥 기준 `command+shift+v`를 하면 되죠.
- 다만, raw markdown에서 저는 font를 12로 해두고 있고, font도 다르게 하는데, markdown 미리보기에서는 이 부분이 달라서, 조금 성가시더라고요. 그래서 그걸 변경했습니다.

## Setting - extension

- setting에 들어가서(`command+,`) 아래 라인을 추가해줍니다.

```json
"markdown.preview.fontFamily": "Menlo, Monaco, 'Courier New', monospace, NanumGothicCoding",
"markdown.preview.fontSize": 12
```
