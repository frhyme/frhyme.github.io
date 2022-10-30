---
title: vim - hardtab 을 softtab으로 수정하기 
category: vim
tags: vim vi  
---

## vim - hardtab 을 softtab으로 수정하기 

- 최근의 coding convention들을 보면, 하나같이 hardtab을 사용하지 않고 있습니다. hardtab은, 우리가 알고 있는 그 탭 `\t` 문자를 말하죠.
- "아니, 나는 지금도 tab을 사용하고 있는데?"라고 생각하실 수 있는데요, vscode와 같은 IDE를 사용하시는 경우, hardtab을 입력해도 알아서 해당 tab을 softtab인 space들로 변경해버리죠. 가령, python file의 경우 hardtab을 4 * space로 알아서 변경해준다는 이야기입니다.
- 그런데, vim에서는 이게 기본적으로 설정되어 있지 않아요. 이것도, 보통은 문제가 없지만, vim에서 text를 복사해서 vscode등으로 가져오는 경우에는, vim에서 작성할 때 입력된 hardtab이 그대로 남아 있어서 waring이 발생하게 되죠. 뭐 큰 문제는 되지 않지만, 노란 색 줄이 죽죽 그어져 있는 거 마음에 들지 않아서 저는 이걸 고쳐야겠습니다.
- `.vimrc` 파일에 아래 내용을 작성해 줍니다.

```vim
" hardtab을 softtab으로 변경해주는 명령어
set expandtab

" softtab의 기본 space 길이를 정의합니다
set softtab=4

" 만약, vi editor mode에서 hardtab을 발견하면, 
" softtab으로 변경해 줄때 그때 space의 개수를 정의합니다.
set tabstop=4
```

- 위와 같이 정의한다고 해서, 기존의 작성된 hardtab이 포함된 문서의 hardtab이 변경되지는 않습니다.
- 이를 변경해 주려면, 문서 내 command mode에서 `:retab`을 사용하면 됩니다.

## reference

- [stackexchange - How to make vim stop making hard tab characters](https://superuser.com/questions/309806/how-to-make-vim-stop-making-hard-tab-characters)
