---
title: html - img tag
category: html 
tags: html a tag img image
---

## html - img tag

- `img` tag를 활용하여 image를 html 문서에 작성하는 방법을 정리하였습니다.
- `img` tag는 다음의 5가지 format을 허용합니다.
  - `JPEG`
  - `PNG`
  - `SVG`
  - `ICO`
  - `GIF`

```html
<!DOCTYPE html>
<html>
    <head>
        <meta charset="utf-8">
        <title>Test html for Image tag</title>
    </head>
    <body>
        <!-- image를 넣어 봤습니다-->
        <h3>Darth Vader img</h3>
        <img src="https://upload.wikimedia.org/wikipedia/en/thumb/7/76/Darth_Vader.jpg/220px-Darth_Vader.jpg">
        <br>
        
        <!-- gif도 넣을 수 있습니다-->
        <h3>Baby Yoda Gif</h3>
        <img src="https://64.media.tumblr.com/442513caac35229ccdd5e39fe822d6bf/f5c2981514e757fd-01/s500x750/a644d95d7d0936a19d19c5737e071711edfb489c.gifv">
        
        <!-- URL이 없으면 alt에 작성된 text를 보여줍니다.-->
        <h3>With Wrong src</h3>
        <img loading='lazy' src="wrongURL" alt="Sorry, Wrong URL">
        
        <!--Image에 hyperLink를 걸어줄 수도 있죠-->
        <h3>Google Logo with link</h3>
        <a href="https://google.com">
            <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/2/2f/Google_2015_logo.svg/368px-Google_2015_logo.svg.png"/>
        </a>
    </body>
</html>
```
