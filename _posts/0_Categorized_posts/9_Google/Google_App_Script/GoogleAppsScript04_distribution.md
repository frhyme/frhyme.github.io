---
title: Google Apps Script - 배포하기
category: google
tags: google javascript google_sheet macro GoogleAppsScript
---

## Google Apps Script - 배포하기

- Google Apps Script로 만든 함수를 외부에 배포할 수 있습니다.
- 제가 주로 쓰는 언어는 python이고, python code 상에서 구글 시트에 저장된 정보를 가져와서 사용하려면 번거롭습니다.
- 오늘 해보려는 것은 구글 시트 내에 있는 데이터를 읽고, 이를 외부에서 사용가능하도록 json등의 형태로 보내줄 수 있도록 하려고 해요.
  1. 구글 시트에서 Google Apps Script를 사용해서 내부의 시트 데이터를 읽고 json의 형태로 전송해주는 API를 만듬
  2. python 코드에서 해당 API에 접속해서 json 데이터를 가져옴.
  3. 분석 다다다 
- 해보자.


```javascript
function doGet(e) {
  // Get방식에 대해서 대응하는 함수
  Logger.log(e)
  var spreadsheet = SpreadsheetApp.getActive()
  var sheet = spreadsheet.getSheetByName("시트1")

  var returnArr = [1, 25, 3]
  Logger.log(returnArr)
  Logger.log(JSON.stringify(returnArr))
  // 
  return HtmlService.createHtmlOutput(JSON.stringify(returnArr))
  //
}

function doPost(e) {
  // post 방식에 대해서 대응하는 방식
}
```

- python에서 해당 web app에 접속해서 json된 자료를 가져오려면 어떻게 해야하나.
- `requests`라는 라이브러리르 쓰면 될것 같은데 흠.

## 배포 유형 

- 배포는 다음과 같은 4가지 유형으로 나뉜다. 우선 이 4가지의 차이를 알아야 하고. 
  - 웹 앱
  - API 실행 파일 
  - 부가기능
  - 라이브러리 
- API 실행 파일, 부가 기능의 경우 다음과 같은 메세지가 뜹니다. 아마 현재는 로컬에서 관리되고 있다면, 이를 GCP에 올려서 여러 유저들에게서 공통으로 관리되는 종류의 클라우드 프로젝트로 변경되어야 한다는 의미로 받아들여집니다.
  - 이 Apps Script 프로젝트는 Apps Script로 관리되는 Google Cloud Platform(GCP) 프로젝트를 사용하고 있습니다.
  - Google Workspace Marketplace에 API 실행 파일 유형을 배포하려면 이 Apps Script 프로젝트를 사용자가 관리하는 Google Cloud Platform(GCP) 프로젝트로 전환해야 합니다.

## Reference

- [google developers - apps script - web app](https://developers.google.com/apps-script/guides/web)
