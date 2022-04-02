---
title: vim 26 - iabbrev 를 사용하여 오늘 날짜를 string으로 가져옵니다
category: vim
tags: vim iabbrev vimscript vi
---

## vim 26 - iabbrev 를 사용하여 오늘 날짜를 string으로 가져옵니다

- 저는 git에 commit을 할 때 항상 날짜를 박아넣습니다. 이는 git에서 각 file 별로 최종 편집 날짜를 보여줄 때, 정확한 날짜가 아니라, '며칠 전'과 같은 형태로 보여주는데, 이게 오히려 혼동을 가져와서 그런거죠.
- 보통 commit을 할 때의 순서는 다음과 같습니다. 모든 commit에서 아래 프로세스가 반복되는데 아래를 좀 더 효율적으로 변경할 수 있을 것 같아요.

1. `git commit`을 사용합니다.
1. git message를 작성할 때 날짜를 써야 하는데 날짜가 기억나지 않으므로 상태표시줄에서 날짜를 확인합니다.
1. 날짜를 확인하고, 그 날짜대로 '2022-X-X'를 타이핑합니다.
1. 이제 추가될 git message를 추가로 작성합니다.

- 이를 간단하게 하기 위해서, `.vimrc` file 내에 아래 내용을 작성해줬습니다.
- 이를 통해 git message를 사용할 때, `__date` 를 사용해서, 기존에 작업하던 프로세스를 좀 더 간소화하였습니다.

```vim
function GetTodayDate()
    " 20220402 - sng_hn.lee - Init
    " vim script에서는 . 를 사용하여 string concatenation을 사용합니다.
    " remove new line by cutting tail
    let today = system('date +%Y-%m-%d')[:-2] . ' ('
    let weekday = system('date +%u')[:-2]

    if weekday=='1'
        let today = today .'Mon'
    elseif weekday=='2'
        let today = today .'Tue'
    elseif weekday=='3'
        let today = today .'Wed'
    elseif weekday=='4'
        let today = today .'Thu'
    elseif weekday=='5'
        let today = today .'Fri'
    elseif weekday=='6'
        let today = today .'Sat'
    elseif weekday=='7'
        let today = today .'Sun'
    endif
    return today . ')'
endfunction

iabbrev <expr> __today GetTodayDate()
```

## Wrap-up

- 개발하다가 vimscript와 shellscript를 헷갈려서 중간에 좀 헤맸습니다.
