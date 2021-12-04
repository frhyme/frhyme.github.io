---
title: vim - bracket completion
category: vim
tags: vi vim vundle plugin bracket
---

## vim - bracket completion

- vim을 사용해서 c로 간단한 코드를 개발하던 중에, 일반적인 IDE들에서는 모두 존재하는 '{'을 타이핑하면 알아서 '}'을 생성해주는 bracket completion이 Vim에서는 되지 않았다. 따라서, vim에서 해당 기능이 구현되도록 설정해보려고 한다.
- 찾아보니 보통 [github - delimitMate](https://github.com/Raimondi/delimitMate)를 사용하는 것으로 보입니다. 다만, 해당 링크로 들어가 보시면, 사용 방법에 대해서 생각보다 자세히 나와 있지 않은 것을 알 수 있습니다.
- 따라서, 저는 [github - auto pairs](https://github.com/jiangmiao/auto-pairs)라고 하는 플러그인을 사용해보기로 합니다. 얘는 delimitMate에 비해서 설치 법등이 훨씬 상세하게 적혀 있습니다.

## Plugin Installation 

- 해당 플러그인을 설치하는 방법은 대략 다음과 같은 방법들이 있습니다.

1. 직접 설치: 플러그인은 vim script로 작성되어 있고, github repo에 이미 공유되어 있으므로 해당 파일 내용을 가져와서(복사해서), `~/.vim/plugin` 내에 파일을 만들어주면 됩니다. 그리고 `.vimrc` 파일 내에 설정을 변경해주면 끝납니다.
2. Vundle을 이용하여 설치: [Vundle](https://github.com/VundleVim/Vundle.vim)은 vim에서 사용하는 plugin들을 관리하는 plugin manager입니다. python에서 pip 가 하는 역할과 비슷하다고 보면 되죠. 따라서, vundle을 설치하고 나면 vundle을 이용해서 plugin을 설치해주면 될 것으로 보입니다.
3. Pathogen을 이용하여 설치: [Pathogen](https://github.com/tpope/vim-pathogen) 또한 Vundle과 비슷하게, vim에서 사용하는 plugin을 관리해주는 manager입니다.

- Vundle과 Pathogen 모두 기능적으로는 유사하게 보이나, github repo 기준으로 볼 때, Vundle이 Star의 수가 두 배 가량 많습니다. 또한 다른 포스팅에서도 Vundle이 더 좋다는 이야기들이 있어서, Vundle을 사용해서 설치해보려고 합니다. 

### Install Vundle, auto-pair

- [Vundle](https://github.com/VundleVim/Vundle.vim)을 설치하기 위해서는 우선 git vundle repo로부터 해당 소스를 가져옵니다.
- 혹시나 싶어서, `~/.vim/bundle/`에 이미 설치되어 있는 것들이 있는지 확인해보았으나, `bundle`폴더도 만들어져 있지 않네요.
- 아래 코드는 Vundle repo에 있는 폴더와 파일들을 `~/.vim/bundle/Vundle.vim/` 그대로 가져오는(clone) 것을 말합니다. 가져온 다음 폴더와 파일들이 잘 생성되었는지 확인해 봅시다.

```bash
git clone https://github.com/VundleVim/Vundle.vim.git ~/.vim/bundle/Vundle.vim
cd ~/.vim/bundle/Vundle.vim
```

- 그 다음, `~/.vimrc` 파일을 열어서 아래 내용을 가장 위에 첨부해줍니다. 만약 기존에 작성된 내용들이 있다면, 그 위에 작성해주면 되겠죠.
  - `call vundle#begin()` ~ `call vundle#end()`: 이 사이에 필요로 하는 plugin이 위치하면 됩니다. 일단은 Vundle.vim을 제외하고는 모두 삭제를 하였어요.
  - 그리고 제가 설치하려는 bracket completion pluing인 [github - autopairs](https://github.com/jiangmiao/auto-pairs)를 설치해보기로 합니다.
  - 설치하려면, 그냥 아래 한 줄을 추가하면 되죠.

```vim
set nocompatible              " be iMproved, required
filetype off                  " required

" set the runtime path to include Vundle and initialize
set rtp+=~/.vim/bundle/Vundle.vim
call vundle#begin()
" alternatively, pass a path where Vundle should install plugins
"call vundle#begin('~/some/path/here')

" let Vundle manage Vundle, required
Plugin 'VundleVim/Vundle.vim'

" 20211203 - Install plugin- autopairs 
Plugin 'jiangmiao/auto-pairs'

" All of your Plugins must be added before the following line
call vundle#end()            " required
filetype plugin indent on    " required
" To ignore plugin indent changes, instead use:
"filetype plugin on
"
" Brief help
" :PluginList       - lists configured plugins
" :PluginInstall    - installs plugins; append `!` to update or just :PluginUpdate
" :PluginSearch foo - searches for foo; append `!` to refresh local cache
" :PluginClean      - confirms removal of unused plugins; append `!` to auto-approve removal
"
" see :h vundle for more details or wiki for FAQ
" Put your non-Plugin stuff after this line
```

- 그리고, vim에 들어가서 command line에서 ':PluginInstall'을 타이핑해줍니다. 순서대로 하면 다음과 같죠.

```vim
vim
:PluginInstall
:q!
```

## Wrap-up

- 해피해킹을 쓰는 입장에서 Vi는 정말 편하고, 손에 금방 익어서 일을 매우 효율적으로 처리할 수 있는 editor이고, command line을 오가면서 일을 해야 할때 특히 유용하긴 한데요. 한글을 기본 언어로 하는 입장에서는 수없이 한글영어전환을 눌러야 해서 꽤나 번거로워지는 것도 사실입니다. 제가 영어를 자유롭게 쓸 수 있는 사람이라면 훨씬 빠르게 적응했을 것 같아요.
- 그러함에도, 최근에는 command line에서 작업해야 하는 일이 늘어나고 있고 vscode가 조금씩 마음에 들지 않는 경우들이 있어서 넘어갈까 말까 고민하고 있는 상황이에요. 지금처럼 plugin들을 조금씩 설치하면서 나중에는 넘어갈지도 모르겠네요.

## Reference

- [[vim/Linux] 7. delimitMate, 괄호 자동 완성 플러그인](https://myeongjae.kim/blog/2017/07/15/vimlinux-7-delimitmate-%EA%B4%84%ED%98%B8-%EC%9E%90%EB%8F%99-%EC%99%84%EC%84%B1-%ED%94%8C%EB%9F%AC%EA%B7%B8%EC%9D%B8)
