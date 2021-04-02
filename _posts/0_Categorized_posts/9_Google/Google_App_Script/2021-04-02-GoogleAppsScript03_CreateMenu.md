---
title: Google Apps Script - Create Menu
category: google
tags: google javascript google_sheet macro GoogleAppsScript
---

## Google Apps Script - Create Menu

- Excel VBA에서는 매크로를 실행하는 버튼을 눌러야하는데, Google Sheet에서는 메뉴를 만듭니다.
- 다음의 코드로 메뉴를 만듭니다. "New Menu"라는 이름의 메뉴를 만들고, 그 밑에 "New Item"이라는 아이템을 만들어서, "myFunction"이라는 함수를 매핑해줍니다.

```javascript
function createMenu() {
  // Menu "New Menu"를 만들어줍니다.
  SpreadsheetApp.getUi().createMenu('New Menu')
  // Menu "New Menu"를 만들어줍니다.
  .addItem('New Item', 'myFunction')
  .addToUi();
}
```

- 다음처럼 함수를 새로 정의해주구요.

```javascript
function myFunction() {
  var spreadsheet = SpreadsheetApp.getActive()
  var sheet = spreadsheet.getSheetByName("시트1")
  // Range는 그냥 Cell이라고 생각하셔도 됩니다.
  // 아래에서는 "A1"만 참조했으므로 사실 1개의 Cell만 참조하는 것이죠.
  var left_top_cell = sheet.getRange("A1")
  for (i = 0; i < 5; i++) {
    for (j = 0; j < 5; j++) {
      left_top_cell.offset(i, j).setValue(10 * i + j)  
    }
  }
}
```

- 만약 메뉴를 삭제하고 싶으면 다음 함수를 실행해 주면 됩니다.

```javascript
function deleteMenu() {
  // 만든 메뉴를 지워줍니다.
  SpreadsheetApp.getActiveSpreadsheet().removeMenu("New Menu")
}
```
