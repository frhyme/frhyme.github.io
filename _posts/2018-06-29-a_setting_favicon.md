---
title: favicon 세팅하기. 
category: others
tags: jekyll favicon
---

## 문득 favicon을 세팅하고 싶어졌습니다. 

- 이제 와서 생각해보니, 왜인지는 모르겠지만...아무튼
- 그래서 구글 포토에서 막 사진을 찾다가, 사촌동생 고양이로 세팅하기로 했습니다. 
- <http://icoconvert.com> 같은 사이트에서 대충 jpg 파일을 ico 파일로 변환하구요. 

## head.html 수정 

- _includes 폴더에 head.html 파일에 아래 한 줄을 추가해줍니다. 

```html
<!-- 아래 한 줄은 20180629에 추가한 파비콘-->
<link rel="icon" type="image/png" href="/assets/images/Favicon.ico">
```

- 참고로 지킬의 경우 적용되는 시점이 좀 느립니다. 참고하세요. 

## config 파일 수정 수정 

- 제가 적용한 테마에서는 config 파일에 favicon 부분이 없어요. 하지만, [이분 블로그](https://moon9342.github.io/jekyll-struct) 에서는 config에서 파비콘을 적용하더라구요. 
- 만약 본인의 config 파일에 파비콘 세팅하는 부분이 있으면 적용하시면 될 것 같네요. 


## reference

- <https://hanjungv.github.io/2017-04-24-1_ETC_livere/>
- <http://icoconvert.com>
