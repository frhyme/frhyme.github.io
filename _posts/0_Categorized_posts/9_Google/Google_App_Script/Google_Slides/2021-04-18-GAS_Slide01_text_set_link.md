---
title: Google Apps Script - Slides - text에 link연결하기
category: google
tags: google javascript GoogleSlides macro GoogleAppsScript 
---

## Google Apps Script - Slides - text에 link연결하기

- Google Apps Script를 사용해서 slide의 text에 link를 연결하는 방법을 정리합니다.

```js
function set_link() {
  var slideId = 'slideId';
  var presentation = SlidesApp.openById(slideId)
  var slides = presentation.getSlides();
  var slide1 = slides[0]
  // textbox를 하나 만들어줍니다.
  var textBox = slide1.insertTextBox(
    text="MyBlogLink", 
    left=10, top=30, 
    width=200, height=50
  )
  // textBox에서 text를 가져온 다음,
  // style을 가져오고, 여기에 link를 연결해줍니다.
  var text = textBox.getText()
  var textStyle = text.getTextStyle()
  textStyle.setLinkUrl("https://frhyme.github.io/")
}
```
