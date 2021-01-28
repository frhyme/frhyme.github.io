---
title: feather icon을 이용해서, 웹에서 예쁜 아이콘 사용하기.
category: others
tags: web html feathericon icon
---

## what is feathericon?? 

- 일단은, 처음에는 웹페이지를 만들때 보통 그냥 텍스트 중심으로 만들게 됩니다. 물론, 텍스트만으로도 충분히 예쁘게 만들 수 있지만, 썩 성에 차지는 않아요. 
- 다행히도, 이 아름다운 세상에는 icon 조차 오픈소스로 풀려 있는 경우가 많습니다. [feathericon](https://feathericons.com/)이 그 아름다움을 지원합니다 하하핫. 
- 아무튼, 이 아이콘들을 이용하면, 웹페이지를 생각보다 훨씬 예쁘게 만들 수 있습니다. 

## do it 

- [documentation](https://github.com/feathericons/feather#feather)에 가면 자세한 사용법들이 정리되어 있습니다. 
    - 아래와 같이 html 문서의 head부분에서 script로 소스를 가져오고, 
    - 필요한 부분에 tag의 속성으로 `data-feather="circle"`을 집어넣고, 
    - 맨 아랫줄에 `feather.replace()`라는 부분을 집어넣어줍니다. 
- 저의 경우는 앞 뒤 부분은 모두 `layout.html`에 집어넣고, 사용합니다. 

```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <title></title>
    <!--CDN으로부터 feather-icon들을 가져옴-->
    <script src="https://unpkg.com/feather-icons"></script>
  </head>
  <body>

    <!-- example icon -->
    <i data-feather="circle"></i>

    <!--맨 아랫줄에 이 라인을 집어넣으면 html페이지를 만든 다음 해당 부분은 icon으로 변경해줌-->
    <script>
      feather.replace()
    </script>
  </body>
</html>
```


## wrap-up

- 필요한 아이콘들을 편하게 사용할 수 있습니다 하하핳.