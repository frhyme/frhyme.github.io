---
title: 맥에서 파워포인트 그림 고화질로 저장하기
category: others
tags: powerpoint mac picture high-resolution
---

## intro

- 저는 대부분의 작업을 맥에서 진행합니다. 다른 건 딱히 불편함을 겪지 못하는데, 논문 작업을 할 때는 불편함을 겪는 일이 많습니다. 
- 특히, 그림 작업은 구글 슬라이드에서 진행하는데, 구글 슬라이드가 그림을 파워포인트처럼 그림을 예쁘게 그려줘서 큰 문제는 없습니다만, 다른 파일로 옮길 때 문제가 발생합니다. 
  - 예를 들어서 구글 슬라이드에서 예쁘게 그린 그림을 구글 닥스로 옮기면 그림이 제대로 안 옮겨지고 텍스트만 옮겨진다거나
  - 그러므로 구글 슬라이드에서 개체를 그림으로 저장하고 싶은데, 여기서는 그림으로 저장하는 기능이 없습니다.... 
- 따라서, 이를 해결하려면 
  - 구글 슬라이드에서 파워포인트로 파일을 변환해서 다운받은 다음
  - 맥에서 파워포인트 파일을 실행하고 원하는 개체를 선택한 다음
  - 그림 저장을 눌러야합니다. 
- 단, 파워포인트는 원래 개체를 그림으로 저장할 때의 dpi가 낮은 값으로 고정되어 있어서 그림의 dpi가 매우 낮습니다. 논문에 집어넣기에는 매우 형편없죠. 

- 윈도우로 작업할 때는 레지스트리 설정을 하면 되었었는데, 맥에서는 어떻게 해야 할지 답답하죠. 

## how to solve it

- 제가 찾은 방법은 아니고요, [이 블로그에 작성된 방법입니다](https://m.blog.naver.com/PostView.nhn?blogId=l3i3m3&logNo=220791456018&proxyReferer=https%3A%2F%2Fwww.google.com%2F)

- 뭔가 정식적인 방법이라기 보다는 약간 특이한 방식입니다만. 
  1. 구글 슬라이드에서 해당 파일을 파워포인트 파일로 다운받습니다. 
  2. 파워포인트 파일로 다운 받은 해당 개체를 선택하고 "복사"합니다. 
  3. 복사하면, 해당 파일이 클립보드에 넘어가 있습니다. 
  4. 맥의 이미지 프로그램, Preview(미리 보기)를 열고 "클립보드로부터 신규"라는 기능을 선택합니다. 
  5. 그 다음 해당 파일을 jpg로 저장하는데 이 때 dpi값을 필요한 만큼 저장합니다.
- 이렇게 하면 원하는 정도로 처리할 수 있습니다. 

## solve it better? 

- 하지만, 매 그림마다 이렇게 저장하는 게 정말 귀찮고 이상하다는 생각이 듭니다. 그래서 더 개선할 수 있는 방법은 없는지 찾아보고 있습니다. 

### 구글 슬라이드에서 바로 클립보드로 저장하는 것은?? 

- 이유는 모르겠지만, 이렇게 할 경우에는 프리뷰에서 클립보드에 저장된 내용을 제대로 읽어오지 못합니다. 
  - 잘 몰라도, 구글 슬라이드는 웹에서 구현되는 프로그램이므로 로컬의 클립보드에 값이 저장되어 있는 것이 아니라, 웹의 클립보드에 저장되어 있....아니 이것도 이상하군요. 웹의 클립보드와 로컬의 클립보드는 구분되어 있지 않습니다. 웹의 아무 이미지나 복사한 다음 프리뷰에서 읽어올 수 있으니까요. 
  - 그렇다면, 오히려 구글 슬라이드에서 그린 개체를 복사했을 때 그 개체는 이미지가 아닐 가능성이 큽니다. 앞에서 말한바와 같이 구글 슬라이드애서 그림을 복사해서 어떤 문서프로그램이든 붙여넣기를 하면, 텍스트만 복사되는 일이 많으니까요. 
  - 이는 결국 구글 슬라이드에서 복사하면 다른 개체들(직사각형, 원, 화살표 등)은 복사하지 못한다는 말이 되는군요. 

### 구글 슬라이드에서 바로 고화질의 그림으로 저장하는 것은??

- 구글 슬라이드에서 슬라이드를 바로 png등의 파일로 다운받을 수 있습니다. 
  - 그러나, 구글 슬라이드에서 다운받은 png 파일의 dpi는 매우 낮습니다. 
  - 다만 pdf로 다운받으면 고화질의 파일이 잘 다운받아집니다.... 
- [제가 던진 질문과 매우 유사한 질문이 이미 여기에 있습니다](https://productforums.google.com/forum/#!topic/docs/kbaWvjEK5mc;context-place=forum/docs). 해결되었는지 유무는 모르겠네요. 흠. 
- [그래서 스택오버플로우에 직접 질문을 올렸습니다.](https://stackoverflow.com/questions/54285308/is-it-possible-to-save-drawing-which-is-drawed-in-google-slides-with-high-dpi?noredirect=1#comment95392851_54285308)
  - google script를 이용하면 이 부분을 쉽게 할 수 있을 것이라고 말씀해주시는데, 아직은 좀 제가 이해가 부족한 것 같다는 생각이 듭니다. 결국 코딩을 해서 해야 하는데 이렇게 하면 더 나아질까 싶은 마음도 좀 있구요. 
- 반대로, 구글 슬라이드의 페이지 설정 부분에서 값을 아주 높게 올려버린 다음 그림을 그리고 다시 그 슬라이드를 다운받으면 고화질의 그림으로 저장되기는 합니다.
  - 그러나, 이 경우에는 텍스트의 크기를 하나하나 다 수정해주어야 하고, 선 굵기 등도 모두 손봐줘야 합니다. 더 귀찮을 일이 될 수도 있는 것이죠. 

## 결론

- 일단은, 다른 방법이 없는 것 같습니다. 직접 Google slide api를 사용해서 코딩하는 방법이 있을 수는 있지만, 이건 제 생각에 그다지 의미있는 작업이 될 것 같지는 않습니다. 
  - 물론, 스크립트를 하나 만들어놓고, 구글 슬라이드 url을 넣고 모든 그림을 다 만들어주는 식으로 한다면, 좋을 수도 있습니다만, 그건 제가 나중에 직접 한번 해보도록 하겠습니다. 
- 아무튼 결론적으로 저는 1) 그림을 구글 슬라이드에서 그리고, 2) 파워포인트로 다운받은 다음, 3) 복사하고 4) 프리뷰에서 고화질로 내보내는 형식으로 하려고 합니다. 이게 그나마 가성비가 맞는 일인 것 같네요.
