---
title: Vim 22 - File 별로 Tab Size 다르게 하기
category: vim
tags: vim tab filetype javascript autocmd
--- 

## Vim 22 - File 별로 Tab Size 다르게 하기

- Vim에서 Python 개발만 진행하다가, 최근에는 Javascrip도 조금씩 쓰고 있습니다.
- python의 경우 tab이 4 space인 반면 JS의 경우는 2 space죠. js에서 2 space가 표준이 된 배경에는 "callback hell"이 있다고 생각됩니다. 들여쓰기를 연속해서 하게 되는 deep nesting이 자주 발생하게 되는데, 이 때 만약 tab이 4 space일 경우 모니터를 넘어가는 일이 생길 수도 있으니까요.
- 저의 경우는 tab보다는 space를 선호하고, 2 space보다는 4 space를 선호합니다. 4 space가 가독성이 훨씬 좋다고 생각하거든요. 하지만, 표준이 있다면 표준을 따릅니다.
- 아무튼 Javascript에서 indentation을 2 space로 변경하려면 다음과 같이 처리하면 됩니다.

```vim
" 20220228 - javascript tab indentation 2
autocmd FileType javascript setlocal ts=2 sts=2 sw=2
```

- `autocmd`: auto command의 약자로, vim 내에서 발생할 수 있는 기정의된 event들에 대해서 특정한 command 발동되도록 하는 명령어입니다.
- `autocmd FileType <file_type_name>`: 어떤 FileType에 대해서 Event를 지정할지 정의합니다. 저는 javascript에 대해서 지정해 줄 것이므로, `javascript` 라고 작성했습니다. 처음에는 `*.js`의 형태로 regex pattern으로 써줘야 하는 건가 싶었는데 위와 같이 언어명을 그대로 써줘야 하는 것으로 보입니다. 다만, 어떤 언어들에 대해서 기정의되어 있는지 확인하고 싶은데, 어떻게 확인해야 할지 모르겠네요.
- `setlocal`: 일반적인 `set`이 global한 영역에서 적용왼다면, `setlocal`의 경우는 현재 buffer에만 잠시 적용되고, 다른 파일을 열면 다시 global에 지정된 값으로 변경된다는 느낌입니다. 즉, '지역변수'라고 생각하시면 될 것 같네요. 
  - `:set`을 사용하면 전역 변수에 할당된 값을 알 수 있고, `:setlocal`을 사용하면 현재 지역(현재 파일)에 정의된 값을 알 수 있습니다.

### Detecting Filetype

- 처음에는 `*.js`와 같이 파일명의 패턴에 대해서 설정값을 바꿔주도록 하는 것인지 알았는데요, `javascript`처럼 filetype을 정해주는 것으로 보입니다.
- 현재 file의 filetype은 `:set filetype?`으로 확인할 수 있습니다. '.md'파일의 경우는 "markdown"으로 확인되네요. 즉, 이미 현재 shell의 어떤 곳에선가 '.md로 종료되는 파일은 filetype을 markdown으로 처리한다'와 같은 명령이 어디선가 실행되는 것으로 보입니다. 어디서 실행되는지 확인하려고 했는데, 못 찾았습니다.
- filetype을 결정해주는 command는 대략 다음과 같습니다.
  - `autocmd`: 특정 이벤트가 발생했을 때, 자동으로 발동되도록 하는 command 
  - `BufNewFile`: 새 파일을 열어서 편집하기 시작할 때(BufNewFile), 
  - `BufRead'`: 파일을 읽었을 때(BufRead)
  - `*.abcd` filename에 대한 pattern, 그냥 다음처럼 바로 넣어주면 그게 filename에 대한 pattern으로 먹히는 것 같습니다.
  - `set filetype=ALPHABET`: 현재 파일의 filetype을 "ALPHABET"라고 한다는 의미입니다. 미리 정해져 있던 것이 아니고, 제가 임의로 작성해줬습니다.
- 아래 커맨드를 `.vimrc` 파일 내에 작성해준 다음 `set filetype?` 을 실행해 보면 filetype이 제가 정의한 대로 잘 변경된 것을 알 수 있습니다.

```vim
autocmd BufNewFile,BufRead *.abcd set filetype=ALPHABET
``` 

## Wrap-up

- 일단은 markdown, javascript에 대해서만 tab을 2 space로 변경해보았습니다. 이후에 또 필요하면 나머지는 그때 변경하려고요.
- 최근에 개발 환경을 vscode 에서 vim으로 완전히 변경하였습니다. 기존에는 vscode에서 잡아주던 설정들을 이제는 vim에서 직접 잡아야 하므로 꽤 번거로움도 있긴 하지만, 그래도 덕분에 배우는 부분도 많은 것 같습니다.

## Reference

- [File별 들여쓰기 설정하기](https://seorenn.blogspot.com/2011/10/vim.html)
- [reddit - javascript - why is twospace tab indent becoming the standard](https://www.reddit.com/r/javascript/comments/5rjrcy/why_is_twospace_tab_indent_becoming_the_standard/)
- [들여쓰기 100년 전쟁, Tab vs Space, 2글자 vs 4글자](https://repo.yona.io/doortts/blog/post/268)
- [Detecting Filetypes](https://learnvimscriptthehardway.stevelosh.com/chapters/44.html)
- [stackoverflow - autocmd check filename in vim](https://stackoverflow.com/questions/6009698/autocmd-check-filename-in-vim)
