---
title: vim 20 - Install NerdTree
category: vim 
tags: vim vi nerdtree plug
--- 

## vim 20 - Install NerdTree

- Vundle을 이용해 설치하므로, NerdTree를 Vundle 목록에 추가해줍니다.
- 추가한 다음, `:PluginInstall`을 실행해주구요.

```vim
" ============================================================
set rtp+=~/.vim/bundle/Vundle.vim
eall vundle#begin()
Plugin 'VundleVim/Vundle.vim'
Plugin 'jiangmiao/auto-pairs'
Plugin 'ervandew/supertab'
" 아래 가 Vundle
Plugin 'https://github.com/preservim/nerdtree'
Plugin 'https://github.com/powerline/powerline', {'rtp': 'powerline/bindings/vim/'}
Plugin 'https://github.com/vim-syntastic/syntastic'
call vundle#end()            " required
```

- 그 다음 `~/.vimrc`에 아래 내용을 수정하여, "normal mode에서 'nerd'를 타이핑하면 NerdTree가 띄워지도록" 해줍니다.

```vim
"=======================================================
" 20220201 - Nerdtree configuration
" normal mode에서 ctrl + n type할 경우 NERDTree가 띄워짐.
nnoremap <C-n> :NERDTreeToggle<CR>
```

- NerdTree의 width가 좁아서, 늘려줍니다.

```vim
let g:NERDTreeWinSize=60
```

- 이렇게 세팅해주고 나면, `ctrl + n`을 사용해서 NerdTree를 활성화/비활성화 해줄 수 있습니다.
- `ctrl + w, w`를 통해 두 window를 오갈 수도 있죠.
- nerdtree에 cursor가 위치하는 상태에서, `m`을 누르면, 다음과 같은 menu 가 뜹니다. file을 지우고, 생성하고 하는 작업들은 여기에서 해주면 됩니다.


### Dev Icon

- 이 형태로는 조금 심심해서, [vim - devicons](https://github.com/ryanoasis/vim-devicons)를 설치하여, nerdtree에서 각 file별로 icon이 뜰 수 있도록 해줍니다.
- Plug 를 이용해서 설치해야하므로, 아래 내용을 `.vimrc` 파일에 추가해줍니다.
- 그리고, `:PlugInstall`을 사용하여, 설치해줍니다.

```vim
" font 문제로 encoding도 정해줘야 함.
set encoding=UTF-8


call plug#begin()
" The default plugin directory will be as follows:
"   - Vim (Linux/macOS): '~/.vim/plugged'
"   - Vim (Windows): '~/vimfiles/plugged'
"   - Neovim (Linux/macOS/Windows): stdpath('data') . '/plugged'
" You can specify a custom plugin directory by passing it as the argument
"   - e.g. `call plug#begin('~/.vim/plugged')`
"   - Avoid using standard Vim directory names like 'plugin'
" Make sure you use single quotes
" --------------------------
" 20220201 - Dev Icons for NerdTree
Plug 'ryanoasis/vim-devicons'
call plug#end()
```

- 설치 후 확인해보면, icon이 잘 뜨는 것을 볼 수 있습니다.

## Wrap-up

- 그 외로도, 다양한 nerdtree용 plugin이 있는 것 같습니다. 가령, github status를 표현해준다거나, file 내용이 변경되었는지 확인한다거나, 하는 다양한 plugin 들이 더 있는 것 같기는 하지만, 귀찮으므로 더 하지 않겠씁니다 하하하.

## Reference 

- [[vi-vim][NerdTree]NerdTree설치하고 사용하기](https://kamang-it.tistory.com/entry/vi-vimNerdTreeNerdTree%EC%84%A4%EC%B9%98%ED%95%98%EA%B3%A0-%EC%82%AC%EC%9A%A9%ED%95%98%EA%B8%B0)
- [github - nerdtree](https://github.com/preservim/nerdtree)
- [stackexchange - how do I change the default size of plugin window nerdtree taglist](https://vi.stackexchange.com/questions/773/how-do-i-change-the-default-size-of-plugin-window-nerdtree-taglist-etc)
