---
title: html - Google Font 연결하기
category: html
tags: html font css
---

## html - Google Font 연결하기

- [Google - Font](https://fonts.google.com/)에 존재하는 다양한 font를 가져와서, html 문서에 적용할 수 있습니다.
- local computer에 font를 다운 받은 다음 적용하는 것이 아니라, 웹피이지를 열 때 직접 [Google - Font](https://fonts.google.com/)에서 font를 가져오는 것이죠. 그냥 클라우드처럼 쓴다고 생각하셔도 문제가 없습니다.
- [Google - Font](https://fonts.google.com/)에서 원하는 font를 눌러서 보면 다음 2가지가 오른편에 뜨는 것을 볼 수 있습니다.

```html
<!-- 이 부분은 html head 부분에 넣어주고-->
<link rel="preconnect" href="https://fonts.gstatic.com">
<link href="https://fonts.googleapis.com/css2?family=Noto+Sans+KR:wght@100&display=swap" rel="stylesheet">
```

- `font-family` attribute에 "Yeon Sung"으로 값을 넣어주면 됩니다.

```css
#p1 {
    font-family: 'Yeon Sung', cursive;
}
```

- 전체 html 문서를 작성하면 다음과 같이 되겠죠.

```html
<!DOCTYPE html>
<html>
    <head>
        <meta charset="utf-8">
        <title>Test html for Google Font</title>
        <!--
        preconnect
        - preconnect는 보통 "한 Domain에서 여러 리소스를 요청하는 상황"에서 연결을 미리 맺어두도록 설정하는 것을 말합니다.
        - 다음처럼 여러 font를 동시에 사용하는 경우에는 preconnect를 맺어둠으로써, 시간을 효율적으로 사용하는 것이 좋죠.    
        -->
        <link rel="preconnect" href="https://fonts.gstatic.com">
        <link href="https://fonts.googleapis.com/css2?family=Yeon+Sung&display=swap" rel="stylesheet">
        <link href="https://fonts.googleapis.com/css2?family=Noto+Sans+KR:wght@100&display=swap" rel="stylesheet">
        <link href="https://fonts.googleapis.com/css2?family=Gugi&display=swap" rel="stylesheet">
        <style>
            #p1 {
                font-family: 'Yeon Sung', cursive;
            }
            #p2 {
                font-family: 'Noto Sans KR', sans-serif;
            }
            #p3 {
                font-family: 'Gugi', cursive;
            }
        </style>
    </head>
    <body>
        <p id="p1"> 첫번째 패러그래프입니다.</p>
        <p id="p2"> 첫번째 패러그래프입니다.</p>
        <p id="p3"> 첫번째 패러그래프입니다.</p>
    </body>
</html>
```

- 다음처럼 CSS 문서 내에서 google font를 다운받아서 적용해줄 수 있습니다.

```html
<!DOCTYPE html>
<html>
    <head>
        <meta charset="utf-8">
        <title>Test html for Google Font</title>
        
        <style>
            /*
            CSS 내에 다음처럼 작성해 줄 수도 있습니다.
            */
            @import url('https://fonts.googleapis.com/css2?family=Yeon+Sung&display=swap');
            #p1 {
                font-family: 'Yeon Sung', cursive;
            }
        </style>
    </head>
    <body>
        <p id="p1"> 첫번째 패러그래프입니다.</p>
    </body>
</html>
```