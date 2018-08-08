---
title: python에서 구글 sheet 읽기 
category: python-lib
tags: python google excel python-lib sheet spread-sheet google-drive gspread
---

## why read google sheet 

- 분석해야 하는 데이터가 구글 시트에 있습니다. 물론 구글 시트에 있는 데이터를 csv로 다운받아서 분석해도 되기는 하는데, 그보다는 가능하다면, 구글에서 바로 긁어와서 처리하고 싶었습니다. 
- 사실, 이게 더 번거로워지는 일일 수도 있긴 한데, 저는 하나의 파일이 복제되어 여러 곳에 산재되는 것을 원하지 않아요. 
- 구글 시트에 있는 파일이 raw file인데(음 일종의 DB라고 생각해도 되죠), 여기서 데이터를 가져와서 바로 처리하고, 결과를 내는 것이 훨씬 깔끔하지, 중간에 부분파일(excel_1이라고 합시다)을 만들면 이 파일은 시간이 지날 수록 raw_file과의 차이가 발생하게 되니까요.
- 데이터 업데이트는 계속 구글 시트에 진행되기 때문에, 중간에 부산물인 다른 파일을 만들 필요가 없는 것 같아요. 그래서 그냥 구글 시트와 바로 연동되는 식으로 코딩해버리는 것이 필요할 것 같아요. 

## gspread

- 늘 그렇지만, 제가 필요로 하는 것들은 이미 어딘가에 잘 구현되어 있습니다. 하하하하
- [gspread](https://github.com/burnash/gspread)라고 파이썬에서 google sheet에 접근하는 라이브러리가 있습니다. github에서 star의 수가 3410개가 되므로 나름 좋은 라이브러리가 아닌가....하고 생각해봅니다. 

- 일단 설치합니다.
    - 밑에 있는 다른 것들은 구글 시트 인증? 뭐 그런거랑 연결된 부분인데 이후에 어차피 설치해야 하니 다 설치해줍니다. 

```
pip install gspread
pip install --upgrade oauth2client
pip install PyOpenSSL
```

## OAuth Credential 

- gspread를 사용하려면 구글 시트에 대한 접근권한을 얻어야 합니다. 
- 자세한 내용은 일단 [gspread](http://gspread.readthedocs.io/en/latest/oauth2.html) 에서 아실 수 있긴 한데요 간단히 설며하자면

- Service Account Key를 획득하시면
- json 파일이 다운받아집니다. 
- json 파일을 열어보시면 client e-mail이라고 적혀 있는 부분이 있는데, 
- 읽으려고 하는 google sheet에서 해당 메일에 접근권한을 줘야 합니다(시트에서 공유같은걸 눌러서 접근권한을 주면 되요)

- 단, 가끔 Google sheet drive api가 막혀 있는 경우가 있는데, 그럴 경우에는 [구글 드라이브 콘솔](https://console.cloud.google.com/?_ga=2.40775202.-1060959523.1440592789&pli=1)에서 해당 api 를 enable해주셔야 합니다. 

## do it.

- 자 이제 사용해봅시다. 

- 앞서 다운받은 `json`파일을 읽어서 `credentials` 객체를 만들어주고 

```python
## credentail init
from oauth2client.service_account import ServiceAccountCredentials
scope = ['https://spreadsheets.google.com/feeds',
         'https://www.googleapis.com/auth/drive']
credentials = ServiceAccountCredentials.from_json_keyfile_name('/Users/frhyme/Downloads/My Project-6f3701259a8e.json', scope)
```

- 이 객체를 `gspread`에 넘겨주고 인증합니다. 
- 이후에 해당 파일에서 시트를 읽어줍니다. 
    - 여기서 에러가 발생한다면, 에러 메세지에 포함된 uri에 일단 들어가보시기 바랍니다. 
    - 아마도 해당 uri가 제대로 안 읽힐텐데, 그 말은 이전에 뭔가 설치되지 않은 부분이 있다는 이야기입니다 

```python
## authorize
import gspread
gc = gspread.authorize(credentials).open("!individual_meet_report")
## sheet file 이름을 넘겨주고 읽습니다. 
```

## using gspread

- 이제 sheet를 잘 읽었으니까 내부에 있는 값들을 잘 읽어봅시다. 
- row, column은 다음의 방식으로 읽습니다. 이것만 알면 되죠 뭐. 만약 시트의 값을 바꾸거나 하고싶으시면 [gspread](https://github.com/burnash/gspread) 여기의 내용을 참고하시면 좋습니다. 

```python
wks = gc.get_worksheet(0)

gc.get_worksheet(-1)## integer position으로 접근 
gc.worksheet('text') ## sheet name으로 접근 

## get row values 
## 0 이 아니라 1부터 시작하는 것을 유의할 것 
for i in range(1, 3):
    row = wks.row_values(i)

## get column values 
## 마찬가지로 1부터 시작함 
for i in range(1, 2):
    col = wks.col_values(i)[:10]
    print(col)
## 각 row를 리스트로 다시 이를 리스트로 만들어서 리턴 
wks.get_all_values()
```

## reference

- [gspread](https://github.com/burnash/gspread)

## raw code 

```python
## credentail init
from oauth2client.service_account import ServiceAccountCredentials
scope = ['https://spreadsheets.google.com/feeds',
         'https://www.googleapis.com/auth/drive']
credentials = ServiceAccountCredentials.from_json_keyfile_name('/Users/frhyme/Downloads/My Project-6f3701259a8e.json', scope)

## authorize
import gspread
gc = gspread.authorize(credentials)
## sheet file 이름을 넘겨주고 읽습니다. 
wks = gc.open("!individual_meet_report").get_worksheet(0)

## get row values 
## 0 이 아니라 1부터 시작하는 것을 유의할 것 
for i in range(1, 3):
    row = wks.row_values(i)

## get column values 
## 마찬가지로 1부터 시작함 
for i in range(1, 2):
    col = wks.col_values(i)[:10]
    print(col)

```