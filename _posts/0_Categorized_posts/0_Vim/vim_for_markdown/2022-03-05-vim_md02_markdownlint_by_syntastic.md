---
title: Syntastic을 이용하여 markdown lint
category: vim
tags: vim markdown syntastic markdownlint
---

## Syntastic을 이용하여 markdown lint

- 현재는 coc nvim을 이용해서 markdownlint를 사용하는데, 이거 말고 syntastic을 이용해서 markdownlint를 적용하는 것이 일관성 측면에서 더 좋지 않을까? 하는 생각이 들었습니다.
- 이유는 두 가지 정도인데요, 하나는 python, javascript 등 기존의lint를 모두 syntastic을 이용해서 해왔기 때문에, markdown에 대해서도 syntastic에 대해서 적용해줄 수 있다면 일관적으로 관리될 수 있겠다, 라는 것이 하나구요.
- 기존에 쓰고 있던 coc-markdownlint의 경우는 Error Msg가 아래 log창에 뜨는 형태가 아니고 해당 line에 cursor가 위치했을 때 표시되는 형태라서 조금 가독성이 떨어지는 느낌이 있었습니다.
- 그리고 coc-markdownlint의 경우 coc.nvim에 내에서 설치하고 제거해야 하고, 설정 파일도 세팅해줘야 하는데요, 이보다는 `.vimrc`내에 내용을 모두 작성해주는 것이 더 좋다고 생각되었구요.
- 따라서, Syntastic을 이용해서 markdown lint를 사용할 수 있도록 설정해줍니다.

### Uninstall markdownlint in Coc.nvim

- 기존에 설치한 coc-markdownlint를 제거합니다. 뭐, 제거하지 않아도 충돌이 발생하거나 하지는 않지만, 지워줍니다.

```sh
:CocList extensions
:CocUninstall coc-markdownlint
:CocList extensions
```

### Install markdownlint

- coc.nvim 류의 extension의 경우 모두 node 기반으로 개발되었지만, [github - markdownlint](https://github.com/markdownlint/markdownlint)의 경우는 ruby 기반으로 개발되었습니다.
- 따라서, `gem install`을 사용하여 `mdl`을 설치해줍니다. 설치하고 나면 `mdl a.md`와 같이 command line에서 markdown lint를 실행할 수 있습니다.

```sh
$ gem install mdl
Fetching tomlrb-2.0.1.gem
Fetching mixlib-shellout-3.2.5.gem
Fetching chef-utils-17.9.52.gem
Fetching mixlib-cli-2.1.8.gem
Fetching mdl-0.11.0.gem
Fetching mixlib-config-3.0.9.gem
Successfully installed chef-utils-17.9.52
Successfully installed mixlib-shellout-3.2.5
Successfully installed tomlrb-2.0.1
Successfully installed mixlib-config-3.0.9
Successfully installed mixlib-cli-2.1.8
Successfully installed mdl-0.11.0
Parsing documentation for chef-utils-17.9.52
Installing ri documentation for chef-utils-17.9.52
Parsing documentation for mixlib-shellout-3.2.5
Installing ri documentation for mixlib-shellout-3.2.5
Parsing documentation for tomlrb-2.0.1
Installing ri documentation for tomlrb-2.0.1
Parsing documentation for mixlib-config-3.0.9
Installing ri documentation for mixlib-config-3.0.9
Parsing documentation for mixlib-cli-2.1.8
Installing ri documentation for mixlib-cli-2.1.8
Parsing documentation for mdl-0.11.0
Installing ri documentation for mdl-0.11.0
Done installing documentation for chef-utils, mixlib-shellout, tomlrb, mixlib-config, mixlib-cli, mdl after 1 seconds
6 gems installed
```

- 이렇게 설치하고 나면, `.md` file을 열면 알아서 syntastic이 markdown lint를 구동해줍니다. 다른 언어들의 경우 다음과 같이 syntax_checker 값을 설정해주지 않으면, 작동이 안된 반면 markdown의 경우는 알아서 잘 해주는 것 같습니다.

```vim
let g:syntastic_python_checkers = ['flake8', 'pycodestyle']
let g:syntastic_javascript_checkers = ['eslint']
```

- 그래도 몇 가지 설정을 더 해주기 위해서, [github - vim-syntastic-checker.txt](https://github.com/vim-syntastic/syntastic/blob/master/doc/syntastic-checkers.txt)를 참조하여 아래의 설정을 `.vimrc`파일에 추가해줍니다.
- 대충 syntastic에서 markdown linter를 연결해주고, 불필요한 두 MDRule을 비활성화해줍니다. command line의 argument로 넘기듯 정해줘야 하는 것이 좀 어색하고 불편해 보이는군요. 이 부분은 coc-markdownlint가 더 깔끔하고 좋습니다만, 일단 뭐 추후에는 나아지겠죠.
- [github-markdownlint - configuration](https://github.com/markdownlint/markdownlint/blob/master/docs/configuration.md)을 참조하면 대략 어떻게 argument를 설정해줘야 하는지 알 수 있습니다.

```vim
" 20220305 - sng_hn.lee - syntax checker for markdown
" let g:syntastic_markdown_checker = 'markdownlint'
" gem install mdl before below line
let g:syntastic_markdown_mdl_exec = 'mdl'
" RESTRICT MD013 for Line length, for restriction use tilde(~)
" RESTRICT MD002 - First header should be a top level header, not adequate
let g:syntastic_markdown_mdl_args = "-r '~MD013','~MD002' "
```

## Wrap-up

- 사용자가 직접 rule을 정의하거나 세부적인 설정값(가령 max_length의 길이)등을 설정할 수도 있는 것으로 보이는데요. 일단 저는 더 필요하지 않아서 여기까지 하고 마무리합니다.

## Reference

- [github - markdownlint](https://github.com/markdownlint/markdownlint)
- [github - vim-syntastic-checker.txt](https://github.com/vim-syntastic/syntastic/blob/master/doc/syntastic-checkers.txt)
- [github - markdownlint - configuration](https://github.com/markdownlint/markdownlint/blob/master/docs/configuration.md)
