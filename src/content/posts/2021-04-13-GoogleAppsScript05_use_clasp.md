---
title: "Google Apps Script - clasp를 사용하여 local에서 script 작성하기"
date: 2021-04-13
category: "google"
tags: ["google", "javascript", "terminal", "macro", "GoogleAppsScript", "GCP"]
permalink: "/google/GoogleAppsScript05_use_clasp/"
---

- 지금까지는 google apps script를 사용하기 위해서는 구글 드라이브(혹은 닥스)에 접속해서 Google Apps Script를 생성하고 브라우저에 수정하는 일들을 했습니다. 코드가 작을 때는 이렇게 해도 아무 문제가 없습니다만, 코드가 길어지거나 하면, local에서 작업하고 싶을 때가 있습니다. git을 쓰기도 하고 뭐 이런저런 이유 때문이죠.
- 본 글에서는 clasp라는 툴을 사용하여 local에서 Google Apps Script를 사용하는 방법을 정리합니다. [github - google - clasp](https://github.com/google/clasp)를 참고했습니다.

## Clasp - Command Line Apps Script Projects

- [clasp](https://github.com/google/clasp)는 "Command Line Apps Script Projects(CLASP)"를 말합니다.
- npm을 사용하여 설치해보겠습니다. sudo를 사용하지 않으니 설치가 안되어서, sudo를 붙여 줍니다. 
- 맥에서는 언젠가부터 보안이 강화되어서, 외부 패키지를 설치하는 대부분의 경우 sudo를 붙이지 않으면, 설치가 되지 않습니다.

```bash
$ sudo npm install -g @google/clasp
Password:
/usr/local/bin/clasp -> /usr/local/lib/node_modules/@google/clasp/src/index.js
npm WARN inquirer-autocomplete-prompt@1.0.1 requires a peer of inquirer@^5.0.0 || ^6.0.0 but none is installed. You must install peer dependencies yourself.

+ @google/clasp@2.3.0
added 167 packages from 96 contributors in 7.985s


   ╭───────────────────────────────────────────────────────────────╮
   │                                                               │
   │      New major version of npm available! 6.14.11 → 7.9.0      │
   │   Changelog: https://github.com/npm/cli/releases/tag/v7.9.0   │
   │               Run npm install -g npm to update!               │
   │                                                               │
   ╰───────────────────────────────────────────────────────────────╯
```

- 그리고 [google - script - usersettings](https://script.google.com/home/usersettings)에서 "사용가능(ON)"으로 설정해줍니다.

### clasp - usage

- `clasp --help`를 통해 어떤 짓들을 할 수 있는지 봅니다.
- 새로운 script를 만들 수도 있고, 가져올 수도 있고(pull), 집어넣을 수도 있고(push), 배치(delopy), 현재 사용중인 project들 리스트업(list), 실행(run) 등을 할 수 있습니다. 사실뭐, 웹브라우저에서 할 수 있는 것들을 다 할 수 있다, 라고 보면 되겠네요.

```bash
$ clasp -help
Usage: clasp <command> [options]

clasp - The Apps Script CLI

Options:
  -v, --version                               
  -h, --help                                  output usage information

Commands:
  login [options]                             Log in to script.google.com
  logout                                      Log out
  create [options]                            Create a script
  clone [options] [scriptId] [versionNumber]  Clone a project
  pull [options]                              Fetch a remote project
  push [options]                              Update the remote project
  status [options]                            Lists files that will be pushed by clasp
  open [options] [scriptId]                   Open a script
  deployments                                 List deployment ids of a script
  deploy [options]                            Deploy a project
  undeploy [options] [deploymentId]           Undeploy a deployment of a project
  version [description]                       Creates an immutable version of the script
  versions                                    List versions of a script
  list                                        List App Scripts projects
  logs [options]                              Shows the StackDriver logs
  run [options] [functionName]                Run a function in your Apps Scripts project
  apis [options]                              List, enable, or disable APIs
    list
    enable <api>
    disable <api>
  help                                        Display help
  setting|settings [settingKey] [newValue]    Update <settingKey> in .clasp.json
  *                                           Any other command is not supported
```

### clasp - login

- 우선 `login`을 합니다. shell에서 다음 커맨드를 사용하면, 웹브라우저를 통해 구글에 로그인이 되고 권한을 줄거냐고 묻습니다. 승인해줍니다.

```bash 
$ clasp login
Logging in globally...
🔑 Authorize clasp by visiting this url:
...
Authorization successful.

Default credentials saved to: ~/.clasprc.json (/Users/user_name/.clasprc.json).
```

### clasp - create new document

- `clasp create`를 사용하여, 새로운 script를 만들어 줍니다.
- 중간에 어떤 script를 만들어 줄 것인지 선택해 줘야 하는데 저는 "standalone"을 선택해줬습니다.

```bash
$ clasp create --title "clasp_test"
? Create which script? standalone
Created new standalone script: https://script.google.com/d/script_id/edit
Warning: files in subfolder are not accounted for unless you set a '.claspignore' file.
Cloned 1 file.
└─ appsscript.json
$ ls
appsscript.json
```

### clasp - open existing document

- 아래와 같이 `clasp open <script_ID>`를 사용하면 웹브라우저를 통해 해당 스크립트를 열 수 있습니다.

```bash
$ clasp open <script_ID>
Opening script: https://script.google.com/d/<script_ID>/edit
```

### clasp - pull and push

- `clasp pull`을 사용해서 cloud에 존재하는 apps script project를 가져올 수 있고,
- `clasp push`를 사용해서 local에 존재하는 apps script project를 cloud로 보낼 수도 있습니다.

```bash
$ clasp pull
Warning: files in subfolder are not accounted for unless you set a '.claspignore' file.
Cloned 2 files.
└─ a.js
└─ appsscript.json

$ clasp push
└─ a.js
└─ appsscript.json
Pushed 2 files.
```

## clasp - version, version, deploy

- `clasp status`를 사용하여 현재 관리되고 있는 file들과 관리되고 있지 않은 파일들을 확인할 수 있고
- `clasp versions`를 사용하여 현재 존재하는 version 들을 확인할 수 있고
- `clasp version "version_name"`을 사용해서 version을 만들어줄 수 있고,
- `clasp delopy version_name`를 사용하여 배포도 해줄 수 있습니다.

```bash
$ clasp status
Not ignored files:
└─ a.js
└─ appsscript.json

Ignored files:
└─ .clasp.json

$ clasp versions
No deployed versions of script.

$ clasp version "first_version"
Created version 1.
$ clasp deploy "first_version"
Created version 2.
...
```

### clasp - run "function_name"

- `clasp run function_name`을 사용하면, 해당 apps script project에 존재하는 function을 실행해줄 수도 있습니다.
- 그러나, 실제로 실행해보면 되지 않죠. 개발 모드 때문에 발생한 문제도 아닌 것으로 보입니다.

```bash
$ clasp run "set_A1"
Running in dev mode.
Could not read API credentials. Are you logged in locally?

$ clasp run "set_A1" --nondev true
Could not read API credentials. Are you logged in locally?
```

- [github - google - clasp - run](https://github.com/google/clasp/blob/master/docs/run.md)에서 하라는대로 해주면 됩니다.
- 하나씩 정리하자면 다음과 같습니다.
- GCP 의 project_ID를 가져와서 `clasp setting projectId <project_ID>`로 등록해줍니다. 

```bash
$ clasp setting projectId project_ID
Updated "projectId": "" → "project_ID"
```

- 이 작업은 그냥 `.clasp.json` 파일에 `projectId`를 추가해주는 것과 동일합니다.

```json
{
    "scriptId":"",
    "projectId":"projectID"
}
```

- 이제 `clasp open`을 사용해서 앱 스크립트 프로젝트로 간 다음, 설정에 GCP project의 number를 작성해줍니다. 이 작업은 Google Apps Script를 GCP와 연결해주는 작업이죠.
- 그 다음 `clasp open --creds`을 통해 OAuth 인증으로 들어가서, Desktop App에 관한 credential.json을 다운받습니다. 얘를 다운받고 이름을 `creds.json`으로 바꿔줄게요.
- 그리고 다시 실행해 봅니다. 저는 현재 "테스트모드"이기 때문에, nondev를 true로 설정하고 실행하면, 해당 함수가 없거나, 배포(deploy)되지 않은 것으로 나옵니다.

```bash
$ clasp run "set_A1" --nondev true
Script API executable not published/deployed.

$ clasp run "set_A1"
Running in dev mode.
Exception: ScriptError Exception: You do not have permission to call SpreadsheetApp.openById. Required permissions: https://www.googleapis.com/auth/spreadsheets [ { function: 'set_A1', lineNumber: 8 } ]
```

- 하지만, 에러가 또 발생하죠. 이번 에러는 권한이 없다는 것이죠. 제가 호출하는 함수인 "set_A1"이라는 함수는 특정 구글 시트에 접근하여, 해당 시트의 값을 변경합니다. 따라서, 구글 시트를 변경할 수 있는 권한이 필요한 셈이죠. 그런데, 저는 이를 아직 부여하지 않은 상황입니다.
- 따라서, appsscript.json 파일에 들어가서 다음과 같이 아래 부분에 `"oauthScopes`에 시트를 수정할 수 있는 권한을 추가해줍니다.

```json
{
  "timeZone": "America/New_York",
  "dependencies": {
  },
  "exceptionLogging": "STACKDRIVER",
  "runtimeVersion": "V8", 
  "oauthScopes": [
    "https://www.googleapis.com/auth/spreadsheets"
  ], 
  "executionApi": {
    "access": "ANYONE"
  }
}
```

- 권한을 변경했으니, 로그인부터 다시 해주어야 합니다.
- 그리고 다시 실행해보면 잘 실행되는 것을 알 수 있죠. 호호호.

```bash
$ clasp login --creds creds.json
Warning: You seem to already be logged in *locally*. You have a ./.clasprc.json
Logging in locally...

Authorizing with the following scopes:
https://www.googleapis.com/auth/spreadsheets
https://www.googleapis.com/auth/script.webapp.deploy

  NOTE: The full list of scopes your project may need can be found at script.google.com under:
  File > Project Properties > Scopes
  
Using credentials located here:
...

🔑 Authorize clasp by visiting this url:
...
Authorization successful.

Local credentials saved to: ./.clasprc.json.
...

$ clasp run "set_A1"
Running in dev mode.
No response.
```

## Wrap-up

- clasp읙 경우도 결국 외부에서 google apss script API를 사용하기 위해서는 GCP에 등록해야 하고 OAuth로 인증받은 `creds.json`파일들을 사용해야 하고, Google 의 다른 API를 사용하기 위해서는 권한을 할당받는 것부터 싹 다 다시 해줘야 합니다 하하하. 이제 몇 번 GCP를 사용하다보니 꽤 익숙하네요.
- 조금 하다보니, 이제는 꽤 익숙해져서, clasp를 사용해서 로컬에서(정확히는 VScode를 사용해서) 작업하고 필요할때마다 push하고 실행하는 식으로 처리해주는 것도 꽤 유용할 것 같습니다. 호호.

## Reference

- [codelabs - developers - google - clasp](https://codelabs.developers.google.com/codelabs/clasp/#0)
- [github - google - clasp](https://github.com/google/clasp)
- [developers - google - apps script - clasp guide](https://developers.google.com/apps-script/guides/clasp)