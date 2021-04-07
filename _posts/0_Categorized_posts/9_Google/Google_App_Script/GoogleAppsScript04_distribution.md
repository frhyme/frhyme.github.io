---
title: Google Apps Script - Google Sheet의 데이터를 python으로 보내기
category: google
tags: google javascript google_sheet macro GoogleAppsScript
---

## Google Apps Script - Google Sheet의 데이터를 python으로 보내기

- Google Apps Script를 사용하여 google sheet의 데이터를 python에서 손쉽게 받아볼 수 있도록 해주려고 합니다.
- 제가 주로 쓰는 언어는 python이고, python code 상에서 구글 시트에 저장된 정보를 가져오는 것은 꽤 번거롭습니다.
- [gspread](https://gspread.readthedocs.io/en/latest/)를 사용해도 되는데, 제 기억에는 별로 코드가 깔끔해지지 않았어요.
- 따라서, 오늘 해보려는 것은 구글 시트 내에 있는 데이터를 읽고, 이를 외부에서 사용가능하도록 json등의 형태로 보내줄 수 있도록 하려고 해요.

### doGet, doPost 함수 정의

- python과 Google Apps Script는 서로 http를 통해 연결됩니다.
- 이를 위해 Google Apps Script 내에 `doGet()` 함수와 `doPost()` 함수를 만듭니다.

```javascript
function doGet(e) {
  // Get방식에 대해서 대응하는 함수
  // e: 전달받은 데이터.
  var spreadsheet = SpreadsheetApp.getActive()
  var sheet = spreadsheet.getSheetByName("시트1")

  // 일단은 그냥 [1, 2, 3]과 같은 간단한 데이터를 보낸다고 할게요.
  var returnArr = [1, 2, 3]

  // HtmlService.createHtmlOutput()를 사용해서 보내려는 데이터를 감싸줍니다.
  return HtmlService.createHtmlOutput(JSON.stringify(returnArr))
  //
}

function doPost(e) {
  // post 방식에 대해서 대응하는 방식
  // 일단은 따로 만들지 않았습니다.
}
```

- 그 다음, 배포 > 새 배포 > '웹 앱'을 선택하고 '배포' 버튼을 꾹 눌러 줍니다.
- 그럼 다음과 같은 형태의 URL이 만들어지죠. 권한이 구글 계정에 종속되어 있기 때문에, 다른 사람이 해당 URL에 접속한다고 해서 뭘 할수는 없습니다.

```plaintext
https://script.google.com/macros/s/.......
```

- 그냥 만들어진 URL을 웹 브라우저 주소창에 쳐도 뭐 됩니다. 그럼 일단 제대로 만들어졌는지 확인할 수는 있죠.

### python code 

- 저는 python에서 `requests` 라이브러리를 사용하여, 해당 URL에 접속해서 데이터를 가져와 보겠습니다. 

```python
code...
```

- code 자체는 잘못된 게 없는데, 데이터가 긁어와지지 않습니다.
- 웹 브라우저에서는 되는데, python에서는 안되는 것은 python에서 접속할 때, 얘에게 접근 권한이 없기 때문이죠. 웹 브라우저에서는 이미 Google에 로그인된 상태이기 때문에, 아무 문제없이 해당 URL에 접속할 수 있지만, python에서는 그 부분이 해결되지 않은 것이죠.
- 과거에는 "익명"도 접근할 수 있도록 해준 것 같은데, 현재는 반드시 구글 ID가 있는 사람에게만 허용해주는 것 같아요.

## Issue

- 데이터는 구글 시트에 저장하고, 분석은 python에서 함. 구글 시트의 파일을 다운받아서 그 파일을 분석해도 되기는 하는데, 그보다는 구글 시트를 서버처럼 굴리면서 바로 데이터를 전송해주는 형태로 해주고 싶음. 그게 좀 더 seamless함.
- 그냥 크롬 브라우저를 사용하면 될 줄 알았는데 그렇지 않음.


## 배포 유형 이제

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
