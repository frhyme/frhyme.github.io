---
title: 지킬에서 한글 폰트 바꾸는 방법
category: others
tags: jekyll font korean blog 
---

## intro

- 저는 맥에서 작업하니까 사파리 라는 웹브라우저를 씁니다. 사파리에서는 별 생각없었는데, 크롬에서는 한글 폰트가 별로 이쁘지 않은것 같아요. 
- 그래서 jekyll에서 폰트를 바꿔보려고 합니다. 

## 과정 

- 일단은 `main.scss`에 다음 코드를 추가하여 웹 폰트를 추가해주고 

```scss
@import url(https://fonts.googleapis.com/earlyaccess/nanumgothiccoding.css);//google web font added
```

- `_custom.scss`에서 폰트를 설정해줍니다. 
  - 이렇게하면 본문과 첫 페이지의 타이틀도 변경됩니다. 
  - 스타일을 변경할 때는 가능하면 `_custom.scss`에 추가해야 이후에도 관리가 편합니다. 

```scss
/* 글 본문 폰트 적용*/
body {
    font-family: 'Nanum Gothic Coding', serif;
}

/* 블로그 들어갔을때 글 제목 폰트 변경*/
div {
    article{
        h2{
            a{
                font-family: 'Nanum Gothic Coding', serif;
            }
        }
    }
}
/* 글 내의 타이틀 변경*/
article{
    div{
        header{
            h1{
                font-family: 'Nanum Gothic Coding', serif;
            }
        }
    }
}
article{
    div{
        section{
            h2{
                font-family: 'Nanum Gothic Coding', serif;
            }
        }
    }
}
div{
    article{
        div{
            a{
                font-family: 'Nanum Gothic Coding', serif;
            }
        }
    }
}
```

- 일단 이렇게 하면 포스트에서의 폰트는 바뀌었고, 이제 블로그 들어갔을때 보이는 제목만 바꿔주면 될듯
- 일단 이런식으로는 안 바뀌는데 흠

## 안전하지 않은 콘텐츠

- localhost에서 확인할 때는 잘 되는데, 직접 사이트에 들어가보면 폰트가 제대로 적용되어 있지 않은 것을 알 수 있어요. 
- 원인을 찾다보니 [여기서](https://rsec.kr/?p=137) 폰트를 http로 가져왔을 경우 안전하지 않은 콘텐츠로 포함되어서 적용되지 않는 일이 있는것 같아요
- 간단하게 `https`로 변경해줬더니 잘 되는 것 같습니다. 

```scss
@import url(https://fonts.googleapis.com/earlyaccess/nanumgothiccoding.css);//google web font added
```

## wrap-up

- 블로그를 볼때마다 좀 손볼게 많을것 같은데, 일단 나중에....헤헤

## reference

- [jekyll 블로그 폰트 바꾸기](http://hesu.github.io/programming/jekyll/2016/04/08/jekyllblog-adding-fonts.html)
- [github - Can I set the font and font size](https://github.com/mmistakes/minimal-mistakes/issues/1352)
- [HTTP, HTTPs (SSL) 로 혼합컨텐츠 (Mixed Content) 가 되었을 때 HTTPs 동작상태 확인](https://rsec.kr/?p=137)
