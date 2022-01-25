---
title: Vim 17 - syntax checking by syntastic
category: vim
tags: vim python pylint vim syntax
---

## Vim 17 - syntax checking by syntastic

- 작성한 code에 대해서, 잔소리해주는 lint를 설치해보기로 합니다.
- 보통은 코드를 작성한 다음, 커맨드 라인에서 다음의 형태로 실행합니다만, 이렇게 하게 되면 vim > bash > vim의 순서로 왔다갔다 해야 한다는 번거로움이 있죠.

```bash
$ pylint a.py
$ flake8 a.py
$ pylama a.py
$ pycodestyle a.py
```

- vim에서 바로 고쳐야할 부분들을 확인하기 위해서, [github - syntastic](https://github.com/vim-syntastic/syntastic)을 설치합니다.
- 저는 Vundle을 이용해서 설치할 것이므로, `.vimrc`파일 내에 아래 내용을 추가해줍니다.

```bash
set rtp+=~/.vim/bundle/Vundle.vim
call vundle#begin()
" 20220125 - Syntastic for syntax checking 
Plugin 'https://github.com/vim-syntastic/syntastic'
" All of your Plugins must be added before the following line
call vundle#end()            " required
```

- 그리고 vim에서 `:PluginInstall`을 사용하여 Vundle로 등록되어 있는 패키지들을 다 설치해줍니다.
- 그리고 python용 syntaschecker를 설정해줍니다.
- pylint가 좀 더 자세한 분석을 해주지만, 시간이 꽤 오래 걸려서, 그냥 `flake8`로 설정해줬습니다

```bash
" 20220125 - for syntastic configuration
" Syntastics에서 권장하는 setting이라서 무지성으로 세팅함.
set statusline+=%#warningmsg#
set statusline+=%{SyntasticStatuslineFlag()}
set statusline+=%*

let g:syntastic_always_populate_loc_list = 1
let g:syntastic_auto_loc_list = 1
let g:syntastic_check_on_open = 1
let g:syntastic_check_on_wq = 0
" pylint, flake8
let g:syntastic_python_checkers = ['flake8', 'pycodestyle']
" syntax checker for c
let g:syntastic_cpp_compiler = 'gcc'
```

## wrap-up

- 그 외에도 다양한 설정이 있을 것 같은데, 저는 일단 이정도로만 하겠습니다 하하하.

## reference

- [github - syntastic](https://github.com/vim-syntastic/syntastic)
