---
title: 지킬에서 한글 폰트 바꾸는 방법
category: 
tags:
---

## intro

- 저는 맥에서 작업하니까 사파리 라는 웹브라우저를 씁니다. 
- 사파리에서는 별 생각없었는데, 크롬에서는 한글 폰트가 별로 이쁘지 않은것 같아요. 
- 그래서 jekyll에서 폰트를 바꿔보려고 합니다. 

- 일단은 `main.scss`에 다음 코드를 추가하여 웹 폰트를 추가해주고 

```scss
@import url(http://fonts.googleapis.com/earlyaccess/nanumgothiccoding.css);//google web font added
```

- `_custom.scss`에서 폰트를 설정해준다. 

```scss
body {
    font-family: Georgia, 'Nanum Gothic Coding', serif;
}
```

- 일단 이렇게 하면 포스트에서의 폰트는 바뀌었고, 이제 블로그 들어갔을때 보이는 제목만 바꿔주면 될듯

## wrap-up



## reference

- <http://hesu.github.io/programming/jekyll/2016/04/08/jekyllblog-adding-fonts.html>
- <https://github.com/mmistakes/minimal-mistakes/issues/1352>