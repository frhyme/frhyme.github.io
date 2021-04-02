---
title: Google Apps Script - Get spreadsheed, set sheet Name
category: google
tags: google javascript google_sheet macro
---

## Google Apps Script - Sheet

### Get spreadsheet by its ID

- Google Apps Script를 사용해서 Sheet file을 열 때, 다음처럼 사용할 수도 있습니다.
  - `SpreadsheetApp`에서 현재 활성화되어 있는 SheetApp을 가리키도록 한 다음, 
  - `spreadsheet.getSheetByName("시트1")`를 사용해서 SheetName으로 시트를 가리키도록 하는 것이죠.

```javascript
function myFunction() {
  var spreadsheet = SpreadsheetApp.getActive()
  // console 창에 결과를 확인하려면 Logger를 사용하면 됩니다.

  Logger.log(spreadsheet.getName())

  if (spreadsheet.getName() == "GoogleAppsScript_Example") {
    var sheet1 = spreadsheet.getSheetByName("시트1")
    var a1 = sheet1.getRange("A1")
    a1.setValue(1000)
    /*
    - chaining을 이용해서 다음처럼 해줘도 됩니다.
    SpreadsheetApp.getActive().getSheetByName("시트1").getRange("A1").setValue(100)
    */
  }
}
```

- 이렇게 하는 것도 좋은데, 저는 `.getActive()`와 같은 방식으로 시트 파일을 가리키도록 하는 것이 좀 불안해요. 만약 실수로라도 다른 파일을 편집하게 되면 안되니까요.
- 구글 시트 파일의 URL을 보면 보통 다음과 같이 구성되어 있습니다.

```url
https://docs.google.com/spreadsheets/d/<SheetFileID>/edit#gid=<SheetID>
```

- 아래에서 `<SheetFileID>`를 사용해서 열 수도 있습니다.
- 찾아 보면, `spreadsheet` 객체에 `.getSheetByID(sheetID)`라는 메소드도 있다고는 하는데, 업데이트되면서 사라졌는지 지금은 없는 것 같습니다. 뭐 `sheetName`으로 찾아도 문제는 없죠.

```javascript
function myFunction() {
  var spreadsheet = SpreadsheetApp.openById("<spreadSheetID>")
  var sheet = spreadsheet.getSheetByName("시트1")
  sheet.getRange("A1").setValue("999")
}
```

### Set spreadsheet Name

- 다음의 방식으로 SpreadSheet의 이름을 변경할 수 있습니다.

```javascript
function myFunction() {
  var spreadsheet = SpreadsheetApp.getActive()
  spreadsheet.rename("NewSheetFileName")
}
```
