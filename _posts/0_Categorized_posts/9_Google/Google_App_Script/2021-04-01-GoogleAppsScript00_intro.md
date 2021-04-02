---
title: Google Apps Script - Intro
category: google
tags: google javascript google_sheet macro GoogleAppsScript
---

## Google Apps Script - Intro

- Excel에서 VBA를 사용해서 시트의 데이터들을 처리해주는 작업을 하다가, 구글 시트에도 비슷한 게 있지 않을까 싶어서 찾아보니 Google App Script라는 것이 있더군요.
- 저는 맥북 유저라서 사실 MS Office 계열의 제품들보다는 Google Office의 제품들을 주로 사용합니다. 그래서 얘가 좀 더 유용할 것 같아요.

## Google Apps Script? 

- [Google Apps Script](https://www.google.com/script/start/)는 Google Workspace 플랫폼에서 돌아가는 어플리케이션(보통 매크로)를 구현하기 위해서 만들어진 언어(플랫폼)입니다. 일단은 그냥 자바스크립트와 유사한 언어, 라고 생각하시면 됩니다. 
- 처음에는 구글 시트에서만 돌아가기 위해 개발된 것처럼 보이지만, 현재는 구글의 모든 앱들을 포괄할 수 있는 플랫폼으로 확장된 것 같아요.

## Google Apps Script - Google Sheet 

- Google Sheet 에서 **"도구 > Script 편집기"** 에 들어갑니다.
- 다음과 같은 함수를 작성해주고, 실행 버튼을 누르면 되는데, 버튼을 누르면 권한을 요청합니다. 뭐 줍니다 나의 쓸모없는 권한들.
- 실행하면, A1 Cell에 값이 업데이트되어 있는 것을 알 수 있습니다. 참 쉬죠.

```js
function myFunction() {
  var spreadsheet = SpreadsheetApp.getActive()
  // console 창에 결과를 확인하려면 Logger를 사용하면 됩니다.

  Logger.log(spreadsheet.getName())

  // 잘못된 동작을 막기 위해서, 파일 이름을 체크합니다.
  if (spreadsheet.getName() == "GoogleAppsScript_Example") {
    /*
    - chaining을 이용해서 다음처럼 해줘도 됩니다만, 저는 풀어서 해줬어요.
    SpreadsheetApp.getActive().getSheetByName("시트1").getRange("A1").setValue(100)
    */
    var sheet1 = spreadsheet.getSheetByName("시트1")
    var a1 = sheet1.getRange("A1")
    a1.setValue(1000)

  } else {
    Logger.log("Wrong file")
  }
}
```

## Wrap-up

- 오늘은 처음이므로 아주 간단하게 Google Apps Script를 사용하는 방법을 정리하였습니다.
- 일단 MS의 VBA에 비해서 편집기 자체가 비교하기 민망할 정도로 탁월해요.
- 그리고 좀 더 찾아봐야겠지만, 기존의 Google 서비스들의 API들과 연동하여 꽤나 재미있는 것들을 해볼 수 있을 것 같아요. 아 오랜만에 좀 설렙니다 호호.

## Reference

- [google - apps script - quickstart](https://developers.google.com/apps-script/quickstart/fundamentals-codelabs)
- [google - apps script - fundamentals 1](https://developers.google.com/codelabs/apps-script-fundamentals-1#0)
