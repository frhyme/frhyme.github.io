---
title: Google Apps Script - Slides - Insert Table
category: google
tags: google javascript GoogleSlides macro GoogleAppsScript 
---

## Google Apps Script - Slides - Insert Table

- Google Apps Script를 사용해서 slide에 Table을 집어넣고 값을 작성하는 방법을 다음과 같이 정리하였습니다.

```js
function slide_text() {
  // 해당 slide 문서의 ID를 집어넣습니다.
  var slideId = 'slideId';
  var presentation = SlidesApp.openById(slideId);
  var slides = presentation.getSlides(); // 슬라이드들을 가져오고
  var tables = slides[0].getTables() // 테이블을 가져오죠(없으면 빈 리스트)
  var row_num = 3;
  var col_num = 5;

  if (tables.length == 0) {
    // 테이블이 없는 경우 새로운 테이블을 만들어줍니다.
    slides[0].insertTable(row_num, col_num);
    var tables = slides[0].getTables()
  } else {
    console.log("table Already exist")
  }
  for (var i = 0; i < row_num; i++) {
    for (var j = 0; j < col_num; j++) {
      // 테이블내 cell에 값들을 업데이트해줍니다.
      var target_table = tables[0];
      var target_cell = target_table.getCell(i, j);
      var target_text = target_cell.getText();
      // 기존의 text를 지웁니다.
      target_text.clear()
      target_text.appendText("row"+i+"col"+j)
    }
  }
  presentation.saveAndClose()
}
```
