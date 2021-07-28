---
title: VScode - Markdown Preview Sync with Cursor position
category: VScode
tags: VScode markdown markdownPreview extension keyBinding
---

## VScode - Markdown Preview Sync with Cursor position

- 저는 Markdown을 사용해서 문서를 작성합니다. 그리고, 작성 중 문서는 markdown preview를 사용해서 확인하죠(맥에서는 `command + shift + v`).
- 그러나, editor에서의 scroll 위치와 markdown preview에서의 scroll 위치가 불일치하는 문제가 있습니다. 가령, editor에서는 제일 아래 쪽에 cursor가 위치해 있었다면, markdown preview에서도 문서를 렌더링한 다음 제일 아래쪽을 보여줘야 하는데, 항상 제일 위쪽에 가 있습니다. 
- 따라서 가령 다음과 같이 진행됩니다. 아래 단계에서 3번이 꽤 번거로운 부분이죠.
  1. 마크다운 문서를 작성한다. 
  2. 작성 중 현재 문서를 확인하기 위하여 markdown preview를 누른다.
  3. 스크롤이 현재 커서와 다르므로 preview 상황에서 커서를 내리며 보고 싶은 위치를 찾는다.
  4. 1로 돌아간다.
- 따라서, 3번 과정을 삭제하는 것이 본 포스팅의 목적입니다.

## Markdown All in One - Preview

- 저는 현재 [Markdown All in One](https://marketplace.visualstudio.com/items?itemName=yzhang.markdown-all-in-one)을 사용하고 있습니다. 그리고, 보통 이런 세부 설정은 해당 extension의 설정값을 변경해 주면 되죠.
- 하지만, 아쉽게도 Markdown All in One에는 그런 설정값이 없는 것 같습니다.

## Markdown Preview Enhanced 

- [Markdown Preview Enhanced](https://marketplace.visualstudio.com/items?itemName=shd101wyy.markdown-preview-enhanced)에는 `"markdown-preview-enhanced.previewTheme"`라는 값이 있습니다. 이 값을 아래와 같이 true로 바꾸어 `setting.json`에 넣어주면 해결됩니다.
- 저는 `previewTheme`까지 모두 변경해줬습니다.

```json
"markdown-preview-enhanced.scrollSync": true,
"markdown-preview-enhanced.previewTheme": "atom-dark.css",
```

- 적용결과를 확인하기 위해서는 우선, `Markdown All in One`을 지우거나 disable로 처리해야 합니다. 
- 그 다음 `command + shift + v`로 적용해보면 markdown preview에서 제 editor가 위치하고 있던 곳으로 알아서 움직여 주는 것을 알 수 있습니다.

## Change Keybinding

- 하지만, 아직 끝난 게 아닙니다.
- `Markdown All in One`을 지우면, auto complete, shortcut등이 적용되지 않죠. 가령 `command + b`로 텍스트를 bold로 처리하는 기능 같은 건 `Markdown All in One`에 포함되어 있어서 지우면 안되죠.
- 그렇다면, 결국 `Markdown All in One`에서 preview 기능만 해제하고 `markdown-preview-enhanced`만 가능하도록 해야 합니다.
- 그럼, `command + shift + v`를 눌렀을 때 동작하는 부분을 수정하면 되는 게 아닐까 싶습니다. 즉 KeyBinding을 수정하면 된다는 이야기죠. KeyBinding에 접근하는데는 여러 방법이 있습니다.
  1. Code > Preference > Keyboard Shortcuts
  2. `command + shift + P`, "Open keyboard shorcuts(JSON)"을 엽니다.
- 그리고 아래 내용을 추가해줍니다. 보는 것처럼, `shift+cmd+v`를 눌렀을 때, `"markdown-preview-enhanced"`를 실행하도록 해준다는 이야기죠.
- 그리고 그 다음 부분은 default로 설정되어 있던 부분을 해제해준다는 의미로 보입니다.

```json
// Place your key bindings in this file to override the defaultsauto[]
[
    // 20210120: ADD for better markdown preview
    // markdown-preview-enhanced support syncing with cursor in editor
    {
        "key": "shift+cmd+v",
        "command": "markdown.extension.togglePreview",
        "when": "markdown-preview-enhanced"
    },
    // disable default.
    {
        "key": "shift+cmd+v",
        "command": "-markdown.extension.togglePreview",
        "when": "!terminalFocus"
    }
]
```

- default 값은 다음과 같습니다.

```json
{ "key": "shift+cmd+v",           
  "command": "markdown.extension.togglePreview",
  "when": "!terminalFocus" 
}
```

## Wrap-up

- 결과적으로는 모두 해결했습니다. 몇 가지 내용을 추가하자면 다음과 같습니다.
  - VScode는 다른 extension없이도 markdown을 지원합니다. 원래, `command + shift + v`를 사용하면 markdown preview가 실행되는 것이죠. 그래서, key bind에 저 default값이 작성되어 있는 것으로 보입니다.
  - `Markdown All in One`이 없는 상태에서, `Markdown-preview-enhanced`를 설치하면, 이 키바인딩이 덮어 씌워지는 것으로 보입니다. 즉, `command + shift + v`을 누르면, 알아서 `Markdown-preview-enhanced`이 실행되도록 설정되는 것이죠.
  - 그러나, `Markdown All in One`을 다시 설치하게 되면, 이 설정이 원래대로 변경됩니다. 따라서, `Markdown-preview-enhanced`는 무효화되죠.
  - 결국 저는 이를 우회하기 위해서, `keybindgs.json`에 제가 원하는 설정을 덮어 씌웠습니다. 이 때 default에 덮어 씌우는 것이 아니라는 점에 유의하세요.
- 결과적으로는 제가 원하는 대로 되기는 했는데, 정말 그런 것인지는 조금 찜찜하군요 호호. 왜냐면 이런 설정 들을 하나씩 해주다보면 나비효과처럼 새로운 문제들이 발생하곤 하거든요. 그래서, 제가 설정을 변경할 때, 지금처럼 세부적으로 모든 과정을 작성해둡니다. 그래야 나중에 문제가 발생하지 않거든요 호호호.
