---
title: vim - insert, command(normal) mode 별로 cursor 모양 변경하기
category: vim  
tags: vim cursor vimrc vi
---

## vim - insert, command mode 별로 cursor 모양 변경하기

- 기본 vim에서는 글을 입력하는 insert mode와 명령을 입력하는 command line에서의 cursor 모양이 동일합니다. 그런데 이 경우 가끔 insert 상황인 줄 알고 입력을 했는데 command line에 입력이 되거나 하는 식으로 실수를 하는 경우들이 있습니다. 현재 insert mode인지 command mode인지 정확하게 확인하려면 타이핑을 해서 입력이 되는지 확인해 보거나, 아니면 왼쪽 아래의 상태표시줄을 확인하면 되죠.
- 좀더 직관적으로(눈의 위치를 이동할 필요없이), 현재 mode를 확인하기 위해서 cursor의 모양 등을 변경해주려고 합니다.
이걸 변경하는 방법을 정리해봅니다.

## set cursorline, nocursorline 

- vim에서 `cursorline`은 cursor가 위치한 곳에 highlight를 넣어주는 것을 의미합니다. 반대로 `nocursorline`은 cursor가 위치한 곳의 highlight를 넣어주지 않는 것을 의미하구요. 간단하게 `.vimrc` 파일 내에 아래 명령어들을 각각 넣어주면 됩니다.
  - column에도 highlight를 하려면 `set cursorcolumn`을 하면 되는데, 아직은 별 필요 없는 것 같아요.
  - 또한, `highlight cursorline guifg=red`등의 command를 통해서 cursorline의 색깔도 바꿀 수 있다는 것 같은데요. 해당 내용은 본 포스팅의 범위를 넘어 가므로 더 진행하지 않겠습니다.

```vim 
set cursorline
set nocursorline
```

- 위 두 command들은 insert, command mode에 따라서 dynamic하게 변경되는 것이 아니라, 초기에 설정된 값이 계속 유지됩니다. 따라서, 이제 위 값들이 user 현재 사용하고 있는 mode에 따라서 변경되도록 해야겠죠.

## with autocmd 

