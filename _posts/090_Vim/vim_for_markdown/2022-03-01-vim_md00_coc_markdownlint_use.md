---
title: Use coc markdownlint
category: vim
tags: vim markdown markdownlint lint
--- 

## Use coc markdownlint

- Vim에서 markdown을 작성 중에 오류 혹은 표준을 잡기 위해서 lint를 사용하려고 합니다. vscode에서는 extension을 설치하면 되지만, vim에서는 이게 조금은 번거롭죠.
- 저는 [coc.nvim](https://github.com/neoclide/coc.nvim)을 사용하고 있어서, 아래 명령어를 사용하여 [github - coc-markdownlint](https://github.com/fannheyward/coc-markdownlint)를 설치하였습니다.

```vim
:CocInstall markdownlint
```

- 그리고, `:CocConfig`을 통해 `coc-setting.json` file에 아래 내용을 추가하여 markdownlint에 대한 설정을 정해줍니다.
  - `onChange`: file 내에 수정이 발생하면 발동되도록
  - `onSave`: file이 저장되었을 때 발동되도록
  - `config`: linting rule을 유효/무효 할 것인지(MD013의 경우 한 줄에 들어가는 문자의 수 에 대한 rule인데, link가 있는 경우에도 길다고 판정하여 무효화였습니다)
- `:CocConfig`을 실행하면, '~/.vim/coc-settings.json' 파일을 수정하게 됩니다. 즉, 그냥 이 파일로 바로 가서 수정해도 동일합니다.

```json
"markdownlint.onChange": false, 
"markdownlint.onSave": true, 
"markdownlint.config": {
    "MD013": false
}
```

## wrap-up

- 간단히 coc.nvim을 사용하여 markdownlint extension을 설치하였습니다.
- 점차coc.nvim의 생태계가 커지는 느낌이 드네요. 다르게 말하면 의존도가 높아지는 느낌이긴 합니다만, 뭐 그저 유지보수가 잘 되기만 기도해보겠습니다 하하하

## Reference

- [github - coc-markdownlint](https://github.com/fannheyward/coc-markdownlint)
