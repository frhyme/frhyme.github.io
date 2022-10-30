---
title: vim32 - get current file name
category: vi
tags: vi vim
---

## vim32 - get current file name

- 저는 markdown을 vim을 사용하여 편집합니다. 이 때, markdown file name을 해당 post의 제목으로 그대로 정하는 경우들이 많은데요. 이게 몹시 사소하지만, 모든 markdown 편집에서 동일하게 작헙하는 내용이라 간단한 명령어로 1) 현재 file 이름을 가져오고, 2) 제목이 들어가야 할 위치에 넣어주기, 로 처리할 수 있을 것 같더라고요.
  - 예를 들어 file name이 `vim_get_current_file_name.md`로 들어온 다면, "vim getlcurrent file name"과 같이, ".md"를 삭제하고, underbar를 space로 변경하는 기능을 추가한 다음, vim cursor에 집어넣어주려고 합니다.
- 그래서 vim script을 사용해서 간단하게 처리해봤습니다.
- 각 명령어들을 설명혀자면 다음과 같습니다.
  - `expand`: 'expand'는 확장 명령어, 정도로 이해하시면 될 것 같은데요. argument로 넘겨 받는 wildcard에 매칭되는 값을 리턴한다, 라고 이해하시면 될 것 같습니다.
  - `split`, `substitute`는 각각 리스트로 분할하고, 문자를 변경하는 기능을 수행하기 때문에 설명이 필요 없을 것 같아요.

```vim
function GetCurrentFileName()
    " 2022-10-30 (Sun): get current file name
    " expand: type "help expand" for more info
    " - % means curent file
    " - :p means absolute path
    " split: split string ex) split("a,b,c", ',')
    " substitute: ex) substitute(target_str, pattern, replace_pattern, flags)
    " flag g means global
    " . means meta character in regex, so, for expressing dot character, use
    " \\.
    " ISSUE:
    " why first character of function name in vim should be upper case?
    let current_file_name = expand("%:p")
    let current_file_name = split(current_file_name , '/')[-1]
    let current_file_name = substitute(current_file_name, "_", " ", "g")
    let current_file_name = split(current_file_name , "\\.")[0]
    return current_file_name
endfunction
```

- 그리고 `iabbrev`를 사용하여 다음과 같이 정의해줍니다.

```vim
autocmd FileType markdown iabbrev __current_file_name <C-R>=GetCurrentFileName()<CR>
```
