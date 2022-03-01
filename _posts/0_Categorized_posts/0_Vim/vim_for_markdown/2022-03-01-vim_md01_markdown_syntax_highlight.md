---
title: Vim21 - Markdown Code block syntax highlight
category: vim
tags: vim vi markdown syntax highlight
--- 

## Vim21 - Markdown Code block syntax highlight

- `~/.vimrc` file 내에 아래 내용을 추가하면, python, vim, json code block에 대해서 markdown 내에서 syntax highlight이 지원됩니다.
  - `g:`: global을 의미하며, 아래 설정을 전역적(globally)으로 설정해준다는 것을 의미합니다.

```vim
let g:markdown_fenced_languages = ['python', 'vim', 'json']
```

- 다만, markdown 관련해서 다른 plugin을 설치해준 적이 없는데도 불구하고, 알아서 위 설정 값이 먹혀서 syntax highlighting이 되는 것이 좀 신기하네요.
- 이제 어떤 이유로 설정되는지를 대략 파악해 보도록 합니다.

## why it works?

- `/usr/local/share` 경로에서 'markdown_fenced_languages'가 존재하는 file을 검색해봅니다.

```sh
cd /usr/local/share
grep -rn '.' -e 'g:markdown_fenced_languages'    
```

- 검색해보면 `/usr/local/share/nvim/runtime/syntax` 경로에 `g:markdown_fenced_languages` 관련 script들이 존재하는 것을 볼 수 있습니다.
- 아마도, 여기서 뭔가 변경되는 것이 아닌가...싶기는 한데요. 확실하게는 모르겠군요.
- 과거에 neovim을 설치했을 때 함께 가져온 것이 아닌가? 하고 추측해 봅니다만, 일단은 이걸 파고들어가는 것은 중요하지 않으므로 대략 그럴 것이다, 정도로만 요약하고 넘어가도록 합니다.

## wrap-up

- [github - vim markdown](https://github.com/preservim/vim-markdown)을 설치하면 다음처럼 다른 방식으로 markdown_fenced_languages를 설정하는 것으로 보입니다. 뭐, 아무튼 일단은 vim-markdown을 설치할 필요가 없고 이미 syntax가 먹혀서 넘어가지만 혹시 변경이 필요하면 나중에 설치해보도록 하겠습니다.

```vim
let g:vim_markdown_fenced_languages = ['csharp=cs']
```

## Reference

- [github - tpope - vim markdown](https://github.com/tpope/vim-markdown)
