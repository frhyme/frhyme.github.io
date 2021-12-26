---
title: vim10 - Install jedi-vim for python
category: vim
tags: vim jedi python programming
---

## vim10 - Install jedi-vim for python

### Install Vundle, Jedi-Vim 

- Vundle을 이용해서, jedi-vim을 설치해봅니다.

```bash
git clone --recursive https://github.com/davidhalter/jedi-vim.git ~/.vim/bundle/jedi-vim
```

- `~/.vimrc`에 아래 내용을 추가해줍니다.

```bash
" ============================================================
set rtp+=~/.vim/bundle/Vundle.vim
call vundle#begin()

" ...
Plugin 'davidhalter/jedi-vim'
" ...
call vundle#end()            " required
```

- 그리고 vim 내에서 `:PluginInstall`을 실행해줍니다.
- python 파일을 열어보니 아래와 같은 오류가 발생하는데 흠. 이건 pathogen, vundle 뭘로 해도 동일한 것으로 보입니다.

```plaintext
Error detected while processing BufRead Autocommands for "*.py"..FileType Autocommands for "*"..function <SNR>7_LoadFTPlugin[17]..script 
Error: jedi-vim failed to initialize Python: jedi-vim requires Vim with support for Python 3. (in BufRead Autocommands for "*.py"..FileType Autocommands for "*"..function <SNR>7_LoadFTPlugin[17]..script
Error detected while processing BufRead Autocommands for "*.py"..FileType Autocommands for "*"..function <SNR>7_LoadFTPlugin[17]..script 
E117: Unknown function: jedi#configure_call_signatures
```

- 이는 현재 사용하고 있는 vim이 jedi-vim에서 원하는 어떤 기능을 실행해주지 못해서, 발생하는 문제라는 이야기죠.

### Install Python feature with vim 

- 따라서, brew 를 사용해서 새로운 vim을 설치해봅니다. 현재 제가 사용중인 python의 버전은 3.7.6입니다

```bash
brew install vim python@3.7         
```

- 일단 vim `:version`을 실행해서, 현재 vim의 version과 설치된 feature들을 확인해 봅니다.
- 확인해 보면, compile이 새롭게 된 것을 알 수 있고, feature에도 원래 없던 langmap이 생겼고, python3도 설치된 것을 알 수 있다. 즉, vim을 세팅하고 나니, 이제 jedi vim이 문제없이 실행됩니다. 물론 바로 설정되지는 않고, 터미널을 껐다 키면 적용되곤 합니다. 만약, 바로 모두 적용하고 싶다면, `:so .vimrc`를 사용하면 됩니다.
- 사실 이제서야 아는 거지만, vim command에서 

- 뒤늦게 보니, 아래와 같은 요구사항이 분명하게 작성되어 있었습니다. 즉, python vim에 함께 compile되어 있어야, jedi-vim이 사용될 수 있다는 얘기죠.

```plaintext
You need a VIM version that was compiled with Python 2.7 or later (+python or +python3). You can check this from within VIM using :python3 import sys; print(sys.version) (use :python for Python 2).
```

- `:so .vimrc`를 사용하면 바로 적용할 수 있다.

### Change Vim to NeoVim

- jedi vim이 가령 `nx.`을 입력해서 메소드를 보려고 하면, 약 5초가 걸립니다. 몇 번 부르고 나면 조금 빨라지기는 하지만.
- 이게 jedi vim의 문제가 아니라, vim 자체의 문제가 아닐까 싶어, vim을 변경해보기로 합니다.

## wrap-up

- 다만, 실제로 Neovim을 설치해서 진행해보니, NeoVim을 설치한다고 해서 jedi-vim이 빨라지는 것 같지는 않습니다.
- 그래서 더 진행하지 않기로 했씁니다.

## reference 

- [github - jedi vim](https://github.com/davidhalter/jedi-vim)
- [vim 빌드해보자](https://ujuc.github.io/2017/01/28/vim_bir-deu-hae-bo-ja/)
