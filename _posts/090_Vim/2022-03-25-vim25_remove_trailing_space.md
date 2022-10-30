---
title: Vim25 - Marking and Deleting Trailing Space
category: vim
tags: vim space highlight autocmd BufWritePre vi
---

## Vim25 - Marking and Deleting Trailing Space

- code나 글을 작성하다 보면 습관적으로 마지막에 space를 넣어주는 못된 습관이 있습니다. 이렇게 마지막에 위치한 white space를 "Trailing space"라고 부릅니다. trail이 "끌다"라는 의미를 가지기 때문에, 한글로 번역한다면 "질질 끌리는 공백" 정도로 표현할 수 있겠네요.
- 보통 Code를 작성할 때, Trailing Space는 지양하는 것이 좋죠. 이유는 [stackexchange - why is trailing whitespace a big deal](https://softwareengineering.stackexchange.com/questions/121555/why-is-trailing-whitespace-a-big-deal)을 읽어 보시면 되는데요. 대충 다음과 같습니다.

1. End 버튼을 통해 line의 끝에 갈 때, 끝의 문자에 Cursor가 위치하게 되는 것이 아니라, 공백에 위치하게 되기에 cursor 움직임이 일관적이지 않게 된다는 것
1. Git과 같은 VCS들은 Line을 기반으로 변동사항을 체크하는데, line의 끝에 Trailing Space만 추가되었어도 해당 Line은 변경되었다고 인지합니다. 따라서, trailing space가 추가될 경우 Code 관리에 부정적인 영향을 줄 수 있으므로 Code Commit시에 제외되도록 처해주는 것이 좋습니다.
1. multiline string 등을 표현할 때, trailing space가 포함되어 있을 경우 debug 가 어려울 수 있다는 점
1. 무의미하게 char 용량을 1개 더 차지한다는 것.

## Vim에서 Trailing Space를 표시하고, 저장 시 삭제해주기

- 저는 기본 IDE로 vim 을 사용하고 있기 때문에, `.vimrc`에 아래 내용을 추가하여 해당 문제를 해결하였습니다.
- Trailing Space가 문서 내에 표시되는 경우 바로 해당 문자의 background가 "darkred"로 표시되도록 설정하였습니다.
- 그리고 주요 몇 타입의 문서에 대해서 해당 문서를 저장할 때, 문서 끝의 Trailing Space가 모두 삭제되도록 처리하였습니다.

```vim
"=============================================================
" 2022.03.25 - sng_hn.lee - trailing space 색깔 변경
" ctermbg = for console version vim
" guibg = for guit version vim
" 따라서,console에서만 사용하는 경우 guibg를 따로 명시하지 않아도 상관이 없다.
highlight TrailingSpace ctermbg=darkred guibg=darkred
match TrailingSpace /\s\+$/
" 2022.03.25 - sng_hn.lee - 저장할 때, 끝에 공백 삭제.
" BufWritePre: 전체 buffer를 file에 쓰기 전 을 의미하는 Event
autocmd FileType markdown,python,html,javascript autocmd BufWritePre <buffer> :%s/\s\+$//e
```

## Wrap-up

- 제가 몇 달 전까지만 해도 주로 사용하던 IDE는 VScode였습니다. VScode에는 굉장히 다양한 plugin이 존재하고 Trailing Space를 삭제해주는 Plugin도 존재해서 비교적 효율적으로 개발을 했었다고 생각했었습니다.
- 다만, vim을 사용하게 되면서, "오히려 좀 더 세부적으로 customizing할 수 있는 건 vim이 아닌가?"라는 생각들을 자주 학게 되는 것 같아요. code 몇 줄을 추가해주면 되는 거니까요.

## Reference

- [[vim] 라인 끝에 있는 공백문자 하이라이트, 저장시 제거 (highlight trailing spaces, remove trailing spaces when save)](https://bloodguy.tistory.com/entry/vim-%EB%9D%BC%EC%9D%B8-%EB%81%9D%EC%97%90-%EC%9E%88%EB%8A%94-%EA%B3%B5%EB%B0%B1%EB%AC%B8%EC%9E%90-%ED%95%98%EC%9D%B4%EB%9D%BC%EC%9D%B4%ED%8A%B8-%EC%A0%80%EC%9E%A5%EC%8B%9C-%EC%A0%9C%EA%B1%B0-highlight-trailing-spaces-remove-trailing-spaces-when-save)
- [stackoverflow - what is the difference between cterm color and gui color](https://stackoverflow.com/questions/60590376/what-is-the-difference-between-cterm-color-and-gui-color)
- [stackexchange - why is trailing whitespace a big deal](https://softwareengineering.stackexchange.com/questions/121555/why-is-trailing-whitespace-a-big-deal)
