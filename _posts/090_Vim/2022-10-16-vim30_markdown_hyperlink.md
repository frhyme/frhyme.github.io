---
title: vim - markdown - hyperlink
category: vim
tags: vi vim markdown hyperlink netrw
---

## vim - markdown - hyperlink

- 저는 markdown을 vim을 이용해서 편집합니다. 따라서 mouse를 거의 사용하지 않는데요.
- markdown 에서 다음의 형태로 reference를 넣고, 만약 해당 경로의 페이지에 방문하고 싶을 경우 일반적인 IDE에서는 마우스 클릭만으로 충분합니다. 그러나, vim에서는 마우스가 먹지 않죠.

```markdown
[stackoverflow - follow link in vim with markdown syntax](https://stackoverflow.com/questions/26919972/follow-link-in-vim-with-markdown-syntax)
```

- 결론부터 말하면, url 위에서 `gx`를 typing하면 해당 경로로 바로 이동할 수 있습니다. 외부 웹브라우저가 열리면서 해당 페이지가 열리죠.
- "Netrw"는 vim에 기본으로 내장되어 있는 file explorer로 보입니다.

## Wrap-up

- 동작 방식이 좀 궁금하기는 한데 그냥 궁금해 하지 않으려고요 하하.

## Reference

- [stackoverflow - follow link in vim with markdown syntax](https://stackoverflow.com/questions/26919972/follow-link-in-vim-with-markdown-syntax)
