---
title: vim - iabbrev - trailing space
category: vim
tags: vim vi iabbrev
---

## vim - abbrev - trailing space

- `iabbrev`는 vim insert mode에서 사용하는 축약어 명렁어로서, 길게 type해야 하는 단어 혹은 구절을 축약어로 만들어두고 빠르게 해당 내용을 입력할 수 있도록 해줍니다.
- 저의 경우는 다음 등으로 사용하고 있습니다.

```vim
iabbrev __fmt ---
\<CR>title:
\<CR>category:
\<CR>tags:
\<CR>---<CR>
```

- 다만 자동완성을 space로 마무리하는 경우에는 trailing space가 남아 있는 경우들이 있어서 꽤 성가신 경우들이 있습니다. 물론 그냥 backspace를 눌러주면 되는 것일 수도 있는데, 제 입장에서는 이게 몹시 성가시거든요.
- 대충 글을 1개 쓸 때마다 backspace를 한 번 더 눌러주기 위해서 5초를 낭비한다고 하면 12개를 쓰면 1분이, 1200개를 쓰면 100분 대략 영화 1편을 볼 수 있는 시간이 낭비되는 셈이므로 몹시 비효율적이군요(비효율적이지 않음). 뭐 아무튼 한 번 해결해 보도록 합시다.

## Solution

- [stackoverflow - preventing trailing whitespace when using vim abbreviations](https://stackoverflow.com/questions/11858927/preventing-trailing-whitespace-when-using-vim-abbreviations)를 읽어보면 해결할 수 있는 방법이 있습니다.
- 개념적으로 말하자면, 다음 순서로 해결되는 셈인데요.
  1. `getchar`: buffer에 있는 입력 값을 가져오고
  1. `nr2char`: 가져온 ascii 입력 값을 char로 변경해주고
  1. `~=`: 가져온 char의 pattern이 white space인 경우에는 `''`로 변경, 아닐 경우 그대로 리턴
  1. `<C-R>=function<CR>`: `function`을 실행하고 그 결과를 cursort 뒤에 집어넣어줌
- 아래를 사용하여 처리하면, 마지막에 무의미하게 들어오는 space를 삭제(정확히는, `''`로 변경)해줄 수 있습니다.

```vim
" 20221012 - frhyme
" :helpgrep Eatchar
" https://stackoverflow.com/questions/11858927/preventing-trailing-whitespace-when-using-vim-abbreviations
func Eatchar(pat)
    " 2022-10-14 (Fri) - frhyme
    " pat stands for pattern
    " nr2char: returns the character the the given ASCII value represents
    " =~ means matches with pattern
    " \s means any white space pattern
    let c = nr2char(getchar(0))
    return (c =~ a:pat) ? '' : c
endfunc

"====================================
" 2022-10-15 (Sat): sample iabbrev for removing trailing_space
" <CR> meand Carriabe Return
" <C-R>=, Ctrl + R= is used to insert the result of an expression at the
" cursor.
" <silent> means "it doesn't show any message while command is being executed
iabbrev <silent> __test_shortcut target_full_word<C-R>=Eatchar('\s')<CR>
```

## Wrap-up

- vim을 가장 사랑하는 이유는 오늘과 같이 직접 제 편집기를 제가 원하는 방향대로 수정할 수 있다는 데 있는 것 같습니다. 완벽하지는 않더라도 내 습관과 패턴에 맞도록 수정해 나가다 보면 개발에서의 생산성이 상당히 올라가거든요.
- 또한 vimscript를 사용하면서 change를 git을 사용해서 관리할 수 있기 때문에, 만약 제 편집기에 문제가 생겼을 경우 어떤 시점으로 복귀하는 것이 굉장히 효율적이죠. 따라서 개발 환경을 변경하는 것이 비교적 쉽습니다.
- 저는 모든 변경은 git에 의해서 관리되어야 한다고 생각하는 사람입니다. 다르게 말하면 애초에 git으로 관리할 수 있는 종류의 것이 아니라면 사용하고 싶지 않아요. 그래서 지금도 vim을 사용하고 있는 것 같습니다.

## Reference

- [stackoverflow - preventing trailing whitespace when using vim abbreviations](https://stackoverflow.com/questions/11858927/preventing-trailing-whitespace-when-using-vim-abbreviations)
- [what does \<C-R\>= means in Vim](https://stackoverflow.com/questions/10862457/what-does-c-r-means-in-vim)
