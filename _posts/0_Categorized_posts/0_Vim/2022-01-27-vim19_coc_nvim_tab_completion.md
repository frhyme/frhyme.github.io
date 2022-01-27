---
title: Vim 19 - Coc.nvim - Trigger completion by Tab
category: vim 
tags: vim coc.nvim vi completion tab
---

## Trigger completion by Tab

- tab으로 Completion이 실행되고, 다음 completion item으로 넘어갈 수 있도록 설정합니.

### Add shell script to .vimrc 

- 아래와 같은 vim script를 `.vimrc` 파일에 작성해주는 방법이 있습니다. [github - coc.nvrim - completion with sources](https://github.com/neoclide/coc.nvim/wiki/Completion-with-sources)에 작성되어 있는 내용인데요.
- 내용을 해석하기 위해 필요한 내용들은 대략 다음과 같네요.
  - `inoremap`: insert mode에서, non recursive하게 mapping 
  - `map <silent><expr> A B`: `<silent>`, `<expr>`은 모두 option이고, A key를 B로 변경해준다는 말이죠.
    - `<silent>`: 입력되는 key가 명령 표시줄에 표시되지 않도록 한다는 것인데, 사실 우리는 insert mode에서 사용하기 때문에 딱히 이 옵션이 유효해 보이지는 않습니다.
    - `<expr>`: 단순히 특정 key를 mapping하는 것이 아니라, 상황에 따라 동적으로 key가 mapping되도록 설정하겠다는 것을 의미합니다. 즉, popup이 띄워진 상황인지 아닌지에 따라 발동되는 key가 달라지도록 메커니즘을 만들어야 하므로, 이 옵션을 넣어줘야 합니다.
  - `<SID>`: 이는 특정 script 파일 내에 존재하는 namespace에 접근하기 위한 목적이다, 라는 것을 명시하는 건데요. 아래 `check_back_space` 함수 앞에는 `s:`라는 부분이 작성되어 있죠. 이는 이는 이 함수의 유효 범위를 정하는 것이구요, 여기서 정의한 범위 밖에서는 해당 함수가 유효하지 않다는 것을 의미합니다. 반대로 이 함수에 접근하기 위해서는 `<SID>`를 작성하고, 함수 이름을 붙여 줘야 하는 것으로 보입니다.
  - `pumvisible()`: popup 창의 발생 유무를 의미합니다. 발생했다면 True를, 아니라면 False를 리턴하는 것으로 보입니다.
  - `<C-n>`: vim에서는 기본적으로 ctrl + n 을 사용하여 completion mode를 발생시킬 수 있습니다. 또한, 이미 popup이 띄워진 상황이라면, next item으로 navigation하는 용도로 사용되죠.
  - `col('.')`: 현재 cursor의 column number, 즉 대충 왼쪽에서 몇 번째 떨어져 있는지를 리턴합니다.
  - `getline('.')`: 현재 줄을 string으로 리턴합니다.
  - `condition ? Do_A: Do_B`: tenary operator로 `condition`이 True이면 Do_A를 False면 Do_B를 하는 것으로 보입니다.
  - `=~ '\s'`: pattern matching을 의미하는 operator이며, `\s`는 white space를 의미합니다. 즉, 기존 cursor의 위치 왼쪽 글자가 공백인지를 묻는 것이죠.

```vim
" use <tab> for trigger completion and navigate to the next complete item
function! s:check_back_space() abort
  let col = col('.') - 1
  return !col || getline('.')[col - 1]  =~ '\s'
endfunction

inoremap <silent><expr> <Tab>
      \ pumvisible() ? "\<C-n>" :
      \ <SID>check_back_space() ? "\<Tab>" :
      \ coc#refresh()
```

- 이걸 기반으로 해석해보자면 다음과 같습니다. 편하게 python code로 써보겠습니다.

```python
if "tab이 눌렸으면":
    if "이미 popup이 띄워져 있는 상황이라면":
        do "Popup 창 내에서 navigation하는 Ctrl + n 버튼을 누름"
    else:
        if "tab이 눌리기 직전 char가 공백이거나, 문자열 제일 앞이라면":
            do "공백인 경우에 tab이 눌렸다면 자동완성이 아니므로, tab 문자를 입력"
        else:
            do "이전 char가 공백이 아니므로, coc#refresh()를 실행"  
else:
    "tab이 눌리지 않았으므로 상관없음"
```

- 하지만, 사실 이렇게 하지말고 그냥 SuperTab이라는 플러그인을 설치해버리면 더 간단한 문제이기는 합니다.

### Install Supertab

- install supertab: 기본적으로 tab은 tab character를 입력하기 위한 목적으로 사용되지만, supertab을 이용하면, 대략 다음의 형태로 변경해줍니다.

```python
if "문자를 입력하다가 tab을 누르면": 
    "문자를 입력중이었으므로 함수 자동완성기능을 실행함"
else:
    "tab character를 입력함"
```

- 한번 설치해 보면 금방 무슨 말인줄 알 수 있는데요. 저는 Vundle을 이용하여 설치하였습니다.
- `.vimrc` 파일에 아래 내용을 추가해줍니다. 이미 Vundle을 사용하고 있다면, 정확히는 `Plugin 'ervandew/supertab'`만 추가해주면 되죠.
- vim에서 `:PluginInstall`을 사용하여 플러그인들을 다 설치해줍니다.

```bash
set rtp+=~/.vim/bundle/Vundle.vim
call vundle#begin()
" 20220112 - Install Supertab for Tab completion in Jedi
" without supertab, when popup was shown and you type tab key, inseter tab
" character. 
Plugin 'ervandew/supertab'
call vundle#end()            " required
```

- 이렇게 설치하고 나면, 앞서 만든 vim script와 동일한 메커니즘이 세팅됩니다. 하하.
- 그래서, 그렇다면 supertab에도 저렇게 간단한 코드만 있는거 아니야? 라는 생각에 `~/.vim/bundle/supertab/plugin/supertab.vim`이라는 파일을 열어봤는데요 하하하하. 훨씬 복잡하게 설계되어 있네요. 그렇다면 저는 supertab으로 넘어가도록 하겠씁니다. 하하하 더 긴 코드니까 더 좋은게 있지 않을까요 하하하.

## Wrap-up

- 흠, 처음에는 supertab을 설치해서 사용하면 된다고 생각했는데요, 정작 vimscript를 이해하고 나니, 저렇게 쓰는 것이 더 좋아보입니다. 찾아보면 좀 더 좋은 설정 들이 있지 않을까? 하는 생각도 들고요 하하.
- 다만....저는 처음에는 tab으로 completion 을 Triggering시키려고 했던 것이 아니라, tab으로 결정(원래 enter가 하는 것)을 하려고 했는데요, 흠...찾아봐야 할 것 같습니다.

## Reference

- [vim의 키 맵 설정 팁](https://soooprmx.com/vim%EC%9D%98-%ED%82%A4-%EB%A7%B5-%EC%84%A4%EC%A0%95-%ED%8C%81/)
- [vim 플러그인의 키맵과 함수 이름](https://soooprmx.com/vim%EC%9D%98-%ED%94%8C%EB%9F%AC%EA%B7%B8%EC%9D%B8-%ED%82%A4%EB%A7%B5%EA%B3%BC-%EC%8A%A4%ED%81%AC%EB%A6%BD%ED%8A%B8-%ED%95%A8%EC%88%98/)
- [StackExchange - Usage of the =~ operator](https://vi.stackexchange.com/questions/6265/usage-of-the-operator)
