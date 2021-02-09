---
title: CSS - backface visiblity
category: css
tags: css visibility
---

## CSS - backface visiblity

- `backface-visibility`는 "뒷면이 보이냐"라는 말이죠. 기본적인 웹 디자인에서는 사용할 일이 없지만, 2D 혹은 3D를 구현하고 이를 회전시키거나 할때 뒷면이 유효하도록 할 것인지 아닌지를 설정하는 것을 말합니다.
- 다음과 같은 간단한 html에서 `backface_visible` class에 속한 요소는 뒷면이 보이도록 하고, `backface_hidden` class에 속한 요소는 뒷면이 보이지 않도록 한다고 해보겠습니다.

```html
<!DOCTYPE html>
<html>
    <head>
        <meta charset="utf-8"/>
        <link rel="stylesheet" href="style.css" />
    </head>
    <body>
        <div class="backface_visible">
            backface_visible
        </div>
        <div class="backface_hidden">
            backface_hidden
        </div>
    </body>
</html>
```

- `style.css`는 다음과 같이 정의합니다.
  - div 요소들에게 너비, 높이를 정해주고 색깔도 정해준다.
  - 요소 위에 마우스를 올렸을 때(hover) 와이축으로 180도 뒤집어서 뒷면이 보이도록 해준다.
  - `backface_visible` class는 `backface-visibility`를 `visible`로 설정하여 뒷면이 보이도록 설정해주고
  - `backface_hidden` class는 hidden으로 설정하여 뒷면이 보이지 않도록 설정해줍니다.

```css
div {
    width: 200px;
    height: 200px;
    color: white;
    font-size: 20px;
}
div:hover {
    transform: rotateY(180deg); 
}

.backface_visible {
    backface-visibility: visible;
    background-color: blue;
    
}

.backface_hidden {
    backface-visibility: hidden;
    background-color: purple;
}
```

- 그리고 html 요소를 브라우저에 띄워서 마우스를 각 요소에 올려보면 어떻게 다른지 확인할 수 있습니다.
