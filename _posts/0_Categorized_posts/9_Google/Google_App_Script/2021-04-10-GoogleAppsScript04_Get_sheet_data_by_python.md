---
title: Google Apps Script - Google Apps Script API 사용하기
category: google
tags: google javascript google_sheet macro GoogleAppsScript GCP 
---

## Google Apps Script - Google Apps Script API 사용하기

- python에서 Google Apps Script에 정의된 함수에 접근하여 사용하는 방법을 정리합니다.
- 좀더 풀어서 말하면 Google Cloud Platform에서 Google Apps Script API를 사용할 수 있도록 정의하고, python에서 이미 Google Apps Script 정의된 함수에 접근하는 것을 해봅니다.

## Google Apps Script - Function 

- Google Apps Script에 다음과 같은 함수가 정의되어 있다고 하겠습니다.
- 아래 함수는 google spreadsheet에 접속하여, `Sheet1`에 `A1`의 값을 업데이트하는 기능을 수행하죠.
- `google_spreadSheet_ID`는 `https://docs.google.com/spreadsheets/d/<google_spreadSheet_ID>/edit#gid=0`에서 참고하면 됩니다.

```js
function set_A1() {
  var spreadsheet = SpreadsheetApp.openById("google_spreadSheet_ID")
  var sheet = spreadsheet.getSheetByName("Sheet1")
  sheet.getRange("A1").setValue("999")
}
```

- 그리고, 위 Google Apps Script의 URL은 보통 다음과 같이 정의되어 있는데요, 아래 `<scriptID>`를 기억해 놓으셔야 합니다.
- 이 `scriptID`는 이후 python에서 해당 Google Apps Script API에 접근할 때 필요하죠.

```plaintext
https://script.google.com/home/projects/<scriptID>/edit
```

## Google Cloud Platform - Google Apps Script API

### Create new Google Cloud Platform project

