---
title: CSS - position property
category: css
tags: css position 
---

## CSS - position property

### 문서 내 작성된 순서에 따라 배치되는 경우

- position property의 다음 세 값은 문서 내에서 작성된 순서에 따라서 배치됩니다. 이미 현재의 요소 위에 다른 요소가 있다면, 그 요소의 아래에 그려지게 된다는 이야기죠.
  - `position: static`: default입니다. 따로 position에 값을 정해주지 않았을 때 `static`으로 넘어가게 되는데요, 만약 html 문서 내에 모든 요소가 static이라면 다 순서대로 왼쪽에서 오른쪽으로, 위에서 아래로 다다다닥 붙어서 생성됩니다. 
  - `position: relative`: 다른 요소들과의 상대적인 위치를 계산합니다. 가령 아래와 같이 정의해 준다면, "위에서 정의된 마지가 static 요소로부터 `20px` 떨어진 위치에 그려준다는 이야기죠.
    
    ```css
    .relative_pos {
        position: relative;
        top: 20px;
    }
    ```

  - `position: sticky`: 요소를 문서에 작성된 순서에 따라 배치합니다. 그러나, 얘는 스크롤을 내리면 위쪽에 그대로 붙어 있다는 점이 다르죠. 그리고 부모 요소로부터 영향을 받습니다.

### 문서의 순서와 상관없는 경우

- 다음 두 position value는 다른 요소들과의 위치를 고려하지 않습니다. 또 부모로부터도 영향을 받지 않죠.
  - `position: absolute`: 부모 요소의 위치로부터 절대적인 위치를 정합니다. 가령 부모 좌표가 (5, 5)이고, absolute인 요소의 좌표가 (10, 10)이 된다면, (15, 15)인 위치에 해당 요소가 위치하게 되죠. 
  - `position: fixed`: 부모 요소의 위치와 상관없이, 항상 (0, 0)으로부터(Browser Viewpoint로부터) 좌표를 계산합니다. 심지어 스크롤을 내려도 항상 고정된 위치에 존재하죠. absolute의 경우는 스크롤을 내리면 사라질 수도 있습니다.

## Wrap-up

- 사실 지금 에제에서는 parent 요소를 그냥 static으로 해두었지만, 부모 요소를 absolute로 설정한 상태에서는 조금씩 달라집니다. 가령 부모 요소가 absolute인 상태에서는 child 요소가 absolute인 경우 부모 요소를 벗어나지 못하는 상황에서 위치가 결정됩니다.

---

## Example

- position에 따른 차이를 확인할 수 있는 문서를 아래와 같이 만들었습니다.
- 아래 문서를 렌더링 해보면 어떤 차이가 있는지 명확하게 아실 수 있을 것 같습니다.

```html
<!DOCTYPE html>
<html>
    <head>
        <meta charset="utf-8"/>
        <style>
            p {
                width: 300px;
                height: 75px;
                padding: 0px;
                margin: 0px;
                border: 3px solid black;
                font-size: 25px;
                text-align: center;
                vertical-align: middle;
                color:white;
                background-color: blue;
                opacity: 0.5;
            }
            .relative_pos {
                /*
                position: relative
                - 문서의 순서상 위에 그려진 요소로부터 위에서 20px 떨어진 위치에 배치해줍니다.
                */
                position: relative;
                top: 20px;
                background-color: green;
            }
            .sticky_pos {
                /*
                position: sticky
                - 문서의 순서상 위에 그려진 요소로부터 위에서 0px, 왼쪽에서 150px
                떨어진 위치에 배치해줍니다.
                */
                position: sticky;
                top: 0px;
                left: 150px;
                background-color: orange;
            }
            
            .fixed_pos {
                /*
                position: fixed
                - webbrowser 상에서 절대저인 위치에 위치해줍니다.
                */
                position: fixed;
                top: 200px;
                left: 500px;
                background-color: purple;
            }
            .absolute_pos {
                /*
                position: absolute:
                절대적인 위치로 요소를 위치시킬 수 있습니다.
                */
                position: absolute;
                top: 300px;
                left: 400px;
                background-color: red;
            }
        </style>
    </head>
    <body>
        <div>
            <p>p without pos(static)</p>
            <p>p without pos(static)</p>
            <p class="sticky_pos">p with Sticky Pos</p>
            <p class="relative_pos">p with Relative Pos</p>
            <p class="absolute_pos">p with Absolute Pos</p>
            <p class="relative_pos">p with Relative Pos</p>
            <p class="relative_pos">p with Relative Pos</p>
            <p class="sticky_pos">p with Sticky Pos</p>
            <p class="relative_pos">p with Relative Pos</p>
            <p>p without pos(static)</p>
            <p class="relative_pos">p with Relative Pos</p>
            <p class="sticky_pos">p with Sticky Pos</p>
            <p class="relative_pos">p with Relative Pos</p>
            <p class="relative_pos">p with Relative Pos</p>
            <p class="relative_pos">p with Relative Pos</p>
            <p class="fixed_pos">p with Fixed Pos</p>
            <p class="relative_pos">p with Relative Pos</p>
            <p class="relative_pos">p with Relative Pos</p>
            <p class="relative_pos">p with Relative Pos</p>
            <p class="relative_pos">p with Relative Pos</p>
            <p class="relative_pos">p with Relative Pos</p>
            <p class="relative_pos">p with Relative Pos</p>
            <p class="relative_pos">p with Relative Pos</p>
            <p class="relative_pos">p with Relative Pos</p>
            <p class="relative_pos">p with Relative Pos</p>
        </div>
    </body>
</html>
```
