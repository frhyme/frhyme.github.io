---
title: Vim 15 - Install coc.nvim
category: vim 
tags: vim completer vi plugin c go
---

## Vim 15 - Install coc.nvim

- 
- 기존에 설치한 Vim Plugin Manager인 Vundle을 사용하여 coc.nvim을 설치하려고 하였습니다. 다만, Vundle을 사용하여 설치하는 방법이 따로 적혀 있지 않기에, 찾아보니 [github - coc.nvim - How to install using Vundle #1210A](https://github.com/neoclide/coc.nvim/issues/1210)에서, 대충 "Vundle은 유지보수도 되고 있지 않은 프로젝트라서 얘는 지원안하고, Vim Plug만 가능하다"는 뉘앙스의 이야기가 있습니다. 넵 그렇다면 Vim Plug를 사용하겠습니다.

### Install Vim Plug

- 아래 명령어를 통해, vim-plug 를 설치합니다.

```bash
$ curl -fLo ~/.vim/autoload/plug.vim --create-dirs \
    https://raw.githubusercontent.com/junegunn/vim-plug/master/plug.vim
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100 82854  100 82854    0     0   330k      0 --:--:-- --:--:-- --:--:--  330k
$ cd ~/.vim/autoload  
```

- 아래 내용을 `.vimrc` 파일에 작성해주고, `:PlugInstall`를 실행하여, 해당 플러그인들을 설치해줍니다.

```bash
"====================================================
call plug#begin()
" The default plugin directory will be as follows:
"   - Vim (Linux/macOS): '~/.vim/plugged'
"   - Vim (Windows): '~/vimfiles/plugged'
"   - Neovim (Linux/macOS/Windows): stdpath('data') . '/plugged'
" You can specify a custom plugin directory by passing it as the argument
"   - e.g. `call plug#begin('~/.vim/plugged')`
"   - Avoid using standard Vim directory names like 'plugin'
" Make sure you use single quotes
Plug 'neoclide/coc.nvim', {'branch': 'release'}
call plug#end()
"====================================================
```

- [github - coc.nvim - language-servers](https://github.com/neoclide/coc.nvim/wiki/Language-servers)를 참고하여, 필요한 language를 설치해줍니다.

- 아래를 통해 go, c를 설치해줍니다.

```bash
:CocInstall coc-go
:CocInstall coc-clangd
```

## Wrap-up

- 이렇게 설치하고 나면, 잘 작동합니다. YouCompleteMe를 사용하지 않아도 될것 같아요. 

## Reference 

- [github - neoclide - coc.nvim](https://github.com/neoclide/coc.nvim)
- [기계인간 - John Grib - coc.nvim을 사용해보자](https://johngrib.github.io/wiki/vim-coc/)
- [github - vim-plug](https://github.com/junegunn/vim-plug)
