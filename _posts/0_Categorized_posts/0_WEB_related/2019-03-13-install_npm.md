---
title: npm을 설치합니다. 
category: others
tags: npm nodejs web
---

## 왜 갑자기 npm인가. 

- 최근 포스트들을 보시면 아시겠지만, 저는 요즘 일종의 웹서비스를 만들고 있습니다. 비교적 단기간에 필요한 기능들을 만들다보니, 아무래도 제가 직접 코딩을 하기보다는 기존에 있는 것들을 가져와서 연결해서 그럴싸하게 만드는 작업들을 많이 하고 있어요. 
- 아무튼, 그 과정에서 제가 사용하고 있는 라이브러리들은 대략 다음과 같습니다. 
    - chart.js
    - d3.js
    - datatable
    - bootstrap
    - jquery 
- 아무튼 이 과정에서, 전체를 CDN을 통해서 다운받다보니, 웹페이지가 렌더링될때, 특히 chart를 그릴때 애니메이션이 툭툭 끊어지는 느낌이 들어요. 그래서 앞서 말한 것들을 내부 프로젝트 폴더에 설치해서 진행하는 것이 훨씬 수월할 것 같았습니다. 
- 그러한 이유로, 찾다보니, 파일을 통째로 다운받은 다음 넣는 것보다, `npm`이라는 패키지 매니저를 사용해서 설치하는 경우가 많은 것 같았습니다. 추가로 `bower`라는 것도 있기는 하던데 `bower`를 설치하려고 해도 결국 `npm`이 있어야 하더라고요.
- 그래서!, 그냥 npm을 깔아보기로 했습니다. 뭐 나중에 nodejs도 사용할 일이 생기지 않겠어요? 

## npm. 

- 영문 위키피디아에는 다음과 같이 설명되어 있습니다. 

> npm (short for Node.js package manager) is a package manager for the JavaScript programming language. It is the default package manager for the JavaScript runtime environment Node.js. It consists of a command line client, also called npm, and an online database of public and paid-for private packages, called the npm registry. 

- nodejs의 기본 패키지 관리자(뭐, python의 pip 같은것이겠죠)이고, 커맨드라인에서 돌아가고, 돈을 내야 하는 패키지, 퍼블릭 패키지 모두 관리할 수 있다. 뭐 그렇게 되어 있네요. 
- 대충 뭐라는 건 알았으니, 설치부터 합시다. npm만 따로 설치할수는 없고, nodejs를 설치하면 npm도 함께 설치할 수 있는 것 같아요. 
    - 아래처럼 설치하고 나서 제대로 깔렸는데 버전을 확인해봅시다.

```bash
brew install node
node -v
npm -v
```

- 이제 아무거나 깔아봅시다. 

```bash
npm install chart.js --save
```

- 흠...깔았는데, 여기서 발생하는 문제가 제가 원하는 것만 설치되는 것이 아니라 `chart.js` 프로젝트의 모든 파일과 폴더가 다 다운받아지는군요 흠....
- 저는 일단 필요한 부분만 남기고 모두 제외했습니다. 그리고 모두 `static`안으로 집어넣었구요. 

## 충분히 빠르지 않다!

- 음, 사실 저는 웹에서 CDN을 통해서 다운받는 것보다, 제 서버에 해당 리소스가 있는게 더 빠르지 않을까? 생각했는데, 조금더 생각해보니 이게 바보같은 생각입니다. 
- 웹페이지는 사용자, 즉 클라이언트 레벨에서 그려지는 것이고, 이 때 필요한 함수나 기타 라이브러리는 사용자의 컴퓨터로 다이렉트로 꽂혀야 하죠. 
- 만약, 제 서버에 관련 파일들이 저장되어 있다면 제 서버에서 클라이언트들로 일일히 소스를 보내야 하는 것이고, 반대로 CDN으로 지정되어 있으면 클라이언트의 컴퓨터에서 다이렉트로 가장 빠른 곳에서 다운받게 되는 것이죠. 즉, 그냥 CDN을 이용하는 것이 더 빠르다는 교훈을 얻었습니다. 하하하하.

## wrap-up

- 조금만 더 생각해보면 알수 있는 것이었는데, 너무 영혼없이 했나봅니다.
- 캐쉬를 저장하더라도, 여전히 chart.js 를 이용한 애니메이션이 늦게 뜨는 문제는 있습니다만, 이는 나중에 처리하도록 하겠습니다. 
- 나중에 모두 정리한다음 한번에 웹사이트 최적화를 진행하는 것이 좋을 것 같아요. 