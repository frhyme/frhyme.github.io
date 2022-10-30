---
title: Vim 18 - set mouse a
category: vim
tags: vim moust vi 
---

## Vim 18 - set mouse a

- 저는 IDE로는 Vim을, python auto completion으로는 coc-nvim, coc-jedi를 사용하고 있습니다.
- 이 때, 각 메소드를 선택할 때, popup 창이 뜨는데요, 팝업 창 옆으로 스크롤이 뜨는데, 이 스크롤을 움직일 수가 없더군요.
- 알고보니, 이 스크롤은 키보드로 움직일 수 있도록 하는 것이 아니고, 마우스로 움직이는 것으로 보입니다. 그리고 vim 설정에 아래 커맨드를 추가해 줘야 하죠. 즉, `.vimrc`파일 내에 아래 를 추가해주면 됩니다.

```bash
set mouse=a
``` 

- 위 커맨드를 설정해 주고 나면, 마우스 스크롤을 사용하여 vim의 문서를 위아래로 움직일 수 있고, 클릭으로 커서를 움직일 수도 있고, 그냥 일반 에디터와 동일하게 모두 움직인다고 보면 됩니다.
- `a`는 "all mode"를 의미한다고 보시면 되고, 특정 모드에서만 발현되도록 하고 싶다면, `i`, `c` 등을 설정해주시면 됩니다

## Wrap-up

- 그 외에도 여러 기능들이 있는 것 같지만, 일단은 여기까지만 알아봅니다. 필요하지 않거든요 호호.

## Reference

- [github - coc-jedi](https://github.com/pappasam/coc-jedi)
- [[번역] Vim mouse mode](https://ujuc.github.io/2015/07/25/vim-mouse-mode/)
