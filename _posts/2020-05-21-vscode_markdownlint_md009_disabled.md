---
title: [vs-code] markdown linkt - MD009 해제하기
category: vs-code
tags: markdown vs-code markdownlint
---

## Intro

- markdownlint에서 MD009는 다음을 말합니다.
- 줄바꿈 앞에 whitespace가 있으면 이 rule이 발생(trigger)되고, "야 고쳐"라는 말이 뜬다는 이야기죠.
  
```plaintext
MD009 - Trailing spaces
Tags: whitespace

Aliases: no-trailing-spaces

Parameters: br_spaces, list_item_empty_lines, strict (number; default 2, boolean; default false, boolean; default false)

This rule is triggered on any lines that end with unexpected whitespace. To fix this, remove the trailing space from the end of the line.
```

- 왜 trailing space를 쓰면 안되는지에 대해서는 [stackexchange - Why is trailing whitespace a big deal?](https://softwareengineering.stackexchange.com/questions/121555/why-is-trailing-whitespace-a-big-deal)를 참고하시면 됩니다.

## MD009 disable

- 이유는 알겠고 대부분의 문서에서 그렇게 해야 한다는 것도 동의를 하지만, 마크다운에서도 그래야 하는지는 잘 모르겠습니다.
- 그냥 글을 쓰는 것인데 매번 글을 작성 중에 끝에 노란색 줄이 뜨는 것이 여간 성가시는 게 아니에요. 
- 그래서 비활성화를 하기로 했습니다.
- `preference > setting > extenstion > markdownlint`에서, 다음을 `setting.json`을 여시고, 다음을 입력해주시면 됩니다.

```json
"markdownlint.config": {
    "MD009": false, // 20200521: 끝에 스페이스 있는 거, 마크다운에서는 별로 신경쓰고 싶지 않음.
},
```

## reference 

- [vscode - markdownlint](https://github.com/DavidAnson/vscode-markdownlint)
