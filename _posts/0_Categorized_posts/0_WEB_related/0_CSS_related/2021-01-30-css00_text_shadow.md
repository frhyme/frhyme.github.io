---
title: css property - text shadow 
category: css
tags: css css_property text_shadow
---

## css property - text shadow 

- css를 사용해서 text의 그림자를 생성할 수 있습니다.

```css
p {
    /*
    - x: shadow가 x선 상에서 얼마나 벗어나는가
    - y: shadow가 y선 상에서 얼마나 벗어나는가
    - radius: 값이 클 수록 그림자가 넓고 
    - color; 색깔
    */
   text-shadow: x y radius color;
}
```

- 다음처럼 작성해서 사용합니다. 

```css
p {
    /*
    - 다음 처럼 2개 이상의 text shadow를 넣을 수도 있습니다.
    */
    text-shadow: 10px 10px 2px red, 1px 5px 2px green, -1px -1px 3px blue;
}
```