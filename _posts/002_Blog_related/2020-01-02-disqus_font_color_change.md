---
title: 만약 jekyll의 disqus의 색깔이 잘 보이지 않는다면.
category: others
tags: jekyll disqus blog
---

## disqus의 색깔이 하얗게 보입니다

- 요즘 블로그를 전반적으로 손을 보고 있습니다. 광고를 달고, 광고의 위치를 바꾸고, 폰트 크기를 수정하는 등의 일을 하고 있죠. 
- 뻔한 이야기를 하나 하자면, 웬만해서는 잘 만들어진 Minimal mistakes와 같은 테마를 고른 뒤에, 본인의 스타일대로 바꾸는 일을 하지 않으시길 간곡히 부탁드립니다. 처음 만들었을 때는 사소한 튜링들을 막 하고 싶지만, 그건 이후에 아주 큰 레거시가 될 수 있습니다. 아무튼 참고하시구요. 

### 우선, 뭐가 문제일까?

- 블로그의 테마를 수정하려면 보통 `_config.yml`에서 아래 부분을 변경해줍니다. 이 부분만 바뀌면 되는 것이죠.

```yml
minimal_mistakes_skin    : "contrast" # "air", "aqua", "contrast", "dark", "dirt", "neon", "mint", "plum", "sunrise"
```

- 다만, 현재 제 테마에서 배경이 하얀색인데, disqus에서도 글이 하얗게 보일 때가 있는 것이죠. 즉, 글이 하나도 보이지 않습니다. 
- 처음에는 이 부분이 제가 과거에 `sass`부분을 마음대로 변경해서 이 부분에 문제가 생긴 것이라고 생각했씁니다. 그래서, 아예 지금 테마를 다 덮어씌워버려야 하는 것일까? 라고 생각했죠.
- 그러나, 그렇지 않습니다. disqus는 다른 서비스에서 제공하는 부분으로 코드를 붙여넣은 것이 다이거든요. 즉, 제 코드로 수정해야 하는 것이 아니라, disqus로 가서 거기에 설정된 것을 바꿔야 한다는 것이죠.

### solve it

- 따라서, disqus의 설정으로 들어가서, Basic -> Appearance -> Color Scheme에서 값을 바꿉니다. 원래는 그냥 "Auto"로 되어 있습니다. 이는, 본문의 텍스트 색상에 따라서 알아서 변경하는 것으로 보이는데요, 지금 저의 경우처럼 제대로 되지 않는 것은, 자동설정에 문제가 있다는 말인 것이죠.
- 따라서, 저는 그냥 `Auto`로 설정하지 않고, 색을 직접 수동으로 설정해주었습니다. 그렇게 변경하고 나니, 이제 글이 선명하게 잘 보이는군요.

## wrap-up

- 디스커스의 색깔은 disqus 서비스로 들어가서 직접 바꿔야 한다! SaaS!