---
title: Vim - indentation guides
category: vim
tags: vim indent vundle plugin vi
---

## Vim - indentation guides

- VScode에는 [visualstudio - indent-rainbow](https://marketplace.visualstudio.com/items?itemName=oderwat.indent-rainbow)라는 indent 깊이에 따라 색깔을 다르게 처리해주는 plugin이 있습니다. python처럼 tab size가 4 space인 경우에는 그나마 구분이 확실한 반면, javascript에서처럼 tab size가 2인 경우에는 어디까지가 같은 코드인지 확인하는 게 쉽지 않습니다. 특히 이 과정에서 지옥의 callback function이 이어지면 더 indent가 헷갈리기 시작합니다.
- 그래서 vim에서도 해결방법이 있는지 확인해 보던 중 [stackexchange - how to add indentation guides lines](https://vi.stackexchange.com/questions/666/how-to-add-indentation-guides-lines)을 통해 몇 가지 해결법을 발견했습니다.

### set cursorcolumn

- `cursorcolumn`은 현재 cursor가 위치한 column 전체의 색을 변경해줍니다(사실 변경이라고 하기는 애매한데, 실제로 해보면 대충 무슨 말인지 알 수 있으실 거에요).
- `.vimrc` 파일 내에 아래 vim script를 추가해줍니다.
- 색깔을 변경하거나 하는 것도 가능하다고는 하는데, 이 경우 vim이 늦게 반응할 수 있다고 하여 설정하지 않습니다.
- 다만, 얘는 line의 가장 앞에 있을 때는 indentation 정도를 확인할 수 있지만, line을 작성하는 중에는 indentation 정도를 알 수 없어서, 한계가 있습니다.

```vim
set cursorcolumn
```

### Install vim-indent-guide

- [vim-indent-guides](https://github.com/nathanaelkane/vim-indent-guides)를 Vundle을 이용하여 설치하고 사용해 봅니다.
- Vundle에 아래 내용을 추가해줍니다.

```vim
Plugin 'nathanaelkane/vim-indent-guides'
```

- Install 을 해줍니다.

```vim
:PluginInstall
```

- 그리고 vim-indent-guids 활성화를 기본값으로 설정하기 위해 아래 설정을 `.vimrc` 에 추가해줍니다.

```vim
let g:indent_guides_enable_on_vim_startup = 1
```

- 색깔 변경들도 가능해 보이지만, 더 custom을 할 경우에는 너무 느려질 것 같아서 그만하겠습니다.

## Wrap-up

- 그래도...색이 그냥 gray scale인게 아쉽기는 하지만. 뭐 그냥 그러려니 하겠습니다 일단은.
- 다만, 오래 걸린다는 말도 그냥 어디서 들은 말일 뿐이므로 나중에 직접 변경해보도록 하겠습니다. 호호

## Reference

- [github - vim-indent-guides](https://github.com/nathanaelkane/vim-indent-guides)
- [stackexchange - how to add indentation guides lines](https://vi.stackexchange.com/questions/666/how-to-add-indentation-guides-lines)

