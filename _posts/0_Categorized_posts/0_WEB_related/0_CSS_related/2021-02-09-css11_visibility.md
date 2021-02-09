---
title: CSS - visibility
category: css
tags: css visibility html
---

## CSS - visibility

- visibility의 값을 수정하여, 상황에 따라 보이도록 혹은 보이지 않도록 할 수 있습니다.
- 기본적으로는 visible하지만, 마우스를 올리면(hover) 보이지 않도록 설정합니다.

```css
.hoverVisible {
    width: 200px;
    height: 200px;
    color: white;
    background-color: blue;
    font-size: 20px;
    visibility: visible;
}

.hoverVisible:hover {
    visibility: hidden;
}
```

- 렌더링해보면, 마우스를 올리면 보여지지 않는 것을 알 수 있습니다.

```html
<!DOCTYPE html>
<html>
    <head>
        <meta charset="utf-8"/>
        <link rel="stylesheet" href="style.css" />
    </head>
    <body>
        <div class="hoverVisible">
            hover visible
        </div>
    </body>
</html>
```