- 우선 [Google Cloud Platform](https://console.cloud.google.com/home)에 접속해서 새로운 GCP 프로젝트를 만들어줍니다. 기존에 있는 프로젝트에도 상관없습니다.
  - python 코드에서 Google Apps Script API에 접근한다는 것은 Google Apps Script 서버에 요청(request)를 보낸다는 것을 말합니다. 그럼 그 요청(request)를 받아서 응답(response)를 해줄 수 있는 일종의 서버가 존재해야 겠죠. 따라서, GCP에서 우리가 보내는 요청에 응답해 줍니다. 이를 위해 프로젝트를 생성하는 것이죠. 이미 존재하는 프로젝트에 추가할 수도 있을 것 같은데, 연습삼아 새로운 프로젝트를 만들어보도록 합니다. 이름은 뭐 대충 "Quickstart for Google Apps Script"라고 대충 정했습니다 호호.
- 그리고 **"API and Service"** 로 들어갑니다. 
- **"API 및 서비스 사용 설정"** 을 누르고, 우리가 사용하려는 "Google Apps Script"를 검색해서 해당 API를 "사용"으로 변경해줍니다. 네, 말그대로 Google Apps Script API를 사용하겠다는 이야기죠.

### Create Credential 

- 그 다음으로는 인증서(Credential)를 다운받아야 합니다.
- 만약, 모르는 사람이 제 Google Apps Script API에 마음대로 접속해서 데이터를 가져간다거나 하면 안되니까요. 그러니까 일종의 열쇠가 필요한 셈이죠.
- **API and Services**로 들어가서 **"사용자 인증정보"**에 들어갑니다.
- **"사용자 인증정보 만들기"** 버튼을 누르고, **OAuth 클라이언트 ID**를 선택해 줍니다.
- 애플리케이션 유형은 **"데스크톱 앱"**으로 선택합니다. 이름은 뭐 대충 만들어주고요. 저는 "DeskClient1"으로 대충 만들었습니다.
- 사용자 동의 화면을 누르고, 접근 가능한 사용자들을 결정해줍니다. Google Workspace를 사용하는 경우에는 "내부"를 선택해서 현재 조직에 속한 사람들만 접속하도록 할 수 있지만, 저는 Google Workspace를 사용하지 않으므로 "외부"만 선택할 수 있죠.
- 이걸 다 만들고 나서 보면, OAuth 2.0 클라이언트 ID 중에 제가 만든 "DeskClient1"을 다운 받을 수 있습니다. 네, 이 파일이 바로 "열쇠"죠.

## python to Google Apps Script 

- 코드를 다음 3 단계로 나누어 정리하였습니다. 

### Get authorization 

- GCP에 접속하여 권한을 획득하는 부분입니다. 
- 필요한 권한(`SCOPES`)를 정의해주고, OAuth에서 다운 받은 `credential.json` 파일을 사용해야 합니다.
- 코드를 처음 사용하게 되면, `credential.json` 파일을 사용하게 되고 웹브라우저를 통해 권한을 승인해주면, 자동으로 `token.json` 파일이 생성됩니다.
- 그다음부터는 `SCOPES` 등이 변경되지 않는다면 웹브라우저를 통해 매번 권한을 승인해줄 필요없이 그대로 사용할 수 있죠.

```python
from __future__ import print_function
import os.path
from googleapiclient import errors
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials

# script, spreadsheet를 수정하는 권한이 필요한 것을 명시합니다.
SCOPES = [
    'https://www.googleapis.com/auth/script.projects', 
    'https://www.googleapis.com/auth/script.scriptapp', 
    'https://www.googleapis.com/auth/spreadsheets'
]

# 권한 획득 Start ###########################
creds = None
if os.path.exists('token.json'):
    creds = Credentials.from_authorized_user_file('token.json', SCOPES)
# If there are no (valid) credentials available, let the user log in.
if not creds or not creds.valid:
    if creds and creds.expired and creds.refresh_token:
        creds.refresh(Request())
    else:
        flow = InstalledAppFlow.from_client_secrets_file(
            'credentials.json', SCOPES)
        creds = flow.run_local_server(port=0)
    # Save the credentials for the next run
    with open('token.json', 'w') as token:
        token.write(creds.to_json())

service = build('script', 'v1', credentials=creds)
# 권한 획득 End ###########################
```

### Get Proejct Metadata 

- `service.projects().get(scriptId=scriptID).execute()`를 사용해서 해당 script에 대한 기본적인 정보를 가져올 수 있습니다.

```python
# 여기에 Google Apps Script의 ID를 작성해줍니다.
# https://docs.google.com/spreadsheets/d/<google_spreadSheet_ID>/edit#gid=0
scriptID = ""
# Call the Apps Script API
# Create a new project
print("===========================================")
response = service.projects().get(
    scriptId=scriptID
).execute()
print(response)
```

- 실행결과는 다음과 같습니다.

```plaintext
{
    'scriptId': '', 
    'title': '', 
    'createTime': '2021-04-10T09:20:42.249Z', 
    'updateTime': '2021-04-10T09:44:19.341Z', 
    'creator': {
        'domain': 'gmail.com', 
        'email': '', 
        'name': ''
    }, 
    'lastModifyUser': {
        'domain': 'gmail.com', 
        'email': '', 
        'name': ''
    }
}
```

### Get Project Source 

- `service.projects().getContent(scriptId=scriptID).execute()`를 통해 Project에 존재하는 file들과 소스들을 가져옵니다.

```python
# Get content
response = service.projects().getContent(
    scriptId=scriptID
).execute()
print(response)
```

- 다음 결과를 보시면 아시겠지만, 해당 script file에 작성되어 있는 metadata들과 source들을 가져옵니다.
- 몇몇 부분들은 제가 삭제했습니다.

```plaintext
{
    'scriptId': '', 
    'files': [
        {
            'name': 'appsscript', 
            'type': 'JSON', 
            'source': 'raw_source_text', 
            'lastModifyUser': {'domain': 'gmail.com', 'email': '', 'name': ''}, 
            'createTime': '2021-04-10T09:20:42.542Z', 
            'updateTime': '2021-04-10T13:12:14.350Z', 
            'functionSet': {}
        }, 
        {
            'name': 'Code', 
            'type': 'SERVER_JS', 
            'source': 'raw_source_text', 
            'lastModifyUser': {
                'domain': 'gmail.com', 'email': '', 'name': ''
            }, 
            'createTime': '2021-04-10T09:20:42.542Z', 
            'updateTime': '2021-04-10T13:12:14.350Z', 
            'functionSet': {
                'values': [
                    {'name': 'set_A1'}, 
                    {'name': 'myFunction'}]
            }
        }
    ]
}
```

### Run function 

- 아래와 같이 `request_body`를 작성해주고, `service.scripts().run(scriptId=scriptID,body=request_body).execute()`를 실행해줍니다.
- 저의 경우 앱을 개시하지 않고 '테스트상태'로 두었기 때문에 `devMode`를 `True`로 설정하여 넘겨줍니다. 이후 해당 앱을 게시하게 되면 이 부분을 False로 변경하거나 삭제해줍니다(default가 False이기 때문)

```python
# 만약 '사용자 동의화면'에서 해당 앱을 '테스트'로 두었다면 아래에서 devMode를 True로 해두어야 합니다.
# default는 False죠.
request_body = {
    "function": 'set_A1', 
    "parameters": [], 
    "devMode": True
}

response = service.scripts().run(
    scriptId=scriptID,
    body=request_body
).execute()
print(response)
```

- 만약, 해당 앱이 테스트 상태인데, `devMode`를 따로 설정하지 않을 경우 다음과 같은 오류가 발생하곤 합니다.

```plaintext
{\n  "error": {\n    "code": 404,\n    "message": "Requested entity was not found.",\n    "status": "NOT_FOUND"\n  }\n}\n'
```

- `response`는 다음과 같습니다만, 이보다는 엑셀에 들어가서, 제가 원하는 대로 A1에 새로운 값이 업데이트되었는지 확인해보는 것이 좋겠죠.
- 확인해보면 값이 업데이트되어 있습니다 호호.

```plaintext
{'done': True, 'response': {'@type': 'type.googleapis.com/google.apps.script.v1.ExecutionResponse'}}
```

## Wrap-up

- Google Sheet API를 사용하든, Google Script API를 사용하든 어떤 API도 사용하려면 동일하게 OAuth Credential이 필요합니다. 다만, 각 API별로 필요로 하는 범위가 달라질 수 있기 때문에, 범위가 변경되거나 하는 경우에는 `token.json`을 새로 만들어 줘야 하죠.
- 저의 경우 GCP의 "OAuth"를 설정할 때, 앱을 바로 게시하지 않고, "테스트"로 게시해둔 상태였습니다. 그런데, 이렇게 처리할 경우 `scripts().run()`을 실행할 때, 계속 함수가 없다는 결과가 나오더라구요. 그래서 꽤 많은, 대략 5시간 넘는 시간동안 헤매었죠. 결국 다시 Google Apps Script API를 꼼꼼하게 살펴본 뒤에야 `devMode`를 확인했고, 결국은 해결했습니다. 생각해보면 결국 여기저기 블로그에 있는 글들보다도 공식 문서에 있는 내용을 꼼꼼하게 보는 것이 더 도움이 될 때가 많더군요. 그렇습니다 호호.
- 사실 이번 글은 중간에 너무 시간이 납이되어서 썩 마음에 들지는 않습니다만...시간을 너무 낭비해서 꼴도 보기 싫어서 넘어갑니다 하하하. 

## Reference

- [구글 앱스 스크립트 외부에서 실행하기](https://www.44bits.io/ko/post/google-app-script-external-execution-by-ruby)
- [google developers - apps script - quickstart](https://developers.google.com/apps-script/api/quickstart/python)
- [google developers - apps script - api](https://developers.google.com/apps-script/api/reference/rest)
- [Execute Google Apps Script functions or Sheets-Macros programmatically using Python & Apps Script API](https://medium.com/@victor.perez.berruezo/execute-google-apps-script-functions-or-sheets-macros-programmatically-using-python-apps-script-ec8343e29fcd)

## Raw Code 

```python
from __future__ import print_function
import os.path
from googleapiclient import errors
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials

# script, spreadsheet를 수정하는 권한이 필요한 것을 명시합니다.
SCOPES = [
    'https://www.googleapis.com/auth/script.projects', 
    'https://www.googleapis.com/auth/script.scriptapp', 
    'https://www.googleapis.com/auth/spreadsheets'
]

# 권한 획득 Start ###########################
creds = None
if os.path.exists('token.json'):
    creds = Credentials.from_authorized_user_file('token.json', SCOPES)
# If there are no (valid) credentials available, let the user log in.
if not creds or not creds.valid:
    if creds and creds.expired and creds.refresh_token:
        creds.refresh(Request())
    else:
        flow = InstalledAppFlow.from_client_secrets_file(
            'credentials.json', SCOPES)
        creds = flow.run_local_server(port=0)
    # Save the credentials for the next run
    with open('token.json', 'w') as token:
        token.write(creds.to_json())

service = build('script', 'v1', credentials=creds)
# 권한 획득 End ###########################


# 여기에 Google Apps Script의 ID를 작성해줍니다.
# https://docs.google.com/spreadsheets/d/<google_spreadSheet_ID>/edit#gid=0
scriptID = ""
# Call the Apps Script API
# Create a new project
print("===========================================")
response = service.projects().get(
    scriptId=scriptID
).execute()
print(response)


# Get content
response = service.projects().getContent(
    scriptId=scriptID
).execute()
print(response)

# 만약 '사용자 동의화면'에서 해당 앱을 '테스트'로 두었다면 아래에서 devMode를 True로 해두어야 합니다.
# default는 False죠.
request_body = {
    "function": 'set_A1', 
    "parameters": [], 
    "devMode": True
}

response = service.scripts().run(
    scriptId=scriptID,
    body=request_body
).execute()
print(response)
```
