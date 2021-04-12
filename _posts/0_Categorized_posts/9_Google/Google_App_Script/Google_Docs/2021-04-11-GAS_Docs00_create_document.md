---
title: Google Apps Script - Docs - Create Document
category: google
tags: google javascript Google_Docs macro GoogleAppsScript 
---

## Google Apps Script - Docs - Create Document

- Google Apps Script를 사용하여 새로운 문서를 만들고, 문서 내에 글을 작성(Append)하는 방법을 정리하였습니다.

```js
function create_document() {
  // "MyFirstDocument" 라는 이름의 Google Document를 만듭니다.
  var doc = DocumentApp.create('MyFirstDocument');
  
  // 문서의 본문(Body)에 접근해서 text를 추가해줍니다.
  var body = doc.getBody()
  var text = "Hello World!!"
  body.appendParagraph(text)

  // 문서의 URL을 가져와서
  // 
  var url = doc.getUrl()
  console.log(url)
}
```

- 기존에 존재하는 document에 접근하여, 특정 text가 없는 경우 해당 텍스트틀 추가해줍니다.

```js
function append_text_to_doc() {
  // 기존에 존재하는 document를 가져옵니다.
  // document를 가져올 때는 documentID를 사용하여 가져오는데, 
  // 이는 다음과 같이 URL에 포함되어 있습니다.
  // https://docs.google.com/document/d/<documentID>/edit
  var documentID = ""
  var doc = DocumentApp.openById(documentID)

  // 본문에 text가 존재하는지 확인하고 없을 경우
  // text를 append해줍니다.
  var text = "Hello World"
  if (doc.getBody().findText(text)) {
    console.log("The text already exists")
  } else {
    var new_text = doc.getBody().appendParagraph(text)
  }  
}
```
