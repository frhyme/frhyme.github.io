---
title: Vim Auto closing html tag
category: html
tags: vi vim html tag
---

## Auto Closing html tag

- html 문서를 작성할 때는 tag를 닫아주는 게 가장 귀찮습니다. 아마 학부 때는 자동으로 닫아주는 게 있다는 사실을 모르고 하나하나 모두 타이핑 해줬던 것으로 기억하는데요.
- [github - vim-closetag](https://github.com/alvan/vim-closetag)를 사용하면 vim에서도 자동으로 닫히는 tag를 쓸 수 있습니다.
- 저는 Vundle을 이용하여 설치할 것이기 때문에, `.vimrc` file 내에 아래 내용을 추가합니다.
- 그리고 `:PluginInstall`을 이용하여 설치해줍니다.

```vim
" 20220310 - sng_hn.lee - vim html auto closetag
Plugin 'alvan/vim-closetag'
```

## Wrap-up

- [github - mattn -emmet-vim](https://github.com/mattn/emmet-vim)도 괜찮아 보이는데, 사용법을 잘 모르겠네요. 다음에 공부해서 정리해보도록 하겠습니다.

## Reference

- [github - mattn -emmet-vim](https://github.com/mattn/emmet-vim)
- [stackexchange - how to generate closing tags for html](https://vi.stackexchange.com/questions/9672/how-to-generate-closing-tags-for-html)
- [github - alvan -vimclosetag](https://github.com/alvan/vim-closetag)
