---
title: CSS - Box Shadow
category: css
tags: css shadow html
---

## CSS - Box Shadow

- 요소의 글 상자 만큼의 `box-shadow`를 만드는 방법을 정리합니다.
- `box-shadow`는 `offset_x, offset_y, blur_radius, spread_radius, color`로 정의됩니다.
  - `offset_x`: box_shadow의 위치 양수(오른쪽), 음수(왼쪽)
  - `offset_y`: box_shadow의 위치 양수(아래쪽), 음수(위쪽)
  - `blur_radius`: 그림자를 얼마나 뿌옇게 뿌려질지 정합니다. 
  이 값이 0px이면 뿌옇지 않고 선명하고, 커질수록 조금씩 영역이 넓어지면서 뿌옇게 그려지죠
  - `spread_radius`: 그림자의 크기를 결정해줍니다. 커질수록 그림 자체가 커지죠.
  - `color`: 그림자의 색을 말합니다.
- 가령 요소 `p`에 대해서 다음처럼 정의되어 있다면
  - 초록색의 그림자를 왼쪽 위 방향으로 하나 넣고, 
  - 빨간색의 그림자를 오른쪽 아래의 방향으로 `blur_raduis`를 20px로, `spread_radius`를 30px로 넣는다는 의미를 가집니다.

```css
p {
    box-shadow: -20px -20px green, 20px 20px 20px 30px red;
}
```

## Example - Box Shadow

- Box Shadow를 사용하여 간단한 예제를 만들어 봤습니다.

```html
<!DOCTYPE html>
<html>
    <head>
        <meta charset="utf-8"/>
        <style>
            p {
                width: 200px;
                height: 200px;
                background-color: black;
                border: 20px solid blue;
                color: white;
                text-align: center;
                vertical-align: middle;
                padding: 5px;
                margin: 60px
            }
            .box_shadow1 {
                /*
                box-shadow offset_x, offset_y, blur_radius, spread_radius, color
                - offset_x: box_shadow의 위치 양수(오른쪽), 음수(왼쪽)
                - offset_y: box_shadow의 위치 양수(아래쪽), 음수(위쪽)
                - blur_radius: 그림자를 얼마나 뿌옇게 뿌려질지 정합니다. 
                이 값이 0px이면 뿌옇지 않고 선명하고, 커질수록 조금씩 영역이 넓어지면서 뿌옇게 그려지죠
                - spread_radius: 그림자의 크기를 결정해줍니다. 커질수록 그림 자체가 커지죠.
                - color: 그림자의 색을 말합니다.
                아래처럼 두 가지 이상의 box shadow를 그려줄수도 있습니다.
                */
                box-shadow: -20px -20px green, 20px 20px 20px 30px red;
            }
        </style>
    </head>
    <body>
        <p class="box_shadow1">
            This is paragraph with Box-Shadow
        </p>
    </body>
</html>
```
