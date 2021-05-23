---
title: vim - vscode vim plugin setting
category: vim
tags: vim vscode 
---

## vim - vscode vim plugin setting

- vs code에서 vim을 사용하기 위하여, [vscode - vim plugin](https://marketplace.visualstudio.com/items?itemName=vscodevim.vim)를 설치하여 사용하고 있습니다.
- 사용중에 약간 번거로움들이 있어서, 설정과 key binding을 아래와 같이 수정하였습니다. 해석하기는 어렵지 않을 거에요.
- 다만, 한글의 경우 영어에 비해서 늦게 입력되는 감이 있어서, 누른다음 정확히 적용되었는지 확인하려면, space를 눌러주는 것이 좋습니다. 특히, 방향키의 경우는 조금 늦게 입력되는 값이 있으니까 꼭 스페이스를 눌러주는 것이 좋습니다. 

```json
    // 20210523 vim setting
    /*
    before: vim의 기본 clipboard와 시스템 기본 clipboard가 달라서 복사한 내용을 붙일 때 성가신 부분이 있음. 
    usesystemclipboard  설정을 true로 변경하면 동일한 clipboard를 사용하게 됨.
    */
    "vim.useSystemClipboard": true, 
    // y로 복사하면 복사한 부분이 잠시 깜빡함.
    "vim.highlightedyank.enable": true,
    "vim.highlightedyank.duration": 1000,
    "vim.insertModeKeyBindings": [
        {
            "before": [],
            "after": []
        }
    ],
    /*
    한글과 영어를 번갈아 가면서 쓰면 한영전환을 여러 번 눌러야 합니다. 
    vim을 쓰는 경우 한영 전환을 반복해서 눌러야 해서 매우 번거로워지죠. 
    이를 해결하기 위해서 다음과 같이, keybinding을 수정하였습니다.
    */
    "vim.normalModeKeyBindings": [
        // normal mode에서 insert 모드로 들어가기 위한 설정
        {
            "before": ["ㅑ"],
            "after": ["i"]
        }, 
        { 
            "before": ["ㅐ"], 
            "after": ["o"]
        },
        { 
            "before": ["ㅁ"], 
            "after": ["a"]
        },
        // hjkl 방향키 설정. 다만 방향키는 조금 늦게 먹음.
        {
            "before": ["ㅗ"],
            "after": ["h"]
        }, 
        {
            "before": ["ㅓ"], 
            "after": ["j"]
        }, 
        {
            "before": ["ㅏ"],
            "after": ["k"]
        },
        {
            "before": ["ㅣ"], 
            "after": ["l"]
        }, 
        {
            "before": ["ㅌ"], 
            "after": ["x"]
        }
    ],
    "vim.commandLineModeKeyBindings": [
        // command mode에서 한영변환없이 바로 저장하기 위한 설정
        {
            "before": ["ㅈ"], 
            "after": ["w"]
        }
    ]
```

## reference

- [vscode - vim plugin](https://marketplace.visualstudio.com/items?itemName=vscodevim.vim)
