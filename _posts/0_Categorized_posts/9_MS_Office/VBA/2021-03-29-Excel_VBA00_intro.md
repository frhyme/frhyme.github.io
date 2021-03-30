---
title: MS Office - Visual Basic for Application(VBA) - Intro
category: MS_Office
tags: MS_Office excel vba macro macOS basic
---

## MS Office - Visual Basic for Application(VBA)

- 최근에는 VBA를 사용해서 엑셀 내 데이터들을 효과적으로 관리하려는 일을 하고 있습니다.
- 대학교 4학년 즈음에 수업에서 VBA를 잠시 써본 적이 있는데요, 이전에 배웠던 언어들인 C, C++, Java등과는 그 문법 등이 미묘하게 달라서 적응이 잘 안되었습니다. 그 이후에는 python을 사용하게 되면 더욱 VBA의 필요성이 없어졌죠.
- 지금도 같은 기능이라면 python으로 개발하는 것이 훨씬 효율적이라고 생각하지만, VBA의 강점이라면 다른 사람의 컴퓨터에 개발환경을 구축할 필요가 없다는 것이겠죠. 엑셀은 모든 직장인들의 기본 툴이라서 설치되어 있지 않은 컴퓨터가 없다고 봅니다. 이는 다시 말해, 내가 엑셀에 매크로를 구현한 다음 다른 사람의 컴퓨터에 파일로 그대로 보내도 알아서 잘 작동한다는 것이죠.
- 반면, python으로 개발을 한 다음 다른 사람의 컴퓨터로 보내게 된다면, 일단 상대방의 컴퓨터에 python이 설치되어 있어야 하고, 관련 라이브러리들이 다 설치되어 있어야 겠죠. 특히 상대방이 비 개발자라면, 이 번거로움은 좀 더 커지게 됩니다. 단지 이 이유 때문이라도 엑셀의 VBA는 경우에 따라 꽤 유용할 수 있겠다, 라는 생각이 들더군요.
- 다만, 여전히 VBA 자체는 약간 다른 언어들과 다른 점들이 있습니다. 익숙하지도 않고요. 그래서 조금씩 공부하면서 배운 내용들을 여기에 정리해보려고 합니다.
- 그리고 본 내용은 모두 macOS에서 구현됩니다.

## Visual Basic? 

- Visual Basic은 Basic이라는 프로그래밍 언어에서 영향을 받은 언어인데요, 현재의 MS-Office에서 사용하는 Visual Basic은 .NET용입니다. 과거에 쓰던 버전은 6.0이구요. 

## Excel VBA for macOS

- macOS에서 VBA를 사용하기 위해서는 우선 "Excel 기본 설정 > 보기 > 개발도구 탭"을 활성화해줍니다.

### 너무 느리다

- 뭐 좀 해보려고 했더니 역시 macOS에서 엑셀, 특히 VBA 작성은 심각하게 느려서 못해먹겠네요. 
- VBA를 사용할 때의 가장 큰 단점은 엑셀에서 VBA를 작성하려고 할 때, 편집기가 매우 구리기 때문입니다. 이는 윈도우즈 환경에서도 꽤나 유효하나, 맥북에서는 그 정도가 심각합니다. VBA를 작성할 때 속도가 심각할 정도로 느립니다. 다크모드가 안된다거나 하는 건 덤으로 빡치죠.

### XVBA 

- 이를 회피하려고, [XVBA](https://marketplace.visualstudio.com/items?itemName=local-smart.excel-live-server)라고 하는 VS code plugin도 다운받아 설치해봤습니다.
- 이 아이는 VScode 내에 프로젝트를 만들어두고 내부에서 excel, vba 등의 파일관리를 한번에 할 수 있도록 해주는 아이죠. [Excel VBA Project in VSCode with XVBA Extension - First Steps](https://www.youtube.com/watch?v=ZjZ1lgzsNXE)이라는 유튜브 영상도 있어서 따라해보았는데, 맥이어서 그런지 몰라도 안되는 건 마찬가지였습니다.

## Wrap-up

- 일단은 excel에서 vba를 직접 편집하는 것은 너무 느려서, 피하기로 했습니다. 제가 생각하고 있는 향후 개선 방안은 다음과 같습니다.
  1. VScode 내에서 VBA 를 작성한 다음 복사해서 excel에 집어넣기: VScode에서 VBA 작성 특히 intellisense 등을 지원하는 플러그인 등이 있다면 특히 좋을 것 같아요.
  2. Visual Studio 등 Visual Basic .Net 전용 IDE 사용하기.
- 둘 중 어떤 것이 가능할지 혹은 둘다 안될지도 모르겠지만, 일단 해보기로 합니다 호호.
