---
title: vim12 - Install Powerline
category: vim
tags: vim vi powerline plugin shell 
---

## vim12 - Install Powerline

- Vim에서 작업시에, [Powerline](https://github.com/powerline/powerline)을 이용해서, 좀더 효과적으로 현재 상황을 확인할 수 있습니다.
- Vundle을 이용해서 설치할 수 있는데요, `.vimrc` 파일 내에 아래와 같은 내용을 작성해줍니다.

```bash
set rtp+=~/.vim/bundle/Vundle.vim
call vundle#begin()
" ...
" 20220106 - Install powerline
" ~/.vim/bundle/powerline/powerline/bindings/vim
Plugin 'https://github.com/powerline/powerline', {'rtp': 'powerline/bindings/vim/'}
" ...
call vundle#end()            " required
```

- 그다음 vim 내에서 `:PluginInstall`을 타이핑하고 엔터를 쳐줍니다.
- 그리고 아래 경로로 가서 powerline이 잘 설치되었는지 확인합니다.

```bash
cd /Users/seunghoonlee/.vim/bundle/powerline
ls
```

- 그리고 .vimrc파일 내에 아래와 같이, Powerline_symbols(테마)를 지정해줍니다

```bash
"====================================================
" 20220106 - sng_hn.lee - PowerLine configurtion
let g:Powerline_symbols = 'fancy'
"====================================================
```

- 그리고, vim으로 파일을 열어 보면 잘 열리는 것을 확인할 수 있습니다.

## Wrap-up

- 몇 가지 설정등을 바꿀 수도 있겠지만, 오늘은 일단 여기까지만 하고 넘어갑니다.
- [github - vim airline](https://github.com/vim-airline/vim-airline)이라고 하는 plugin도 있습니다. 오히려 얘가 github 기준 star의 수가 많은데요. 어떤 차이가 있는지 궁금하네요.

## reference

- [linux powerline 설치](https://jootc.com/p/20180521979)
- [Bash Terminal을 세련되게 - Mac](https://vvshinevv.tistory.com/77)
- [github - powerline](https://github.com/powerline/powerline)
- [github - vim airline](https://github.com/vim-airline/vim-airline)
- [github - powerline - issues - 414](https://github.com/powerline/powerline/issues/414)
