---
title: MarkdownLint - MD033 - no inline html
category: MarkdownLint
tags: markdown markdownlint tab
---

## MarkdownLint - MD033 - no inline html

- MD033은 markdown document 내에 html 요소를 그대로 집어넣는 경우 발생합니다.

> This rule is triggered whenever raw HTML is used in a markdown document

- 즉, 아래처럼 html 요소를 backtick 없이 그대로 마크다운 문서 내에 집어넣는 경우 발생하는 에러죠.

```html
<b>Inline HTML header</b>
```

- 다만, 왜 허용되지 않는지는 잘 모르겠습니다. 그냥 pure한 마크다운 문서를 만들기 위해서 html 요소를 완전히 배체하자는 것인지 아니면 마크다운 문법 내에 html 요소가 혼재되어 있을 경우 제대로 렌더링하지 못하는 오류가 발생하는 것인지, 어느 쪽인지 모르겠지만 아무튼 안된다고 하는 군요.

## Allow Element

- 사실 그냥 Warning 정도의 메세지와 노란 색 줄이 그어져 있는 것이 좀 보기 귀찮은 것이지, 무시해도 되기는 합니다.
- 그러나, 영 거슬린다면, `setting.json`에 다음 내용을 작성해서 집어넣으면 됩니다. 아래 code는 `<b>`에 대해서 MD033을 허용하지 않겠다는 이야기죠.

```json
"markdownlint.config": {
    "MD033":{
        // 20210119: 테스트를 위해 작성
        "allowed_elements": ["b"]
    }
},
```

## Reference

- [markdown lint rules MD033 - no inline html](https://github.com/updownpress/markdown-lint/blob/master/rules/033-no-inline-html.md)
