---
title: favicon 세팅하기. 
category: others
tags: jekyll favicon
---

## 문득 favicon을 세팅하고 싶어졌습니다. 

- 이제 와서 생각해보니, 왜인지는 모르겠지만...아무튼
- 그래서 구글 포토에서 막 사진을 찾다가, 사촌동생 고양이로 세팅하기로 했습니다. 
- <http://icoconvert.com> 같은 사이트에서 대충 jpg 파일을 ico 파일로 변환하구요. 

- _includes 폴더에 head.html 파일에 아래 한 줄을 추가해줍니다. 

```html
<!-- 아래 한 줄은 20180629에 추가한 파비콘-->
<link rel="icon" type="image/png" href="/assets/images/Favicon.ico">
```

- 잘 됩니다.

## reference

- <https://hanjungv.github.io/2017-04-24-1_ETC_livere/>
- <http://icoconvert.com>
