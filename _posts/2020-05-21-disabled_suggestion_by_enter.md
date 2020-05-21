---
title: tab-completion or enter-completion 설정 및 해제
category: vs-code
tags: vs-code autto-completion intellsense
---

## Intro: tab이냐 엔터냐

- 자동완성(auto-completion)은 매우 유용한 기능입니다.
- 특히 code-snippet과 연결하여, 특정한 `prefix`에 대해서 자동으로 매칭되도록 설정해준다면 매우 편하게 사용할 수 있죠.
- 다만, 그 지점에서 1) `enter`를 사용하여 변경을 할 것인가 2) `tab`을 사용하여 변경할 것인가에 따른 차이를 서술하려고 합니다. 

## tab-completion is better

- 저는 vs-code를 쓰고 있고 vs-code의 경우 기본적으로 tab, enter 모두에 대해서 자동완성이 되도록 설정되어 있습니다.
- 이를 `setting.json`으로 본다면 다음과 같죠. 정확히는, 아래의 설정이 default값이죠.

```json
"editor.acceptSuggestionOnEnter": "on",
"editor.tabCompletion": "on",
```

- 다만, enter로 줄바꿈을 할 경우, '줄을 바꿔야 하는 위치`에서 엔터를 쳤는데 자동으로 제시된 구문(suggestion)이 적용되는 일이 있습니다. 많이 발생하는 일은 아니지만, 이거 꽤 번거롭고 빡치는 일이죠.
- 더불어, suggestion에서 적합한 것을 찾을 때는 화살표를 사용하는데, 이 화살표는 보통 키보드 오른쪽에 있고 따라서 99%의 사람들은 오른손으로 작업을 하게 됩니다. 그리고, `엔터` 또한 오른쪽에 있으므로 오른손으로 화살표를 누르고, 다시 엔터를 눌러야 하므로 같은 손이 사용된다는 문제가 있죠.
- 어찌 보면 문제는 아닙니다. 하지만, 오른손으로 화살표를 누르고, 왼손으로 `tab`을 통해 자동완성을 한다면 더 효율적으로 사용할 수 있을 것 같아요.
- 따라서, 저는 다음과 같이 설정을 변경하여 `setting.json`에 작성하였습니다.이렇게 할경우, `enter`에 대해서는 자동완성이 적용되지 않고 `tab`에 대해서만 유효하게 됩니다.

```jsond
"editor.acceptSuggestionOnEnter": "off",
"editor.tabCompletion": "on",
```

## python에서만 유효하도록

- 만약 이 부분이 모든 파일이 아닌 markdown에만 유효하도록 하려면 다음과 같이 하면 됩니다.

```json
"[markdown]":{
    // 20200520: 비슷한 코드에 대해서 알아서 제안해주는 기능. 이 아이를 true로 설정해야, code-snippet이 실행됨
    "editor.quickSuggestions": true, 
    // 20200520: suggesion을 적용하는 것을 tab만으로 가능하도록 변경함. 원래는 둘 다 가능했지만, 
    // 가끔 엔터를 쳤는데, 다른 걸로 자동으로 바뀌는 경우가 있어서, 이를 막기 위해 엔터로 변경하는 것을 막음.
    "editor.acceptSuggestionOnEnter": "off",
    "editor.tabCompletion": "on",// default
    // 20200520: snippet을 suggestion에서 가장 위에 오도록 설정해줌.
    "editor.snippetSuggestions": "top"
},
```

## wrap-up

- 처음에는 마크다운에서만 해제하였는데, 아무리 생각해도 python에서도 tab-completion이 훨씬 좋은 것 같아서, 모두 변경하였습니다.
