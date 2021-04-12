---
title: Google Apps Script - Docs - Append text with style
category: google
tags: google javascript Google_Docs macro GoogleAppsScript 
---

## Google Apps Script - Docs - Append text with style

- 문서에 text를 집어넣을 때, 기 정의된 style을 사용하여 집어넣어절 수도 있습니다.

```js
function append_heading_to_doc() {
  // docs의 documentID를 사용하여 문서를 열고, 
  var documentID = ""
  var doc = DocumentApp.openById(documentID)

  // Append text with Heading1
  var heading1_text = "Title"
  doc.getBody().appendParagraph(heading1_text)
     .setHeading(DocumentApp.ParagraphHeading.HEADING1)
  
  // Append text with Heading2
  var heading2_text = "sub_Title"
  doc.getBody().appendParagraph(heading2_text)
     .setHeading(DocumentApp.ParagraphHeading.HEADING2)
  
  // Append text with Heading3
  var heading3_text = "sub_sub_Title"
  doc.getBody().appendParagraph(heading3_text)
     .setHeading(DocumentApp.ParagraphHeading.HEADING3)
  
  // Append text with normal style
  var text = "normal_text"
  doc.getBody().appendParagraph(heading3_text)
     .setHeading(DocumentApp.ParagraphHeading.NORMAL) 
}
```
