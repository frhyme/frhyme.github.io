---
title: Vim 14 - Auto Completion
category: vim
tags: vim shell completion vi abbrev
---

## Vim - Auto Completion

- Vim에서 사용할 수 있는 Auto Completion 을 정리합니다.
- 다양한 Blog로부터 도움을 받았으나, 특히, [John Grib - vim 자동완성 기능 사용하기](https://johngrib.github.io/wiki/vim-auto-completion/#youcompleteme)으로부터 큰 도움을 받았습니다.

### Basic Auto Completion

- vim 사용 중에 Insert Mode에서 기본적으로 사용할 수 있는 자동완성 단축키는 다음 등이 있습니다. 모두, Insert Mode에서만 사용 가능합니다. 아래에서는 풀어서 `Ctrl` + `r` 등으로 작성하였으나, 보통은 그냥 `<C-r>` 등으로 표현합니다.
    1. `Ctrl` + `p`: 현재 cursor 이전의(previous) word들을 기본으로 matching completion. 즉, 현재 커서에서 바로 윗 줄에 있는 keyword가 가장 먼저 나옵니다.
    2. `Ctrl` + `n`: 현재 cursor 이후의(next) word들을 기본으로 matching completion. 현재 Cursor의 다음 줄(recursive)에 있는 keyword가 가장 먼저 나옵니다.
    3. `Ctrl` + `a`: 가장 최근에 삽입된 keyword를 넣어줍니다. 이건 약간 트리키해서 보충이 필요함.
    4. `Ctrl` + `x`, `f`: 현재 vim이 연 파일이 존재하는 폴더 내의 파일명 들을 가져올 수 있습니다.
    5. `Ctrl` + `r`: register에 저장되어 있는 값을 가져와서 붙여넣습니다.

### Abbreviation - basic

- abbreviation은 "약자"를 의미하며, 긴 코드를 매번 타이핑 할 필요 없이, 특정 문자열에 긴 문자열을 매핑하는 방법을 말합니다.
- 다양하게 사용될 수 있으나, 저는 markdown작업을 위해서, markdown 문서 가장 앞에 작성하는 frontmatter를 빠르게 타이핑할 수 있도록 연결해두었습니다.
- 특히 오타 교정용으로 유용하다고 하지만, 오타를 안내는 습관을 만드는 것이 더 좋지 않을까, 하는 생각도 있어서, 과도한 사용은 오히려 독이 될 수 있을 거라는 생각을 합니다.

```bash
"====================================================
" Abbreviation - 20220105 - sng_hn.lee
" abbreviate 를 줄여서 ab 로 써도 문제가 없습니다.
" 하지만 저는 가독성을 위해 가능하면 full world를 쓰기 때문에 다음처럼
" 사용하였습니다.
" for Single word
abbreviate abc aaaaaaaaaaaaa
" iabbrev: valid in insert mode
" cabbrev: valid in command mode
iabbrev aaa bbb
cabbrev bbb ccc
" for Multi line 
" \: bash에서 multiline을 표시할 때는 앞에 backslash 
" <CR>: linebreak 
iabbrev multiline 
\line1
\<CR>line2
\<CR>line3
" Front Matter for Markdown
iabbrev frontmatter 
\---
\<CR>title:
\<CR>category: 
\<CR>ttags:
\<CR>---
"====================================================
```

### Abbreviation - Advanced

- 간단한 문자열 치환만으로 끝내지 않고, 해당 문자열에 shell script를 mapping하여 이상한 짓을 할 수도 있죠.
- `system()`은 shell script 내에서 shell command를 사용할 수 있는 명령어입니다. argument로 shell command를 넘겨주면 변환되죠. 해당 명령어는 shell 에 바로 입력하는 것은 안되고, shell script내에서만 작성할 수 있습니다.
- 해당 command가 shell script인 경우, 즉 해당 script를 실행한 다음 그 결과를 리턴해야 하는 경우애는 `iabbrev` 다음에 `<expr>`을 붙여서 해당 명령어는 shell script라는 것을 명시해줍니다.
- 예제는 다음과 같습니다.

```sh
" command for shell script
iabbrev <expr> __pwd system('pwd')
iabbrev <expr> __ls system('ls')
```

## Wrap-up

- 처음에는 vim에서 작업을 하려면 무조건 YouCompleteMe와 같은 plugin이 필수라고 생각했는데요, 오늘 공부한 내용들을 사용해서, 어느 정도는 효율적으로 작업할 수 있지 않을까 합니다.

## Reference

- [georgebrock - vim completion](https://georgebrock.github.io/talks/vim-completion/)
- [baeldung - vim registers](https://www.baeldung.com/linux/vim-registers)
- [Vi, Vim 약어 매크로](https://ttend.tistory.com/750)
- [vim - Multi Line Abbreviations](https://vim.fandom.com/wiki/Multi-line_abbreviations)
