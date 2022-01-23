---
title: Vim 16 - jedi-vim to coc.nvim
category: vim 
tags: vim completer vi plugin jedi python
---

## python completer를 Jedi에서 coc.nvim으로 변경해봅니다

- 처음에는 Jedi를 사용해서 python auto complete를 사용했습니다만, .(dot)을 누른다음, popup이 뜨는 데 까지 너무 오랜 시간이 소요되더군요. 물론 맨 처음 라이브러리를 호출하고 나면, 그다음부터는 조금 빨라지기는 했지만, 그래도 충분히 빠르지는 않았습니다.
- 따라서, jedi-vim을 사용하지 않고, coc.nvim을 통해 coc-jedi를 설치하기로 했습니다
- 우선, 기존에 Vundle을 통해 설치한 jedi-vim을 해제합니다.

```bash
" ============================================================
set rtp+=~/.vim/bundle/Vundle.vim
call vundle#begin()
" 20211222 - Install Jedi-vim for python autocomplete
" Disable for use coc.nvim in python 
" Plugin 'davidhalter/jedi-vim'
call vundle#end()            " required
```

- 그리고 아래 명령어를 사용하여, coc-jedi를 설치해줍니다.
- coc-jedi 말고도, coc-python, coc-pyright 등을 설치해서 사용할 수도 있습니다만, 저는 현재로서는 coc-jedi가 제일 좋아 보입니다.

```bash
:CocInstall coc-jedi
```

- 다른 유용한 명령어들로는 다음이 있습니다.

```bash
:CocConfig
:CocUninstall coc-jedi
:CocList extensions
```

### coc-jedi configurtion 

- [coc-jedi](https://github.com/pappasam/coc-jedi)에서 주요 configuration을 확인할 수 있습니다.
- 저는 일단, 아래 두 모듈에 대해서 로드가 빨리 되도록 처리한 상황입니다. 

```python
{
    "jedi.jediSettings.autoImportModules": ["numpy", "pandas"]
}
```

## Wrap-up

- 완벽하지는 않고, documentation이 되어 있기는 하나, 충분히 잘 이해되는 정도로 정리되어 있지는 않아서 진행하면서 좀 더 봐야 할 것 같아요.
- 그리고, 사실 파이썬으로 개발하는 사람들은 대부분 pycharm을 사용하거나, vscode를 사용하겠죠. 따라서, 사용자가 적은 편이고, 블로그등을 통해서 참고할 수 있는 내용도 제한적이므로, 아직 파훼할 내용들이 좀 더 많아보여요.
- 앞으로도 configuration을 보면서 더 수정할 것 같은데요, 자잘한 내용들은 진행하면서 더 추가하는 식으로 진행하겠습니다. 대략 다음 내용들이 추가되지 않을까 싶네요.
  - popup 창 스크롤 하는 방법 > `set mouse=a`
  - tab completion
  - syntax and convention checking: pylint가 잘되지 않아서, syntastic을 상해보려고 합니다
- 물론 완벽하지는 않습니다. type 추론이 잘 되지 않는다거나, 자동 완성이 생긴 다음 캐릭터를 지우면 자동완성이 다시 생기지 않는다거나, 하는 문제들이 있지만, 일단은 더 써보면서 맞춰 봐야 할 것 같아요. 
- 이제 auto completion에 대한 자잘한 설정, tab completion, syntac and convention checking을 하면 될 것 같습니다.

## Reference 

- [coc.nvim - language servers - python](https://github.com/neoclide/coc.nvim/wiki/Language-servers#python)
- [Python 개발자를 위한 Vim 설정!](https://m.blog.naver.com/onevibe12/222003789290)
- [NeoVim 기반 개발환경 설정](https://www.joinc.co.kr/w/man/12/neovim)
- [github - coc-jedi](https://github.com/pappasam/coc-jedi)
