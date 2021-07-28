---
title: vim - color theme 설정
category: shell
tags: vim shell terminal theme
---

## vim - color theme 설정

- vim의 color theme을 변경해줍니다(vim은 vi의 향상된(iMproved) 버전입니다).
- 홈(`~`) 디렉토리에 `.vim`폴더를 만들고 내부에 다시 `colors` 폴더를 만들어 줍니다.
- 맥북의 경우 `/usr/share/vim/vim81/colors`를 내에 이미 설치되어 있는 colorscheme들도 있습니다만, 저는 [jellybeans](https://github.com/nanotech/jellybeans.vim)를 다운받습니다. 그리고 앞서 만들어준 `.vim/color` 내에 새로운 theme를 넣어 줍니다.

```plaintext
cd ~/.vim/colors
curl -O https://raw.githubusercontent.com/nanotech/jellybeans.vim/master/colors/jellybeans.vim
```

- 그 다음, Home directory에 `.vimrc` 파일을 만들고 다음을 작성해줍니다. `.vimrc` 파일은 vim이 실행되면 자동으로 실행되는 커맨드를 말합니다.
  - `syntax on`: syntax highlighting을 활성화
  - `colorscheme jellybeans`: color scheme를 jellybeans으로 설정해줌
  - `set number`: 각 줄에 number를 매김

```plaintext
syntax on
colorscheme jellybeans
set number
```

- 이제 `vim`을 실행하면 colorscheme이 적용되어 있는 것을 알 수 있습니다.
