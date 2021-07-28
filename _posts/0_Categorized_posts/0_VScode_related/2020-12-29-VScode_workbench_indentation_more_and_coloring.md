---
title: VScode - Workbench indentation more
category: VScode
tags: VScode 
---

## VScode - Workbench indentation more

- Explorer 부분에 여러 폴더와 파일이 존재하는데요, nested인 경우 들여쓰기 폭이 너무 작아서 구별이 되지 않아서, 얘를 늘렸습니다.
- setting 들어가셔서 아래 부분을 손 보면 됩니다.

```json
"workbench.tree.indent": 16,
```

- 저는 추가로 같은 경로라는 것을 표시해주는 색깔도 추가했습니다.

```json
"workbench.colorCustomizations": {
    // ...
    // ... 
    // 20201229 frhyme added this.
    "tree.indentGuidesStroke": "#00ff00"
}
```
