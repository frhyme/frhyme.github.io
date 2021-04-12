---
title: Google Apps Script - Docs - Append Table
category: google
tags: google javascript Google_Docs macro GoogleAppsScript 
---

## Google Apps Script - Docs - Append Table

- `doc.getBody().appendTable()`을 사용해서 Google Doc 문서 내에 Table을 추가할 수 있습니다.

```js
function append_table_to_doc() {
  // 기존에 존재하는 document를 가져옵니다.
  // document를 가져올 때는 documentID를 사용하여 가져오는데, 
  // 이는 다음과 같이 URL에 포함되어 있습니다.
  // https://docs.google.com/document/d/<documentID>/edit
  var documentID = ""
  var doc = DocumentApp.openById(documentID)

  // rows는 table의 data를 의미합니다.
  // 첫번째 list는 Header, 두번째 list부터 row가 되죠.
  var rows = [
    ["column1_Name", "column2_Name"], 
    ["col1_value1", "col2_value1"], 
    ["col1_value2", "col2_value2"]
  ]
  
  // .appendTable(rows)를 사용하여 문서에 테이블을 추가해줍니다.
  var table = doc.getBody().appendTable(rows);
}
```
