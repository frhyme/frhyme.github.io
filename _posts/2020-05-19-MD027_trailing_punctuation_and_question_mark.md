---
title: Markdown Rule - MD026 - Trailing punctuation in header
category: markdown
tags: markdown lint markdown-lint
---

## Intro - 왜 갑자기 마크다운 이야기인가

- 저는 IDE로 VS-code를 사용하고, 문서 편집은 보통 마크다운을 사용합니다. 그리고 마크다운 문법이 복잡하니 않으니까 보통 그냥 막 써오고 있었죠.
- 그러다 보니 가끔 HTML로 정확하게 변환되지 않는 경우들도 있고 해서 얼마전부터는 [vscode-Markdownlint](https://github.com/DavidAnson/vscode-markdownlint)를 설치해서 사용하고 있습니다. 이 아이를 설치하고 **마크다운 문서를 작성하면 화면에서 마크다운-Rule에 위배되는 부분은 노란 색으로 줄이 좍좍 쳐집니다.**
- 어떻게 보면 별 것 아닌데, 저는 좋습니다. 이렇게 해서 조금씩 마크다운의 문법에 친숙해지면 좋거든요.

## MD026: Trailing punctuation in header

- 오늘은 다른 글을 쓰다가, 제목에 `?`을 넣으니까 아래의 오류가 뜨더군요. 해석하자면 "MD026: 구두문자 중 하나인 물음표(?)가 맨 끝에 오면 안되는 규칙을 위반했어."라는 이야기죠. punctuation은 "구두문자"를 의미하고요, header에는 원래 짧은 1개의 문장만을 넣는 것을 권유합니다. 따라서, 물음표와 같이 문장의 종결을 의미하는 문자가 오면 안된다는 이야기죠.

```code
MD026/no-trailing-punctuation: Trailing punctuation in heading [Punctuation: '?']markdownlint(MD026)
```

- 특별한 이유가 있는가? 하고 찾아보니, 꼭 그런것 같지는 않습니다. 그냥 앞서 말한대로 제목에는 짧은 1개의 문장이 들어오는 것이 좋으므로 그렇게 권유한 것일 뿐 반드시 그래야 하는 것 같지는 않아요. **혹시, 명확한 어떤 이유를 아시는 분은 알려주시면 감사하겠습니다.**
  
## 만약 Header에 ?를 쓰고 싶다면?

- 그러함에도 만약 쓰고 싶다면 다음처럼 할 수 있습니다.
- 우선 `commmand + ,`를 눌러서 setting으로 가고, 거기서 extenstion 부분에서 markdownlint로 갑니다. 그리고 `setting.json`을 열어서 다음 부분을 추가해주면 됩니다. 참 쉽죠?

```json
"markdownlint.config": {
    "MD026":{
        "punctuation":".,;:!"
    }
}
```

## wrap-up

- 저는 처음에는 마크다운을 HTML로 변환해주는 과정에서, `?`가 있을 경우 문제가 발생한다거나, 하는 이유가 있을 줄 알았습니다. 하지만, 그런게 아니고 그냥 권유에 가까운 것 같네요.