---
title: vim11 - Insert mode에서 backspace 가 먹히지 않을때
category: vim
tags: vim vi backspace 
---

## vim11 - Insert mode에서 backspace 가 먹히지 않을때

- 종종 vi, vim에서 Insert Mode에서 character를 지울 때 backspace 가 먹히지 않을 때가 있습니다.

```bash
$ set backspace=indent,eol,start
```

- 그냥 한번에 하고 싶으면 다음을 사용하면 되죠.

```bash
$ echo "set backspace=indent,eol,start" >> ~/.vimrc
```

## wrap-up

- 만약 이렇게 했는데도 잘 안된다면 그냥 nvim으로 가버릴까봐요.

## Reference 

- [ShellHacks - Vi/Vim – Backspace Not Working](https://www.shellhacks.com/vi-vim-backspace-not-working/)
- [stackoverflow - backspace key not working in vim vi](https://stackoverflow.com/questions/11560201/backspace-key-not-working-in-vim-vi)
