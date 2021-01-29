---
title: html - audio tag
category: html
tags: html audio tag
---

## html - audio tag

- html 문서 내에 audio tag를 넣는 방법을 정리하였습니다.

```html
<!DOCTYPE html>
<html>
    <head>
        <meta charset="utf-8">
        <title>Test html for Audio tag</title>
    </head>
    <body>
        <h3> Test Audio </h3>
        <!--
            다음의 attribute를 사용해서 다양하게 설정해 줄 수 있습니다.
            - controls: 음악 재생버튼 등 제어판이 표시됩니다.
            - muted: 음악을 시작할 때 초기 음량이 0으로 설정됩니다.
            - autoplay: 페이지가 로딩되면 바로 음악이 시작됩니다.
            - loop: 
        -->
        <audio controls muted src="https://www.learningcontainer.com/wp-content/uploads/2020/02/Kalimba.mp3"></audio>
    </body>
</html>
```