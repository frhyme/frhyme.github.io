---
title: Markdown Front-matter 빠르게 입력하기
category: markdown
tags: markdown yaml code-snippet vs-code
---

## Intro: Markdown Front-matter 자동완성

- 저는 jekyll기반의 블로그를 가지고 있고, 따라서 마크다운으로 글을 씁니다(다만, 요즘은 HEXO가 이쁘더군요. 나중에 시간이 나면 옮길 마음도 있습니다).
- 블로그에 쓸 새로운 글감이 떠오른다면, 우선 제가 쓰는 IDE인 vs-code를 실행하고, 해당 블로그 폴더로 들어간 다음, 새로운 마크다운 파일을 생성합니다. 이름은 뭐 언제나 대충 쓰구요.
- 다만, 지킬 기반의 블로그에서 마크다운을 쓸 때 맨 윗줄에는 다음과 같은 Front matter가 들어갑니다.

```plaintext
---
title: 이 글의 제목
category: 어떤 카테고리에 속하는지
tags: markdown jeklyy 태그1 태그2
---
```

- Jekyll이 마크다운 파일을 HTML로 변환할 때 반드시 필요한 일종의 소스인 셈이죠.
- 다만, 문제는 모든 마크다운 파일에 공통적으로 저 부분이 들어가야 하는데, 매번 제가 마크다운 파일을 새로 생성할 때마다 Front matter의 형식을 직접 쳐야 한다는 번거로움이 있습니다. 사소하다면 사소한 것인데, 생각해보니까 개선할 수 있지 않을까? 하는 생각이 들었습니다. 최소한, 다음 부분만이라고 입력되게 한다면 더 빠르게 글을 작성할 수 있을 테니까요.

```plaintext
---
title:
category:
tags:
---
```

- 따라서 저는 마크다운 파일 내에서 반복되는 이 Front matter를 빠르게 작성하려고 합니다.
  
## Code snippet을 이용하여 빠르게 작성하자

- 저는 "Code snippet"이라는 기능을 통해 이를 구현하려고 합니다.
- Snippet은 한국어로 "조각"을 의미하며, Code Snippet은 "코드 조각"이라는 의미가 됩니다. 특정 명령어(`prefix`)를 만들고 파일 작업시에 해당 명령어가 입력될 경우 해당 명령어에 연결된 코드(`Body`)를 자동으로 변환해주는 기능을 말하죠. 비슷하게는 이클립스의 code template이 있습니다.
- 따라서, 저는 가령 `front_matter`라는 명령어를 마크다운 파일에서 입력하면, 자동으로 이 부분이 다음과 같이 변환되게 하려고 합니다. 일단은, 가능할 것으로 보입니다.

```plaintext
---
title:
category:
tags:
---
```

- VS-code에서 설정(preference)으로 들어간 다음(`Code > Preference`), `markdown.json` 파일 내에 아래 부분을 작성해줍니다. 즉, 저는 글로벌(global) 영역에서 code-snippet 기능을 사용하는 것이 아니라, 마크다운 파일 내에만 적용되도록 해준 것이죠. 물론, 글로벌 영역에서 설정해줘도 됩니다만, 저는 각각의 json에 분할해서 작성해주는 것이 훨씬 바람직한 코딩 방법이라고 생각해요.
- 아래 부분의 내용은 각각 다음과 같습니다.
  - `prefix`: 단축 명령어, 이 명령어를 치면 바꿔준다.
  - `body`: 단축 명령어가 실행되면 변활될 텍스트. 한줄 한줄을 따로 리스트 내 원소로 정리해준다.
  - `description`: 단축 명령어에 대한 설명

```json
"Generate Front Matter":{
    "prefix": "front_matter",
    "body":[
        "---",
        "title: ",
        "category: ",
        "tags: ",
        "---"
    ],
    "description": "this is description"
}
```

## Fail: 안되는 이유

- 다만, 슬프게도 이렇게 했는데 되지 않더군요. 이유를 모르겠어서, `Code > Preference > python.json`에 들어가서 아래와 같은 똑같은 코드를 넣어 보니, 문제없이 돌아가는 것을 확인했습니다. 네, 그렇다면 이제 문제는 명확해집니다. 현재 작성된 것은 문제가 없지만, 마크다운에서는 안된다는 것이죠.

```json
"Generate YAML header":{
    "prefix": "generate_yaml_header",
    "body":[
        "---",
        "title: ",
        "category: ",
        "tags: ",
        "---"
    ],
    "description": "this is description"
}
```

## 해결

- 구글에서  "vs code code snippet for markdown doesn't work"라고 검색하였고 [이 링크에서](https://github.com/Microsoft/vscode/issues/28048) 답을 찾았습니다.
- 링크의 내용을 정리하자면, "네 설정에 문제가 있는거다. 그러니까 아래 부분을 `setting.json`에 추가해라. 라는 말입니다. 마크다운 에디터에서 `quickSuggestions`이 가능하도록 하고, `snippetSuggestions`의 우선순위를 높이라, 라는 말이죠.
- `command + p`를 치고 `setting.json`을 쳐서 설정에 들어가서 아래 내용을 추가해줍니다.

```json
"[markdown]":  {
    "editor.quickSuggestions": true,
    "editor.snippetSuggestions": "top"
}
```

- 이렇게 하고 나면 아주 원활하게 잘 됩니다.

## wrap-up

- 지금까지 늘 code-snippet을 보기만 하고 직접 사용해본 적은 없는데, 꽤 유용한 기능으로 보이는 군요. 다만 기존의 snippet들이 엄청 많은지, 뭘 칠 때마다 뭐가 자꾸 뜹니다. 약간 귀찮네요 흠. 하지만 어쩔 수 없죠.

## reference

- [Snippets in Visual Studio Code](https://code.visualstudio.com/docs/editor/userdefinedsnippets)
- [VS Code Snippet(코드조각) 만들기](https://llighter.github.io/hugo_blog/2018/05/vs-code-snippet%EC%BD%94%EB%93%9C%EC%A1%B0%EA%B0%81-%EB%A7%8C%EB%93%A4%EA%B8%B0/)
- [Markdown Snippet Prefix Does Not Trigger Snippet #28048](https://github.com/Microsoft/vscode/issues/28048)
