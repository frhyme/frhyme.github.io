---
title: vscode - sidebar file filtering disable 
category: vscode
tags: vscode sidebar setting json
---

## vscode - sidebar file filtering disable 

- vscode에서 sidebar를 검색할 때 filename에 따라 filtering하도록 하는 기능이 활성화될때가 있는데요. 저는 이게 상당히 성가시더군요.
- 그래서, `setting.json`에서 다음 내용을 추가해주시면 해당 기능이 활성화되지 않습니다. 

```json
"workbench.list.automaticKeyboardNavigation": false
```
