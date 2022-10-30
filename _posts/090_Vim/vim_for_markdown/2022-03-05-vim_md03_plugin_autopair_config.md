---
title: Vim - plugin AutoPair Config 수정
category: vim
tags: vim markdown plugin autopair
---

## Vim - plugin AutoPair Config 수정

- 저는 markdown을 포함한 대부분의 문서 파일을 vim을 이용해서 편집합니다.
- 이 때 괄호 등을 쓸 때가 많은데요. 매번 bracket을 양쪽 다 입력하는 것이 꽤나 번거로운 일이므로, [github - auto-pairs](https://github.com/jiangmiao/auto-pairs)라는 플러그인을 사용하고 있습니다.
- 다만, filetype별로 활성화가 필요한 자동완성 pair 가 다르기 때문에, 다음 내용을 `.vimrc` 파일 내에 작성하여 filetype 별로 활성화되는 auto pair를 다르게 설정해줍니다.
- backtick, single quote의 경우 1개로 감싸지는 경우도 있고 3개로 감싸지는 경우도 있습니다. 이 두 개가 모두 존재하니까, markdown 내에서 꼬이는 경우들이 있어서,  해당 부분을 제외해주었습니다.

```vim
"=======================================================
" 20220305 - Plugin AutoPair Config
" filetype별로 설정을 변경함.
" (default) let g:AutoPairs = {'(':')', '[':']', '{':'}',"'":"'",'"':'"', "`":"`", '```':'```', '"""':'"""', "'''":"'''"}
autocmd FileType vim let g:AutoPairs = {}
autocmd FileType markdown let g:AutoPairs = {'(':')', '[':']', '{':'}',"'":"'",'"':'"', '```':'```', '"""':'"""', "'''":"'''"}
```

## Wrap-up

- vim script를 좀더 잘 쓴다면 제가 제 용도에 맞게 직접 vim script를 써서 진행해 줄 수 있을텐데, 그정도는 아니라서 일단은 plugin을 그대로 사용합니다. 다만, 나중에는 제가 직접 작성할 수 있으면 좋겠네요.
- `.vimrc` 파일 내에 점차 많은 내용들이 쌓이면서 점차 vim의 구동이 느려지는 것 같은 느낌이 있네요.

## Reference

[github - auto-pairs](https://github.com/jiangmiao/auto-pairs)
