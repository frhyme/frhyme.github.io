---
title: Google Apps Script - Slides - Line chart 만들기
category: google
tags: google javascript GoogleSlides macro GoogleAppsScript 
---

## Google Apps Script - Slides - Line chart 만들기

- 저는 excel, matplotlib 등을 사용해서 차트를 만드는 것보다 슬라이드에 직접 모양을 하나씩 만드는 것을 더 선호합니다.
- Google Slides에 그림을 그리는 경우에는 마우스를 쓰지 않고, Google Apps Script를 사용해서 처리할 수도 있죠.
- 코드는 다음과 같습니다.

```js
function draw_line_chart() {
  var slideId = '';
  var presentation = SlidesApp.openById(slideId)
  var targetSlide = presentation.getSlides()[2]
  
  // Clear shapes
  var shapes = targetSlide.getShapes()
  for (var i=0; i < shapes.length; i++) {
    shapes[i].remove()
  }
  // Clear lines
  var lines = targetSlide.getLines()
  for (var i=0; i < lines.length; i++) {
    lines[i].remove()
  }

  // Set Data
  // Label : y_lst(height) 의 조합으로 정리함.
  var data_dict = {
    'A': [7, 8, 7, 7, 7, 7, 8, 8, 7, 7, 8, 7, 8, 8, 7, 7, 8, 7, 8, 8, 7, 8, 6, 6, 7, 9],
    'B': [3.174, 3.102, 2.948, 2.951, 3.091, 2.936, 2.927, 2.871, 2.813, 2.95, 3.084, 3.116, 3.135, 3.179, 3.229, 3.088, 3.025, 2.898, 2.972, 3.009, 2.991, 3.012, 2.749, 2.77, 2.889, 2.824]
  }  

  var color_dict = {
    'A': "#FF0000", 
    'B': "#00FF00"
  }

  // 저는 Slide를 14:10으로 하여 다음과 같은 좌표로 정하였습니다. 
  // 슬라이드 규격이 다르면 수정해야 합니다
  var fullWidth = 620;
  var leftStart = 30;
  var topStart = 350;

  var shapeType = SlidesApp.ShapeType.ELLIPSE
  var shapeDiameter = 5;
  var lineWeight = 3;
  var valueRatio = 20
  var lineAlpha = 0.5
  var shapeAlpha = 1.0

  // draw x-axis 
  for ([label, values] of Object.entries(data_dict)) {
    var betweenShapeWidth = fullWidth / (values.length - 1);
    for (var i=0; i < values.length; i++) {
      var x_textBox = targetSlide.insertTextBox(SlidesApp.ShapeType.RECTANGLE)
      x_textBox.getText().setText( ((i + 3) % 4 + 1) + "Q")
      
      var betweenWidthSum = i * betweenShapeWidth;
      x_textBox.setLeft(leftStart +  betweenWidthSum - 10)
      x_textBox.setWidth(40)
      x_textBox.setTop(topStart + 10)
      x_textBox.getText().getTextStyle().setFontSize(9)
      x_textBox.getText().getTextStyle().setBold(true)
      x_textBox.getText().getTextStyle().setForegroundColor("#FFFFFF")
      x_textBox.setHeight(30)
    }
    break
  }
  // draw y-line
  for ([label, values] of Object.entries(data_dict)) {
    for (var i=0; i < values.length; i++) {
      if (i % 4 == 0) {
        var betweenWidthSum = i * betweenShapeWidth;
        var thisLine = targetSlide.insertLine(
          SlidesApp.LineCategory.STRAIGHT, 
          startLeft=leftStart +  betweenWidthSum + betweenShapeWidth / 2 + 3, 
          startTop=100, 
          endLeft=leftStart +  betweenWidthSum + betweenShapeWidth / 2 + 3, 
          endTop=topStart + 10 
        )
        thisLine.getLineFill().setSolidFill("#888888", 1.0)
        thisLine.setWeight(1.5)
        // SlidesApp.DashStyle.DASH, 
        
        thisLine.setDashStyle(SlidesApp.DashStyle.DOT)
      } 
    }
    break;
  }
  
  for ([label, values] of Object.entries(data_dict)) {
    console.log(label)
    var betweenShapeWidth = fullWidth / (values.length - 1);
    
    var shapeColor = color_dict[label]
    var lineColor = color_dict[label]

    // Insert shapes
    for (var i=0; i < values.length; i++) {
      targetSlide.insertShape(shapeType);
    }
    // 마지막 n개 shape를 가져온다.
    var shapes = targetSlide.getShapes().slice(-values.length)
    
    // Insert label 
    var labelBox = targetSlide.insertTextBox(SlidesApp.ShapeType.RECTANGLE)
    labelBox.setLeft(leftStart + fullWidth + 10)
    labelBox.setTop(topStart - values.slice(-1)[0] * valueRatio - shapeDiameter * 2)
    labelBox.getText().clear()
    labelBox.getText().setText(label)
    labelBox.getText().getTextStyle().setForegroundColor(color_dict[label])
    labelBox.getText().getTextStyle().setFontSize(10)
    labelBox.setWidth(80)
    labelBox.setHeight(10)

    // set position of shape
    for (var i=0; i < shapes.length; i++) {
      var thisShape = shapes[i];
      var betweenWidthSum = i * betweenShapeWidth;
      var value = values[i] * valueRatio
      thisShape.setLeft(leftStart +  betweenWidthSum)
      thisShape.setTop(topStart - value)
      thisShape.setWidth(shapeDiameter)
      thisShape.setHeight(shapeDiameter)
      thisShape.getBorder().getLineFill().setSolidFill(shapeColor, shapeAlpha)
      thisShape.getBorder().setWeight(3)
      thisShape.getFill().setSolidFill("#000000")
    }
    // Insert line
    // Draw line
    for (var i=0; i < (shapes.length - 1); i++) {
      prevShape = shapes[i]
      nextShape = shapes[i+1]
      halfWidth = prevShape.getWidth() / 2.0
      helfHeight = prevShape.getHeight() / 2.0
      var startLeft = prevShape.getLeft() + halfWidth
      var startTop = prevShape.getTop() + helfHeight
      var endLeft = nextShape.getLeft() + halfWidth
      var endTop = nextShape.getTop() + helfHeight

      var thisLine = targetSlide.insertLine(
        SlidesApp.LineCategory.STRAIGHT, 
        startLeft=startLeft, startTop=startTop, 
        endLeft=endLeft, endTop=endTop
      )
      thisLine.setWeight(lineWeight)
      thisLine.getLineFill().setSolidFill(lineColor, lineAlpha)
      thisLine.sendBackward()
      thisLine.sendToBack()
    }
  }
}
```
