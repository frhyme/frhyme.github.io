---
title: Google Apps Script - Range
category: google
tags: google javascript google_sheet macro
---

## Google Apps Script - Range

- Google Apps Script를 사용해서 Sheet의 Cell의 값을 변경하는 방법을 정리합니다.
- 다음은 Sheet 내의 A1부터 E5까지의 Cell에 값을 입력해주는 코드입니다. 
- 코드 자체가 복잡하지 않아서 따로 설명하지는 않겠습니다. 

```javascript
function myFunction() {
  var spreadsheet = SpreadsheetApp.getActive()
  var sheet = spreadsheet.getSheetByName("시트1")
  // Range는 그냥 Cell이라고 생각하셔도 됩니다.
  // 아래에서는 "A1"만 참조했으므로 사실 1개의 Cell만 참조하는 것이죠.
  var left_top_cell = sheet.getRange("A1")

  for (i = 0; i < 5; i++) {
    for (j = 0; j < 5; j++) {
      // offset은 상대참조를 하는 메소드입니다.
      // offset(0, 0): 기존 cell
      // offset(1, 0): 기존 cell 한 칸 아래 cell
      // offset(0, 1): 기존 cell 한 칸 오른쪽 cell
      left_top_cell.offset(i, j).setValue( i * 10 + j)
    }
  }
}
```
