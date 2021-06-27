---
title: vim - clipboard 공유 
category: vim
tags: vim vi clipboard yank
---

## vim - clipboard공유 

- vim에서 작업하다가 일정 코드를 복사해서 vim 외부, 가령 vscode로 복사해서 붙여넣어야 할 때가 있습니다.
- 이때, 마우스로 긁은 다음 ctrl + c, v를 사용하면 문제없이 복사되기는 하는데요. 이렇게 하지 않고, visual mode에서 block을 지정한 다음 y를 눌러서 복사를 하는 경우에는 외부에 붙여넣을 수가 없습니다.
- 이걸 해결하려면 `.vimrc`에 아래 내용을 추가해주면 됩니다.

```vimrc
set clipboard=unnamed
```
