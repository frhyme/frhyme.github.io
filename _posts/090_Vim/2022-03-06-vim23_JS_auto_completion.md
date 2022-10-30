---
title: Vim - Javascript - Auto completion 설정
category: vim
tags: vim javascript vi tsserver autocompletion
---

## Vim - Javascript - Auto completion 설정

- Vim에서 javascript auto completion을 사용하려면, [github - neoclide -coc-tsserver](https://github.com/neoclide/coc-tsserver)를 설치해야 하는 걸로 보입니다.
- coc-tsserver를 사용하려면, [coc.nvim](https://github.com/neoclide/coc.nvim)도 설치되어야 합니다.
- vim에서 아래 명령어를 실행하여, coc-tsserver를 설치해줍니다.

```vim
:CocInstall coc-tsserver
```

- 설치 후 `.js` file을 열어 보면 auto completion이 적용될 뿐 아니라, JSLint 역할도 해주는 것으로 보이네요.

## Wrap-up

- coc-tsserver 에서도 기본적인 lint를 처리해줍니다.
- 기존에 설치했던 ESLint의 경우 load에 시간이 오래 걸려서 적용 후 이후 `.js` 파일을 열 때 오래 걸리는 문제가 있어서 여차하면 변경해줘도 괜찮을 것 같다.

## Reference

- [github - pangloss - vim-javascript](https://github.com/pangloss/vim-javascript)
- [github - neoclide -coc-tsserver](https://github.com/neoclide/coc-tsserver)
