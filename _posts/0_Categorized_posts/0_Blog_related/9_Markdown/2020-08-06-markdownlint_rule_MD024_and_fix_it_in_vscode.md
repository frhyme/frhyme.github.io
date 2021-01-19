---
title: MarkdownLint - MD024 - Multiple headings with the same content
category: MarkdownLint
tags: markdown markdownlint
---

## Intro - MarkdownLint

- [markdownlint](https://github.com/DavidAnson/markdownlint/blob/main/doc/Rules.md)는 markdown 문서 작성 중에, 문법이 잘못되었다면 노란색으로 첨삭해주는 아주 친절하고 고맙고 귀찮은 새끼입니다 호호호.
- 귀찮기는 해도, 전반적으로 다 타당한 이야기이기는 해서, 보통 노란 줄이 뜨면 고치게 되고 이것이 반복되면 좋은 문서 작성 습관이 생기게 되죠.
- 아무튼, 오늘 말하려는 것이 markdownlint를 칭찬하려는 것은 아니고, 그중 MD024라는 rule에 대한 것을 정리해봤습니다.

## MD024 - 한 페이지 내에 같은 이름의 heading이 있으면 안된다?

- [MD024](https://github.com/DavidAnson/markdownlint/blob/main/doc/Rules.md#md024---multiple-headings-with-the-same-content)는 "한 페이지(마크다운 문서) 내에 동일한 이름의 heading이 있으면 안된다고 말합니다.
- 가령 다음과 같은 형식으로 heading이 작성된다면, 문제가 발생한다는 이야기지요. 동시에 `heading1`이라는 이름을 가진 제목이 중복으로 등장하면 안되니까요.

```markdown
## heading1

## heading1
```

- 다만, 다음과 같은 경우에도 MD024는 발현됩니다. 제목 `Summary`는 중복되는 것처럼 보이지만, 서로 다른 큰 제목 아래에 있죠. 따라서, 이 두 아이에 대해서 똑같이 적용하는 것은, 별로 타당해보이지 않아요.

```markdown
## Heading1

### Summary 

## Heading2

### Summary 
```

- 당연하지만, 이미 2017년에 [MD024 (Multiple headers with same content) should only trigger under the same nesting](https://github.com/markdownlint/markdownlint/issues/175) 라는 이슈가 있었습니다. 이때문만인지는 모르겠지만, 아무튼 고칠 수 있는 방법은 있죠.

## How to solve it

- 우선, 저는 VScode를 사용하고 있습니다. setting으로 들어가서, extension에서 markdownlint 부분을 클릭한 다음, 아래의 json 부분을 넣어주면 됩니다.

```json
"markdownlint.config": {
    "MD024":{
        "siblings_only": true,
    }// 20200806 - 서로 다른 제목 아래에 있는 경우 제목 중복 허용
},
```

## wrap-up

- 참 쉽죠? 별것 아니지만, 만약 마크다운에서 알려주는 잔소리가 마음에 들지 않는다면, 그 이유를 한번 찾아보세요. 별 것 아닌처럼 느껴지더라도, 그런 것들이 시간에 따라 점차 쌓이면, 생각보다 괜찮은 지식들을 획득할 수 있습니다. 습관이 중요한 것 같아요. 좋은 습관을 만들고 오랫동안 유지한다면, 분명히 좋은 날이 옵니다.
- 혹은, 꼭 그렇지 않더라도, 매일 작은 호기심들을 해결하면, 그 자체로 기분이 좋잖아요? 호호

## reference

- [stackexchange - How do I change Markdownlint settings in Visual Studio Code](https://superuser.com/questions/1295409/how-do-i-change-markdownlint-settings-in-visual-studio-code)
- [MD024 - mutliple headings with the same content](https://github.com/DavidAnson/markdownlint/blob/main/doc/Rules.md#md024---multiple-headings-with-the-same-content)