- [autocmd](http://vimdoc.sourceforge.net/htmldoc/autocmd.html)는 사용자의 상황을 인식하고 자동으로 command가 실행되도록 하는 command입니다. 간단하게는 `au`라고 타이핑하기도 하죠.
- 사용자가 직접 event를 정의하는 것은 불가능하고(정확히는 제가 모르고요), 기정의되어 있는 event들을 가져와서 해당 event가 발생했을 때, 특정 command가 실행되도록 하려고 합니다. 
- 즉, insert mode에서는 cursorline을 활성화시키고, normal mode에서는 nocursorline을 활성화시키는 방향으로 진행하면 되겠죠. 그렇다면, mode가 전환되었을 때를 의미하는 event 가 정의되어 있어야 합니다.

### Event - InsertEnter, InsertLeave

- vim 에서 `:help InsertEnter`을 사용해서 InsertEnter Event에 대한 설명을 확인해 보면 다음과 같습니다. 대충 보면, insert mode 를 시작하기 전, 시작한 다음, 등의 event들이 이미 정의되어 있네요. 저는 `InsertEnter`, `InsertLeave` event를 이용하기로 합니다.

```plaintext
InsertEnter            Just before starting Insert mode.  Also for
                Replace mode and Virtual Replace mode.  The
                |v:insertmode| variable indicates the mode.
                Be careful not to do anything else that the
                user does not expect.
                The cursor is restored afterwards.  If you do
                not want that set |v:char| to a non-empty
                string.
                            *InsertLeavePre*
InsertLeavePre            Just before leaving Insert mode.  Also when
                using CTRL-O |i_CTRL-O|.  Be careful not to
                change mode or use `:normal`, it will likely
                cause trouble.
                            *InsertLeave*
InsertLeave            Just after leaving Insert mode.  Also when
                using CTRL-O |i_CTRL-O|.  But not for |i_CTRL-C|.
                            *MenuPopup*
```

- 따라서, `.vimrc`파일 내에 아래와 같은 내용을 작성했습니다. 
- `InsertEnter` Event가 발생하면 `set cursorline` 명령어를 활성화해주고, `InsertLeave` Event가 발생하면 `set nocursorline`을 활성화해준다는 이야기죠.
  - 중간의 `*`은 모든 파일에 대해서 적용한다, 라는 의미입니다. 만약 `*.c`로 변경해준다면, ".c"로 끝나는 파일들에 대해서만 해당 내용이 적용됩니다.

```vim
autocmd InsertEnter * set cul
autocmd InsertLeave * set nocul
```

- 가끔 autocmd 앞에 ":"을 붙여줘야 한다고 하는 경우들도 있습니다. [stackoverflow - why some commands in vim requires a colon while some dont](https://stackoverflow.com/questions/14051712/why-some-commands-in-vim-require-a-colon-while-some-dont)를 읽어 보면, colon을 붙이는 것은 vim에서는 상관없고, vi에서 사용하던 기법이라고 하네요.
- 사실 `autocmd InsertEnter * set cul`을 굳이 `.vimrc`에 집어넣지 않고, 직접 vim을 실행한 다음 comand line으로 들어가서 실행해도 됩니다. 이 때 command를 입력하기 위해서는 ":"을 쳐야 하는데요, 그 관행이 그대로 남아 있는 것으로 보입니다. 현재는 필요하지 않은 것으로 보입니다.

## Change cursor shape

- cursor의 모양을 변경하려면 다음을 `.vimrc`파일 내에 작성하면 됩니다.
- 아래를 적용하면 되긴 되는데...왜 아래의 방법이 작동하는지에 대해서는 아직 명확한 방법을 찾아내지 못했어요.

```vim
" 20211203 - change cursor shape for each insert, command mode
" Ps = 0  -> blinking block.
" Ps = 1  -> blinking block (default).
" Ps = 2  -> steady block.
" Ps = 3  -> blinking underline.
" Ps = 4  -> steady underline.
" Ps = 5  -> blinking bar (xterm).
" Ps = 6  -> steady bar (xterm).
" t_SI: Start Insert mode
" t_EI: End Insert mode

let &t_SI = "\<ESC>[6 q"
let &t_EI = "\<ESC>[2 q"
```

- [vimdoc](http://vimdoc.sourceforge.net/htmldoc/term.html#termcap-cursor-shape)을 확인해 보면, `&t_SI`는 vim에서 "Start Insert mode"가 실행될 때, vim이 실행된 terminal로 보내는 sequence로 보입니다. 사실 terminal과 vim은 별개의 것이므로, vim에서 발생한 변동상황에 대해서 vim은 terimal로 신호를 보내는 것으로 보입니다.
- cursor의 모양은 vim에 의존적인 것이 아니라, 사용자가 사용하는 terminal에서 정의하는 것으로 보입니다. 따라서, vim에서 직접 변경할 수는 없고, terminal에서 직접 커서 모양을 변경해야 하는 것이죠. 다만, vim에서 어떤 변경점이 발생했을 때, 이를 terminal로 신호로 보낸다면, 그 신호 내에 cursor를 변경하는 모양까지 같이 씌워서 넘겨버리는 되는 것 같아요. 아마 위의 코드가 그런 내용이 아닐까 싶습니다.

## wrap-up

- 메커니즘에 대해서는 파악이 덜 되었지만, 어쨌든 제가 원하는 대로 바꾸기는 했습니다. 다만 아쉬움이 남으므로...나중에는 보충을 해야할것 같아요.

## Reference 

- [stackoverflow - how to change the cursor between normal and insert modes](https://stackoverflow.com/questions/6488683/how-to-change-the-cursor-between-normal-and-insert-modes-in-vim)
- [Vim Control Sequence Examples](https://ttssh2.osdn.jp/manual/4/en/usage/tips/vim.html)
