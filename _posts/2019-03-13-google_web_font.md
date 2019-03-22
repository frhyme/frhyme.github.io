---
title: Google web-font 적용하기. 
category: others
tags: web google font html 
---

## 왜 폰트를 변경해야 하나요. 

- 물론, 기존의 폰트도 적당히 괜찮습니다만, 제가 유난히 예쁜 것에 신경을 많이 쓰는 것 같습니다. 웹서비스를 만들다보면 결국 내가 이 웹서비스가 예쁘다는 생각을 하지 않으면 생각보다 진도가 더디게 나가는 일들이 있어요. 즉, 내가 이 웹서비스를 충분히 괜찮다고 생각해야 더 애정이 가고 하나라도 더 고치게 되는 일이 발생하죠. 
- 즉, 상대적으로 손쉽게 예쁘게 만들기 위해서는 우선, 폰트를 바꾸는 것이 좋습니다. 

## 웹폰트란? 

- 웹폰트란, 웹서비스를 방문하는 사람의 컴퓨터에 해당 폰트가 있냐 없냐와 상관없이 일관적인 경험을 제공하기 위해서, 웹에서 폰트관련 데이터를 가져와서, 렌더링해주는 것을 말합니다. d3.js처럼 다른 라이브러리를 쓸때 CDN을 통해서 가져오는 것과 동일하다고 말씀드릴 수 있겠네요. 
- 따라서 부트스트랩을 사용할 때처럼, 해당 소스를 가져오고, 적용해주면 끝납니다. 
 
## do it.

- 우선 [구글 웹폰트](https://fonts.google.com/?subset=korean&selection.family=Nanum+Gothic)로 들어갑니다. 
- 원하는 폰트를 선택하고 나면, 링크가 생성됩니다. 
- 대략 다음처럼 생성하고 진행하면 됩니다. 저는 일단 귀찮아서, 스타일로 넣었지만, CSS로 넣는 것이 나중을 생각하면 훨씬 편할 것 같네요.

```html
<html>
    <head>
        <link href="https://fonts.googleapis.com/css?family=Black+Han+Sans|Do+Hyeon|Jua|Nanum+Gothic|Sunflower:300" rel="stylesheet">
    </head>
    <body>
        <p style="font-family: 'Nanum Gothic', sans-serif;">
            나눔고딕입니다.
        </p>
        <p style="font-family: 'Sunflower', sans-serif;">
            선플라워입니다.
        </p>
        <p style="font-family: 'Do Hyeon', sans-serif;">
            도현체입니다.
        </p>
    </body>
</html>
```

## wrap-up

- 동시에 3개 이상의 폰트를 사용할 경우 웹페이지의 로딩이 현저히 느려질 수 있습니다. 
- 따라서, 가능하면 2개 이하로 조절하여 만드는 것이 좋아요. 당연한 이야기지만, 3개 이상을 쓰면 웹서비스 자체도 되게 너저분해질 수 있거든요.
- 또한, 영어 한글을 각각 적용하고 싶을때는 순서대로, 영어폰트 먼저 한글 폰트 먼저 적용하면 됩니다. 

```css
p {
    font-family: Roboto, Nanum Gothic;
}
```