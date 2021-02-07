---
title: Toast UI Grid - Basic
category: web
tags: web toast table html javascript
---

## Toast UI Grid - Basic

- [toast-ui Grid](https://nhn.github.io/tui.grid/latest/)를 사용하여 table을 그리는 방법을 정리합니다.
- 일반적으로 html에서 table은 다음의 형태로 표현해줍니다. 뭐...이렇게 해줘도 문제는 없는데 table은 워낙 많이 쓰이는 요소이기 때문에 javascript 단에서 쉽게 쓸 수 있도록 정의해놓은 많은 라이브러리들이 있죠. 그 중 하나가, [toast-ui Grid](https://nhn.github.io/tui.grid/latest/)입니다.

```html
<table>
    <tr>
        <th>colA</th>
        <th>colB</th>
        <th>colC</th>
    </tr>
    <tr>
        <td>val1</td>
        <td>val2</td>
        <td>val3</td>
    </tr>
</table>
```

## Toast UI Grid - Example

- 우선 html 문서를 정의해줍니다.
- [toast-ui Grid](https://nhn.github.io/tui.grid/latest/)를 CDN을 통해서 연결해줍니다.
- 그리고, id가 `"grid"`인 div 요소를 하나 만들어 줍니다. 이후 script단에서 해당 요소에 그림을 그려줄 겁니다.

```html
<html>
    <head>
        <meta charset="UTF-8">
        <!-- ADD Toast Grid -->
        <link rel="stylesheet" href="https://uicdn.toast.com/grid/latest/tui-grid.css" />
        <script src="https://uicdn.toast.com/grid/latest/tui-grid.js"></script>
    </head>    
    <body>
        <h3> Test Table </h3>
        <div id="grid"></div>
        <p> Table End </p>
    </body>
</html>
```

- javascript단은 다음과 같습니다. 
- 굳이 `setTimeout`을 넣어준 이유는 id가 `"grid"`인 요소가 마들어지기 전에 javascript가 돌아가는 일이 생길 수 있어서, 충분한 시간적 여유를 두고 만들어 준거죠.

```js
setTimeout(
    function drawGrid() {
        var Grid = tui.Grid;
        const grid = new Grid({
            el: document.getElementById('grid'),
            /* 
            column을 정의해줍니다.
            - header: 테이블에 표시될 칼럼 명
            - name: data에서 넘어올 ID
            */
            columns: [
                {
                    header: 'colA_name', name: 'colA_ID'
                },
                {
                    header: 'colB_name', name: 'colB_ID'
                }, 
                {
                    header: 'colC_name', name: 'colC_ID'
                }
            ], 
            data: []
        });
        /*
        */
        data = [
            {
                colA_ID: 'colA_val1',
                colB_ID: 'colB_val1', 
                colC_ID: 'colC_val1'
            },
            {
                colA_ID: 'colA_val2',
                colB_ID: 'colB_val2', 
                colC_ID: 'colC_val2'
            }
        ];
        grid.resetData(data);
        Grid.applyTheme('striped'); 
    }, 
    1000
);
```

---

## raw html

- 전체 문서는 다음과 같습니다.

```html
<html>
    <head>
        <meta charset="UTF-8">
        <!-- ADD Toast Grid -->
        <link rel="stylesheet" href="https://uicdn.toast.com/grid/latest/tui-grid.css" />
        <script src="https://uicdn.toast.com/grid/latest/tui-grid.js"></script>
        <script>
            setTimeout(
                function drawGrid() {
                    var Grid = tui.Grid;
                    const grid = new Grid({
                        el: document.getElementById('grid'),
                        /* 
                        column을 정의해줍니다.
                        - header: 테이블에 표시될 칼럼 명
                        - name: data에서 넘어올 ID
                        */
                        columns: [
                            {
                                header: 'colA_name', name: 'colA_ID'
                            },
                            {
                                header: 'colB_name', name: 'colB_ID'
                            }, 
                            {
                                header: 'colC_name', name: 'colC_ID'
                            }
                        ], 
                        data: []
                    });
                    /*
                    */
                    data = [
                        {
                            colA_ID: 'colA_val1',
                            colB_ID: 'colB_val1', 
                            colC_ID: 'colC_val1'
                        },
                        {
                            colA_ID: 'colA_val2',
                            colB_ID: 'colB_val2', 
                            colC_ID: 'colC_val2'
                        }
                    ];
                    grid.resetData(data);
                    Grid.applyTheme('striped'); 
                }, 
                1000
            );
        </script>
    </head>    
    <body>
        <h3> Test Table </h3>
        <div id="grid"></div>
        <p> Table End </p>
    </body>
</html>
```
