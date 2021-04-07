---
title: GCP - Google Sheet API를 사용하여 python에서 데이터 긁어오기
category: GoogleCloudPlatform
tags: google gcp GoogleSheet sheet python GoogleDrive 
---

## GCP - Google Sheet API를 사용하여 python에서 데이터 긁어오기

- Google Sheet API를 사용하여 python에서 Google Sheet의 데이터를 가져오는 방법을 정리합니다.
- 물론 [gspread](https://gspread.readthedocs.io/en/latest/)를 사용해서 가져올 수도 있고 이 라이브러리가 github에서 Star가 5k가 넘고 보면 해당 라이브러리가 잘 유지되고 있는 것 같기는 하지만, 직접 접근하는 방법을 좀 정리해보고 싶었습니다.
- [developers - google - python - quickstart](https://developers.google.com/sheets/api/quickstart/python)를 참고하여 작성하였습니다.

## GCP - Google Sheet API

### Create new Google Cloud Platform project

- 우선 [Google Cloud Platform](https://console.cloud.google.com/home)에 접속해서 새로운 GCP 프로젝트를 만들어줍니다.
  - python 코드에서 Google Sheet의 데이터를 가져올 수 있도록 한다는 것은 python 코드에서 Google Sheet 데이터를 가지고 있는 서버에 요청(request)를 보낸다는 것을 말합니다. 그럼 그 요청(request)를 받아서 응답(response)를 해줄 수 있는 일종의 서버가 존재해야 겠죠. 따라서, GCP에서 우리가 보내는 요청에 응답해 줍니다. 이를 위해 프로젝트를 생성하는 것이죠. 이미 존재하는 프로젝트에 추가할 수도 있을 것 같은데, 연습삼아 새로운 프로젝트를 만들어보도록 합니다. 이름은 뭐 대충 "Quickstart for Google Sheet"라고 대충 정했습니다 호호.
- 그리고 **"API and Service"** 로 들어갑니다. 
- **"API 및 서비스 사용 설정"** 을 누르고, 우리가 사용하려는 "Google Sheet"를 검색해서 해당 API를 "사용"으로 변경해줍니다. 네, 말그대로 Google Sheet API를 사용하겠다는 이야기죠.

### Create Credential 

- 그 다음으로는 인증서(Credential)를 다운받아야 합니다.
- 만약, 모르는 사람이 제 Google Sheet에 마음대로 접속해서 데이터를 가져간다거나 하면 안되니까요. 그러니까 일종의 열쇠가 필요한 셈이죠.
- **API and Services**로 들어가서 **"사용자 인증정보"**에 들어갑니다.
- **"사용자 인증정보 만들기"** 버튼을 누르고, **OAuth 클라이언트 ID**를 선택해 줍니다.
- 애플리케이션 유형은 **"데스크톱 앱"**으로 선택합니다. 이름은 뭐 대충 만들어주고요. 저는 "DeskClient1"으로 대충 만들었습니다.
- 사용자 동의 화면을 누르고, 접근 가능한 사용자들을 결정해줍니다. Google Workspace를 사용하는 경우에는 "내부"를 선택해서 현재 조직에 속한 사람들만 접속하도록 할 수 있지만, 저는 Google Workspace를 사용하지 않으므로 "외부"만 선택할 수 있죠.
- 이걸 다 만들고 나서 보면, OAuth 2.0 클라이언트 ID 중에 제가 만든 "DeskClient1"을 다운 받을 수 있습니다. 네, 이 파일이 바로 "열쇠"죠.

## Python to Google Sheet API

- 이제 python에서 Google Sheet API를 사용해보겠습니다.
- 아래 command를 사용해서 필요한 python 라이브러리들을 설치합니다.

```bash
pip install --upgrade google-api-python-client google-auth-httplib2 google-auth-oauthlib
```

- 그리고 아까 다운 받은 json 파일을 python code 파일과 같은 경로에 `credentials.json`의 이름으로 저장해줍니다.
- python code는 다음과 같아요. 이 코드는 [Google Sheets - python - quickstart](https://developers.google.com/sheets/api/quickstart/python)에 있는 코드를 가져와서 comment만 더 달았습니다.

```python
# 코드를 구현하기 위해 필요한 라이브러리들입니다.
# 일단은 그대로 복사해서 넣어줍니다.
from __future__ import print_function
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials

# Google Sheet에 대한 권한을 정해주는 부분입니다.
# 아래는 readonly로 설정되어 있죠. 만약, 이후 이 권한이 변경된다면 token.json도 새롭게 변경되어야 합니다.
SCOPES = ['https://www.googleapis.com/auth/spreadsheets.readonly']

# 대상 google spreadsheet의 ID, 시트와 접근 범위를 작성합니다.
# spreadsheet의 ID는 보통 URL에 포함되어 있습니다.
# URL: https://docs.google.com/spreadsheets/d/<SPREADSHEET_ID>
SAMPLE_SPREADSHEET_ID = '...'
# 접근하려는 Sheet와 범위도 같이 정해줍니다.
SAMPLE_RANGE_NAME = 'Sheet1!A1:B4'


def main():
    creds = None
    # 처음 접속할 때는 token.json이 없습니다.
    # 처음에 접속할 때는 이전에 다운 받은 credentials.json 파일을 사용하여 접속하게 되고, 
    # 그 다음 token.json 파일이 자동으로 생성되죠. 
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

    service = build('sheets', 'v4', credentials=creds)

    # Call the Sheets API
    sheet = service.spreadsheets()
    result = sheet.values().get(
        spreadsheetId=SAMPLE_SPREADSHEET_ID,
        range=SAMPLE_RANGE_NAME
    ).execute()

    values = result.get('values', [])
    print(values)  
    # [['A1_value', 'B1_value'], ['A2_value', 'B2_value'], ['A3_value', 'B3_value']]


if __name__ == '__main__':
    main()
```

- 그리고 위 코드를 실행해 보면, 웹브라우저가 실행되면서 구글에 로그인을 하고 접속 권한을 설정해야 합니다.
- 그러고 나면 다음처럼 결과가 잘 나오는 것을 알 수 있죠.

```plaintext
[['A1_value', 'B1_value'], ['A2_value', 'B2_value'], ['A3_value', 'B3_value']]
```

## Wrap-up

- 처음에는 그냥 Google Apps Script를 사용하면서, Apps Script를 사용해서 Google Sheet의 데이터를 python에서 가져올 수 있도록 해주려고 했는데요. 그게 잘 안되서 결국은 Google Sheet API를 사용해서 이런 걸 해봤습니다.
- 근데, 이걸 하고 나니, Google Apps Script를 사용해서도 비슷하게 할 수 있을 것 같네요.

## Reference

- [developers - google - python - quickstart](https://developers.google.com/sheets/api/quickstart/python)
