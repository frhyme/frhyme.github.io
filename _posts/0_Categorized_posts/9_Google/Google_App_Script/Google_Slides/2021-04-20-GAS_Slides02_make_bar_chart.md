---
title: Google Apps Script - Slides - Bar chart 만들기
category: google
tags: google javascript GoogleSlides macro GoogleAppsScript 
---

## Google Apps Script - Slides - Bar chart 만들기

- 저는 엑셀이나 matplotlib 등을 사용해서 차트를 만드는 것보다, 구글 슬라이드에서 직접 모양을 하나씩 넣어가면서 차트를 만드는 것을 더 좋아합니다.
- 따라서, 오늘은 간단한 bar chart의 형태를 하나하나 모양을 추가하면서 만드는 코드를 정리하였습니다.

```js
function myFunction() {
  // presentation을 엽니다.
  var slideId = '';
  var presentation = SlidesApp.openById(slideId)
  var targetSlide = presentation.getSlides()[2]

  var leftStart = 10;
  var topStart = 100;
  var eachShapeWidth = 6;
  var betweenShapeWidth = 2;
  
  // heights에 들어 있는 값이 
  // 각각 그려져야 하는 bar의 길이를 말합니다.
  var heights = [866, 930, 1070, 1072]
  
  if (targetSlide.getShapes().length != heights.length) {
    // 현재 모양이 추가되어 있지 않을 경우, 새롭게 모양을 추가해줍니다.
    for (var i=0; i < heights.length; i++) {
      var thisShape = targetSlide.insertShape(SlidesApp.ShapeType.RECTANGLE);
    }
  }
  // shape들을 하나씩 위치와 색깔등을 변경해줍니다.
  var shapes = targetSlide.getShapes()
  for (var i=0; i < heights.length; i++) {
    var thisShape = shapes[i];
    var widthSum = i * eachShapeWidth;
    var betweenWidthSum = i * betweenShapeWidth;
    var height = heights[i] / 20.0
    // shape의 위치를 정할 때, left, top을 통해 그려져야 하는 포인트를 찾습니다.
    // 그런데 여기서 bar는 아래쪽에 맞춰져 있는 것이 필요하기 때문에, 
    // 위치를 맞추기 위해서 일정값(300)에서 height를 빼주는 식으로 처리하여 
    // 좌표를 역으로 처리해줍니다.
    thisShape.setLeft(leftStart + (widthSum + betweenWidthSum))
    thisShape.setTop(300 - height)
    thisShape.setWidth(eachShapeWidth)
    thisShape.setHeight(height)
    
    thisShape.getBorder().setTransparent()
    thisShape.getFill().setSolidFill("#5F0000")
    //thisShape.getBorder().setTransparent()
  } 
}
```

## Wrap-up

- 여러 모양들을 한번에 선택하여, "아래쪽 맞춤"을 해줄 수 있을 것 같은데, 그 방법을 찾지 못해서 좀 아쉽네요.
