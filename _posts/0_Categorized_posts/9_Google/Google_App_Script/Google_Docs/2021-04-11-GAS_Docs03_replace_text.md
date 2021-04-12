---
title: Google Apps Script - Docs - Replace text
category: google
tags: google javascript Google_Docs macro GoogleAppsScript 
---

## Google Apps Script - Docs - Replace text

- `.replaceText("originalText", "newText")`를 사용해서 텍스트를 변환할 수 있습니다.
- 원래 문서에 다음과 같이 작성되어 있다고 하겠습니다.

```plaintext
abc abc abc
```

- 다음 코드를 작성하고 실행해 봅니다.

```js
function replace_text() {
  // open document by document ID 
  var documentID = ""
  var doc = DocumentApp.openById(documentID)
  
  // .replaceText를 사용해서 text 변환
  doc.body().replaceText("abc", "def")
}
```

- 그럼 다음과 같이 짠 하고 바뀝니다.

```plaintext
def def def
```
