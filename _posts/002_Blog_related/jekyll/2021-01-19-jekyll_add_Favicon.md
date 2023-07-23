---
title: jekyll에 favicon을 추가해줍니다.
category: blog
tags: blog jekyll favicon
---

## jekyll에 favicon을 추가해줍니다

- favicon없이 `jekyll serve`를 통해 로컬에 블로그를 띄우면, 다음과 같은 사소한 오류가 뜹니다.

```plaintext
ERROR `/favicon.ico' not found.
```

- 별거 아닌데 귀찮아서 일단 해결해봅니다. 
- `/assets` 폴더 내에 `favicon.ico` 파일을 넣어줍니다.
- `_includes` 폴더 내에 `head.html`의 위쪽에 아래 내용을 추가해줍니다.

```html
<!-- 20210119 ADD favicon-->
<link rel="icon" type="image/png" href="/assets/favicon.ico">
```

## Wrap-up

- 저의 경우 jekyll theme로 [minimal mistake](https://mmistakes.github.io/minimal-mistakes/)를 사용하고 있습니다. theme마다 적용 방법이 조금씩 다릅니다.

## Reference

- [jekyll 사이트 favicon 추가하기](https://min9nim.github.io/2018/03/add-favicon/)
