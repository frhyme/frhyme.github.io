---
title: CSS - linear gradient
category: css
tags: css background
---

## CSS - linear gradient

- css를 사용해서 html 요소의 background를 linear gradient로 설정합니다.
- `linear-gradient(angle, color1 color_stop_line, ... , colorN color_stop_line)`으로 정의해줍니다.
  - `angle`: gradient를 그려주는 방향을 결정해줍니다. `0deg`일 경우에는 위쪽으로, `90deg`일 경우에는 오른쪽으로 그려주죠.
  - `color1 color_stop_lineN`: `color1`는 어떤 색으로 그릴지 선택하고, `color_stop_line`은 이 색의 정지선을 정해줍니다. 
    - 가령 `red 50%`라고 정한다면, 빨간색으로 전체 길이의 50% 까지 그린 다음 이후에 gradient를 그려준다는 이야기죠. 따라서, 여러 색으로 gradient를 그릴 때, 당연히 `color_stop_lineN`의 값은 오름차순으로 커져야 됩니다.

```css
.gradient0 {
    /*
    linear_gradient(angle, color1 color_stop_line, ... , colorN color_stop_line)
    angle: linear gradient의 방향을 정합니다.
    - to top(0deg): 위로 gradient
    - to right(90deg): 오른쪽으로 gradient
    - to bottom(180deg): 아래쪽으로 gradient
    - to right(270deg): 왼쪽으로 gradient
    (color color_stop_line)
    - red 30%: 는 빨간색을 30%까지 계속 그려준다는 말을 말합니다. 즉, 전체 길이의 30% 이후부터 gradient가 시작되는 것이죠.
    - white 90%:  또한 90%까지 gradient를 그리고 또 그뒤에는 그냥 white 그려지죠.
    */
    background: linear-gradient(to top, red 30%, white 90%);
}
```

- 간단하게 html 문서로 다음과 같이 작성해봤습니다.

```html
<!DOCTYPE html>
<html>
    <head>
        <meta charset="utf-8"/>
        <style>
            p {
                width: 400px;
                height: 500px;
            }
            .gradient0 {
                /*
                linear_gradient(angle, color1 color_stop_line, ... , colorN color_stop_line)
                angle: linear gradient의 방향을 정합니다.
                - to top(0deg): 위로 gradient
                - to right(90deg): 오른쪽으로 gradient
                - to bottom(180deg): 아래쪽으로 gradient
                - to right(270deg): 왼쪽으로 gradient
                (color color_stop_line)
                - red 30%: 는 빨간색을 30%까지 계속 그려준다는 말을 말합니다. 즉, 전체 길이의 30% 이후부터 gradient가 시작되는 것이죠.
                - white 90%:  또한 90%까지 gradient를 그리고 또 그뒤에는 그냥 white 그려지죠.
                */
                background: linear-gradient(to top, red 30%, white 90%);
            }
        </style>
    </head>
    <body>
        <div>
            <p class="gradient0">
                This is paragraph with Background Gradient Image
            </p>
        </div>
    </body>
</html>
```

## Wrap-up

- 여러 gradient의 투명도를 조절해서 한번에 그릴 수 있나 싶었는데, 이건 일단은 잘 안되는 것 같네요. 나중에 더 자세히 알아보겠습니다.
