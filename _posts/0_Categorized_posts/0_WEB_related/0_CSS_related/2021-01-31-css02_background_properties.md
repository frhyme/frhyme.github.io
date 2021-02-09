---
title: CSS - background properties
category: css
tags: css background
---

## CSS - background properties

- css의 background의 다양한 설정값을 변경합니다.
  - `background-image`: 요소의 background를 image로 설정합니다.
    - 값을 `linear-gradient(red, blue)`으로 설정하면 gradient로 예쁘게 설정됩니다. 호호.
  - `background-size`: background의 크기를 설정합니다.
  - `background-repeat`: background의 이미지가 요소의 전체 image보다 작은 경우에 반복해서 넣어줄지 설정합니다. 
  - `background-attachment`: 웹 페이지가 스크롤을 내릴 만큼 긴 경우에, scroll에 따라 이미지가 따라 내려갈지 아니면 그냥 위에 숨겨질지를 정합니다.
  - `background-position`: background의 위치를 정합니다.
  - `background-clip`: background가 요소의 어떤 영역까지 커버할지 정합니다. 가령, padding까지 포함해서 그릴지, content만 그릴지 등에 대해서 정한다는 이야기죠.

```css
div {
    /*
    background-image: image로 background를 설정해줍니다.
    */
    background-image: url(https://images.unsplash.com/photo-1528207776546-365bb710ee93?ixid=MXwxMjA3fDB8MHxzZWFyY2h8MXx8cGFuY2FrZXN8ZW58MHx8MHw%3D&ixlib=rb-1.2.1&w=1000&q=80);
    
    /*
    background-size: image의 width, height를 설정합니다.
    - 200px 300px: width, height를 설정합니다.
    - contain: 요소보다 작지만 가장 크게 만들어줍니다.
    즉 현재는 div 요소 내에 있으므로 div보다는 작지만(padding을 유지하면서) 가장 크게
    - cover: 요소보다 크지만 가장 작게 만들어줍니다.
    */
    background-size: cover;
    /* 
    background-repeat: 
    image의 크기가 요소의 크기보다 작은 경우 몇번 반복할지 정합니다.
    - no-repeat: 반복하지 않는다.
    - repeat: 반복한다.
    - repeat-x: x 축으로 반복한다.
    - repeat-y: y 축으로 반복한다.
    */
    background-repeat: no-repeat;
    /*
    background-attachment: 
    - fixed: scroll을 내려도 그림이 창에 고정되어서 계속 보입니다.
    - scroll: scroll에 따라 그림이 보이고 안 보이고 합니다.
    */
    background-attachment: fixed;
    /*
    background-position: image의 위치
    */
    background-position: center;
    /*
    background-clip: background를 어디에 그려질지 정합니다.
    - content-box: content가 위치한 곳에만 그려준다.
    - border-box: border까지 포함해서 그려준다.
    - padding-box: padding까지 포함해서 그려준다.
    */
    background-clip: content-box;
}
```

- 예제 html 문서로 다음처럼 정리하였습니다.

```html
<!DOCTYPE html>
<html>
    <head>
        <meta charset="utf-8"/>
        <style>
            div {
                width: 800px;
                height: 600px;
                padding: 20px;
                border: 10px solid black;
                /*
                background-image: image로 background를 설정해줍니다.
                */
                background-image: url(https://images.unsplash.com/photo-1528207776546-365bb710ee93?ixid=MXwxMjA3fDB8MHxzZWFyY2h8MXx8cGFuY2FrZXN8ZW58MHx8MHw%3D&ixlib=rb-1.2.1&w=1000&q=80);
                
                /*
                background-size: image의 width, height를 설정합니다.
                - 200px 300px: width, height를 설정합니다.
                - contain: 요소보다 작지만 가장 크게 만들어줍니다.
                즉 현재는 div 요소 내에 있으므로 div보다는 작지만(padding을 유지하면서) 가장 크게
                - cover: 요소보다 크지만 가장 작게 만들어줍니다.
                */
                background-size: cover;
                /* 
                background-repeat: 
                image의 크기가 요소의 크기보다 작은 경우 몇번 반복할지 정합니다.
                - no-repeat: 반복하지 않는다.
                - repeat: 반복한다.
                - repeat-x: x 축으로 반복한다.
                - repeat-y: y 축으로 반복한다.
                */
                background-repeat: no-repeat;
                /*
                background-attachment: 
                - fixed: scroll을 내려도 그림이 창에 고정되어서 계속 보입니다.
                - scroll: scroll에 따라 그림이 보이고 안 보이고 합니다.
                */
                background-attachment: fixed;
                /*
                background-position: image의 위치
                */
                background-position: center;
                /*
                background-clip: background를 어디에 그려질지 정합니다.
                - content-box: content가 위치한 곳에만 그려준다.
                - border-box: border까지 포함해서 그려준다.
                - padding-box: padding까지 포함해서 그려준다.
                */
                background-clip: content-box;
            }
            p {
                width: 50%;
                height: 200px;
                padding: 5px;
                border: 5px solid black;
                color: white;
            }
            .bg_Color_red {
                /*
                background-color
                - inherit: parent 요소의 색을 그대로 사용하게 됩니다.
                - initial: default의 색을 사용하게 됩니다.
                - rgb: (Red, Green, Blue)의 색 조합으로 색을 정의합니다. 
                - rgba: (Red, Green, Blue, Alpha) RGB + alpha(투명도)의 색 조합으로 정의합니다.
                */
                background-color: rgba(255, 0, 0, 0.5);
            }
            .bg_Gradient_img {
                /*
                색깔을 gradient로 쭉 정렬해줍니다.
                */
                background-image: linear-gradient(red, blue, black, green);
            }
        </style>
    </head>
    <body>
        <div>
            <p class="bg_Color_red">
                This is paragraph with Background Color Red
            </p>
            <p class="bg_Gradient_img">
                This is paragraph with Background Gradient Image
            </p>
        </div>
    </body>
</html>
```
